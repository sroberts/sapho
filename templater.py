#!/usr/bin/env python
# encoding: utf-8
"""
sapho: templater.py

Created by Scott Roberts.
Copyright (c) 2011 TogaFoamParty Studios. All rights reserved.
"""

import sys
import getopt


help_message = '''
Sapho Templater is for automatically generating, populating, and posting Sapho wiki pages to a Dokuwiki implimentation. This takes a lot of the pain out of generating a new page.
'''

class Templater(object):
    # Filler text pulled from http://www.lipsum.com
    lipsum = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    lipsum_short = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    lipsum_word = "Lorem ipsum"
    
    # Major Page Types
    def generateSetPage(pagename):
        wikitext = "====== Summary ======\n"
        wikitext += "%s" % lipsum
        wikitext += "==== Hypotheses ====\n"
        wikitext += "  * [[https://localhost/ach/%s|%s]]" % (hypothesispath, hypothesisname)
        
        wikitext += "====== Compromise Vector & Persistence ======\n"
        wikitext += "==== Compromise Vector ====\n"
        wikitext += "%s" % lipsum
        
        wikitext += "===== Persistence =====\n"
        wikitext += "%s" % lipsum
        
        wikitext += "====== Detection =====\n"
        wikitext += "==== ArcSight Content ====\n"
        wikitext += "  * %s" % lipsum_short
        
        wikitext += "==== Netwitness Content ====\n"
        wikitext += "  * %s" % lipsum_short
        
        wikitext += "==== Open Tickets ====\n"
        wikitext += "  * %s" % lipsum_short
        
        wikitext += "===== Indicators =====\n"
        wikitext += "==== Known Compromised Hosts ====\n"
        wikitext += "^ IP Address ^ Host Name ^ User Name ^ Title ^ Department ^ Notes ^\n"
        wikitext += "|            |           |           |       |            |       |\n"
        
        wikitext += "==== Known Compromised Accounts ====\n"
        wikitext += "^ Username ^ User ^ Notes ^\n"
        wikitext += "|          |      |       |\n"
        
        wikitext += "==== IP Indicators ====\n"
        wikitext += "^ IP Address ^ Location ^ URL ^ Research ^ Notes ^\n"
        wikitext += "|            |          |     |          |       |\n"
        
        wikitext += "==== URL Indicators ====\n"
        wikitext += "^ URL ^ Associated IP Addresses ^ Location ^ Research ^ Notes ^\n"
        wikitext += "|     |                         |          |          |       |\n"
        
        wikitext += "==== Known Attacker Ports ====\n"
        wikitext += "^ Port ^ Type ^ Service ^ Notes ^\n"
        wikitext += "|      |      |         |       |\n"
        
        wikitext += "==== Bad User Agent Strings ====\n"
        wikitext += "^  UserAgent String        ^ Notes ^\n"
        wikitext += "|                          |       |\n"
        
        wikitext += "==== Known Malicious Files ====\n"
        wikitext += "^ Filename ^ Type ^ Size ^ MD5 ^ SSDeep ^ File ^ Report ^ Notes ^\n"
        wikitext += "|          |      |      |     |        |      |        |       |\n"
        
        return [intrusion:pagename, wikitext]
    
    def generateWikiStartTemplate():
        wikitext = "====== Summary ======\n"
        wikitext += "===== Terms and Processes =====\n"
        wikitext += "  * [[Activity Classification]]\n"
        wikitext += "  * [[Wiki Conventions]]\n"
        
        wikitext += "====== News ======\n"
        wikitext += "===== SANS ISC =====\n"
        wikitext += "{{rss>http://isc.sans.edu/rssfeed_full.xml 5 author date 1h }}\n"
        wikitext += "===== Team Cymru =====\n"
        wikitext += "{{rss>http://www.team-cymru.org/News/secnews.rss 5 author date 1h }}\n"
        
        wikitext += "====== Intrusion Campaigns ======\n"
        wikitext += "===== Alpha Campaign =====\n"
        wikitext += "  * [[intrusion:Alpha Alpha]] - **Date Identified:** -\n"
        wikitext += "  * [[intrusion:Alpha Bravo]] - **Date Identified:** -\n"
        wikitext += "**C2:** - **Exfil:** -"
        wikitext += "===== Bravo Campaign =====\n"
        wikitext += "  * [[intrusion:Bravo Alpha]] - **Date Identified:** -\n"
        wikitext += "  * [[intrusion:Bravo Bravo]] - **Date Identified:** -\n"
        wikitext += "**C2:** - **Exfil:** -\n"
        
        wikitext += "====== Third Party Intelligence ======\n"
        wikitext += "  * [[thirdpartyintel:TPI-Alpha]] - **Date Received:** -\n"
        wikitext += "  * [[thirdpartyintel:TPI-Bravo]] - **Date Received:** -\n"
        wikitext += "  * [[thirdpartyintel:Archive]] - **Date Received:** -\n"
        
        wikitext += "====== Known Malicious Tools ======\n"
        wikitext += "===== Exploits =====\n"
        wikitext += "  * [[malcode:Alpha.exploit]] - Exploitation tool Alpha.\n"
        wikitext += "===== Implants =====\n"
        wikitext += "  * Alpha\n"
        wikitext += "    * AA: [[malcode:Alpha.implant]]\n"
        wikitext += "  * Bravo\n"
        wikitext += "    * BA: [[malcode:Bravo.implant]]\n"
        wikitext += "===== Utilities =====\n"
        wikitext += "  * [[malcode:Alpha.util]] - Alpha.util summary.\n"
        
        wikitext += "====== Sapho Tools ======\n"
        wikitext += "  * [[Sapho.util]] - Sapho.util summary.\n"
        
        wikitext += "====== Known Threat Actors ======\n"
        wikitext += "===== Known Threat Groups =====\n"
        wikitext += "  * [[actor:Actor Alpha]]\n"
        wikitext += "  * [[actor:Actor Bravo]]\n"
        wikitext += "===== Known Threat Actors =====\n"
        wikitext += "  * [[actor:Person Alpha]]\n"
        wikitext += "  * [[actor:Person Bravo]]\n"
        
        wikitext += "====== Templates ======\n"
        wikitext += "  * [[template:Compromise Page Template]]\n"
        wikitext += "  * [[template:Attacker Tool Page Template]]\n"
        
        return wikitext
    
    def generateThirdPartyIntelligencePage(self):
        """docstring for generateThirdPartyIntelligencePage"""
        pass
    
    def generateExploitPage(self):
        """docstring for generateExploitPage"""
        pass
    
    def generateImplantsPage(self):
        """docstring for generateImplantsPage"""
        pass
    def generateUtilitiesPage(self):
        """docstring for generateUtilitiesPage"""
        pass
    def generateSaphoToolPage(self):
        """docstring for generateSaphoToolPage"""
        pass
    
    def generateKnownThreatGroupPage(self):
        """docstring for generateKnownThreatGroupPage"""
        pass
    
    def generateKnownThreatActorPage(self):
        """docstring for generateKnownThreatActorPage"""
        pass
    
    # Common Elements
    def generateNewsArticle(title=lipsum_short, author=lipsum_word, date="20000101", url="hxxp://www.example.com/article", article_body=lipsum):
        wikitext = "==== %s ====" % title
        wikitext += "^ Author | %s |" % author
        wikitext += "^ Date   | %s |" % date
        wikitext += "^ URL    | %s |" % url
        
        wikitext += "> %s" % article_body

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "hp:v", ["help", "name="])
        except getopt.error, msg:
            raise Usage(msg)
    
        # option processing
        for option, value in opts:
            if option == "-v":
                verbose = True
            if option in ("-h", "--help"):
                raise Usage(help_message)
            if option in ("p", "--name"):
                output = value
    
        "==== %s ====" % (title)
        "^ Author | %s |" % (author)
        "^ Date   | %s |" % (date)
        "^ URL    | %s |" % (url)
        
        for line in artcile_body.split"\n":
            print "> %s" % line
    
    def postAsPage(self, pagename, wikitext):
        """docstring for postAsPage"""
        pass

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "ho:v", ["help", "output="])
        except getopt.error, msg:
            raise Usage(msg)
        
        # option processing
        for option, value in opts:
            if option == "-v":
                verbose = True
            if option in ("-h", "--help"):
                raise Usage(help_message)
            if option in ("-o", "--output"):
                output = value
            
    except Usage, err:
        print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
        print >> sys.stderr, "\t for help use --help"
        return 2


if __name__ == "__main__":
    sys.exit(main())