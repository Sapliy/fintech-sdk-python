# WalletTopUpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**reference_id** | **str** |  | [optional] 

## Example

```python
from sapliy_fintech.models.wallet_top_up_request import WalletTopUpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WalletTopUpRequest from a JSON string
wallet_top_up_request_instance = WalletTopUpRequest.from_json(json)
# print the JSON string representation of the object
print(WalletTopUpRequest.to_json())

# convert the object into a dict
wallet_top_up_request_dict = wallet_top_up_request_instance.to_dict()
# create an instance of WalletTopUpRequest from a dict
wallet_top_up_request_from_dict = WalletTopUpRequest.from_dict(wallet_top_up_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


