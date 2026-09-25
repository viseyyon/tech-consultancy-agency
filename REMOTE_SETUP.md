# 🚀 REMOTE SETUP GUIDE
## Technology Consultancy Agency - New Claude Code Instance

---

## STEP 1: VERIFY PREREQUISITES

```bash
# Check Python (need 3.9+)
python3 --version

# Check Git
git --version

# Check pip
pip3 --version
```

**Expected output**:
```
Python 3.9.x or higher
git version 2.x.x
pip 21.x.x or higher
```

**If missing, install**:

**macOS**:
```bash
# Install Homebrew (if needed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python & Git
brew install python git
```

**Linux (Ubuntu/Debian)**:
```bash
sudo apt update
sudo apt install -y python3 python3-pip git
```

**Windows (WSL)**:
```bash
sudo apt update
sudo apt install -y python3 python3-pip git
```

---

## STEP 2: CLONE REPOSITORY

```bash
# Create directory
mkdir -p ~/Documents
cd ~/Documents

# Clone from GitHub
git clone https://github.com/viseyyon/tech-consultancy-agency.git

# Enter directory
cd tech-consultancy-agency

# Verify files
ls -la
```

**Expected files**:
- consultancy_orchestrator.py
- deep_research_agent.py
- obsidian_integrator.py
- vault_analyzer.py
- app.py
- requirements.txt
- obsidian_vault/ (directory with 495+ notes)

---

## STEP 3: INSTALL DEPENDENCIES

```bash
# Still in ~/Documents/tech-consultancy-agency

# Install Python packages
pip3 install -r requirements.txt

# Verify installation
python3 -c "import streamlit; print('✅ Streamlit installed')"
python3 -c "import bcrypt; print('✅ bcrypt installed')"
```

**Expected output**:
```
✅ Streamlit installed
✅ bcrypt installed
```

**If errors**, try:
```bash
pip3 install --user -r requirements.txt
```

---

## STEP 4: TEST COMPONENTS

```bash
# Test 1: Import components
python3 << 'EOF'
print("🧪 Testing components...")

try:
    from deep_research_agent import DeepResearchAgent
    print("✅ DeepResearchAgent - OK")
except Exception as e:
    print(f"❌ DeepResearchAgent - FAILED: {e}")

try:
    from obsidian_integrator import ObsidianIntegrator
    print("✅ ObsidianIntegrator - OK")
except Exception as e:
    print(f"❌ ObsidianIntegrator - FAILED: {e}")

try:
    from consultancy_orchestrator import ConsultancyOrchestrator
    print("✅ ConsultancyOrchestrator - OK")
except Exception as e:
    print(f"❌ ConsultancyOrchestrator - FAILED: {e}")

try:
    from vault_analyzer import VaultAnalyzer
    print("✅ VaultAnalyzer - OK")
except Exception as e:
    print(f"❌ VaultAnalyzer - FAILED: {e}")

print("\n✅ All components loaded successfully!")
EOF
```

**Expected output**:
```
🧪 Testing components...
✅ DeepResearchAgent - OK
✅ ObsidianIntegrator - OK
✅ ConsultancyOrchestrator - OK
✅ VaultAnalyzer - OK

✅ All components loaded successfully!
```

---

## STEP 5: RUN QUICK TEST

```bash
# Test full analysis pipeline
python3 << 'EOF'
import sys
sys.path.insert(0, '.')

from consultancy_orchestrator import ConsultancyOrchestrator

print("🔍 Running test analysis...")
print("=" * 60)

orchestrator = ConsultancyOrchestrator()

# Test URL validation
test_url = "https://github.com/bifrost0x/webssh"
valid, error = orchestrator.validate_input(test_url)

if valid:
    print(f"✅ URL validation: PASS")
    print(f"📊 Test URL: {test_url}")
    
    # Quick analysis
    print("\nRunning analysis (may take 10-30 seconds)...")
    results = orchestrator.run_pipeline(test_url)
    
    if results.get('status') == 'complete':
        research = results['stages']['research']['findings']
        print(f"\n✅ ANALYSIS COMPLETE!")
        print(f"⭐ Stars: {research.get('stars', 0)}")
        print(f"🍴 Forks: {research.get('forks', 0)}")
        print(f"🔧 Tech Stack: {', '.join(research.get('technology', [])[:5])}")
        print(f"📝 Features: {len(research.get('features', []))} extracted")
        print(f"\n✅ System is working correctly!")
    else:
        print(f"⚠️  Analysis completed with status: {results.get('status')}")
        print(f"Note: {results.get('obsidian', {})}")
else:
    print(f"❌ URL validation: FAILED - {error}")
EOF
```

**Expected output**:
```
🔍 Running test analysis...
============================================================
✅ URL validation: PASS
📊 Test URL: https://github.com/bifrost0x/webssh

Running analysis (may take 10-30 seconds)...

✅ ANALYSIS COMPLETE!
⭐ Stars: 200
🍴 Forks: 35
🔧 Tech Stack: docker, homelab, offline-first, openid-connect, passkeys
📝 Features: 5 extracted

✅ System is working correctly!
```

---

## STEP 6: INTEGRATE WITH CLAUDE CODE

### **Option A: Claude Skill** (Recommended - Easy)

```bash
# Create Claude directories
mkdir -p ~/.claude/skills

# Create skill file
cat << 'SKILLEOF' > ~/.claude/skills/analyze-repo.md
---
name: analyze-repo
description: Analyze GitHub/GitLab repository with multi-agent system
category: research
---

# Repository Analysis Skill

Analyzes GitHub or GitLab repositories using the Technology Consultancy Agency.

## Usage

\`/analyze-repo <url>\`

## Implementation

\`\`\`python
import sys
sys.path.insert(0, '$HOME/Documents/tech-consultancy-agency')

from consultancy_orchestrator import ConsultancyOrchestrator

# Get URL from args
url = args if isinstance(args, str) else args.get('url', '')

if not url:
    print("❌ Usage: /analyze-repo <github-url>")
    sys.exit(1)

# Run analysis
orchestrator = ConsultancyOrchestrator()
valid, error = orchestrator.validate_input(url)

if not valid:
    print(f"❌ Invalid URL: {error}")
    sys.exit(1)

print(f"🔍 Analyzing: {url}")
results = orchestrator.run_pipeline(url)

if results.get('status') != 'complete':
    print(f"❌ Analysis failed: {results.get('error')}")
    sys.exit(1)

# Display results
research = results['stages']['research']['findings']
print(f"\n✅ Analysis Complete!")
print(f"\n⭐ Stars: {research.get('stars', 0)}")
print(f"🍴 Forks: {research.get('forks', 0)}")
print(f"🎯 Purpose: {research.get('purpose', 'N/A')[:100]}...")
print(f"\n🔧 Technology ({len(research.get('technology', []))} items):")
for tech in research.get('technology', [])[:10]:
    print(f"   - {tech}")

print(f"\n✨ Features ({len(research.get('features', []))} items):")
for feat in research.get('features', [])[:5]:
    print(f"   - {feat[:80]}...")

# Note saved location
obsidian = results.get('obsidian', {})
if obsidian.get('success'):
    print(f"\n📝 Saved to: {obsidian.get('note_path')}")
else:
    print(f"\n📝 Note: {obsidian}")

print(f"\n📋 Report: {results.get('report_path')}")
\`\`\`

## Examples

\`\`\`
/analyze-repo https://github.com/fastapi/fastapi
/analyze-repo https://github.com/vercel/next.js
\`\`\`
SKILLEOF

echo "✅ Claude Skill created: ~/.claude/skills/analyze-repo.md"
```

### **Option B: Add to CLAUDE.md** (Alternative)

```bash
# Create or append to CLAUDE.md
cat << 'CLAUDEEOF' >> ~/.claude/CLAUDE.md

## Technology Consultancy Agency

**Location**: \`~/Documents/tech-consultancy-agency/\`

**Description**: Multi-agent system for analyzing GitHub/GitLab repositories

**Components**:
- Deep Research Agent (GitHub scraping, metadata extraction)
- Technology Assessor (tech stack evaluation)
- Business Value Analyzer (ROI analysis)
- Integration Strategist (integration planning)
- Report Synthesizer (final reports + Obsidian notes)

**Usage**:
\`\`\`bash
cd ~/Documents/tech-consultancy-agency
./consultancy_orchestrator.py <github-url>
\`\`\`

**Vault**: 495+ repository analyses in \`obsidian_vault/\`

**Search vault**:
\`\`\`python
from vault_analyzer import VaultAnalyzer
analyzer = VaultAnalyzer('obsidian_vault')
results = analyzer.search_notes('docker kubernetes')
\`\`\`

**Web UI**: https://tech-consultancy-agency.streamlit.app
CLAUDEEOF

echo "✅ Added to ~/.claude/CLAUDE.md"
```

---

## STEP 7: VERIFY INTEGRATION

```bash
# Check skill exists
ls -lh ~/.claude/skills/analyze-repo.md

# Check CLAUDE.md
tail -20 ~/.claude/CLAUDE.md

# Check vault
ls obsidian_vault/*.md | wc -l
```

**Expected output**:
```
-rw-r--r-- ... ~/.claude/skills/analyze-repo.md
(Shows CLAUDE.md content)
495 (number of vault notes)
```

---

## STEP 8: FIRST ANALYSIS TEST

### **In Claude Code, use**:

```
You: /analyze-repo https://github.com/anthropics/anthropic-sdk-python

Claude: [Runs analysis]
Shows: Stars, forks, tech stack, features
Saves to: obsidian_vault/anthropic-sdk-python.md
```

### **Or via command line**:

```bash
cd ~/Documents/tech-consultancy-agency
./consultancy_orchestrator.py https://github.com/anthropics/anthropic-sdk-python
```

---

## ✅ VERIFICATION CHECKLIST

```bash
# Run complete verification
cat << 'VERIFYEOF' > /tmp/verify.sh
#!/bin/bash
echo "🔍 VERIFICATION CHECKLIST"
echo "=" | tr -c '\n' '=' | head -c 60; echo ""

# 1. Python
echo ""
echo "1️⃣ Python:"
python3 --version | grep -q "3\.[9-9]\|3\.1[0-9]" && echo "   ✅ Python 3.9+" || echo "   ❌ Python too old"

# 2. Repository
echo ""
echo "2️⃣ Repository:"
if [ -d "$HOME/Documents/tech-consultancy-agency" ]; then
    echo "   ✅ Repository cloned"
    cd "$HOME/Documents/tech-consultancy-agency"
    COUNT=$(ls obsidian_vault/*.md 2>/dev/null | wc -l | tr -d ' ')
    echo "   ✅ Vault notes: $COUNT"
else
    echo "   ❌ Repository not found"
fi

# 3. Dependencies
echo ""
echo "3️⃣ Dependencies:"
python3 -c "import streamlit" 2>/dev/null && echo "   ✅ streamlit" || echo "   ❌ streamlit missing"
python3 -c "import bcrypt" 2>/dev/null && echo "   ✅ bcrypt" || echo "   ❌ bcrypt missing"

# 4. Components
echo ""
echo "4️⃣ Components:"
cd "$HOME/Documents/tech-consultancy-agency" 2>/dev/null && \
python3 -c "from consultancy_orchestrator import ConsultancyOrchestrator; print('   ✅ Orchestrator')" 2>/dev/null || \
echo "   ❌ Orchestrator failed"

# 5. Claude Integration
echo ""
echo "5️⃣ Claude Integration:"
if [ -f "$HOME/.claude/skills/analyze-repo.md" ]; then
    echo "   ✅ Claude Skill installed"
else
    echo "   ⚠️  Claude Skill not installed (optional)"
fi

echo ""
echo "=" | tr -c '\n' '=' | head -c 60; echo ""
echo "✅ VERIFICATION COMPLETE!"
VERIFYEOF

bash /tmp/verify.sh
```

---

## 🎯 QUICK REFERENCE

### **Analyze Repository**:
```bash
cd ~/Documents/tech-consultancy-agency
./consultancy_orchestrator.py <github-url>
```

### **Search Vault**:
```bash
cd ~/Documents/tech-consultancy-agency
grep -r "keyword" obsidian_vault/*.md
```

### **View Analysis**:
```bash
cat obsidian_vault/repo-name.md
```

### **In Claude Code**:
```
/analyze-repo <github-url>
```

---

## 🆘 TROUBLESHOOTING

### **Issue: "Module not found"**

```bash
# Fix: Install dependencies
cd ~/Documents/tech-consultancy-agency
pip3 install --user -r requirements.txt
```

### **Issue: "Permission denied"**

```bash
# Fix: Make scripts executable
chmod +x consultancy_orchestrator.py
chmod +x sync_vault.sh
```

### **Issue: "Cannot fetch GitHub"**

- Check internet connection
- Verify URL is correct (https://github.com/owner/repo)
- GitHub might be rate-limiting (wait 1 minute)

### **Issue: "Claude Skill not working"**

```bash
# Verify skill file
cat ~/.claude/skills/analyze-repo.md

# Check file exists
ls -la ~/.claude/skills/

# Restart Claude Code
```

### **Issue: "Vault not found"**

```bash
# Verify vault exists
ls ~/Documents/tech-consultancy-agency/obsidian_vault/

# Re-clone if needed
cd ~/Documents
rm -rf tech-consultancy-agency
git clone https://github.com/viseyyon/tech-consultancy-agency.git
```

---

## 📊 SETUP TIME

- **Prerequisites**: 2-5 minutes (if installing Python/Git)
- **Clone & Install**: 2-3 minutes
- **Testing**: 1-2 minutes
- **Integration**: 1-2 minutes

**Total**: ~10 minutes for complete setup

---

## 🚀 NEXT STEPS

1. ✅ Setup complete - All components working
2. Try your first analysis: `/analyze-repo https://github.com/anthropics/anthropic-sdk-python`
3. Search the vault: Browse `obsidian_vault/` for 495+ existing analyses
4. Read docs: `INTEGRATION_GUIDE.md` for advanced features

---

## 📚 ADDITIONAL RESOURCES

- **Full Integration Guide**: `INTEGRATION_GUIDE.md`
- **Web UI**: https://tech-consultancy-agency.streamlit.app
- **GitHub**: https://github.com/viseyyon/tech-consultancy-agency
- **Vault**: 495+ analyses in `obsidian_vault/`

---

**Setup complete! Start analyzing repositories.** 🎉
