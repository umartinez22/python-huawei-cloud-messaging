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

    def _build_notification_payload(
            self, topic: str, token: str, title: str, message_body: str):
        return {
            'message': {
                'topic': topic,
                'token': [token] if token is not None else None,
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

    def _send_notification_request(self, payload: object):
        request = Request(
            self.url_push,
            data=json.dumps(payload).encode(),
            headers={"Content-type": "application/json",
                     "Authorization": f'Bearer {self.get_access_token()}'}
        )
        response = json.loads(urlopen(request).read())
        return response['msg'].lower() == 'success'

    def notify_topic_subscribers(
            self, topic: str, title: str, message_body: str):
        payload = self._build_notification_payload(
            topic, None, title, message_body)
        return self._send_notification_request(payload)

    def notify_single_device(self, token: str, title: str, message_body: str):
        payload = self._build_notification_payload(
            None, token, title, message_body)
        return self._send_notification_request(payload)
