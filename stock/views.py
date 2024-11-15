from django.shortcuts import render,HttpResponse
# from yahoo_fin.stock_info import *
import yfinance as yf





def home(request):
    return HttpResponse('Hello Welcome')



def subscribe(request):

    if request.method == 'GET':
        nifty50_tickers = [
                "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS",
            ]
        return render(request, 'subscribe.html',{'data':nifty50_tickers})
    
    if request.method == 'POST':
        pass



def update(request):
    s = request.GET.getlist('subscribe')
    print(s)
    stock = yf.Ticker('RELIANCE.NS')

    stock_info = stock.info
    current_price = stock_info.get("currentPrice")

    context = {
        "current_price": current_price,
    }
    print(context)
    return render(request,'stocks.html',context)

