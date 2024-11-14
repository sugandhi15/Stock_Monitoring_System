from django.shortcuts import render,HttpResponse
# from yahoo_fin.stock_info import *
import yfinance as yf

# Create your views here.
def home(request):
    return HttpResponse('Hello Welcome')

# def subscribe(request):
#     # data = tickers_nifty50()
#     nifty50_tickers = [
#             "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS",
#         ]
#     data = {ticker: yf.Ticker(ticker).info for ticker in nifty50_tickers}
#     print(data)
#     return render(request, 'subscribe.html',{'data':nifty50_tickers})

# def update(request):
#     stock = yf.Ticker('RELIANCE.NS')

#     stock_info = stock.info
#     current_price = stock_info.get("currentPrice")

#     # Pass this data to the template for display
#     context = {
#         # "stock":"RELIANCE.NS",
#         "current_price": current_price,
#     }
#     print(context)
#     return render(request,'stocks.html',context)
