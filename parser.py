import os;
import urllib.request;


def checkForFile():
	url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
	if os.path.exists("./http_access_log.txt") == False:
		print("Downloading access logs from:", url)
		urllib.request.urlretrieve(url, "./http_access_log.txt")  
	else:
		print("what")

checkForFile()
