# CreateZoneRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** |  | 
**name** | **str** |  | 
**mode** | **str** |  | 
**template_name** | **str** |  | [optional] 

## Example

```python
from sapliyio_fintech.generated.models.create_zone_request import CreateZoneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateZoneRequest from a JSON string
create_zone_request_instance = CreateZoneRequest.from_json(json)
# print the JSON string representation of the object
print(CreateZoneRequest.to_json())

# convert the object into a dict
create_zone_request_dict = create_zone_request_instance.to_dict()
# create an instance of CreateZoneRequest from a dict
create_zone_request_from_dict = CreateZoneRequest.from_dict(create_zone_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


