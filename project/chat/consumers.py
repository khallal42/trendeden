from channels.generic.websocket import WebsocketConsumer
from .models import *


class chatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
    def desconnect(self):
        pass
    def recieve(self, event):
        message = event.get("text")
        if message :
            send_msg = chat_mesg.objects.create(message=message)
            self.send({
                "type": "websocket.send",
                "text": send_msg.text,
            })
        
        