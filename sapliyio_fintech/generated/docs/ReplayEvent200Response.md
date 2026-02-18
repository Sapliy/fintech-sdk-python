# ReplayEvent200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**event_id** | **str** |  | [optional] 
**original_id** | **str** |  | [optional] 

## Example

```python
from sapliyio_fintech.generated.models.replay_event200_response import ReplayEvent200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReplayEvent200Response from a JSON string
replay_event200_response_instance = ReplayEvent200Response.from_json(json)
# print the JSON string representation of the object
print(ReplayEvent200Response.to_json())

# convert the object into a dict
replay_event200_response_dict = replay_event200_response_instance.to_dict()
# create an instance of ReplayEvent200Response from a dict
replay_event200_response_from_dict = ReplayEvent200Response.from_dict(replay_event200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


