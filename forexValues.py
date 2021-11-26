#!/usr/bin/python3
import urllib.request
import json
import matplotlib.pyplot as plt
import sys

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
	plt.title(exName + ' Foreign Exchange Value')
	plt.plot(xaxis, yaxis)
	plt.show()
	plt.close()

if len(sys.argv) < 2:
	print("specify num observations (if a second argument is passed direct quotations will be used)")
	exit()

# might use less resources if all items are not stored in future (eg once done with CADUSD overwrite)
#		idea give user the option of combining different plots in same chart (use legend and new branch)
baseURL = "https://www.bankofcanada.ca/valet/observations/"
baseCurr = 'CAD'
currencyList = ['USD', 'EUR', 'GBP']
numObs = int(sys.argv[1]) #number of observations
observations = {}

for item in currencyList:
	#format URL depending on whether the indirect or direct ex rate is desired
	tmpName = ''
	if len(sys.argv) > 2:
		tmpName = 'FX' + item + baseCurr
	else:
		tmpName = 'FX' + baseCurr + item
	tmpUrl = baseURL + tmpName + "/json?recent=" + str(numObs)
	#parse_data assumes observations is in the format of a list of tuples each item is (dayi, valuei)
	observations[tmpName] = parse_data(get_data(tmpUrl), 'observations', tmpName)
	#reverse the observations pair 
	dayList = [x[0] for x in reversed(observations[tmpName])]
	currList = [x[1] for x in reversed(observations[tmpName])]
	#overwrite currency value list with each item being coverted from str to float
	currList = list(map(lambda x: float(x), currList))
	plot_data(dayList, currList, baseCurr+item)
