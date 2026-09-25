#!/bin/bash
# setup_integration.sh - Quick integration setup for new Claude instances

set -e

echo "🚀 Technology Consultancy Agency - Integration Setup"
echo "=" | tr -c '\n' '=' | head -c 60; echo ""

# Variables
CONSULTANCY_DIR="$HOME/Documents/tech-consultancy-agency"
VAULT_DIR="$CONSULTANCY_DIR/obsidian_vault"
CLAUDE_DIR="$HOME/.claude"
OBSIDIAN_VAULT="$HOME/Documents/Obsidian Vault"

echo ""
echo "📍 Checking installation..."

# Check if in consultancy directory
if [ ! -f "consultancy_orchestrator.py" ]; then
    echo "❌ Not in consultancy directory"
    echo "Please run from: ~/Documents/tech-consultancy-agency/"
    exit 1
fi

echo "✅ In consultancy directory"

# Check Python dependencies
echo ""
echo "📦 Checking dependencies..."
python3 -c "import streamlit; import bcrypt" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "✅ Python dependencies installed"
else
    echo "⚠️  Installing dependencies..."
    pip3 install -r requirements.txt
fi

# Test components
echo ""
echo "🧪 Testing components..."

python3 << 'EOF'
try:
    from deep_research_agent import DeepResearchAgent
    from obsidian_integrator import ObsidianIntegrator
    from consultancy_orchestrator import ConsultancyOrchestrator
    print("✅ All components import successfully")
except Exception as e:
    print(f"❌ Import failed: {e}")
    exit(1)
EOF

# Create Claude directories
echo ""
echo "📁 Setting up Claude directories..."
mkdir -p "$CLAUDE_DIR/skills"
mkdir -p "$HOME/mcp-servers/tech-consultancy"

# Option 1: Claude Skill
echo ""
echo "1️⃣ Setting up Claude Skill..."
cat << 'SKILL_EOF' > "$CLAUDE_DIR/skills/analyze-repo.md"
---
name: analyze-repo
description: Analyze GitHub/GitLab repository with multi-agent system
category: research
---

# Repository Analysis

Usage: /analyze-repo <github-url>

Implementation:
```python
import sys
sys.path.insert(0, '$HOME/Documents/tech-consultancy-agency')
from consultancy_orchestrator import ConsultancyOrchestrator

url = args if isinstance(args, str) else args.get('url', '')
orchestrator = ConsultancyOrchestrator()
results = orchestrator.run_pipeline(url)

# Display results
research = results['stages']['research']['findings']
print(f"⭐ Stars: {research['stars']}")
print(f"🔧 Tech: {', '.join(research['technology'][:5])}")
print(f"📝 Saved to: {results['obsidian']['note_path']}")
```
SKILL_EOF

echo "✅ Claude Skill created: ~/.claude/skills/analyze-repo.md"

# Option 2: Symlink
echo ""
echo "2️⃣ Setting up vault symlink..."
if [ -d "$OBSIDIAN_VAULT" ]; then
    if [ ! -L "$OBSIDIAN_VAULT/99-tech-consultancy" ]; then
        ln -s "$VAULT_DIR" "$OBSIDIAN_VAULT/99-tech-consultancy"
        echo "✅ Symlink created: ~/Documents/Obsidian Vault/99-tech-consultancy"
    else
        echo "✅ Symlink already exists"
    fi
else
    echo "⚠️  Main Obsidian vault not found, skipping symlink"
fi

# Option 3: CLAUDE.md entry
echo ""
echo "3️⃣ Updating CLAUDE.md..."
if [ -f "$CLAUDE_DIR/CLAUDE.md" ]; then
    if ! grep -q "Technology Consultancy Agency" "$CLAUDE_DIR/CLAUDE.md"; then
        cat << 'CLAUDE_EOF' >> "$CLAUDE_DIR/CLAUDE.md"

## Technology Consultancy Agency

**Location**: `~/Documents/tech-consultancy-agency/`
**Vault**: `~/Documents/Obsidian Vault/99-tech-consultancy/` (symlink)

**Tools**:
- Orchestrator: `./consultancy_orchestrator.py <url>`
- Vault search: `vault_analyzer.py`
- Web UI: https://tech-consultancy-agency.streamlit.app

**Usage**:
```bash
cd ~/Documents/tech-consultancy-agency
./consultancy_orchestrator.py https://github.com/owner/repo
```

**Vault**: 495+ repository analyses (stars, forks, tech stack, features)
CLAUDE_EOF
        echo "✅ Added to CLAUDE.md"
    else
        echo "✅ Already in CLAUDE.md"
    fi
else
    echo "⚠️  CLAUDE.md not found, skipping"
fi

# Summary
echo ""
echo "=" | tr -c '\n' '=' | head -c 60; echo ""
echo "✅ INTEGRATION COMPLETE!"
echo ""
echo "📋 What was set up:"
echo "   ✅ Claude Skill: ~/.claude/skills/analyze-repo.md"
echo "   ✅ Vault symlink: ~/Documents/Obsidian Vault/99-tech-consultancy"
echo "   ✅ CLAUDE.md: Updated with consultancy info"
echo ""
echo "🎯 Usage in Claude Code:"
echo "   /analyze-repo https://github.com/owner/repo"
echo ""
echo "   Or: 'Analyze https://github.com/owner/repo using consultancy'"
echo ""
echo "📚 Full docs: INTEGRATION_GUIDE.md"
echo ""
echo "🚀 Ready to use!"
