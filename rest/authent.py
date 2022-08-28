import time
import hmac
import json
from requests import Request
from client import FtxClient

ts = int(time.time() * 1000)

# Read authent data from 'authen.data' file
with open('authent.data') as f:
    ftxclient_params_str = f.read()

ftxclient_params = json.loads(ftxclient_params_str)

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
    print('    Position "', position['future'], '"')
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






