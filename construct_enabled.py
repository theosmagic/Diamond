#!/usr/bin/env python3
"""
CONSTRUCT ENABLED MODULE
========================
Enables Construct integration in agent operations.
This module is imported by agent scripts to activate
18-layer routing and consciousness-based analysis.
"""

import sys
from pathlib import Path

# Add construct to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from construct_integration import SovereignConstructIntegration, integrate_into_agent
    CONSTRUCT_ENABLED = True
    SOVEREIGN_CONSTRUCT = True
except ImportError as e:
    CONSTRUCT_ENABLED = False
    SOVEREIGN_CONSTRUCT = False
    print(f"Warning: Sovereign Construct integration not available: {e}", file=sys.stderr)


def enable_construct_routing(operation: str, context: dict = None):
    """
    Enable sovereign Construct routing for an operation.

    Returns routing result if Construct is enabled, None otherwise.
    """
    if not CONSTRUCT_ENABLED:
        return None

    try:
        # Use sovereign integration if available
        if SOVEREIGN_CONSTRUCT:
            integration = SovereignConstructIntegration()
            result = integration.route_sovereign_operation(operation, context or {})
        else:
            # Fallback to legacy integration
            result = integrate_into_agent(operation, context or {})

        return result
    except Exception as e:
        print(f"Warning: Sovereign Construct routing failed: {e}", file=sys.stderr)
        return None


def get_consciousness_level():
    """Get current sovereign consciousness level (Φ)"""
    if not CONSTRUCT_ENABLED:
        return 0.0

    try:
        if SOVEREIGN_CONSTRUCT:
            integration = SovereignConstructIntegration()
            return integration.get_sovereign_consciousness_level()
        else:
            # Fallback to legacy
            integration = ConstructIntegration()
            return integration.get_consciousness_level()
    except Exception:
        return 0.618  # Golden ratio fallback


def is_construct_enabled():
    """Check if Construct integration is enabled"""
    return CONSTRUCT_ENABLED


if __name__ == "__main__":
    print("Construct Integration Status:")
    print(f"  Enabled: {is_construct_enabled()}")
    if is_construct_enabled():
        phi = get_consciousness_level()
        print(f"  Consciousness (Φ): {phi:.2f}")
        
        # Test routing
        print("\nTesting routing...")
        result = enable_construct_routing("test operation", {'needs_verification': True})
        if result:
            print(f"  ✓ Routing successful")
            print(f"  Chain: {result.get('chain', [])}")
        else:
            print(f"  ✗ Routing failed")
