#!/usr/bin/python

import sys
import operator

t = [None]

if len(sys.argv) > 1:
	(p, s) = sys.argv
else:
	sys.exit(Exception("usage: " + sys.argv[0] + " STRING"))

dico = dict((k, s[k]) for k in range(len(s)))
# print(dico)
d = sorted(dico.items(), key=operator.itemgetter(1))
d.insert(0, (len(s), None))
# print(d)
t = []
for k, v in d:
	if k == 0:
		t.append(None)
	else:
		t.append(s[k - 1])
# print(t)

# print with $ when of None
output = ""
for item in t:
	if item == None:
		output += '$'
	else:
		output += item
print(output)
