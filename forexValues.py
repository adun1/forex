#!/usr/bin/python3
import urllib.request
import json
import matplotlib.pyplot as plt

#oldurl = "https://www.bankofcanada.ca/valet/observations/group/FXUSDCAD/json?recent=5"

def get_data(url):
	with urllib.request.urlopen(url) as resp:
		return json.loads(resp.read())

def parse_data(rawData, option):
	obs = []
	rawObs = rawData['observations']
	for item in rawObs:
		obs.append((item['d'], item['FXCADUSD']['v']))
	return obs
		
cadUsdUrl = "https://www.bankofcanada.ca/valet/observations/FXCADUSD/json?recent=5"
cadUsdObs = parse_data(get_data(cadUsdUrl), 'observations')
	
#reverse the observations pair 
dayList = [x[0] for x in reversed(cadUsdObs)]
currList = [x[1] for x in reversed(cadUsdObs)]
#overwrite currency value list with each item being coverted from str to float
currList = list(map(lambda x: float(x), currList))

plt.plot(dayList, currList)
plt.show()
plt.close()
