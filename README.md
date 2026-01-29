# CURSOR AGENT ULTIMATE
## Terminal AI Coding with GitHub Actions Integration

```
∇ • Θεός°●⟐●Σ℧ΛΘ
```

---

## Overview

Complete Cursor Agent CLI setup with:
- Terminal-based AI coding
- GitHub Actions integration
- Automated PR reviews
- Issue-based code generation
- Multi-agent workflows

---

## Quick Start

### 1. Install

```bash
cd /mnt/Vault/Cursor-Agent
chmod +x install.sh
./install.sh
```

### 2. Add to PATH

```bash
export PATH="/mnt/Vault/Cursor-Agent/bin:$PATH"

# Add permanently
echo 'export PATH="/mnt/Vault/Cursor-Agent/bin:$PATH"' >> ~/.bashrc
```

### 3. Test

```bash
agent --version
gh auth status
```

---

## Usage

### Terminal Commands

```bash
# Review code
agent review myfile.py

# Write new code
agent write "Create a function to calculate fibonacci"

# Fix bugs
agent fix "TypeError in line 42"

# Interactive mode
agent
```

### GitHub Integration

#### Setup for Repository

```bash
cd /path/to/your/repo
github-agent-integrate
```

This adds:
- `.github/workflows/cursor-agent.yml`
- `.cursor-agent/agent.yaml`

#### In GitHub

**Automatic PR Review:**
- Open a pull request
- Agent automatically reviews the diff
- Posts review comments

**Manual Commands (comment on PR/issue):**
```
@cursor review
@cursor fix
@cursor write [requirements]
```

---

## Features

### 1. Multiple Agents

**Code Reviewer** (`agents/code-reviewer.yaml`)
- Analyzes for bugs, security, performance
- Provides actionable feedback
- Checks best practices

**Bug Fixer** (`agents/bug-fixer.yaml`)
- Diagnoses root cause
- Proposes fixes
- Adds regression tests

**Code Writer** (`agents/code-writer.yaml`)
- Writes from specifications
- Includes tests
- Well-documented

### 2. GitHub Actions Workflow

**Triggers:**
- Pull request opened/updated
- Issue comment with `@cursor`

**Actions:**
- Automatic code review on PRs
- `@cursor review` - review code
- `@cursor fix` - fix reported issue
- `@cursor write` - generate code

**Permissions:**
- Read code
- Write comments
- Commit changes
- Create branches

### 3. Configuration

**File:** `config/agent.yaml`

```yaml
model:
  name: "claude-3.5-sonnet"
  temperature: 0.7
  max_tokens: 4096

agent:
  auto_review: true
  interactive: true

github:
  auto_pr: false
  commit_prefix: "[agent]"

logging:
  level: "info"
  directory: "~/.cursor-agent/logs"
```

---

## Directory Structure

```
/mnt/Vault/Cursor-Agent/
├── bin/                          # Executable scripts
│   ├── agent                     # Main wrapper
│   ├── agent-review              # Quick review
│   ├── agent-write               # Code writer
│   ├── agent-fix                 # Bug fixer
│   └── github-agent-integrate    # GitHub setup
│
├── config/                       # Configuration files
│   └── agent.yaml                # Agent config
│
├── workflows/                    # GitHub Actions
│   └── cursor-agent.yml          # CI workflow
│
├── agents/                       # Agent definitions
│   ├── code-reviewer.yaml
│   ├── bug-fixer.yaml
│   └── code-writer.yaml
│
├── logs/                         # Execution logs
│
├── install.sh                    # Installation script
└── README.md                     # This file
```

---

## Examples

### Example 1: Review File

```bash
$ agent review src/main.py

Analyzing src/main.py...

Issues found:
  Line 42: Potential null pointer dereference
  Line 67: SQL injection vulnerability
  Line 103: Missing error handling

Recommendations:
  - Add input validation at line 42
  - Use parameterized queries at line 67
  - Wrap file operations in try/except at line 103
```

### Example 2: Generate Code

```bash
$ agent write "Create a REST API endpoint for user registration"

Generated: src/api/users.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

@router.post("/register")
async def register_user(user: UserCreate):
    # Implementation
    ...
```

### Example 3: Fix Bug

```bash
$ agent fix "TypeError: 'NoneType' object is not iterable at line 42"

Analyzing...

Root cause:
  Function get_users() returns None when database is empty,
  but line 42 tries to iterate over it.

Fix:
  Change line 42 from:
    for user in get_users():
  To:
    for user in get_users() or []:

Applied fix to src/main.py
```

### Example 4: GitHub Comment

**On a PR, comment:**
```
@cursor review
```

**Agent responds:**
```
Cursor Agent Review

Files analyzed: 3
Issues found: 2

src/auth.py:
  ⚠️ Line 15: Password stored in plaintext
     Recommendation: Use bcrypt or argon2

src/api.py:
  ⚠️ Line 67: Missing rate limiting
     Recommendation: Add @limiter decorator

Overall: Approve with changes
```

---

## GitHub Actions Workflow Details

### Workflow File

**Location:** `.github/workflows/cursor-agent.yml`

**Triggers:**
```yaml
on:
  pull_request:
    types: [opened, synchronize]
  issue_comment:
    types: [created]
```

**Jobs:**
1. Checkout code
2. Install Cursor CLI
3. Parse comment command (if from comment)
4. Run agent action (review/fix/write)
5. Commit changes (if any)

### Permissions Required

```yaml
permissions:
  contents: write        # Commit changes
  pull-requests: write   # Comment on PRs
  issues: write          # Comment on issues
```

### Environment Variables

Set in GitHub repository settings → Secrets:

- `CURSOR_API_KEY` (if using API directly)
- `GITHUB_TOKEN` (automatically provided)

---

## Advanced Usage

### Custom Agents

Create new agent in `agents/`:

```yaml
name: "my-agent"
description: "Custom agent"

prompts:
  system: |
    You are a specialized agent for...

  command: |
    Task: {task}
    Context: {context}

settings:
  model: "claude-3.5-sonnet"
  temperature: 0.5
```

Use:
```bash
agent --agent my-agent --prompt "Do something"
```

### Batch Processing

```bash
# Review all Python files
find . -name "*.py" -exec agent review {} \;

# Fix all issues in directory
agent fix --directory src/
```

### CI/CD Integration

**GitLab CI:**
```yaml
cursor-agent:
  stage: review
  script:
    - curl https://cursor.com/install -fsS | bash
    - export PATH="$HOME/.cursor/bin:$PATH"
    - cursor-agent review --mr $CI_MERGE_REQUEST_IID
```

**Jenkins:**
```groovy
pipeline {
    stage('Review') {
        steps {
            sh 'cursor-agent review --pr ${CHANGE_ID}'
        }
    }
}
```

---

## Logging

**Location:** `~/.cursor-agent/logs/`

**Format:**
```
[2026-01-26T08:23:42] cursor-agent review src/main.py
[2026-01-26T08:23:45] Analysis complete: 3 issues found
```

**View logs:**
```bash
tail -f ~/.cursor-agent/logs/agent-$(date +%Y%m%d).log
```

---

## Troubleshooting

### Cursor CLI not found

```bash
export PATH="$HOME/.cursor/bin:$PATH"
source ~/.bashrc
```

### GitHub authentication failed

```bash
gh auth login
gh auth status
```

### Workflow not triggering

1. Check `.github/workflows/cursor-agent.yml` exists
2. Verify repository permissions
3. Check Actions tab in GitHub

### Agent not responding to comments

1. Comment must include `@cursor`
2. Check workflow logs in GitHub Actions
3. Verify `GITHUB_TOKEN` permissions

---

## API Reference

### CLI Commands

```bash
cursor-agent [command] [options]

Commands:
  review <file>     Review code
  write <prompt>    Generate code
  fix <issue>       Fix bug
  chat              Interactive mode

Options:
  --model <name>    Override model
  --temp <float>    Set temperature
  --verbose         Verbose output
  --help            Show help
```

### Configuration API

```yaml
model:
  name: string              # Model name
  temperature: float        # 0.0 - 1.0
  max_tokens: int           # Max response length

agent:
  auto_review: boolean      # Auto-review PRs
  interactive: boolean      # Interactive mode
  verbose: boolean          # Verbose logging

github:
  auto_pr: boolean          # Auto-create PRs
  default_branch: string    # Default branch
  commit_prefix: string     # Commit message prefix
```

---

## Best Practices

1. **Review Before Committing**
   - Always review agent-generated code
   - Test thoroughly
   - Check for sensitive data

2. **Use Specific Prompts**
   - Bad: "fix this"
   - Good: "Fix TypeError in authentication module"

3. **Incremental Changes**
   - Small, focused changes
   - One issue per agent run
   - Easier to review

4. **Security**
   - Never commit API keys
   - Review all generated code
   - Use read-only mode for untrusted repos

5. **Performance**
   - Cache agent responses
   - Batch similar operations
   - Use appropriate temperature settings

---

## FAQ

**Q: Is this open source?**
A: The Cursor CLI itself is proprietary, but this integration is custom.

**Q: Cost?**
A: Cursor CLI usage may have costs. Check cursor.com/pricing

**Q: Which models are supported?**
A: Claude 3.5 Sonnet (default), GPT-4, others via config

**Q: Can I use offline?**
A: No, requires API access to LLM providers

**Q: How do I update?**
A: Run `./install.sh` again to reinstall

---

## Related Resources

- [Cursor Documentation](https://cursor.com/docs)
- [Cursor CLI Docs](https://cursor.com/docs/cli)
- [GitHub Actions Docs](https://docs.github.com/actions)
- [GitHub CLI](https://cli.github.com/)

---

## License

MIT License (for this integration setup)

Cursor CLI is proprietary software - see cursor.com for license.

---

```
∇ • Θεός°●⟐●Σ℧ΛΘ

Terminal AI coding is now active.

$ agent --version
$ github-agent-integrate
$ agent review your-code.py

The command line is the interface to AI-assisted development.
```

---

**Status:** COMPLETE ✓
**Integration:** READY ✓
**Documentation:** COMPREHENSIVE ✓
