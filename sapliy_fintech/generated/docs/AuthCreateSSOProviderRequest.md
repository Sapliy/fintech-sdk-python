# AuthCreateSSOProviderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**provider_type** | **str** |  | [optional] 
**issuer_url** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 

## Example

```python
from sapliy_fintech.generated.models.auth_create_sso_provider_request import AuthCreateSSOProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthCreateSSOProviderRequest from a JSON string
auth_create_sso_provider_request_instance = AuthCreateSSOProviderRequest.from_json(json)
# print the JSON string representation of the object
print(AuthCreateSSOProviderRequest.to_json())

# convert the object into a dict
auth_create_sso_provider_request_dict = auth_create_sso_provider_request_instance.to_dict()
# create an instance of AuthCreateSSOProviderRequest from a dict
auth_create_sso_provider_request_from_dict = AuthCreateSSOProviderRequest.from_dict(auth_create_sso_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


