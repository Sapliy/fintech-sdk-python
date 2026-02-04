# ZoneServiceUpdateZoneBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sapliy_fintech.generated.models.zone_service_update_zone_body import ZoneServiceUpdateZoneBody

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneServiceUpdateZoneBody from a JSON string
zone_service_update_zone_body_instance = ZoneServiceUpdateZoneBody.from_json(json)
# print the JSON string representation of the object
print(ZoneServiceUpdateZoneBody.to_json())

# convert the object into a dict
zone_service_update_zone_body_dict = zone_service_update_zone_body_instance.to_dict()
# create an instance of ZoneServiceUpdateZoneBody from a dict
zone_service_update_zone_body_from_dict = ZoneServiceUpdateZoneBody.from_dict(zone_service_update_zone_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


