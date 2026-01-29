# Script Registry System - Quick Reference

## Quick Commands

### Register All Scripts
```bash
npm run registry register-all "Theos" royalty_on_verbatim 5.0
```
Registers all scripts in the project with:
- Author: "Theos"
- License: `royalty_on_verbatim` (royalty applies on verbatim usage)
- Royalty: 5.0%

### Detect Verbatim Usage
```bash
npm run registry detect suspicious_script.ts "https://github.com/user/repo"
```
Checks if a script contains verbatim code from registered scripts.
- First argument: File to check
- Second argument: Where it was detected (repo URL, contract address, etc.)

### Generate Report
```bash
npm run registry report
```
Shows:
- Total scripts registered
- Verbatim usages detected
- Total royalties generated
- List of registered scripts

## Current Status

✅ **1,718 scripts registered**
- Author: Theos
- License: `royalty_on_verbatim`
- Royalty: 5% on verbatim usage
- 0 verbatim usages detected

## How It Works

1. **Registration**: Scripts are hashed (SHA-256) and stored in registry
2. **Detection**: When checking a file, system compares hashes
3. **Verbatim Match**: If hash matches → verbatim usage detected
4. **Royalty**: 5% royalty applies when verbatim usage detected

## Protection

- ✅ Hash-based detection (exact matches)
- ✅ Normalized content comparison (handles formatting differences)
- ✅ Similarity detection (>95% = verbatim)
- ✅ Automatic royalty tracking
- ✅ Detection logging

## Registry Files

- `script_registry/registry.json` - Main registry
- `script_registry/verbatim_detections.json` - Detected verbatim usages

## Example Workflow

```bash
# 1. Register all your scripts
npm run registry register-all "Theos" royalty_on_verbatim 5.0

# 2. Check a suspicious file
npm run registry detect copied_script.ts "https://github.com/suspicious/repo"

# 3. View report
npm run registry report
```

## License Types

- `royalty_on_verbatim` - Royalty applies if used verbatim (default)
- `attribution_required` - Attribution required, no royalty
- `open_source` - Open source, no restrictions
