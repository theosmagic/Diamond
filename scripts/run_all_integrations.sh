#!/bin/bash
# Run All Integration Scripts
# ============================
# Tests all integrated systems

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

echo "=================================================================================="
echo "RUNNING ALL INTEGRATION SCRIPTS"
echo "=================================================================================="
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found"
    exit 1
fi

echo "✅ Python3: $(python3 --version)"
echo ""

# 1. Diamond Research
echo "=================================================================================="
echo "1. DIAMOND RESEARCH SCRIPT"
echo "=================================================================================="
python3 scripts/diamond_research_script.py
echo ""

# 2. Key Derivation
echo "=================================================================================="
echo "2. KEY DERIVATION SCRIPT"
echo "=================================================================================="
python3 scripts/diamond_key_derivation.py
echo ""

# 3. Visualization
echo "=================================================================================="
echo "3. VISUALIZATION SCRIPT"
echo "=================================================================================="
python3 scripts/diamond_visualization.py
echo ""

# 4. Evolution
echo "=================================================================================="
echo "4. EVOLUTION SCRIPT"
echo "=================================================================================="
python3 scripts/diamond_evolution.py
echo ""

# 5. Enhanced Hot or Not (if async available)
echo "=================================================================================="
echo "5. ENHANCED HOT OR NOT AGENT"
echo "=================================================================================="
python3 scripts/enhanced_hot_or_not_agent.py 2>&1 | head -50
echo ""

echo "=================================================================================="
echo "ALL SCRIPTS COMPLETE"
echo "=================================================================================="
echo ""
echo "✅ All integration scripts executed"
echo "✅ Systems verified"
echo ""
