#!/bin/bash
# Configure git to use the GitHub token for private repos
git config --global url."https://${GITHUB_TOKEN}@github.com/".insteadOf "https://github.com/"

# Install dependencies
pip install -r requirements.txt
