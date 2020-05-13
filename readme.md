# Python Huawei Cloud Messaging

Wrapper of api push huawei for sending notification push using python.

## Example

### Subcribers topic
```
CLIENT_ID = "00000000"
CLIENT_SECRET = "0000000000000000000000000000000000000000000000000000000000000000"

HCMNotification(CLIENT_ID, CLIENT_SECRET).notify_topic_subscribers('test_topic', 'test title', 'test body')
```