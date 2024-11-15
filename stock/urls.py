from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('subscribe',views.subscribe),
    path('update',views.update),
]