import config
#https://github.com/sammchardy/python-binance
from binance.client import Client
import time
import constant
from binance.exceptions import BinanceOrderException, BinanceAPIException

#TODO remove global variable usage
#TODO change balance output to only one crypto and GBP
#TODO look into limit orders rather than market orders
#TODO change or add further crypto symbols
#TODO implement get operation details
#TODO add logging
#TODO implement trends
#TODO add monitoring with dashboard
#TODO add lightweight db for price straoge persistence
#TODO test strategies on past data

api_key = config.api_key
api_secret = config.api_secret

client = Client(api_key, api_secret)

# get market depth
depth = client.get_order_book(symbol='XRPGBP')
print(depth)


#Helper functions

def get_balances():
    print("Getting balances")
    print(client.get_account())
    return client.get_account()

#Get market price of XRPGBP
def get_market_price():
    print("Getting market price")
    return float(client.get_symbol_ticker(symbol='XRPGBP').get("price"))

print(get_market_price())

#TODO factor in 0.1% binance fee
def place_sell_order():
    print("place sell order")
    # Sell 49.9 Ripple Coins with GBP

    try:
       result = client.create_order(
           symbol='XRPGBP',
           side=Client.SIDE_SELL,
           type=Client.ORDER_TYPE_MARKET,
           quantity=49.9)
    except BinanceAPIException as e:
       print(e)
    else:
       print("Success")
    return get_market_price()


#TODO factor in 0.1% binance fee
def place_buy_order():
    print("place buy order")

    # Buy 50 Ripple Coins with GBP

    try:
       result = client.create_order(
           symbol='XRPGBP',
           side=Client.SIDE_BUY,
           type=Client.ORDER_TYPE_MARKET,
           quantity=50)
    except BinanceOrderException as e:
       print(e)
    else:
       print("Success")
    return get_market_price()

def get_operation_details():
    print("get operation details")
    return 100

#Decision making

isNextOperationBuy = True

lastOpPrice = 0.22503000

def attempt_to_make_trade():
    print ("attempt to make a trade")
    currentPrice = get_market_price()
    percentageDiff = ((currentPrice - lastOpPrice)/lastOpPrice)*100
    print("percentage diff is: " + str(percentageDiff))
    if isNextOperationBuy:
        try_to_buy(percentageDiff)
    else:
        try_to_sell(percentageDiff)

def try_to_buy(percentageDiff):
    global isNextOperationBuy
    global lastOpPrice
    print ("try to buy")
    if percentageDiff >= constant.UPWARD_TREND_THRESHOLD or percentageDiff <= constant.DIP_THRESHOLD:
        lastOpPrice = place_buy_order()
        print(lastOpPrice)
        isNextOperationBuy = False
    else:
        print("not buying")

def try_to_sell(percentageDiff):
    global isNextOperationBuy
    global lastOpPrice
    print ("try to sell")
    if percentageDiff >= constant.PROFIT_THRESHOLD or percentageDiff <= constant.STOP_LOSS_THRESHOLD:
        lastOpPrice = place_sell_order()
        print(lastOpPrice)
        isNextOperationBuy = True
    else:
        print("not selling")


#Main loop

while True:
    attempt_to_make_trade()
    time.sleep(7200)


