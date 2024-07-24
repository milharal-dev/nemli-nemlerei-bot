#!/bin/bash
# Combined pre-commit script

set -e  # Exit immediately if a command exits with a non-zero status.

echo "🔄 - Attempting to update dependencies..."
if pdm install 2>&1 | tee /dev/tty; then
  echo "✅ - All dependencies are up to date!"
else
  echo "❌ - Some dependencies are out of date!"
  exit 1
fi

echo "🔄 - Attempting to format code..."
if pdm format 2>&1 | tee /dev/tty; then
  echo "✅ - Files formatted successfully!"
else
  echo "❌ - Failed to format code!"
  exit 1
fi

echo "🔄 - Attempting to run test suite..."
if pdm tests 2>&1 | tee /dev/tty; then
  echo "✅ - Test suite passed!"
else
  echo "❌ - Test suite failed!"
  exit 1
fi

echo "🚀 - Pre-commit hook completed successfully!"
