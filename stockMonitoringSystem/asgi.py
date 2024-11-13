import os

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from stock.routing import websocket_urlpatterns

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockMonitoringSystem.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter({
  "http": get_asgi_application(),
   "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
   ),
})