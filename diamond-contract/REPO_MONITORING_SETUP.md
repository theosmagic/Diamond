# 📊 65 Repos Monitoring Setup

## Overview

Monitor all 65 repos for unexpected contract interactions and deployment failures using Blockscout + GitHub integration.

## Monitoring Strategy

### 1. Contract Address Mapping

Each repo may have associated contracts. Map them:

```json
{
  "spellcaster-facets": {
    "contracts": ["0x..."],
    "chain": 42161,
    "monitor": true
  },
  "treasure-marketplace-contracts": {
    "contracts": ["0x09986B4e255B3c548041a30A2Ee312Fe176731c2"],
    "chain": 42161,
    "monitor": true
  },
  ...
}
```

### 2. Alert Conditions

**Unexpected Interactions**:
- Failed transactions
- Large value transfers (> threshold)
- Unknown sender addresses
- Unusual gas usage
- Contract upgrades

**Deployment Failures**:
- Transaction reverts
- Out of gas errors
- Contract verification failures

### 3. GitHub Integration

**On Alert**:
1. Create GitHub Issue in relevant repo
2. Create Gist with transaction details
3. Update repo README with alert status
4. Notify via GitHub Actions

## Implementation

### Repo Monitor Script
**File**: `integrations/repo_monitor.py` ✅

**Features**:
- Monitors all 65 repos
- Detects unexpected interactions
- Creates GitHub issues
- Logs to Gists

### Usage

```python
from integrations.repo_monitor import RepoMonitor

monitor = RepoMonitor()

# Monitor all repos
results = await monitor.monitor_all_repos()

# Monitor specific repo
result = await monitor.monitor_repo_contracts("spellcaster-facets")

# Alert on unexpected
await monitor.alert_on_unexpected(
    repo_name="treasure-project-contracts",
    contract_address="0x...",
    tx_hash="0x..."
)
```

## Configuration

### 1. Contract Addresses

Create `config/repo_contracts.json`:
```json
{
  "repos": {
    "spellcaster-facets": {
      "contracts": ["0x..."],
      "chain_id": 42161
    },
    ...
  }
}
```

### 2. Alert Thresholds

```json
{
  "thresholds": {
    "large_transfer": "1000000000000000000",  // 1 ETH
    "gas_limit": "5000000",
    "failed_tx": true
  }
}
```

### 3. GitHub Configuration

- Personal Access Token (PAT) ✅ (from env.txt)
- Repo permissions
- Issue templates
- Label configuration

## Automation

### GitHub Actions Workflow

```yaml
name: Repo Monitoring
on:
  schedule:
    - cron: '*/5 * * * *'  # Every 5 minutes
  workflow_dispatch:

jobs:
  monitor:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Monitor
        run: python3 integrations/repo_monitor.py
      - name: Create Issues
        if: failure()
        uses: actions/github-script@v6
```

## Next Steps

1. **Map Contract Addresses** - Create config file
2. **Set Up Monitoring** - Configure thresholds
3. **Test Alerts** - Verify GitHub integration
4. **Automate** - Set up GitHub Actions
5. **Integrate with Diamond** - Create monitoring facets

---

**Status**: Monitoring system ready ✅  
**Next**: Configure contract addresses and thresholds
