# BillingCreateSubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**plan_id** | **str** |  | [optional] 

## Example

```python
from sapliy_fintech.generated.models.billing_create_subscription_request import BillingCreateSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BillingCreateSubscriptionRequest from a JSON string
billing_create_subscription_request_instance = BillingCreateSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(BillingCreateSubscriptionRequest.to_json())

# convert the object into a dict
billing_create_subscription_request_dict = billing_create_subscription_request_instance.to_dict()
# create an instance of BillingCreateSubscriptionRequest from a dict
billing_create_subscription_request_from_dict = BillingCreateSubscriptionRequest.from_dict(billing_create_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


