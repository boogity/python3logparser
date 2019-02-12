import os; import urllib.request; import re;
from collections import Counter
from time import sleep

def checkForFile():                                                 #check if file exists, else download
	url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
	if os.path.exists("./http_access_log.txt") == False:            
		print("Downloading access logs from:", url)
		urllib.request.urlretrieve(url, "./http_access_log.txt")  

def lineCount(logs):                                                #count lines for total number of requests
	with open(logs) as x:
		for i, l in enumerate(x):
			pass
	return i+1

def monthlylogs(): 
	jan = 0; feb = 0; mar = 0; apr = 0; may = 0; jun = 0; 
	jul = 0; aug = 0; sep = 0; octs = 0; nov = 0; dec = 0;
	with open("./http_access_log.txt") as logs:				
		for line in logs:								
			if re.search('\W*(Jan)\W*', line):
				jan+=1
			if re.search('\W*(Feb)\W*', line):
				feb+=1
			if re.search('\W*(Mar)\W*', line):
				mar+=1
			if re.search('\W*(Apr)\W*', line):
				apr+=1
			if re.search('\W*(May)\W*', line):
				may+=1
			if re.search('\W*(Jun)\W*', line):
				jun+=1
			if re.search('\W*(Jul)\W*', line):
				jul+=1
			if re.search('\W*(Aug)\W*', line):
				aug+=1
			if re.search('\W*(Sep)\W*', line):
				sep+=1
			if re.search('\W*(Oct)\W*', line):
				octs+=1
			if re.search('\W*(Nov)\W*', line):
				nov+=1
			if re.search('\W*(Dec)\W*', line):
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

def redirectCodes(totalResponses):
	redirectCounter = 0.0
	with open("./http_access_log.txt") as logs:				
		for line in logs:
			if re.search('\s*(30\d)\s\S+', line):
				redirectCounter += 1
	print("Percentage of requests redirected elsewhere: {0:.2%}".format(redirectCounter/totalResponses))		
	
def clientErrors(totalResponses):
	errorCounter = 0.0
	with open("./http_access_log.txt") as logs:				
		for line in logs:
			if re.search('\s*(4\d\d)\s\S+', line):
				errorCounter += 1
	print("Percentage of unsuccessful requests: {0:.2%}".format(errorCounter/totalResponses))		

def main(): 
	checkForFile()
	totalResponses = lineCount("http_access_log.txt")
	print("Total number of requests made:", totalResponses)
	monthlylogs()
	redirectCodes(totalResponses)
	clientErrors(totalResponses)
	
main()
# import os; import urllib.request; import re;
# from collections import Counter
# from time import sleep

# # regex = '([(\w+)]+) - - \[(.*?)\] "(.*?)" (\d+) (\S+)'				#breaks log into groupings of origin, date&time, command file protocol, code, size 
# # regex = '([(\w+)]+) - - \[(.*?)\] "(.*)?"? (\d+) (\S+)'				#works for all errors until "GET"
# # regex = '([(\w+)]+) - - \[(.*?)\] "(.*)?"? (\d+) (\S+)|([(\w+)]+) - - \[(.*?)\] "(.*)? '
# regex = '([(\w+)]+) - - \[(.*?)\] "(.*)?"? (\d+) (\S+)|([(\w+)]+) - - \[(.*?)\] "(.*)?|([(\w+)]+) (\d+) - (\s+)(.*)?|(\S+) (\S+)" (\d+) -   (\S+)'


# def lineCount(logs):                                                #count lines for total number of requests, keep corrupt entries as they're still requests
# 	with open(logs) as x:
# 		for i, l in enumerate(x):
# 			pass
# 	return i+1

# def checkForFile():                                                 #check if file exists, else download
# 	url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
# 	if os.path.exists("./http_access_log.txt") == False:            
# 		print("Downloading access logs from:", url)
# 		urllib.request.urlretrieve(url, "./http_access_log.txt")  

# def isEntryValid(logs):                                             #corrupt entries lack hyphens, check for and remove corrupt log entries
# 	validlog = '-'
# 	invalid = 0
# 	print("Stripping invalid or unreadable logfiles...")
# 	with open('http_access_log.txt') as rawlogs, open('validlogs.txt', 'w') as validlogs:
# 		for line in rawlogs:
# 			if not any(validlog in line for valid in validlog):
# 				pass
# 				invalid += 1
# 			else:
# 				validlogs.write(line)
# 	sleep(1)
# 	print("Removed %d unreadable logfiles" % invalid)
# 	return invalid


# def successCodes(logs, loglength):
# 	with open(logs) as validlogs:				
# 		i = 0
# 		array = []
# 		successcodes = 0
# 		for line in validlogs:								#creating array of each log line
# 			array.append(line)

# 	while (i < loglength):								#iterate through strings in array for regex
# 		print("Line number: ", i)
# 		line = re.findall(regex, array[i]).groups()
# 		if(line[3].startswith("3")):
# 			successcodes+=1
# 		i+=1
# 	print("Number of successcodes: ", successcodes)


# def failCodes(logs):
# 	pass


# def main(): 
# 	checkForFile()
# 	totalResponses = lineCount("http_access_log.txt")
# 	print("Number of requests made:", totalResponses)
# 	totalErrorResponses = isEntryValid("http_access_log.txt")
# 	totalValidResponses = totalResponses - totalErrorResponses
# 	successCodes("validlogs.txt", totalValidResponses)

# main()

# #usps case number ca141722721
# # local      index.html
# # remote - - [10/Oct/1995:08:57:04 -0600] "GET index.html HTTP/1.0" 200 6061
# # remote - - [10/Oct/1995:08:57:06 -0600] "GET 3119.gif HTTP/1.0" 200 2048
# # local - - [10/Oct/1995:08:57:19 -0600] "GET index.html HTTP/1.0" 200 3020