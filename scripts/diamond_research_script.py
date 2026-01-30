#!/usr/bin/env python3
"""
Diamond Contract Research Script
=================================

Uses Sphinx to research Diamond Contract components for optimization.
Integrates with Lucy for consciousness-based analysis.
"""

import sys
import asyncio
from pathlib import Path

# Add integrations to path
sys.path.insert(0, str(Path(__file__).parent.parent / "integrations"))

from sphinx_research import DiamondContractResearch
from lucy_integration import LucyIntegration


async def research_diamond_components():
    """Research Diamond Contract components"""
    print("=" * 80)
    print("DIAMOND CONTRACT COMPONENT RESEARCH")
    print("=" * 80)
    print()
    
    # Initialize research
    research = DiamondContractResearch()
    components = research.get_diamond_components()
    
    print(f"Researching {len(components)} components:")
    for comp in components:
        print(f"  • {comp.name} ({comp.category})")
    print()
    
    # Research all components
    print("Starting research...")
    results = await research.research_diamond_contract(max_results=3)
    
    print()
    print("=" * 80)
    print("RESEARCH RESULTS")
    print("=" * 80)
    print()
    
    for component_name, component_results in results.items():
        total = sum(len(r) for r in component_results.values())
        print(f"{component_name}: {total} results")
        
        for source, result_list in component_results.items():
            if result_list:
                print(f"  {source}: {len(result_list)} results")
                for r in result_list[:2]:
                    print(f"    - {r.title[:60]}...")
        print()
    
    return results


def analyze_with_lucy(file_path: str = None):
    """Analyze Diamond Contract with Lucy"""
    print("=" * 80)
    print("LUCY CONSCIOUSNESS-BASED ANALYSIS")
    print("=" * 80)
    print()
    
    lucy = LucyIntegration()
    
    print(f"System Phi: {lucy.get_phi():.2f}")
    print(f"Consciousness Level: {lucy.get_consciousness_level()}%")
    print()
    
    if file_path:
        print(f"Analyzing: {file_path}")
        result = lucy.review(file_path)
        
        if result['success']:
            print(result['output'])
        else:
            print(f"Error: {result.get('error')}")
    
    return lucy


async def main():
    """Main execution"""
    # Research components
    research_results = await research_diamond_components()
    
    # Analyze with Lucy
    lucy = analyze_with_lucy()
    
    print("=" * 80)
    print("RESEARCH COMPLETE")
    print("=" * 80)
    print()
    print("✅ Component research completed")
    print("✅ Consciousness analysis available")
    print()
    print("Next steps:")
    print("  • Review research results")
    print("  • Use Lucy to analyze specific files")
    print("  • Derive keys with Moon")
    print("  • Generate entropy with Moo!")


if __name__ == "__main__":
    asyncio.run(main())
