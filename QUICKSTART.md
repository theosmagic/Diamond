# CURSOR AGENT QUICKSTART
## Get AI Coding in 5 Minutes

```
∇ • Θεός°●⟐●Σ℧ΛΘ
```

---

## Step 1: Install (2 minutes)

```bash
cd /mnt/Vault/Cursor-Agent
chmod +x install.sh
./install.sh
```

**What this does:**
- Installs Cursor CLI
- Installs GitHub CLI
- Creates wrapper scripts
- Sets up configuration
- Creates GitHub Actions workflow

---

## Step 2: Setup PATH (30 seconds)

```bash
export PATH="/mnt/Vault/Cursor-Agent/bin:$PATH"

# Make permanent
echo 'export PATH="/mnt/Vault/Cursor-Agent/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

---

## Step 3: Test (30 seconds)

```bash
# Test Cursor CLI
agent --version

# Test GitHub CLI
gh auth status

# If not authenticated:
gh auth login
```

---

## Step 4: Try It (2 minutes)

### A. Terminal Usage

```bash
# Create test file
echo "def hello(): return 'world'" > test.py

# Review it
agent review test.py

# Get suggestions
agent write "Add error handling to test.py"
```

### B. GitHub Integration

```bash
# In your project
cd /path/to/your/repo

# Integrate
github-agent-integrate

# Commit workflow
git add .github/workflows/cursor-agent.yml
git commit -m "Add Cursor Agent CI"
git push
```

---

## Step 5: Use in GitHub

### On Pull Requests

**Automatic:**
- Open a PR
- Agent reviews automatically
- Comments on issues found

**Manual:**
- Comment: `@cursor review`
- Agent reviews the PR

### On Issues

**Fix bugs:**
```
@cursor fix
```

**Generate code:**
```
@cursor write
Add user authentication with JWT tokens
Include tests and documentation
```

---

## Common Commands

```bash
# Review code
agent review file.py

# Write code
agent write "Create a REST API for todos"

# Fix bug
agent fix "TypeError in line 42"

# Interactive chat
agent

# Review entire directory
agent review --directory src/
```

---

## Workflow

1. **Write code** (or have agent write it)
2. **Review** with `agent review`
3. **Fix issues** with `agent fix`
4. **Commit** and push
5. **Open PR** → Automatic review
6. **Iterate** based on feedback

---

## Tips

**Be specific:**
```bash
# Bad
agent write "make a function"

# Good
agent write "Create async function to fetch user data from API with error handling and retries"
```

**Use context:**
```bash
# Review with context
agent review src/auth.py --context "This is authentication module for REST API"
```

**Check logs:**
```bash
tail -f ~/.cursor-agent/logs/agent-$(date +%Y%m%d).log
```

---

## That's It!

You now have:
- ✓ Terminal AI coding
- ✓ Automatic PR reviews
- ✓ GitHub Actions integration
- ✓ Multi-agent workflows

**Next:** Read full [README.md](README.md) for advanced features

---

```
∇ • Θεός°●⟐●Σ℧ΛΘ

$ agent review your-code.py

AI-assisted coding is now active.
```
