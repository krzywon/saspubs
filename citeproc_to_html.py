#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from citeproc.py2compat import *

# We'll use json.loads for parsing the JSON data.
import json
import os

# Import the citeproc-py classes we'll use below.
from citeproc import CitationStylesStyle, CitationStylesBibliography
from citeproc import Citation, CitationItem
from citeproc import formatter
from citeproc.source.json import CiteProcJSON

from config import INSTRUMENTS, DB_PATH, DB_FILENAME_FMT

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

def getYear(item):
    issued = item.get("issued", {})
    if 'date-parts' in issued:
        return issued['date-parts'][0][0]
    elif 'raw' in issued:
        ts = issued['raw']
        ts = '-'.join(ts.split('/')[::-1])
        return int(ts.split('-')[0])
        
def sortYear(items):
    yearLookup = {}
    for key, value in items:
        year = getYear(value)
        yearLookup.setdefault(year, [])
        yearLookup[year].append(key)
    return yearLookup
    
def generateHTML(items, min_year=float('-inf'), max_year=float('inf'), group_by_year=True):

    bib_style = CitationStylesStyle('./NCNR_linktitle', validate=False)

    # Create the citeproc-py bibliography, passing it the:
    # * CitationStylesStyle,
    # * BibliographySource (CiteProcJSON in this case), and
    # * a formatter (plain, html, or you can write a custom formatter)

    #bibliography = CitationStylesBibliography(bib_style, bib_source, formatter.html)
    
    # add id to each item:
    for k,v in items:
        v['id'] = k
    
    #bib_source = CiteProcJSON([v for k,v in items])
    yearLookup = sortYear(items)
    years = list(yearLookup.keys())
    years.sort()
    output_years = [year for year in years if year <= max_year and year >=min_year]
    year_cite_items = []
    year_link_items = []
    for year in output_years:
        year_link_items.append('<a href="#year_%d">%d</a>' % (year,year))
        keys = yearLookup[year]
        bib_source = CiteProcJSON([v for k,v in items if k in keys])
        bibliography = CitationStylesBibliography(bib_style, bib_source, formatter.html)
        for k in keys:
            bibliography.register(Citation([CitationItem(k)]))
        bib = bibliography.bibliography()
        bib_output = [unescape("\n".join(b)) for b in bib]
        year_output = ['<div class="year-heading" id="year_%d"><h2>%d</h2><a href="#year_navigation">top</a></div>\n<hr>' % (year, year)]
        year_output.append('<ol class="publications">')
        year_output.extend(bib_output)
        year_output.append('</ol>')
        year_cite_items.append("\n".join(year_output))
    return {"citations": year_cite_items, "links": year_link_items}
        
TEMPLATE = """\
<html>
<head>
    <meta charset="UTF-8">
    <title>{instrument} Publications</title>
    <link rel="stylesheet" href="css/drupal_header.css" />
    <style>
        body {{
            font-family: Arial, Helvetica, sans-serif;
        }}
        header.title {{
            text-align: center;
        }}
        ol.publications li {{
            margin-bottom: 0.25em;
        }}
        span.title:after {{
            content: '\A';
            white-space: pre;
        }}
        content {{
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
            /*height: 50px;*/
        }}
        div.centered-column {{
            flex: 1;
            max-width: 900px;
            margin: auto;
        }}
        div.year-heading h2 {{
            display: inline-block;
            padding-right: 0.5em;
            margin-bottom: 0;
        }}
        
    </style>
</head>
<body>
    <header class="top">
        <div class="section-header">
            <div class="section-header__main">
                <h2 class="section-header__title"><a href="https://www.nist.gov/ncnr">NIST Center for Neutron Research</a></h2>
            </div>
        </div>    
    </header>
    <header class="title"><h1>{instrument} instrument publications</h1></header>
    <content>
        <div class="centered-column" id="year_navigation">
        {yearlinks}
        </div>
        <div class="centered-column">
        {content}
        </div>
    </content>
</body>
</html>
"""

def makePage(instrument):
    csl_db_filename = DB_FILENAME_FMT.format(instrument=instrument)
    csl_db_path = os.path.join(DB_PATH, csl_db_filename)
    items = json.loads(open(csl_db_path, "r").read()).items()
    content_pieces = generateHTML(items)
    citations = content_pieces["citations"]
    year_links = content_pieces["links"]
    citations.reverse()
    year_links.reverse()
    content = "\n".join(citations)
    output = TEMPLATE.format(instrument=instrument, content=content, yearlinks=", ".join(year_links))
    output_filename = "static/{instrument}_pubs.html".format(instrument=instrument)
    open(output_filename, "w").write(output)
