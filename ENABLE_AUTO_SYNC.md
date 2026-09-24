# Enable Automatic Vault Sync (5-minute intervals)

Sir, the automated sync is installed but needs **Full Disk Access** permission to run automatically.

---

## 🎯 OPTION 1: Grant Full Disk Access (Recommended - 2 minutes)

### **Steps**:

1. **Open System Settings**
   ```
   System Settings → Privacy & Security → Full Disk Access
   ```

2. **Click the lock icon** (bottom left) and authenticate

3. **Click the "+" button**

4. **Navigate to and add**:
   ```
   /bin/bash
   ```

5. **Enable the checkbox** next to `/bin/bash`

6. **Restart the launchd agent**:
   ```bash
   launchctl unload ~/Library/LaunchAgents/com.viseyyon.obsidian-sync.plist
   launchctl load ~/Library/LaunchAgents/com.viseyyon.obsidian-sync.plist
   ```

7. **Verify it's working** (wait 5 minutes, then):
   ```bash
   tail -10 ~/Documents/Cluade_clone/agency_consultancy/vault_sync.log
   ```

---

## 🎯 OPTION 2: Use Cron (Alternative - 3 minutes)

If you prefer not to grant Full Disk Access, use cron instead:

### **Steps**:

1. **Edit crontab**:
   ```bash
   crontab -e
   ```

2. **Add this line** (press `i` to insert):
   ```bash
   */5 * * * * /Users/manoharans/Documents/Cluade_clone/agency_consultancy/sync_vault.sh >> /Users/manoharans/Documents/Cluade_clone/agency_consultancy/vault_sync.log 2>&1
   ```

3. **Save and exit** (press `Esc`, type `:wq`, press Enter)

4. **Verify cron entry**:
   ```bash
   crontab -l
   ```

5. **Wait 5 minutes** and check the log:
   ```bash
   tail -10 ~/Documents/Cluade_clone/agency_consultancy/vault_sync.log
   ```

---

## 🎯 OPTION 3: Manual Sync (Instant)

Run sync manually whenever you want:

```bash
~/Documents/Cluade_clone/agency_consultancy/sync_vault.sh
```

---

## ✅ VERIFY SYNC IS WORKING

### **Check Sync Status**:
```bash
tail -f ~/Documents/Cluade_clone/agency_consultancy/vault_sync.log
```

### **Expected Output** (every 5 minutes):
```
[2026-09-25 01:08:00] Starting vault sync...
[2026-09-25 01:08:02] Syncing vault to repo...
[2026-09-25 01:08:03] Pushing to GitHub...
[2026-09-25 01:08:07] ✅ Sync complete!
[2026-09-25 01:08:07] ---
```

### **Check Last Sync**:
```bash
tail -5 ~/Documents/Cluade_clone/agency_consultancy/vault_sync.log
```

### **Check launchd Status** (Option 1 only):
```bash
launchctl list | grep obsidian
# Should show: <PID> 0 com.viseyyon.obsidian-sync
# 0 = success, 126 = permission denied
```

---

## 📊 WHAT GETS SYNCED

**Source**: `~/Documents/Obsidian Vault/10-knowledge`  
**Destination**: `~/Documents/Cluade_clone/agency_consultancy/obsidian_vault/`  
**Then**: Auto-pushed to GitHub → Streamlit Cloud

### **Included**:
- ✅ All markdown files (`.md`)
- ✅ Claude memory folder (`claude-memory/`)
- ✅ All subfolders
- ✅ Images and attachments

### **Excluded** (Security):
- ❌ `.git/` - Git metadata
- ❌ `.obsidian/` - Obsidian settings
- ❌ `.trash/` - Deleted files
- ❌ `claude-projects/` - Contains API keys

---

## 🔧 TROUBLESHOOTING

### **Issue: "Operation not permitted"**

**Solution**: Grant Full Disk Access (Option 1 above)

### **Issue: Sync not running every 5 minutes**

**Check**:
```bash
# For launchd (Option 1)
launchctl list | grep obsidian

# For cron (Option 2)
crontab -l
```

### **Issue: No new commits on GitHub**

**Manual test**:
```bash
# Run sync manually
~/Documents/Cluade_clone/agency_consultancy/sync_vault.sh

# Check if it worked
git -C ~/Documents/Cluade_clone/agency_consultancy log --oneline -5
```

### **Issue: Changes not appearing in Streamlit**

**Wait for**:
1. Sync to run (every 5 min)
2. GitHub commit (instant after sync)
3. Streamlit Cloud deploy (2-3 min after commit)

**Total**: ~8 minutes max from local change to live web UI

---

## 🎯 RECOMMENDATION

**Use Option 1** (Full Disk Access) because:
- ✅ Already installed and configured
- ✅ Runs as launchd daemon (more reliable)
- ✅ Better error handling
- ✅ Logs to dedicated files
- ✅ Auto-starts on boot

**Alternative**: Use Option 2 (cron) if you prefer not to grant Full Disk Access

**For testing**: Use Option 3 (manual) to verify sync works immediately

---

## 📋 CURRENT STATUS

**Sync Script**: ✅ Installed  
**launchd Agent**: ✅ Configured  
**Permission**: ⚠️  Needs Full Disk Access  
**Manual Sync**: ✅ Working (last run: 2026-09-25 01:03)  

**Action Required**: Grant Full Disk Access (Option 1) OR setup cron (Option 2)

---

**Sir, choose your preferred option and follow the steps above to enable automatic sync!** 🚀
