"""
Foundry + Tenderly Integration
===============================

Integration of Foundry with Tenderly Virtual TestNet for contract deployment and verification.

Based on: https://docs.tenderly.co/virtual-testnets/smart-contract-frameworks/foundry

Features:
- Contract deployment to Tenderly Virtual TestNet
- Contract verification
- Script execution with --slow flag
- Foundry configuration management
"""

import os
import subprocess
from typing import Optional, Dict, Any, List
from pathlib import Path
from integrations.config import get_tenderly_api_key
from integrations.tenderly_rpc import get_tenderly_http_endpoint


class FoundryTenderlyIntegration:
    """
    Foundry + Tenderly Integration
    
    Manages Foundry deployment and verification on Tenderly Virtual TestNet.
    """
    
    # Tenderly Virtual TestNet Chain ID
    TENDERLY_CHAIN_ID = 73571
    
    def __init__(self, api_key: Optional[str] = None, rpc_url: Optional[str] = None):
        """
        Initialize Foundry + Tenderly Integration
        
        Args:
            api_key: Tenderly API key (defaults to TENDERLY_API environment variable)
            rpc_url: Tenderly Virtual TestNet RPC URL (defaults to first HTTP endpoint)
        """
        self.api_key = api_key or get_tenderly_api_key()
        self.rpc_url = rpc_url or get_tenderly_http_endpoint(0)
        self.verifier_url = f"{self.rpc_url}/verify/etherscan"
        
        # Set environment variables
        if self.api_key:
            os.environ["TENDERLY_ACCESS_KEY"] = self.api_key
            os.environ["TENDERLY_API"] = self.api_key
        if self.rpc_url:
            os.environ["TENDERLY_VIRTUAL_TESTNET_RPC_URL"] = self.rpc_url
            os.environ["TENDERLY_VERIFIER_URL"] = self.verifier_url
    
    def check_foundry(self) -> Dict[str, Any]:
        """
        Check if Foundry (forge) is installed
        
        Returns:
            Check result
        """
        try:
            result = subprocess.run(
                ["forge", "--version"],
                capture_output=True,
                text=True,
                timeout=10
            )
            return {
                "available": result.returncode == 0,
                "version": result.stdout.strip() if result.returncode == 0 else None,
                "error": result.stderr if result.returncode != 0 else None
            }
        except FileNotFoundError:
            return {
                "available": False,
                "version": None,
                "error": "Foundry (forge) is not installed. Install from: https://book.getfoundry.sh/getting-started/installation"
            }
        except Exception as e:
            return {
                "available": False,
                "version": None,
                "error": str(e)
            }
    
    def deploy_contract(
        self,
        contract_name: str,
        private_key: Optional[str] = None,
        constructor_args: Optional[List[str]] = None,
        verify: bool = True
    ) -> Dict[str, Any]:
        """
        Deploy contract to Tenderly Virtual TestNet
        
        Args:
            contract_name: Name of the contract to deploy
            private_key: Private key for deployment (defaults to environment variable)
            constructor_args: Constructor arguments
            verify: Whether to verify the contract
        
        Returns:
            Deployment result
        """
        foundry_check = self.check_foundry()
        if not foundry_check["available"]:
            return {
                "success": False,
                "error": foundry_check["error"]
            }
        
        if not private_key:
            private_key = os.getenv("PRIVATE_KEY") or os.getenv("OPENSEA_12_WORD_SEED")
        
        if not private_key:
            return {
                "success": False,
                "error": "Private key required for deployment"
            }
        
        try:
            cmd = [
                "forge", "create", contract_name,
                "--rpc-url", self.rpc_url,
                "--private-key", private_key,
                "--etherscan-api-key", self.api_key,
                "--broadcast"
            ]
            
            if verify:
                cmd.extend([
                    "--verify",
                    "--verifier-url", self.verifier_url
                ])
            
            if constructor_args:
                cmd.extend(["--constructor-args"] + constructor_args)
            
            result = subprocess.run(
                cmd,
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
                "error": str(e)
            }
    
    def verify_contract(
        self,
        contract_address: str,
        contract_name: str,
        constructor_args: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Verify contract on Tenderly Virtual TestNet
        
        Args:
            contract_address: Deployed contract address
            contract_name: Contract name
            constructor_args: Constructor arguments
        
        Returns:
            Verification result
        """
        foundry_check = self.check_foundry()
        if not foundry_check["available"]:
            return {
                "success": False,
                "error": foundry_check["error"]
            }
        
        try:
            cmd = [
                "forge", "verify-contract",
                contract_address,
                contract_name,
                "--etherscan-api-key", self.api_key,
                "--verifier-url", self.verifier_url,
                "--watch"
            ]
            
            if constructor_args:
                cmd.extend(["--constructor-args"] + constructor_args)
            
            result = subprocess.run(
                cmd,
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
                "error": str(e)
            }
    
    def run_script(
        self,
        script_path: str,
        private_key: Optional[str] = None,
        verify: bool = True,
        slow: bool = True
    ) -> Dict[str, Any]:
        """
        Run Foundry script on Tenderly Virtual TestNet
        
        Args:
            script_path: Path to script (e.g., "script/Counter.s.sol:CounterScript")
            private_key: Private key for execution
            verify: Whether to verify contracts
            slow: Use --slow flag to prevent transaction batching
        
        Returns:
            Script execution result
        """
        foundry_check = self.check_foundry()
        if not foundry_check["available"]:
            return {
                "success": False,
                "error": foundry_check["error"]
            }
        
        if not private_key:
            private_key = os.getenv("PRIVATE_KEY") or os.getenv("OPENSEA_12_WORD_SEED")
        
        if not private_key:
            return {
                "success": False,
                "error": "Private key required for script execution"
            }
        
        try:
            cmd = [
                "forge", "script", script_path,
                "--rpc-url", self.rpc_url,
                "--private-key", private_key,
                "--etherscan-api-key", self.api_key,
                "--broadcast"
            ]
            
            if slow:
                cmd.append("--slow")
            
            if verify:
                cmd.extend([
                    "--verify",
                    "--verifier-url", self.verifier_url
                ])
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=600
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
                "error": str(e)
            }
    
    def get_config(self) -> Dict[str, Any]:
        """
        Get Foundry + Tenderly configuration
        
        Returns:
            Configuration dictionary
        """
        return {
            "tenderly_access_key": self.api_key[:20] + "..." if self.api_key else None,
            "rpc_url": self.rpc_url,
            "verifier_url": self.verifier_url,
            "chain_id": self.TENDERLY_CHAIN_ID,
            "foundry_available": self.check_foundry()["available"]
        }


# Global instance
_foundry_tenderly: Optional[FoundryTenderlyIntegration] = None


def get_foundry_tenderly(api_key: Optional[str] = None, rpc_url: Optional[str] = None) -> FoundryTenderlyIntegration:
    """Get global Foundry + Tenderly integration instance"""
    global _foundry_tenderly
    if _foundry_tenderly is None:
        _foundry_tenderly = FoundryTenderlyIntegration(api_key, rpc_url)
    return _foundry_tenderly


if __name__ == "__main__":
    integration = FoundryTenderlyIntegration()
    config = integration.get_config()
    foundry_check = integration.check_foundry()
    
    print("=" * 80)
    print("FOUNDRY + TENDERLY INTEGRATION")
    print("=" * 80)
    print()
    print(f"Tenderly RPC URL: {config['rpc_url']}")
    print(f"Verifier URL: {config['verifier_url']}")
    print(f"Chain ID: {config['chain_id']}")
    print(f"Foundry Available: {foundry_check['available']}")
    if foundry_check['available']:
        print(f"Foundry Version: {foundry_check['version']}")
    else:
        print(f"Error: {foundry_check['error']}")
    print()
    print("=" * 80)
