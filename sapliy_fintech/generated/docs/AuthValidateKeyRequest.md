# AuthValidateKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_hash** | **str** |  | [optional] 

## Example

```python
from sapliy_fintech.models.auth_validate_key_request import AuthValidateKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthValidateKeyRequest from a JSON string
auth_validate_key_request_instance = AuthValidateKeyRequest.from_json(json)
# print the JSON string representation of the object
print(AuthValidateKeyRequest.to_json())

# convert the object into a dict
auth_validate_key_request_dict = auth_validate_key_request_instance.to_dict()
# create an instance of AuthValidateKeyRequest from a dict
auth_validate_key_request_from_dict = AuthValidateKeyRequest.from_dict(auth_validate_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


