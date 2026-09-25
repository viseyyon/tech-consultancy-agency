#!/usr/bin/env python3
"""
Deep Research Agent - URL Intelligence & Content Extraction
Part of Technology Consultancy Agency

Role: Primary agent for fetching and analyzing URLs (GitHub repos, docs, articles)
Output: Structured findings for downstream agents
"""

import json
import re
import time
from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any, List
from urllib.parse import urlparse
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class ResearchFindings:
    """Structured output from Deep Research Agent"""
    url: str
    source_type: str  # github_repo, documentation, article, api_docs
    purpose: str
    technology: List[str]
    stars: Optional[int]
    forks: Optional[int]
    features: List[str]
    code_samples: List[str]
    community_metrics: Dict[str, Any]
    last_updated: str
    confidence: float
    flags: List[str]
    error: Optional[str] = None


class DeepResearchAgent:
    """
    Deep Research Agent - Primary intelligence gathering

    Responsibilities:
    - Validate and fetch URLs
    - Extract metadata and content
    - Parse GitHub repos, docs, articles
    - Generate structured findings
    """

    ALLOWED_DOMAINS = [
        'github.com', 'gitlab.com', 'bitbucket.org',
        'docs.python.org', 'readthedocs.io', 'readthedocs.org',
        'medium.com', 'dev.to', 'arxiv.org'
    ]

    TIMEOUT_SECONDS = 30
    MAX_RETRIES = 3

    def __init__(self):
        self.session_id = f"research_{int(time.time())}"
        logger.info(f"Deep Research Agent initialized - Session: {self.session_id}")

    def validate_url(self, url: str) -> tuple[bool, str]:
        """
        Validate URL for security and allowed domains

        Returns: (is_valid, error_message)
        """
        try:
            parsed = urlparse(url)

            # Check scheme
            if parsed.scheme not in ['http', 'https']:
                return False, f"Invalid scheme: {parsed.scheme} (only http/https allowed)"

            # Check for localhost/IP addresses
            if parsed.hostname in ['localhost', '127.0.0.1'] or \
               parsed.hostname.startswith('192.168.') or \
               parsed.hostname.startswith('10.'):
                return False, "Local/internal URLs not allowed"

            # Check allowed domains
            domain_allowed = any(
                parsed.hostname == domain or parsed.hostname.endswith(f'.{domain}')
                for domain in self.ALLOWED_DOMAINS
            )

            if not domain_allowed:
                return False, f"Domain {parsed.hostname} not in whitelist"

            return True, ""

        except Exception as e:
            return False, f"URL parsing error: {str(e)}"

    def detect_source_type(self, url: str) -> str:
        """Detect source type from URL"""
        if 'github.com' in url or 'gitlab.com' in url or 'bitbucket.org' in url:
            return 'github_repo'
        elif 'docs.' in url or 'readthedocs' in url:
            return 'documentation'
        elif 'medium.com' in url or 'dev.to' in url:
            return 'article'
        elif 'api' in url.lower():
            return 'api_docs'
        else:
            return 'unknown'

    def fetch_with_retry(self, url: str) -> tuple[bool, Optional[str], Optional[str]]:
        """
        Fetch URL content with exponential backoff retry

        Returns: (success, html_content, error_message)
        """
        try:
            import urllib.request
            import urllib.error
        except ImportError:
            return False, None, "urllib not available"

        for attempt in range(self.MAX_RETRIES):
            try:
                logger.info(f"Fetching URL (attempt {attempt + 1}/{self.MAX_RETRIES}): {url}")

                # Fetch actual HTML content
                req = urllib.request.Request(
                    url,
                    headers={'User-Agent': 'Mozilla/5.0 (TechConsultancyBot/1.0)'}
                )

                with urllib.request.urlopen(req, timeout=self.TIMEOUT_SECONDS) as response:
                    html_content = response.read().decode('utf-8')

                logger.info(f"Successfully fetched: {url} ({len(html_content)} bytes)")
                return True, html_content, None

            except urllib.error.HTTPError as e:
                error_msg = f"HTTP {e.code}: {e.reason}"
                logger.warning(f"Fetch attempt {attempt + 1} failed: {error_msg}")

                if e.code == 404:
                    return False, None, "Repository not found (404)"
                elif e.code == 403:
                    return False, None, "Access forbidden (403) - possible rate limit"

            except Exception as e:
                error_msg = f"Fetch attempt {attempt + 1} failed: {str(e)}"
                logger.warning(error_msg)

            if attempt < self.MAX_RETRIES - 1:
                delay = 2 ** (attempt + 1)
                logger.info(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                return False, None, "Max retries exceeded"

        return False, None, "Max retries exceeded"

    def extract_github_metadata(self, url: str, html_content: str) -> Dict[str, Any]:
        """Extract metadata from GitHub repository HTML"""
        # Parse GitHub URL
        match = re.search(r'github\.com/([^/]+)/([^/]+)', url)
        if not match:
            return {}

        owner, repo = match.groups()
        repo = repo.replace('.git', '')

        metadata = {
            'owner': owner,
            'repo': repo,
            'stars': 0,
            'forks': 0,
            'language': '',
            'topics': [],
            'description': ''
        }

        if not html_content:
            return metadata

        try:
            # Extract stars (e.g., <span id="repo-stars-counter-star" ... >1,234</span>)
            stars_match = re.search(r'id="repo-stars-counter-star"[^>]*>([0-9,\.k]+)</span>', html_content)
            if stars_match:
                stars_str = stars_match.group(1).replace(',', '').replace('k', '000').replace('.', '')
                metadata['stars'] = int(float(stars_str)) if stars_str.replace('.', '').isdigit() else 0

            # Extract forks (e.g., <span id="repo-network-counter" ... >123</span>)
            forks_match = re.search(r'id="repo-network-counter"[^>]*>([0-9,\.k]+)</span>', html_content)
            if forks_match:
                forks_str = forks_match.group(1).replace(',', '').replace('k', '000').replace('.', '')
                metadata['forks'] = int(float(forks_str)) if forks_str.replace('.', '').isdigit() else 0

            # Extract description
            desc_match = re.search(r'<p class="f4 my-3">([^<]+)</p>', html_content)
            if not desc_match:
                desc_match = re.search(r'name="description" content="([^"]+)"', html_content)
            if desc_match:
                metadata['description'] = desc_match.group(1).strip()

            # Extract primary language (multiple patterns)
            lang_patterns = [
                r'<span itemprop="programmingLanguage">([^<]+)</span>',
                r'aria-label="([A-Za-z\+\#]+)\s+[0-9\.]+\s*%',  # From language bar
                r'>([A-Za-z\+\#]+)</span>\s*<span[^>]*>[0-9\.]+%</span>',  # Adjacent to percentage
            ]

            for pattern in lang_patterns:
                lang_match = re.search(pattern, html_content)
                if lang_match:
                    metadata['language'] = lang_match.group(1).strip()
                    break

            # Extract topics/tags (improved pattern)
            topic_patterns = [
                r'<a[^>]*href="/topics/[^"]*"[^>]*>([^<]+)</a>',  # Primary pattern
                r'topic-tag[^>]*>([^<]+)<',  # Fallback pattern
                r'data-octo-click="topic"[^>]*>([^<]+)<',  # Alternative
            ]

            all_topics = []
            for pattern in topic_patterns:
                topics = re.findall(pattern, html_content)
                all_topics.extend([t.strip() for t in topics if t.strip()])

            # Remove duplicates while preserving order
            seen = set()
            unique_topics = []
            for topic in all_topics:
                if topic.lower() not in seen:
                    seen.add(topic.lower())
                    unique_topics.append(topic)

            metadata['topics'] = unique_topics[:10]  # Limit to 10

            # Extract key features from README (if present in HTML)
            features = []

            # Look for bullet points or list items in README
            readme_lists = re.findall(r'<li[^>]*>([^<]+(?:<[^>]+>[^<]+</[^>]+>)*[^<]*)</li>', html_content)
            for item in readme_lists[:20]:  # Check first 20 list items
                # Clean HTML tags
                clean_item = re.sub(r'<[^>]+>', '', item).strip()
                # Keep items that look like features (not too short, not navigation)
                if (20 < len(clean_item) < 200 and
                    not clean_item.lower().startswith(('code of conduct', 'license', 'readme', 'security'))):
                    features.append(clean_item)
                    if len(features) >= 5:  # Limit to 5 features
                        break

            metadata['features'] = features

            logger.info(f"Extracted: {metadata['stars']} stars, {metadata['forks']} forks, {len(metadata['topics'])} topics, {len(features)} features, language={metadata['language']}")

        except Exception as e:
            logger.warning(f"Failed to parse GitHub metadata: {e}")

        return metadata

    def analyze_url(self, url: str) -> ResearchFindings:
        """
        Main analysis method - orchestrates URL research

        Args:
            url: URL to analyze

        Returns:
            ResearchFindings with structured data
        """
        start_time = time.time()
        logger.info(f"=== Starting analysis: {url} ===")

        # Step 1: Validate URL
        is_valid, error_msg = self.validate_url(url)
        if not is_valid:
            logger.error(f"Validation failed: {error_msg}")
            return ResearchFindings(
                url=url,
                source_type='unknown',
                purpose='',
                technology=[],
                stars=None,
                forks=None,
                features=[],
                code_samples=[],
                community_metrics={},
                last_updated='',
                confidence=0.0,
                flags=['validation_failed'],
                error=error_msg
            )

        # Step 2: Detect source type
        source_type = self.detect_source_type(url)
        logger.info(f"Detected source type: {source_type}")

        # Step 3: Fetch content with retry
        success, html_content, error = self.fetch_with_retry(url)
        if not success:
            logger.error(f"Fetch failed: {error}")
            return ResearchFindings(
                url=url,
                source_type=source_type,
                purpose='',
                technology=[],
                stars=None,
                forks=None,
                features=[],
                code_samples=[],
                community_metrics={},
                last_updated='',
                confidence=0.0,
                flags=['fetch_failed'],
                error=error
            )

        # Step 4: Extract metadata based on source type
        if source_type == 'github_repo':
            metadata = self.extract_github_metadata(url, html_content)
        else:
            metadata = {}

        # Build technology list from language + topics
        technology = []
        if metadata.get('language'):
            technology.append(metadata['language'])
        technology.extend(metadata.get('topics', []))

        # Use description or fallback
        purpose = metadata.get('description') or f"GitHub repository: {metadata.get('repo', 'unknown')}"

        # Step 5: Build findings
        findings = ResearchFindings(
            url=url,
            source_type=source_type,
            purpose=purpose,
            technology=technology[:10],  # Limit to 10 items
            stars=metadata.get('stars', 0),
            forks=metadata.get('forks', 0),
            features=metadata.get('features', []),  # Extracted from README
            code_samples=[],  # Could be extracted later
            community_metrics={
                'stars': metadata.get('stars', 0),
                'forks': metadata.get('forks', 0),
                'topics': len(metadata.get('topics', []))
            },
            last_updated=time.strftime('%Y-%m-%d'),
            confidence=0.85 if metadata.get('stars', 0) > 0 else 0.60,  # Higher confidence with real data
            flags=['active_development'] if metadata.get('stars', 0) > 100 else []
        )

        duration = time.time() - start_time
        logger.info(f"=== Analysis complete in {duration:.2f}s ===")

        return findings

    def to_json(self, findings: ResearchFindings) -> str:
        """Convert findings to JSON for hand-off"""
        return json.dumps(asdict(findings), indent=2)

    def save_findings(self, findings: ResearchFindings, output_path: str):
        """Save findings to disk"""
        try:
            with open(output_path, 'w') as f:
                f.write(self.to_json(findings))
            logger.info(f"Findings saved to: {output_path}")
        except Exception as e:
            logger.error(f"Failed to save findings: {e}")


def main():
    """CLI entry point for testing"""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python3 deep_research_agent.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    agent = DeepResearchAgent()
    findings = agent.analyze_url(url)

    print("\n" + "="*60)
    print("DEEP RESEARCH AGENT - FINDINGS")
    print("="*60)
    print(agent.to_json(findings))

    if findings.error:
        sys.exit(1)


if __name__ == '__main__':
    main()
