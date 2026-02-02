# WalletCreateWalletRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from sapliy_fintech.models.wallet_create_wallet_request import WalletCreateWalletRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WalletCreateWalletRequest from a JSON string
wallet_create_wallet_request_instance = WalletCreateWalletRequest.from_json(json)
# print the JSON string representation of the object
print(WalletCreateWalletRequest.to_json())

# convert the object into a dict
wallet_create_wallet_request_dict = wallet_create_wallet_request_instance.to_dict()
# create an instance of WalletCreateWalletRequest from a dict
wallet_create_wallet_request_from_dict = WalletCreateWalletRequest.from_dict(wallet_create_wallet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


