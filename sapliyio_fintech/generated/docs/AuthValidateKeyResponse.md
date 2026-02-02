# AuthValidateKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** |  | [optional] 
**user_id** | **str** |  | [optional] 
**environment** | **str** |  | [optional] 
**scopes** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**rate_limit_quota** | **int** |  | [optional] 

## Example

```python
from sapliyio_fintech.models.auth_validate_key_response import AuthValidateKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthValidateKeyResponse from a JSON string
auth_validate_key_response_instance = AuthValidateKeyResponse.from_json(json)
# print the JSON string representation of the object
print(AuthValidateKeyResponse.to_json())

# convert the object into a dict
auth_validate_key_response_dict = auth_validate_key_response_instance.to_dict()
# create an instance of AuthValidateKeyResponse from a dict
auth_validate_key_response_from_dict = AuthValidateKeyResponse.from_dict(auth_validate_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


