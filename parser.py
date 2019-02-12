import os; import urllib.request; import re;
from collections import Counter
from time import sleep

def checkForFile():                                                 #check if file exists, else download
	url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
	if os.path.exists("./http_access_log.txt") == False:            
		print("Downloading access logs from:", url)
		urllib.request.urlretrieve(url, "./http_access_log.txt")  

def lineCount(logs):                                                #count lines for total number of requests, this includes corrupted log entries as they're still requests made / served
	with open(logs) as x:
		for i, l in enumerate(x):
			pass
	return i+1

def monthlylogs(): 
	jan = 0; feb = 0; mar = 0; apr = 0; may = 0; jun = 0; 			#counters for monthly logs
	jul = 0; aug = 0; sep = 0; octs = 0; nov = 0; dec = 0;
	with open("./http_access_log.txt") as logs:				
		for line in logs:								
			# if re.search('\W*(Jan)\W*', line):
			if re.search('(/Jan/)', line):
				jan+=1
			if re.search('(/Feb/)', line):
				feb+=1
			if re.search('(/Mar/)', line):
				mar+=1
			if re.search('(/Apr/)', line):
				apr+=1
			if re.search('(/May/)', line):
				may+=1
			if re.search('(/Jun/)', line):
				jun+=1
			if re.search('(/Jul/)', line):
				jul+=1
			if re.search('(/Aug/)', line):
				aug+=1
			if re.search('(/Sep/)', line):
				sep+=1
			if re.search('(/Oct/)', line):
				octs+=1
			if re.search('(/Nov/)', line):
				nov+=1
			if re.search('(/Dec/)', line):
				dec+=1
		print("Total responses in January: ", jan)
		print("Total responses in February: ", feb)
		print("Total responses in March: ", mar)
		print("Total responses in April: ", apr)
		print("Total responses in May: ", may)
		print("Total responses in June: ", jun)
		print("Total responses in July: ", jul)
		print("Total responses in August: ", aug)
		print("Total responses in September: ", sep)
		print("Total responses in October: ", octs)
		print("Total responses in November: ", nov)
		print("Total responses in December: ", dec)

def redirectCodes(totalResponses):							#counter for redirection 30x codes adds up then divides by total responses, including invalid or corrupt entries
	redirectCounter = 0.0
	with open("./http_access_log.txt") as logs:				
		for line in logs:
			if re.search('\s*(30\d)\s\S+', line):
				redirectCounter += 1
	print("Percentage of requests redirected elsewhere: {0:.2%}".format(redirectCounter/totalResponses))		
	
def clientErrors(totalResponses):							#counter for client error 4xx codes adds up then divides by total responses, including invalid or corrupt entries
	errorCounter = 0.0
	with open("./http_access_log.txt") as logs:				
		for line in logs:
			if re.search('\s*(4\d\d)\s\S+', line):
				errorCounter += 1
	print("Percentage of unsuccessful requests: {0:.2%}".format(errorCounter/totalResponses))		

def fileCount():
	filelog = []
	leastcommon = []
	with open("./http_access_log.txt") as logs:
		for line in logs:
			try:
				filelog.append(line[line.index("GET")+4:line.index("HTTP")])		#find all files sandwiched between GET requests and HTTP protocol"
			except:
				pass
	counter = Counter(filelog)
	for count in counter.most_common(1):														
		print("Most commonly requested file: {} with {} requests.".format(str(count[0]), str(count[1])))
	for count in counter.most_common():					#checking for file requests that only occur once as they must be the least requested
		if str(count[1]) == '1':
			leastcommon.append(count[0])
	if leastcommon:										#TODO find least common file as well, there are MANY file requests that only occur once in the string though. Print all? 													
		response = input("Looks like there were {} file(s) that were requested only once, show all? (y/n)".format(len(leastcommon)))
		if response == ('y' or 'Y'):
			for file in leastcommon:
				print(file)
	
def main(): 
	checkForFile()
	totalResponses = lineCount("http_access_log.txt")
	print("Total number of requests made:", totalResponses)
	monthlylogs()
	redirectCodes(totalResponses)
	clientErrors(totalResponses)
	fileCount()

main()
