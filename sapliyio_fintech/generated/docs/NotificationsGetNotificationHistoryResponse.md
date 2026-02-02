# NotificationsGetNotificationHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notifications** | [**List[NotificationsNotification]**](NotificationsNotification.md) |  | [optional] 

## Example

```python
from sapliyio_fintech.models.notifications_get_notification_history_response import NotificationsGetNotificationHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsGetNotificationHistoryResponse from a JSON string
notifications_get_notification_history_response_instance = NotificationsGetNotificationHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationsGetNotificationHistoryResponse.to_json())

# convert the object into a dict
notifications_get_notification_history_response_dict = notifications_get_notification_history_response_instance.to_dict()
# create an instance of NotificationsGetNotificationHistoryResponse from a dict
notifications_get_notification_history_response_from_dict = NotificationsGetNotificationHistoryResponse.from_dict(notifications_get_notification_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


