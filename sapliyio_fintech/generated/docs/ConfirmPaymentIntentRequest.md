# ConfirmPaymentIntentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method_id** | **str** |  | [optional] 

## Example

```python
from sapliyio_fintech.generated.models.confirm_payment_intent_request import ConfirmPaymentIntentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmPaymentIntentRequest from a JSON string
confirm_payment_intent_request_instance = ConfirmPaymentIntentRequest.from_json(json)
# print the JSON string representation of the object
print(ConfirmPaymentIntentRequest.to_json())

# convert the object into a dict
confirm_payment_intent_request_dict = confirm_payment_intent_request_instance.to_dict()
# create an instance of ConfirmPaymentIntentRequest from a dict
confirm_payment_intent_request_from_dict = ConfirmPaymentIntentRequest.from_dict(confirm_payment_intent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


