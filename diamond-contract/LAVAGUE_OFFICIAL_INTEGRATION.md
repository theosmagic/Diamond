# LaVague Official Integration

**Date**: January 29, 2026  
**Status**: ✅ Integrated with Official LaVague Patterns

---

## ✅ Official LaVague Integration

### Repository Analysis
- **Main Repository**: https://github.com/lavague-ai/LaVague
- **Organization**: https://github.com/orgs/lavague-ai/repositories
- **Documentation**: https://docs.lavague.ai/
- **License**: Apache License 2.0

### Official LaVague Pattern

```python
from lavague.core import WorldModel, ActionEngine
from lavague.core.agents import WebAgent
from lavague.drivers.selenium import SeleniumDriver

selenium_driver = SeleniumDriver(headless=False)
world_model = WorldModel()
action_engine = ActionEngine(selenium_driver)
agent = WebAgent(world_model, action_engine)
agent.get("https://huggingface.co/docs")
agent.run("Go on the quicktour of PEFT")
```

---

## 📋 Our Integration

### Files Updated

#### `integrations/lavague_api.py`
- ✅ Uses official imports: `lavague.core.WorldModel`, `ActionEngine`
- ✅ Uses official imports: `lavague.core.agents.WebAgent`
- ✅ Supports `SeleniumDriver` and `PlaywrightDriver`
- ✅ Follows official API patterns
- ✅ Added telemetry configuration support
- ✅ Improved error handling for driver methods

#### `integrations/lavague_chrome_extension.py` (New)
- ✅ Chrome Extension driver integration
- ✅ Follows official Chrome Extension patterns
- ✅ Supports multiple tabs
- ✅ Element highlighting support

---

## 🚀 Supported Drivers

### Driver Feature Matrix

| Feature | Selenium | Playwright | Chrome Extension |
|---------|----------|-----------|------------------|
| Headless agents | ✅ | ⏳ | N/A |
| Handle iframes | ✅ | ✅ | ❌ |
| Open several tabs | ✅ | ⏳ | ✅ |
| Highlight elements | ✅ | ✅ | ✅ |

✅ supported  
⏳ coming soon  
❌ not supported

---

## 📦 Installation

```bash
pip install lavague
```

### Dependencies
- `lavague>=1.0.0` (in requirements.txt)
- `selenium>=4.0.0` (for Selenium driver)
- `playwright>=1.40.0` (for Playwright driver)

---

## 🔧 Configuration

### Environment Variables

**Required:**
- `OPENAI_API_KEY` - OpenAI API key for LLM calls

**Optional:**
- `LAVAGUE_TELEMETRY` - Set to `"NONE"` to disable telemetry

### Telemetry

LaVague collects telemetry by default. To disable:

```bash
export LAVAGUE_TELEMETRY=NONE
```

---

## 💻 Usage Examples

### Basic Usage (Selenium)

```python
from integrations.lavague_api import LaVagueAgent

# Create agent
agent = LaVagueAgent(driver_type="selenium", headless=False)

# Navigate and run objective
agent.navigate("https://huggingface.co/docs")
result = agent.run("Go on the quicktour of PEFT")

# Close
agent.close()
```

### Basic Usage (Playwright)

```python
from integrations.lavague_api import LaVagueAgent

# Create agent with Playwright
agent = LaVagueAgent(driver_type="playwright", headless=True)

# Navigate and run objective
agent.navigate("https://example.com")
result = agent.run("Fill out the contact form")

# Close
agent.close()
```

### Chrome Extension Usage

```python
from integrations.lavague_chrome_extension import LaVagueChromeExtensionAgent

# Create Chrome Extension agent
agent = LaVagueChromeExtensionAgent()

# Navigate and run objective
agent.navigate("https://example.com")
result = agent.run("Find and click the About link")

# Close
agent.close()
```

### Context Manager

```python
from integrations.lavague_api import LaVagueAgent

# Use context manager for automatic cleanup
with LaVagueAgent(driver_type="selenium", headless=False) as agent:
    agent.navigate("https://huggingface.co/docs")
    agent.run("Go on the quicktour of PEFT")
```

### Quick Function

```python
from integrations.lavague_api import run_objective

# Quick function for single objectives
result = run_objective(
    objective="Find and click the About link",
    url="https://example.com",
    driver_type="selenium",
    headless=True
)
```

### Interactive Demo

```python
from integrations.lavague_api import LaVagueAgent

agent = LaVagueAgent(driver_type="selenium", headless=False)
agent.navigate("https://huggingface.co/docs")

# Launch Gradio demo
agent.demo("Go on the quicktour of PEFT")
```

---

## 🎯 Key Features

### World Model
- Takes objective and current page state
- Outputs appropriate set of instructions
- Customizable configuration

### Action Engine
- "Compiles" instructions into action code
- Executes actions (Selenium/Playwright)
- Customizable configuration

### Web Agent
- Combines World Model and Action Engine
- Provides high-level API
- Supports multiple objectives

---

## 📊 Token Usage & Costs

LaVague uses LLMs (default: OpenAI's `gpt4-o`) under the hood.

Cost depends on:
- Models chosen
- Complexity of objective
- Website being interacted with

See LaVague's [token counting documentation](https://docs.lavague.ai/en/latest/docs/get-started/token-usage/) for tracking.

---

## ✅ Compliance Status

**Official Patterns**: ✅ Followed
- Uses official imports
- Follows official API structure
- Matches official usage patterns

**Documentation**: ✅ Updated
- References official documentation
- Includes official examples
- Documents all supported drivers

**Features**: ✅ Complete
- Selenium driver ✅
- Playwright driver ✅
- Chrome Extension driver ✅
- Telemetry configuration ✅
- Error handling ✅

---

## 🔗 Resources

- **Main Repository**: https://github.com/lavague-ai/LaVague
- **Documentation**: https://docs.lavague.ai/
- **Quick Tour**: https://docs.lavague.ai/en/latest/docs/get-started/quick-tour/
- **Chrome Extension**: https://docs.lavague.ai/en/latest/docs/get-started/docs-chrome/
- **Troubleshooting**: https://docs.lavague.ai/en/latest/docs/get-started/troubleshoot/
- **Discord**: https://discord.gg/SDxn9KpqX9

---

**Status**: ✅ **LAVAGUE OFFICIAL INTEGRATION COMPLETE**

**Our integration now follows official LaVague patterns and best practices.** 🚀
