# LaVague Integration

LaVague is a Large Action Model framework for developing AI Web Agents. This integration provides a seamless way to use LaVague within the Cursor-Agent system.

## Installation

LaVague and its dependencies are included in `requirements.txt`. Install with:

```bash
pip install -r requirements.txt
```

Or install LaVague directly:

```bash
pip install lavague selenium playwright
```

For Playwright, you'll also need to install browser binaries:

```bash
playwright install
```

## Configuration

LaVague requires an OpenAI API key. Set it in one of these ways:

1. **Environment variable:**
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

2. **In env.txt:**
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

## Quick Start

### Basic Usage

```python
from integrations.lavague_api import LaVagueAgent

# Create an agent
agent = LaVagueAgent(driver_type="selenium", headless=False)

# Navigate to a URL
agent.navigate("https://example.com")

# Run an objective
result = agent.run("Click on the 'About' link")

# Cleanup
agent.close()
```

### Using Context Manager

```python
from integrations.lavague_api import LaVagueAgent

with LaVagueAgent(driver_type="selenium", headless=False) as agent:
    agent.navigate("https://huggingface.co/docs")
    agent.run("Go on the quicktour of PEFT")
```

### Quick Function

```python
from integrations.lavague_api import run_objective

result = run_objective(
    objective="Search for 'Python' in the search box",
    url="https://example.com",
    driver_type="selenium",
    headless=False,
    max_steps=5
)
```

### Task Runner

Run multiple tasks sequentially:

```python
from integrations.lavague_api import LaVagueTaskRunner

tasks = [
    {
        "url": "https://example.com",
        "objective": "Find the 'About' section",
        "max_steps": 3
    },
    {
        "url": "https://example.com",
        "objective": "Click on 'Contact' link",
        "max_steps": 2
    }
]

runner = LaVagueTaskRunner(driver_type="selenium", headless=False)
results = runner.run_tasks(tasks)
```

## API Reference

### LaVagueAgent

Main class for web automation.

**Parameters:**
- `driver_type` (str): "selenium" or "playwright" (default: "selenium")
- `headless` (bool): Run browser in headless mode (default: False)
- `world_model_config` (dict, optional): Custom World Model configuration
- `action_engine_config` (dict, optional): Custom Action Engine configuration

**Methods:**
- `navigate(url: str) -> Dict`: Navigate to a URL
- `run(objective: str, max_steps: Optional[int] = None) -> Dict`: Run an objective
- `demo(objective: str) -> None`: Launch interactive Gradio demo
- `get_current_url() -> str`: Get current page URL
- `get_page_title() -> str`: Get current page title
- `take_screenshot(path: Optional[str] = None) -> str`: Take a screenshot
- `close() -> None`: Close browser and cleanup

### LaVagueTaskRunner

Runner for executing multiple tasks sequentially.

**Parameters:**
- `driver_type` (str): "selenium" or "playwright" (default: "selenium")
- `headless` (bool): Run browser in headless mode (default: True)

**Methods:**
- `run_tasks(tasks: List[Dict], start_url: Optional[str] = None) -> List[Dict]`: Run multiple tasks

### Convenience Functions

- `create_agent(driver_type="selenium", headless=False) -> LaVagueAgent`: Create an agent instance
- `run_objective(objective, url=None, driver_type="selenium", headless=True, max_steps=None) -> Dict`: Quick function to run a single objective

## Driver Comparison

| Feature | Selenium | Playwright |
|---------|----------|------------|
| Headless agents | ✅ | ⏳ |
| Handle iframes | ✅ | ✅ |
| Open several tabs | ✅ | ⏳ |
| Highlight elements | ✅ | ✅ |

## Examples

See `examples/lavague_example.py` for complete examples.

## Integration with Sovereign Agent

LaVague can be integrated into the sovereign agent system:

```python
from sovereign_agent import SovereignAgent
from integrations.lavague_api import LaVagueAgent

class WebAutomationAgent(SovereignAgent):
    def __init__(self):
        super().__init__()
        self.web_agent = LaVagueAgent()
    
    def automate_web_task(self, objective: str, url: str):
        """Execute web automation with sovereign verification"""
        context = {
            "objective": objective,
            "url": url,
            "sovereign": True
        }
        
        verified_context = self._apply_declaration_verification(context)
        self.web_agent.navigate(url)
        result = self.web_agent.run(objective)
        
        return self.execute_operation("web_automation", {
            **verified_context,
            "result": result
        })
```

## Resources

- [LaVague Documentation](https://docs.lavague.ai/)
- [LaVague GitHub](https://github.com/lavague-ai/LaVague)
- [LaVague Discord](https://discord.gg/SDxn9KpqX9)

## Notes

- LaVague uses LLMs (default: OpenAI GPT-4) which incurs API costs
- Token usage can be tracked using LaVague's built-in token counter
- Telemetry is enabled by default (set `LAVAGUE_TELEMETRY="NONE"` to disable)
- Never include personal information in objectives
