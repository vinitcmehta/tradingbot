import config
#https://github.com/sammchardy/python-binance
from binance.client import Client
import time
import constant

#TODO remove global variable usage
#TODO finish psuedocode logic
#TODO implement helper functions
#TODO add logging
#TODO implement trends
#TODO add monitoring with dashboard
#TODO add lightweight db for price straoge persistence
#TODO test strategies on past data

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
    get_market_price()
    if isNextOperationBuy:
        try_to_buy()
    else:
        try_to_sell()


def try_to_buy():
    global isNextOperationBuy
    print ("try to buy")
    print(constant.UPWARD_TREND_THRESHOLD)
    print(constant.DIP_THRESHOLD)
    place_buy_order()
    isNextOperationBuy = False

def try_to_sell():
    global isNextOperationBuy
    print ("try to sell")
    print(constant.PROFIT_THRESHOLD)
    print(constant.STOP_LOSS_THRESHOLD)
    place_sell_order()
    isNextOperationBuy = True


#Main loop

while True:
    attempt_to_make_trade()
    time.sleep(5)


