# NCNR automated publications feed

## Backend

Based on [Zotero](https://www.zotero.org)

- [ncnr_publications](https://www.zotero.org/groups/1942669/ncnr_instruments/items) group (private membership, public read)
- collections for each instrument (BT7, MAGIK, DCS, etc.)
- Instrument scientist manages publication list
- Collection ID for instruments is added to config.py for automatic sync with NCNR pages (frontend)


### Recurring backend jobs

- Every 5 minutes: look for new entries or deletions from Zotero, through the api (https://api.zotero.org)
- Every month: pull citation counts for every item with a DOI from https://api.crossref.org
- Every 6 months: manually download a new table of Journal Impact Factors from Clarivate: 
  https://jcr.incites.thomsonreuters.com/JCRJournalHomeAction.action?year=&edition=&journal=

## Frontend

Static pages pushed to the NCNR server https://ncnr.nist.gov
Two views:

1.  Pretty view
  * https://ncnr.nist.gov/publications/publications_browser.html?instrument=NG7SANS
  * https://ncnr.nist.gov/publications/publications_browser.html?instrument=BT7
  * ...
2.  Table view:
  * https://ncnr.nist.gov/publications/NG7SANS_pubs.html
  * https://ncnr.nist.gov/publications/MAGIK_pubs.html
 
<i>citation count is from crossref.org</i>
<i>JIF is from Thomson Reuters</i>