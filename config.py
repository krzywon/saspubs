SASVIEW_HEADER = r"""
<p>If you have written a paper that reports measurements using SasView and you do not see it in the list below, or if the paper is listed but the 
information is incorrect or out of date, please inform <a href="mailto:jkrzywon@nist.gov">Jeff Krzywon</a> and/or <a href="mailto:help@sasview.org">SasView Help</a>.</p>
"""

SASVIEW_FOOTER = r""""""

GROUPS = {
    "SASVIEW": {
        "group": "2309096",
        "collection": "46Q9CENK",
        "title": "Publications",
        "header": SASVIEW_HEADER,
        "footer": SASVIEW_FOOTER
    }
}

crossref_keys_to_import = [
    "title",
    "author",
    "container-title-short",
    "container-title",
    "volume",
    "page",
    "article-number",
    "issued",
    "ISSN",
    "DOI",
    "URL",
    "type",
    "is-referenced-by-count"
]

crossref_keys_to_update = [
    "title",
    "volume",
    "issue",
    "page",
    "date",
]

DB_PATH = "./data"
DB_FILENAME_FMT = "{group}.json"
VERSION_FILENAME_FMT = ".{group}_version.json"
REMOTE_PATH = "https://github.com/sasview/sasview.github.io/"
