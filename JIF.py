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
                    print(k, lookup[title][k])
                    v[k] = float(lookup[title][k])
                
def update_JIF_by_either(values):
    issn_lookup = make_lookup()
    title_lookup = make_lookup_bytitle()
    for v in values:
        found = False
        if "ISSN" in v:
            for issn in v["ISSN"]:
                if issn in issn_lookup and not found:
                    found = True
                    for k in EXPORT_KEYS:
                        v[k] = float(issn_lookup[issn][k])
                        
        if "container-title" in v and not found:
            title = v["container-title"].upper()
            if title in title_lookup:
                found = True
                for k in EXPORT_KEYS:
                    print(k, title_lookup[title][k])
                    v[k] = float(title_lookup[title][k])
    
