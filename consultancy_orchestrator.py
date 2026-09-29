#!/usr/bin/env python3
"""
Technology Consultancy Agency - Main Orchestrator
Enterprise-grade multi-agent consultancy automation

Usage:
    ./consultancy_orchestrator.py <URL>
    ./consultancy_orchestrator.py --url https://github.com/example/repo
"""

import argparse
import json
import logging
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

from deep_research_agent import DeepResearchAgent, ResearchFindings
from obsidian_integrator import ObsidianIntegrator

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/consultancy.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


class ConsultancyOrchestrator:
    """
    Main orchestrator for Technology Consultancy Agency

    Coordinates: Deep Research Agent → Technology Assessor → Business Value Analyzer
                 → Integration Strategist → Report Synthesizer
    """

    def __init__(self, output_dir: str = "reports"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Initialize log directory
        Path("logs").mkdir(exist_ok=True)

        # Initialize agents
        self.research_agent = DeepResearchAgent()
        self.obsidian = ObsidianIntegrator()

        logger.info("Consultancy Orchestrator initialized")

    def validate_input(self, url: str) -> tuple[bool, str]:
        """Validate input URL"""
        if not url:
            return False, "URL is required"
        if not url.startswith(('http://', 'https://')):
            return False, "URL must start with http:// or https://"
        return True, ""

    def run_pipeline(self, url: str) -> Dict[str, Any]:
        """
        Execute full consultancy pipeline

        Pipeline:
        1. Deep Research Agent - URL analysis
        2. Technology Assessor - Stack evaluation
        3. Business Value Analyzer - Use cases & ROI
        4. Integration Strategist - Integration planning
        5. Report Synthesizer - Final report + Obsidian update
        """
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        session_id = f"consultancy_{timestamp}"

        logger.info(f"=== Starting consultancy pipeline: {session_id} ===")
        logger.info(f"Target URL: {url}")

        results = {
            'session_id': session_id,
            'url': url,
            'timestamp': timestamp,
            'stages': {}
        }

        try:
            # Stage 1: Deep Research
            logger.info("Stage 1/5: Deep Research Agent")
            findings = self.research_agent.analyze_url(url)

            if findings.error:
                logger.error(f"Research failed: {findings.error}")
                results['status'] = 'failed'
                results['error'] = findings.error
                return results

            results['stages']['research'] = {
                'status': 'complete',
                'findings': findings.__dict__
            }

            # Save findings
            findings_file = self.output_dir / f"{session_id}_findings.json"
            self.research_agent.save_findings(findings, str(findings_file))

            # Stage 2: Technology Assessment
            logger.info("Stage 2/5: Technology Assessor")
            tech_assessment = self.assess_technology(findings)
            results['stages']['technology'] = tech_assessment

            # Stage 3: Business Value Analysis
            logger.info("Stage 3/5: Business Value Analyzer")
            business_value = self.analyze_business_value(findings, tech_assessment)
            results['stages']['business_value'] = business_value

            # Stage 4: Integration Strategy
            logger.info("Stage 4/5: Integration Strategist")
            integration = self.plan_integration(findings, tech_assessment, business_value)
            results['stages']['integration'] = integration

            # Stage 5: Report Synthesis & Obsidian Update
            logger.info("Stage 5/5: Report Synthesizer")

            # Update Obsidian
            obsidian_result = self.obsidian.integrate(findings.__dict__)
            results['obsidian'] = obsidian_result

            # Set status before generating report
            results['status'] = 'complete'

            # Generate report
            report_path = self.generate_report(results)
            results['report_path'] = str(report_path)

            logger.info(f"=== Pipeline complete: {session_id} ===")

        except Exception as e:
            logger.error(f"Pipeline failed: {e}", exc_info=True)
            results['status'] = 'error'
            results['error'] = str(e)

        return results

    def assess_technology(self, findings: ResearchFindings) -> Dict[str, Any]:
        """Technology Assessor Agent - Intelligent assessment based on real data"""

        # Calculate maturity score (1-10) based on stars, forks, and tech stack
        stars = findings.stars
        forks = findings.forks
        tech_count = len(findings.technology)

        # Maturity scoring algorithm
        maturity = 0
        if stars >= 1000: maturity += 3
        elif stars >= 100: maturity += 2
        elif stars >= 10: maturity += 1

        if forks >= 100: maturity += 2
        elif forks >= 20: maturity += 1

        if tech_count >= 8: maturity += 2
        elif tech_count >= 5: maturity += 1

        if len(findings.features) >= 5: maturity += 2
        elif len(findings.features) >= 3: maturity += 1

        maturity_score = min(maturity, 10)

        # Assess code quality based on community engagement
        star_fork_ratio = forks / max(stars, 1)
        if star_fork_ratio > 0.3:
            code_quality = 'excellent'
        elif star_fork_ratio > 0.1:
            code_quality = 'good'
        elif star_fork_ratio > 0.05:
            code_quality = 'fair'
        else:
            code_quality = 'needs_review'

        # Infer architecture from tech stack
        tech_lower = [t.lower() for t in findings.technology]
        if any(t in tech_lower for t in ['kubernetes', 'docker', 'microservices']):
            architecture = 'microservices'
        elif any(t in tech_lower for t in ['monolith', 'rails', 'django']):
            architecture = 'monolithic'
        elif any(t in tech_lower for t in ['serverless', 'lambda', 'functions']):
            architecture = 'serverless'
        else:
            architecture = 'standard'

        # Identify risks based on tech stack and metrics
        risks = []
        if tech_count > 15:
            risks.append('high_complexity_stack')
        if stars < 50:
            risks.append('low_community_adoption')
        if forks < 5:
            risks.append('limited_maintenance_capacity')
        if not findings.features:
            risks.append('documentation_gaps')

        return {
            'status': 'complete',
            'maturity_score': maturity_score,
            'tech_stack': findings.technology,
            'tech_count': tech_count,
            'risks': risks if risks else ['minimal_risks'],
            'architecture': architecture,
            'code_quality': code_quality,
            'star_fork_ratio': round(star_fork_ratio, 3),
            'assessment_basis': {
                'stars': stars,
                'forks': forks,
                'tech_items': tech_count,
                'features': len(findings.features)
            }
        }

    def analyze_business_value(self, findings: ResearchFindings, tech_assessment: Dict) -> Dict[str, Any]:
        """Business Value Analyzer - Data-driven ROI and use case analysis"""

        # Extract use cases from features and description
        use_cases = []
        if findings.features:
            # Use actual features as use cases
            use_cases = [f.split('.')[0].strip() for f in findings.features[:5]]
        else:
            # Infer from technology stack
            tech_lower = [t.lower() for t in findings.technology]
            if any(t in tech_lower for t in ['docker', 'kubernetes', 'deployment']):
                use_cases.append('Infrastructure automation and orchestration')
            if any(t in tech_lower for t in ['api', 'rest', 'graphql']):
                use_cases.append('API integration and service connectivity')
            if any(t in tech_lower for t in ['ml', 'ai', 'machine-learning']):
                use_cases.append('AI/ML model deployment and optimization')
            if any(t in tech_lower for t in ['security', 'auth', 'encryption']):
                use_cases.append('Security enhancement and access control')

        if not use_cases:
            use_cases = ['General development automation', 'Team productivity enhancement']

        # Calculate ROI based on stars and maturity
        stars = findings.stars
        maturity = tech_assessment['maturity_score']

        # ROI estimation algorithm
        # High stars + high maturity = high value
        if stars >= 1000 and maturity >= 7:
            cost_savings = '$5000-10000/quarter'
            efficiency_gain = '60-80%'
            payback_period = '1-2 months'
            competitive_position = 'Market Leader'
        elif stars >= 500 and maturity >= 6:
            cost_savings = '$3000-5000/quarter'
            efficiency_gain = '40-60%'
            payback_period = '2-3 months'
            competitive_position = 'Strong'
        elif stars >= 100 and maturity >= 5:
            cost_savings = '$1500-3000/quarter'
            efficiency_gain = '30-40%'
            payback_period = '3-4 months'
            competitive_position = 'Competitive'
        elif stars >= 50:
            cost_savings = '$500-1500/quarter'
            efficiency_gain = '20-30%'
            payback_period = '4-6 months'
            competitive_position = 'Emerging'
        else:
            cost_savings = '$200-500/quarter'
            efficiency_gain = '10-20%'
            payback_period = '6-12 months'
            competitive_position = 'Experimental'

        # Calculate adoption score
        adoption_score = min(10, int((stars / 100) * 2 + maturity / 2))

        return {
            'status': 'complete',
            'use_cases': use_cases,
            'roi_estimate': {
                'cost_savings': cost_savings,
                'efficiency_gain': efficiency_gain,
                'payback_period': payback_period,
                'adoption_score': adoption_score
            },
            'competitive_position': competitive_position,
            'market_validation': {
                'stars': stars,
                'community_size': 'large' if stars > 1000 else 'medium' if stars > 100 else 'small',
                'adoption_trend': 'proven' if stars > 500 else 'growing' if stars > 50 else 'early'
            }
        }

    def plan_integration(self, findings: ResearchFindings, tech: Dict, business: Dict) -> Dict[str, Any]:
        """Integration Strategist - Smart integration planning based on stack and complexity"""

        tech_stack = findings.technology
        tech_lower = [t.lower() for t in tech_stack]
        maturity = tech['maturity_score']
        tech_count = len(tech_stack)

        # Identify integration points based on actual tech stack
        integration_points = {}

        # API/Service integration
        if any(t in tech_lower for t in ['api', 'rest', 'graphql', 'http']):
            integration_points['API Integration'] = 'REST/GraphQL endpoints via HTTP client'

        # Container/Infrastructure integration
        if any(t in tech_lower for t in ['docker', 'kubernetes', 'containerization']):
            integration_points['Infrastructure'] = 'Docker containerization and Kubernetes orchestration'

        # Database integration
        if any(t in tech_lower for t in ['database', 'sql', 'postgres', 'mysql', 'mongodb']):
            integration_points['Data Layer'] = 'Database connectivity and ORM integration'

        # Authentication integration
        if any(t in tech_lower for t in ['auth', 'oauth', 'security', 'jwt', 'oidc', 'openid-connect']):
            integration_points['Authentication'] = 'OAuth/OIDC authentication flow integration'

        # CLI/Automation integration
        if any(t in tech_lower for t in ['cli', 'command-line', 'automation', 'script']):
            integration_points['Automation'] = 'CLI integration and workflow automation'

        # AI/ML integration
        if any(t in tech_lower for t in ['ai', 'ml', 'machine-learning', 'llm', 'neural']):
            integration_points['AI/ML'] = 'Model inference and training pipeline integration'

        # Default integration if none detected
        if not integration_points:
            integration_points = {
                'Direct Integration': 'Library import and API usage',
                'Agent Enhancement': 'Extend existing agent capabilities'
            }

        # Calculate effort estimate based on complexity
        complexity_score = 0
        complexity_score += tech_count / 2  # More tech = more complexity
        complexity_score += (10 - maturity)  # Lower maturity = more effort
        complexity_score += len(tech['risks'])  # More risks = more effort

        if complexity_score <= 3:
            effort_estimate = '1-2 weeks'
            complexity_level = 'Low'
        elif complexity_score <= 6:
            effort_estimate = '2-4 weeks'
            complexity_level = 'Medium'
        elif complexity_score <= 10:
            effort_estimate = '4-8 weeks'
            complexity_level = 'High'
        else:
            effort_estimate = '8-12 weeks'
            complexity_level = 'Very High'

        # Rollout phases based on maturity and risks
        if maturity >= 7 and len(tech['risks']) <= 2:
            rollout_phases = ['Quick Pilot', 'Production']
        elif maturity >= 5:
            rollout_phases = ['Pilot', 'Staging', 'Production']
        else:
            rollout_phases = ['Research', 'Prototype', 'Pilot', 'Staging', 'Production']

        # Prerequisites based on tech stack
        prerequisites = []
        if any(t in tech_lower for t in ['docker', 'kubernetes']):
            prerequisites.append('Container runtime environment')
        if any(t in tech_lower for t in ['database', 'sql']):
            prerequisites.append('Database infrastructure')
        if any(t in tech_lower for t in ['auth', 'oauth']):
            prerequisites.append('Authentication provider setup')

        return {
            'status': 'complete',
            'integration_points': integration_points,
            'effort_estimate': effort_estimate,
            'complexity_level': complexity_level,
            'rollout_phases': rollout_phases,
            'prerequisites': prerequisites if prerequisites else ['Standard development environment'],
            'integration_readiness': {
                'maturity': maturity,
                'risk_count': len(tech['risks']),
                'complexity_score': round(complexity_score, 1)
            }
        }

    def generate_report(self, results: Dict[str, Any]) -> Path:
        """Generate consultancy report"""
        report_path = self.output_dir / f"{results['session_id']}_report.md"

        content = f"""# Technology Consultancy Report

**Session**: {results['session_id']}
**URL**: {results['url']}
**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Status**: {results['status']}

---

## Executive Summary

Repository analyzed successfully. Key findings:

- **Technology Maturity**: {results['stages']['technology']['maturity_score']}/10
- **Business Value**: {results['stages']['business_value']['competitive_position']}
- **Integration Effort**: {results['stages']['integration']['effort_estimate']}

---

## Technical Assessment

### Technology Stack
{chr(10).join(f"- {t}" for t in results['stages']['technology']['tech_stack'])}

### Code Quality
- **Assessment**: {results['stages']['technology']['code_quality']}
- **Architecture**: {results['stages']['technology']['architecture']}

### Risks Identified
{chr(10).join(f"- {r}" for r in results['stages']['technology']['risks'])}

---

## Business Value

### Use Cases
{chr(10).join(f"{i+1}. {uc}" for i, uc in enumerate(results['stages']['business_value']['use_cases']))}

### ROI Analysis
- **Cost Savings**: {results['stages']['business_value']['roi_estimate']['cost_savings']}
- **Efficiency Gain**: {results['stages']['business_value']['roi_estimate']['efficiency_gain']}
- **Payback Period**: {results['stages']['business_value']['roi_estimate']['payback_period']}

---

## Integration Recommendations

### Integration Points
{chr(10).join(f"- **{k}**: {v}" for k, v in results['stages']['integration']['integration_points'].items())}

### Implementation Phases
{chr(10).join(f"{i+1}. {p}" for i, p in enumerate(results['stages']['integration']['rollout_phases']))}

**Estimated Effort**: {results['stages']['integration']['effort_estimate']}

---

## Obsidian Integration

**Status**: {results['obsidian']['success']}
**Note Created**: {results['obsidian'].get('note_path', 'N/A')}
**Updates**: {', '.join(results['obsidian'].get('updates', []))}

---

**Generated by**: Technology Consultancy Agency (Multi-Agent System)
**Report Path**: `{report_path}`
"""

        report_path.write_text(content)
        logger.info(f"Report generated: {report_path}")

        return report_path


def main():
    """CLI entry point"""
    parser = argparse.ArgumentParser(
        description='Technology Consultancy Agency - Automated Analysis',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('url', nargs='?', help='URL to analyze')
    parser.add_argument('--url', dest='url_flag', help='URL to analyze (alternative syntax)')
    parser.add_argument('--output', default='reports', help='Output directory')

    args = parser.parse_args()

    # Get URL from positional or flag
    url = args.url or args.url_flag

    if not url:
        parser.print_help()
        sys.exit(1)

    # Initialize orchestrator
    orchestrator = ConsultancyOrchestrator(output_dir=args.output)

    # Validate input
    valid, error = orchestrator.validate_input(url)
    if not valid:
        logger.error(f"Invalid input: {error}")
        sys.exit(1)

    # Run pipeline
    results = orchestrator.run_pipeline(url)

    # Print summary
    print("\n" + "="*60)
    print("CONSULTANCY AGENCY - RESULTS")
    print("="*60)
    print(f"Session: {results['session_id']}")
    print(f"Status: {results['status']}")

    if results['status'] == 'complete':
        print(f"Report: {results['report_path']}")
        print(f"Obsidian: {results['obsidian']['note_path']}")
        print("\n✅ Analysis complete")
    else:
        print(f"Error: {results.get('error', 'Unknown')}")
        print("\n❌ Analysis failed")
        sys.exit(1)


if __name__ == '__main__':
    main()
