# NotificationsCreateWebhookEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**enabled_events** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from sapliyio_fintech.models.notifications_create_webhook_endpoint_request import NotificationsCreateWebhookEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsCreateWebhookEndpointRequest from a JSON string
notifications_create_webhook_endpoint_request_instance = NotificationsCreateWebhookEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationsCreateWebhookEndpointRequest.to_json())

# convert the object into a dict
notifications_create_webhook_endpoint_request_dict = notifications_create_webhook_endpoint_request_instance.to_dict()
# create an instance of NotificationsCreateWebhookEndpointRequest from a dict
notifications_create_webhook_endpoint_request_from_dict = NotificationsCreateWebhookEndpointRequest.from_dict(notifications_create_webhook_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


