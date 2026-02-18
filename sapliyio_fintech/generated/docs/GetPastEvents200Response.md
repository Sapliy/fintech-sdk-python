# GetPastEvents200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | **List[object]** |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 

## Example

```python
from sapliyio_fintech.generated.models.get_past_events200_response import GetPastEvents200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPastEvents200Response from a JSON string
get_past_events200_response_instance = GetPastEvents200Response.from_json(json)
# print the JSON string representation of the object
print(GetPastEvents200Response.to_json())

# convert the object into a dict
get_past_events200_response_dict = get_past_events200_response_instance.to_dict()
# create an instance of GetPastEvents200Response from a dict
get_past_events200_response_from_dict = GetPastEvents200Response.from_dict(get_past_events200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


