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
	else:
		print("what")

def main():	
	checkForFile()
	print("Number of requests made:", lineCount("./http_access_log.txt"))

main()