# ValidateKey200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** |  | [optional] 
**user_id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**environment** | **str** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 

## Example

```python
from sapliyio_fintech.generated.models.validate_key200_response import ValidateKey200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateKey200Response from a JSON string
validate_key200_response_instance = ValidateKey200Response.from_json(json)
# print the JSON string representation of the object
print(ValidateKey200Response.to_json())

# convert the object into a dict
validate_key200_response_dict = validate_key200_response_instance.to_dict()
# create an instance of ValidateKey200Response from a dict
validate_key200_response_from_dict = ValidateKey200Response.from_dict(validate_key200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


