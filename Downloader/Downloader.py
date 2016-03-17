#!/usr/bin/python

import requests
import re
import os.path
import sys

if len(sys.argv) > 1:
	work = sys.argv[1]
else:
	work = "toDownload.txt"

dirname = os.path.dirname(work)
if len(dirname) > 0:
	dirname += "/"
fo = open(work, "r")
for line in fo:
	print "url: %s" % (line)
	fl = requests.get(line, stream=True)
	filename = firstplace = dirname + re.findall("filename=\"(\S+)\"", fl.headers['Content-Disposition'])[0]
	i = 0
	while os.path.isfile(filename):
		i += 1
		filename = firstplace[:firstplace.rfind('.')] + " (" + str(i) + ")" + firstplace[firstplace.rfind('.'):]
	print "in file: %s" % (filename)
	with open (filename, "wb") as Output:
	  for chunk in fl.iter_content(chunk_size=1024):
		if chunk:
		  Output.write(chunk)
fo.close()
