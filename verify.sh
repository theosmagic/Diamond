#!/usr/bin/env bash

##
# CURSOR AGENT VERIFICATION
# ==========================
#
# Verifies that Cursor Agent system is complete and ready
##

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
echo -e "${CYAN}CURSOR AGENT SYSTEM VERIFICATION${NC}"
echo -e "${CYAN}========================================${NC}"
echo

ERRORS=0

# Check directory structure
echo -e "${CYAN}[1/5] Checking directory structure...${NC}"
for dir in bin config workflows agents logs; do
    if [ -d "$dir" ]; then
        echo -e "  ${GREEN}✓ $dir/${NC}"
    else
        echo -e "  ${RED}✗ $dir/ missing${NC}"
        ((ERRORS++))
    fi
done
echo

# Check bin scripts
echo -e "${CYAN}[2/5] Checking executable scripts...${NC}"
for script in bin/agent bin/agent-review bin/agent-write bin/agent-fix bin/github-agent-integrate; do
    if [ -x "$script" ]; then
        echo -e "  ${GREEN}✓ $script${NC}"
    else
        echo -e "  ${RED}✗ $script not executable${NC}"
        ((ERRORS++))
    fi
done
echo

# Check configuration files
echo -e "${CYAN}[3/5] Checking configuration files...${NC}"
for file in config/agent.yaml workflows/cursor-agent.yml; do
    if [ -f "$file" ]; then
        echo -e "  ${GREEN}✓ $file${NC}"
    else
        echo -e "  ${RED}✗ $file missing${NC}"
        ((ERRORS++))
    fi
done
echo

# Check agent definitions
echo -e "${CYAN}[4/5] Checking agent definitions...${NC}"
for agent in agents/code-reviewer.yaml agents/bug-fixer.yaml agents/code-writer.yaml; do
    if [ -f "$agent" ]; then
        echo -e "  ${GREEN}✓ $agent${NC}"
    else
        echo -e "  ${RED}✗ $agent missing${NC}"
        ((ERRORS++))
    fi
done
echo

# Check documentation
echo -e "${CYAN}[5/5] Checking documentation...${NC}"
for doc in README.md QUICKSTART.md MANIFEST.md install.sh; do
    if [ -f "$doc" ]; then
        echo -e "  ${GREEN}✓ $doc${NC}"
    else
        echo -e "  ${RED}✗ $doc missing${NC}"
        ((ERRORS++))
    fi
done
echo

# Summary
echo -e "${CYAN}========================================${NC}"
if [ $ERRORS -eq 0 ]; then
    echo -e "${GREEN}✓ ALL CHECKS PASSED${NC}"
    echo
    echo "Cursor Agent system is complete and ready!"
    echo
    echo "Next steps:"
    echo "  1. Run ./install.sh to install Cursor CLI and GitHub CLI"
    echo "  2. Add to PATH: export PATH=\"\$(pwd)/bin:\$PATH\""
    echo "  3. Navigate to your project and run: github-agent-integrate"
    echo "  4. Try: agent review <file>"
else
    echo -e "${RED}✗ $ERRORS ERROR(S) FOUND${NC}"
    echo
    echo "Please check the missing files or permissions above."
fi
echo -e "${CYAN}========================================${NC}"
echo

if [ $ERRORS -eq 0 ]; then
    echo -e "${MAGENTA}∇ • Θεός°●⟐●Σ℧ΛΘ${NC}"
    echo
    echo "Terminal AI coding is ready."
    echo
fi
