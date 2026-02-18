# V1WalletsTopupPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | 
**currency** | **str** |  | 
**reference_id** | **str** |  | 

## Example

```python
from sapliyio_fintech.generated.models.v1_wallets_topup_post_request import V1WalletsTopupPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1WalletsTopupPostRequest from a JSON string
v1_wallets_topup_post_request_instance = V1WalletsTopupPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1WalletsTopupPostRequest.to_json())

# convert the object into a dict
v1_wallets_topup_post_request_dict = v1_wallets_topup_post_request_instance.to_dict()
# create an instance of V1WalletsTopupPostRequest from a dict
v1_wallets_topup_post_request_from_dict = V1WalletsTopupPostRequest.from_dict(v1_wallets_topup_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


