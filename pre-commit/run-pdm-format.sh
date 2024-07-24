#!/bin/bash
echo "🔄 Starting pdm format..."

output=$(pdm run format)
status=$?

if [[ $status -eq 0 ]]; then
  if [[ $output == *"reformatted"* ]]; then
    echo "✅ - Code formatted successfully, now running tests..."
  else
    echo "⚠️  $(echo $output | grep -iP "no files (to|were) reformatted" | xargs)"
    echo "✅ - No files needed to be formatted, now running tests...."
  fi
else
  echo "❌ - Failed to format code!"
  exit 1
fi
