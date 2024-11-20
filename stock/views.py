from django.shortcuts import render,HttpResponse,redirect
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

    def get(self,request):
            return render(request,'signup.html')

    def post(self,request):
        try:
            # username = request.data['username']
            # password = request.data['password']
            # email = request.data['email']
            # data = {
            #     'username': username,
            #     'password': password,
            #     'email': email,
            # }
            print("working")
            serializer = UserSerializer(data=request.data)
            print(serializer)
            if serializer.is_valid():
                print("validated")
                serializer.save()
                # return HttpResponse("Signed up successfully")
                return redirect("https://stock-monitoring-system.onrender.com/login/")
            else:
                return Response({
                    "msg":"Please enter valid data"
                })
            
        except Exception as e:
            return Response({
                "msg":str(e)
            })




def chart(request):
    token  = request.GET.get('token')
    if token:
        if request.method == 'GET':
                return render(request, 'chart.html',{"token":token})
        else:
            return Response({
                "message":"Error occured"
        })
    else:
        return Response({
            "message":"please pass jwt token as query parameter"
        })


