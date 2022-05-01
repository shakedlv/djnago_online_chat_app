from email import message
import json
from msilib import text
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.utils.timezone import datetime


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

        self.send(text_data=json.dumps({
            'type':'connection_established',
            'message':'You are now connected!',
            'date': time
        }))

    
    
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        time = text_data_json['date']
        usercode = text_data_json['usercode']
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'date': time,
                'usercode':usercode
            }
        )

    def chat_message(self, event):
        message = event['message']
        time = event['date']
        usercode = event['usercode']

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            'date': time,
            'usercode':usercode
        }))