#!/usr/bin/env python3
"""
Vault Analyzer - Obsidian Vault Knowledge Management
Scans, categorizes, and provides statistics for Obsidian vault contents

Part of Technology Consultancy Agency
"""

import os
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class VaultAnalyzer:
    """Analyzes Obsidian vault structure and content"""

    def __init__(self, vault_path: str = None):
        # Auto-detect vault path based on environment
        if vault_path is None:
            # Try local path first
            local_path = Path("~/Documents/Obsidian Vault/10-knowledge").expanduser()
            # Try repo-embedded path (for cloud deployment)
            repo_path = Path("obsidian_vault")

            if local_path.exists():
                self.vault_path = local_path
            elif repo_path.exists():
                self.vault_path = repo_path
            else:
                # Default to repo path (will create if needed)
                self.vault_path = repo_path
        else:
            self.vault_path = Path(vault_path).expanduser()

        logger.info(f"VaultAnalyzer initialized for: {self.vault_path}")

    def extract_frontmatter(self, content: str) -> Dict[str, Any]:
        """
        Extract YAML frontmatter from markdown content

        Returns dict with frontmatter fields, or empty dict if no frontmatter
        """
        frontmatter = {}

        # Check for YAML frontmatter (starts and ends with ---)
        if not content.startswith('---'):
            return frontmatter

        try:
            # Find second --- marker
            end_marker = content.find('---', 3)
            if end_marker == -1:
                return frontmatter

            # Extract frontmatter section
            yaml_content = content[3:end_marker].strip()

            # Parse line by line (simple parser, not full YAML)
            for line in yaml_content.split('\n'):
                line = line.strip()
                if ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip()

                    # Handle lists (tags: [tag1, tag2, tag3])
                    if value.startswith('[') and value.endswith(']'):
                        value = [v.strip() for v in value[1:-1].split(',')]

                    # Convert numeric values
                    elif value.isdigit():
                        value = int(value)

                    frontmatter[key] = value

            return frontmatter

        except Exception as e:
            logger.warning(f"Failed to parse frontmatter: {e}")
            return {}

    def categorize_note(self, frontmatter: Dict[str, Any], filename: str) -> str:
        """
        Determine note category based on frontmatter and filename

        Categories: repository, tool, framework, analysis, index, uncategorized
        """
        # Check explicit type field
        if 'type' in frontmatter:
            return frontmatter['type'].lower()

        # Check tags
        if 'tags' in frontmatter:
            tags = frontmatter['tags']
            if isinstance(tags, str):
                tags = [tags]

            for tag in tags:
                tag_lower = tag.lower()
                if 'repository' in tag_lower or 'repo' in tag_lower:
                    return 'repository'
                elif 'tool' in tag_lower:
                    return 'tool'
                elif 'framework' in tag_lower:
                    return 'framework'
                elif 'analysis' in tag_lower:
                    return 'analysis'

        # Check filename patterns
        filename_lower = filename.lower()
        if 'index' in filename_lower:
            return 'index'
        elif filename.endswith('-analysis.md'):
            return 'analysis'

        return 'uncategorized'

    def scan_vault(self) -> Dict[str, Any]:
        """
        Scan entire vault and return categorized structure

        Returns:
            {
                'notes': [{file, title, category, frontmatter, modified}, ...],
                'categories': {category: count, ...},
                'total_notes': int,
                'last_scan': timestamp
            }
        """
        logger.info(f"Scanning vault: {self.vault_path}")

        if not self.vault_path.exists():
            logger.error(f"Vault path does not exist: {self.vault_path}")
            return {
                'notes': [],
                'categories': {},
                'total_notes': 0,
                'last_scan': datetime.now().isoformat(),
                'error': 'Vault path not found'
            }

        notes = []
        categories = {}

        # Scan all .md files
        for md_file in self.vault_path.rglob('*.md'):
            try:
                content = md_file.read_text(encoding='utf-8')
                frontmatter = self.extract_frontmatter(content)
                category = self.categorize_note(frontmatter, md_file.name)

                # Get file stats
                stat = md_file.stat()
                modified = datetime.fromtimestamp(stat.st_mtime)

                note_data = {
                    'file': md_file.name,
                    'path': str(md_file.relative_to(self.vault_path)),
                    'title': frontmatter.get('title', md_file.stem),
                    'category': category,
                    'frontmatter': frontmatter,
                    'modified': modified.isoformat(),
                    'size': stat.st_size
                }

                notes.append(note_data)

                # Count categories
                categories[category] = categories.get(category, 0) + 1

            except Exception as e:
                logger.warning(f"Failed to process {md_file.name}: {e}")
                continue

        # Sort notes by modified date (newest first)
        notes.sort(key=lambda x: x['modified'], reverse=True)

        result = {
            'notes': notes,
            'categories': categories,
            'total_notes': len(notes),
            'last_scan': datetime.now().isoformat()
        }

        logger.info(f"Scan complete: {len(notes)} notes, {len(categories)} categories")
        return result

    def get_recent_notes(self, limit: int = 10) -> List[Dict]:
        """Get most recently modified notes"""
        vault_data = self.scan_vault()
        return vault_data['notes'][:limit]

    def get_stats(self) -> Dict[str, Any]:
        """Get vault statistics"""
        vault_data = self.scan_vault()

        # Calculate additional stats
        notes = vault_data['notes']

        # Count by category
        category_counts = vault_data['categories']

        # Recent activity (last 7 days)
        recent_cutoff = datetime.now().timestamp() - (7 * 24 * 60 * 60)
        recent_activity = sum(
            1 for note in notes
            if datetime.fromisoformat(note['modified']).timestamp() > recent_cutoff
        )

        # Total size
        total_size = sum(note['size'] for note in notes)

        return {
            'total_notes': vault_data['total_notes'],
            'categories': category_counts,
            'recent_activity_7d': recent_activity,
            'total_size_kb': round(total_size / 1024, 2),
            'last_scan': vault_data['last_scan']
        }

    def search_notes(self, query: str, category: Optional[str] = None) -> List[Dict]:
        """
        Search notes by title, tags, or content

        Args:
            query: Search term
            category: Filter by category (optional)

        Returns:
            List of matching notes
        """
        vault_data = self.scan_vault()
        notes = vault_data['notes']
        query_lower = query.lower()

        results = []
        for note in notes:
            # Filter by category if specified
            if category and note['category'] != category:
                continue

            # Search in title
            if query_lower in note['title'].lower():
                results.append(note)
                continue

            # Search in tags
            tags = note['frontmatter'].get('tags', [])
            if isinstance(tags, str):
                tags = [tags]
            if any(query_lower in tag.lower() for tag in tags):
                results.append(note)
                continue

        return results

    def get_category_notes(self, category: str) -> List[Dict]:
        """Get all notes in a specific category"""
        vault_data = self.scan_vault()
        return [
            note for note in vault_data['notes']
            if note['category'] == category
        ]


def main():
    """CLI test interface"""
    analyzer = VaultAnalyzer()

    print("="*60)
    print("VAULT ANALYZER - KNOWLEDGE BASE SCAN")
    print("="*60)

    # Get statistics
    stats = analyzer.get_stats()

    print(f"\n📊 Statistics:")
    print(f"  Total Notes: {stats['total_notes']}")
    print(f"  Total Size: {stats['total_size_kb']} KB")
    print(f"  Recent Activity (7 days): {stats['recent_activity_7d']}")

    print(f"\n📁 Categories:")
    for category, count in sorted(stats['categories'].items(), key=lambda x: x[1], reverse=True):
        print(f"  {category}: {count}")

    print(f"\n📝 Recent Notes:")
    recent = analyzer.get_recent_notes(5)
    for note in recent:
        print(f"  - {note['title']} ({note['category']}) - {note['modified'][:10]}")

    print(f"\n✅ Scan completed: {stats['last_scan']}")


if __name__ == '__main__':
    main()
