# EmitEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**data** | **object** |  | [optional] 
**idempotency_key** | **str** |  | [optional] 

## Example

```python
from sapliyio_fintech.generated.models.emit_event_request import EmitEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmitEventRequest from a JSON string
emit_event_request_instance = EmitEventRequest.from_json(json)
# print the JSON string representation of the object
print(EmitEventRequest.to_json())

# convert the object into a dict
emit_event_request_dict = emit_event_request_instance.to_dict()
# create an instance of EmitEventRequest from a dict
emit_event_request_from_dict = EmitEventRequest.from_dict(emit_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


