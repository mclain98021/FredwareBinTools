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
from __future__ import division
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="fileName", help="file to parse, default=%default", metavar="FILE", default="apache.log")
parser.add_option("-a", "--reportAll", action="store_true", dest="reportAll", help="show all reports", default=False)
parser.add_option("-t", "--top10", action="store_true", dest="reportTop10", help="Top 10 requested pages and the number of requests made for each", default=False)
parser.add_option("-s", "--success", action="store_true", dest="reportSucccessPercentReq", help="Percentage of successful requests (anything in the 200s and 300s range)", default=False)
parser.add_option("-u", "--unsuccess", action="store_true", dest="reportUnsucccessPercentReq", help="Percentage of unsuccessful requests (anything that is not in the 200s or 300s range)", default=False)
parser.add_option("-r", "--top10Unsuccess", action="store_true", dest="reportTop10Unsuccess", help="Top 10 unsuccessful page requests", default=False)
parser.add_option("-i", "--top10IpPages", action="store_true", dest="reportTop10IpPages", help="The top 10 IPs making the most requests, displaying the IP address and number of requests made", default=False)
#parser.add_option("-m", "--numReqPerMinute", action="store_true", dest="reportReqPerMinute", help="The total number of requests made every minute in the entire time period covered by the file provided.", default=False)

(options, args) = parser.parse_args()

# accumulators for report stats
#totalRequests = 0
#requestMap = 0
#successCount = 0
#failCount = 0
errorList = []

totalPages = {}
failPages = {}
successPages = {}
ipPages={}

def analizeFile(fileName):
    print "Parsing file:", fileName
    try:
        f = open(fileName)
    except IOError:
        errorList.append("Can not read " + fileName)
        return
    lineno = 0
    for line in f:
        lineno += 1
        try:
            analizeLine(line)
        except:
            errorList.append("Error in " + fileName + " on line " + str(lineno))
    return

def analizeLine(logLine):
    '''
    Fields in record are whitespace separated:
    IP - - [timestamp] "request path status ?
    '''
#    print logLine
    r = logLine.split()
    #print r
    '''
    0 = IP                        3 = timestamp        4 = TZ    5 = method    6 = page                    7 = protocol    8 = status    9 = ?
    ['10.0.16.208', '-', '-', '[31/Oct/1994:23:59:50', '+0000]', '"GET', '/finance/list.php?value=60549', 'HTTP/1.0"', '404', '1595']
    '''
    ip = r[0]
    timestamp = r[3].lstrip('[')
    #timestamp = time.strptime(r[3].lstrip('['),"%d/%b/%Y:%H:%M:%S")
    method = r[5].lstrip('"')
    #page = r[6].split("?")[0]
    page = r[6]
    stat = int(r[8])
    
    if page in totalPages:
        totalPages[page] = totalPages[page] + 1
    else:
        totalPages.update({page:1})
        
    if ip in ipPages:
        ipPages[ip] = ipPages[ip] +1
    else:
        ipPages.update({ip:1})
        
    if (stat >= 200) and (stat < 400):
        # success
        if page in successPages:
            successPages[page] = successPages[page] + 1
        else:
            successPages.update({page:1})
    else:
        # failure
        if page in failPages:
            failPages[page] = failPages[page] + 1
        else:
            failPages.update({page:1})
         
    return

def reportTop10(dict):
    s=sorted(dict,key=dict.__getitem__,reverse=True)
    i = 1
    for k in s:
        print i,k,dict[k]
        if i == 10:
            break
        i += 1

def report():
    if options.reportAll or options.reportTop10:
        print "Most requested pages:"
        reportTop10(totalPages)
    ''' not in spec but useful?
        print "Most successful pages (page, count):"
        reportTop10(successPages)
    '''
    if options.reportAll or options.reportSucccessPercentReq:
        # print len(successPages),"/",len(totalPages),len(failPages)
        print "Percentage of successful requests: ",str(len(successPages)/len(totalPages)*100.),"%"
    
    if options.reportAll or options.reportUnsucccessPercentReq:
        print "Most failed pages (page, count):"
        reportTop10(failPages)
    
    if options.reportAll or options.reportTop10IpPages:
        print "The top 10 IPs making the most requests, (IP, count)"
        reportTop10(ipPages)
    return

def usage():
    parser.print_help()
    exit(-1)
    return

def go():
    print "Apache log file parser demonstration by Fred McLain, July 2nd 2016"
    if 1 == len(sys.argv):
        usage()  # require command line arguments or show usage and bail out
    analizeFile(options.fileName)
    report()
    if len(errorList) > 0:
        print "Errors in input",errorList
    return 

go()
