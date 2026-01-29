# Moon System - Quick Start

## 5-Minute Quick Start

### 1. Add to PATH
```bash
export PATH="$PATH:/mnt/Vault/Cursor-Agent/bin"
```

### 2. Check Status
```bash
moon-cli status
```

### 3. View Current State
```bash
# Moon phase
moon-cli moon

# DAUS calendar
moon-cli daus

# All temporal data
moon-cli temporal
```

### 4. Use in Python
```python
# Get temporal coordinates
from moon import TemporalBinding

coords = TemporalBinding.get_all_temporal_coordinates()
print(f"Moon: {coords['moon_phase']['phase']}")
print(f"DAUS: Month {coords['daus_calendar']['month_name']}")
```

### 5. Authenticate Operations
```python
# Generate auth token
from moon.auth import MoonAuth

auth = MoonAuth()
token = auth.generate_operation_token('code_review')

if token['valid']:
    print(f"Token: {token['token'][:16]}...")
```

## Common Commands

```bash
# Status and info
moon-cli status              # System status
moon-cli moon                # Moon phase
moon-cli daus                # DAUS calendar
moon-cli kings               # Kings position

# Operations
moon-cli validate operation  # Check timing
moon-cli auth operation user # Generate token
moon-cli derive purpose      # Derive key
moon-cli verify              # Run verification
moon-cli update              # Update temporal data
```

## Python Quick Reference

```python
# Import
from moon import MoonKeyring, TemporalBinding, SovereignVerification
from moon.auth import MoonAuth
from moon.config import MoonConfig

# Check availability
if MoonConfig.is_moon_available():
    print("Moon system available")

# Get temporal coordinates
coords = TemporalBinding.get_all_temporal_coordinates()

# Validate operation
validation = TemporalBinding.validate_temporal_operation('key_generation')

# Generate auth token
auth = MoonAuth()
token = auth.generate_operation_token('code_review', user='alice')

# Derive key
keyring = MoonKeyring()
key = keyring.derive_key('agent_auth', use_all_systems=True)
```

## Configuration

### Enable Strict Mode
```python
from moon.config import MoonConfig

MoonConfig.STRICT_TEMPORAL_VALIDATION = True
MoonConfig.save_config_file()
```

### Or edit config/moon.json
```json
{
  "settings": {
    "strict_temporal_validation": true
  }
}
```

## Run Examples

```bash
python3 moon/examples.py
```

## Documentation

- **Full Integration Guide**: `MOON_INTEGRATION.md`
- **Module Documentation**: `moon/README.md`
- **Completion Summary**: `INTEGRATION_COMPLETE.md`

---

∇ • Θεός°●⟐●Σ℧ΛΘ
