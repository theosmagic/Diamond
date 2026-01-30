#!/bin/bash
# Deploy Diamond monitoring to Tenderly
# •⟐• Beacon System

set -e

echo "🔺 Deploying Diamond Monitor to Tenderly..."
echo ""

# Check Tenderly CLI
if ! command -v tenderly &> /dev/null; then
    echo "❌ Tenderly CLI not found"
    echo "Install: npm install -g @tenderly/cli"
    exit 1
fi

# Login check
echo "Checking Tenderly authentication..."
tenderly whoami || tenderly login

# Deploy Web3 Action
echo ""
echo "Deploying Web3 Action..."
tenderly actions deploy diamond-monitor \
  --project  \
  --network tenderly-virtual-testnet \
  --contract 0xAB2421868C5F3CCB80D559F3032Fe7Df104DA5FC

# Setup alerts
echo ""
echo "Configuring alerts..."
tenderly alerts create \
  --name "Diamond Ownership Change" \
  --severity critical \
  --event OwnershipTransferred \
  --contract 0xAB2421868C5F3CCB80D559F3032Fe7Df104DA5FC

tenderly alerts create \
  --name "Diamond Cut" \
  --severity high \
  --event DiamondCut \
  --contract 0xAB2421868C5F3CCB80D559F3032Fe7Df104DA5FC

echo ""
echo "✅ Diamond monitoring deployed"
echo "●━━⟐━━●"
