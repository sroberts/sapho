#!/usr/bin/env python
# encoding: utf-8
"""
sapho:network_research.py

Created by Scott J. Roberts on 2012-01-10.
Copyright (c) 2012 TogaFoamParty Studios. All rights reserved.
"""

import sys
import getopt
from dokuwikixmlrpc import *

help_message = '''
The help message goes here.
'''

class SaphoNetworkResearch(object):
	
	def generate_ip_page(self, ip):
		"""docstring for generate_ip_page"""
		pass
	
	def generate_url_page(self, url):
		"""docstring for generate_url_page"""
		pass
	

class Usage(Exception):
	def __init__(self, msg):
		self.msg = msg


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
