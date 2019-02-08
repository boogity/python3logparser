import os; import urllib.request; import re;
from collections import Counter
from time import sleep

regex = '([(\w+)]+) - - \[(.*?)\] "(.*?)" (\d+) (\d+)'				#breaks log into groupings of origin, date&time, command file protocol, code, size 


def lineCount(logs):                                                #count lines for total number of requests, keep corrupt entries as they're still requests
	with open(logs) as x:
		for i, l in enumerate(x):
			pass
	return i+1

def checkForFile():                                                 #check if file exists, else download
	url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
	if os.path.exists("./http_access_log.txt") == False:            
		print("Downloading access logs from:", url)
		urllib.request.urlretrieve(url, "./http_access_log.txt")  

def isEntryValid(logs):                                             #corrupt entries lack hyphens, check for and remove corrupt log entries
	validlog = '-'
	invalid = 0
	print("Stripping invalid or unreadable logfiles...")
	with open('http_access_log.txt') as rawlogs, open('validlogs.txt', 'w') as validlogs:
		for line in rawlogs:
			if not any(validlog in line for valid in validlog):
				pass
				invalid += 1
			else:
				validlogs.write(line)
	sleep(1)
	print("Removed %d unreadable logfiles" % invalid)
	return invalid


def successCodes(logs, loglength):
	with open(logs) as validlogs:				
		i = 0
		array = []
		successcodes = 0
		for line in validlogs:								#creating array of each log line
			array.append(line)

	while (i < loglength):								#iterate through strings in array for regex
		line = re.match(regex, array[i]).groups()
		if(line[3].startswith("3")):
			successcodes+=1
		i+=1
	print("Number of successcodes: ", successcodes)


def failCodes(logs):
	pass


def main(): 
	checkForFile()
	totalResponses = lineCount("http_access_log.txt")
	print("Number of requests made:", totalResponses)
	totalErrorResponses = isEntryValid("http_access_log.txt")
	totalValidResponses = totalResponses - totalErrorResponses
	successCodes("validlogs.txt", totalValidResponses)

main()

#usps case number ca141722721
# local      index.html
# remote - - [10/Oct/1995:08:57:04 -0600] "GET index.html HTTP/1.0" 200 6061
# remote - - [10/Oct/1995:08:57:06 -0600] "GET 3119.gif HTTP/1.0" 200 2048
# local - - [10/Oct/1995:08:57:19 -0600] "GET index.html HTTP/1.0" 200 3020