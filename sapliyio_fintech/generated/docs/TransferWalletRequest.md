# TransferWalletRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_user_id** | **str** |  | 
**amount** | **int** |  | 
**currency** | **str** |  | 
**reference_id** | **str** |  | 

## Example

```python
from sapliyio_fintech.generated.models.transfer_wallet_request import TransferWalletRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransferWalletRequest from a JSON string
transfer_wallet_request_instance = TransferWalletRequest.from_json(json)
# print the JSON string representation of the object
print(TransferWalletRequest.to_json())

# convert the object into a dict
transfer_wallet_request_dict = transfer_wallet_request_instance.to_dict()
# create an instance of TransferWalletRequest from a dict
transfer_wallet_request_from_dict = TransferWalletRequest.from_dict(transfer_wallet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


