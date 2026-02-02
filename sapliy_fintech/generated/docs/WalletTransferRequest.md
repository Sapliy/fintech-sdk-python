# WalletTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_user_id** | **str** |  | [optional] 
**to_user_id** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**reference_id** | **str** |  | [optional] 

## Example

```python
from sapliy_fintech.models.wallet_transfer_request import WalletTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WalletTransferRequest from a JSON string
wallet_transfer_request_instance = WalletTransferRequest.from_json(json)
# print the JSON string representation of the object
print(WalletTransferRequest.to_json())

# convert the object into a dict
wallet_transfer_request_dict = wallet_transfer_request_instance.to_dict()
# create an instance of WalletTransferRequest from a dict
wallet_transfer_request_from_dict = WalletTransferRequest.from_dict(wallet_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


