#!/usr/bin/env bash

# Usage:
# Pass a ssh private key file name as the first argument
# saspubs and sasview.github.io must be on the same base path

conda.bat activate zotero
python instrument_zotero_feed.py

cp static/SASVIEW_publications.md ../sasview.github.io/publications.md
cd ../sasview.github.io/
SSHKEY=$0
git diff-index --quiet HEAD -- || ssh-agent bash -c "ssh-add " + $SSHKEY
git commit publications.md -m "publications auto-update `date -d now`"; git push
conda.bat deactivate