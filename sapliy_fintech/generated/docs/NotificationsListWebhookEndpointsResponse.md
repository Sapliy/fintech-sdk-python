# NotificationsListWebhookEndpointsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoints** | [**List[NotificationsWebhookEndpoint]**](NotificationsWebhookEndpoint.md) |  | [optional] 

## Example

```python
from sapliy_fintech.models.notifications_list_webhook_endpoints_response import NotificationsListWebhookEndpointsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsListWebhookEndpointsResponse from a JSON string
notifications_list_webhook_endpoints_response_instance = NotificationsListWebhookEndpointsResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationsListWebhookEndpointsResponse.to_json())

# convert the object into a dict
notifications_list_webhook_endpoints_response_dict = notifications_list_webhook_endpoints_response_instance.to_dict()
# create an instance of NotificationsListWebhookEndpointsResponse from a dict
notifications_list_webhook_endpoints_response_from_dict = NotificationsListWebhookEndpointsResponse.from_dict(notifications_list_webhook_endpoints_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


