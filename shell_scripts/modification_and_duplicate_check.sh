#!/usr/bin/env bash

# Usage:
# Pass a ssh private key file name as the first argument
# saspubs and sasview.github.io must be on the same base path\

# Get the SSH key from the arguments
SSHKEY=$1
APIKEY=$2
# Change path to directory of the script in case it isn't already
cd "$(dirname "$0")";
cd "../";
# Pull latest saspubs repo
ssh-agent -t 60 bash -c "ssh-add $SSHKEY; git pull";
# Output the latest publications page
python update_current_list.py SASVIEW $APIKEY;
# copy the page to the sasview.github.io repo
cp static/SASVIEW_publications.md ../sasview.github.io/publications.md;
# Move to and pull latest sasview.github.io repo
cd ../sasview.github.io/;
ssh-agent -t 60 bash -c "ssh-add $SSHKEY; git pull";
# Check for differences
if ! git diff-index --quiet HEAD --; then
  # Commit and push any changes to the publications page
  git commit publications.md -m "publications auto-modification-and-duplicate-removal-update `date -d now`";
  ssh-agent -t 60 bash -c "ssh-add $SSHKEY;  git push";
fi
