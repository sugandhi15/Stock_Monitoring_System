from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    # path('subscribe',views.subscribe),
    # path('update',views.update),
]