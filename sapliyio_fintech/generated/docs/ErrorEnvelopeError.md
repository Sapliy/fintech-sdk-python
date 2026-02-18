# ErrorEnvelopeError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**message** | **str** |  | 
**request_id** | **str** |  | [optional] 
**trace_id** | **str** |  | [optional] 

## Example

```python
from sapliyio_fintech.generated.models.error_envelope_error import ErrorEnvelopeError

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorEnvelopeError from a JSON string
error_envelope_error_instance = ErrorEnvelopeError.from_json(json)
# print the JSON string representation of the object
print(ErrorEnvelopeError.to_json())

# convert the object into a dict
error_envelope_error_dict = error_envelope_error_instance.to_dict()
# create an instance of ErrorEnvelopeError from a dict
error_envelope_error_from_dict = ErrorEnvelopeError.from_dict(error_envelope_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


