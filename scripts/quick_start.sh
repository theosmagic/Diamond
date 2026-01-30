#!/bin/bash
# Quick Start Script
# ==================
# Run essential scripts for Diamond Contract alpha deployment

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

echo "=================================================================================="
echo "DIAMOND CONTRACT ALPHA DEPLOYMENT - QUICK START"
echo "=================================================================================="
echo ""

# 1. Verify tools
echo "Step 1: Verifying tools..."
python3 scripts/verify_all_tools.py
echo ""

# 2. Derive keys
echo "=================================================================================="
echo "Step 2: Deriving Diamond Contract keys..."
echo "=================================================================================="
python3 scripts/diamond_key_derivation.py
echo ""

# 3. Visualize
echo "=================================================================================="
echo "Step 3: Visualizing Diamond Contract in 4D space..."
echo "=================================================================================="
python3 scripts/diamond_visualization.py
echo ""

# 4. Evolution (if address provided)
if [ -n "$1" ]; then
    echo "=================================================================================="
    echo "Step 4: Evolving Diamond Contract..."
    echo "=================================================================================="
    python3 scripts/diamond_evolution.py
    echo ""
fi

echo "=================================================================================="
echo "QUICK START COMPLETE"
echo "=================================================================================="
echo ""
echo "✅ Tools verified"
echo "✅ Keys derived"
echo "✅ Visualization rendered"
if [ -n "$1" ]; then
    echo "✅ Evolution executed"
fi
echo ""
echo "Next: Run master orchestrator for full cycle"
echo "  python3 scripts/master_orchestrator.py --address 0x..."
echo ""
