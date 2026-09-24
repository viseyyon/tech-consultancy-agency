#!/bin/bash
# Quick Start Script for Technology Consultancy Agency Web UI

echo "🤖 Technology Consultancy Agency - Web UI"
echo "=========================================="
echo ""

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null; then
    echo "📦 Installing Streamlit..."
    pip install streamlit
fi

# Create necessary directories
mkdir -p reports logs .streamlit

echo "🚀 Starting web interface..."
echo ""
echo "Access the app at: http://localhost:8501"
echo "Press Ctrl+C to stop"
echo ""

# Run Streamlit
streamlit run app.py
