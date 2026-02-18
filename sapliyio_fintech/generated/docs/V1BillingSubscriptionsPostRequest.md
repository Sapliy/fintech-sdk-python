# V1BillingSubscriptionsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **str** |  | 
**customer_id** | **str** |  | [optional] 

## Example

```python
from sapliyio_fintech.generated.models.v1_billing_subscriptions_post_request import V1BillingSubscriptionsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1BillingSubscriptionsPostRequest from a JSON string
v1_billing_subscriptions_post_request_instance = V1BillingSubscriptionsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1BillingSubscriptionsPostRequest.to_json())

# convert the object into a dict
v1_billing_subscriptions_post_request_dict = v1_billing_subscriptions_post_request_instance.to_dict()
# create an instance of V1BillingSubscriptionsPostRequest from a dict
v1_billing_subscriptions_post_request_from_dict = V1BillingSubscriptionsPostRequest.from_dict(v1_billing_subscriptions_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


