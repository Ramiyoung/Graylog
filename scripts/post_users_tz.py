#!/usr/local/bin/python3

import json, requests, argparse
from grapi.grapi import Grapi
from requests.structures import CaseInsensitiveDict

GRAYLOG_URL = "http://vdr3xiflm001.gdp.int:9000/api/users"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
headers["Accept"] = "application/json"
headers["X-Requested-By"] = "cli"

parser = argparse.ArgumentParser(description='Modifying user timezone')
parser.add_argument('--sid', metavar='session-id', type=str, nargs=1, help='fill in your Graylog user session id (a token from your Graylog user interface is required)', required=True)
parser.add_argument('--users', metavar='users', type=str, nargs='+', help='list of users', required=True)
parser.add_argument('--timezone', metavar='timezone', type=str, nargs=1, help='timezone(Europe/Paris, Europe/Vienna, UTC...)', default="UTC", required=True)

args = parser.parse_args()
graylog_sid = args.sid[0]
graylog_timezone = args.timezone[0]
graylog_users = args.users

tz_params = {    
    "timezone": graylog_timezone
}

for u in graylog_users:
    GRAYLOG_USER_URL = GRAYLOG_URL + '/' + str(u)
    x = requests.put(GRAYLOG_USER_URL, headers=headers, auth=(graylog_sid, 'session'), data=json.dumps(tz_params))
    print (x)