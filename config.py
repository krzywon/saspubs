SANS_HEADER_START = r"""
<p>If you have written a paper that reports measurements using this instrument and you do not see it in the list below, or if the paper is listed but the 
information is incorrect or out of date, please inform <a href="mailto:jkrzywon@nist.gov">Jeff Krzywon</a> and/or <a href="mailto:butler@nist.gov">Paul Butler</a>.</p>
"""

SANS_HEADER_FINISH = r"""
<p>If you reduced your data using the Igor Macros, please include the reference ""<a href="http://dx.doi.org/10.1107/S0021889806035059">Reduction and Analysis of SANS and USANS Data using Igor Pro</a>", Kline, S. R. <i>J Appl. Cryst.</i> <b>39</b>(6), 895 (2006).</p>
<p>Please be aware that all papers with NIST coauthors must be reviewed and approved by the Washington Editorial Review Board (WERB). Members of WERB are concerned not only with scientific merit but with three specific matters: measurement uncertainties, the use of SI units, and brand names. For more detailed information please visit <A href="https://www.nist.gov/ncnr/nist-technical-publication-policy-werb">WERB</A> and/or speak with your NIST coauthor(s).</p>
"""

NG7SANS_HEADER = (SANS_HEADER_START + r"""
<p>If you write a paper that reports measurements using the NG7 30m SANS Instrument, please be sure to
<ol>
<li>include an acknowledgement to NIST if there are no NIST coauthors,and</li>
<li>include a reference to the paper describing the 30m SANS Instruments: "<a href="http://dx.doi.org/10.1107/S0021889897017020">The 30 m Small-Angle Neutron Scattering Instruments at the National Institute of Standards and Technology</a>", Glinka CJ, et al. <i>J Appl. Cryst.</i> <b>31</b>(3), 430 (1998).  Thanks!</li>
</ol>
""" + SANS_HEADER_FINISH)

NGB30SANS_HEADER = (SANS_HEADER_START + r"""
<p>If you write a paper or give a presentation that reports measurements using the NG3/NGB30m SANS Instrument, please be sure to:</p>
<ol>
<li>include an <A href="https://www.nist.gov/ncnr/publishing-your-results/publishing-chrns-results">acknowledgement</A> to the NSF, and to NIST if there are no NIST coauthors,and</li>
<li>include a reference to the paper describing the 30m SANS Instruments: "<a href="http://dx.doi.org/10.1107/S0021889897017020">The 30 m Small-Angle Neutron Scattering Instruments at the National Institute of Standards and Technology</a>", Glinka CJ, et al. <i>J Appl. Cryst.</i> <b>31</b>(3), 430 (1998).  Thanks!</li>
</ol>
""" + SANS_HEADER_FINISH)

USANS_HEADER = (SANS_HEADER_START + r"""
<p>If you write a paper or give a presentation that reports measurements using the USANS Instrument, please be sure to:</p>
<ol type="lower-alpha">
<li>include an <A href="https://www.nist.gov/ncnr/publishing-your-results/publishing-chrns-results">acknowledgement</A> to the NSF, and to NIST if there are no NIST coauthors,and</li>
<li>include a reference to the paper describing the USANS Instrument: "<a href="http://dx.doi.org/10.1107/S0021889805032103">Design and performance of a thermal-neutron double-crystal diffractometer for USANS at NIST</a>", Barker JG, et al. <i>J Appl. Cryst.</i> <b>38</b>(6), 1004 (2005).</li>
</ol>
""" + SANS_HEADER_FINISH)

VSANS_HEADER = (SANS_HEADER_START + r"""
<p>If you write a paper or give a presentation that reports measurements using the vSANS Instrument, please be sure to include an <A href="https://www.nist.gov/ncnr/publishing-your-results/publishing-chrns-results">acknowledgement</A> to the NSF, and to NIST if there are no NIST coauthors.</p>
""" + SANS_HEADER_FINISH)

SANS_HEADER = (SANS_HEADER_START + r"""
<p>If you write a paper that reports measurements using any of the SANS Instruments, please be sure to:</p>
<ol>
<li>Include an acknowledgement to NIST if there are no NIST coauthors.</li>
<li>For the NGB 30m SANS, USANS, and VSANS instruments include an <A href="https://www.nist.gov/ncnr/publishing-your-results/publishing-chrns-results"> acknowledgement</A> to the NSF.</li>
<li>include a reference to the appropriate paper describing the Instrument used (not applicable for 8m SANS):</li>
<ul>
<li>NG7 and NGB 30m SANS: "<a href="http://dx.doi.org/10.1107/S0021889897017020">The 30 m Small-Angle Neutron Scattering Instruments at the National Institute of Standards and Technology</a>", Glinka CJ, et al. <i>J Appl. Cryst.</i> <b>31</b>(3), 430 (1998).</li>
<li>USANS: "<a href="http://dx.doi.org/10.1107/S0021889805032103">Design and performance of a thermal-neutron double-crystal diffractometer for USANS at NIST</a>", Barker JG, et al. <i>J Appl. Cryst.</i> <b>38</b>(6), 1004 (2005).</li>
</ul>
</ol>
""" + SANS_HEADER_FINISH)

SANS_FOOTER = r"""
"""

MACS_HEADER = r"""
<h2>Acknowledgement Information</h2>

<p>If you write a paper that reports measurements using the MACS, please be sure to include this acknowledgement to the NSF, and to NIST</p>

<p><em>"Access to MACS was provided by the Center for High Resolution Neutron Scattering, a partnership between the National Institute of Standards and Technology and the National Science Foundation under Agreement No. DMR-1508249."</em></p>

<p>Please also include a reference to the following paper describing the MACS</p>

<p><em>"MACS-a new high intensity cold neutron spectrometer at NIST" by J. A. Rodriguez, D. M. Adler, P. C. Brand, C. Broholm, J. C. Cook, C. Brocker, R. Hammond, Z. Huang, P. Hundertmark, J. W. Lynn, N. C. Maliszewskyj, J. Moyer, J. Orndorff, D. Pierce, T. D. Pike, G. Scharfstein, S. A. Smee and R. Vilaseca, 
<a href="http://iopscience.iop.org/0957-0233/19/3/034023">Meas. Sci. Technol. 19 034023 (2008)</a></em></p>

<p>In addition, the following (or similar) acknowledgement is expected to appear in all publications of work done at the NCNR that do not explicitly have a coauthor from the NCNR.</p>

<p><em>We acknowledge the support of the National Institute of Standards and Technology, U.S. Department of Commerce, in providing the neutron research facilities used in this work.</em></p>

<p>Please be aware that all papers with NIST coauthors must be reviewed and approved by the Washington Editorial Review Board (WERB). Members of WERB are concerned not only with scientific merit but with three specific matters: measurement uncertainties, the use of SI units, and brand names. For more detailed information please click here, and/or speak with your NIST coauthor(s).</p>
<h3><a href="https://scholar.google.com/citations?hl=en&user=LUG29CwAAAAJ&view_op=list_works&authuser=1">MACS Publications statistics</a></h3>
"""
MACS_FOOTER = ""

HFBS_HEADER = r"""
<h2>Acknowledgment information</h2>
<p>If you have written a paper that includes data taken on the HFBS and you do not see it in the list below, or if the information in our list is incorrect, please contact Madhusudan Tyagi with the correct information.</p>

<p>If you write a paper that reports measurements using the HFBS, please be sure to:
  <ol type="a">
    <li>include an acknowledgment to the NSF, and to NIST if there are no NIST co-authors, and </li>
    <li>include a reference to the following paper:</li>
  </ol>

<span class="title"><a href="https://doi.org/10.1063/1.1568557">
The high-flux backscattering spectrometer at the NIST Center for Neutron Research
</a></span>
<span class="author">
Meyer, A., Dimeo, R.M., Gehring, P.M., and Neumann, D.A.
</span>
, 
<span class="journal">Review of Scientific Instruments</span>
<span class="volume"><b>74</b></span>, 2759-2777 (2003)
</p>

<p>If you used the DAVE software package to treat your data, please include an appropriate reference:</p>
<span class="title"><a href="http://nvl.nist.gov/pub/nistpubs/jres/114/6/V114.N06.A04.pdf">
DAVE: A comprehensive software suite for the reduction, visualization, and analysis of low energy neutron spectroscopic data
</a></span>
<span class="author">
R.T. Azuah, L.R. Kneller, Y. Qiu, P.L.W. Tregenna-Piggott, C.M. Brown, J.R.D. Copley, and R.M. Dimeo,
</span>
<span class="journal">J. Res. Natl. Inst. Stan. Technol.</span>
<span class="volume"><b>114</b></span>, 341-358 (2009).
</p>
<p>Please be aware that all papers with NIST co-authors must be reviewed and approved by the Washington Editorial Review Board (WERB). Members of WERB are concerned not only with scientific merit but with three specific matters: measurement uncertainties,	the use of SI units, and brand names. For more detailed information please click here and/or speak with your NIST co-author(s).</p>

"""
HFBS_FOOTER = ""

NSE_HEADER = """
<p>If you have written a paper that reports measurements using NSE and you do not see it in the list below, 
or if the paper is listed but the information is incorrect or out of date, please inform 
<a href="mailto:afaraone@nist.gov">Antonio Faraone</a>.
</p>
"""
NSE_FOOTER = ""

NG7REFL_HEADER = """
<p>If you have written a paper that includes data taken on the NG7 horizontal reflectometer and you do not see it in the list below, 
or if the information in our list is incorrect, please contact 
<a href="mailto:guangcui.yuan@nist.gov">Guangcui Yuan</a> with the correct information.</p>

<p>If you write a paper that reports measurements using the NG7, please be sure to:
<a href="https://www.nist.gov/ncnr/publishing-your-results">include an acknowledgment to NIST</a> if there are no NIST co-authors.
If you used the Reflpak software package to treat your data, please include 
<a href="http://www.ncnr.nist.gov/reflpak">an appropriate reference or acknowledgment.</a></p>

<p>Please be aware that all papers with NIST co-authors must be reviewed and approved by the Washington Editorial Review Board (WERB). 
Members of WERB are concerned not only with scientific merit but with three specific matters: 
<strong>measurement uncertainties</strong>, the use of <strong>SI units</strong>, and <strong>brand names</strong>. 
For more detailed information please <a href="https://www.nist.gov/ncnr/nist-technical-publication-policy-werb">click here</a> 
and/or speak with your NIST co-author(s).</p>
"""
NG7REFL_FOOTER = ""


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
        "collection": "TKAGDRTW",
        "header": NG7REFL_HEADER,
        "footer": NG7REFL_FOOTER
    },
    "NG7SANS": {
        "group": "1942669",
        "collection": "RV37EK44",
        "header": NG7SANS_HEADER,
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
        "collection": "2TQMBS9X",
        "header": NGB30SANS_HEADER,
        "footer": SANS_FOOTER
    },
    "NGB10SANS": {
        "group": "1942669",
        "collection": "QTGN36EH"
    },
    "NSE": {
        "group": "1942669",
        "collection": "XT6XYDEH",
        "header": NSE_HEADER,
        "footer": NSE_FOOTER
    },
    "SANS": {
        "group": "1942669",
        "collection": "BS3GD4WM",
        "header": SANS_HEADER,
        "footer": SANS_FOOTER
    },
    "USANS": {
        "group": "1942669",
        "collection": "64AMFBBD",
        "header": USANS_HEADER,
        "footer": SANS_FOOTER
    },
    "VSANS": {
        "group": "1942669",
        "collection": "E49EHS33",
        "header": VSANS_HEADER,
        "footer": SANS_FOOTER
    },
    "DCS": {
        "group": "1942669",
        "collection": "5NKTCIUL"
    },
    "BT1": {
        "group": "2165335",
        "collection": "E8D4RVEN",
        "title": "High Resolution Powder Diffractometer (BT1)"
    },
    "MACS": {
        "group": "1942669",
        "collection": "SCPXUF5T",
        "header": MACS_HEADER,
        "footer": MACS_FOOTER
    },
    "HFBS": {
        "group": "1942669",
        "collection": "9GDX95BA",
        "header": HFBS_HEADER,
        "footer": HFBS_FOOTER
    },
    "TEST": {
        "group": "1925268",
        "collection": "YQIVUSAD"
    },
    "TEST2": {
        "group": "1925268",
        "collection": "FAHFDH4G"
    },
    "He3": {
        "group": "2159399",
        "collection": "TCW8VPUS"
    },
    "He3_CANDOR": {
        "group": "2159399",
        "collection": "FWNBJJNN",
        "title": "He3 CANDOR"
    },
    "He3_MACS": {
        "group": "2159399",
        "collection": "TTE8G75U",
        "title": "He3 MACS"
    },
    "He3_MAGIK": {
        "group": "2159399",
        "collection": "XVSBQW83",
        "title": "He3 MAGIK"
    },
    "He3_NSF": {
        "group": "2159399",
        "collection": "7BI5GZQK",
        "title": "He3 NSF"
    },
    "He3_SANS": {
        "group": "2159399",
        "collection": "79PMRAEH",
        "title": "He3 SANS"
    },
    "He3_TRIPLEAXIS": {
        "group": "2159399",
        "collection": "3UC3GUJA",
        "title": "He3 Triple Axis"
    },
    "SURF": {
        "group": "2160414",
        "collection": "6W59BX5Z",
        "title": "NCNR SURF"
    },
    "SHIP": {
        "group": "2160414",
        "collection": "IUV4DIQ3",
        "title": "NCNR SHIP"
    },
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
