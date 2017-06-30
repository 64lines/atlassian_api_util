from urllib2 import Request, urlopen, HTTPError
import base64
import sys
import getopt
import json

def fetch_data(user, password, jql):
    url = "https://cafetosoftware.atlassian.net/rest/api/2/search?jql=%s" % jql
    request = Request(url)
    base64string = base64.b64encode('%s:%s' % (user, password))
    request.add_header("Authorization", "Basic %s" % base64string)

    issues = []
    print "Fetching data from Rest API..."
    try:
        response = urlopen(request)
        issues = json.loads(response.read())['issues']
    except HTTPError as e:
        print e.code
    else:
        print "200"

    print issues

def main():
    command = "atlassian_api_calculator.py -u <user> -p <password> -j <jql>" 
    try:
       opts, args = getopt.getopt(sys.argv[1:], "hup:j", ["user=", "password=", "jql="])
    except getopt.GetoptError:
       print command 
       sys.exit(2)

    user = ""
    password = ""
    jql = ""
    for opt, arg in opts:
        if opt == '-h':
            print command
            sys.exit()
        elif opt in ('-u', '--user'):
            user = arg
        elif opt in ('-p', '--password'):
            password = arg
        elif opt in ('-j', '--jql'):
            jql = arg

    fetch_data(user, password, jql)

main()
