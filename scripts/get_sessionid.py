#!/usr/local/bin/python3

import json, requests, argparse
from grapi.grapi import Grapi
from requests.structures import CaseInsensitiveDict

GRAYLOG_URL = "http://vdr3xiflm001.gdp.int:9000/api/system/sessions"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
headers["Accept"] = "application/json"
headers["X-Requested-By"] = "cli"

parser = argparse.ArgumentParser(description='Retrieving authentication session id (a token from your Graylog user interface is required)')
parser.add_argument('--username', metavar='user', type=str, nargs=1, help='fill in your graylog user account name', required=True)
parser.add_argument('--password', metavar='passwd', type=str, nargs=1, help='fill in your graylog user account password', required=True)

args = parser.parse_args()

graylog_username = args.username[0]
graylog_password = args.password[0]

# Authenticating
plain_auth_data = { "username" : graylog_username , "password" : graylog_password }
auth_req = requests.post(GRAYLOG_URL, headers=headers, data=json.dumps(plain_auth_data))
auth_session = auth_req.json()
session_id = auth_session["session_id"]

print(session_id)