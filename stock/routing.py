from django.urls import re_path
from .consumers import stockMonitoring

websocket_urlpatterns = [
    re_path(r'ws/somepath/', stockMonitoring.as_asgi()),
]