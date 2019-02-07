import os;
import urllib.request;


def lineCount(logs):
	with open(logs) as x:
		for i, l in enumerate(x):
			pass
	return i+1

def checkForFile():
	url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
	if os.path.exists("./http_access_log.txt") == False:
		print("Downloading access logs from:", url)
		urllib.request.urlretrieve(url, "./http_access_log.txt")  

def isEntryValid(logs):
	validlog = '-'
	print("Stripping invalid or unreadable logfiles...")
	with open('http_access_log.txt') as rawlogs, open('validlogs.txt', 'w') as validlogs:
		for line in rawlogs:
			if not any(validlog in line for valid in validlog):
				pass
			else:
				validlogs.write(line)


def main():	
	checkForFile()
	print("Number of requests made:", lineCount("./http_access_log.txt"))
	isEntryValid("./http_access_log.txt")


main()

#usps case number ca141722721
# local      index.html
# remote - - [10/Oct/1995:08:57:04 -0600] "GET index.html HTTP/1.0" 200 6061
# remote - - [10/Oct/1995:08:57:06 -0600] "GET 3119.gif HTTP/1.0" 200 2048
# local - - [10/Oct/1995:08:57:19 -0600] "GET index.html HTTP/1.0" 200 3020