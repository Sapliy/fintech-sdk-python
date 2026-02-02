# BillingListSubscriptionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscriptions** | [**List[BillingSubscription]**](BillingSubscription.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from sapliyio_fintech.models.billing_list_subscriptions_response import BillingListSubscriptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BillingListSubscriptionsResponse from a JSON string
billing_list_subscriptions_response_instance = BillingListSubscriptionsResponse.from_json(json)
# print the JSON string representation of the object
print(BillingListSubscriptionsResponse.to_json())

# convert the object into a dict
billing_list_subscriptions_response_dict = billing_list_subscriptions_response_instance.to_dict()
# create an instance of BillingListSubscriptionsResponse from a dict
billing_list_subscriptions_response_from_dict = BillingListSubscriptionsResponse.from_dict(billing_list_subscriptions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


