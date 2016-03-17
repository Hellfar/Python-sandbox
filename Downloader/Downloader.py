#!/usr/bin/python

import requests
import re
import os.path

work = "toDownload.txt"
fo = open(work, "r")
for line in fo:
	print "url: %s" % (line)
	fl = requests.get(line, stream=True)
	filename = os.path.dirname(work) + re.findall("filename=\"(\S+)\"", fl.headers['Content-Disposition'])[0]
	os.path.isfile(filename)
	with open (filename, "wb") as Output:
	  for chunk in fl.iter_content(chunk_size=1024):
		if chunk:
		  Output.write(chunk)
fo.close()
