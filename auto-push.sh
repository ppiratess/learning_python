#!/bin/bash

# Check if a commit message is provided
if [ -z "$1" ]; then
  echo "Error: No commit message provided."
  echo "Usage: ./push-current-branch.sh \"Your commit message\""
  exit 1
fi

commit_message="$1"
branch=$(git rev-parse --abbrev-ref HEAD)

# Confirm the commit message
echo "You entered the commit message: \"$commit_message\""
read -p "Do you want to proceed? (Y/n): " confirm

# Convert input to lowercase for comparison
confirm=${confirm,,}

if [[ "$confirm" != "y" && "$confirm" != "" ]]; then
  echo "❌ Commit aborted."
  exit 1
fi

# Add all changes
git add .

# Commit the changes with the provided message
git commit -m "$commit_message"

# Push to the current branch
git push origin "$branch"

echo "✅ Successfully pushed changes to $branch!"
