
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

plugin_url = 'https://analytics.rightscale.com/api/plugin_costs'

plugin_headers =	{
	'Authorization': 'Bearer {0}'.format(access_token),
	'Content-Type': 'application/json',
	'X-API-VERSION': '1.0'
					}

plugin_payload =	{
	'account_href': parent_acc,
	'start_time': '2017-01-01T00:00:00+00:00',
	'total_cost': '0.999',
	'product': 'Plugin Cost Product',
  	'product_category': 'Other'
					}

plugin_call = requests.post(url=plugin_url, headers=plugin_headers, json=plugin_payload)

if plugin_call.status_code == 200:
	print('Created new plugin cost')
else:
	print('Something went wrong...')
	print(plugin_call.text)
