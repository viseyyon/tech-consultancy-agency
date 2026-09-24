# Obsidian Vault (Cloud Deployment)

This folder contains a subset of the Obsidian vault for cloud deployment on Streamlit.

## For Cloud Deployment

When deployed to Streamlit Cloud, the app reads notes from this `obsidian_vault/` folder since it cannot access the local `~/Documents/Obsidian Vault/` directory.

## For Local Development

When running locally, the app automatically detects and uses the full vault at:
- `~/Documents/Obsidian Vault/10-knowledge` (644 notes)

## Sync Strategy

**Option 1: Manual Sync** (Current)
- Copy important notes to this folder
- Commit and push to GitHub
- Streamlit Cloud displays them

**Option 2: Automated Sync** (Recommended)
- Set up Obsidian Git plugin
- Configure to sync this subfolder
- Auto-commits new notes to GitHub
- Streamlit Cloud auto-updates

## Current Contents

Sample notes for demonstration:
- `anthropic-sdk-python.md` - Repository analysis example
- `Repository Index.md` - Master index

## Adding More Notes

To add more notes to cloud deployment:

```bash
# Copy notes from main vault
cp ~/Documents/Obsidian\ Vault/10-knowledge/*.md ./obsidian_vault/

# Commit and push
git add obsidian_vault/
git commit -m "Update vault notes for cloud"
git push origin main
```

Streamlit Cloud will auto-deploy with updated notes!
