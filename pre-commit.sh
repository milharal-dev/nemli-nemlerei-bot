#!/bin/sh

LOG_FILE="pre-commit.log"

{
  echo "🔄 - Attempting to update dependencies..."
  pdm install
  if [ $? -ne 0 ]; then
    echo "\n❌ - Some dependencies are out of date!"
    exit 1
  fi

  echo "✅ - All dependencies are up to date!"
  echo "\n🔄 - Attempting to format the code now...\n"
  pdm format
  if [ $? -ne 0 ]; then
    echo "\n❌ - Failed to format code!"
    exit 1
  fi

  echo "\n✅ - Files formatted successfully!"
  echo "\n🔄 - Attempting to lint now...\n"
  pdm lint nemli/ tests/
  if [ $? -ne 0 ]; then
    echo "\n❌ - Linting failed!"
    exit 1
  fi

  echo "\n✅ - Linting passed!"
  echo "\n🔄 - Attempting to run the test suite now..."
  pdm test
  if [ $? -ne 0 ]; then
    echo "\n❌ - Test suite failed!"
    exit 1
  fi

  echo "\n✅ - Test suite passed!"
  echo "🚀 - I am now committing this!"
} 2>&1 | tee "$LOG_FILE"