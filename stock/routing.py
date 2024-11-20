from django.urls import re_path
from .consumers import stockMonitoring

webUrls = [
    re_path(r'ws/stock', stockMonitoring.as_asgi()),
]