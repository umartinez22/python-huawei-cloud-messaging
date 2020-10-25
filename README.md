# Python Huawei Cloud Messaging

Wrapper of huawei cloud messaging [(Push Kit)](https://developer.huawei.com/consumer/en/hms/huawei-pushkit/) for sending push notification using python.

## Home page

https://pypi.org/project/pyhcm/

## Install
```pip install pyhcm```

## Example

### Send notification to topic
```
CLIENT_ID = "00000000"
CLIENT_SECRET = "0000000000000000000000000000000000000000000000000000000000000000"

HCMNotification(CLIENT_ID, CLIENT_SECRET).notify_topic_subscribers('test_topic', 'test title', 'test body')
```

### Send notification to user

```
CLIENT_ID = "00000000"
CLIENT_SECRET = "0000000000000000000000000000000000000000000000000000000000000000"

HCMNotification(CLIENT_ID, CLIENT_SECRET).notify_single_device('token_xyz', 'test title', 'test body')
```