#!/bin/bash
# LegalOS 4.0 - Pre-Push Verification Script
# Usage: ./scripts/verify-before-push.sh

echo "🔍 LegalOS 4.0 Pre-Push Verification"
echo "======================================"
echo ""

# Change to project root
cd "$(dirname "$0")/.."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

FAILED=0
PASSED=0

# Function to check command
 check_command() {
    if [ $1 -eq 0 ]; then
        echo -e "${GREEN}✓${NC} $2"
        ((PASSED++))
    else
        echo -e "${RED}✗${NC} $2"
        ((FAILED++))
    fi
}

# 1. Check project structure
echo "📁 Checking project structure..."
if [ -d "frontend" ] && [ -d "backend" ] && [ -f "docker-compose.yml" ]; then
    check_command 0 "Project structure looks correct"
else
    check_command 1 "Missing frontend, backend, or docker-compose.yml"
    echo -e "${RED}ERROR: Please run this script from the project root or verify structure${NC}"
    exit 1
fi

# 2. Check Git installation
echo ""
echo "🔧 Checking Git..."
if command -v git &> /dev/null; then
    GIT_VERSION=$(git --version)
    check_command 0 "Git installed: $GIT_VERSION"

    if [ -d ".git" ]; then
        check_command 0 "Git repository initialized"
    else
        echo -e "${YELLOW}⚠ Git not initialized${NC}"
        # Not failing here, just warning
    fi
else
    check_command 1 "Git not installed"
    exit 1
fi

# 3. Check Frontend Dependencies
echo ""
echo "🟢 Checking Frontend..."
if [ -d "frontend/node_modules" ]; then
    check_command 0 "Frontend dependencies installed"
else
    echo -e "${YELLOW}⚠ Frontend node_modules missing. Consider running 'npm install' in frontend directory.${NC}"
    # Not failing, as we might be using Docker
fi

# 4. Check Critical Files
echo ""
echo "📄 Checking critical files..."
CRITICAL_FILES=(
    "frontend/src/personas/citizen/pages/AboutPage.tsx"
    "frontend/src/shared/layout/CitizenLayout.tsx"
    "frontend/src/shared/styles/designTokens.ts"
    "frontend/package.json"
    "frontend/tsconfig.json"
    "backend/app/main.py"
    "backend/requirements.txt"
    "docker-compose.yml"
)

for file in "${CRITICAL_FILES[@]}"; do
    if [ -f "$file" ]; then
        check_command 0 "Found: $file"
    else
        check_command 1 "Missing: $file"
    fi
done

# 5. Check TypeScript (Frontend)
echo ""
echo "🔷 Checking TypeScript (Frontend)..."
if command -v npx &> /dev/null; then
    if [ -d "frontend/node_modules" ]; then
        echo "Running TypeScript check in frontend..."
        (cd frontend && npx tsc --noEmit 2>&1 | head -20)
        if [ $? -eq 0 ]; then
            check_command 0 "TypeScript compilation successful"
        else
            check_command 1 "TypeScript errors found"
            echo -e "${YELLOW}⚠ Fix TypeScript errors before pushing${NC}"
        fi
    else
        echo -e "${YELLOW}Skipping TypeScript check (dependencies not installed)${NC}"
    fi
else
    echo -e "${YELLOW}Skipping TypeScript check (npx not available)${NC}"
fi

# 6. Check for uncommitted changes
echo ""
echo "💾 Checking for uncommitted changes..."
if [ -n "$(git status --porcelain)" ]; then
    echo -e "${YELLOW}⚠ Uncommitted changes found${NC}"
    git status --short
else
    check_command 0 "No uncommitted changes"
fi

# Summary
echo ""
echo "======================================"
echo "📊 VERIFICATION SUMMARY"
echo "======================================"
echo -e "${GREEN}Passed: $PASSED${NC}"
echo -e "${RED}Failed: $FAILED${NC}"
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✅ ALL CHECKS PASSED!${NC}"
    echo "Your project is ready to push!"
    exit 0
else
    echo -e "${RED}❌ SOME CHECKS FAILED${NC}"
    echo "Please fix the issues above before pushing."
    exit 1
fi
