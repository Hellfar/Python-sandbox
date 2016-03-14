#!/usr/bin/python

import requests
import re

fo = open("toDownload.txt", "r")
for line in fo:
	print "url: %s" % (line)
	fl = requests.get(line, stream=True)
	filename = re.findall("filename=\"(\S+)\"", fl.headers['Content-Disposition'])[0]
	with open (filename, "wb") as Output:
	  for chunk in fl.iter_content(chunk_size=1024):
		if chunk:
		  Output.write(chunk)
fo.close()
