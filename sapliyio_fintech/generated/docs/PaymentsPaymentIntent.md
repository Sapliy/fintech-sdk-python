# PaymentsPaymentIntent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**application_fee_amount** | **str** |  | [optional] 
**on_behalf_of** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 

## Example

```python
from sapliyio_fintech.models.payments_payment_intent import PaymentsPaymentIntent

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentsPaymentIntent from a JSON string
payments_payment_intent_instance = PaymentsPaymentIntent.from_json(json)
# print the JSON string representation of the object
print(PaymentsPaymentIntent.to_json())

# convert the object into a dict
payments_payment_intent_dict = payments_payment_intent_instance.to_dict()
# create an instance of PaymentsPaymentIntent from a dict
payments_payment_intent_from_dict = PaymentsPaymentIntent.from_dict(payments_payment_intent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


