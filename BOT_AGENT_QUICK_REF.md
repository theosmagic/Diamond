# Bot Agent Quick Reference

## Quick Start

```python
from bot_agent import UnifiedBotAgent

# Initialize all services
agent = UnifiedBotAgent()

# Check status
status = agent.get_status()
```

## Available Services

### 1. Jules - AI Coding Agent
```python
# Generate code
result = agent.generate_code("Create a REST API", "python")

# Review code
result = agent.review_code(code_string, "python")
```

### 2. Cloudagents - Cloudflare Services
```python
# List DNS records
result = await agent.manage_dns("list")

# Create DNS record
result = await agent.manage_dns("create", 
    name="example.com",
    type="A",
    content="1.2.3.4"
)
```

### 3. Reblitbots - Automation
```python
# Rebase branch
result = agent.rebase_branch("feature-branch")

# Lint code
result = agent.lint_code(["file.py"], "python")

# Run tests
result = agent.reblitbots.run_tests(".", "pytest")
```

### 4. GitHub API
```python
# List repositories
result = await agent.github_list_repos()

# Use GitHub API directly
repos = await agent.github.list_repos()
issues = await agent.github.list_issues("owner", "repo")
```

### 5. LaVague - Web Automation
```python
# Create web agent
web_agent = agent.create_web_agent(driver_type="selenium", headless=False)

# Navigate and automate
web_agent.navigate("https://example.com")
result = web_agent.run("Click on About link")
web_agent.close()
```

## CLI Commands

```bash
# Status
python3 bot_agent.py --status

# Generate code
python3 bot_agent.py --generate "Create a function" --language python

# Rebase branch
python3 bot_agent.py --rebase feature-branch

# List GitHub repos
python3 bot_agent.py --list-repos

# Test all services
python3 execute_bot_agents.py --all
```

## Credentials (from env.txt)

- `JULES_API` - Jules coding agent
- `GITHUB_TOKEN` - GitHub API
- `CLOUDFLARE_API_TOKEN` - Cloudflare API
- `CLOUDFLARE_GLOBAL_API` - Cloudflare Global API
- `OPENAI_API_KEY` - LaVague (optional)

## Integration with Coding Agents

Add to your agent scripts:

```python
from bot_agent import UnifiedBotAgent

class MyCodingAgent:
    def __init__(self):
        self.bot = UnifiedBotAgent()
    
    def write_code(self, requirements):
        # Use Jules for code generation
        code = self.bot.generate_code(requirements, "python")
        return code
    
    def deploy(self):
        # Use Cloudagents for DNS
        await self.bot.manage_dns("create", ...)
    
    def automate_web(self, url, task):
        # Use LaVague for web automation
        web = self.bot.create_web_agent()
        web.navigate(url)
        web.run(task)
        web.close()
```
