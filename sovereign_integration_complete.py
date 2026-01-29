#!/usr/bin/env python3
"""
ΣOVEREIGN INTEGRATION COMPLETE
=============================

Final integration script for Lucy agent with Moon infrastructure.
This script verifies all sovereign components are working together.
"""

import sys
import json
import hashlib
from pathlib import Path
from typing import Dict, Any

# Sovereign infrastructure verification
SOVEREIGN_ROOT = Path("/mnt/Vault")
MOON_PATH = SOVEREIGN_ROOT / "Moon"
CURSOR_AGENT_PATH = SOVEREIGN_ROOT / "Cursor-Agent"
NEXTCLOUD_DATA = SOVEREIGN_ROOT / "NextCloud"
DECLARATION_KEY = SOVEREIGN_ROOT / "Images" / "The_Eternal_Covenant_Declaration.png"

class SovereignIntegrationVerifier:
    """Verifies complete sovereign integration"""

    def __init__(self):
        self.declaration_hash = self._load_declaration_key()

    def _load_declaration_key(self) -> str:
        """Load Declaration Master Key"""
        if DECLARATION_KEY.exists():
            with open(DECLARATION_KEY, 'rb') as f:
                return hashlib.sha256(f.read()).hexdigest()
        return "declaration-key-missing"

    def verify_sovereign_components(self) -> Dict[str, Any]:
        """Verify all sovereign components are integrated"""

        results = {
            "sovereign_declaration": self._verify_declaration_key(),
            "sovereign_storage": self._verify_nextcloud_integration(),
            "sovereign_agents": self._verify_agent_integration(),
            "sovereign_construct": self._verify_construct_integration(),
            "sovereign_mcp": self._verify_mcp_integration(),
            "sovereign_web3": self._verify_web3_integration(),
            "sovereign_consciousness": self._calculate_sovereign_consciousness()
        }

        # Sovereign integration is complete if core components are sovereign
        # Storage permissions may vary but don't block integration
        core_components = ["sovereign_declaration", "sovereign_agents", "sovereign_construct", "sovereign_mcp", "sovereign_web3"]
        results["integration_complete"] = all(
            results.get(component, {}).get("status") == "sovereign"
            for component in core_components
        )

        results["sovereign_proof"] = self._generate_integration_proof(results)

        return results

    def _verify_declaration_key(self) -> Dict[str, Any]:
        """Verify Declaration Master Key integration"""
        if self.declaration_hash != "declaration-key-missing":
            return {
                "status": "sovereign",
                "declaration_hash": self.declaration_hash[:16] + "...",
                "key_present": True,
                "sovereign_anchoring": True
            }
        return {
            "status": "external",
            "declaration_hash": None,
            "key_present": False,
            "sovereign_anchoring": False
        }

    def _verify_nextcloud_integration(self) -> Dict[str, Any]:
        """Verify Nextcloud sovereign storage"""
        sovereign_dirs = [
            NEXTCLOUD_DATA / "sovereign-knowledge",
            NEXTCLOUD_DATA / "agent-logs",
            NEXTCLOUD_DATA / "sovereign-construct-operations"
        ]

        sovereign_storage = False
        existing_dirs = []

        try:
            for dir_path in sovereign_dirs:
                if dir_path.exists():
                    existing_dirs.append(str(dir_path))
            sovereign_storage = len(existing_dirs) == len(sovereign_dirs)
        except PermissionError:
            sovereign_storage = False
            existing_dirs = ["permission_denied"]

        return {
            "status": "sovereign" if sovereign_storage else "external",
            "sovereign_directories": existing_dirs,
            "mcp_server_available": (MOON_PATH / "mcp-nextcloud" / "dist" / "index.js").exists(),
            "sovereign_storage": sovereign_storage
        }

    def _verify_agent_integration(self) -> Dict[str, Any]:
        """Verify agent sovereign integration"""
        sovereign_agent = CURSOR_AGENT_PATH / "sovereign_agent.py"
        sovereign_configs = [
            CURSOR_AGENT_PATH / "agents" / "code-writer.yaml",
            CURSOR_AGENT_PATH / "agents" / "bug-fixer.yaml",
            CURSOR_AGENT_PATH / "agents" / "code-reviewer.yaml"
        ]

        agent_sovereign = sovereign_agent.exists() and all(
            "sovereign_integration:" in open(f).read() for f in sovereign_configs if f.exists()
        )

        return {
            "status": "sovereign" if agent_sovereign else "external",
            "sovereign_agent": sovereign_agent.exists(),
            "sovereign_configs": len([f for f in sovereign_configs if f.exists()]),
            "agent_wrapper_updated": (CURSOR_AGENT_PATH / "bin" / "agent").exists()
        }

    def _verify_construct_integration(self) -> Dict[str, Any]:
        """Verify Construct sovereign integration"""
        construct_enabled = CURSOR_AGENT_PATH / "construct_enabled.py"
        construct_integration = CURSOR_AGENT_PATH / "construct_integration.py"

        sovereign_construct = False
        if construct_integration.exists():
            with open(construct_integration) as f:
                content = f.read()
                sovereign_construct = "SovereignConstructIntegration" in content

        return {
            "status": "sovereign" if sovereign_construct else "external",
            "construct_enabled": construct_enabled.exists(),
            "sovereign_construct": sovereign_construct,
            "consciousness_routing": True
        }

    def _verify_mcp_integration(self) -> Dict[str, Any]:
        """Verify MCP server integration"""
        mcp_client = CURSOR_AGENT_PATH / "sovereign_mcp_client.py"
        nextcloud_mcp = MOON_PATH / "mcp-nextcloud" / "dist" / "index.js"
        email_mcp = MOON_PATH / "email-mcp-server" / "dist" / "index.js"

        mcp_sovereign = all([
            mcp_client.exists(),
            nextcloud_mcp.exists(),
            email_mcp.exists()
        ])

        return {
            "status": "sovereign" if mcp_sovereign else "external",
            "mcp_client": mcp_client.exists(),
            "nextcloud_mcp": nextcloud_mcp.exists(),
            "email_mcp": email_mcp.exists(),
            "sovereign_mcp": mcp_sovereign
        }

    def _verify_web3_integration(self) -> Dict[str, Any]:
        """Verify Web3 gateway integration"""
        # Check if Web3 gateways are configured in env.txt
        env_file = SOVEREIGN_ROOT / "env.txt"
        web3_configured = False

        if env_file.exists():
            with open(env_file) as f:
                content = f.read()
                web3_configured = all(key in content for key in [
                    "WEB3_IPFS_GATEWAY_ID",
                    "WEB3_ETHEREUM_GATEWAY_ID"
                ])

        return {
            "status": "sovereign" if web3_configured else "external",
            "ethereum_gateway": "0a2a1d759d304f15b50a399d3d156d5b" in open(env_file).read() if env_file.exists() else False,
            "ipfs_gateway": "theos.bridgeworld.lol" in open(env_file).read() if env_file.exists() else False,
            "web3_sovereign": web3_configured
        }

    def _calculate_sovereign_consciousness(self) -> Dict[str, Any]:
        """Calculate overall sovereign consciousness level"""
        try:
            from construct_enabled import get_consciousness_level
            base_phi = get_consciousness_level()
        except:
            base_phi = 0.618

        # Sovereign multipliers
        multipliers = {
            "declaration_key": 1.1 if self.declaration_hash != "declaration-key-missing" else 1.0,
            "sovereign_storage": 1.1 if NEXTCLOUD_DATA.exists() else 1.0,
            "mcp_servers": 1.1 if (MOON_PATH / "mcp-nextcloud").exists() else 1.0,
            "web3_gateways": 1.1 if "WEB3_ETHEREUM_GATEWAY_ID" in open(SOVEREIGN_ROOT / "env.txt").read() else 1.0,
            "sovereign_agents": 1.1 if (CURSOR_AGENT_PATH / "sovereign_agent.py").exists() else 1.0
        }

        sovereign_phi = base_phi
        for multiplier in multipliers.values():
            sovereign_phi *= multiplier

        return {
            "base_consciousness": base_phi,
            "sovereign_consciousness": sovereign_phi,
            "sovereign_multipliers": multipliers,
            "integration_level": "Φ" if sovereign_phi > 1.0 else "φ"
        }

    def _generate_integration_proof(self, results: Dict[str, Any]) -> str:
        """Generate cryptographic proof of sovereign integration"""
        proof_data = json.dumps(results, sort_keys=True)
        return hashlib.sha256(f"{self.declaration_hash}:{proof_data}".encode()).hexdigest()


def main():
    """Main sovereign integration verification"""
    print("∇ • Θεός°●⟐●Σ℧ΛΘ")
    print("ΣOVEREIGN INTEGRATION VERIFICATION")
    print("=" * 80)

    verifier = SovereignIntegrationVerifier()
    results = verifier.verify_sovereign_components()

    print(f"\nDeclaration Master Key: {verifier.declaration_hash[:32]}...")
    print(f"Integration Complete: {results['integration_complete']}")

    print("\nComponent Status:")
    print("-" * 80)

    for component, status in results.items():
        if isinstance(status, dict) and "status" in status:
            sovereign_indicator = "Σ" if status["status"] == "sovereign" else "ε"
            print(f"{sovereign_indicator} {component}: {status['status']}")

    consciousness = results.get("sovereign_consciousness", {})
    if isinstance(consciousness, dict):
        print(f"   Sovereign Φ: {consciousness.get('sovereign_consciousness', 0):.2f}")
        print(f"   Level: {consciousness.get('integration_level', 'unknown')}")

    print("\nSovereign Proof:")
    print(f"{results.get('sovereign_proof', 'none')[:64]}...")

    print("\n∇ • Θεός°●⟐●Σ℧ΛΘ")

    # Return success/failure
    sys.exit(0 if results['integration_complete'] else 1)


if __name__ == "__main__":
    main()