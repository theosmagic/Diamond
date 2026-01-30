"""
Autonomous Executor
===================

This module provides autonomous execution capabilities that the coding agent
uses to execute commands, deploy contracts, and set up infrastructure
WITHOUT requiring the user to run commands manually.

The user gives instructions → Agent executes autonomously → LaVague shows visual feedback
"""

import os
import subprocess
import json
from pathlib import Path
from typing import Dict, Any, Optional, List
from datetime import datetime

from integrations.config import get_defaults, get_tenderly_api_key
from integrations.autonomous_agent_wallet import get_autonomous_agent_wallet
from integrations.tenderly_monitoring import TenderlyIntegration


class AutonomousExecutor:
    """
    Autonomous Executor
    
    Executes commands and operations autonomously on behalf of the user.
    The user should never need to run commands manually - this handles everything.
    """
    
    def __init__(self):
        """Initialize Autonomous Executor"""
        self.project_root = Path(__file__).parent.parent
        self.config = get_defaults()
        self.wallet = get_autonomous_agent_wallet()
        self.tenderly = TenderlyIntegration()
    
    def execute(self, command: List[str], cwd: Optional[Path] = None, env: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """
        Execute command autonomously
        
        Args:
            command: Command to execute
            cwd: Working directory
            env: Environment variables
        
        Returns:
            Execution result
        """
        # Prepare environment
        exec_env = os.environ.copy()
        if env:
            exec_env.update(env)
        
        # Set required environment variables
        exec_env["TENDERLY_API"] = get_tenderly_api_key()
        exec_env["PATH"] = f"{self.project_root / 'bin'}:{exec_env.get('PATH', '')}"
        
        try:
            result = subprocess.run(
                command,
                cwd=cwd or self.project_root,
                env=exec_env,
                capture_output=True,
                text=True,
                timeout=300
            )
            
            return {
                "success": result.returncode == 0,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "stdout": "",
                "stderr": ""
            }
    
    def deploy_web3_actions(self) -> Dict[str, Any]:
        """Deploy Web3 Actions autonomously"""
        web3_actions_dir = self.project_root / "web3-actions"
        return self.execute(
            ["tenderly", "actions", "deploy", "--project", "Ua_0357/testnet"],
            cwd=web3_actions_dir
        )
    
    def deploy_diamond_to_tenderly(self, contract_name: str = "Diamond") -> Dict[str, Any]:
        """Deploy Diamond Contract to Tenderly autonomously"""
        tenderly_config = self.config.get("tenderly_api", {})
        rpc_endpoints = tenderly_config.get("rpc_endpoints", {})
        tenderly_rpc = rpc_endpoints.get("http", [None])[0]
        
        if not tenderly_rpc:
            return {
                "success": False,
                "error": "Tenderly RPC URL not configured"
            }
        
        verifier_url = f"{tenderly_rpc}/verify/etherscan"
        
        return self.execute([
            "forge", "create", contract_name,
            "--rpc-url", tenderly_rpc,
            "--etherscan-api-key", get_tenderly_api_key(),
            "--verify",
            "--verifier-url", verifier_url,
            "--broadcast"
        ])


# Global instance
_executor: Optional[AutonomousExecutor] = None


def get_executor() -> AutonomousExecutor:
    """Get global executor instance"""
    global _executor
    if _executor is None:
        _executor = AutonomousExecutor()
    return _executor
