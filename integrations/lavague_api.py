"""
LaVague Web Agent Integration
=============================

Integration with LaVague framework for AI-powered web automation.
LaVague is a Large Action Model framework for developing AI Web Agents.

Official Repository: https://github.com/lavague-ai/LaVague
Documentation: https://docs.lavague.ai/

Features:
- Web automation with LLM-powered actions
- Support for Selenium and Playwright drivers
- Customizable World Model and Action Engine
- Interactive Gradio interface
- Token usage tracking
- Chrome Extension driver support

Based on official LaVague patterns:
- Uses lavague.core.WorldModel and ActionEngine
- Uses lavague.core.agents.WebAgent
- Supports SeleniumDriver, PlaywrightDriver
- Follows official API patterns from LaVague documentation
"""

import os
from typing import Optional, Dict, Any, List
from pathlib import Path


def load_env():
    """Load environment variables from env.txt"""
    config = {}
    possible_paths = [
        "/mnt/Vault/env.txt",
        "/mnt/Vault/Cursor-Agent/env.txt",
        os.path.join(os.getcwd(), "env.txt")
    ]
    
    env_file = None
    for path in possible_paths:
        if os.path.exists(path):
            env_file = path
            break

    if env_file:
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#') or line.startswith('-----'):
                    continue
                if '=' in line:
                    key_part, value = line.split('=', 1)
                    key = key_part.strip()
                    if key.startswith('export '):
                        key = key[7:].strip()
                    config[key] = value.strip().strip('"').strip("'")
    return config


ENV = load_env()


class LaVagueAgent:
    """
    LaVague Web Agent Integration
    
    A wrapper around LaVague's WebAgent for easy integration into
    the sovereign agent system.
    
    Example:
        agent = LaVagueAgent(driver_type="selenium", headless=False)
        agent.navigate("https://example.com")
        result = agent.run("Fill out the contact form with test data")
    """

    def __init__(
        self,
        driver_type: str = "selenium",
        headless: bool = False,
        world_model_config: Optional[Dict[str, Any]] = None,
        action_engine_config: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize LaVague Agent
        
        Args:
            driver_type: "selenium" or "playwright"
            headless: Run browser in headless mode
            world_model_config: Custom World Model configuration
            action_engine_config: Custom Action Engine configuration
        """
        try:
            from lavague.core import WorldModel, ActionEngine
            from lavague.core.agents import WebAgent
        except ImportError:
            raise ImportError(
                "LaVague is not installed. Install it with: pip install lavague"
            )

        # Setup API key from environment (LaVague uses OPENAI_API_KEY by default)
        api_key = ENV.get('OPENAI_API_KEY') or os.getenv('OPENAI_API_KEY')
        if api_key:
            os.environ['OPENAI_API_KEY'] = api_key
        else:
            # Check for telemetry setting
            telemetry = ENV.get('LAVAGUE_TELEMETRY', os.getenv('LAVAGUE_TELEMETRY', ''))
            if telemetry.upper() == 'NONE':
                os.environ['LAVAGUE_TELEMETRY'] = 'NONE'

        # Initialize driver
        if driver_type == "selenium":
            from lavague.drivers.selenium import SeleniumDriver
            self.driver = SeleniumDriver(headless=headless)
        elif driver_type == "playwright":
            from lavague.drivers.playwright import PlaywrightDriver
            self.driver = PlaywrightDriver(headless=headless)
        else:
            raise ValueError(f"Unknown driver type: {driver_type}. Use 'selenium' or 'playwright'")

        # Initialize World Model
        if world_model_config:
            self.world_model = WorldModel(**world_model_config)
        else:
            self.world_model = WorldModel()

        # Initialize Action Engine (official pattern: ActionEngine(driver))
        if action_engine_config:
            self.action_engine = ActionEngine(self.driver, **action_engine_config)
        else:
            self.action_engine = ActionEngine(self.driver)

        # Create Web Agent
        self.agent = WebAgent(self.world_model, self.action_engine)
        self.driver_type = driver_type
        self.headless = headless

    def navigate(self, url: str) -> Dict[str, Any]:
        """
        Navigate to a URL
        
        Args:
            url: URL to navigate to
            
        Returns:
            Status dictionary
        """
        try:
            self.agent.get(url)
            return {
                "success": True,
                "url": url,
                "message": f"Navigated to {url}"
            }
        except Exception as e:
            return {
                "success": False,
                "url": url,
                "error": str(e)
            }

    def run(self, objective: str, max_steps: Optional[int] = None) -> Dict[str, Any]:
        """
        Run an objective using the LaVague agent
        
        Args:
            objective: Natural language objective to achieve
            max_steps: Maximum number of steps to take (optional)
            
        Returns:
            Result dictionary with execution details
        """
        try:
            if max_steps:
                result = self.agent.run(objective, max_steps=max_steps)
            else:
                result = self.agent.run(objective)
            
            return {
                "success": True,
                "objective": objective,
                "result": result,
                "message": "Objective completed"
            }
        except Exception as e:
            return {
                "success": False,
                "objective": objective,
                "error": str(e)
            }

    def demo(self, objective: str) -> None:
        """
        Launch interactive Gradio demo for the objective
        
        Args:
            objective: Natural language objective to demonstrate
        """
        self.agent.demo(objective)

    def get_current_url(self) -> str:
        """
        Get current page URL
        
        Returns:
            Current page URL
        """
        try:
            return self.agent.driver.get_url()
        except AttributeError:
            # Fallback for different driver implementations
            return self.driver.get_url() if hasattr(self.driver, 'get_url') else ""

    def get_page_title(self) -> str:
        """
        Get current page title
        
        Returns:
            Current page title
        """
        try:
            return self.agent.driver.get_title()
        except AttributeError:
            # Fallback for different driver implementations
            return self.driver.get_title() if hasattr(self.driver, 'get_title') else ""

    def take_screenshot(self, path: Optional[str] = None) -> str:
        """
        Take a screenshot of the current page
        
        Args:
            path: Optional path to save screenshot
            
        Returns:
            Path to saved screenshot
        """
        if not path:
            path = f"/tmp/lavague_screenshot_{os.getpid()}.png"
        
        self.agent.driver.save_screenshot(path)
        return path

    def close(self) -> None:
        """Close the browser and cleanup"""
        try:
            self.agent.driver.quit()
        except:
            pass

    def __enter__(self):
        """Context manager entry"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.close()


class LaVagueTaskRunner:
    """
    Task runner for executing multiple LaVague objectives
    
    Useful for running sequences of web automation tasks.
    """

    def __init__(self, driver_type: str = "selenium", headless: bool = True):
        """
        Initialize task runner
        
        Args:
            driver_type: "selenium" or "playwright"
            headless: Run browser in headless mode
        """
        self.driver_type = driver_type
        self.headless = headless
        self.agent = None

    def run_tasks(
        self,
        tasks: List[Dict[str, Any]],
        start_url: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Run a list of tasks sequentially
        
        Args:
            tasks: List of task dictionaries with 'url' and 'objective' keys
            start_url: Optional starting URL
            
        Returns:
            List of results for each task
        """
        results = []
        
        try:
            self.agent = LaVagueAgent(
                driver_type=self.driver_type,
                headless=self.headless
            )

            if start_url:
                self.agent.navigate(start_url)

            for i, task in enumerate(tasks):
                url = task.get('url')
                objective = task.get('objective')
                max_steps = task.get('max_steps')

                if url:
                    nav_result = self.agent.navigate(url)
                    if not nav_result['success']:
                        results.append({
                            "task_index": i,
                            "success": False,
                            "error": f"Failed to navigate: {nav_result.get('error')}"
                        })
                        continue

                if objective:
                    result = self.agent.run(objective, max_steps=max_steps)
                    result['task_index'] = i
                    results.append(result)
                else:
                    results.append({
                        "task_index": i,
                        "success": False,
                        "error": "No objective provided"
                    })

        finally:
            if self.agent:
                self.agent.close()

        return results


# Convenience functions

def create_agent(
    driver_type: str = "selenium",
    headless: bool = False
) -> LaVagueAgent:
    """
    Create a LaVague agent instance
    
    Args:
        driver_type: "selenium" or "playwright"
        headless: Run browser in headless mode
        
    Returns:
        LaVagueAgent instance
    """
    return LaVagueAgent(driver_type=driver_type, headless=headless)


def run_objective(
    objective: str,
    url: Optional[str] = None,
    driver_type: str = "selenium",
    headless: bool = True,
    max_steps: Optional[int] = None
) -> Dict[str, Any]:
    """
    Quick function to run a single objective
    
    Args:
        objective: Natural language objective
        url: Optional starting URL
        driver_type: "selenium" or "playwright"
        headless: Run browser in headless mode
        max_steps: Maximum number of steps
        
    Returns:
        Result dictionary
    """
    agent = LaVagueAgent(driver_type=driver_type, headless=headless)
    
    try:
        if url:
            agent.navigate(url)
        
        return agent.run(objective, max_steps=max_steps)
    finally:
        agent.close()


if __name__ == "__main__":
    # Example usage
    print("LaVague Integration Test")
    print("=" * 50)
    
    # Check if API key is set
    api_key = ENV.get('OPENAI_API_KEY') or os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("⚠️  Warning: OPENAI_API_KEY not found in environment")
        print("Set it in env.txt or as environment variable")
    else:
        print("✅ OPENAI_API_KEY found")
    
    print("\nExample usage:")
    print("""
    from integrations.lavague_api import LaVagueAgent
    
    # Create agent
    agent = LaVagueAgent(driver_type="selenium", headless=False)
    
    # Navigate and run objective
    agent.navigate("https://example.com")
    result = agent.run("Find and click the 'About' link")
    
    # Or use context manager
    with LaVagueAgent() as agent:
        agent.navigate("https://huggingface.co/docs")
        agent.run("Go on the quicktour of PEFT")
    """)
