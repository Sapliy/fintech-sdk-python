# EmitEvent202Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from sapliyio_fintech.generated.models.emit_event202_response import EmitEvent202Response

# TODO update the JSON string below
json = "{}"
# create an instance of EmitEvent202Response from a JSON string
emit_event202_response_instance = EmitEvent202Response.from_json(json)
# print the JSON string representation of the object
print(EmitEvent202Response.to_json())

# convert the object into a dict
emit_event202_response_dict = emit_event202_response_instance.to_dict()
# create an instance of EmitEvent202Response from a dict
emit_event202_response_from_dict = EmitEvent202Response.from_dict(emit_event202_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


