import json
import csv

CSV_SOURCE_FILE = "JournalHomeGrid.csv"
SKIP_LINES = 1
EXPORT_KEYS = [
    "Journal Impact Factor"
]

def make_lookup():
    cf = open(CSV_SOURCE_FILE, "r")
    for i in range(SKIP_LINES):
        cf.readline()
    reader = csv.DictReader(cf)
    lookup = {}
    for row in reader:
        issn = row["ISSN"]
        lookup[issn] = row
    return lookup
    
def make_lookup_bytitle():
    cf = open(CSV_SOURCE_FILE, "r")
    for i in range(SKIP_LINES):
        cf.readline()
    reader = csv.DictReader(cf)
    lookup = {}
    for row in reader:
        title = row["Full Journal Title"].upper()
        lookup[title] = row
    return lookup

def update_JIF(values):
    lookup = make_lookup()
    for v in values:
        if "ISSN" in v:
            for issn in v["ISSN"]:
                if issn in lookup:
                    for k in EXPORT_KEYS:
                        v[k] = float(lookup[issn][k])
                    continue

def update_JIF_bytitle(values):
    lookup = make_lookup_bytitle()
    for v in values:
        if "container-title" in v:
            title = v["container-title"].upper()
            if title in lookup:
                for k in EXPORT_KEYS:
                    v[k] = float(lookup[title][k])
                
