import time
import hmac
import json
from urllib.parse import urlencode, quote
from requests import Request
from client import FtxClient

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
print('Instanciating FTX REST client ...')
ftxclient = FtxClient(**ftxclient_params)
print('Client instanciated!')

print('## BALANCES')

print('Getting total USD balance ...')
ftxtotalusdbalance = ftxclient.get_total_usd_balance()
print('Got total USD balance!')
print('	   Total USD balance: ', ftxtotalusdbalance, ' USD')

print('Getting total account USD balance ...')
ftxtotalaccountusdbalance = ftxclient.get_total_account_usd_balance()
print('Got total account USD balance!')
print('	   Total account USD balance: ', ftxtotalaccountusdbalance, ' USD')

#print('Getting markets ...')
#ftxmarkets = ftxclient.get_markets()
#print('Got markets!')
#print('    Got a total of ', len(ftxmarkets), ' markets!')
#print(ftxmarkets)

print('## POSITIONS')

print('Getting positions ...')
ftxpositions = ftxclient.get_positions()
print('Got positions!')
print('	   Got ', len(ftxpositions), ' positions')
#print(ftxpositions)

for position in ftxpositions:
    print('    Position "{}"'.format(position['future']))
    print('	   Side: ', position['side'])
    print('	   Size: ', position['size'])
    print('	   Cost: ', position['cost'])
    print('	   Entry price: ', position['entryPrice'])
    print('	   PnL: ')
    print('	     unrealized: ', position['unrealizedPnl'], '')
    print('	     realized: ', position['realizedPnl'])

print('## ORDERS')

print('Getting BTC-PERP open orders ...')
ftxopenorders_btcperp = ftxclient.get_open_orders('BTC-PERP')
print('Got BTC-PERP open orders!')
print('	   Have ', len(ftxopenorders_btcperp), ' orders on BTC-PERP market')

print('Getting ADA-PERP open orders ...')
ftxopenorders_adaperp = ftxclient.get_open_orders('ADA-PERP')
print('Got ADA-PERP open orders!')
print('	   Have ', len(ftxopenorders_adaperp), ' orders on ADA-PERP market')

print('Getting ETH-PERP open orders ...')
ftxopenorders_ethperp = ftxclient.get_open_orders('ETH-PERP')
print('Got ETH-PERP open orders!')
print('	   Have ', len(ftxopenorders_ethperp), ' orders on ETH-PERP market')






