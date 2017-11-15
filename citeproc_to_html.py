#!/usr/bin/env python

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from citeproc.py2compat import *

# We'll use json.loads for parsing the JSON data.
import json
import math

# Import the citeproc-py classes we'll use below.
from citeproc import CitationStylesStyle, CitationStylesBibliography
from citeproc import Citation, CitationItem
from citeproc import formatter
from citeproc.source.json import CiteProcJSON

try:
    from urllib.parse import unquote
except ImportError:
    from urllib import unquote

from html import unescape

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
    
def generateHTML(items, min_year=-math.inf, max_year=math.inf, group_by_year=True):

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
    output_items = []
    for year in output_years:
        keys = yearLookup[year]
        bib_source = CiteProcJSON([v for k,v in items if k in keys])
        bibliography = CitationStylesBibliography(bib_style, bib_source, formatter.html)
        for k in keys:
            bibliography.register(Citation([CitationItem(k)]))
        bib = bibliography.bibliography()
        bib_output = [unescape("\n".join(b)) for b in bib]
        year_output = ['<h2 class="year-heading">%d</h2>' % (year,)]
        year_output.append('<ol class="publications">')
        year_output.extend(bib_output)
        year_output.append('</ol>')
        output_items.append("\n".join(year_output))
    return output_items
        
TEMPLATE = """\
<html>
<head>
    <meta charset="UTF-8">
    <title>{instrument} Publications</title>
    <style>
        body {{
            font-family: Arial, Helvetica, sans-serif;
        }}
        header {{
            text-align: center;
        }}
        ol.publications li {{
            margin-bottom: 0.25em;
        }}
        span.title:after {{
            content: '\A';
            white-space: pre;
        }}
    </style>
</head>
<body>
    <header><h1>{instrument} instrument publications</h1></header>
    <content>
    {content}
    </content>
</body>
</html>
"""

def makePage(instrument):
    items = json.loads(open("{instrument}.json".format(instrument=instrument), "r").read()).items()
    content_pieces = generateHTML(items)
    content_pieces.reverse()
    content = "\n".join(content_pieces)
    output = TEMPLATE.format(instrument=instrument, content=content)
    open("{instrument}_pubs.html".format(instrument=instrument), "w").write(output)
