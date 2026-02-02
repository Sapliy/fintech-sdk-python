# AuthSSOProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**provider_type** | **str** |  | [optional] 
**issuer_url** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from sapliyio_fintech.models.auth_sso_provider import AuthSSOProvider

# TODO update the JSON string below
json = "{}"
# create an instance of AuthSSOProvider from a JSON string
auth_sso_provider_instance = AuthSSOProvider.from_json(json)
# print the JSON string representation of the object
print(AuthSSOProvider.to_json())

# convert the object into a dict
auth_sso_provider_dict = auth_sso_provider_instance.to_dict()
# create an instance of AuthSSOProvider from a dict
auth_sso_provider_from_dict = AuthSSOProvider.from_dict(auth_sso_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


