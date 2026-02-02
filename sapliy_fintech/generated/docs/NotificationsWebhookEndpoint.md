# NotificationsWebhookEndpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**enabled_events** | **List[str]** |  | [optional] 
**secret** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 

## Example

```python
from sapliy_fintech.models.notifications_webhook_endpoint import NotificationsWebhookEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsWebhookEndpoint from a JSON string
notifications_webhook_endpoint_instance = NotificationsWebhookEndpoint.from_json(json)
# print the JSON string representation of the object
print(NotificationsWebhookEndpoint.to_json())

# convert the object into a dict
notifications_webhook_endpoint_dict = notifications_webhook_endpoint_instance.to_dict()
# create an instance of NotificationsWebhookEndpoint from a dict
notifications_webhook_endpoint_from_dict = NotificationsWebhookEndpoint.from_dict(notifications_webhook_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


