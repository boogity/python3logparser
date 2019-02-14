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
	jul = 0; aug = 0; sep = 0; oct94 = 0; oct95 = 0; nov = 0; dec = 0;
	janlogs=open("january1995logs.txt", "a+"); feblogs=open("february1995logs.txt", "a+"); marlogs=open("march1995logs.txt", "a+"); 
	aprlogs=open("april1995logs.txt", "a+"); maylogs=open("may1995logs.txt", "a+"); junlogs=open("june1995logs.txt", "a+");
	jullogs=open("july1995logs.txt", "a+"); auglogs=open("august1995logs.txt", "a+"); seplogs=open("september1995logs.txt", "a+");
	oct94logs=open("october1994logs.txt", "a+"); oct95logs=open("october1995logs.txt", "a+"); novlogs=open("november1995logs.txt", "a+"); declogs=open("december1995logs.txt", "a+");   

	with open("./http_access_log.txt") as logs:				
		for line in logs:								
			if re.search('(/Jan/)', line):
				jan+=1
				janlogs.write(line)
			if re.search('(/Feb/)', line):
				feb+=1
				feblogs.write(line)				
			if re.search('(/Mar/)', line):
				mar+=1
				marlogs.write(line)
			if re.search('(/Apr/)', line):
				apr+=1
				aprlogs.write(line)
			if re.search('(/May/)', line):
				may+=1
				maylogs.write(line)
			if re.search('(/Jun/)', line):
				jun+=1
				junlogs.write(line)
			if re.search('(/Jul/)', line):
				jul+=1
				jullogs.write(line)
			if re.search('(/Aug/)', line):
				aug+=1
				auglogs.write(line)
			if re.search('(/Sep/)', line):
				sep+=1
				seplogs.write(line)
			if re.search('(/Oct/1994)', line):
				oct94+=1
				oct94logs.write(line)
			if re.search('(/Oct/1995)', line):
				oct95+=1
				oct95logs.write(line)
			if re.search('(/Nov/)', line):
				nov+=1
				novlogs.write(line)
			if re.search('(/Dec/)', line):
				dec+=1
				declogs.write(line)

		print("Total responses in October, 1994: ", oct94)
		print("Total responses in November, 1994: ", nov)
		print("Total responses in December, 1994: ", dec)
		print("Total responses in January, 1995: ", jan)
		print("Total responses in February, 1995: ", feb)
		print("Total responses in March, 1995: ", mar)
		print("Total responses in April, 1995: ", apr)
		print("Total responses in May, 1995: ", may)
		print("Total responses in June, 1995: ", jun)
		print("Total responses in July, 1995: ", jul)
		print("Total responses in August, 1995: ", aug)
		print("Total responses in September, 1995: ", sep)
		print("Total responses in October, 1995", oct95)

def weeklyLogs():
	week1 = 0; week2 = 0; week3 = 0; week4 = 0;
	with open("./october1994logs.txt") as oct94logs:
		for line in oct94logs:
			if re.search('(?:[0][1-7]?\/)', line):
				week1+=1
	print("Number of requests made in the 1st week of October: ", week1)


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
	# checkForFile()
	# totalResponses = lineCount("http_access_log.txt")
	# print("Total number of requests made:", totalResponses)
	# monthlylogs()
	weeklyLogs()
	# redirectCodes(totalResponses)
	# clientErrors(totalResponses)
	# fileCount()

main()
