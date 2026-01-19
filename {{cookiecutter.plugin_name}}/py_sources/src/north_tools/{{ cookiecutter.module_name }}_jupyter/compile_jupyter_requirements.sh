#!/bin/bash

# Script to compile requirements-jupyter.txt from test_jupyter directory
# This script uses uv pip compile to generate the requirements file

set -e

# Get the directory where this script is located
NORTH_TOOL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname $(dirname $(dirname $(dirname "$NORTH_TOOL_DIR"))))"
echo "Project root detected at: $PROJECT_ROOT"

REQUIREMENTS_IN="$NORTH_TOOL_DIR/requirements.in"
REQUIREMENTS_OUT="$NORTH_TOOL_DIR/requirements-jupyter.txt"

# Check if requirements.in exists
if [ ! -f "$REQUIREMENTS_IN" ]; then
    echo "Error: $REQUIREMENTS_IN not found"
    exit 1
fi

# Navigate to project root
cd "$PROJECT_ROOT"

# Compile requirements
echo "Compiling requirements-jupyter.txt from $REQUIREMENTS_IN, pyproject.toml, and extra 'nomad'"
# M
uv pip compile pyproject.toml "$REQUIREMENTS_IN" -o "$REQUIREMENTS_OUT"

if [ $? -eq 0 ]; then
    echo "✓ Successfully created $REQUIREMENTS_OUT"
else
    echo "✗ Failed to compile requirements"
    exit 1
fi
