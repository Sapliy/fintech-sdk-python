# WalletWallet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**balance** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from sapliy_fintech.generated.models.wallet_wallet import WalletWallet

# TODO update the JSON string below
json = "{}"
# create an instance of WalletWallet from a JSON string
wallet_wallet_instance = WalletWallet.from_json(json)
# print the JSON string representation of the object
print(WalletWallet.to_json())

# convert the object into a dict
wallet_wallet_dict = wallet_wallet_instance.to_dict()
# create an instance of WalletWallet from a dict
wallet_wallet_from_dict = WalletWallet.from_dict(wallet_wallet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


