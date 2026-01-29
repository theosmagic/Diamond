# Moon System Integration

## Overview

The Cursor-Agent now includes full integration with the **Moon Phasing Keyring** system from `/mnt/Vault/Moon`. This provides cryptographic authentication and temporal binding for agent operations.

## What is the Moon System?

The Moon system is a cryptographic framework that binds operations to:

- **Moon Phases** - Celestial mechanics (astronomical calculations)
- **DAUS Calendar** - Covenant temporal system (13 months, 390 days/year)
- **Kings List** - Sumerian historical position (Pre-Flood foundation)
- **DAUS 5 Elements** - Sacred geometry (Fire, Water, Wind, Earth, Ether)

**Principle**: *"You cannot fake the moon, the calendar, or the kings."*

## Integration Architecture

```
Cursor-Agent/
├── moon/                      # Moon system library
│   ├── __init__.py            # Main exports
│   ├── keyring.py             # Key derivation (wraps declaration_master_keyring_system.py)
│   ├── temporal.py            # Temporal binding (wraps temporal_binding.py)
│   ├── verification.py        # Sovereign verification (wraps sovereign_verification_system.py)
│   ├── auth.py                # Authentication system
│   ├── config.py              # Configuration
│   ├── examples.py            # Usage examples
│   └── README.md              # Documentation
├── bin/
│   └── moon-cli               # CLI tool
└── config/
    └── moon.json              # Configuration file (optional)
```

The integration works as a **library module** that wraps the complete Moon system at `/mnt/Vault/Moon`.

## Features

### 1. Cryptographic Key Derivation

Derive deterministic keys from:
- Declaration PNG (source of truth)
- Construct (26-hour temporal structure)
- Moon Phase
- Chrony/NTP time
- DAUS Calendar

```python
from moon import MoonKeyring

keyring = MoonKeyring()
key = keyring.derive_key('agent_auth', use_all_systems=True)
```

### 2. Temporal Validation

Validate operations against current temporal state:

```python
from moon import TemporalBinding

validation = TemporalBinding.validate_temporal_operation('key_generation')
if validation['valid']:
    # Operation is optimal for current moon phase
    proceed_with_operation()
```

### 3. Sovereign Verification

Three-entity verification system:
- Declaration (Scroll) - Source of Truth
- Birth.cert (Sovereign Man) - Proof of I AM
- Time.png (Covenant Seal)

```python
from moon import SovereignVerification

verifier = SovereignVerification()
if verifier.verify_all():
    # All three entities verified
    proceed_with_verified_operation()
```

### 4. Agent Authentication

Generate temporal-bound authentication tokens:

```python
from moon.auth import MoonAuth

auth = MoonAuth()
token = auth.generate_operation_token('code_review', user='alice')

if token['valid']:
    # Token includes temporal coordinates and validation
    execute_with_token(token)
```

## Quick Start

### 1. Check Status

```bash
cd /mnt/Vault/Cursor-Agent
export PATH="$PATH:/mnt/Vault/Cursor-Agent/bin"

moon-cli status
```

### 2. View Temporal Coordinates

```bash
# Current moon phase
moon-cli moon

# DAUS calendar
moon-cli daus

# Kings position
moon-cli kings

# All coordinates (JSON)
moon-cli temporal
```

### 3. Generate Authentication Token

```bash
moon-cli auth code_review alice
```

### 4. Validate Operation Timing

```bash
moon-cli validate key_generation
```

### 5. Run Examples

```bash
python3 moon/examples.py
```

## Configuration

### Feature Flags

Edit `config/moon.json` or use Python:

```python
from moon.config import MoonConfig

# Enable strict temporal validation (blocks operations outside optimal phases)
MoonConfig.STRICT_TEMPORAL_VALIDATION = True

# Require sovereign verification before operations
MoonConfig.REQUIRE_VERIFICATION = True

# Save configuration
MoonConfig.save_config_file()
```

### Configuration File Format

`config/moon.json`:
```json
{
  "features": {
    "temporal_validation": true,
    "sovereign_verification": true,
    "key_derivation": true
  },
  "settings": {
    "strict_temporal_validation": false,
    "require_verification": false
  }
}
```

## Usage in Agent Code

### Basic Usage

```python
from moon.auth import MoonAuth

# Initialize
auth = MoonAuth()

# Check if available
if auth.is_enabled():
    # Generate token for operation
    token = auth.generate_operation_token('code_review')

    if token['valid']:
        # Proceed with operation
        # Token includes temporal binding
        print(f"Moon Phase: {token['data']['temporal']['moon_phase']['phase']}")
```

### With Temporal Validation

```python
from moon.auth import MoonAuth

# Enable strict validation
auth = MoonAuth(enable_strict_validation=True)

# Verify operation can proceed
verification = auth.verify_operation('key_generation')

if verification['allowed']:
    if verification['optimal']:
        print("Optimal timing for operation")
    else:
        print(f"Warning: {verification['reason']}")

    # Proceed
    generate_key()
else:
    print(f"Operation blocked: {verification['reason']}")
```

### With Sovereign Verification

```python
from moon.auth import MoonAuth
from moon.config import MoonConfig

# Require verification
MoonConfig.REQUIRE_VERIFICATION = True

auth = MoonAuth()

# This performs full verification
result = auth.authenticate_with_verification('code_review')

if result.get('authenticated') and result.get('verified'):
    # Fully verified operation
    proceed_with_verified_operation()
```

## Operation Types and Moon Phases

Different operations are optimal during specific moon phases:

| Operation | Optimal Moon Phases | Purpose |
|-----------|-------------------|---------|
| `key_generation` | New Moon, Waxing Crescent | Generate new keys |
| `seal` | Full Moon | Seal/manifest operations |
| `flow` | First Quarter, Last Quarter | Flow operations |
| `accumulate` | Waxing Gibbous | Accumulate data |
| `return` | Waning Gibbous, Waning Crescent | Return/cleanup |

When `STRICT_TEMPORAL_VALIDATION = True`, operations outside their optimal phases are blocked.

## CLI Reference

```bash
# System status
moon-cli status

# Temporal coordinates
moon-cli temporal        # All (JSON)
moon-cli moon            # Moon phase
moon-cli daus            # DAUS calendar
moon-cli kings           # Kings position

# Key operations
moon-cli derive <purpose>                 # Derive key
moon-cli validate <operation>             # Validate timing
moon-cli auth <operation> [user]          # Generate token
moon-cli verify                           # Sovereign verification
moon-cli update                           # Update JSON files
```

## Integration with Existing Agent

### Modify Agent Code

Add to your agent initialization:

```python
from moon.auth import MoonAuth
from moon.config import MoonConfig

class CursorAgent:
    def __init__(self):
        # ... existing initialization ...

        # Initialize Moon auth (optional)
        self.moon_auth = None
        if MoonConfig.is_moon_available():
            try:
                self.moon_auth = MoonAuth()
                print("✅ Moon authentication enabled")
            except Exception as e:
                print(f"⚠️  Moon authentication unavailable: {e}")

    def execute_operation(self, operation, user=None):
        # Optional: Validate with Moon
        if self.moon_auth and self.moon_auth.is_enabled():
            verification = self.moon_auth.verify_operation(operation, show_warnings=True)

            if not verification['allowed']:
                raise PermissionError(f"Operation blocked: {verification['reason']}")

        # ... existing operation logic ...
```

## Dependencies

### Required
- Python 3.6+
- `/mnt/Vault/Moon` directory with complete Moon system
- Standard library only

### Optional
- `chrony` or `ntp` for precise time synchronization
- `timedatectl` for timezone info
- Sovereign images at `/mnt/Vault/Images/`:
  - `The_Eternal_Covenant_Declaration.png`
  - `Birth.png`
  - `Time.png`

## Troubleshooting

### Moon System Not Available

```python
from moon.config import MoonConfig

status = MoonConfig.get_status()
print(f"Available: {status['available']}")
print(f"Components: {status['components']}")
```

### Import Errors

```bash
# Ensure /mnt/Vault/Moon exists
ls -la /mnt/Vault/Moon

# Check Python path
python3 -c "import sys; print('\n'.join(sys.path))"
```

### Temporal Data Not Current

```bash
# Update temporal JSON files
moon-cli update
```

## Examples

See `moon/examples.py` for comprehensive examples:

```bash
python3 moon/examples.py
```

This runs:
1. System status check
2. Temporal coordinates display
3. Key derivation example
4. Temporal validation example
5. Authentication example
6. Sovereign verification example

## Architecture Notes

The integration follows these principles:

1. **Separation**: Moon system remains at `/mnt/Vault/Moon`, Cursor-Agent wraps it
2. **Optional**: Moon features are optional, agents work without them
3. **No modifications**: Original Moon system is not modified
4. **Library pattern**: Clean import interface via `moon` module
5. **Graceful degradation**: System works even if components are unavailable

## Status

✅ Moon Keyring integrated
✅ Temporal Binding integrated
✅ Sovereign Verification integrated
✅ Authentication system implemented
✅ Configuration system implemented
✅ CLI tool created
✅ Examples provided
✅ Documentation complete

## Source Systems

All functionality wraps the complete Moon system:

- `/mnt/Vault/Moon/declaration_master_keyring_system.py`
- `/mnt/Vault/Moon/temporal_binding.py`
- `/mnt/Vault/Moon/sovereign_verification_system.py`
- `/mnt/Vault/Moon/DAUS/`
- `/mnt/Vault/Moon/Kings/`
- `/mnt/Vault/Moon/Images/`

---

∇ • Θεός°●⟐●Σ℧ΛΘ

**Integration Status**: COMPLETE ✓
**Documentation**: COMPREHENSIVE ✓
**Ready for Use**: YES ✓
