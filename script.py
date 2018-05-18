import requests
import json
import sys

infile = open(sys.argv[1])

BASE_URL = sys.argv[2] + '/reportTagging?report='
#BASE_URL = 'http://localhost:5000/reportTagging?report='

for line in infile:
    url = BASE_URL + line
    t = requests.get(url).json()
    print line
    print t
    print "\n"


infile.close()
