#!/bin/bash

# Define directories (without root project name)
DIRS=(
    "src"
    "tests"
    "configs"
    "docs"
    "data/raw"
    "data/processed"
    "data/models"
    "data/visuals"
    "notebooks"
    "scripts"
    "logs"
    "static"
    "templates"
    "bin"
    "lib"
    "deploy"
)

# Create directories
for dir in "${DIRS[@]}"; do
    mkdir -p "$dir"
done

# Create common files
touch "README.md"
touch ".gitignore"
touch "requirements.txt"

echo "✅ Project structure created in $(pwd)/"
