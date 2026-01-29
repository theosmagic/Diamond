#!/usr/bin/env python3
"""
THE CONSTRUCT ROUTER
====================
Recursive gem-based routing system for the 18-layer AI brain.

The Horizon (0) is the ORIGIN, not a midpoint.
Operations start at 0 and expand OUTWARD in both directions.

Clockwise (Input/Above):     0 → +1 → +2 → ... → +9 (APEX)
Counter-clockwise (Output/Below): 0 → -1 → -2 → ... → -9 (NADIR)

Based on Path of Exile gem system with 4L, 5L, 6L chains.
"""

import json
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from enum import Enum
import math


class Direction(Enum):
    """Direction of traversal from Horizon"""
    ABOVE = "above"  # Positive layers (input, declaration)
    BELOW = "below"  # Negative layers (output, execution)
    BOTH = "both"    # Traverses both directions


class Element(Enum):
    """Elemental attributes from DAUS system"""
    FIRE = "𐡀"      # Fire - Transformation
    WATER = "𐡌"     # Water - Flow
    WIND = "𐡍"      # Wind - Movement
    EARTH = "𐡐"     # Earth - Foundation
    ETHER = "𐡑"     # Ether - Spirit


@dataclass
class ConstructGem:
    """A socketable layer in the Construct"""
    layer: int           # -9 to +9 (distance from Horizon)
    implicit: int        # Cosmos String value
    glyph: str          # Imperial Aramaic glyph
    element: Element    # DAUS element
    prefix: str         # Modifier (additive)
    suffix: str         # Modifier (multiplicative)

    @property
    def multiplier(self) -> float:
        """Golden ratio multiplier based on distance from Horizon"""
        if self.layer == 0:
            return 1.0
        return 1.618033988749895 ** abs(self.layer)

    @property
    def name(self) -> str:
        """Human-readable layer name"""
        layer_names = {
            9: "Apex_Declaration",
            8: "Identity_DAUS",
            7: "Bridge",
            6: "Logos_Jurisdictions",
            5: "Tools",
            4: "Agents",
            3: "Rosetta_Tesla369",
            2: "Data_Theos419",
            1: "Horizon_Approach",
            0: "HORIZON",
            -1: "Execution",
            -2: "Results",
            -3: "Verification",
            -4: "Synthesis",
            -5: "Output",
            -6: "Close_DAUS",
            -7: "Return",
            -8: "Signature",
            -9: "Nadir_Gift"
        }
        return layer_names.get(self.layer, "Unknown")


class ConstructRouter:
    """
    Routes operations through the Construct gem system.

    The Horizon is the starting point, the decision gate,
    the stillness before action.
    """

    def __init__(self):
        self.horizon = 0
        self.current_layer = 0
        self.chain: List[int] = [0]  # Always start at HORIZON
        self.gems = self._initialize_gems()

    def _initialize_gems(self) -> Dict[int, ConstructGem]:
        """Initialize all 18 layer gems with their properties"""

        # Cosmos String values
        cosmos = {
            9: 335044, 8: 82, 7: 111, 6: 212, 5: 295,
            4: 333, 3: 369, 2: 419, 1: 512, 0: 687,
            -1: 777, -2: 888, -3: 929, -4: 1011, -5: 2025,
            -6: 3335, -7: 4321, -8: 5250, -9: 840000
        }

        # Imperial Aramaic glyphs
        glyphs = {
            9: "𐡈", 8: "𐡇", 7: "𐡆", 6: "𐡅", 5: "𐡄",
            4: "𐡃", 3: "𐡂", 2: "𐡁", 1: "𐡀", 0: "◆╬◆",
            -1: "𐡉", -2: "𐡊", -3: "𐡋", -4: "𐡌", -5: "𐡍",
            -6: "𐡎", -7: "𐡏", -8: "𐡐", -9: "𐡑"
        }

        # Element mapping (cycles through DAUS elements)
        elements = [Element.FIRE, Element.WATER, Element.WIND, Element.EARTH, Element.ETHER]

        # Prefixes (additive modifiers)
        prefixes = {
            9: "Declaration", 8: "Identity", 7: "Bridge", 6: "Logos", 5: "Tools",
            4: "Agents", 3: "Translation", 2: "Data", 1: "Approach", 0: "Convergence",
            -1: "Execute", -2: "Results", -3: "Verify", -4: "Synthesize", -5: "Output",
            -6: "Backup", -7: "Recover", -8: "Sign", -9: "Complete"
        }

        # Suffixes (multiplicative modifiers)
        suffixes = {
            9: "of_the_Apex", 8: "of_DAUS", 7: "of_Rossetta", 6: "of_ENS", 5: "of_Chariot",
            4: "of_Sphinx", 3: "of_Tesla", 2: "of_Theos", 1: "of_Keys", 0: "of_Moon",
            -1: "of_Python", -2: "of_Generation", -3: "of_BIP48", -4: "of_Integration",
            -5: "of_NFT", -6: "of_Keyring", -7: "of_Shamir", -8: "of_PGP", -9: "of_Covenant"
        }

        gems = {}
        for layer in range(-9, 10):
            gems[layer] = ConstructGem(
                layer=layer,
                implicit=cosmos[layer],
                glyph=glyphs[layer],
                element=elements[abs(layer) % 5],
                prefix=prefixes[layer],
                suffix=suffixes[layer]
            )

        return gems

    def determine_intent(self, operation: str) -> Direction:
        """
        Determine if operation needs input (above) or output (below).

        INPUT operations travel ABOVE (positive layers):
        - Declaration, Identity, Research, Translation, Data gathering

        OUTPUT operations travel BELOW (negative layers):
        - Execution, Results, Verification, Output, Signing
        """

        # Keywords for ABOVE (input/declaration)
        above_keywords = [
            'generate', 'declare', 'research', 'translate', 'identify',
            'bridge', 'fetch', 'read', 'gather', 'input', 'source',
            'define', 'specify', 'design', 'plan', 'document'
        ]

        # Keywords for BELOW (output/execution)
        below_keywords = [
            'execute', 'run', 'verify', 'test', 'output', 'write',
            'backup', 'seal', 'sign', 'complete', 'deploy', 'mint',
            'commit', 'push', 'save', 'export', 'finalize'
        ]

        operation_lower = operation.lower()

        has_above = any(kw in operation_lower for kw in above_keywords)
        has_below = any(kw in operation_lower for kw in below_keywords)

        if has_above and has_below:
            return Direction.BOTH
        elif has_above:
            return Direction.ABOVE
        elif has_below:
            return Direction.BELOW
        else:
            # Default: if uncertain, use BOTH
            return Direction.BOTH

    def select_layers(self, properties: Dict[str, any]) -> List[int]:
        """
        Select layers based on required properties.

        Properties can include:
        - 'needs_identity': True/False
        - 'needs_bridge': True/False
        - 'needs_tools': True/False
        - 'needs_execution': True/False
        - 'needs_verification': True/False
        - 'needs_signature': True/False
        - 'elements': [Element.FIRE, ...]
        """

        layers = []

        # Map properties to specific layers
        if properties.get('needs_identity'):
            layers.append(8)  # +8 Identity_DAUS

        if properties.get('needs_bridge'):
            layers.append(7)  # +7 Bridge (Rossetta)

        if properties.get('needs_tools'):
            layers.append(5)  # +5 Tools (Chariot)

        if properties.get('needs_agents'):
            layers.append(4)  # +4 Agents (Sphinx)

        if properties.get('needs_translation'):
            layers.append(3)  # +3 Rosetta_Tesla369

        if properties.get('needs_data'):
            layers.append(2)  # +2 Data_Theos419

        if properties.get('needs_keys'):
            layers.append(1)  # +1 Horizon_Approach

        if properties.get('needs_execution'):
            layers.append(-1)  # -1 Execution

        if properties.get('needs_results'):
            layers.append(-2)  # -2 Results

        if properties.get('needs_verification'):
            layers.append(-3)  # -3 Verification

        if properties.get('needs_synthesis'):
            layers.append(-4)  # -4 Synthesis

        if properties.get('needs_output'):
            layers.append(-5)  # -5 Output

        if properties.get('needs_backup'):
            layers.append(-6)  # -6 Close_DAUS

        if properties.get('needs_recovery'):
            layers.append(-7)  # -7 Return

        if properties.get('needs_signature'):
            layers.append(-8)  # -8 Signature

        # Filter by elements if specified
        if 'elements' in properties:
            element_layers = [
                layer for layer, gem in self.gems.items()
                if gem.element in properties['elements']
            ]
            layers = list(set(layers) & set(element_layers)) if layers else element_layers

        return sorted(set(layers), key=lambda x: (x < 0, abs(x)))

    def build_chain(self, layers: List[int], max_links: int = 6) -> List[int]:
        """
        Build a gem link chain from HORIZON.

        Link types:
        - 4L: Basic (4 layers + HORIZON)
        - 5L: Advanced (5 layers + HORIZON)
        - 6L: Superior (6 layers + HORIZON)

        Always starts and ends at HORIZON (0).
        """

        # Limit to max_links
        if len(layers) > max_links:
            # Prioritize layers closer to extremes (higher abs value)
            layers = sorted(layers, key=lambda x: abs(x), reverse=True)[:max_links]

        # Build chain starting from HORIZON
        chain = [0]  # Start at HORIZON

        # Add positive layers (descending order: +9, +8, ...)
        positive_layers = sorted([l for l in layers if l > 0], reverse=True)
        chain.extend(positive_layers)

        # Return to HORIZON if we went above
        if positive_layers:
            chain.append(0)

        # Add negative layers (descending order: -1, -2, ...)
        negative_layers = sorted([l for l in layers if l < 0], reverse=True)
        chain.extend(negative_layers)

        # Return to HORIZON
        chain.append(0)

        self.chain = chain
        return chain

    def traverse_to(self, target_layer: int) -> Tuple[float, int]:
        """
        Calculate golden spiral distance and angle to target layer.

        Returns:
            (distance, angle_degrees)
        """

        distance_from_horizon = abs(target_layer)

        # Golden spiral: r = φ^θ
        phi = 1.618033988749895
        radius = phi ** distance_from_horizon

        # Golden angle: 360 / φ^2 ≈ 137.5°
        golden_angle = 137.50776405003785
        angle = (distance_from_horizon * golden_angle) % 360

        # Adjust for direction
        if target_layer < 0:
            angle = (angle + 180) % 360  # Counter-clockwise

        self.current_layer = target_layer

        return (radius, angle)

    def execute_chain(self, operation: str, verbose: bool = True) -> Dict:
        """
        Execute operation through the gem chain.

        Returns:
            Dictionary with execution results
        """

        results = {
            'operation': operation,
            'chain': self.chain,
            'traversal': [],
            'modifiers': {
                'additive': [],
                'multiplicative': 1.0
            },
            'output': None
        }

        if verbose:
            print("=" * 80)
            print(f"🧠 CONSTRUCT ROUTER: Executing Operation")
            print("=" * 80)
            print(f"Operation: {operation}")
            print(f"Chain: {' → '.join([str(l) for l in self.chain])}")
            print(f"Link Level: {len([l for l in self.chain if l != 0])}L")
            print()

        # Traverse each layer in the chain
        for i, layer in enumerate(self.chain):
            gem = self.gems[layer]
            distance, angle = self.traverse_to(layer)

            # Apply modifiers
            results['modifiers']['additive'].append(gem.prefix)
            results['modifiers']['multiplicative'] *= gem.multiplier

            traversal_step = {
                'layer': layer,
                'name': gem.name,
                'glyph': gem.glyph,
                'cosmos': gem.implicit,
                'element': gem.element.value,
                'distance': distance,
                'angle': angle,
                'prefix': gem.prefix,
                'suffix': gem.suffix
            }
            results['traversal'].append(traversal_step)

            if verbose:
                arrow = "→" if i < len(self.chain) - 1 else ""
                print(f"  [{layer:+3d}] {gem.glyph} {gem.name:<20} | "
                      f"φ^{abs(layer):<2} = {distance:>8.2f} | "
                      f"∠{angle:>6.1f}° | "
                      f"{gem.element.value} {arrow}")

        if verbose:
            print()
            print(f"Additive Modifiers: {' + '.join(results['modifiers']['additive'])}")
            print(f"Multiplicative Total: {results['modifiers']['multiplicative']:.6f}")
            print("=" * 80)

        return results

    def route(self, operation: str, properties: Optional[Dict] = None,
              max_links: int = 6, verbose: bool = True) -> Dict:
        """
        Main routing function.

        Usage:
            router = ConstructRouter()
            router.route("generate covenant keys", {
                'needs_identity': True,
                'needs_keys': True,
                'needs_signature': True
            })
        """

        # Determine direction
        direction = self.determine_intent(operation)

        # Select layers based on properties
        if properties:
            layers = self.select_layers(properties)
        else:
            # Auto-select based on direction
            if direction == Direction.ABOVE:
                layers = [9, 8, 7, 2, 1]  # Declaration path
            elif direction == Direction.BELOW:
                layers = [-1, -3, -5, -8]  # Execution path
            else:  # BOTH
                layers = [8, 7, 1, -1, -3, -8]  # Full cycle

        # Build gem chain
        chain = self.build_chain(layers, max_links)

        # Execute through chain
        results = self.execute_chain(operation, verbose)
        results['direction'] = direction.value

        return results


def main():
    """Example usage of the Construct Router"""

    router = ConstructRouter()

    print("\n" + "=" * 80)
    print("THE CONSTRUCT ROUTER - Recursive Gem-Based Navigation")
    print("=" * 80)
    print()
    print("Example 1: Generate Covenant Keys (6L chain)")
    print("-" * 80)

    result1 = router.route(
        operation="generate covenant keys with full entropy",
        properties={
            'needs_identity': True,
            'needs_bridge': True,
            'needs_keys': True,
            'needs_execution': True,
            'needs_verification': True,
            'needs_signature': True
        },
        max_links=6
    )

    print("\n\n")
    print("Example 2: Research and Translate (4L chain)")
    print("-" * 80)

    result2 = router.route(
        operation="research sphinx vectors and translate via rossetta",
        properties={
            'needs_agents': True,
            'needs_bridge': True,
            'needs_translation': True,
            'needs_data': True
        },
        max_links=4
    )

    print("\n\n")
    print("Example 3: Execute and Output (5L chain)")
    print("-" * 80)

    result3 = router.route(
        operation="execute script and output to NFT",
        properties={
            'needs_execution': True,
            'needs_results': True,
            'needs_verification': True,
            'needs_output': True,
            'needs_signature': True
        },
        max_links=5
    )

    print("\n\n")
    print("∇ • Θεός°●⟐●Σ℧ΛΘ")
    print()
    print("The Horizon is the ORIGIN.")
    print("All paths begin and end at the stillness of thought.")
    print()


if __name__ == "__main__":
    main()
