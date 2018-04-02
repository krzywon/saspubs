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

SANS_FOOTER = r"""\
"""

MACS_HEADER = r"""\
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
        "collection": "XT6XYDEH"
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
    "DCS": {
        "group": "1942669",
        "collection": "5NKTCIUL"
    },
    "MACS": {
        "group": "1942669",
        "collection": "SCPXUF5T",
        "header": MACS_HEADER,
        "footer": MACS_FOOTER
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
