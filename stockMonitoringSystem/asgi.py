import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from stock.routing import webUrls

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockMonitoringSystem.settings')

django.setup()

application = get_asgi_application()

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
   "websocket": AuthMiddlewareStack(
        URLRouter(
            webUrls
        )
   ),
})