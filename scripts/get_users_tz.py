#!/usr/local/bin/python3

import json, requests, argparse
from grapi.grapi import Grapi
from requests.structures import CaseInsensitiveDict

GRAYLOG_URL = "http://vdr3xiflm001.gdp.int:9000/api/users"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
headers["Accept"] = "application/json"
headers["X-Requested-By"] = "cli"

parser = argparse.ArgumentParser(description='Listing all users timezone')
parser.add_argument('--sid', metavar='sid', type=str, nargs=1, help='fill in your Graylog user session id (a token from your Graylog user interface is required)', required=True)

args = parser.parse_args()
graylog_sid = args.sid[0]

#Retrieving user list

get_users = requests.get (GRAYLOG_URL, headers=headers, auth=(graylog_sid, 'session'))
users = get_users.json()
#gdp_users = []

for key in users:
    for e in users[key]:
        if "graylog-sidecar" in e["username"]:
            pass
        elif "admin" in e["username"]:
            pass
        else:
            print(f"username: {e['username']}, timezone: {e['timezone']}")
            #gdp_users.append(e["username"])