# V1AuthRegisterPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 

## Example

```python
from sapliyio_fintech.generated.models.v1_auth_register_post201_response import V1AuthRegisterPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1AuthRegisterPost201Response from a JSON string
v1_auth_register_post201_response_instance = V1AuthRegisterPost201Response.from_json(json)
# print the JSON string representation of the object
print(V1AuthRegisterPost201Response.to_json())

# convert the object into a dict
v1_auth_register_post201_response_dict = v1_auth_register_post201_response_instance.to_dict()
# create an instance of V1AuthRegisterPost201Response from a dict
v1_auth_register_post201_response_from_dict = V1AuthRegisterPost201Response.from_dict(v1_auth_register_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


