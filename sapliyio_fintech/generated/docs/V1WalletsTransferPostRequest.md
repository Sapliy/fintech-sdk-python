# V1WalletsTransferPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_user_id** | **str** |  | 
**amount** | **int** |  | 
**currency** | **str** |  | 
**reference_id** | **str** |  | 

## Example

```python
from sapliyio_fintech.generated.models.v1_wallets_transfer_post_request import V1WalletsTransferPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1WalletsTransferPostRequest from a JSON string
v1_wallets_transfer_post_request_instance = V1WalletsTransferPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1WalletsTransferPostRequest.to_json())

# convert the object into a dict
v1_wallets_transfer_post_request_dict = v1_wallets_transfer_post_request_instance.to_dict()
# create an instance of V1WalletsTransferPostRequest from a dict
v1_wallets_transfer_post_request_from_dict = V1WalletsTransferPostRequest.from_dict(v1_wallets_transfer_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


