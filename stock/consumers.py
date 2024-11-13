import json
from channels.generic.websocket import WebsocketConsumer




class stockMonitoring(WebsocketConsumer):


    def connect(self):
        #  accept accepts the request to connect
        self.accept()
        # text_data sends text data in response we also have bytes_data
        self.send(text_data=json.dumps({  # json dumps will convert dictionary to JSON
            'message': 'Hello there! '
        }))
    


    # when user send data
    def receive(self, text):
        pass



    def disconnect(self, close_code):
        # close_code return the code which can be used to return the message on disconnect
        pass
    