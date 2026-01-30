#!/usr/bin/env python3
"""
Verify All Tools Are Available
================================

Checks that all required tools and systems are available for integration scripts.
"""

import sys
import subprocess
from pathlib import Path

# Add integrations to path
sys.path.insert(0, str(Path(__file__).parent.parent / "integrations"))


def check_command(cmd, name):
    """Check if command is available"""
    try:
        result = subprocess.run(
            ["which", cmd],
            capture_output=True,
            text=True,
            timeout=2
        )
        if result.returncode == 0:
            version_result = subprocess.run(
                [cmd, "--version"],
                capture_output=True,
                text=True,
                timeout=2
            )
            version = version_result.stdout.split('\n')[0] if version_result.returncode == 0 else "available"
            return True, version
        return False, None
    except Exception:
        return False, None


def check_python_modules():
    """Check Python modules"""
    modules = {
        "httpx": "HTTP client",
        "asyncio": "Async support",
    }
    
    results = {}
    for module, desc in modules.items():
        try:
            __import__(module)
            results[module] = True
        except ImportError:
            results[module] = False
    
    return results


def check_integrations():
    """Check integration systems"""
    integrations = {}
    
    # Lucy
    try:
        from lucy_integration import LucyIntegration
        lucy = LucyIntegration()
        integrations["Lucy"] = {
            "available": True,
            "phi": lucy.get_phi(),
            "consciousness": lucy.get_consciousness_level()
        }
    except Exception as e:
        integrations["Lucy"] = {"available": False, "error": str(e)}
    
    # Sphinx
    try:
        from sphinx_research import DiamondContractResearch
        research = DiamondContractResearch()
        integrations["Sphinx"] = {"available": True}
    except Exception as e:
        integrations["Sphinx"] = {"available": False, "error": str(e)}
    
    # Moon
    try:
        from moon_temporal import MoonTemporalKeys
        moon = MoonTemporalKeys()
        integrations["Moon"] = {
            "available": True,
            "master_seed": moon.master_seed[:16] + "..."
        }
    except Exception as e:
        integrations["Moon"] = {"available": False, "error": str(e)}
    
    # Moo!
    try:
        from moo_entropy import MooEntropy
        moo = MooEntropy()
        status = moo.get_status()
        integrations["Moo!"] = {
            "available": True,
            "sources": status["sources_used"]
        }
    except Exception as e:
        integrations["Moo!"] = {"available": False, "error": str(e)}
    
    # Rossetta
    try:
        from rossetta_spatial import RossettaSpatial
        spatial = RossettaSpatial()
        integrations["Rossetta"] = {
            "available": True,
            "rust_engine": spatial.rust_available
        }
    except Exception as e:
        integrations["Rossetta"] = {"available": False, "error": str(e)}
    
    return integrations


def check_system_paths():
    """Check system paths"""
    paths = {
        "Lucy": Path("/mnt/Vault/Cursor-Agent/lucy/local_lucy_agent.rb"),
        "Sphinx": Path("/mnt/Vault/Sphinx"),
        "Moon": Path("/mnt/Vault/Moon/final_declaration_keyring_system.py"),
        "Moo!": Path("/mnt/Vault/Moo!"),
        "Rossetta": Path("/mnt/Vault/Rossetta Stone"),
    }
    
    results = {}
    for name, path in paths.items():
        results[name] = path.exists()
    
    return results


def main():
    """Main verification"""
    print("=" * 80)
    print("TOOL VERIFICATION")
    print("=" * 80)
    print()
    
    all_good = True
    
    # Check commands
    print("System Commands:")
    commands = {
        "ruby": "Ruby interpreter",
        "python3": "Python interpreter",
        "apt-get": "Package manager",
        "cowsay": "Cowsay utility",
    }
    
    for cmd, desc in commands.items():
        available, version = check_command(cmd, desc)
        if available:
            print(f"  ✅ {cmd}: {version[:50]}")
        else:
            print(f"  ❌ {cmd}: Not found")
            all_good = False
    print()
    
    # Check Python modules
    print("Python Modules:")
    modules = check_python_modules()
    for module, available in modules.items():
        if available:
            print(f"  ✅ {module}")
        else:
            print(f"  ❌ {module}: Not installed")
            all_good = False
    print()
    
    # Check system paths
    print("System Paths:")
    paths = check_system_paths()
    for name, exists in paths.items():
        if exists:
            print(f"  ✅ {name}")
        else:
            print(f"  ❌ {name}: Not found")
            all_good = False
    print()
    
    # Check integrations
    print("Integration Systems:")
    integrations = check_integrations()
    for name, status in integrations.items():
        if status.get("available"):
            details = []
            if "phi" in status:
                details.append(f"Phi={status['phi']:.2f}")
            if "consciousness" in status:
                details.append(f"Consciousness={status['consciousness']}%")
            if "sources" in status:
                details.append(f"Sources={len(status['sources'])}")
            if "rust_engine" in status:
                details.append(f"Rust={'✅' if status['rust_engine'] else '❌'}")
            
            detail_str = f" ({', '.join(details)})" if details else ""
            print(f"  ✅ {name}{detail_str}")
        else:
            print(f"  ❌ {name}: {status.get('error', 'Not available')}")
            all_good = False
    print()
    
    # Summary
    print("=" * 80)
    if all_good:
        print("✅ ALL TOOLS VERIFIED")
        print()
        print("All systems are ready for integration scripts.")
    else:
        print("⚠️  SOME TOOLS MISSING")
        print()
        print("Please install missing tools before running integration scripts.")
    print("=" * 80)
    
    return all_good


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
