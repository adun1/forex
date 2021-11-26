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
	rawObs = rawData[option]
	for item in rawObs:
		obs.append((item['d'], item['FXCADUSD']['v']))
	return obs
	
def plot_data(xaxis, yaxis):
	plt.plot(xaxis, yaxis)
	plt.show()
	plt.close()

# might use less resources if all items are not stored in future (eg once done with CADUSD overwrite)
urlItems = {"cadUsd": "https://www.bankofcanada.ca/valet/observations/FXCADUSD/json?recent=5"}

#parse_data assumes observations is in the format of a list of tuples each item is (dayi, valuei)
observations = {}
observations['cadUsd'] = parse_data(get_data(urlItems['cadUsd']), 'observations')

#reverse the observations pair 
dayList = [x[0] for x in reversed(observations['cadUsd'])]
currList = [x[1] for x in reversed(observations['cadUsd'])]

#overwrite currency value list with each item being coverted from str to float
currList = list(map(lambda x: float(x), currList))
plot_data(dayList, currList)
