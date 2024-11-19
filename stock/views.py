from django.shortcuts import render,HttpResponse
# from yahoo_fin.stock_info import *
import yfinance as yf
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from rest_framework.response import Response



def home(request):
    return HttpResponse('Hello Welcome')



class signup(APIView):
    permission_classes = (AllowAny,)

    def post(self,request):
        try:
            username = request.data['username']
            password = request.data['password']
            email = request.data['email']
            data = {
                'username': username,
                'password': password,
                'email': email,
            }
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "msg": "Signed up successfully"
                })
            else:
                return Response({
                    "msg":"error occured"
                })
            
        except Exception as e:
            return Response({
                "msg":str(e)
            })


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

