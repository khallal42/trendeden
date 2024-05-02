"""
ASGI config for project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator

from chat import routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter({
    "http" : django_asgi_app,
    "websocket" : AllowedHostsOriginValidator(AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns)))
    
})