import json
from channels.generic.websocket import AsyncWebsocketConsumer
# from asgiref.sync import async_to_sync
# from channels.layers import get_channel_layer
import datetime
import yfinance as yf
import asyncio



class stockMonitoring(AsyncWebsocketConsumer):


    async def connect(self):
        await self.accept()
        self.subsrcribed = False
        await self.send(text_data=json.dumps({
            'message': 'Hello there! '
        }))





    # when user send data
    async def receive(self, text_data):
        data = json.loads(text_data)


        if data['action'] == 'subscribe':

            if data['channel'] == 'stock_update' : 
                stocks = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS"]
                self.subscribed = True
                asyncio.create_task(self.stockUpdates(stocks))

                
            elif data['channel'] == 'price_updates':
                stocks = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS"]
                self.subscribed = True
                asyncio.create_task(self.priceUpdates(stocks))


            elif data['channel'] == 'new_product_arrivals':
                pass
            elif data['channel'] == 'order_status_updates':
                pass
        

        elif data['action'] == 'unsubscribe':
            if data['channel'] == 'stock_update' : 
                self.subscribed=False
                await self.send(text_data=json.dumps({ 
                    'message': 'unsubscribed successfully '
                }))



        else:
            await self.send(text_data=json.dumps({ 
                    'message': 'please enter valid data'
            }))




    async def disconnect(self, close_code):
        self.subscribed=False
        print('disconnected')
    





    async def priceUpdates(self, stocks):
            last_prices = {}
            while self.subscribed: 
                for stock in stocks:
                    try:
                        ticker = yf.Ticker(stock)
                        current_price = ticker.info.get('currentPrice')

                        if last_prices.get(stock) != current_price:
                            last_prices[stock] = current_price
                            await self.send(text_data=json.dumps({
                                'stock': stock,
                                'price': current_price,
                                "last_updated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
                            }))
                    except Exception as e:
                        await self.send(text_data=json.dumps({
                            'error': f"Failed to fetch data for {stock}: {str(e)}"
                        }))

                await asyncio.sleep(10)