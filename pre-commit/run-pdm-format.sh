#!/bin/bash
echo "🔄 - Attempting to format code..."

if pdm format; then
  echo "✅ - Files formatted successfully!"
else
  echo "❌ - Failed to format code!"
  exit 1
fi
