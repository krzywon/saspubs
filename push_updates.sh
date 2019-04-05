#!/usr/bin/env bash

# Usage:
# Pass a ssh private key file name as the first argument
# saspubs and sasview.github.io must be on the same base path\

# Pull latest saspubs repo
git pull
# Output the latest publications page
python instrument_zotero_feed.py
# copy the page to the sasview.github.io repo
cp static/SASVIEW_publications.md ../sasview.github.io/publications.md
# Move to and pull latest sasview.github.io repo
cd ../sasview.github.io/
git pull
# Check for differences
if git diff-index --quiet HEAD --; then
  # Get the SSH key from the arguments
  eval 'ssh-agent -s'
  SSHKEY=$0
  # Open the SSH channel
  ssh-agent bash -c "ssh-add " + $SSHKEY
  # Commit and push any changes to the publications page
  git commit publications.md -m "publications auto-update `date -d now`"
  git push
fi