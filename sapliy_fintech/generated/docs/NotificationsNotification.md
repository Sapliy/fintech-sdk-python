# NotificationsNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**recipient** | **str** |  | [optional] 
**channel** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**sent_at** | **str** |  | [optional] 

## Example

```python
from sapliy_fintech.models.notifications_notification import NotificationsNotification

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsNotification from a JSON string
notifications_notification_instance = NotificationsNotification.from_json(json)
# print the JSON string representation of the object
print(NotificationsNotification.to_json())

# convert the object into a dict
notifications_notification_dict = notifications_notification_instance.to_dict()
# create an instance of NotificationsNotification from a dict
notifications_notification_from_dict = NotificationsNotification.from_dict(notifications_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


