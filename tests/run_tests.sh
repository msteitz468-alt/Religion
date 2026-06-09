#!/bin/bash
# tests/run_tests.sh

echo "Starting E2E Tests..."
FAILED=0
PASSED=0

# Find all executable scripts in tests/tier* directories
TEST_SCRIPTS=$(find tests/tier* -type f \( -name "*.py" -o -name "*.sh" \) | sort)

for script in $TEST_SCRIPTS; do
    # Ensure it is executable
    chmod +x "$script"
    
    echo "Running $script ..."
    if [[ "$script" == *.py ]]; then
        python3 "$script"
    else
        bash "$script"
    fi
    
    EXIT_CODE=$?
    if [ $EXIT_CODE -eq 0 ]; then
        echo "[PASS] $script"
        PASSED=$((PASSED + 1))
    else
        echo "[FAIL] $script"
        FAILED=$((FAILED + 1))
    fi
done

echo "----------------------------------------"
echo "Tests Passed: $PASSED"
echo "Tests Failed: $FAILED"

if [ $FAILED -gt 0 ]; then
    exit 1
else
    exit 0
fi
