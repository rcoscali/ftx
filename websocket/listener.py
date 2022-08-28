import time
import hmac
import json
from urllib.parse import urlencode, quote
from requests import Request
from client import FtxWebsocketClient

ts = int(time.time() * 1000)

# Read authent data from 'authent.data' file
# This file is a json for the FtxClient dict
# provided as params at client instanciation
# It has the following format:
# {
#     "api_key" : "<YourAPIKey>",
#     "api_secret" : "<YourAPIKeySecret>",
#     "subaccount_name" : "<YourURIEncodedSubAccountName>"
# }

with open('authent.data') as f:
    ftxclient_params_str = f.read()

# Handle URLEncoded subaccount name
ftxclient_params = json.loads(ftxclient_params_str)
ftxclient_subaccount_str = ftxclient_params['subaccount_name']
ftxclient_subaccount = urlencode({'subaccount_name':ftxclient_subaccount_str}, quote_via=quote)
ftxclient_params_eqix = ftxclient_subaccount.find("=") + 1
ftxclient_params['subaccount_name'] = ftxclient_subaccount[ftxclient_params_eqix:]
print('Sub account name: "{}"'.format(ftxclient_params['subaccount_name']))

# Instanciating client
print('Instanciating FTX WebSocket client ...')
ftxclient = FtxWebsocketClient(**ftxclient_params)
print('WebSocket Client instanciated!')

# Connect websocket
print('Connecting ...')
ftxclient.connect()
print('Connected!')

# Get trades
print('Subscribing for orders ...')
orders = ftxclient.get_orders()
print('Subscribed orders!')
print('orders = {} '.format(orders))

