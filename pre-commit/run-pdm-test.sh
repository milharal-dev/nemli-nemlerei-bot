#!/bin/bash
echo "🔄 Starting pdm test..."

# Run pdm test and capture output
output=$(pdm run test)
status=$?

if [[ $status -eq 0 ]]; then
  if [[ $output == *"collected 0 items"* ]]; then
    echo "⚠️ - No tests were run, please add tests to your project!"
    echo "✅ - Test suite passed!"
    echo "🚀 - I am committing this now!"
  else
    echo "✅ pdm test completed successfully!"
  fi
else
  echo "❌ pdm test failed!"
  exit 1
fi
