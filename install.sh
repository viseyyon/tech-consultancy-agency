#!/bin/bash
# One-line installer for Technology Consultancy Agency
# Usage: curl -fsSL https://raw.githubusercontent.com/viseyyon/tech-consultancy-agency/main/install.sh | bash

set -e

echo "🚀 Technology Consultancy Agency - One-Line Installer"
echo "=" | tr -c '\n' '=' | head -c 60; echo ""

# Variables
INSTALL_DIR="$HOME/Documents/tech-consultancy-agency"
REPO_URL="https://github.com/viseyyon/tech-consultancy-agency.git"

# Check prerequisites
echo ""
echo "📋 Checking prerequisites..."

# Python
if command -v python3 &> /dev/null; then
    PY_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
    echo "✅ Python $PY_VERSION found"
else
    echo "❌ Python 3 not found. Please install Python 3.9+"
    exit 1
fi

# Git
if command -v git &> /dev/null; then
    echo "✅ Git found"
else
    echo "❌ Git not found. Please install Git"
    exit 1
fi

# Clone repository
echo ""
echo "📥 Cloning repository..."
if [ -d "$INSTALL_DIR" ]; then
    echo "⚠️  Directory exists, updating..."
    cd "$INSTALL_DIR"
    git pull origin main
else
    mkdir -p "$HOME/Documents"
    git clone "$REPO_URL" "$INSTALL_DIR"
    cd "$INSTALL_DIR"
fi

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
pip3 install -q -r requirements.txt 2>&1 | grep -v "already satisfied" || true

# Test components
echo ""
echo "🧪 Testing components..."
python3 << 'EOF'
try:
    from consultancy_orchestrator import ConsultancyOrchestrator
    from vault_analyzer import VaultAnalyzer
    print("✅ All components working")
except Exception as e:
    print(f"❌ Component test failed: {e}")
    exit(1)
EOF

# Create Claude Skill
echo ""
echo "⚙️  Setting up Claude integration..."
mkdir -p "$HOME/.claude/skills"

cat << 'SKILLEOF' > "$HOME/.claude/skills/analyze-repo.md"
---
name: analyze-repo
description: Analyze GitHub/GitLab repository with multi-agent system
category: research
---

# Repository Analysis Skill

Usage: /analyze-repo <url>

Implementation:
```python
import sys
sys.path.insert(0, '$HOME/Documents/tech-consultancy-agency')
from consultancy_orchestrator import ConsultancyOrchestrator

url = args if isinstance(args, str) else args.get('url', '')
orchestrator = ConsultancyOrchestrator()
results = orchestrator.run_pipeline(url)

research = results['stages']['research']['findings']
print(f"⭐ Stars: {research['stars']}")
print(f"🔧 Tech: {', '.join(research['technology'][:5])}")
print(f"📝 Saved: {results['obsidian']['note_path']}")
```
SKILLEOF

echo "✅ Claude Skill installed"

# Summary
echo ""
echo "=" | tr -c '\n' '=' | head -c 60; echo ""
echo "✅ INSTALLATION COMPLETE!"
echo ""
echo "📍 Location: $INSTALL_DIR"
echo "📚 Vault: $(ls "$INSTALL_DIR/obsidian_vault"/*.md 2>/dev/null | wc -l | tr -d ' ') notes"
echo ""
echo "🎯 Usage in Claude Code:"
echo "   /analyze-repo https://github.com/owner/repo"
echo ""
echo "📖 Full docs: $INSTALL_DIR/REMOTE_SETUP.md"
echo ""
echo "🚀 Ready to use!"
