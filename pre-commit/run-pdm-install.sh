#!/bin/sh
echo "🔄 - Attempting to update dependencies..."

if pdm install; then
  echo "✅ - All dependencies are up to date!"
else
  echo "❌ - Some dependencies are out of date!"
  exit 1
fi