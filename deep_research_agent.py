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

    def fetch_with_retry(self, url: str) -> tuple[bool, Optional[Dict[str, Any]], Optional[str]]:
        """
        Fetch URL with exponential backoff retry

        Returns: (success, data, error_message)
        """
        for attempt in range(self.MAX_RETRIES):
            try:
                logger.info(f"Fetching URL (attempt {attempt + 1}/{self.MAX_RETRIES}): {url}")

                # Import WebFetch tool (assume available in environment)
                # In real implementation, use actual HTTP client or tool
                # For demo, simulate fetch

                # Placeholder for actual fetch logic
                # In production: use requests library or WebFetch tool
                data = {
                    'url': url,
                    'fetched_at': time.strftime('%Y-%m-%d %H:%M:%S'),
                    'status': 'success'
                }

                logger.info(f"Successfully fetched: {url}")
                return True, data, None

            except Exception as e:
                error_msg = f"Fetch attempt {attempt + 1} failed: {str(e)}"
                logger.warning(error_msg)

                if attempt < self.MAX_RETRIES - 1:
                    # Exponential backoff: 2s, 4s, 8s
                    delay = 2 ** (attempt + 1)
                    logger.info(f"Retrying in {delay} seconds...")
                    time.sleep(delay)
                else:
                    return False, None, error_msg

        return False, None, "Max retries exceeded"

    def extract_github_metadata(self, url: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Extract metadata from GitHub repository"""
        # Parse GitHub URL
        match = re.search(r'github\.com/([^/]+)/([^/]+)', url)
        if not match:
            return {}

        owner, repo = match.groups()
        repo = repo.replace('.git', '')

        # In production: call GitHub API
        # For demo: return structure
        return {
            'owner': owner,
            'repo': repo,
            'stars': 0,  # Fetch from API
            'forks': 0,  # Fetch from API
            'language': 'Python',  # Fetch from API
            'topics': []  # Fetch from API
        }

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
        success, data, error = self.fetch_with_retry(url)
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
            metadata = self.extract_github_metadata(url, data)
        else:
            metadata = {}

        # Step 5: Build findings
        findings = ResearchFindings(
            url=url,
            source_type=source_type,
            purpose=f"Analysis of {source_type}",  # Extract from README
            technology=metadata.get('topics', []),
            stars=metadata.get('stars'),
            forks=metadata.get('forks'),
            features=[],  # Parse from README
            code_samples=[],  # Extract code blocks
            community_metrics={
                'contributors': 0,  # From API
                'commits': 0,  # From API
                'issues': 0  # From API
            },
            last_updated=time.strftime('%Y-%m-%d'),
            confidence=0.85,
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
