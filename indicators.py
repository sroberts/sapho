#!/usr/bin/env python
# encoding: utf-8
"""
indicators.py

Created by Scott J. Roberts on 2012-01-04.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os

# Indicator Classes
class Indicator_ArpEntryItem(object):
	"""Based on Mandiant's OpenIOC XML specification. Address Resolution Protocol (ARP) is a telecommunications protocol used for resolution of network layer addresses into link layer addresses, a critical function in multiple-access networks. (Wikipedia: http://en.wikipedia.org/wiki/Address_Resolution_Protocol)."""
	
	physicalAddress = lipsum_word
	iPv4Address = "127.0.0.1"
	iPv6Address = "::1"
	interface = lipsum_word
	interfaceType = lipsum_word
	state = lipsum_word
	cache = lipsum_word
	isRouter = False
	lastReachable = "01/01/2001 00:00:00"
	lastUnreachable = "01/01/2001 00:00:00"
	
	def __init__(self, arg):
		super(Indicator_ArpEntryItem, self).__init__()
		self.arg = arg

    def generateWikiTableHeader(self):
        """docstring for generateWikiTableHeader"""
        wikitext = "^ Physical Address ^ IPV4 Address ^ IPV6 Address ^ Interface ^ Interface Type ^ State ^ Cache ^ Router ^ Last Reachable ^ Last Unreachable ^ "
        return wikitext

    def generateWikiTableRow(self, physicalAddress = lipsum_word, iPv4Address = "127.0.0.1", iPv6Address = "::1", interface = lipsum_word, interfaceType = lipsum_word, state = lipsum_word, cache = lipsum_word, isRouter = False, lastReachable = "01/01/2001 00:00:00", lastUnreachable = "01/01/2001 00:00:00"):
        """docstring for generateWikiTableHeader"""
        wikitext = "| %s               | %s           | %s           | %s        | %s             | %s    | %s    | %s     | %s             | %s               | " % (physicalAddress, iPv4Address, iPv6Address, interface, interfaceType, state, cache, str(isRouter), lastReachable, lastUnreachable)    
        return wikitext
    
    def generateDefaultWikiTemplate(self):
        """docstring for generateWikiTemplate"""
        wikitext = ""
        wikitext += generateWikiTableHeader()
        wikitext += generateWikiTableRow()
        
        return wikitext

class Indicator_DnsEntryItem(object:
    """Based on Mandiant's OpenIOC XML specification. The Domain Name System (DNS) is a hierarchical distributed naming system for computers, services, or any resource connected to the Internet or a private network. It associates various information with domain names assigned to each of the participating entities. Most importantly, it translates domain names meaningful to humans into the numerical identifiers associated with networking equipment for the purpose of locating and addressing these devices worldwide. (Wikipedia: http://en.wikipedia.org/wiki/Domain_Name_System)."""
                             
	RecordName = lipsum
	RecordType = lipsum
	TimeToLive = "01/01/2001 00:00:00"
	Flags = lipsum
	Host = lipsum
	IPv4Address = lipsum
    IPv6Address = lipsum
	PrimaryServerName = lipsum
	AdministratorName = lipsum
	Refresh = "01/01/2001 00:00:00"
	Retry = "01/01/2001 00:00:00"
	Expire = "01/01/2001 00:00:00"
	DefaultTimeToLive = "01/01/2001 00:00:00"
	MailboxName = lipsum
	MailboxErrorsName = lipsum
	MxHost = lipsum
	Bitmask = lipsum
	OriginalTimeToLive = "01/01/2001 00:00:00"
	ExpirationDate = "01/01/2001 00:00:00"
	DateSigned = "01/01/2001 00:00:00"
	CreationDate = "01/01/2001 00:00:00"
	LookupTimeout = "01/01/2001 00:00:00"
	CacheTimeout = "01/01/2001 00:00:00"

def main():
	pass


if __name__ == '__main__':
	main()

