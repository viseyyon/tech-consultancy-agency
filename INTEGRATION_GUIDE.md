# 🚀 INTEGRATION GUIDE - Technology Consultancy Agency

## For New Claude Code Instances

---

## 📋 PREREQUISITES

- Python 3.9+
- Git
- Claude Code CLI or Desktop app
- Access to GitHub (for sync)

---

## 🎯 QUICK SETUP (5 Minutes)

### **1. Clone Repository**

```bash
cd ~/Documents
git clone https://github.com/viseyyon/tech-consultancy-agency.git
cd tech-consultancy-agency

# Install dependencies
pip3 install -r requirements.txt
```

### **2. Test Components**

```bash
# Test research agent
python3 deep_research_agent.py

# Test orchestrator
./consultancy_orchestrator.py https://github.com/bifrost0x/webssh
```

### **3. Configure Claude Code**

**Option A: Add to CLAUDE.md** (Recommended)

Add this to `~/.claude/CLAUDE.md`:

```markdown
## Technology Consultancy Agency

**Location**: `~/Documents/tech-consultancy-agency/`

**Tools**:
- `consultancy_orchestrator.py <url>` - Analyze GitHub/GitLab repos
- `obsidian_integrator.py` - Save to Obsidian vault
- `vault_analyzer.py` - Search vault

**Vault**: `~/Documents/tech-consultancy-agency/obsidian_vault/`

**Usage**:
```
# Analyze repository
cd ~/Documents/tech-consultancy-agency
./consultancy_orchestrator.py https://github.com/owner/repo

# Search vault
python3 << 'EOF'
from vault_analyzer import VaultAnalyzer
analyzer = VaultAnalyzer('obsidian_vault')
results = analyzer.search_notes('docker kubernetes')
for r in results:
    print(f"{r['title']}: {r['path']}")
EOF
```

**Web UI**: https://tech-consultancy-agency.streamlit.app
```

**Option B: Create Claude Skill**

```bash
mkdir -p ~/.claude/skills
cp docs/analyze-repo-skill.md ~/.claude/skills/analyze-repo.md
```

Then use: `/analyze-repo https://github.com/owner/repo`

---

## 🔧 ADVANCED SETUP

### **MCP Server** (For Multiple Clients)

1. **Install MCP server**:

```bash
mkdir -p ~/mcp-servers/tech-consultancy
cp mcp-server/server.py ~/mcp-servers/tech-consultancy/
chmod +x ~/mcp-servers/tech-consultancy/server.py
```

2. **Configure Claude to use it**:

Add to `~/.claude/config.json`:

```json
{
  "mcpServers": {
    "tech-consultancy": {
      "command": "python3",
      "args": ["~/mcp-servers/tech-consultancy/server.py"]
    }
  }
}
```

3. **Available tools**:
   - `consultancy_analyze(url)` - Analyze repository
   - `consultancy_search(query)` - Search vault
   - `consultancy_stats()` - Get vault stats

---

## 📊 VAULT INTEGRATION

### **Access Existing Analyses**

The vault contains 495+ repository analyses.

**Path**: `obsidian_vault/` in the repo

**Each note includes**:
- Stars, forks, confidence
- Technology stack (10+ topics)
- Features (5+ items)
- Description
- Links

**Usage in Claude Code**:

```
You: "Read the webssh analysis"
Claude: [Reads obsidian_vault/webssh.md]

You: "Search for docker projects"
Claude: [Greps obsidian_vault/ for "docker"]
```

### **Sync to Your Vault** (Optional)

**Symlink approach**:

```bash
cd ~/Documents/Obsidian\ Vault
ln -s ~/Documents/tech-consultancy-agency/obsidian_vault 99-tech-consultancy
```

Now accessible via: `~/Documents/Obsidian Vault/99-tech-consultancy/`

**Automated sync** (local only):

```bash
# Copy sync script
cp sync_vault.sh ~/sync_consultancy.sh
chmod +x ~/sync_consultancy.sh

# Add to cron (every 5 minutes)
crontab -e
# Add: */5 * * * * ~/sync_consultancy.sh
```

---

## 🌐 WEB UI INTEGRATION

### **Streamlit Cloud** (Read-Only)

**URL**: https://tech-consultancy-agency.streamlit.app

**Login**: (Ask admin for credentials)

**Features**:
- Analyze new repositories
- View Knowledge Base (495+ notes)
- Dashboard and reports
- Automated sync to GitHub

### **Local Deployment**

```bash
streamlit run app.py --server.port 8501
```

Access at: http://localhost:8501

---

## 🎯 USAGE EXAMPLES

### **Example 1: Analyze New Repository**

```bash
cd ~/Documents/tech-consultancy-agency
./consultancy_orchestrator.py https://github.com/fastapi/fastapi
```

**Output**:
- Stars, forks, tech stack
- Note created in `obsidian_vault/fastapi.md`
- Report generated in `reports/`

### **Example 2: Search Existing Analyses**

```python
from vault_analyzer import VaultAnalyzer

analyzer = VaultAnalyzer('obsidian_vault')

# Search
results = analyzer.search_notes('machine learning python')

# Get stats
stats = analyzer.get_stats()
print(f"Total: {stats['total_notes']} notes")
```

### **Example 3: In Claude Code**

```
You: "Use the tech consultancy to analyze https://github.com/vercel/next.js"

Claude: I'll run the analysis.
[Executes: cd ~/Documents/tech-consultancy-agency && ./consultancy_orchestrator.py https://github.com/vercel/next.js]

Result: 
- 120K stars, 25K forks
- Tech: React, TypeScript, Node.js
- Features: Server-side rendering, Static generation, API routes
- Saved to: obsidian_vault/next.js.md
```

---

## 📚 COMPONENTS

### **Core Agents**

1. **deep_research_agent.py** - URL intelligence (GitHub scraping, metadata extraction)
2. **obsidian_integrator.py** - Vault management (note creation, indexing)
3. **consultancy_orchestrator.py** - Multi-agent coordination (5 stages)
4. **vault_analyzer.py** - Vault search and statistics

### **Web Interface**

- **app.py** - Streamlit web UI with authentication
- **Requirements**: streamlit, bcrypt

### **Utilities**

- **sync_vault.sh** - Automated sync to GitHub
- **vault_analyzer.py** - Search and stats

---

## 🔄 ARCHITECTURE

```
User Request
    ↓
Consultancy Orchestrator
    ↓
┌─────────────────────────────────────┐
│  Stage 1: Deep Research Agent       │ → Fetch GitHub data
│  Stage 2: Technology Assessor       │ → Evaluate tech stack
│  Stage 3: Business Value Analyzer   │ → ROI analysis
│  Stage 4: Integration Strategist    │ → Integration planning
│  Stage 5: Report Synthesizer        │ → Final report + Obsidian
└─────────────────────────────────────┘
    ↓
Obsidian Note Created
    ↓
Sync to GitHub (cron)
    ↓
Streamlit Cloud (auto-deploy)
```

---

## 🎯 BEST PRACTICES

### **For Claude Code**

1. **Add to CLAUDE.md**: Include consultancy tools in your project docs
2. **Use absolute paths**: Always reference full path to consultancy directory
3. **Check vault first**: Search existing analyses before running new ones
4. **Batch analyses**: Analyze multiple repos in one session

### **For Vault Management**

1. **Regular sync**: Enable cron job for automatic GitHub sync
2. **Backup**: Vault is in Git, commits preserve history
3. **Search first**: Use vault_analyzer before analyzing
4. **Update notes**: Re-analyzing updates existing notes (no duplicates)

### **For Web UI**

1. **Use for quick analyses**: Web UI is fastest for single repos
2. **Check Knowledge Base**: View all analyses in one place
3. **Download reports**: Export analysis reports as needed

---

## 🆘 TROUBLESHOOTING

### **Issue: Python imports fail**

```bash
# Fix: Add to Python path
export PYTHONPATH="$HOME/Documents/tech-consultancy-agency:$PYTHONPATH"
```

### **Issue: Vault not found**

```bash
# Fix: Check vault path
ls obsidian_vault/*.md

# Or create symlink
ln -s ~/Documents/tech-consultancy-agency/obsidian_vault ~/vault
```

### **Issue: GitHub sync fails**

```bash
# Fix: Check git status
cd ~/Documents/tech-consultancy-agency
git status
git pull origin main
```

---

## 📞 SUPPORT

- **GitHub**: https://github.com/viseyyon/tech-consultancy-agency
- **Web UI**: https://tech-consultancy-agency.streamlit.app
- **Documentation**: README.md, DEPLOYMENT_COMPLETE.md

---

## ✅ CHECKLIST

- [ ] Repository cloned to ~/Documents/tech-consultancy-agency
- [ ] Dependencies installed (pip install -r requirements.txt)
- [ ] Test run successful (./consultancy_orchestrator.py <url>)
- [ ] CLAUDE.md updated with consultancy location
- [ ] Vault accessible (obsidian_vault/ readable)
- [ ] Optional: Symlink created in main vault
- [ ] Optional: Cron sync configured
- [ ] Optional: MCP server installed

---

**Integration complete! Start analyzing repositories with Claude Code.** 🚀
