#!/bin/bash
# Obsidian Vault to GitHub Sync Script
# Syncs local vault → repo → GitHub every 5 minutes

VAULT_PATH="$HOME/Documents/Obsidian Vault/10-knowledge"
REPO_PATH="$HOME/Documents/Cluade_clone/agency_consultancy"
DEST_PATH="$REPO_PATH/obsidian_vault"
LOG_FILE="$REPO_PATH/vault_sync.log"

# Log start
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting vault sync..." >> "$LOG_FILE"

# Check if vault exists
if [ ! -d "$VAULT_PATH" ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: Vault not found at $VAULT_PATH" >> "$LOG_FILE"
    exit 1
fi

# Create destination if needed
mkdir -p "$DEST_PATH"

# Sync vault to repo using rsync (mirror)
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Syncing vault to repo..." >> "$LOG_FILE"
rsync -av --delete \
    --exclude='.git' \
    --exclude='.obsidian' \
    --exclude='.trash' \
    --exclude='claude-projects' \
    "$VAULT_PATH/" "$DEST_PATH/" >> "$LOG_FILE" 2>&1

SYNC_RESULT=$?
if [ $SYNC_RESULT -ne 0 ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: rsync failed with code $SYNC_RESULT" >> "$LOG_FILE"
    exit 1
fi

# Change to repo directory
cd "$REPO_PATH" || exit 1

# Git operations
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Committing changes..." >> "$LOG_FILE"

# Add vault changes
git add obsidian_vault/ >> "$LOG_FILE" 2>&1

# Check if there are changes
if git status --porcelain | grep -q '^'; then
    # Commit
    git commit -m "Auto-sync: Obsidian vault update $(date '+%Y-%m-%d %H:%M')" >> "$LOG_FILE" 2>&1

    # Push
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Pushing to GitHub..." >> "$LOG_FILE"
    git push origin main >> "$LOG_FILE" 2>&1

    if [ $? -eq 0 ]; then
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] ✅ Sync complete!" >> "$LOG_FILE"
    else
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] ⚠️  Push failed" >> "$LOG_FILE"
    fi
else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] No changes to sync" >> "$LOG_FILE"
fi

echo "[$(date '+%Y-%m-%d %H:%M:%S')] ---" >> "$LOG_FILE"
