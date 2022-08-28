import time
import hmac
from requests import Request
from client import FtxClient

ts = int(time.time() * 1000)

# Instanciating client
print('Instanciating FTX REST client ...')
ftxclient_params = {
    "api_key" : 'ibmjTTz6t2vOwxC2_HO8Y3Agu0XU5u9bWHKAL4-d',
    "api_secret" : 'ChhqNybMGvX4AbQJ8t9x-fg0w571A-Y-g_nGv3bp',
    "subaccount_name" : 'napbots'
}
ftxclient = FtxClient(**ftxclient_params)
print('Client instanciated!')

print('Getting markets ...')
ftxmarkets = ftxclient.get_markets()
print('Got markets!')
print('    Got a total of ', len(ftxmarkets), ' markets!')
#print(ftxmarkets)

print('Getting ETH-PERP open orders ...')
ftxopenorders_ethperp = ftxclient.get_open_orders('ETH-PERP')
print('Got ETH-PERP open orders!')
print('    Have ', len(ftxopenorders_ethperp), ' orders on ETH-PERP market')

print('Getting ETH-0930 open orders ...')
ftxopenorders_eth0930 = ftxclient.get_open_orders('ETH-0930')
print('Got ETH-0930 open orders!')
print('    Have ', len(ftxopenorders_eth0930), ' orders on ETH-0930 market')

print('Getting ETH-1230 open orders ...')
ftxopenorders_eth1230 = ftxclient.get_open_orders('ETH-1230')
print('Got ETH-1230 open orders!')
print('    Have ', len(ftxopenorders_eth1230), ' orders on ETH-1230 market')

print('Getting ETH/AUD open orders ...')
ftxopenorders_ethaud = ftxclient.get_open_orders('ETH/AUD')
print('Got ETH/AUD open orders!')
print('    Have ', len(ftxopenorders_ethaud), ' orders on ETH/AUD market')

print('Getting ETH/BRZ open orders ...')
ftxopenorders_ethbrz = ftxclient.get_open_orders('ETH/BRZ')
print('Got ETH/BRZ open orders!')
print('    Have ', len(ftxopenorders_ethbrz), ' orders on ETH/BRZ market')

print('Getting ETH/BTC open orders ...')
ftxopenorders_ethbtc = ftxclient.get_open_orders('ETH/BTC')
print('Got ETH/BTC open orders!')
print('    Have ', len(ftxopenorders_ethbtc), ' orders on ETH/BTC market')

print('Getting ETH/EUR open orders ...')
ftxopenorders_etheur = ftxclient.get_open_orders('ETH/EUR')
print('Got ETH/EUR open orders!')
print('    Have ', len(ftxopenorders_etheur), ' orders on ETH/EUR market')

print('Getting ETH/JPY open orders ...')
ftxopenorders_ethjpy = ftxclient.get_open_orders('ETH/JPY')
print('Got ETH/JPY open orders!')
print('    Have ', len(ftxopenorders_ethjpy), ' orders on ETH/JPY market')

print('Getting ETH/USD open orders ...')
ftxopenorders_ethusd = ftxclient.get_open_orders('ETH/USD')
print('Got ETH/USD open orders!')
print('    Have ', len(ftxopenorders_ethusd), ' orders on ETH/USD market')

print('Getting ETH/USDT open orders ...')
ftxopenorders_ethusdt = ftxclient.get_open_orders('ETH/USDT')
print('Got ETH/USDT open orders!')
print('    Have ', len(ftxopenorders_ethusdt), ' orders on ETH-USDT market')



print('Getting BTC-PERP open orders ...')
ftxopenorders_btcperp = ftxclient.get_open_orders('BTC-PERP')
print('Got BTC-PERP open orders!')
print('    Have ', len(ftxopenorders_btcperp), ' orders on BTC-PERP market')

print('Getting BTC-MOVE-0828 open orders ...')
ftxopenorders_btcmove0828 = ftxclient.get_open_orders('BTC-MOVE-0828')
print('Got BTC-MOVE-0828 open orders!')
print('    Have ', len(ftxopenorders_btcmove0828), ' orders on BTC-MOVE-0828 market')

print('Getting BTC-MOVE-0829 open orders ...')
ftxopenorders_btcmove0829 = ftxclient.get_open_orders('BTC-MOVE-0829')
print('Got BTC-MOVE-0829 open orders!')
print('    Have ', len(ftxopenorders_btcmove0829), ' orders on BTC-MOVE-0829 market')

print('Getting BTC-MOVE-WK-0902 open orders ...')
ftxopenorders_btcmovewk0902 = ftxclient.get_open_orders('BTC-MOVE-WK-0902')
print('Got BTC-MOVE-WK-0902 open orders!')
print('    Have ', len(ftxopenorders_btcmovewk0902), ' orders on BTC-MOVE-WK-0902 market')

print('Getting BTC-MOVE-WK-0909 open orders ...')
ftxopenorders_btcmovewk0909 = ftxclient.get_open_orders('BTC-MOVE-WK-0909')
print('Got BTC-MOVE-WK-0909 open orders!')
print('    Have ', len(ftxopenorders_btcmovewk0909), ' orders on BTC-MOVE-WK-0909 market')

print('Getting BTC-MOVE-WK-0916 open orders ...')
ftxopenorders_btcmovewk0916 = ftxclient.get_open_orders('BTC-MOVE-WK-0916')
print('Got BTC-MOVE-WK-0916 open orders!')
print('    Have ', len(ftxopenorders_btcmovewk0916), ' orders on BTC-MOVE-WK-0916 market')

print('Getting BTC-0930 open orders ...')
ftxopenorders_btc0930 = ftxclient.get_open_orders('BTC-0930')
print('Got BTC-0930 open orders!')
print('    Have ', len(ftxopenorders_btc0930), ' orders on BTC-0930 market')

print('Getting BTC-MOVE-2022Q3 open orders ...')
ftxopenorders_btcmove2022q3 = ftxclient.get_open_orders('BTC-MOVE-2022Q3')
print('Got BTC-MOVE-2022Q3 open orders!')
print('    Have ', len(ftxopenorders_btcmove2022q3), ' orders on BTC-MOVE-2022Q3 market')

print('Getting BTC-1230 open orders ...')
ftxopenorders_btc1230 = ftxclient.get_open_orders('BTC-1230')
print('Got BTC-1230 open orders!')
print('    Have ', len(ftxopenorders_btc1230), ' orders on BTC-1230 market')

print('Getting BTC-MOVE-2022Q4 open orders ...')
ftxopenorders_btcmove2022q4 = ftxclient.get_open_orders('BTC-MOVE-2022Q4')
print('Got BTC-MOVE-2022Q4 open orders!')
print('    Have ', len(ftxopenorders_btcmove2022q4), ' orders on BTC-MOVE-2022Q4 market')

print('Getting BTC/AUD open orders ...')
ftxopenorders_btcaud = ftxclient.get_open_orders('BTC/AUD')
print('Got BTC/AUD open orders!')
print('    Have ', len(ftxopenorders_btcaud), ' orders on BTC/AUD market')

print('Getting BTC/BRZ open orders ...')
ftxopenorders_btcbrz = ftxclient.get_open_orders('BTC/BRZ')
print('Got BTC/BRZ open orders!')
print('    Have ', len(ftxopenorders_btcbrz), ' orders on BTC/BRZ market')

print('Getting BTC/EUR open orders ...')
ftxopenorders_btceur = ftxclient.get_open_orders('BTC/EUR')
print('Got BTC/EUR open orders!')
print('    Have ', len(ftxopenorders_btceur), ' orders on BTC/EUR market')

print('Getting BTC/JPY open orders ...')
ftxopenorders_btcjpy = ftxclient.get_open_orders('BTC/JPY')
print('Got BTC/JPY open orders!')
print('    Have ', len(ftxopenorders_btcjpy), ' orders on BTC/JPY market')

print('Getting BTC/TRYB open orders ...')
ftxopenorders_btctryb = ftxclient.get_open_orders('BTC/TRYB')
print('Got BTC/TRYB open orders!')
print('    Have ', len(ftxopenorders_btctryb), ' orders on BTC/TRYB market')

print('Getting BTC/USD open orders ...')
ftxopenorders_btcusd = ftxclient.get_open_orders('BTC/USD')
print('Got BTC/USD open orders!')
print('    Have ', len(ftxopenorders_btcusd), ' orders on BTC/USD market')

print('Getting BTC/USDT open orders ...')
ftxopenorders_btcusdt = ftxclient.get_open_orders('BTC/USDT')
print('Got BTC/USDT open orders!')
print('    Have ', len(ftxopenorders_btcusdt), ' orders on BTC-USDT market')


