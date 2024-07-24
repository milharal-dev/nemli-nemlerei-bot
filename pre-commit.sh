#!/bin/sh

(
  echo "🔄 - Attempting to update dependencies..."
  true;
) &&
pdm install ||
(
  echo "❌ - Some dependencies are out of date!"
  false;
)

(
  echo "✅ - All dependencies are up to date!"
  echo -e "\n"
  echo "🔄 - Attempting to format code now..."
  true;
) &&
pdm format ||
(
  echo "❌ - Failed to format code!"
  false;
)

(
  echo "✅ - Files formatted successfully!"
  echo -e "\n"
  echo "🔄 - Attempting to lint now..."
  true; 
) &&
pdm lint nemli/ tests/ ||
(
  echo "❌ - Linting failed!"
  false;
)

(
  echo "✅ - Linting passed!"
  echo -e "\n"
  echo "🔄 - Attempting to run test suite now..."
  true;
) &&
pdm test ||
(
  echo "❌ - Test suite failed!"
  false;
)

echo "✅ - Test suite passed!" &&
echo -e "\n" &&
echo "🚀 - I am now committing this!"
