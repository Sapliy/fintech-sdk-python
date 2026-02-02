# AuthInitiateSSOResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_url** | **str** |  | [optional] 

## Example

```python
from sapliy_fintech.models.auth_initiate_sso_response import AuthInitiateSSOResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthInitiateSSOResponse from a JSON string
auth_initiate_sso_response_instance = AuthInitiateSSOResponse.from_json(json)
# print the JSON string representation of the object
print(AuthInitiateSSOResponse.to_json())

# convert the object into a dict
auth_initiate_sso_response_dict = auth_initiate_sso_response_instance.to_dict()
# create an instance of AuthInitiateSSOResponse from a dict
auth_initiate_sso_response_from_dict = AuthInitiateSSOResponse.from_dict(auth_initiate_sso_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


