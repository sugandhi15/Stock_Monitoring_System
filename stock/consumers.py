import json
from channels.generic.websocket import AsyncWebsocketConsumer
import yfinance as yf
import asyncio
import random
from django.conf import settings
import jwt

# generating changing price for testing
def generateRandomPrice():
    price = random.uniform(0,1000)
    return price



class stockMonitoring(AsyncWebsocketConsumer):

    activeTask = None

    async def connect(self):
        try:
            await self.accept()
            token = self.scope['query_string'].decode('utf-8').split('=')[-1]
            print(token)
        # try:
            decoded_token = jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=["HS256"]
            )
            print(decoded_token)
            self.user = decoded_token['user_id'] 

            if not self.user:
                await self.send(text_data=json.dumps({
                    'message':'Error Occured'
                }))

            print(self.user)
            self.subsrcribed = False
            await self.send(text_data=json.dumps({   # json.dumps convert python dict to json
                'message': 'Connected Successsfully! '
            }))
        except Exception as e:
            await self.send(text_data=json.dumps({
                'message':"Error Occured"
            }))




    async def receive(self, text_data):
        try:
            data = json.loads(text_data)  # converts json to python object
            if self.activeTask:
                self.activeTask.cancel()
            if data['action'] == 'subscribe':

                if data['channel'] == 'stock_update' : 
                    stocks = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS"]
                    self.subscribed = True
                    self.activeTask =asyncio.create_task(self.stockUpdates(stocks))   # create_task runs task in background and loops

                    
                elif data['channel'] == 'price_update':
                    stocks = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS"]
                    self.subscribed = True
                    self.activeTask =asyncio.create_task(self.priceUpdates(stocks))

                else:
                    self.send(text_data=json.dumps({
                        'message':'Plese enter valid channel'
                    }))

            elif data['action'] == 'unsubscribe':
                if data['channel'] == 'stock_update' : 
                    self.subscribed=False
                    await self.send(text_data=json.dumps({ 
                        'message': 'unsubscribed successfully '
                    }))

                else:
                    self.send(text_data=json.dumps({
                        'message':'Plese enter valid channel'
                    }))

            else:
                await self.send(text_data=json.dumps({ 
                        'message': 'please enter valid data'
                }))

        except Exception as e:
            await self.send(text_data=json.dumps({
                'error': "Error Occured"
            }))



    async def disconnect(self, close_code):
        try:
            self.subscribed=False
            print('disconnected')
        except Exception as e:
            print("Error occured")
    


    async def stockUpdates(self,stocks):
        last_prices = {}
        while self.subscribed: 
            for stock in stocks:
                try:
                    ticker = yf.Ticker(stock)
                    info = ticker.info
                    # current_price = info.get('currentPrice')
                    # for testing use this to get  changing random data
                    current_price = generateRandomPrice()

                    previous_close = info.get('previousClose')
                    market_cap = info.get('marketCap')
                    pe_ratio = info.get('trailingPE')
                    high = info.get('dayHigh')
                    low = info.get('dayLow')
                    volume = info.get('volume')

                    if last_prices.get(stock) != current_price:
                        last_prices[stock] = current_price
                        await self.send(text_data=json.dumps({
                            'stock': stock,
                            'price': current_price,
                            'previous_close': previous_close,
                            'market_cap': market_cap,
                            'pe_ratio': pe_ratio,
                            'high': high,
                            'low': low,
                            'volume': volume,
                        }))

                    else:
                        pass

                except Exception as e:
                    await self.send(text_data=json.dumps({
                        'error': "Error Occured"
                    }))

            await asyncio.sleep(2)   # stops in seconds





    async def priceUpdates(self, stocks):
        last_prices = {}
        while self.subscribed: 
            for stock in stocks:
                try:
                    ticker = yf.Ticker(stock)
                    # current_price = ticker.info.get('currentPrice')
                    # for testing use this to get  changing random data
                    current_price = generateRandomPrice()

                    if last_prices.get(stock) != current_price:
                        last_prices[stock] = current_price
                        await self.send(text_data=json.dumps({
                            'stock': stock,
                            'price': current_price
                        }))
                    
                    else:
                        pass
                    
                except Exception as e:
                    await self.send(text_data=json.dumps({
                        'error': "Error Occured"
                    }))

            await asyncio.sleep(2)










#  by mqtt

# import time
# import yfinance as yf
# import paho.mqtt.client as mqtt



# def on_connect(client, userdata, flags, rc):
#     if rc == 0:
#         print("Connected Successfully")
#     else:
#         print(f"Connection failed with code {rc}")


# client = mqtt.Client()
# client.on_connect = on_connect

# client.connect("test.mosquitto.org", 1883, 60)
# client.loop_start()


# def getPrice(ticker):
#     try:
#         stock = yf.Ticker(ticker)
#         data = stock.history(period="1d")
#         if not data.empty:
#             return data['Close'].iloc[-1]
#         else:
#             print("Error Occured")
#             return None
#     except Exception as e:
#         print("Error occured")
#         return None



# def MonitoringChange(ticker, interval=60):
#     last_price = getPrice(ticker)
#     data = f"{ticker} = {last_price}"
#     print(data)
#     client.publish("stock/price/initial",str(data))

#     if last_price is None:
#         print("Unable to fetch")
#         return

#     while True:
#         time.sleep(interval)  
#         current_price = getPrice(ticker)
#         print("stock/price/curr" ,current_price)
#         client.publish("stock/price/curr" ,str(current_price))

#         if current_price is None:
#             continue

#         if current_price != last_price:
#             print(f"Price changed for {ticker} from {last_price} to {current_price}")
#             message = f"Stock {ticker} price changed: {current_price}"
#             print("stock/price/updated"+message)
#             client.publish("stock/price/updated",str(message))
#             last_price = current_price


# try:
#     MonitoringChange("AAPL", interval=60) 
# except KeyboardInterrupt:
#     print("Exit")
#     client.loop_stop()
#     client.disconnect()




