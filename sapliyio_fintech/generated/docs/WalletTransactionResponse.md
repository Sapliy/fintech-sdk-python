# WalletTransactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from sapliyio_fintech.models.wallet_transaction_response import WalletTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WalletTransactionResponse from a JSON string
wallet_transaction_response_instance = WalletTransactionResponse.from_json(json)
# print the JSON string representation of the object
print(WalletTransactionResponse.to_json())

# convert the object into a dict
wallet_transaction_response_dict = wallet_transaction_response_instance.to_dict()
# create an instance of WalletTransactionResponse from a dict
wallet_transaction_response_from_dict = WalletTransactionResponse.from_dict(wallet_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


