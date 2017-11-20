INSTRUMENTS = {
    
    "MAGIK": {
        "group": "1942669",
        "collection": "29DQ33DH"
    },
    "PBR": {
        "group": "1942136",
        #"collection": "5FB99F7A"
    },
    "NG7SANS": {
        "group": "1942669",
        "collection": "RV37EK44"
    },
    "BT7": {
        "group": "1942669",
        "collection": "VWZ2CZZJ"
    },
    "NGB30SANS": {
        "group": "1942669",
        "collection": "2TQMBS9X"
    },
    "NGB10SANS": {
        "group": "1942669",
        "collection": "QTGN36EH"
    },
    "NSE": {
        "group": "1942669",
        "collection": "XT6XYDEH"
    },
    "USANS": {
        "group": "1942669",
        "collection": "64AMFBBD"
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

DB_PATH = "./data"
DB_FILENAME_FMT = "{instrument}.json"
VERSION_FILENAME_FMT = ".{instrument}_version.json"
REMOTE_PATH = "/var/www/html/publications/"
