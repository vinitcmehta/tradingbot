import config
#https://github.com/sammchardy/python-binance
from binance.client import Client
import time
import constant

api_key = config.api_key
api_secret = config.api_secret

client = Client(api_key, api_secret)

# get market depth
depth = client.get_order_book(symbol='BNBBTC')

print(depth)

#Helper functions

def get_balances():
    print("Getting balances")

def get_market_price():
    print("Getting market price")

def place_sell_order():
    print("place sell order")

def place_buy_order():
    print("place buy order")

def get_operation_details():
    print("get operation details")

#Decision making

isNextOperationBuy = True

lastOpPrice = 100.00

def attempt_to_make_trade():
    print ("attempt to make a trade")

def try_to_buy():
    print ("try to buy")
    isNextOperationBuy = False

def try_to_sell():
    print ("try to sell")
    isNextOperationBuy = True


#Main loop

while True:
    attempt_to_make_trade()
    time.sleep(30)


