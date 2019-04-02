# SasView automated publications feed

Based off of ncnr_publications created by Brian Maranville.

## Backend

Based on [Zotero](https://www.zotero.org)

- [sasview_publications](https://www.zotero.org/groups/2309096/sasview/items) group (private membership, public read)
- SasView members manage publication list
- Collection ID(s) for SasView list(s) is added to config.py for automatic sync with sasview pages (frontend)

### Recurring backend job

- Every 5 minutes: look for new entries or deletions from Zotero, through the api (https://api.zotero.org)

## Frontend

Static page pushed to the sasview.github.io repository.

- MD file pushed to github - https://github.com/sasview/sasview.github.io/publications.md
- HTML generated by Beautiful Jekyll template - https://sasview.org/publications/