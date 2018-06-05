#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from citeproc.py2compat import *

# We'll use json.loads for parsing the JSON data.
import json
import os
import re

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

MONTHDAY_FIRST_SLASH = re.compile(r'^(\d{1,2}/)+\d{4}$')
YEAR_FIRST_SLASH = re.compile(r'^\d{4}(/\d{1,2})+$')
ISO_STYLE_DATE = re.compile(r'^\d{4}(-\d{1,2}){0,1,2}$')
JUST_YEAR = re.compile(r'\d{4}')

def getYear(item):
    issued = item.get("issued", {})
    if 'date-parts' in issued:
        return issued['date-parts'][0][0]
    elif 'raw' in issued:
        ts = issued['raw']
        ts = '-'.join(ts.split('/')[::-1])
        return int(ts.split('-')[0])
        
def getDateString(item):
    issued = item.get("issued", {})
    if 'date-parts' in issued:
        ta = issued['date-parts'][0]
        #return "-".join(map(lambda d: format(d, '02d'), issued['date-parts'][0]))
    elif 'raw' in issued:
        ts = issued['raw']
        # convert slash dates to ISO format YYYY-MM-DD
        if MONTHDAY_FIRST_SLASH.match(ts):
            ta = ts.split('/')[::-1]
        elif YEAR_FIRST_SLASH.match(ts):
            ta = ts.split('/')
        elif ISO_STYLE_DATE.match(ts):
            ta = ts.split('-')
        else:
            #something else... just get the year.
            ta = JUST_YEAR.findall(ts)
        ta = list(map(int, ta))
    
    date_array = [1970,1,1]
    for i, ti in enumerate(ta):
        if i<3:
            date_array[i] = ti
    return "-".join(map(lambda d: format(d, '02d'), date_array))
        
def sortYear(items):
    yearLookup = {}
    for key, value in items:
        year = getYear(value)
        yearLookup.setdefault(year, [])
        yearLookup[year].append(key)
    return yearLookup
    
def generateHTML(db, min_year=float('-inf'), max_year=float('inf'), group_by_year=True):

    bib_style = CitationStylesStyle('./NCNR_linktitle', validate=False)
    #bib_style = CitationStylesStyle('harvard1', validate=False)

    # Create the citeproc-py bibliography, passing it the:
    # * CitationStylesStyle,
    # * BibliographySource (CiteProcJSON in this case), and
    # * a formatter (plain, html, or you can write a custom formatter)

    #bibliography = CitationStylesBibliography(bib_style, bib_source, formatter.html)
    
    # add id to each item:
    items = db.items()
    for k,v in items:
        v['id'] = k
    
    bib_source = CiteProcJSON([v for k,v in items])
    yearLookup = sortYear(items)
    #print(yearLookup)
    years = list(yearLookup.keys())
    years.sort()
    output_years = [year for year in years if year <= max_year and year >=min_year]
    year_cite_items = []
    year_link_items = []
    patent_items = []
    for year in output_years:
        year_link_items.append('<a href="#year_%d">%d</a>' % (year,year))
        keys = yearLookup[year]
        keys.sort(key=lambda k: getDateString(db[k]), reverse=True)
        #bib_source = CiteProcJSON([v for k,v in items if k in keys])
        bibliography = CitationStylesBibliography(bib_style, bib_source, formatter.html)
        citations = [Citation([CitationItem(k)]) for k in keys]
        for c in citations:
            bibliography.register(c)
        
        bib = bibliography.bibliography()
        cite_bib = []
        for k,b in zip(keys, bib):
            if db[k].get('type', None) == 'patent':
                patent_items.append(unescape("".join(b)))
            else:
                cite_bib.append(b)
        bib_output = [unescape("".join(b)) for b in cite_bib]
        year_output = ['<div class="year-heading" id="year_%d"><h2>%d</h2><a href="#year_navigation">top</a></div>\n<hr>' % (year, year)]
        year_output.append('<ol class="publications">')
        year_output.extend(bib_output)
        year_output.append('</ol>')
        year_cite_items.append("\n".join(year_output))
    return {"citations": year_cite_items, "links": year_link_items, "patents": patent_items}

def callback(t):
    pass

TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title} Publications</title>
    <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,700" rel="stylesheet" />
    <link rel="shortcut icon" href="https://www.nist.gov/sites/all/themes/nist_style/favicon.ico" type="image/vnd.microsoft.icon" />
    <link rel="stylesheet" href="css/drupal_header.css" />
    <style>
        body {{
            font-family: Arial, Helvetica, sans-serif;
        }}
        header.title {{
            font-family: 'Source Sans Pro', sans-serif;
            text-align: center;
        }}
        ol.publications li {{
            margin-bottom: 0.25em;
        }}
        span.title:after {{
            content: '\A';
            white-space: pre;
        }}
        div.content {{
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
            /*height: 50px;*/
        }}
        div.centered-column {{
            flex: 0 0 1;
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
                <h1 class="section-header__title"><a href="https://www.nist.gov/ncnr">NIST Center for Neutron Research</a></h1>
            </div>
        </div>    
    </header>
    <header class="title"><h1>{title} Publications</h1></header>
    <div class="content">
        <div class="centered-column" id="preamble">
        {preamble}
        </div>
        <div class="centered-column" id="year_navigation">
        {yearlinks}
        </div>
        <div class="centered-column">
        {content}
        </div>
        <div class="centered-column" id="postscript">
        {postscript}
        </div>
    </div>
</body>
</html>
"""

PATENTS_SECTION="""
            <div class="patents">
                <h2>Patents</h2>
                    <ol>
                        {patent_items}
                    </ol>
            </div>
"""

def makePage(instrument):
    csl_db_filename = DB_FILENAME_FMT.format(instrument=instrument)
    csl_db_path = os.path.join(DB_PATH, csl_db_filename)
    db = json.loads(open(csl_db_path, "r").read())
    content_pieces = generateHTML(db)
    citations = content_pieces["citations"]
    year_links = content_pieces["links"]
    patents = content_pieces["patents"]
    citations.reverse()
    year_links.reverse()
    content = "\n".join(citations)
    preamble = INSTRUMENTS[instrument].get('header', '')
    if len(patents) > 0:
        preamble += PATENTS_SECTION.format(patent_items="\n                        ".join(patents))
    postscript = INSTRUMENTS[instrument].get('footer', '')
    title = INSTRUMENTS[instrument].get("title", "{instrument} Instrument".format(instrument=instrument))
    output = TEMPLATE.format(title=title, content=content, yearlinks=", ".join(year_links), preamble=preamble, postscript=postscript)
    output_filename = "static/{instrument}_pubs.html".format(instrument=instrument)
    open(output_filename, "w").write(output)
    
if __name__ == '__main__':
    import sys
    instruments = sys.argv[1:]
    if len(instruments) < 1:
        print("usage: citeproc_to_html.py <instrument> <other_instrument>... or citeproc_to_html.py all")
    elif instruments[0].lower() == "all":
        for instrument in INSTRUMENTS:
            makePage(instrument)
    else:
        for instrument in instruments:
            makePage(instrument)
