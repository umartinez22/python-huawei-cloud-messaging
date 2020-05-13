from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode
import json


class HCMNotification:

    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.url_auth = 'https://oauth-login.cloud.huawei.com/oauth2/v2/token'
        self.url_push = f'https://push-api.cloud.huawei.com/v1/{client_id}/messages:send'

    def get_access_token(self):
        request = Request(
            self.url_auth,
            data=urlencode({"grant_type": "client_credentials", "client_id": self.client_id,
                            "client_secret": self.client_secret}).encode(),
            headers={"Content-type": "application/x-www-form-urlencoded"}
        )
        return json.loads(urlopen(request).read())['access_token']

    def notify_topic_subscribers(self, topic: str, title: str, message_body: str):
        payload = {
            'message': {
                'topic': topic,
                'android': {
                    'notification': {
                        'title': title,
                        'body': message_body,
                        'click_action': {
                            'type': 3
                        }
                    }
                }
            }
        }

        request = Request(
            self.url_push,
            data=json.dumps(payload).encode(),
            headers={"Content-type": "application/json",
                     "Authorization": f'Bearer {self.get_access_token()}'}
        )
        response = json.loads(urlopen(request).read())
        
        return response['msg'] == 'Success'
