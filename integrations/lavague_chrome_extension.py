"""
LaVague Chrome Extension Driver Integration
==========================================

Integration with LaVague's Chrome Extension driver for web automation.

Official Documentation: https://docs.lavague.ai/en/latest/docs/get-started/docs-chrome/

Features:
- Chrome Extension driver support
- Interactive browser automation
- Element highlighting
- Multiple tabs support
"""

import os
from typing import Optional, Dict, Any
from integrations.lavague_api import load_env

ENV = load_env()


class LaVagueChromeExtensionAgent:
    """
    LaVague Agent using Chrome Extension driver
    
    Chrome Extension driver features:
    - ✅ Open several tabs
    - ✅ Highlight elements
    - ❌ Headless agents (not supported)
    - ❌ Handle iframes (not supported)
    
    Based on official LaVague Chrome Extension patterns.
    """

    def __init__(
        self,
        world_model_config: Optional[Dict[str, Any]] = None,
        action_engine_config: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize LaVague Agent with Chrome Extension driver
        
        Args:
            world_model_config: Custom World Model configuration
            action_engine_config: Custom Action Engine configuration
        """
        try:
            from lavague.core import WorldModel, ActionEngine
            from lavague.core.agents import WebAgent
            from lavague.drivers.chrome_extension import ChromeExtensionDriver
        except ImportError:
            raise ImportError(
                "LaVague Chrome Extension driver is not available. "
                "Install LaVague and set up Chrome Extension: "
                "https://docs.lavague.ai/en/latest/docs/get-started/docs-chrome/"
            )

        # Setup API key from environment
        api_key = ENV.get('OPENAI_API_KEY') or os.getenv('OPENAI_API_KEY')
        if api_key:
            os.environ['OPENAI_API_KEY'] = api_key

        # Initialize Chrome Extension driver
        self.driver = ChromeExtensionDriver()

        # Initialize World Model
        if world_model_config:
            self.world_model = WorldModel(**world_model_config)
        else:
            self.world_model = WorldModel()

        # Initialize Action Engine
        if action_engine_config:
            self.action_engine = ActionEngine(self.driver, **action_engine_config)
        else:
            self.action_engine = ActionEngine(self.driver)

        # Create Web Agent
        self.agent = WebAgent(self.world_model, self.action_engine)
        self.driver_type = "chrome_extension"

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


def create_chrome_extension_agent(
    world_model_config: Optional[Dict[str, Any]] = None,
    action_engine_config: Optional[Dict[str, Any]] = None
) -> LaVagueChromeExtensionAgent:
    """
    Create a LaVague Chrome Extension agent instance
    
    Args:
        world_model_config: Custom World Model configuration
        action_engine_config: Custom Action Engine configuration
        
    Returns:
        LaVagueChromeExtensionAgent instance
    """
    return LaVagueChromeExtensionAgent(
        world_model_config=world_model_config,
        action_engine_config=action_engine_config
    )
