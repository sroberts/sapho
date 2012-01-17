lipsum = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
lipsum_short = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
lipsum_word = "Lorem ipsum"
lipsum_date = "19990101" #sample date in YYYYMMDD format
lipsum_datetime = "19990101 12:00:00" #sample date in YYYYMMDD HH:MM:SS format
lipsum_url = "http://www.example.com"
lipsum_email = "sample@example.com"
lipsum_ip = "192.168.1.1"

class foo:
	def generateIpHeaderWikiText(self, version=lipsum_word, ihl=lipsum_word, typeOfService="0000", totalLength="0000", identification="0000", flags=lipsum_word, fragmentOffset="0000", ttl="36000", protocol="1", headerChecksum=lipsum_word, sip=lipsum_ip, dip=lipsum_ip, options=lipsum_word, padding="0000"):
		"""docstring for generateIpHeaderWikiText"""
	
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

	def generateIcmpHeaderWikiText(self, icmpType, icmpCode, checksum, restOfHeader):
		"""docstring for generateIcmpHeaderWikiText"""
	
		wikitext = "=== ICMP Header ===\n"
		wikitext += "^  Type  ^  Code  ^  Checksum  ^\n"
		wikitext += "|  %s  |  %s  |  %s  |\n" % (icmpType, icmpCode, checksum)
		wikitext += "^  Rest of Header  ^^^\n"
		wikitext += "|  %s  |||\n" % (restOfHeader)
	
		return wikitext

	def generateIpv4TcpHeaderWikiText(self, sip, dip, seqNum, ackNum, dataOffset, reserved, urg, ack, psh, rst, syn, fin, window, checksum, urgentPointer, options, padding, data):
		"""docstring for generateIpv4HeaderWikiText"""
	
		wikitext = "=== IPv4 TCP Header ===\n"
		wikitext += "^  Source Port  ^  Destination Port  ^^^^^^^^\n"
		wikitext += "|  %s  |  %s  ||||||||\n" % (sip, dip)
		wikitext += "^  Sequence Number  ^^^^^^^^^\n"
		wikitext += "|  %s  |||||||||\n" % (seqNum)
		wikitext += "^  Acknowledgement Number  ^^^^^^^^^\n"
		wikitext += "|  %s  |||||||||\n" % (ackNum)
		wikitext += "^  Data Offset  ^  Reserved  ^  URG  ^ ACK ^ PSH ^ RST ^ SYN ^ FIN ^ Window ^\n"
		wikitext += "|  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |\n" % (dataOffset, reserved, urg, ack, psh, rst, syn, fin, window)
		wikitext += "^  Checksum  ^^^^^^^^  Urgent Pointer  ^"
		wikitext += "|  %s  ||||||||  %s  |\n" % (checksum, urgentPointer)
		wikitext += "^  Options  ^^^^^^^^^\n"
		wikitext += "|  %s  |||||||||\n" % (options)
		wikitext += "^  Padding  ^^^^^^^^^\n"
		wikitext += "|  %s  |||||||||\n" % (padding)
		wikitext += "^  data  ^^^^^^^^^\n"
		wikitext += "|  %s  |||||||||\n" % (data)
	
		return wikitext

	def generateIpv4UdpHeaderWikiText(self, sip, dip, length, checksum, data):
		"""docstring for generateIpv4UdpHeaderWikiText"""
		
		wikitext = "=== IPv4 UDP Header ===\n"
		wikitext += "^  Source Port Number  ^  Destination Port  ^\n"
		wikitext += "|  %s  |  %s  |\n" % (sip, dip)
		wikitext += "^  Length  ^  Checksum  ^\n"
		wikitext += "|  %s  |  %s  |\n" % (length, checksum)
		wikitext += "^  data  ^^\n"
		wikitext += "|  %s  ||\n" % (data)
	
		return wikitext

	def generateL2tpHeaderWikiText(self, flagsAndVerInfo, length, tunnelId, sessionId, ns, nr, offsetSize, offsetPad, payloadData):
		"""docstring for generateL2tpHeaderWikiText"""
		
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
bar = foo()
print bar.generateIpHeaderWikiText()
print bar.generateIcmpHeaderWikiText()
print bar.generateIpv4TcpHeaderWikiText()	
print bar.generateIpv4UdpHeaderWikiText()
print bar.generateL2tpHeaderWikiText()