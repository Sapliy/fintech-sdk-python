# PaymentServiceConfirmPaymentIntentBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method_id** | **str** |  | [optional] 

## Example

```python
from sapliy_fintech.models.payment_service_confirm_payment_intent_body import PaymentServiceConfirmPaymentIntentBody

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentServiceConfirmPaymentIntentBody from a JSON string
payment_service_confirm_payment_intent_body_instance = PaymentServiceConfirmPaymentIntentBody.from_json(json)
# print the JSON string representation of the object
print(PaymentServiceConfirmPaymentIntentBody.to_json())

# convert the object into a dict
payment_service_confirm_payment_intent_body_dict = payment_service_confirm_payment_intent_body_instance.to_dict()
# create an instance of PaymentServiceConfirmPaymentIntentBody from a dict
payment_service_confirm_payment_intent_body_from_dict = PaymentServiceConfirmPaymentIntentBody.from_dict(payment_service_confirm_payment_intent_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


