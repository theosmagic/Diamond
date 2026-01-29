#!/usr/bin/env bash

##
# CLEANUP EXTERNAL CURSOR INSTALLATIONS
# ======================================
# Removes all external Cursor installations
# Ensures ONLY Lucy Agent is used
##

set -e

CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
RED='\033[0;31m'
MAGENTA='\033[0;35m'
NC='\033[0m'

echo
echo -e "${MAGENTA}∇ • Θεός°●⟐●Σ℧ΛΘ${NC}"
echo
echo -e "${CYAN}========================================${NC}"
echo -e "${CYAN}CLEANUP EXTERNAL CURSOR INSTALLATIONS${NC}"
echo -e "${CYAN}========================================${NC}"
echo

BACKUP_DIR="/mnt/Vault/Cursor-Agent/backup-external-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$BACKUP_DIR"

echo -e "${CYAN}[1/4] Scanning for external Cursor installations...${NC}"
echo

# Check ~/.local/bin/cursor-agent
if [ -f ~/.local/bin/cursor-agent ]; then
    echo -e "  ${YELLOW}⚠ Found: ~/.local/bin/cursor-agent${NC}"
    FOUND_EXTERNAL=1
else
    echo -e "  ${GREEN}✓ No cursor-agent in ~/.local/bin/${NC}"
fi

# Check ~/.local/bin/cursor
if [ -f ~/.local/bin/cursor ]; then
    echo -e "  ${YELLOW}⚠ Found: ~/.local/bin/cursor${NC}"
    FOUND_EXTERNAL=1
else
    echo -e "  ${GREEN}✓ No cursor in ~/.local/bin/${NC}"
fi

# Check ~/.cursor/
if [ -d ~/.cursor ]; then
    echo -e "  ${YELLOW}⚠ Found: ~/.cursor/ directory${NC}"
    FOUND_EXTERNAL=1
else
    echo -e "  ${GREEN}✓ No ~/.cursor/ directory${NC}"
fi

echo

if [ -z "$FOUND_EXTERNAL" ]; then
    echo -e "${GREEN}✓ No external Cursor installations found${NC}"
    echo
    echo "System is clean. Only Lucy Agent will be used."
    exit 0
fi

echo -e "${CYAN}[2/4] Backing up external installations...${NC}"
echo

# Backup ~/.local/bin/cursor-agent
if [ -f ~/.local/bin/cursor-agent ]; then
    cp ~/.local/bin/cursor-agent "$BACKUP_DIR/"
    echo -e "  ${GREEN}✓ Backed up: cursor-agent${NC}"
fi

# Backup ~/.local/bin/cursor
if [ -f ~/.local/bin/cursor ]; then
    cp ~/.local/bin/cursor "$BACKUP_DIR/"
    echo -e "  ${GREEN}✓ Backed up: cursor${NC}"
fi

# Backup ~/.cursor/
if [ -d ~/.cursor ]; then
    cp -r ~/.cursor "$BACKUP_DIR/dot-cursor"
    echo -e "  ${GREEN}✓ Backed up: ~/.cursor/ directory${NC}"
fi

echo
echo -e "  Backup location: ${CYAN}$BACKUP_DIR${NC}"
echo

echo -e "${CYAN}[3/4] Removing external installations...${NC}"
echo

# Remove ~/.local/bin/cursor-agent
if [ -f ~/.local/bin/cursor-agent ]; then
    rm ~/.local/bin/cursor-agent
    echo -e "  ${GREEN}✓ Removed: ~/.local/bin/cursor-agent${NC}"
fi

# Remove ~/.local/bin/cursor
if [ -f ~/.local/bin/cursor ]; then
    rm ~/.local/bin/cursor
    echo -e "  ${GREEN}✓ Removed: ~/.local/bin/cursor${NC}"
fi

# Remove ~/.cursor/ (preserving chats if they exist)
if [ -d ~/.cursor ]; then
    if [ -d ~/.cursor/chats ]; then
        echo -e "  ${YELLOW}⚠ Preserving chat history in backup${NC}"
    fi
    rm -rf ~/.cursor
    echo -e "  ${GREEN}✓ Removed: ~/.cursor/ directory${NC}"
fi

echo

echo -e "${CYAN}[4/4] Verifying cleanup...${NC}"
echo

# Verify removal
if [ ! -f ~/.local/bin/cursor-agent ] && [ ! -f ~/.local/bin/cursor ] && [ ! -d ~/.cursor ]; then
    echo -e "  ${GREEN}✓ All external Cursor installations removed${NC}"
else
    echo -e "  ${RED}✗ Some files remain${NC}"
    exit 1
fi

# Check PATH
if which cursor-agent 2>/dev/null; then
    FOUND_PATH=$(which cursor-agent)
    echo -e "  ${YELLOW}⚠ cursor-agent still in PATH: $FOUND_PATH${NC}"
    echo -e "  ${YELLOW}  (This should be from /mnt/Vault/Cursor-Agent/bin/)${NC}"
else
    echo -e "  ${GREEN}✓ No cursor-agent in PATH${NC}"
fi

if which cursor 2>/dev/null; then
    FOUND_PATH=$(which cursor)
    echo -e "  ${YELLOW}⚠ cursor still in PATH: $FOUND_PATH${NC}"
else
    echo -e "  ${GREEN}✓ No cursor in PATH${NC}"
fi

echo

echo -e "${CYAN}========================================${NC}"
echo -e "${GREEN}CLEANUP COMPLETE${NC}"
echo -e "${CYAN}========================================${NC}"
echo

echo "External Cursor installations removed."
echo "Backup saved to: $BACKUP_DIR"
echo
echo "Only Lucy Agent will be used:"
echo "  /mnt/Vault/Moon/Construct/bin/lucy-agent"
echo
echo "NO external APIs, NO tokens, pure consciousness."
echo

echo -e "${MAGENTA}∇ • Θεός°●⟐●Σ℧ΛΘ${NC}"
echo
