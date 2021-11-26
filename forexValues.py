#!/usr/bin/python3
import urllib.request
import json
import matplotlib.pyplot as plt

def get_data(url):
	with urllib.request.urlopen(url) as resp:
		return json.loads(resp.read())

def parse_data(rawData, option, exName):
	obs = []
	rawObs = rawData[option]
	for item in rawObs:
		obs.append((item['d'], item[exName]['v']))
	return obs
	
def plot_data(xaxis, yaxis, exName):
	plt.xlabel('Date')
	plt.ylabel('Value')
	plt.title(exName[2:] + ' Foreign Exchange Value')
	plt.plot(xaxis, yaxis)
	plt.show()
	plt.close()

# might use less resources if all items are not stored in future (eg once done with CADUSD overwrite)
#		idea give user the option of combining different plots in same chart (use legend)
currencyList = ['FXCADUSD', 'FXCADEUR', 'FXCADGBP']
numObs = 5 #number of observations
observations = {}

for item in currencyList:
	tmpUrl = "https://www.bankofcanada.ca/valet/observations/" + item + "/json?recent=" + str(numObs)
	#parse_data assumes observations is in the format of a list of tuples each item is (dayi, valuei)
	observations[item] = parse_data(get_data(tmpUrl), 'observations', item)
	#reverse the observations pair 
	dayList = [x[0] for x in reversed(observations[item])]
	currList = [x[1] for x in reversed(observations[item])]
	#overwrite currency value list with each item being coverted from str to float
	currList = list(map(lambda x: float(x), currList))
	plot_data(dayList, currList, item)
