#!/usr/bin/python3
import urllib.request
import json

#oldurl = "https://www.bankofcanada.ca/valet/observations/group/FXUSDCAD/json?recent=5"

url = "https://www.bankofcanada.ca/valet/observations/FXCADUSD/json?recent=5"

#req = urllib.request.Request(url)

with urllib.request.urlopen(url) as resp:
	tmp = resp.read()
	#print(tmp)
	
a = json.loads(tmp)
obs = a['observations']
for item in obs:
	print(item['d'], ": ", item['FXCADUSD']['v'], sep="")

