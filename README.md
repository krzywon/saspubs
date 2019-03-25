# SasView automated publications feed

Based off of ncnr_publications created by Brian Maranville.

## Backend

Based on [Zotero](https://www.zotero.org)

- [sasview_publications](https://www.zotero.org/groups/2309096/sasview/items) group (private membership, public read)
- SasView members manage publication list
- Collection ID(s) for SasView list(s) is added to config.py for automatic sync with sasview pages (frontend)

### Recurring backend jobs

- Every 5 minutes: look for new entries or deletions from Zotero, through the api (https://api.zotero.org)
- Every month: pull citation counts for every item with a DOI from https://api.crossref.org
- Every 6 months: manually download a new table of Journal Impact Factors from Clarivate: 
  https://jcr.incites.thomsonreuters.com/JCRJournalHomeAction.action?year=&edition=&journal=

## Frontend

Static pages pushed to the sasview.github.io repository.
Two views:

1.  Pretty view - https://sasview.org/publications_browser.html?group=SASVIEW
2.  Table view - https://sasview.org/publications/sasview_pubs.html
 
<i>citation count is from crossref.org</i>
<i>JIF is from Thomson Reuters</i>