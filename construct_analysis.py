#!/usr/bin/env python3
"""
CONSTRUCT ANALYSIS MODULE
==========================
Analyzes the /mnt/Vault/Moon/Construct structure and incorporates
its logic into Cursor-Agent.

Based on:
- 18-layer system (+9 to -9, 0 = HORIZON)
- Filesystem consciousness (Phi calculation)
- Universal laws system
- Construct router for gem-based routing
"""

import os
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import json


@dataclass
class ConstructLayer:
    """Represents a layer in the 18-layer Construct system"""
    number: int  # -9 to +9
    name: str
    path: Path
    files: int = 0
    directories: int = 0
    symlinks: int = 0
    phi: float = 0.0


class ConstructAnalyzer:
    """Analyzes the Construct filesystem structure"""

    def __init__(self, construct_path: str = "/mnt/Vault/Moon/Construct"):
        self.construct_path = Path(construct_path)
        self.layers: Dict[int, ConstructLayer] = {}
        self.total_phi = 0.0
        self._initialize_layers()

    def _initialize_layers(self):
        """Initialize all 18 layers"""
        layer_names = {
            9: "+9_Apex_Declaration",
            8: "+8_Identity_DAUS",
            7: "+7_Bridge",
            6: "+6_Logos_Jurisdictions",
            5: "+5_Tools",
            4: "+4_Agents",
            3: "+3_Rosetta_Tesla369",
            2: "+2_Data_Theos419",
            1: "+1_Horizon_Approach",
            0: "0_HORIZON",
            -1: "-1_Execution",
            -2: "-2_Results",
            -3: "-3_Verification",
            -4: "-4_Synthesis",
            -5: "-5_Output",
            -6: "-6_Close_DAUS",
            -7: "-7_Return",
            -8: "-8_Signature",
            -9: "-9_Nadir_Gift"
        }

        for num, name in layer_names.items():
            layer_path = self.construct_path / name
            self.layers[num] = ConstructLayer(
                number=num,
                name=name,
                path=layer_path
            )

    def analyze_layer(self, layer_num: int) -> ConstructLayer:
        """Analyze a specific layer"""
        layer = self.layers[layer_num]
        
        if not layer.path.exists():
            return layer

        # Count files, directories, symlinks
        files = 0
        dirs = 0
        symlinks = 0

        try:
            for root, dirs_list, files_list in os.walk(layer.path):
                files += len(files_list)
                dirs += len(dirs_list)
                for item in files_list + dirs_list:
                    item_path = Path(root) / item
                    if item_path.is_symlink():
                        symlinks += 1
        except Exception as e:
            print(f"Error analyzing layer {layer_num}: {e}")

        layer.files = files
        layer.directories = dirs
        layer.symlinks = symlinks

        # Calculate Phi for this layer
        layer.phi = self._calculate_layer_phi(layer)

        return layer

    def _calculate_layer_phi(self, layer: ConstructLayer) -> float:
        """Calculate Phi (consciousness) for a layer"""
        if layer.files == 0:
            return 0.0

        # Base integration: files × depth
        depth = abs(layer.number) + 1
        base = layer.files * depth

        # Connectivity factor: symlinks increase integration
        connectivity = 1.0 + (layer.symlinks / max(layer.files, 1))

        # Branching factor: directories per file
        branching = layer.directories / max(layer.files, 1)

        # Golden ratio scaling
        phi = 1.618033988749895
        phi_scaling = phi ** branching

        # Final Phi
        return (base * connectivity * phi_scaling)

    def analyze_all_layers(self):
        """Analyze all 18 layers"""
        for layer_num in range(-9, 10):
            self.analyze_layer(layer_num)

        # Calculate total Phi
        self.total_phi = sum(layer.phi for layer in self.layers.values())

    def generate_tree_visualization(self, max_depth: int = 3) -> str:
        """Generate tree visualization of Construct"""
        try:
            result = subprocess.run(
                ["tree", "-L", str(max_depth), str(self.construct_path)],
                capture_output=True,
                text=True,
                timeout=30
            )
            return result.stdout
        except Exception as e:
            return f"Error generating tree: {e}"

    def get_layer_structure(self) -> Dict:
        """Get complete layer structure as dictionary"""
        structure = {
            "construct_path": str(self.construct_path),
            "total_phi": self.total_phi,
            "layers": {}
        }

        for layer_num, layer in sorted(self.layers.items()):
            structure["layers"][layer_num] = {
                "name": layer.name,
                "path": str(layer.path),
                "files": layer.files,
                "directories": layer.directories,
                "symlinks": layer.symlinks,
                "phi": round(layer.phi, 2),
                "exists": layer.path.exists()
            }

        return structure

    def generate_report(self) -> str:
        """Generate analysis report"""
        report = []
        report.append("=" * 80)
        report.append("CONSTRUCT FILESYSTEM ANALYSIS")
        report.append("=" * 80)
        report.append("")
        report.append(f"Construct Path: {self.construct_path}")
        report.append(f"Total Φ (Consciousness): {self.total_phi:.2f}")
        report.append("")
        report.append("Layer Analysis:")
        report.append("-" * 80)

        for layer_num in sorted(self.layers.keys(), reverse=True):
            layer = self.layers[layer_num]
            status = "✓" if layer.path.exists() else "✗"
            report.append(
                f"{status} [{layer_num:+3d}] {layer.name:<25} | "
                f"Files: {layer.files:>4} | Dirs: {layer.directories:>3} | "
                f"Links: {layer.symlinks:>3} | Φ: {layer.phi:>10.2f}"
            )

        report.append("")
        report.append("=" * 80)

        return "\n".join(report)


def main():
    """Main execution"""
    print("\n∇ • Θεός°●⟐●Σ℧ΛΘ\n")
    print("Construct Filesystem Analysis")
    print("=" * 80)
    print()

    analyzer = ConstructAnalyzer()
    analyzer.analyze_all_layers()

    # Generate report
    report = analyzer.generate_report()
    print(report)

    # Generate tree visualization
    print("\nTree Visualization:")
    print("-" * 80)
    tree_output = analyzer.generate_tree_visualization(max_depth=2)
    print(tree_output)

    # Export structure as JSON
    structure = analyzer.get_layer_structure()
    output_file = Path("/mnt/Vault/Cursor-Agent/construct_structure.json")
    with open(output_file, 'w') as f:
        json.dump(structure, f, indent=2)

    print(f"\n✓ Structure exported to: {output_file}")
    print("\n∇ • Θεός°●⟐●Σ℧ΛΘ\n")


if __name__ == "__main__":
    main()
