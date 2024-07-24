#!/bin/bash
# Combined pre-commit script

set -e  # Exit immediately if a command exits with a non-zero status.

echo "🔄 - Attempting to update dependencies..."
if stdbuf -oL -eL pdm install | tee /dev/tty; then
  echo "✅ - All dependencies are up to date!" | stdbuf -oL -eL tee /dev/tty
else
  echo "❌ - Some dependencies are out of date!" | stdbuf -oL -eL tee /dev/tty
  exit 1
fi

echo "🔄 - Attempting to format code..."
if stdbuf -oL -eL pdm format | tee /dev/tty; then
  echo "✅ - Files formatted successfully!" | stdbuf -oL -eL tee /dev/tty
else
  echo "❌ - Failed to format code!" | stdbuf -oL -eL tee /dev/tty
  exit 1
fi

echo "🔄 - Attempting to run test suite..."
if stdbuf -oL -eL pdm tests | tee /dev/tty; then
  echo "✅ - Test suite passed!" | stdbuf -oL -eL tee /dev/tty
else
  echo "❌ - Test suite failed!" | stdbuf -oL -eL tee /dev/tty
  exit 1
fi

echo "🚀 - Pre-commit hook completed successfully!" | stdbuf -oL -eL tee /dev/tty