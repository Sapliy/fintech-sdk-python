# V1AuthRegisterPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from sapliyio_fintech.generated.models.v1_auth_register_post_request import V1AuthRegisterPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1AuthRegisterPostRequest from a JSON string
v1_auth_register_post_request_instance = V1AuthRegisterPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1AuthRegisterPostRequest.to_json())

# convert the object into a dict
v1_auth_register_post_request_dict = v1_auth_register_post_request_instance.to_dict()
# create an instance of V1AuthRegisterPostRequest from a dict
v1_auth_register_post_request_from_dict = V1AuthRegisterPostRequest.from_dict(v1_auth_register_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


