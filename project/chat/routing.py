from django.urls import path
from .consumers import *
from .consumers import *

websocket_urlpatterns = [
    path("chat/", chatConsumer.as_asgi()),
]