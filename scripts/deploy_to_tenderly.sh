#!/bin/bash
# Deploy contracts to Tenderly Virtual TestNet
# Usage: ./scripts/deploy_to_tenderly.sh

set -e

echo "🚀 Deploying to Tenderly Virtual TestNet..."
echo ""

# Configuration
TENDERLY_RPC="https://virtual.mainnet.us-east.rpc.tenderly.co/ba0e32f8-b5f3-4ca6-a2cc-3ab4fa250000"
PRIMARY_WALLET="0x67A977eaD94C3b955ECbf27886CE9f62464423B2"

# Check if private key is set
if [ -z "$DEPLOYER_PRIVATE_KEY" ]; then
    echo "❌ Error: DEPLOYER_PRIVATE_KEY environment variable not set"
    echo "   Set it with: export DEPLOYER_PRIVATE_KEY=<your_key>"
    exit 1
fi

echo "📍 Target Network: Tenderly Virtual TestNet (Chain ID: 73571)"
echo "📍 Deployer: $PRIMARY_WALLET"
echo ""

# Deploy Diamond (example - adjust as needed)
echo "1️⃣  Deploying Diamond Proxy..."
DIAMOND_ADDRESS=$(cast send \
    --rpc-url "$TENDERLY_RPC" \
    --private-key "$DEPLOYER_PRIVATE_KEY" \
    --create \
    "$(cat contracts/Diamond.sol)" \
    --json | jq -r '.contractAddress')

echo "   ✅ Diamond deployed: $DIAMOND_ADDRESS"
echo ""

# Deploy Signature Verifier
echo "2️⃣  Deploying Signature Verifier..."
VERIFIER_ADDRESS=$(cast send \
    --rpc-url "$TENDERLY_RPC" \
    --private-key "$DEPLOYER_PRIVATE_KEY" \
    --create \
    "$(cat contracts/SignatureVerifier.sol)" \
    --json | jq -r '.contractAddress')

echo "   ✅ Verifier deployed: $VERIFIER_ADDRESS"
echo ""

# Update config
echo "3️⃣  Updating configuration..."
cat > /tmp/deployment_result.json << EOF
{
  "diamond_address": "$DIAMOND_ADDRESS",
  "verifier_address": "$VERIFIER_ADDRESS",
  "network": "tenderly-virtual-testnet",
  "chain_id": 73571,
  "deployer": "$PRIMARY_WALLET",
  "timestamp": "$(date -Iseconds)"
}
EOF

echo "   ✅ Configuration saved to /tmp/deployment_result.json"
echo ""

# Push to Tenderly for monitoring
echo "4️⃣  Registering contracts with Tenderly..."
cd /mnt/Vault/Cursor-Agent
tenderly contracts push --networks 73571

echo ""
echo "✅ DEPLOYMENT COMPLETE"
echo ""
echo "📍 Diamond: $DIAMOND_ADDRESS"
echo "📍 Verifier: $VERIFIER_ADDRESS"
echo ""
echo "🔍 Monitor on Tenderly:"
echo "   https://dashboard.tenderly.co/Ua_0357/project/testnet"
