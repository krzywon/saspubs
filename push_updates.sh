#!/usr/bin/env bash

cp ../sasview_publications/static/SASVIEW_publications.md ../publications.md
SSHKEY=$0
git diff-index --quiet HEAD -- || ssh-agent bash -c "ssh-add " + $SSHKEY
git commit publications.md -m "publications auto-update `date -d now`"; git push