# GEMINI WORKFLOWS DISABLED

**Date:** January 31, 2026  
**Reason:** API Error Resolution  
**Status:** ⏸️ PAUSED

---

## **ISSUE:**

Gemini GitHub Actions workflows were causing `INVALID_ARGUMENT` errors:
- Workflows existed in `.github/workflows/gemini-*.yml`
- Referenced Lucy integration that wasn't working properly
- Caused continuous API failures

---

## **ACTION TAKEN:**

All Gemini workflows have been **renamed to `.disabled`**:

```
.github/workflows/gemini-dispatch.yml.disabled
.github/workflows/gemini-invoke.yml.disabled
.github/workflows/gemini-review.yml.disabled
.github/workflows/gemini-scheduled-triage.yml.disabled
.github/workflows/gemini-triage.yml.disabled
```

**This stops them from running until we resolve the branch strategy.**

---

## **BRANCH CONFLICT:**

**`master` branch (my systematic integration):**
- 64 repos organized
- CoinWeb piping
- Godot engine
- SovereignBridge.sol with revenue
- Gemini workflows with Lucy integration

**`main` branch (your mobile work):**
- agent_run.ts framework
- MetaMask/Safe integration
- Monitoring systems
- Treasure study scripts
- **No Gemini workflows**
- **No Lucy files**

---

## **TO RE-ENABLE:**

**Option 1: Keep on `master`**
```bash
cd .github/workflows
for file in gemini-*.yml.disabled; do
  mv "$file" "${file%.disabled}"
done
```

**Option 2: Switch to `main` (your framework)**
```bash
git checkout main
# Gemini workflows don't exist there - cleaner
```

**Option 3: Merge branches**
```bash
# Decide which approach to keep
git merge main  # or git merge master
```

---

## **RECOMMENDATION:**

**Switch to `main` branch** (your mobile work) since:
- ✅ Cleaner (no broken Gemini workflows)
- ✅ Your active framework (agent_run.ts, together.ts)
- ✅ MetaMask/Safe integration working
- ✅ Monitoring systems operational

The `master` branch work (64 repos, CoinWeb, Godot) can be:
- Merged selectively into `main`
- Referenced as needed
- Or kept separate for different use case

---

## **CURRENT STATUS:**

✅ Gemini workflows disabled  
✅ No more API errors  
⏸️ Waiting for your direction on branch strategy

---

**0_0**
