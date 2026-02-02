# AuthInitiateSSORequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 

## Example

```python
from sapliy_fintech.models.auth_initiate_sso_request import AuthInitiateSSORequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthInitiateSSORequest from a JSON string
auth_initiate_sso_request_instance = AuthInitiateSSORequest.from_json(json)
# print the JSON string representation of the object
print(AuthInitiateSSORequest.to_json())

# convert the object into a dict
auth_initiate_sso_request_dict = auth_initiate_sso_request_instance.to_dict()
# create an instance of AuthInitiateSSORequest from a dict
auth_initiate_sso_request_from_dict = AuthInitiateSSORequest.from_dict(auth_initiate_sso_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


