# ZoneCreateZoneRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 
**template_name** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sapliy_fintech.generated.models.zone_create_zone_request import ZoneCreateZoneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneCreateZoneRequest from a JSON string
zone_create_zone_request_instance = ZoneCreateZoneRequest.from_json(json)
# print the JSON string representation of the object
print(ZoneCreateZoneRequest.to_json())

# convert the object into a dict
zone_create_zone_request_dict = zone_create_zone_request_instance.to_dict()
# create an instance of ZoneCreateZoneRequest from a dict
zone_create_zone_request_from_dict = ZoneCreateZoneRequest.from_dict(zone_create_zone_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


