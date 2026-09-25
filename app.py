#!/usr/bin/env python3
"""
Technology Consultancy Agency - Streamlit Web UI (Simple Auth Version)
Enterprise-grade web interface with lightweight authentication
"""

import streamlit as st
import bcrypt
import json
import os
from pathlib import Path
from datetime import datetime
import time

# Import agency components (with error handling)
try:
    from deep_research_agent import DeepResearchAgent, ResearchFindings
    from obsidian_integrator import ObsidianIntegrator
    from consultancy_orchestrator import ConsultancyOrchestrator
    COMPONENTS_AVAILABLE = True
except Exception as e:
    COMPONENTS_AVAILABLE = False
    COMPONENT_ERROR = str(e)

# Page config
st.set_page_config(
    page_title="Technology Consultancy Agency",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Authentication credentials
USERS = {
    'rudram': {
        'name': 'Surendran Manoharan',
        'email': 'rudram.startup@gmail.com',
        'password_hash': b'$2b$12$lII2ktQTh05qKVowh5OiBeygqgFnJPWAQ1RIbszbnmgONDJiaGE12'  # Suren9234!
    }
}

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'username' not in st.session_state:
    st.session_state.username = None
if 'name' not in st.session_state:
    st.session_state.name = None

# Authentication logic
def check_password(username, password):
    """Verify username and password"""
    if username in USERS:
        user = USERS[username]
        return bcrypt.checkpw(password.encode(), user['password_hash'])
    return False

def login():
    """Display login form"""
    st.markdown("### 🔐 Login to Technology Consultancy Agency")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

        if submit:
            if check_password(username, password):
                st.session_state.authenticated = True
                st.session_state.username = username
                st.session_state.name = USERS[username]['name']
                st.success(f"Welcome {USERS[username]['name']}!")
                st.rerun()
            else:
                st.error("Invalid username or password")

def logout():
    """Logout user"""
    st.session_state.authenticated = False
    st.session_state.username = None
    st.session_state.name = None
    st.rerun()

# Main app logic
if not st.session_state.authenticated:
    login()
    st.stop()

# User is authenticated - show main app
with st.sidebar:
    st.success(f"Welcome **{st.session_state.name}**!")
    if st.button("Logout"):
        logout()

    st.markdown("---")
    st.markdown("### 🤖 Multi-Agent System")
    st.markdown("""
    **5 Specialized Agents:**
    - 🔍 Deep Research Agent
    - 🔧 Technology Assessor
    - 💼 Business Value Analyzer
    - 🏗️ Integration Strategist
    - 📊 Report Synthesizer
    """)

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
</style>
""", unsafe_allow_html=True)

# Initialize session state for app
if 'analysis_history' not in st.session_state:
    st.session_state.analysis_history = []

# Main header
st.markdown('<p class="big-font">🤖 Technology Consultancy Agency</p>', unsafe_allow_html=True)
st.markdown("**AI-Powered Technology Research & Integration Analysis**")
st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Dashboard",
    "🔍 Analyze Repository",
    "📚 Knowledge Base",
    "📋 Reports",
    "ℹ️ About"
])

with tab1:
    st.header("📊 Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Analyses", len(st.session_state.analysis_history))

    with col2:
        st.metric("Active Agents", 5)

    with col3:
        st.metric("Knowledge Base", "495+ notes")

    with col4:
        st.metric("Status", "🟢 Active")

    st.markdown("### Recent Activity")
    if st.session_state.analysis_history:
        for analysis in st.session_state.analysis_history[-5:]:
            st.markdown(f"- **{analysis.get('repo_name', 'Unknown')}** - {analysis.get('timestamp', 'N/A')}")
    else:
        st.info("No analyses yet. Start by analyzing a repository!")

with tab2:
    st.header("🔍 Analyze Repository")
    st.markdown("Enter a GitHub or GitLab repository URL to analyze")

    url = st.text_input("Repository URL", placeholder="https://github.com/username/repo")

    if st.button("Start Analysis", type="primary"):
        if url:
            if not COMPONENTS_AVAILABLE:
                st.error(f"Analysis components unavailable: {COMPONENT_ERROR}")
                st.stop()

            with st.spinner("🤖 Multi-agent system analyzing..."):
                try:
                    # Initialize orchestrator
                    orchestrator = ConsultancyOrchestrator()

                    # Validate URL
                    valid, error_msg = orchestrator.validate_input(url)
                    if not valid:
                        st.error(f"Invalid URL: {error_msg}")
                        st.stop()

                    # Run analysis pipeline
                    st.info("🔍 Stage 1/5: Deep Research Agent")
                    results = orchestrator.run_pipeline(url)

                    # Check for errors
                    if results.get('status') == 'failed':
                        st.error(f"Analysis failed: {results.get('error', 'Unknown error')}")
                        st.stop()

                    # Get research findings
                    research = results['stages'].get('research', {})
                    findings = research.get('findings', {})

                    # Display results
                    st.success("✅ Analysis complete!")

                    # Repository info
                    st.markdown("### 📊 Repository Analysis")
                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.metric("⭐ Stars", findings.get('stars', 'N/A'))
                    with col2:
                        st.metric("🍴 Forks", findings.get('forks', 'N/A'))
                    with col3:
                        st.metric("📈 Confidence", f"{findings.get('confidence', 0):.0%}")

                    # Technology stack
                    if findings.get('technology'):
                        st.markdown("### 🔧 Technology Stack")
                        tech_cols = st.columns(min(len(findings['technology']), 4))
                        for idx, tech in enumerate(findings['technology'][:4]):
                            with tech_cols[idx % 4]:
                                st.info(tech)

                    # Purpose
                    if findings.get('purpose'):
                        st.markdown("### 🎯 Purpose")
                        st.write(findings['purpose'])

                    # Features
                    if findings.get('features'):
                        st.markdown("### ✨ Key Features")
                        for feature in findings['features'][:5]:
                            st.markdown(f"- {feature}")

                    # Save to history
                    st.session_state.analysis_history.append({
                        'repo_name': url.split('/')[-1],
                        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M'),
                        'stars': findings.get('stars', 0),
                        'technology': findings.get('technology', [])
                    })

                    # Note about vault sync
                    st.markdown("---")
                    st.info("📝 Analysis saved to Obsidian vault. Will sync to GitHub within 5 minutes.")

                except Exception as e:
                    st.error(f"Analysis error: {str(e)}")
                    import traceback
                    with st.expander("🔍 Error Details"):
                        st.code(traceback.format_exc())
        else:
            st.warning("Please enter a valid URL")

with tab3:
    st.header("📚 Knowledge Base")

    try:
        from vault_analyzer import VaultAnalyzer
        analyzer = VaultAnalyzer()
        stats = analyzer.get_stats()

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Notes", stats['total_notes'])
        with col2:
            st.metric("Categories", len(stats['categories']))
        with col3:
            st.metric("Recent Activity", stats['recent_activity_7d'])
        with col4:
            st.metric("Size", f"{stats['total_size_kb']} KB")

        st.markdown("### Categories")
        for cat, count in sorted(stats['categories'].items(), key=lambda x: x[1], reverse=True):
            st.markdown(f"- **{cat.title()}**: {count} notes")

        st.markdown("### Recent Notes")
        recent = analyzer.get_recent_notes(10)
        for note in recent:
            with st.expander(f"📝 {note['title']}"):
                st.markdown(f"**Category**: {note['category']}")
                st.markdown(f"**Modified**: {note['modified'][:10]}")

    except Exception as e:
        st.error(f"Knowledge Base unavailable: {e}")
        st.info("The vault will sync automatically every 5 minutes")

with tab4:
    st.header("📋 Reports")
    st.info("Analysis reports will appear here after completing repository analyses")

with tab5:
    st.header("ℹ️ About")
    st.markdown("""
    ### Technology Consultancy Agency

    **AI-Powered Multi-Agent System** for automated technology research and integration analysis.

    **Features**:
    - 🔍 Deep repository analysis
    - 💼 Business value assessment
    - 🏗️ Integration recommendations
    - 📊 Comprehensive reports
    - 📚 Knowledge base management
    - 🔄 Auto-sync with Obsidian vault

    **Status**: ✅ Fully Operational

    **Logged in as**: {st.session_state.name} ({st.session_state.username})
    """)

    if not COMPONENTS_AVAILABLE:
        st.warning(f"Some components are loading: {COMPONENT_ERROR}")
