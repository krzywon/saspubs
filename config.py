SANS_HEADER = r"""\
"""

SANS_FOOTER = r"""\
"""

INSTRUMENTS = {
    
    "MAGIK": {
        "group": "1942669",
        "collection": "29DQ33DH"
    },
    "PBR": {
        "group": "1942136",
        #"collection": "5FB99F7A"
    },
    "NG7REFL": {
        "group": "1942669",
        "collection": "TKAGDRTW"
    },
    "NG7SANS": {
        "group": "1942669",
        "collection": "RV37EK44", 
        "header": SANS_HEADER,
        "footer": SANS_FOOTER
    },
    "BT7": {
        "group": "1942669",
        "collection": "VWZ2CZZJ",
        "title": "Thermal Triple Axis"
    },
    "SPINS": {
        "group": "1942669",
        "collection": "ICQ7KQ23"
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
    },
    "DCS": {
        "group": "1942669",
        "collection": "5NKTCIUL"
    },
    "MACS": {
        "group": "1942669",
        "collection": "SCPXUF5T"
    },
    "HFBS": {
        "group": "1942669",
        "collection": "9GDX95BA"
    },
    "TEST": {
        "group": "1925268",
        "collection": "YQIVUSAD"
    },
    "TEST2": {
        "group": "1925268",
        "collection": "FAHFDH4G"
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
