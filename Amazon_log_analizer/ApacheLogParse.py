#!/usr/bin/python
''' 
Apache log analysis script for Amazon Code challenge.
July 2nd 2016 by Fred McLain.
Copyright (C) 2016 Fred McLain, all rights reserved.

high level language of your choice (e.g. Python/Ruby/Perl)

The right fit language appears to be Python, so I'm going with that even though I'm a Java developer.

required:
* Top 10 requested pages and the number of requests made for each
* Percentage of successful requests (anything in the 200s and 300s range)
* Percentage of unsuccessful requests (anything that is not in the 200s or 300s range)
* Top 10 unsuccessful page requests
* The top 10 IPs making the most requests, displaying the IP address and number of requests made.
* Option parsing to produce only the report for one of the previous points (e.g. only the top 10 urls, only the percentage of successful requests and so on)
* A README file explaining how to use the tool, what its dependencies and any assumptions you made while writing it

optional:
* Unit tests for your code.
* The total number of requests made every minute in the entire time period covered by the file provided.
* For each of the top 10 IPs, show the top 5 pages requested and the number of requests for each.

Assumptions:
* Statistics for the number of pages and requesting IPs does not exceed available memory.
* Log file lines are of a uniform format
* Log records are in time order

Sample log lines:
10.0.68.207 - - [31/Oct/1994:14:00:17 +0000] "POST /finance/request.php?id=39319 HTTP/1.1" 200 56193
10.0.173.204 - - [31/Oct/1994:14:00:20 +0000] "GET /kernel/get.php?name=ndCLVHvbDM HTTP/1.1" 403 759

Records are new line separated.

Fields in record are whitespace separated:
    IP - - [timestamp] "request path status ?
'''
import sys
from optparse import OptionParser

# global vars to track options
'''
reportAll = True
reportTop10Req = False
reportSucccessPercentReq = False
reportUnsucccessPercentReq = False
reportUnsucccessPagePercentReq = False
reportTop10Unsuccess = False
reportTop10IpPages = False
reportReqPerMinute = False
fileName = ""
'''

parser = OptionParser()
parser.add_option("-f", "--file", dest="fileName", help="file to parse, default=%default", metavar="FILE", default="apache.log")
parser.add_option("-a", "--reportAll", action="store_true", dest="reportAll", help="show all reports", default=False)
parser.add_option("-t", "--top10", action="store_true", dest="reportTop10", help="Top 10 requested pages and the number of requests made for each", default=False)
parser.add_option("-s", "--success", action="store_true", dest="reportSucccessPercentReq", help="Percentage of successful requests (anything in the 200s and 300s range)", default=False)
parser.add_option("-u", "--unsuccess", action="store_true", dest="reportUnsucccessPercentReq", help="Percentage of unsuccessful requests (anything that is not in the 200s or 300s range)", default=False)
parser.add_option("-r", "--top10Unsuccess", action="store_true", dest="reportTop10Unsuccess", help="Top 10 unsuccessful page requests", default=False)
parser.add_option("-i", "--top10IpPages", action="store_true", dest="reportTop10IpPages", help="The top 10 IPs making the most requests, displaying the IP address and number of requests made", default=False)
parser.add_option("-m", "--numReqPerMinute", action="store_true", dest="reportReqPerMinute", help="The total number of requests made every minute in the entire time period covered by the file provided.", default=False)

(options, args) = parser.parse_args()

# accumulators for report stats
totalRequests = 0
requestMap = 0
successCount = 0
failCount = 0

def analizeFile(fileName):
    print "Parsing file:", fileName
    return

def analizeLine(logLine):
    return

def report():
    return

def usage():
    parser.print_help()
    exit(-1)
    return

def go():
    print "Apache log file parser demonstration by Fred McLain, July 2nd 2016"
    if 1 == len(sys.argv):
        usage() # require command line arguments or show usage and bail out
    analizeFile(options.fileName)
    report()
    
    return 

go()
