import config
#https://github.com/sammchardy/python-binance
from binance.client import Client

api_key = config.api_key
api_secret = config.api_secret

client = Client(api_key, api_secret)

# get market depth
depth = client.get_order_book(symbol='BNBBTC')

print(depth)

