# ZoneListZonesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zones** | [**List[ZoneZone]**](ZoneZone.md) |  | [optional] 

## Example

```python
from sapliy_fintech.generated.models.zone_list_zones_response import ZoneListZonesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneListZonesResponse from a JSON string
zone_list_zones_response_instance = ZoneListZonesResponse.from_json(json)
# print the JSON string representation of the object
print(ZoneListZonesResponse.to_json())

# convert the object into a dict
zone_list_zones_response_dict = zone_list_zones_response_instance.to_dict()
# create an instance of ZoneListZonesResponse from a dict
zone_list_zones_response_from_dict = ZoneListZonesResponse.from_dict(zone_list_zones_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


