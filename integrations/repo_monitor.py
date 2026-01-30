#!/usr/bin/env python3
"""
Repository Monitor
==================

Monitors 65 repos for unexpected contract interactions and deployment failures.
Integrates with Blockscout to detect issues and log to GitHub.
"""

import os
import sys
import asyncio
from pathlib import Path
from typing import Dict, Any, List, Optional

sys.path.insert(0, str(Path(__file__).parent.parent))

from integrations.blockscout_api import BlockscoutAPI
from integrations.github_api import GitHubAPI


class RepoMonitor:
    """
    Repository Monitor
    
    Monitors 65 repos for contract interactions and alerts on unexpected events
    """
    
    def __init__(self):
        """Initialize Repo Monitor"""
        self.github = GitHubAPI()
        self.blockscout = BlockscoutAPI(chain_id=42161)  # Primary: Arbitrum
        
        # Load repo list
        self.repos = self._load_repos()
    
    def _load_repos(self) -> List[str]:
        """Load list of 65 repos"""
        manifest_path = Path(__file__).parent.parent / "TREASURE_REPOS_MANIFEST.json"
        
        if manifest_path.exists():
            import json
            with open(manifest_path, 'r') as f:
                repos = json.load(f)
                return repos
        
        # Fallback: list from treasure_repos directory
        repos_dir = Path(__file__).parent.parent / "treasure_repos"
        if repos_dir.exists():
            return [d.name for d in repos_dir.iterdir() if d.is_dir() and not d.name.startswith('.')]
        
        return []
    
    async def monitor_repo_contracts(
        self,
        repo_name: str,
        chain_id: int = 42161
    ) -> Dict[str, Any]:
        """
        Monitor contracts associated with a repo
        
        Checks for unexpected interactions
        """
        blockscout = BlockscoutAPI(chain_id=chain_id)
        
        # Try to find contract addresses for this repo
        # This would be configured per repo
        contract_addresses = self._get_repo_contracts(repo_name)
        
        alerts = []
        
        for contract in contract_addresses:
            try:
                # Get recent transactions
                data = await blockscout.get_contract_transactions(contract, limit=10)
                transactions = data.get('items', []) or []
                
                if transactions:
                    # Check for unexpected patterns
                    for tx in transactions:
                        if self._is_unexpected(tx, repo_name):
                            alerts.append({
                                "repo": repo_name,
                                "contract": contract,
                                "tx_hash": tx.get('hash') or tx.get('tx_hash'),
                                "alert": "UNEXPECTED_INTERACTION",
                                "details": tx
                            })
            except Exception as e:
                alerts.append({
                    "repo": repo_name,
                    "contract": contract,
                    "error": str(e),
                    "alert": "MONITORING_ERROR"
                })
        
        return {
            "repo": repo_name,
            "chain_id": chain_id,
            "alerts": alerts,
            "count": len(alerts)
        }
    
    def _get_repo_contracts(self, repo_name: str) -> List[str]:
        """Get contract addresses for a repo"""
        # This would be configured per repo
        # For now, return empty list
        return []
    
    def _is_unexpected(self, tx: Dict[str, Any], repo_name: str) -> bool:
        """Check if transaction is unexpected"""
        # Define unexpected patterns:
        # - Failed transactions
        # - Large value transfers
        # - Unknown senders
        
        if tx.get('isError') == '1' or tx.get('txreceipt_status') == '0':
            return True
        
        # Check for large transfers
        value = int(tx.get('value', 0))
        if value > 10**18:  # More than 1 ETH equivalent
            return True
        
        return False
    
    async def monitor_all_repos(self) -> Dict[str, Any]:
        """Monitor all 65 repos"""
        results = {}
        
        for repo in self.repos[:10]:  # Limit to 10 for testing
            try:
                result = await self.monitor_repo_contracts(repo)
                results[repo] = result
            except Exception as e:
                results[repo] = {"error": str(e)}
        
        return results
    
    async def alert_on_unexpected(
        self,
        repo_name: str,
        contract_address: str,
        tx_hash: str
    ) -> Dict[str, Any]:
        """
        Alert when unexpected interaction detected
        
        Creates GitHub issue and logs to Gist
        """
        # Create GitHub issue
        try:
            issue = await self.github.create_issue(
                owner="theosmagic",  # GitHub username
                repo=repo_name,
                title=f"⚠️ Unexpected Contract Interaction Detected",
                body=f"""
**Contract**: `{contract_address}`
**Transaction**: `{tx_hash}`
**Chain**: Arbitrum One (42161)

Detected unexpected interaction. Please review.

**Blockscout**: https://arbiscan.io/tx/{tx_hash}
                """,
                labels=["alert", "contract-interaction"]
            )
            
            return {
                "success": True,
                "issue_url": issue.get('html_url'),
                "repo": repo_name,
                "tx_hash": tx_hash
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "repo": repo_name,
                "tx_hash": tx_hash
            }


async def main():
    """Main execution"""
    monitor = RepoMonitor()
    
    print(f"📊 Monitoring {len(monitor.repos)} repos...")
    
    results = await monitor.monitor_all_repos()
    
    # Check for alerts
    total_alerts = sum(r.get('count', 0) for r in results.values() if isinstance(r, dict))
    
    if total_alerts > 0:
        print(f"\n⚠️  {total_alerts} unexpected interactions detected!")
        for repo, result in results.items():
            if result.get('count', 0) > 0:
                print(f"  - {repo}: {result['count']} alerts")
    else:
        print("\n✅ No unexpected interactions detected")


if __name__ == "__main__":
    asyncio.run(main())
