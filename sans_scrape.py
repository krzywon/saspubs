import requests
import json
import re

#DOI_MATCH = re.compile(r'doi\.org/([^\"]+)"')
DOI_MATCH = re.compile(r'"http.*/(10\.[^"]+)"')
DOI_XML_MATCH = re.compile(r'>http.*/(10\.[^<]+)<')

turl = "https://www.ncnr.nist.gov/instruments/ng7sans/ng7_sans_publications.html"

url_params = {
    #"NGB30SANS": {
        #"base_url": "https://www.ncnr.nist.gov/instruments/ng3sans/",
        #"previous_years_url": "ng3_sans_publications_%d.html",
        #"previous_years": {"start": 2001, "end": 2016},
        #"current": "ng3_sans_publications.html"
    #},
    #"NG7SANS": {
        #"base_url": "https://www.ncnr.nist.gov/instruments/ng7sans/",
        #"previous_years_url": "ng7_sans_publications_%d.html",
        #"previous_years": {"start": 2001, "end": 2016},
        #"current": "ng7_sans_publications.html"
    #},
    #"PBR": {
        #"base_url": "https://www.ncnr.nist.gov/instruments/pbr/",
        #"current": "pub.html"
    #},
    #"BT7": {
    #    "base_url": "https://ncnr.nist.gov/instruments/bt7_new/",
    #    "current": "Thermal_Triple_Axis_Publications.html"
    #},
    #"NSE": {
    #    "base_url": "https://www.ncnr.nist.gov/instruments/nse/",
    #    "current": "NSE_publications.html"
    #},
    #"NG7R": {
    #    "base_url": "https://ncnr.nist.gov/instruments/ng7refl/",
    #    "current": "NG7pubs.html"
    #},
    #"USANS": {
      #"base_url": "https://www.ncnr.nist.gov/instruments/usans/",
      #"current": "publications.html"
    #},
    #"USANS_earlier": {
      #"base_url": "https://www.ncnr.nist.gov/instruments/usans/",
      #"current": "publications_early.html" 
    #},
    #"DCS": {
      #"base_url": "https://ncnr.nist.gov/instruments/dcs/",
      #"current": "dcs_pubs.html"
    #},
    #"MACS": {
      #"base_url": "https://ncnr.nist.gov/instruments/macs/",
      #"current": "publications.html"
    #},
    #"HFBS": {
      #"base_url": "https://www.ncnr.nist.gov/instruments/hfbs/",
      #"current": "HFBS-Pub.xml"
    #},
    "BT1": {
        "base_url": "https://ncnr.nist.gov/instruments/bt1/",
        "current": "bt1_pubs.html"
    }
}

doi_lists = {}

for k,v in url_params.items():
    doi_list = []
    cy = requests.get(v["base_url"] + v["current"]).text
    doi_list.extend(DOI_MATCH.findall(cy))
    doi_list.extend(DOI_XML_MATCH.findall(cy))
    if "previous_years" in v:
        for y in range(v["previous_years"]["start"], v["previous_years"]["end"]+1):
            print(v["previous_years_url"] % y)
            cy = requests.get(v["base_url"] + (v["previous_years_url"] % y)).text
            doi_list.extend(DOI_MATCH.findall(cy))
            doi_list.extend(DOI_XML_MATCH.findall(cy))
    doi_lists[k] = doi_list
    #open(k + "_dois.json", "w").write(json.dumps(doi_list, indent=2))
    open(k + "_bare_dois.txt", "w").write("\n".join(doi_list))
    

    
