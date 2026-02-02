# AuthValidateTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** |  | [optional] 
**client_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 
**expires_at** | **str** |  | [optional] 

## Example

```python
from sapliyio_fintech.models.auth_validate_token_response import AuthValidateTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthValidateTokenResponse from a JSON string
auth_validate_token_response_instance = AuthValidateTokenResponse.from_json(json)
# print the JSON string representation of the object
print(AuthValidateTokenResponse.to_json())

# convert the object into a dict
auth_validate_token_response_dict = auth_validate_token_response_instance.to_dict()
# create an instance of AuthValidateTokenResponse from a dict
auth_validate_token_response_from_dict = AuthValidateTokenResponse.from_dict(auth_validate_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


