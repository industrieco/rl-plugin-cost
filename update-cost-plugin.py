
import requests
import json
import os

auth_endpoint = 'https://' + os.environ['RS_SERVER'] + '/api/oauth2'
parent_acc = "/api/accounts/" + os.environ['RS_ACCOUNT_ID']
refresh_token = os.environ['RS_REFRESH_TOKEN']
plugin_id = "https://analytics.rightscale.com/api/plugin_costs/" + os.environ['RS_PLUGIN_ID']

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

update_url = plugin_id

update_headers =	{
	'Authorization': 'Bearer {0}'.format(access_token),
	'Content-Type': 'application/json',
	'X-API-VERSION': '1.0'
					}

update_payload =	{
	'account_href': parent_acc,
	'start_time': '2017-01-01T00:00:00+00:00',
	'total_cost': '0.999',
	'product': 'Plugin Cost Product',
  	'product_category': 'Other'
					}

update_call = requests.patch(url=update_url, headers=update_headers, json=update_payload)

if update_call.status_code == 200:
	print('Updated plugin cost')
else:
	print('Something went wrong...')
	print(update_call.text)
