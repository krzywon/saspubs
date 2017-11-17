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

DB_PATH = "./csl_data"
DB_FILENAME_FMT = "{db_path}/{instrument}.json"
VERSION_FILENAME_FMT = "{db_path}/.{instrument}_version.json"
REMOTE_PATH = "/var/www/html/publications/data/"
