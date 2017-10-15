
import requests
import json
import os

auth_endpoint = 'https://' + os.environ['RS_SERVER'] + '/api/oauth2'
parent_acc = "/api/accounts/" + os.environ['RS_ACCOUNT_ID']
refresh_token = os.environ['RS_REFRESH_TOKEN']

auth_headers =	{'X-API-Version': '1.5'}

auth_payload =	{
	'grant_type': 'refresh_token',
	'refresh_token': refresh_token
				}

auth_call = requests.post(url=auth_endpoint, headers=auth_headers, data=auth_payload)

if auth_call.status_code == 200:
	print('Success!')
else:
	print('Something went wrong...')
	print(auth_call.text)

auth_output = json.loads(auth_call.text)
access_token = auth_output['access_token']

index_url = 'https://analytics.rightscale.com/api/plugin_costs'

index_headers =		{
	'Authorization': 'Bearer {0}'.format(access_token),
	'Content-Type': 'application/json',
	'X-API-VERSION': '1.0'
					}

index_call = requests.get(url=index_url, headers=index_headers)

if index_call.status_code == 200:
	print('Success!')
else:
	print('Something went wrong...')
	print(index_call.text)
