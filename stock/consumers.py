import json
from channels.generic.websocket import WebsocketConsumer

class stockMonitoring(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'message': 'Hello there! '
        }))
    
    def disconnect(self, close_code):
        pass
    
    def receive(self, text_data):
        pass