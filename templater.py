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

help_message = '''
Sapho Templater is for automatically generating, populating, and posting Sapho wiki pages to a Dokuwiki implimentation. This takes a lot of the pain out of generating a new page.
'''
# Filler text pulled from http://www.lipsum.com except date & url
lipsum = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
lipsum_short = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
lipsum_word = "Lorem ipsum"
lipsum_date = "19990101" #sample date in YYYYMMDD format
lipsum_url = "http://www.example.com"
	
# Wiki Classes
class WikiTemplater(object):
	doku_username = "sapho"
	doku_password = "sapho_password"
	
	# Major Page Types
	def generateSetPage(self, summary=lipsum, compromise=lipsum, persistence=lipsum, siem_content=[lipsum_short, lipsum_short], ids_rules=[lipsum_short, lipsum_short], tickets=[lipsum_short, lipsum_short]):
		wikitext = "====== Summary ======\n"
		wikitext += "%s\n" % summary
		
		wikitext += "====== Compromise Vector & Persistence ======\n"
		wikitext += "==== Compromise Vector ====\n"
		wikitext += "%s\n" % compromise
		
		wikitext += "===== Persistence =====\n"
		wikitext += "%s\n" % persistence
		
		wikitext += "====== Detection =====\n"
		wikitext += "==== SIEM Content ====\n"
		for siem_rule in siem_content:
			wikitext += "  * %s\n" % siem_rule
		
		wikitext += "==== IDS Content ====\n"
		for ids_rule in ids_rules:
			wikitext += "  * %s" % ids_rule
		
		wikitext += "==== Open Tickets ====\n"
		for ticket in tickets:
			wikitext += "  * %s" % ticket
		
		wikitext += "===== Indicators =====\n"
		wikitext += "==== Known Compromised Hosts ====\n"
		wikitext += "^ IP Address ^ Host Name ^ User Name ^ Title ^ Department ^ Notes ^\n"
		wikitext += "|			  |			  |			  |		  |			   |	   |\n"
		
		wikitext += "==== Known Compromised Accounts ====\n"
		wikitext += "^ Username ^ User ^ Notes ^\n"
		wikitext += "|		 	|	   |	   |\n"
		
		wikitext += "==== IP Indicators ====\n"
		wikitext += "^ IP Address ^ Location ^ URL ^ Research ^ Notes ^\n"
		wikitext += "|			  |			 |	   |		  |	   	  |\n"
		
		wikitext += "==== URL Indicators ====\n"
		wikitext += "^ URL ^ Associated IP Addresses ^ Location ^ Research ^ Notes ^\n"
		wikitext += "|	   |						 |			|		   |	   |\n"
		
		wikitext += "==== Known Attacker Ports ====\n"
		wikitext += "^ Port ^ Type ^ Service ^ Notes ^\n"
		wikitext += "|		|	   |		 |		 |\n"
		
		wikitext += "==== Bad User Agent Strings ====\n"
		wikitext += "^ UserAgent String ^ Notes ^\n"
		wikitext += "|					|		|\n"
		
		wikitext += "==== Known Malicious Files ====\n"
		wikitext += "^ Filename ^ Type ^ Size ^ MD5 ^ SSDeep ^ File ^ Report ^ Notes ^\n"
		wikitext += "|			|	   |	  |	 	|		 |	  	|		 |	   	 |\n"
		
		return wikitext
	
	def generateWikiStartTemplate(self):
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
		wikitext += "	* AA: [[malcode:Alpha.implant]]\n"
		wikitext += "  * Bravo\n"
		wikitext += "	* BA: [[malcode:Bravo.implant]]\n"
		wikitext += "===== Utilities =====\n"
		wikitext += "  * [[malcode:Alpha.util]] - Alpha.util summary.\n"
		
		wikitext += "====== Known Threat Actors ======\n"
		wikitext += "===== Known Threat Groups =====\n"
		wikitext += "  * [[actor:Actor Alpha]]\n"
		wikitext += "  * [[actor:Actor Bravo]]\n"
		wikitext += "===== Known Threat Actors =====\n"
		wikitext += "  * [[actor:Person Alpha]]\n"
		wikitext += "  * [[actor:Person Bravo]]\n"
		
		wikitext += "====== Templates ======\n"
		wikitext += "  * [[template:Set Page Template]]\n"
		wikitext += "  * [[template:Compromise Page Template]]\n"
		wikitext += "  * [[template:Attacker Tool Page Template]]\n"
		
		return wikitext
	
	def generateThirdPartyIntelligencePage(self, filename="example.file", tipDate=datetime.date.today(), analystName=lipsum_word, data=lipsum, indicators = [lipsum_word, lipsum_word]):
		"""Generates a page for adding any Third Party intelligence products to the wiki. May require some manipulation to add into wiki format."""
		wikitext = "====== Metadata ======"
		wikitext += "^ File | %s\n" % (filename)
		wikitext += "^ Date | %s\n" % (tipdate)
		wikitext += "^ Analyst | %s\n" % (analystName)
		
		wikitext += "====== Data ======\n"
		wikitext += "%s\n" % (data)
		
		wikitext += "====== Indicators ======\n"
		for indicator in indicators:
			wikitext += "  * %s\n" % (indicator)
		
		wikitext += "File: FIXME Add files her with upload dialog.\n" 
		
		return wikitext	
	
	def generateExploitPage(self, exploit_name=lipsum_word, date_exploit_identified=lipsum_date, date_exploit_public=lipsum_date, date_exploit_updated=lipsum_date, author=lipsum_word, actor=[[Alpha]], vuln_app=lipsum_word, vuln_mod=lipsum_word, vuln_ver="1.0", vuln_patch="N/A", mitigation=lipsum, edb=0000, cve="CVE-0000-0000", osvdb=0000, exploit_sources[lipsum_url,lipsum_url], notes=lipsum):
		wikitext = "Name: %s" % exploit_name
		
		wikitext += "===== Timeline ====="
		wikitext += "^ Exploit Identified | %s" % date_exploit_identified
		wikitext += "^ Public Exploit Published | %s" % date_exploit_public
		wikitext += "^ Exploit Updated | %s" % date_exploit_updated
		
		wikitext += "===== Developer ====="
		wikitext += "Author: %s" % author
		wikitext += "Actor: %s" % actor
		
		wikitext += "===== Vulnerable Systesm ====="
		wikitext += "^ Vulnerable Application | %s" % vuln_app
		wikitext += "^ Vulnerable Module | %s" % vuln_mod
		wikitext += "^ Vulnerable Versions | %s" % vuln_ver
		wikitext += "^ Vulnerable Languages | %s" % vuln_lang
		wikitext += "^ Patch | %s" % str(vuln_patch)
		
		wikitext += "===== Mitigation ====="
		wikitext += "%s" % mitigation
		
		wikitext += "===== Files ====="
		wikitext += "^ Delivery Code | FIXME Add files with upload dialog. |" 
		wikitext += "^ Exploit Code | FIXME Add files with upload dialog. |"
		
		wikitext += "===== References ====="
		wikitext += "ExploitDB-ID: %s" % str(edb)
		wikitext += "CVE: %s" % cve
		wikitext += "OSVDB-ID: %s" % str(osvdb)
		
		wikitext += "=== Exploit Sources ==="
		for exploit_source in exploit sources:
			wikitext += "  * <nowiki>%s</nowiki>" % exploit_source 
			
		wikitext += "===== Notes ====="
		wikitext += "%s" % notes
		
		return wikitext
	
	def generateImplantsPage(self, intrusionSet="Alpha Alpha", filename="Example.file", filetype="example", fileSize=0000, md5sum="d41d8cd98f00b204e9800998ecf8427e", sha="da39a3ee5e6b4b0d3255bfef95601890afd80709", ssdeep="3::", analystName=lipsum_word, summary=lipsum, avDefs = {"Symantec": "none", "McAfee":"none"}, filehooking=[lipsum_short, lipsum_short], persistence=[lipsum_short, lipsum_short], spreading_mechs=[lipsum_short, lipsum_short], exfil_mechs=[lipsum_short, lipsum_short], c2_mechs=[lipsum_short, lipsum_short], oss=[lipsum_short, lipsum_short], requiredfiles=[lipsum_short, lipsum_short], secondstages=[lipsum_short, lipsum_short], regkeys=[lipsum_short, lipsum_short], behav_summary=lipsum, logs=[lipsum_short, lipsum_short], strings=[lipsum_short, lipsum_short], other=[lipsum_short, lipsum_short], network_indicators=[lipsum_short, lipsum_short], fs_indicators=[lipsum_short, lipsum_short], mitigation_steps=[lipsum_short, lipsum_short], eradication_steps=[lipsum_short, lipsum_short]):
		"""docstring for generateImplantsPage"""
		
		wikitext = "**Implant Report:** //%s/////%s// (//%s//)" % (intrusionSet, filename, md5sum)
		
		wikitext += "**Reverse Engineer:** %s" % (analystName)
		
		wikitext += "**Date:** %s" % (date)
		
		wikitext += "**Associated FO Set:** %s" % (intrusionSet)
		
		wikitext += "===== Summary of the Analysis: ====="
		wikitext += "%s" % (summary)
		
		wikitext += "===== Identification ====="
		wikitext += "^ File Name | %s |" % (filename)
		wikitext += "^ File Type | %s |" % (filetype)
		wikitext += "^ File Size | %s |" % (str(filesize))
		wikitext += "^ MD5	   | %s |" % (md5)
		wikitext += "^ SHA	   | %s |" % (sha)
		wikitext += "^ Ssdeep	| %s |" % (ssdeep) 
		
		wikitext += "====Current anti-virus detection capabilities:===="
		for vendor in avDefs:
			wikitext += "^ %s | %s |" % (vendor, avDefs[vendor])
			
		wikitext += "===== Characteristics ====="
		wikitext += "==== File Hooking ===="
		for filehook in filehooking:
			wikitext += "  * %s" % (filehook)
			
		wikitext += "==== Persistence Mechanisms ===="
		for persistance_mech in persistence:
			wikitext += "  * %s" % (persistance_mech)
			
		wikitext += "==== Spreading Mechanisms ===="
		for spreading_mech in spreading_mechs:
			wikitext += "  * %s" % (spreading_mech)
			
		wikitext += "==== Exfiltration Mechanisms ===="
		for exfil_mech in exfil_mechs:
			wikitext += "  * %s" % (exfil_mech)
			
		wikitext += "==== Command and Control Mechanisms ===="
		for c2_mech in c2mechs:
			wikitext += "  * %s " % (c2_mech)
			
		wikitext += "===== Dependencies ====="
		wikitext += "==== Supported Operating Systems ===="
		for os in oss:
			wikitext += "  * %s " % (os)
			
		wikitext += "==== Required Files ===="
		for requiredfile in requiredfiles:
			wikitext += "  * %s " % (requiredfile)
			
		wikitext += "==== Second Stage Downloads ===="
		for secondstage in secondstages:
			wikitext += "  * %s " % (secondstage)
			
		wikitext += "==== Registry Keys ===="
		for regkey in regkeys:
			wikitext += "  * %s " % (regkeys)
			
		wikitext += "===== Behavioral and code analysis findings ====="
		wikitext += "//%s//" % (behav_summary)
		
		wikitext += "===== Supporting Figures ====="
		wikitext += "==== Logs ===="
		for log in logs:
			wikitext += "  * %s" % (log)
			
		wikitext += "==== Interesting Strings ===="
		for string in strings:
			wikitext += "  * %s" % (string)
			
		wikitext += "==== Other Relevant Files or Data ===="
		for oth in other:
			wikitext += "  * %s" % (oth)
			
		wikitext += "===== Incident Recommendations ====="
		wikitext += "==== Network Indicators ===="
		for network_indicator in network_indicators:
			wikitext += "  * %s" % (network_indicator)
			
		wikitext += "==== File System Indicators ===="
		for fs_indicator in fs_indicators:
			wikitext += "  * %s" % (fs_indicator)
			
		wikitext += "==== Mitigation Steps ===="
		for mitigation_step in mitigation_steps:
			wikitext += "  * %s" % (mitigation_step)
			
		wikitext += "==== Eradication Steps ===="
		for eradication_step in eradication_steps:
			wikitext += "  * %s" % (eradication_step)
		
		return wikitext
	
	
	def generateThreatGroupPage(self, group_name="Alpha", group_summary=lipsum, group_presence=[lipsum_url, lipsum_url], group_type="Unknown", membership=[lipsum_word, lipsum_word], pre_ex_methods=[lipsum_word, lipsum_word], pre_ex_tools=[lipsum_word, lipsum_word], ex_methods=[lipsum_word, lipsum_word], ex_tools=[lipsum_word, lipsum_word], post_ex_methods=[lipsum_word, lipsum_word], post_ex_tools=[lipsum_word, lipsum_word], periods_of_operation=[[lipsum_date, lipsum_date], [lipsum_date, lipsum_date]]):
		"""Generates Dokuwiki page for profiling a malicious group including key methodologies and tools."""
		wikitext = "===== Group: % =====\n" % group_name
		wikitext += "^ Summary | %s |\n" % group_summary
		
		sites = ""
		for site in group_presence:
			site += "%s, " % site
			
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
			wikitext += "  * period_of_operation[0] - period_of_operation[1]\n"
			
		return wikitext
	
	def generateThreatActorPage(self, actor_identifier=lipsum_word, date_audited="01/01/2000", given_name=lipsum_word, date_of_birth="01/01/2001", country_of_birth=lipsum_word, location=lipsum_word age="00", names_aliases = [lipsum_word, lipsum_word, lipsum_word], email_addresses = [lipsum_word, lipsum_word, lipsum_word], social_media_sites = ["twitter", "facebook", "linkedin"]):
		"""Allows programatic generation of a page of a thrat actor. If no factors are given this generates a template page with dummy values."""
		wikitext = "====== %s ======" % actor_identifier
		wikitext += "^ Date Audited	 | %s |" % date_audited
		wikitext += "^ Name			 | %s |" % given_name
		wikitext += "^ DOB			  | %s |" % date_of_birth
		wikitext += "^ Country of Birth | %s |" % country_of_birth
		wikitext += "^ Location		 | %s |" % location
		wikitext += "^ Age			  | %s |" % age
		
		wikitext += "===== Names/Aliases ====="
		for name_alias in names_aliases:
			wikitext += "  * %s" % name_alias
		
		wikitext += "===== Email Addresses ====="
		for email_address in email_addresses:
			wikitext += "  * %s" % email_address
		
		wikitext += "===== Social Media Sites ====="
		"""Ideally would be formatted as tables. First version will be formatted as bullets."""
		wikitext += "^ IM Names | %s |" % date_audited
		wikitext += "^ Site/group Affiliation | %s |" % date_audited
		wikitext += "^ URLs | %s |" % date_audited
		wikitext += "^ Domain Data | %s |" % date_audited
		wikitext += "===== Screen Shots ====="
		wikitext += "===== Tools Used =====" 
		wikitext += "^ Google Searches and Links | %s |" % date_audited
		
		return wikitext
	
	# Common Elements Generators
	def generateNewsArticle(self, title=lipsum_short, author=lipsum_word, date="20000101", url="hxxp://www.example.com/article", article_body=lipsum):
		wikitext = "==== %s ====\n" % title
		wikitext += "^ Author | %s |\n" % author
		wikitext += "^ Date   | %s |\n" % date
		wikitext += "^ URL    | %s |\n" % url
		
		for line in article_body.split("\n"):
			wikitext += "> %s\n" % line
		
		return wikitext
	
	# Wiki Methods
	def postAsPage(self, pagename, wikitext):
		"""docstring for postAsPage"""
		pass

# Client Code
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