import time
import yfinance as yf
import paho.mqtt.client as mqtt



def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected Successfully")
    else:
        print(f"Connection failed with code {rc}")


client = mqtt.Client()
client.on_connect = on_connect

client.connect("test.mosquitto.org", 1883, 60)
client.loop_start()


# def on_publish(client, userdata, mid):
#     print(f"Message {mid} published successfully!")

# client.on_publish = on_publish




def getPrice(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")
        if not data.empty:
            return data['Close'].iloc[-1]
        else:
            print("Error Occured")
            return None
    except Exception as e:
        print("Error occured")
        return None



def MonitoringChange(ticker, interval=60):
    last_price = getPrice(ticker)
    data = f"{ticker} = {last_price}"
    print(data)
    client.publish("stock/price/initial",str(data))

    if last_price is None:
        print("Unable to fetch")
        return

    while True:
        time.sleep(interval)  
        current_price = getPrice(ticker)
        print("current_price =" ,current_price)
        client.publish("current_price =" ,str(current_price))

        if current_price is None:
            continue

        if current_price != last_price:
            print(f"Price changed for {ticker} from {last_price} to {current_price}")
            message = f"Stock {ticker} price changed: {current_price}"
            print("stock/price/updated"+message)
            client.publish("stock/price/updated",str(message))
            last_price = current_price


try:
    MonitoringChange("AAPL", interval=60) 
except KeyboardInterrupt:
    print("Exit")
    client.loop_stop()
    client.disconnect()





# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# # from asgiref.sync import async_to_sync
# # from channels.layers import get_channel_layer
# import time
# import yfinance as yf
# import asyncio



# class stockMonitoring(AsyncWebsocketConsumer):


#     async def connect(self):
#         await self.accept()
#         self.subsrcribed = False
#         await self.send(text_data=json.dumps({
#             'message': 'Hello there! '
#         }))




#     # when user send data
#     async def receive(self, text_data):
#         data = json.loads(text_data)


#         if data['action'] == 'subscribe':

#             if data['channel'] == 'stock_update' : 
#                 stocks = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS"]
#                 self.subscribed = True
#                 asyncio.create_task(self.priceUpdates(stocks))

                
#             elif data['channel'] == 'price_updates':
#                 stocks = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS"]
#                 self.subscribed = True
#                 asyncio.create_task(self.priceUpdates(stocks))


#             elif data['channel'] == 'new_product_arrivals':
#                 pass


#             elif data['channel'] == 'order_status_updates':
#                 pass
        


#         elif data['action'] == 'unsubscribe':
#             if data['channel'] == 'stock_update' : 
#                 self.subscribed=False
#                 await self.send(text_data=json.dumps({ 
#                     'message': 'unsubscribed successfully '
#                 }))



#         else:
#             await self.send(text_data=json.dumps({ 
#                     'message': 'please enter valid data'
#             }))




#     async def disconnect(self, close_code):
#         self.subscribed=False
#         print('disconnected')
    





#     async def priceUpdates(self, stocks):
#             last_prices = {}
#             while self.subscribed: 
#                 for stock in stocks:
#                     try:
#                         ticker = yf.Ticker(stock)
#                         current_price = ticker.info.get('currentPrice')

#                         if last_prices.get(stock) != current_price:
#                             last_prices[stock] = current_price
#                             await self.send(text_data=json.dumps({
#                                 'stock': stock,
#                                 'price': current_price,
#                                 "last_updated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
#                             }))
#                     except Exception as e:
#                         await self.send(text_data=json.dumps({
#                             'error': f"Failed to fetch data for {stock}: {str(e)}"
#                         }))

#                 await asyncio.sleep(10)


