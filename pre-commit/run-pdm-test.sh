#!/bin/bash
echo "🔄 - Attempting to run test suite..."

if pdm tests; then
  echo "✅ - Test suite passed!"
else
  echo "❌ - Test suite failed!"
  exit 1
fi
