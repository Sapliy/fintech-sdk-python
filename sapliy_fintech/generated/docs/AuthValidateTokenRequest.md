# AuthValidateTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 

## Example

```python
from sapliy_fintech.models.auth_validate_token_request import AuthValidateTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthValidateTokenRequest from a JSON string
auth_validate_token_request_instance = AuthValidateTokenRequest.from_json(json)
# print the JSON string representation of the object
print(AuthValidateTokenRequest.to_json())

# convert the object into a dict
auth_validate_token_request_dict = auth_validate_token_request_instance.to_dict()
# create an instance of AuthValidateTokenRequest from a dict
auth_validate_token_request_from_dict = AuthValidateTokenRequest.from_dict(auth_validate_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


