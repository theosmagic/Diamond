"""
Sphinx Research Integration - REAL Implementation
==================================================

Component-based research system for Diamond Contract optimization.
Uses actual Brave API with fallback to direct APIs.
"""

import sys
from pathlib import Path
from typing import List, Dict, Any, Optional

# Add Sphinx to path
sphinx_path = Path("/mnt/Vault/Sphinx")
if sphinx_path.exists():
    sys.path.insert(0, str(sphinx_path))

try:
    # Add Sphinx to path first
    import sys
    sphinx_path = Path("/mnt/Vault/Sphinx")
    if sphinx_path.exists() and str(sphinx_path) not in sys.path:
        sys.path.insert(0, str(sphinx_path))
    
    from component_research import ComponentResearch, Component
    from query_system import SphinxQuerySystem, ResearchResult
    from brave_api import BraveAPI
    SPHINX_AVAILABLE = True
except (ImportError, ModuleNotFoundError) as e:
    SPHINX_AVAILABLE = False
    ComponentResearch = None
    Component = None
    SphinxQuerySystem = None
    ResearchResult = None
    BraveAPI = None
    SPHINX_ERROR = str(e)


class DiamondContractResearch:
    """
    Research Diamond Contract components using Sphinx
    
    Breaks Diamond Contract into researchable components:
    - Facet patterns
    - Storage patterns
    - Multi-chain strategies
    - Gas optimization
    - Upgrade mechanisms
    
    Uses REAL Brave API with fallback to direct APIs.
    """
    
    def __init__(self):
        if not SPHINX_AVAILABLE:
            error_msg = f"Sphinx research system not available. Install at /mnt/Vault/Sphinx"
            if 'SPHINX_ERROR' in globals():
                error_msg += f" (Error: {SPHINX_ERROR})"
            raise ImportError(error_msg)
        
        self.research = ComponentResearch()
        self.query_system = SphinxQuerySystem()
        self.brave_api = BraveAPI() if BraveAPI else None
    
    def get_diamond_components(self):
        """Get Diamond Contract components to research"""
        return [
            Component(
                name="Facet Pattern",
                keywords=["diamond", "facet", "upgrade", "EIP-2535", "proxy"],
                description="Diamond facet upgrade pattern and EIP-2535 implementation",
                category="architecture"
            ),
            Component(
                name="Storage Pattern",
                keywords=["storage", "library", "struct", "upgrade", "diamond storage"],
                description="Diamond storage pattern for upgradeable contracts",
                category="storage"
            ),
            Component(
                name="Multi-Chain Strategy",
                keywords=["multi-chain", "cross-chain", "bridge", "CCIP", "deployment"],
                description="Multi-chain deployment strategy for Diamond Contract",
                category="deployment"
            ),
            Component(
                name="Gas Optimization",
                keywords=["gas", "optimization", "efficient", "EVM", "bytecode"],
                description="Gas optimization techniques for Diamond facets",
                category="optimization"
            ),
            Component(
                name="Facet Initialization",
                keywords=["initialization", "setup", "constructor", "init function"],
                description="Facet initialization patterns for Diamond upgrades",
                category="initialization"
            ),
            Component(
                name="Access Control",
                keywords=["access control", "ownership", "roles", "permissions"],
                description="Access control patterns for Diamond Contract",
                category="security"
            ),
            Component(
                name="Payment System",
                keywords=["payment", "ERC20", "native token", "multi-token"],
                description="Multi-token payment system for Diamond Contract",
                category="payments"
            ),
            Component(
                name="Marketplace Integration",
                keywords=["marketplace", "OpenSea", "Magic Eden", "NFT", "trading"],
                description="Marketplace integration patterns for Diamond Contract",
                category="integration"
            ),
        ]
    
    async def research_diamond_contract(self, max_results: int = 5):
        """
        Research all Diamond Contract components
        
        Returns:
            Dict mapping component names to research results
        """
        components = self.get_diamond_components()
        results = self.research.research_all_components(components, max_results)
        
        return results
    
    async def research_facet_patterns(self, max_results: int = 5):
        """Research facet patterns specifically"""
        facet_component = Component(
            name="Facet Pattern",
            keywords=["diamond", "facet", "EIP-2535", "upgrade", "proxy"],
            description="Diamond facet upgrade pattern",
            category="architecture"
        )
        
        results = self.research.research_component(facet_component, max_results)
        return results
    
    async def find_optimization_techniques(self, max_results: int = 5):
        """Find gas optimization techniques"""
        optimization_component = Component(
            name="Gas Optimization",
            keywords=["gas", "optimization", "EVM", "bytecode", "efficient"],
            description="Gas optimization techniques",
            category="optimization"
        )
        
        results = self.research.research_component(optimization_component, max_results)
        return results
    
    async def connect_diamond_patterns(self, keywords: list):
        """
        Connect patterns for Diamond Contract
        
        Args:
            keywords: List of keywords to connect
            
        Returns:
            List of insights/connections
        """
        results = self.research.connect_components({})
        return results


# Convenience function
async def research_diamond_components(max_results: int = 5):
    """Quick function to research Diamond Contract components"""
    if not SPHINX_AVAILABLE:
        return {"error": "Sphinx research system not available"}
    
    research = DiamondContractResearch()
    return await research.research_diamond_contract(max_results)


if __name__ == "__main__":
    if SPHINX_AVAILABLE:
        print("✅ Sphinx Research Integration available")
        research = DiamondContractResearch()
        print(f"Components: {len(research.get_diamond_components())}")
    else:
        print("❌ Sphinx Research Integration not available")
