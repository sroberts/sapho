#!/usr/bin/env python
# encoding: utf-8
"""
sapho: templater.py

Created by Scott Roberts.
Copyright (c) 2011 TogaFoamParty Studios. All rights reserved.
"""

import sys
import getopt
import datetime
from dokuwikixmlrpc import *

# Filler text pulled from http://www.lipsum.com except date, url, email
lipsum = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
lipsum_short = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
lipsum_word = "Lorem ipsum"
lipsum_date = "19990101" #sample date in YYYYMMDD format
lipsum_datetime = "19990101 12:00:00" #sample date in YYYYMMDD HH:MM:SS format
lipsum_ip = "192.168.1.1"
lipsum_url = "http://www.example.com"
lipsum_email = "sample@example.com"
lipsum_num = 0000
	
# Wiki Classes
class SaphoTemplater(object):
	
	"""def __init__(self, url=None, username=None, password=None):
		
		if url == True:
			self.wiki = DokuWikiClient(url, username, password)"""
	
	# Major Page Types
	def generateSetPage(self, summary=lipsum, compromise=lipsum, from_addresses=[[lipsum_word, lipsum_email], [lipsum_word, lipsum_email]], to_addresses=[[lipsum_word, lipsum_email], [lipsum_word, lipsum_email]], cc_addresses=[[lipsum_word, lipsum_email], [lipsum_word, lipsum_email]], datetime=lipsum_datetime, subject=lipsum_short, body=lipsum, attachments=[lipsum_word, lipsum_word], persistence=lipsum, siem_content=[lipsum_short, lipsum_short], ids_rules=[lipsum_short, lipsum_short], fw_rules=[lipsum_short, lipsum_short],tickets=[lipsum_short, lipsum_short], notes=lipsum):
		wikitext = "====== Summary ======\n"
		wikitext += "%s\n" % summary
		
		wikitext += "====== Compromise Vector & Persistence ======\n"
		wikitext += "===== Compromise Vector =====\n"
		wikitext += "%s\n" % compromise
		
		wikitext += "==== Phishing/Spearfishing/Spam Email ====\n"
		
		from_add = ""
		for from_address in from_addresses:
			from_add += "%s <%s>, " % (from_address[0], from_address[1])
		wikitext += "^ From			| %s |\n" % from_add
		
		to = ""
		for to_address in to_addresses:
			to += "%s <%s>, " % (to_address[0], to_address[1])
		wikitext += "^ To			| %s |\n" % to
		
		cc = ""
		for cc_address in cc_addresses:
			cc += "%s <%s>, " % (cc_address[0], cc_address[1])
		wikitext += "^ CC			| %s |\n" % cc
		
		wikitext += "^ Date & Time	| %s |\n" % datetime
		
		wikitext += "^ Subject		| %s |\n" % subject
		wikitext += "^ Body			| <nowiki>%s</nowiki>|\n" % body
		
		attached = ""
		for attachment in attachments:
			attached += "%s, " % attachments
		wikitext += "^ Attachments 	| FIXME Add using files dialog %s |\n" % attached
		wikitext += "^ MIME			| FIXME Add using file dialog |\n"
		
		wikitext += "===== Persistence =====\n"
		wikitext += "%s\n" % persistence
		
		wikitext += "====== Detection =====\n"
		wikitext += "==== SIEM Content ====\n"
		for siem_rule in siem_content:
			wikitext += "  * %s\n" % siem_rule
			
		wikitext += "==== IDS Content ====\n"
		for ids_rule in ids_rules:
			wikitext += "  * %s\n" % ids_rule
			
		wikitext += "==== Firewall Content ====\n"
		for fw_rule in fw_rules:
			wikitext += "  * %s\n" % ids_rule
			
		wikitext += "==== Open Tickets ====\n"
		for ticket in tickets:
			wikitext += "  * %s\n" % ticket
			
		wikitext += "===== Compromised Resources =====\n"	
		wikitext += "==== Known Compromised Hosts ====\n"
		wikitext += "^ IP Address ^ Host Name ^ User Name ^ Title ^ Department ^ Notes ^\n"
		wikitext += "|			  |			   |           |       |            |       |\n"
		
		wikitext += "==== Known Compromised Accounts ====\n"
		wikitext += "^ Username ^ User ^ Notes ^\n"
		wikitext += "|		 	|	   |	    |\n"
		
		wikitext += "===== Indicators =====\n"		
		wikitext += "==== IP Indicators ====\n"
		wikitext += "^ IP Address ^ Location ^ URL ^ Research ^ Notes ^\n"
		wikitext += "|			  |			  |     |          |       |\n"
		
		wikitext += "==== URL Indicators ====\n"
		wikitext += "^ URL ^ Associated IP Addresses ^ Location ^ Research ^ Notes ^\n"
		wikitext += "|	  |			||	  ||\n"
		
		wikitext += "==== Known Attacker Ports ====\n"
		wikitext += "^ Port ^ Type ^ Service ^ Notes ^\n"
		wikitext += "|		|	   |		 |		 |\n"
		
		wikitext += "==== Bad SSL Certificate ====\n"
		wikitext += "^ Version								|		|\n" 
		wikitext += "^ Serial Number						|		|\n" 
		wikitext += "^ Algorithm ID							|		|\n" 
		wikitext += "^ Issuer								|		|\n" 
		wikitext += "^ Validity								|		|\n" 
		wikitext += "^ Not Before							|		|\n" 
		wikitext += "^ Not After							|		|\n" 
		wikitext += "^ Subject								|		|\n" 
		wikitext += "^ Subject Public Key Info				|		|\n" 
		wikitext += "^ Public Key Algorithm					|		|\n" 
		wikitext += "^ Subject Public Key					|		|\n" 
		wikitext += "^ Issuer Unique Identifier (optional)	|		|\n" 
		wikitext += "^ Subject Unique Identifier (optional)	|		|\n" 
		wikitext += "^ Extensions (optional)				|		|\n" 
		wikitext += "^ Certificate Signature Algorithm		|		|\n" 
		wikitext += "^ Certificate Signature				|		|\n"
		
		wikitext += "==== Bad User Agent Strings ====\n"
		wikitext += "^ UserAgent String ^ Notes ^\n"
		wikitext += "|					|  		|\n"
		
		wikitext += "==== Known Malicious Files ====\n"
		wikitext += "^ Filename ^ Type ^ Size ^ MD5 ^ SSDeep ^ File ^ Report ^ Notes ^\n"
		wikitext += "|			|	   |	  |	 	|		 |	  	|		 |	   	 |\n"
		
		wikitext += "===== Notes =====\n"
		wikitext += "%s" % notes
		
		return wikitext
	
	def generateWikiStartTemplate(self):
		wikitext = "====== Summary ======\n"
		wikitext += "{{http://infosuck.org/0x003f.png?600}} \n\nFIXME at least remove the hotlink.\n"
		
		wikitext += "===== Terms and Processes =====\n"
		wikitext += "  * [[Activity Classification]]\n"
		wikitext += "  * [[Wiki Conventions]]\n"
		wikitext += "  * [[Suggested Reading]]\n"
		
		wikitext += "====== News ======\n"
		wikitext += "===== SANS ISC =====\n"
		wikitext += "{{rss>http://isc.sans.edu/rssfeed_full.xml 5 author date 1h }}\n"
		wikitext += "===== US-CERT: Technical Security Alerts =====\n"
		wikitext += "{{rss>https://www.us-cert.gov/channels/techalerts.rdf 5 author date 1h }}\n"
		wikitext += "===== Team Cymru =====\n"
		wikitext += "{{rss>http://www.team-cymru.org/News/secnews.rss 5 author date 1h }}\n"
		
		wikitext += "====== Intrusion Campaigns ======\n"
		wikitext += "===== Alpha Campaign =====\n"
		wikitext += "  * [[intrusionset:Alpha Alpha]] - **Date Identified:** 19990101\n"
		wikitext += "  * [[intrusionset:Alpha Bravo]] - **Date Identified:** 19990101\n"
		wikitext += "**C2:** - **Exfil:** -"
		wikitext += "===== Bravo Campaign =====\n"
		wikitext += "  * [[intrusionset:Bravo Alpha]] - **Date Identified:** 19990101\n"
		wikitext += "  * [[intrusionset:Bravo Bravo]] - **Date Identified:** 19990101\n"
		wikitext += "**C2:** - **Exfil:** -\n"
		wikitext += "\n[[intrusionset:Archived Intrusion Sets]]\n"
		
		wikitext += "====== Third Party Intelligence ======\n"
		wikitext += "  * [[thirdpartyintel:TPI-Alpha]] - **Date Received:** 19990101\n"
		wikitext += "  * [[thirdpartyintel:TPI-Bravo]] - **Date Received:** 19990101\n"
		wikitext += "  * [[thirdpartyintel:Archived Third Party Intelligence]]\n"
		
		wikitext += "====== Known Malicious Tools ======\n"
		wikitext += "===== Exploits =====\n"
		wikitext += "  * [[malcode_exploits:Alpha.exploit]] - Exploitation tool Alpha.\n"
		wikitext += "  * [[malcode_exploits:Bravo.exploit]] - Exploitation tool Bravo.\n"
		wikitext += "===== Implants =====\n"
		wikitext += "  * Alpha\n"
		wikitext += "    * AA: [[malcode_implants:Alpha.implant]]\n"
		wikitext += "  * Bravo\n"
		wikitext += "    * BA: [[malcode_implants:Bravo.implant]]\n"
		wikitext += "===== Utilities =====\n"
		wikitext += "  * [[malcode_utilities:Alpha.util]] - Alpha.util summary.\n"
		wikitext += "  * [[malcode_utilities:Bravo.util]] - Bravo.util summary.\n"
		
		wikitext += "====== Known Threat Actors ======\n"
		wikitext += "===== Known Threat Groups =====\n"
		wikitext += "  * [[actor:Group Alpha]] - Prefix: Alpha\n"
		wikitext += "  * [[actor:Group Bravo]] - Prefix: Bravo\n"
		wikitext += "===== Known Threat Actors =====\n"
		wikitext += "  * [[actor:Person Alpha]]  - Prefix: Alpha\n"
		wikitext += "  * [[actor:Person Bravo]]  - Prefix: Alpha\n"
		
		wikitext += "====== Templates ======\n"
		wikitext += "  * [[template:Intrusion Set Page]]\n"
		wikitext += "  * [[template:Third Party Intelligence Page]]\n"
		wikitext += "  * [[template:Exploit Page]]\n"
		wikitext += "  * [[template:Implant Page]]\n"
		wikitext += "  * [[template:Malicious Group Page]]\n"
		wikitext += "  * [[template:Malicious Actor Page]]\n"
		
		return wikitext
	
	def generateThirdPartyIntelligencePage(self, filename="example.file", tipDate=datetime.date.today(), analystName=lipsum_word, data=lipsum, indicators = [lipsum_word, lipsum_word]):
		"""Generates a page for adding any Third Party intelligence products to the wiki. May require some manipulation to add into wiki format."""
		wikitext = "====== Metadata ======\n"
		wikitext += "^ File    | %s |\n" % (filename)
		wikitext += "^ Date    | %s |\n" % (tipDate)
		wikitext += "^ Analyst | %s |\n" % (analystName)
		
		wikitext += "====== Data ======\n"
		wikitext += "%s\n" % (data)
		
		wikitext += "====== Indicators ======\n"
		for indicator in indicators:
			wikitext += "  * %s\n" % (indicator)
			
		wikitext += "**File:** FIXME Add files here with upload dialog.\n" 

		return wikitext
	
	def generateExploitPage(self, exploit_name=lipsum_word, date_exploit_identified=lipsum_date, date_exploit_public=lipsum_date, date_exploit_updated=lipsum_date, author=lipsum_word, actor="[[Alpha]]", vuln_app=lipsum_word, vuln_mod=lipsum_word, vuln_ver="1.0", vuln_lang=lipsum_word, vuln_patch="N/A", mitigation=lipsum, edb=0000, cve="CVE-0000-0000", osvdb=0000, exploit_sources=[lipsum_url,lipsum_url], notes=lipsum):
		wikitext = "===== Timeline =====\n"
		wikitext += "^ Exploit Identified | %s |\n" % date_exploit_identified
		wikitext += "^ Public Exploit Published | %s |\n" % date_exploit_public
		wikitext += "^ Exploit Updated | %s |\n" % date_exploit_updated
		
		wikitext += "===== Developer =====\n"
		wikitext += "Author: %s\n" % author
		wikitext += "Actor: %s\n" % actor
		
		wikitext += "===== Vulnerable Systesm =====\n"
		wikitext += "^ Vulnerable Application | %s |\n" % vuln_app
		wikitext += "^ Vulnerable Module      | %s |\n" % vuln_mod
		wikitext += "^ Vulnerable Versions    | %s |\n" % vuln_ver
		wikitext += "^ Vulnerable Languages   | %s |\n" % vuln_lang
		wikitext += "^ Patch                  | %s |\n" % str(vuln_patch)
		
		wikitext += "===== Mitigation =====\n"
		wikitext += "%s\n" % mitigation
		
		wikitext += "===== Files =====\n"
		wikitext += "^ Delivery Code | FIXME Add files with upload dialog. |\n" 
		wikitext += "^ Exploit Code | FIXME Add files with upload dialog. |\n"
		
		wikitext += "===== References =====\n"
		wikitext += "ExploitDB-ID: %s\n" % str(edb)
		wikitext += "CVE: %s\n" % cve
		wikitext += "OSVDB-ID: %s\n" % str(osvdb)
		
		wikitext += "=== Exploit Sources ===\n"
		for exploit_source in exploit_sources:
			wikitext += "  * <nowiki>%s</nowiki>\n" % exploit_source 
			
		wikitext += "===== Notes =====\n"
		wikitext += "%s\n" % notes
		
		return wikitext
	
	def generateImplantPage(self, intrusionSet="Alpha Alpha", filename="Example.file", filetype="example", fileSize=0000, md5sum="d41d8cd98f00b204e9800998ecf8427e", sha="da39a3ee5e6b4b0d3255bfef95601890afd80709", ssdeep="3::", date=lipsum_date, analystName=lipsum_word, summary=lipsum, avDefs = {"Symantec": "none", "McAfee":"none"}, filehooking=[lipsum_short, lipsum_short], persistence=[lipsum_short, lipsum_short], spreading_mechs=[lipsum_short, lipsum_short], exfil_mechs=[lipsum_short, lipsum_short], c2_mechs=[lipsum_short, lipsum_short], oss=[lipsum_short, lipsum_short], requiredfiles=[lipsum_short, lipsum_short], secondstages=[lipsum_short, lipsum_short], regkeys=[lipsum_short, lipsum_short], behav_summary=lipsum, logs=[lipsum_short, lipsum_short], strings=[lipsum_short, lipsum_short], other=[lipsum_short, lipsum_short], network_indicators=[lipsum_short, lipsum_short], fs_indicators=[lipsum_short, lipsum_short], mitigation_steps=[lipsum_short, lipsum_short], eradication_steps=[lipsum_short, lipsum_short]):
		"""docstring for generateImplantsPage"""
		
		wikitext = "^ Implant Report    | %s: %s |\n" % (intrusionSet, filename)
		wikitext += "^ Reverse Engineer  | %s |\n" % (analystName)
		wikitext += "^ Date              | %s |\n" % (date)
		wikitext += "^ Associated FO Set | %s |\n" % (intrusionSet)
		
		wikitext += "===== Summary of the Analysis: =====\n"
		wikitext += "%s\n" % (summary)
		
		wikitext += "===== Identification =====\n"
		wikitext += "^ File Name | %s |\n" % (filename)
		wikitext += "^ File Type | %s |\n" % (filetype)
		wikitext += "^ File Size | %s |\n" % (str(fileSize))
		wikitext += "^ MD5	   | %s |\n" % (md5sum)
		wikitext += "^ SHA	   | %s |\n" % (sha)
		wikitext += "^ Ssdeep	| %s |\n" % (ssdeep) 
		
		wikitext += "====Current anti-virus detection capabilities:====\n"
		for vendor in avDefs:
			wikitext += "^ %s | %s |\n" % (vendor, avDefs[vendor])
			
		wikitext += "===== Characteristics =====\n"
		wikitext += "==== File Hooking ====\n"
		for filehook in filehooking:
			wikitext += "  * %s\n" % (filehook)
			
		wikitext += "==== Persistence Mechanisms ====\n"
		for persistance_mech in persistence:
			wikitext += "  * %s\n" % (persistance_mech)
			
		wikitext += "==== Spreading Mechanisms ====\n"
		for spreading_mech in spreading_mechs:
			wikitext += "  * %s\n" % (spreading_mech)
			
		wikitext += "==== Exfiltration Mechanisms ====\n"
		for exfil_mech in exfil_mechs:
			wikitext += "  * %s\n" % (exfil_mech)
			
		wikitext += "==== Command and Control Mechanisms ====\n"
		for c2_mech in c2_mechs:
			wikitext += "  * %s\n" % (c2_mech)
			
		wikitext += "===== Dependencies =====\n"
		wikitext += "==== Supported Operating Systems ====\n"
		for os in oss:
			wikitext += "  * %s\n" % (os)
			
		wikitext += "==== Required Files ====\n"
		for requiredfile in requiredfiles:
			wikitext += "  * %s\n" % (requiredfile)
			
		wikitext += "==== Second Stage Downloads ====\n"
		for secondstage in secondstages:
			wikitext += "  * %s\n" % (secondstage)
			
		wikitext += "==== Registry Keys ====\n"
		for regkey in regkeys:
			wikitext += "  * %s\n" % (regkey)
			
		wikitext += "===== Behavioral and code analysis findings =====\n"
		wikitext += "//%s//\n" % (behav_summary)
		
		wikitext += "===== Supporting Figures =====\n"
		wikitext += "==== Logs ====\n"
		for log in logs:
			wikitext += "  * %s\n" % (log)
			
		wikitext += "==== Interesting Strings ====\n"
		for string in strings:
			wikitext += "  * %s\n" % (string)
			
		wikitext += "==== Other Relevant Files or Data ====\n"
		for oth in other:
			wikitext += "  * %s\n" % (oth)
			
		wikitext += "===== Incident Recommendations =====\n"
		wikitext += "==== Identification ====\n"	
		wikitext += "=== Network Indicators ===\n"
		for network_indicator in network_indicators:
			wikitext += "  * %s\n" % (network_indicator)
			
		wikitext += "=== File System Indicators ===\n"
		for fs_indicator in fs_indicators:
			wikitext += "  * %s\n" % (fs_indicator)
			
		wikitext += "==== Mitigation ====\n"
		wikitext += "=== Containment Steps ====\n"
		for mitigation_step in mitigation_steps:
			wikitext += "  * %s\n" % (mitigation_step)
			
		wikitext += "=== Eradication Steps ====\n"
		for eradication_step in eradication_steps:
			wikitext += "  * %s\n" % (eradication_step)
			
		return wikitext
	
	def generateThreatGroupPage(self, group_name="Alpha", group_summary=lipsum, group_presence=[lipsum_url, lipsum_url], group_type="Unknown", membership=["actor:person alpha", "actor:person bravo"], related_groups=["actor:group alpha", "actor:group bravo"], pre_ex_methods=[lipsum_short, lipsum_short], pre_ex_tools=[lipsum_word, lipsum_word], ex_methods=[lipsum_short, lipsum_short], ex_tools=[lipsum_word, lipsum_word], post_ex_methods=[lipsum_short, lipsum_short], post_ex_tools=[lipsum_word, lipsum_word], periods_of_operation=[[lipsum_date, lipsum_date], [lipsum_date, lipsum_date]]):
		"""Generates Dokuwiki page for profiling a malicious group including key methodologies and tools."""
		wikitext = "===== Group: %s =====\n" % group_name
		wikitext += "^ Summary | %s |\n" % group_summary
		
		sites = ""
		for site in group_presence:
			sites += "%s, " % site
			
		wikitext += "^ Web Presence | %s |\n" % sites
		wikitext += "^ Group Type | %s |\n" % group_type
		
		wikitext += "===== Membership =====\n"
		for member in membership:
			wikitext += "  * [[actor:%s]]\n" % member
		wikitext += "==== Associated Groups ====\n"
		for member in membership:
			wikitext += "  * [[actor:%s]]\n" % member
			
		wikitext += "===== Methodology & Tools =====\n"
		wikitext += "==== Pre-Exploitation Attempt ====\n"
		wikitext += "=== Methodology ===\n"
		for pre_ex_method in pre_ex_methods:
			wikitext += "  * %s\n" % pre_ex_method
			
		wikitext += "=== Tool Chain ===\n"
		for pre_ex_tool in pre_ex_tools:
			wikitext += "  * %s\n" % pre_ex_tool
			
		wikitext += "==== Exploitation Attempt ====\n"
		wikitext += "=== Methodology ===\n"
		for ex_method in ex_methods:
			wikitext += "  * %s\n" % ex_method
			
		wikitext += "=== Tool Chain ===\n"
		for ex_tool in ex_tools:
			wikitext += "  * %s\n" % ex_tool
			
		wikitext += "==== Post Exploitation Attempt ====\n"
		wikitext += "=== Methodology ===\n"
		for post_ex_method in post_ex_methods:
			wikitext += "  * %s\n" % post_ex_method
			
		wikitext += "=== Tool Chain ===\n"
		for post_ex_tool in post_ex_tools:
			wikitext += "  * %s\n" % post_ex_method
			
		wikitext += "===== Periods of Operations =====\n"
		for period_of_operation in periods_of_operation:
			wikitext += "  * %s - %s\n" % (period_of_operation[0], period_of_operation[1])
			
		return wikitext
	
	def generateThreatActorPage(self, actor_identifier=lipsum_word, date_audited=lipsum_date, given_name=lipsum_word, date_of_birth=lipsum_date, country_of_birth=lipsum_word, location=lipsum_word, age="00", names_aliases = [lipsum_word, lipsum_word], email_addresses = [lipsum_email, lipsum_email], im=lipsum_word, affiliation=lipsum_word, urls=lipsum_url,  domain_data=lipsum_url, google_searches=[lipsum_word, lipsum_word], social_media_sites = {"twitter":lipsum_url, "facebook":lipsum_url, "linkedin":lipsum_url}, notes=lipsum):
		"""Allows programatic generation of a page of a thrat actor. If no factors are given this generates a template page with dummy values."""
		wikitext = "====== %s ======\n" % actor_identifier
		wikitext += "^ Date Audited     | %s |\n" % date_audited
		wikitext += "^ Name             | %s |\n" % given_name
		wikitext += "^ DOB              | %s |\n" % date_of_birth
		wikitext += "^ Age              | %s |\n" % age
		wikitext += "^ Country of Birth | %s |\n" % country_of_birth
		wikitext += "^ Location         | %s |\n" % location
		
		wikitext += "===== Names/Aliases =====\n"
		for name_alias in names_aliases:
			wikitext += "  * %s\n" % name_alias
			
		wikitext += "===== Email Addresses =====\n"
		for email_address in email_addresses:
			wikitext += "  * %s\n" % email_address
			
		wikitext += "===== Web & Social Media Presence =====\n"
		wikitext += "^ IM Names               | %s | %s |\n" % (im, date_audited)
		wikitext += "^ Site/group Affiliation | %s | %s |\n" % (affiliation, date_audited)
		wikitext += "^ URLs                   | %s | %s |\n" % (urls, date_audited)
		wikitext += "^ Domain Data            | %s | %s |\n" % (domain_data, date_audited)
		wikitext += "^ Twitter                | %s | %s |\n" % (social_media_sites["twitter"], date_audited)
		wikitext += "^ Facebook               | %s | %s |\n" % (social_media_sites["facebook"], date_audited)
		wikitext += "^ LinkedIn               | %s | %s |\n" % (social_media_sites["linkedin"], date_audited)
		
		wikitext += "===== Screen Shots =====\n"
		wikitext += "FIXME Add relevent screenshots using file upload dialog\n"
		
		wikitext += "===== Investigation History =====\n" 
		wikitext += "^ Search Type ^ Search Term ^ Date Audited ^\n"
		for google_search in google_searches:
			wikitext += "| Google Search | %s | %s |\n" % (google_search, date_audited)
			
		wikitext += "===== Notes =====\n"
		wikitext += "%s" % notes
		
		return wikitext
	
	def initialSetup(self, wiki_url, username, password):
		"""initialSetup adds the default start page and sample templates to an uninitilized sapho setup"""
		self.postAsPage(wiki_url, username, password, "start", self.generateWikiStartTemplate())
		
		#add Activity Classification
		#add Wiki Conventions
		
		self.postAsPage(wiki_url, username, password, "intrusionset:alpha_alpha", self.generateSetPage())
		self.postAsPage(wiki_url, username, password, "intrusionset:alpha_bravo", self.generateSetPage())
		self.postAsPage(wiki_url, username, password, "intrusionset:bravo_alpha", self.generateSetPage())
		self.postAsPage(wiki_url, username, password, "intrusionset:bravo_bravo", self.generateSetPage())
		
		#add Archived Sets page
		
		self.postAsPage(wiki_url, username, password, "thirdpartyintel:tpi-alpha", self.generateThirdPartyIntelligencePage())
		self.postAsPage(wiki_url, username, password, "thirdpartyintel:tpi-bravo", self.generateThirdPartyIntelligencePage())
		
		self.postAsPage(wiki_url, username, password, "malcode_exploits:alpha.exploit", self.generateExploitPage())
		self.postAsPage(wiki_url, username, password, "malcode_exploits:bravo.exploit", self.generateExploitPage())
		
		self.postAsPage(wiki_url, username, password, "malcode_implants:alpha.implant", self.generateImplantPage())
		self.postAsPage(wiki_url, username, password, "malcode_implants:bravo.implant", self.generateImplantPage())
		
		#add Utility code page
		
		self.postAsPage(wiki_url, username, password, "actor:Group Alpha", self.generateThreatGroupPage())
		self.postAsPage(wiki_url, username, password, "actor:Group Bravo", self.generateThreatGroupPage())
		
		self.postAsPage(wiki_url, username, password, "actor:Person Alpha", self.generateThreatActorPage())
		self.postAsPage(wiki_url, username, password, "actor:Person Bravo", self.generateThreatActorPage())
		
		self.postAsPage(wiki_url, username, password, "template:Intrusion Set Page", self.generateSetPage())
		self.postAsPage(wiki_url, username, password, "template:Third Party Intelligence Page", self.generateThirdPartyIntelligencePage())
		self.postAsPage(wiki_url, username, password, "template:Exploit Page", self.generateExploitPage())
		self.postAsPage(wiki_url, username, password, "template:Implant Page", self.generateImplantPage())
		self.postAsPage(wiki_url, username, password, "template:Malicious Group Page", self.generateThreatGroupPage())
		self.postAsPage(wiki_url, username, password, "template:Malicious Actor Page", self.generateThreatActorPage())
		
	
	# Common Elements Generators
	def generateNewsArticlePage(self, title=lipsum_word, author=lipsum_word, date="20000101", url=lipsum_url, article_body=lipsum):
		"""Creates wikitext for news article."""
		wikitext = "==== %s ====\n" % title
		wikitext += "^ Author | %s |\n" % author
		wikitext += "^ Date   | %s |\n" % date
		wikitext += "^ URL    | %s |\n\n" % url
		
		for line in article_body.split("\n"):
			wikitext += "> %s\n" % line
			
		return wikitext
	
	def generateIpHeaderWikiText(self, version=lipsum_word, ihl=lipsum_word, typeOfService=lipsum_num, totalLength=lipsum_num, identification=lipsum_num, flags=lipsum_word, fragmentOffset=lipsum_num, ttl=lipsum_num, protocol=lipsum_num, headerChecksum=lipsum_word, sip=lipsum_ip, dip=lipsum_ip, options=lipsum_word, padding=lipsum_num):
		"""Creates wikitext for IPv4 header information."""
		
		wikitext = "=== IP Header ===\n"
		wikitext += "^  Version  ^  IHL  ^  Type of Service  ^  Total Length  ^\n"
		wikitext += "|  %s  |  %s  |  %s  |  %s  |\n" % (version, ihl, typeOfService, totalLength)
		wikitext += "^  Identification  ^^  Flags  ^  Fragment Offset  ^\n"
		wikitext += "|  %s  ||  %s  |  %s  |\n" % (identification, flags, fragmentOffset)
		wikitext += "^  Time To Live  ^  Protocol  ^  Header Checksum  ^^\n"
		wikitext += "|  %s  |  %s  |  %s  ||\n" % (ttl, protocol, headerChecksum)
		wikitext += "^  Source IP Address  ^^^^\n"
		wikitext += "|  %s  ||||\n" % (sip)
		wikitext += "^  Destination IP Address  ^^^^\n"
		wikitext += "|  %s  ||||\n" % (dip)
		wikitext += "^  Options  ^^^  Padding  ^\n"
		wikitext += "|  %s  |||  %s  |\n" % (options, padding)
		
		return wikitext
		
	def generateIcmpHeaderWikiText(self, icmpType="1", icmpCode="1", checksum=lipsum_word, restOfHeader=lipsum_short):
		"""Creates wikitext for ICMP header information."""
		
		wikitext = "=== ICMP Header ===\n"
		wikitext += "^  Type  ^  Code  ^  Checksum  ^\n"
		wikitext += "|  %s  |  %s  |  %s  |\n" % (icmpType, icmpCode, checksum)
		wikitext += "^  Rest of Header  ^^^\n"
		wikitext += "|  %s  |||\n" % (restOfHeader)
		
		return wikitext
		
	def generateIpv4TcpHeaderWikiText(self, sip=lipsum_ip, dip=lipsum_ip, seqNum=lipsum_num, ackNum=lipsum_num, dataOffset=lipsum_num, reserved="", urg="0", ack="0", psh="0", rst="0", syn="0", fin="0", window=lipsum_num, checksum=lipsum_num, urgentPointer=lipsum_num, options=lipsum_word, padding=lipsum_num, data=lipsum_short):
		"""Creates wikitext for IPv4 TCP header information."""
		
		wikitext = "=== IPv4 TCP Header ===\n"
		wikitext += "^  Source Port  ^  Destination Port  ^^^^^^^^\n"
		wikitext += "|  %s  |  %s  ||||||||\n" % (sip, dip)
		wikitext += "^  Sequence Number  ^^^^^^^^^\n"
		wikitext += "|  %s  |||||||||\n" % (seqNum)
		wikitext += "^  Acknowledgement Number  ^^^^^^^^^\n"
		wikitext += "|  %s  |||||||||\n" % (ackNum)
		wikitext += "^  Data Offset  ^  Reserved  ^  URG  ^ ACK ^ PSH ^ RST ^ SYN ^ FIN ^ Window ^\n"
		wikitext += "|  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |\n" % (dataOffset, reserved, urg, ack, psh, rst, syn, fin, window)
		wikitext += "^  Checksum  ^^^^^^^^  Urgent Pointer  ^\n"
		wikitext += "|  %s  ||||||||  %s  |\n" % (checksum, urgentPointer)
		wikitext += "^  Options  ^^^^^^^^^\n"
		wikitext += "|  %s  |||||||||\n" % (options)
		wikitext += "^  Padding  ^^^^^^^^^\n"
		wikitext += "|  %s  |||||||||\n" % (padding)
		wikitext += "^  data  ^^^^^^^^^\n"
		wikitext += "|  %s  |||||||||\n" % (data)
		
		return wikitext
		
	def generateIpv4UdpHeaderWikiText(self, sip=lipsum_ip, dip=lipsum_ip, length=lipsum_num, checksum=lipsum_num, data=lipsum_short):
		"""Creates wikitext for IPv4 UDP header information."""
		
		wikitext = "=== IPv4 UDP Header ===\n"
		wikitext += "^  Source Port Number  ^  Destination Port  ^\n"
		wikitext += "|  %s  |  %s  |\n" % (sip, dip)
		wikitext += "^  Length  ^  Checksum  ^\n"
		wikitext += "|  %s  |  %s  |\n" % (length, checksum)
		wikitext += "^  data  ^^\n"
		wikitext += "|  %s  ||\n" % (data)
		
		return wikitext
		
	def generateL2tpHeaderWikiText(self, flagsAndVerInfo=lipsum_word, length=lipsum_num, tunnelId=lipsum_num, sessionId=lipsum_num, ns=lipsum_num, nr=lipsum_num, offsetSize=lipsum_num, offsetPad=lipsum_num, payloadData=lipsum_short):
		"""Creates wikitext for L2TP header information."""
		
		wikitext = "=== L2TP  ===\n"
		wikitext += "^  Flags and Version Info  ^  Length (opt)  ^\n"
		wikitext += "|  %s  |  %s  |\n" % (flagsAndVerInfo, length)
		wikitext += "^  Tunnel Id  ^  Session ID  ^\n"
		wikitext += "|  %s  |  %s  |\n" % (tunnelId, sessionId)
		wikitext += "^  Ns (opt)  ^  Nr (opt)  ^\n"
		wikitext += "|  %s  |  %s  |\n" % (ns, nr)
		wikitext += "^  Offset Size (opt)  ^  Offset Pad (opt)  ^\n"
		wikitext += "|  %s  |  %s  |\n" % (offsetSize, offsetPad)
		wikitext += "^  Payload data  ^^\n"
		wikitext += "|  %s  ||\n" % (payloadData)
		
		return wikitext
	
	# Wiki Methods
	def postAsPage(self, url, username, password, pagename, wikitext):
		"""Post wikitext to preset dokuwiki as page pagename."""
		
		try:
			wiki = DokuWikiClient(url, username, password)
			
			if wikitext in ["template:Intrusion Set Page", "template:Third Party Intelligence Page", "template:Exploit Page", "template:Implant Page", "template:Malicious Group Page", "template:Malicious Actor Page"]:
				wiki.put_page(pagename, wiki.page(wikitext))
			else:
				wiki.put_page(pagename, wikitext)
			
			print "Page [[%s]] posted" % pagename
		
		except Exception as e:
			print "Error: %s" % e
			
	

class Usage(Exception):
	def __init__(self, msg):
		self.msg = msg
	

# Client Code

def post_original_templates(self, arg):
	"""docstring for post_original_templates"""
	pass

def post_modified_templates(self, arg):
	"""docstring for post_modified_templates"""
	pass



help_message = '''
Sapho Templater is for automatically generating, populating, and posting Sapho wiki pages to a Dokuwiki implimentation. This takes a lot of the pain out of generating a new page.

Program Options:
\t-w, --wiki	wiki url: on localhost http://127.0.0.1/~mentat/dokuwiki
\t-u, --user	username: a user allowed to use xml-rpc interface
\t-p, --pass	password: password for the sapho user
\t-f			to file: will print template(s) to a file in the present working directory
\t-s			to screen: will print template(s) to the screen

Sapho:
\t--setup		Installs complete sapho wiki including sample pages and templates (requires wiki, username, password).
\t--template	Posts a single page based on a current template. Specify title as an argument "Alpha Alpha", then select a template. Use "-o" or "--original" to get original templates.
'''

def main(argv=None):
	
	if argv is None:
		argv = sys.argv
	try:
		try:
			opts, args = getopt.getopt(argv[1:], "hiw:u:p:vo", ["help", "wiki=", "user=", "pass=", "setup", "template=", "title=", "print=", "original"])
		except getopt.error, msg:
			raise Usage(msg)
		
		# option processing
		wiki_url = None
		username = None 
		password = None
		setup_to_wiki = False
		original = False
		page_title = ""
		wiki = SaphoTemplater()
		
		for option, value in opts:
			if option == "-v":
				verbose = True
			#if option == "-i":
				#interactive = True
			if option == "-f":
				to_file = True
			if option == "-s":
				to_screen = True
			if option in ("-h", "--help"):
				raise Usage(help_message)
			if option in ("-w", "--wiki"):
				wiki_url = value
			if option in ("-u", "--user"):
				username = value
			if option in ("-p", "--pass"):
				password = value
			if option in ("-o", "--original"):
				original = True
			if option in ("--setup"):
				setup_to_wiki = True
			if option in ("--template"):
				page_title = value
			
		if (wiki_url == False or username == False or password == False) and to_file == False:
			to_screen = True
		elif setup_to_wiki == True:
			wiki.initialSetup(wiki_url, username, password)
		elif page_title and original == True:
			print "Select an original template for page %s:" % value
			print "\t1) Intrusion Set Page"
			print "\t2) Third Party Intelligence Page"
			print "\t3) Exploit Page"
			print "\t4) Implant Page"
			print "\t5) Malicious Group Page"
			print "\t6) Malicious Actor Page"
			
			page_to_wiki = input("Template: ")
			
			if page_to_wiki == 1:
				wiki.postAsPage(wiki_url, username, password, "intrusionset:%s" % page_title, wiki.generateSetPage())
			elif page_to_wiki == 2:
				wiki.postAsPage(wiki_url, username, password, "thirdpartyintel:%s" % page_title, wiki.generateThirdPartyIntelligencePage())
			elif page_to_wiki == 3:
				wiki.postAsPage(wiki_url, username, password, "malcode_exploits:%s" % page_title, wiki.generateExploitPage())
			elif page_to_wiki == 4:
				wiki.postAsPage(wiki_url, username, password, "malcode_implants:%s" % page_title, wiki.generateImplantPage())
			elif page_to_wiki == 5:
				wiki.postAsPage(wiki_url, username, password, "actor:%s" % page_title, wiki.generateThreatGroupPage())
			elif page_to_wiki == 6:
				wiki.postAsPage(wiki_url, username, password, "actor:%s" % page_title, wiki.generateThreatActorPage())
			else:
				raise Usage("Invalid template selected")
		elif page_title and original == False:
			print "Select your template for page %s:" % value
			print "\t1) Intrusion Set Page"
			print "\t2) Third Party Intelligence Page"
			print "\t3) Exploit Page"
			print "\t4) Implant Page"
			print "\t5) Malicious Group Page"
			print "\t6) Malicious Actor Page" 
			
			page_to_wiki = input("Template: ")
			
			if page_to_wiki == 1:
				wiki.postAsPage(wiki_url, username, password, "intrusionset:%s" % page_title, "template:Intrusion Set Page")
			elif page_to_wiki == 2:
				wiki.postAsPage(wiki_url, username, password, "thirdpartyintel:%s" % page_title, "template:Third Party Intelligence Page")
			elif page_to_wiki == 3:
				wiki.postAsPage(wiki_url, username, password, "malcode_exploits:%s" % page_title, "template:Exploit Page")
			elif page_to_wiki == 4:
				wiki.postAsPage(wiki_url, username, password, "malcode_implants:%s" % page_title, "template:Implant Page")
			elif page_to_wiki == 5:
				wiki.postAsPage(wiki_url, username, password, "actor:%s" % page_title, "template:Malicious Group Page")
			elif page_to_wiki == 6:
				wiki.postAsPage(wiki_url, username, password, "actor:%s" % page_title, "template:Malicious Actor Page")
			
	except Usage, err:
		print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
		print >> sys.stderr, "\t for help use --help"
		return 2
	

if __name__ == "__main__":
	sys.exit(main())