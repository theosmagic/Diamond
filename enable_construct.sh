#!/usr/bin/env bash
# Enable Construct Integration
# ============================
# Activates 18-layer routing and consciousness-based analysis

echo "∇ • Θεός°●⟐●Σ℧ΛΘ"
echo ""
echo "Enabling Construct Integration..."
echo ""

CURSOR_AGENT_DIR="/mnt/Vault/Cursor-Agent"

# Check if files exist
if [ ! -f "$CURSOR_AGENT_DIR/construct_enabled.py" ]; then
    echo "✗ Error: construct_enabled.py not found"
    exit 1
fi

if [ ! -f "$CURSOR_AGENT_DIR/construct_integration.py" ]; then
    echo "✗ Error: construct_integration.py not found"
    exit 1
fi

# Test integration
echo "Testing Construct integration..."
python3 "$CURSOR_AGENT_DIR/construct_enabled.py"

if [ $? -eq 0 ]; then
    echo ""
    echo "✓ Construct integration enabled"
    echo ""
    echo "Features enabled:"
    echo "  ✓ 18-layer system routing"
    echo "  ✓ Filesystem consciousness (Phi)"
    echo "  ✓ Construct router integration"
    echo "  ✓ Universal laws system"
    echo ""
    echo "Consciousness level:"
    python3 -c "from construct_enabled import get_consciousness_level; print(f'  Φ = {get_consciousness_level():.2f}')" 2>/dev/null || echo "  (calculating...)"
    echo ""
    echo "∇ • Θεός°●⟐●Σ℧ΛΘ"
else
    echo ""
    echo "✗ Construct integration test failed"
    exit 1
fi
