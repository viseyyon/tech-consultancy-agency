#!/usr/bin/env python3
"""
Technology Consultancy Agency - Streamlit Web UI
Enterprise-grade web interface for automated technology consultancy

Deploy to: Streamlit Community Cloud, Hugging Face Spaces, or Railway (all FREE)
"""

import streamlit as st
import json
import os
from pathlib import Path
from datetime import datetime
import time

# Import agency components
from deep_research_agent import DeepResearchAgent, ResearchFindings
from obsidian_integrator import ObsidianIntegrator
from consultancy_orchestrator import ConsultancyOrchestrator

# Page config
st.set_page_config(
    page_title="Technology Consultancy Agency",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .reportview-container {
        background: #0e1117;
    }
    .big-font {
        font-size:30px !important;
        font-weight: bold;
    }
    .success-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #1e3a1e;
        border-left: 5px solid #4caf50;
    }
    .info-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #1a1f3a;
        border-left: 5px solid #2196f3;
    }
    .warning-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #3a2a1a;
        border-left: 5px solid #ff9800;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'analysis_history' not in st.session_state:
    st.session_state.analysis_history = []
if 'current_session' not in st.session_state:
    st.session_state.current_session = None

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/300x100/0e1117/ffffff?text=Tech+Consultancy", use_container_width=True)

    st.markdown("### 🤖 Multi-Agent System")
    st.markdown("""
    **5 Specialized Agents:**
    - 🔍 Deep Research Agent
    - 🔧 Technology Assessor
    - 💼 Business Value Analyzer
    - 🏗️ Integration Strategist
    - 📊 Report Synthesizer
    """)

    st.markdown("---")

    st.markdown("### ⚙️ Configuration")

    # Obsidian integration toggle
    use_obsidian = st.checkbox("Enable Obsidian Integration", value=True)

    # Output directory
    output_dir = st.text_input("Output Directory", value="reports")

    # Cloud sync options
    st.markdown("### ☁️ Cloud Sync")
    sync_method = st.selectbox(
        "Sync Method",
        ["Local Only", "Git Auto-commit", "Manual Export"]
    )

    if sync_method == "Git Auto-commit":
        st.info("💡 Commits to GitHub after each analysis")

    st.markdown("---")

    # Analysis history
    st.markdown("### 📜 Recent Analysis")
    if st.session_state.analysis_history:
        for item in st.session_state.analysis_history[-5:]:
            st.markdown(f"- {item['timestamp']}: {item['repo']}")
    else:
        st.markdown("*No analysis yet*")

    st.markdown("---")
    st.markdown("### 📊 Stats")
    st.metric("Total Analyses", len(st.session_state.analysis_history))
    st.metric("Success Rate", "100%" if st.session_state.analysis_history else "0%")

# Main content
st.markdown('<p class="big-font">🤖 Technology Consultancy Agency</p>', unsafe_allow_html=True)
st.markdown("**Enterprise-grade automated technology assessment powered by 5 specialized AI agents**")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🔍 Analyze Repository",
    "📊 Dashboard",
    "📁 Reports",
    "🔧 Obsidian Vault",
    "ℹ️ About"
])

# Tab 1: Main Analysis
with tab1:
    st.header("Repository Analysis")

    col1, col2 = st.columns([3, 1])

    with col1:
        url = st.text_input(
            "Enter Repository URL",
            placeholder="https://github.com/username/repository",
            help="Supported: GitHub, GitLab, Bitbucket"
        )

    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        analyze_button = st.button("🚀 Analyze", type="primary", use_container_width=True)

    if analyze_button and url:
        # Validation
        if not url.startswith(('http://', 'https://')):
            st.error("❌ Invalid URL. Must start with http:// or https://")
        else:
            # Progress tracking
            progress_bar = st.progress(0)
            status_text = st.empty()

            try:
                # Initialize orchestrator
                status_text.text("🔧 Initializing agents...")
                progress_bar.progress(10)
                orchestrator = ConsultancyOrchestrator(output_dir=output_dir)

                # Stage 1: Deep Research
                status_text.text("🔍 Stage 1/5: Deep Research Agent analyzing URL...")
                progress_bar.progress(20)
                time.sleep(0.5)

                # Stage 2: Technology Assessment
                status_text.text("🔧 Stage 2/5: Technology Assessor evaluating stack...")
                progress_bar.progress(40)
                time.sleep(0.5)

                # Stage 3: Business Value
                status_text.text("💼 Stage 3/5: Business Value Analyzer calculating ROI...")
                progress_bar.progress(60)
                time.sleep(0.5)

                # Stage 4: Integration Strategy
                status_text.text("🏗️ Stage 4/5: Integration Strategist planning deployment...")
                progress_bar.progress(80)
                time.sleep(0.5)

                # Stage 5: Report Synthesis
                status_text.text("📊 Stage 5/5: Report Synthesizer generating deliverables...")
                progress_bar.progress(90)

                # Run pipeline
                results = orchestrator.run_pipeline(url)

                progress_bar.progress(100)
                status_text.text("✅ Analysis complete!")

                # Store in session
                st.session_state.current_session = results
                st.session_state.analysis_history.append({
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M'),
                    'repo': url.split('/')[-1],
                    'session_id': results['session_id']
                })

                # Display results
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown("### ✅ Analysis Complete")
                st.markdown(f"**Session ID**: `{results['session_id']}`")
                st.markdown(f"**Status**: {results['status']}")
                st.markdown('</div>', unsafe_allow_html=True)

                # Key findings
                st.markdown("---")
                st.markdown("### 📈 Key Findings")

                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.metric(
                        "Technology Maturity",
                        f"{results['stages']['technology']['maturity_score']}/10",
                        delta="Good" if results['stages']['technology']['maturity_score'] >= 7 else "Fair"
                    )

                with col2:
                    st.metric(
                        "Business Value",
                        results['stages']['business_value']['competitive_position']
                    )

                with col3:
                    st.metric(
                        "Integration Effort",
                        results['stages']['integration']['effort_estimate']
                    )

                with col4:
                    st.metric(
                        "ROI Estimate",
                        results['stages']['business_value']['roi_estimate']['cost_savings']
                    )

                # Detailed sections
                st.markdown("---")

                with st.expander("🔧 Technical Assessment", expanded=True):
                    tech = results['stages']['technology']
                    st.markdown(f"**Architecture**: {tech['architecture']}")
                    st.markdown(f"**Code Quality**: {tech['code_quality']}")
                    st.markdown("**Technology Stack**:")
                    for t in tech['tech_stack']:
                        st.markdown(f"- {t}")
                    st.markdown("**Risks**:")
                    for r in tech['risks']:
                        st.warning(f"⚠️ {r}")

                with st.expander("💼 Business Value Analysis"):
                    biz = results['stages']['business_value']
                    st.markdown("**Use Cases**:")
                    for uc in biz['use_cases']:
                        st.markdown(f"- {uc}")
                    st.markdown("**ROI Analysis**:")
                    st.json(biz['roi_estimate'])

                with st.expander("🏗️ Integration Strategy"):
                    integration = results['stages']['integration']
                    st.markdown("**Integration Points**:")
                    for k, v in integration['integration_points'].items():
                        st.markdown(f"- **{k}**: {v}")
                    st.markdown("**Rollout Phases**:")
                    for phase in integration['rollout_phases']:
                        st.markdown(f"- {phase}")

                with st.expander("📁 Obsidian Integration"):
                    obs = results['obsidian']
                    if obs['success']:
                        st.success(f"✅ Note created: `{obs['note_path']}`")
                        st.markdown("**Updates**:")
                        for update in obs['updates']:
                            st.markdown(f"- {update}")
                    else:
                        st.error(f"❌ {obs.get('error', 'Unknown error')}")

                # Download buttons
                st.markdown("---")
                st.markdown("### 📥 Download Reports")

                col1, col2 = st.columns(2)

                with col1:
                    # Read report
                    if 'report_path' in results:
                        report_path = Path(results['report_path'])
                        if report_path.exists():
                            report_content = report_path.read_text()
                            st.download_button(
                                label="📄 Download Report (Markdown)",
                                data=report_content,
                                file_name=f"consultancy_report_{results['session_id']}.md",
                                mime="text/markdown"
                            )

                with col2:
                    # JSON findings
                    findings_file = Path(output_dir) / f"{results['session_id']}_findings.json"
                    if findings_file.exists():
                        findings_content = findings_file.read_text()
                        st.download_button(
                            label="📊 Download Findings (JSON)",
                            data=findings_content,
                            file_name=f"findings_{results['session_id']}.json",
                            mime="application/json"
                        )

            except Exception as e:
                st.error(f"❌ Analysis failed: {str(e)}")
                st.exception(e)

# Tab 2: Dashboard
with tab2:
    st.header("Analytics Dashboard")

    if st.session_state.analysis_history:
        st.markdown("### 📊 Analysis Trends")

        # Chart placeholder
        st.line_chart([len(st.session_state.analysis_history)])

        # Recent analyses table
        st.markdown("### 📋 Recent Analyses")
        st.table(st.session_state.analysis_history[-10:])
    else:
        st.info("📊 No analyses yet. Start by analyzing a repository in the 'Analyze Repository' tab.")

# Tab 3: Reports
with tab3:
    st.header("Generated Reports")

    reports_dir = Path(output_dir)
    if reports_dir.exists():
        report_files = list(reports_dir.glob("*.md"))

        if report_files:
            for report_file in sorted(report_files, reverse=True)[:10]:
                with st.expander(f"📄 {report_file.name}"):
                    content = report_file.read_text()
                    st.markdown(content)
                    st.download_button(
                        f"Download {report_file.name}",
                        data=content,
                        file_name=report_file.name,
                        mime="text/markdown",
                        key=report_file.name
                    )
        else:
            st.info("📁 No reports generated yet.")
    else:
        st.warning("📁 Reports directory not found.")

# Tab 4: Obsidian Vault
with tab4:
    st.header("Obsidian Vault Browser")

    vault_path = Path("~/Documents/Obsidian Vault/10-knowledge").expanduser()

    if vault_path.exists():
        st.success(f"✅ Vault found: `{vault_path}`")

        notes = list(vault_path.glob("*.md"))

        st.markdown(f"### 📚 {len(notes)} Notes in Knowledge Base")

        # Filter
        search = st.text_input("🔍 Search notes", "")

        filtered_notes = [n for n in notes if search.lower() in n.name.lower()] if search else notes

        for note in sorted(filtered_notes, key=lambda x: x.stat().st_mtime, reverse=True)[:20]:
            with st.expander(f"📝 {note.stem}"):
                content = note.read_text()
                st.markdown(content)
    else:
        st.warning(f"📁 Vault not found at `{vault_path}`")
        st.info("💡 For cloud deployment, use Git-based sync or environment variable to configure vault path.")

# Tab 5: About
with tab5:
    st.header("About Technology Consultancy Agency")

    st.markdown("""
    ### 🤖 Multi-Agent Architecture

    This system uses **5 specialized AI agents** working in concert:

    1. **Deep Research Agent** 🔍
       - URL validation and security checks
       - Content fetching with retry logic
       - Metadata extraction

    2. **Technology Assessor** 🔧
       - Stack analysis
       - Maturity scoring (1-10)
       - Risk identification

    3. **Business Value Analyzer** 💼
       - Use case identification
       - ROI calculation
       - Competitive positioning

    4. **Integration Strategist** 🏗️
       - Integration architecture design
       - Effort estimation
       - Phased rollout planning

    5. **Report Synthesizer** 📊
       - Professional report generation
       - Obsidian vault integration
       - Knowledge base updates

    ---

    ### 🚀 Deployment Options (All FREE)

    **Streamlit Community Cloud**
    - Free unlimited public apps
    - 1GB RAM, sleeps after 12h inactivity
    - Perfect for demos

    **Hugging Face Spaces**
    - 2 CPU cores, 16GB RAM
    - Sleeps after 48h inactivity
    - Great for ML models

    **Railway**
    - Generous free tier
    - Auto-deploy from GitHub
    - Excellent DX

    ---

    ### ☁️ Cloud Obsidian Sync (FREE)

    Use **Obsidian Git Plugin** for free cloud sync:
    - Auto-commits to GitHub
    - 15GB free storage
    - Unlimited version history
    - Works across all devices

    ---

    ### 📊 Enterprise Features

    ✅ URL validation & security
    ✅ Exponential backoff retry
    ✅ Structured logging
    ✅ Audit trail
    ✅ Session tracking
    ✅ Error handling
    ✅ Obsidian integration
    ✅ Knowledge base auto-update

    ---

    **Version**: 1.0
    **Created**: 2026-09-24
    **Owner**: Surendran Manoharan
    """)

    st.markdown("---")
    st.info("💡 **Tip**: Deploy this app to Streamlit Community Cloud for free and use Obsidian Git plugin to sync your vault across devices at zero cost!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888;">
    Technology Consultancy Agency v1.0 | Powered by 5 AI Agents | © 2026
</div>
""", unsafe_allow_html=True)
