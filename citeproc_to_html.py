#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from citeproc.py2compat import *

# We'll use json.loads for parsing the JSON data.
import json
import os
import re
import io
from dateutil import parser as dateparser
import datetime

# Import the citeproc-py classes we'll use below.
from citeproc import CitationStylesStyle, CitationStylesBibliography
from citeproc import Citation, CitationItem
from citeproc import formatter
from citeproc.source.json import CiteProcJSON

from config import GROUPS, DB_PATH, DB_FILENAME_FMT

try:
    from urllib.parse import unquote
except ImportError:
    from urllib import unquote

try:
    from html import unescape
except ImportError:
    import HTMLParser
    parser = HTMLParser.HTMLParser()
    unescape = parser.unescape


# The following JSON data describes 5 references picked from the CSL test suite.
MONTHDAY_FIRST_SLASH = re.compile(r'^(\d{1,2}/)+\d{4}$')
YEAR_FIRST_SLASH = re.compile(r'^\d{4}(/\d{1,2})+$')
ISO_STYLE_DATE = re.compile(r'^\d{4}(-\d{1,2}){0,1,2}$')
JUST_YEAR = re.compile(r'\d{4}')
NO_DATE = "1970-01-01 00:00:00"
DEFAULT_DATE = dateparser.parse("1970-01-01 00:00:00")


def get_year(item):
    issued = item.get("issued", {})
    if 'date-parts' in issued:
        return int(issued['date-parts'][0][0])
    elif 'raw' in issued:
        d = dateparser.parse(issued['raw'])
        return d.year
    else:
        return 0


def get_date_string(item):
    issued = item.get("issued", {})
    if 'date-parts' in issued:
        date_array = issued['date-parts'][0]
        ts = "-".join(map(str, date_array)) 
    elif 'raw' in issued:
        ts = issued['raw']
    else:
        ts = NO_DATE
    
    d = dateparser.parse(ts, default=DEFAULT_DATE)
    return d.date().isoformat()


def sort_year(items):
    year_lookup = {}
    for key, value in items:
        year = get_year(value)
        year_lookup.setdefault(year, [])
        year_lookup[year].append(key)
    return year_lookup


def generate_md(db, min_year=float('-inf'), max_year=float('inf'), group_by_year=True):

    directory = os.path.dirname(os.path.abspath(__file__))
    file_location = directory + os.path.sep + "static" + os.path.sep + "SasView_linktitle"
    bib_style = CitationStylesStyle(file_location, validate=False)

    # Create the citeproc-py bibliography, passing it the:
    # * CitationStylesStyle,
    # * BibliographySource (CiteProcJSON in this case), and
    # * a formatter (plain, html, or you can write a custom formatter)
    
    # add id to each item:
    items = db.items()
    for k, v in items:
        v['id'] = k
    
    bib_source = CiteProcJSON([v for k,v in items])
    year_lookup = sort_year(items)
    years = list(year_lookup.keys())
    years.sort()
    output_years = [year for year in years if year <= max_year and year >=min_year]
    year_cite_items = []
    year_link_items = []
    patent_items = []
    for year in output_years:
        year_link_items.append('[{0}](#{0})'.format(year))
        keys = year_lookup[year]
        keys.sort(key=lambda l: get_date_string(db[l]), reverse=True)
        bibliography = CitationStylesBibliography(bib_style, bib_source, formatter.plain)
        citations = [Citation([CitationItem(k)]) for k in keys]
        for c in citations:
            bibliography.register(c)
        
        bib = bibliography.bibliography()
        cite_bib = []
        for k, b in zip(keys, bib):
            if db[k].get('type', None) == 'patent':
                patent_items.append(unescape("".join(b)))
            else:
                cite_bib.append(b)
        bib_output = [unescape("".join(b)) for b in cite_bib]
        year_output = ['## {0}\n'.format(year)]
        year_output.append('<small>[top](#acknowledgements-and-contacts)</small>\n')
        year_output.append('---\n')
        for i, bib_i in enumerate(bib_output):
            bib_final = ("{0}. " + bib_i).format(i)
            year_output.append(bib_final)
        year_cite_items.append("\n".join(year_output))
    return {"citations": year_cite_items, "links": year_link_items, "patents": patent_items}


def callback(t):
    pass


TEMPLATE = """---
layout: page
title: {title}
---
## Acknowledgements and Contacts

If you found this software useful to your work please don't forget to acknowledge its use in your publications as suggested below and reference this website: _http://www.sasview.org/_. Please also consider letting us know by sending us the reference to your work. This will help us to ensure the long term support and development of the software.

> _This work benefited from the use of the SasView application, originally developed under NSF award DMR-0520547. SasView contains code developed with funding from the European Union's Horizon 2020 research and innovation programme under the SINE2020 project, grant agreement No 654000._

{preamble}

---

{year_links}

---

{content}

{postscript}
"""


PATENTS_SECTION = """
{patent_items}
"""


def make_page(group):
    csl_db_filename = DB_FILENAME_FMT.format(group=group)
    csl_db_path = os.path.join(DB_PATH, csl_db_filename)
    with io.open(csl_db_path, 'r', encoding='utf8') as f:
        db = json.loads(f.read())
    content_pieces = generate_md(db)
    citations = content_pieces["citations"]
    year_links = content_pieces["links"]
    patents = content_pieces["patents"]
    citations.reverse()
    year_links.reverse()
    content = "\n".join(citations)
    preamble = GROUPS[group].get('header', '')
    if len(patents) > 0:
        preamble += PATENTS_SECTION.format(patent_items="\n                        ".join(patents))
    postscript = GROUPS[group].get('footer', '')
    title = GROUPS[group].get("title", "{group}".format(group=group))
    output = TEMPLATE.format(title=title, content=content, year_links=", ".join(year_links), preamble=preamble, postscript=postscript)
    output_filename = "static/{group}_publications.md".format(group=group)
    with io.open(output_filename, 'w', encoding='utf8') as f:
        f.write(output)


if __name__ == '__main__':
    import sys
    groups = sys.argv[1:]
    if len(groups) < 1:
        print("usage: citeproc_to_html.py <group> <other_group>... or citeproc_to_html.py all")
    elif groups[0].lower() == "all":
        for group in GROUPS:
            make_page(group)
    else:
        for group in groups:
            make_page(group)
