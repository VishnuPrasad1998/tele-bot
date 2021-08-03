import json
from channels.generic.websocket import WebsocketConsumer
from .views import respond_to_websockets
from .models import Buttonhits
from django.contrib.auth.models import User

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if text_data_json['command'] == "start":
            global id 
            id = text_data_json['user_id']
            self.start("")
        elif text_data_json['command'] == "send":
            text = text_data_json['text']
            try:
                hits = Buttonhits.objects.get(user=id)
            except:
                hits = None
            if not hits:
                user = User(id=id)
                new_hit = Buttonhits(user=user)
                new_hit.save()
                hits = Buttonhits.objects.get(user=id)
            
            fat_hits = hits.fat_hits
            dumb_hits = hits.dumb_hits
            stupid_hits = hits.dumb_hits
            if text == "fat":
                fat_hits = fat_hits + 1
                Buttonhits.objects.filter(user=id).update(fat_hits=fat_hits)
            elif text == "dumb":
                dumb_hits = dumb_hits + 1
                Buttonhits.objects.filter(user=id).update(dumb_hits=dumb_hits)
            elif text == "stupid":
                stupid_hits = stupid_hits + 1
                Buttonhits.objects.filter(user=id).update(stupid_hits=stupid_hits)
            self.chat_send(text)

    def start(self, message):
        pass

    def chat_leave(self, message):
        pass

    def chat_send(self, message):
        message_to_send_content = {
            'text': message,
            'type': 'text',
            'source': 'CANDIDATE'
        }
        self.send(json.dumps(message_to_send_content))
        response = respond_to_websockets(
            message_to_send_content
        )
        response['source'] = 'BOT'
        self.send(json.dumps(response))
