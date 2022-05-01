import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import main.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_project.settings")

application = ProtocolTypeRouter({
  'http': get_asgi_application(),
  'websocket': AuthMiddlewareStack(
      URLRouter(
          main.routing.websocket_urlpatterns
      )
  )
})