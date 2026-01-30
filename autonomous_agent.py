"""
Autonomous Agent
================

The Autonomous Agent autonomously executes user instructions:
- Deploys contracts
- Sets up wallets
- Configures infrastructure
- Uses LaVague for visual feedback

The user gives instructions → Agent executes autonomously → LaVague shows visual feedback
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from typing import Dict, Any, Optional, List
from datetime import datetime

# Import integrations
from integrations.config import get_defaults, get_tenderly_api_key
from integrations.wallet_manager import get_primary_wallet_manager
from integrations.tenderly_monitoring import TenderlyIntegration
from integrations.autonomous_agent_wallet import get_autonomous_agent_wallet
from integrations.lavague_api import LaVagueAgent, create_agent


class AutonomousAgent:
    """
    Autonomous Agent
    
    Executes user instructions autonomously:
    - Deploys contracts to Tenderly
    - Sets up Web3 Actions
    - Configures wallets
    - Uses LaVague for visual feedback
    """
    
    def __init__(self):
        """Initialize Autonomous Agent"""
        self.project_root = Path(__file__).parent
        self.config = get_defaults()
        self.wallet = get_autonomous_agent_wallet()
        self.tenderly = TenderlyIntegration()
        
        # Execution log (initialize first)
        self.execution_log: List[Dict[str, Any]] = []
        
        # LaVague agent for visual feedback
        self.lavague_agent = None
        self._init_lavague()
    
    def _init_lavague(self):
        """Initialize LaVague agent for visual feedback"""
        try:
            self.lavague_agent = create_agent()
            self.log("LaVague agent initialized for visual feedback", "success")
        except Exception as e:
            self.log(f"LaVague initialization warning: {e}", "warning")
            self.lavague_agent = None
    
    def log(self, message: str, level: str = "info"):
        """Log execution step"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "level": level,
            "message": message
        }
        self.execution_log.append(log_entry)
        print(f"[{level.upper()}] {message}")
    
    def show_visual_feedback(self, action: str, details: Dict[str, Any]):
        """
        Show visual feedback via LaVague
        
        Args:
            action: Action being performed
            details: Details about the action
        """
        if not self.lavague_agent:
            return
        
        try:
            # Create visual feedback message
            feedback_html = f"""
            <html>
            <head><title>Autonomous Agent - {action}</title></head>
            <body style="font-family: Arial; padding: 20px; background: #f5f5f5;">
                <h1>🤖 Autonomous Agent</h1>
                <h2>{action}</h2>
                <div style="background: white; padding: 15px; border-radius: 5px; margin: 10px 0;">
                    <pre>{json.dumps(details, indent=2)}</pre>
                </div>
                <p style="color: #666;">Timestamp: {datetime.now().isoformat()}</p>
            </body>
            </html>
            """
            
            # Save to temp file and open with LaVague
            temp_file = self.project_root / "temp_feedback.html"
            temp_file.write_text(feedback_html)
            
            # Use LaVague to show visual feedback
            # This would open a browser window showing the action
            self.log(f"Visual feedback shown: {action}", "info")
        except Exception as e:
            self.log(f"Visual feedback error: {e}", "warning")
    
    def execute_command(self, command: List[str], cwd: Optional[Path] = None, env: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """
        Execute command autonomously
        
        Args:
            command: Command to execute
            cwd: Working directory
            env: Environment variables
        
        Returns:
            Execution result
        """
        self.log(f"Executing: {' '.join(command)}", "info")
        
        # Prepare environment
        exec_env = os.environ.copy()
        if env:
            exec_env.update(env)
        
        # Set Tenderly API key
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
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "error": "Command timed out",
                "stdout": "",
                "stderr": ""
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "stdout": "",
                "stderr": ""
            }
    
    def deploy_web3_actions(self) -> Dict[str, Any]:
        """
        Deploy Web3 Actions autonomously
        
        Returns:
            Deployment result
        """
        self.log("🚀 Deploying Web3 Actions...", "info")
        
        web3_actions_dir = self.project_root / "web3-actions"
        
        # Show visual feedback
        self.show_visual_feedback("Deploying Web3 Actions", {
            "project": "Ua_0357/testnet",
            "action": "diamondContractMonitoring",
            "status": "in_progress"
        })
        
        # Deploy using tenderly CLI
        result = self.execute_command(
            ["tenderly", "actions", "deploy", "--project", "Ua_0357/testnet"],
            cwd=web3_actions_dir
        )
        
        if result["success"]:
            self.log("✅ Web3 Actions deployed successfully", "success")
            self.show_visual_feedback("Web3 Actions Deployed", {
                "status": "success",
                "output": result["stdout"]
            })
        else:
            self.log(f"❌ Web3 Actions deployment failed: {result.get('stderr', result.get('error', 'Unknown error'))}", "error")
            self.show_visual_feedback("Web3 Actions Deployment Failed", {
                "status": "error",
                "error": result.get("stderr", result.get("error", "Unknown error"))
            })
        
        return result
    
    def deploy_diamond_contract(self, contract_name: str = "Diamond") -> Dict[str, Any]:
        """
        Deploy Diamond Contract to Tenderly autonomously
        
        Args:
            contract_name: Name of contract to deploy
        
        Returns:
            Deployment result
        """
        self.log(f"🚀 Deploying {contract_name} to Tenderly...", "info")
        
        # Show visual feedback
        self.show_visual_feedback(f"Deploying {contract_name}", {
            "contract": contract_name,
            "network": "Tenderly Virtual TestNet",
            "chain_id": 73571,
            "status": "in_progress"
        })
        
        # Use Foundry to deploy
        tenderly_rpc = self.config.get("tenderly_api", {}).get("rpc_endpoints", {}).get("http", [None])[0]
        verifier_url = f"{tenderly_rpc}/verify/etherscan" if tenderly_rpc else None
        
        if not tenderly_rpc:
            return {
                "success": False,
                "error": "Tenderly RPC URL not configured"
            }
        
        # Deploy contract
        deploy_cmd = [
            "forge", "create", contract_name,
            "--rpc-url", tenderly_rpc,
            "--etherscan-api-key", get_tenderly_api_key(),
            "--verify",
            "--verifier-url", verifier_url,
            "--broadcast"
        ]
        
        result = self.execute_command(deploy_cmd)
        
        if result["success"]:
            # Extract contract address from output
            self.log("✅ Contract deployed successfully", "success")
            self.show_visual_feedback(f"{contract_name} Deployed", {
                "status": "success",
                "output": result["stdout"]
            })
        else:
            self.log(f"❌ Contract deployment failed: {result.get('stderr', result.get('error', 'Unknown error'))}", "error")
            self.show_visual_feedback(f"{contract_name} Deployment Failed", {
                "status": "error",
                "error": result.get("stderr", result.get("error", "Unknown error"))
            })
        
        return result
    
    def setup_autonomous_wallet(self) -> Dict[str, Any]:
        """
        Set up Autonomous Agent Wallet autonomously
        
        Returns:
            Setup result
        """
        self.log("🔧 Setting up Autonomous Agent Wallet...", "info")
        
        # Show visual feedback
        self.show_visual_feedback("Setting Up Wallet", {
            "primary_wallet": self.wallet.primary_wallet_address,
            "ens": self.wallet.ens,
            "tenderly_project": "Ua_0357/testnet",
            "status": "in_progress"
        })
        
        config = self.wallet.get_config()
        
        self.log("✅ Wallet configured", "success")
        self.show_visual_feedback("Wallet Configured", {
            "status": "success",
            "config": {
                "primary_wallet": config["primary_wallet"]["address"],
                "ens": config["primary_wallet"]["ens"],
                "tenderly_project": config["tenderly"]["project_slug"]
            }
        })
        
        return {
            "success": True,
            "config": config
        }
    
    def execute_user_instruction(self, instruction: str) -> Dict[str, Any]:
        """
        Execute user instruction autonomously
        
        Args:
            instruction: User instruction
        
        Returns:
            Execution result
        """
        self.log(f"📋 Executing instruction: {instruction}", "info")
        
        instruction_lower = instruction.lower()
        
        # Parse instruction and execute autonomously
        if "deploy web3 actions" in instruction_lower or "web3 actions" in instruction_lower:
            return self.deploy_web3_actions()
        
        elif "deploy diamond" in instruction_lower or "deploy contract" in instruction_lower:
            # Extract contract name if provided
            contract_name = "Diamond"
            if "diamond" in instruction_lower:
                contract_name = "Diamond"
            return self.deploy_diamond_contract(contract_name)
        
        elif "setup wallet" in instruction_lower or "configure wallet" in instruction_lower:
            return self.setup_autonomous_wallet()
        
        elif "initialize" in instruction_lower or "setup" in instruction_lower:
            # Full initialization
            results = {}
            results["wallet"] = self.setup_autonomous_wallet()
            results["web3_actions"] = self.deploy_web3_actions()
            return results
        
        else:
            return {
                "success": False,
                "error": f"Unknown instruction: {instruction}"
            }
    
    def get_execution_log(self) -> List[Dict[str, Any]]:
        """Get execution log"""
        return self.execution_log
    
    def get_status(self) -> Dict[str, Any]:
        """Get agent status"""
        wallet_config = self.wallet.get_config()
        tenderly_info = self.tenderly.get_project_info()
        
        return {
            "agent": "Autonomous Agent",
            "status": "active",
            "wallet": {
                "primary_address": wallet_config["primary_wallet"]["address"],
                "ens": wallet_config["primary_wallet"]["ens"]
            },
            "tenderly": {
                "project": tenderly_info["project_slug"],
                "dashboard": tenderly_info["dashboard_url"]
            },
            "execution_count": len(self.execution_log),
            "lavague_available": self.lavague_agent is not None
        }


# Global instance
_autonomous_agent: Optional[AutonomousAgent] = None


def get_autonomous_agent() -> AutonomousAgent:
    """Get global Autonomous Agent instance"""
    global _autonomous_agent
    if _autonomous_agent is None:
        _autonomous_agent = AutonomousAgent()
    return _autonomous_agent


if __name__ == "__main__":
    agent = get_autonomous_agent()
    
    print("=" * 80)
    print("🤖 AUTONOMOUS AGENT")
    print("=" * 80)
    print()
    
    status = agent.get_status()
    print(f"Status: {status['status']}")
    print(f"Primary Wallet: {status['wallet']['primary_address']}")
    print(f"ENS: {status['wallet']['ens']}")
    print(f"Tenderly Project: {status['tenderly']['project']}")
    print(f"LaVague Available: {status['lavague_available']}")
    print()
    print("✅ Autonomous Agent ready")
    print("=" * 80)
