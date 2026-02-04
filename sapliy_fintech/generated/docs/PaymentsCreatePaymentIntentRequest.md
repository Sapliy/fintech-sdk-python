# PaymentsCreatePaymentIntentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**application_fee_amount** | **str** |  | [optional] 
**on_behalf_of** | **str** |  | [optional] 

## Example

```python
from sapliy_fintech.generated.models.payments_create_payment_intent_request import PaymentsCreatePaymentIntentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentsCreatePaymentIntentRequest from a JSON string
payments_create_payment_intent_request_instance = PaymentsCreatePaymentIntentRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentsCreatePaymentIntentRequest.to_json())

# convert the object into a dict
payments_create_payment_intent_request_dict = payments_create_payment_intent_request_instance.to_dict()
# create an instance of PaymentsCreatePaymentIntentRequest from a dict
payments_create_payment_intent_request_from_dict = PaymentsCreatePaymentIntentRequest.from_dict(payments_create_payment_intent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


