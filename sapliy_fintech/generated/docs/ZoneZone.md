# ZoneZone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 
**secret_key** | **str** |  | [optional] 
**publishable_key** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**template_name** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**created_at** | **str** |  | [optional] 

## Example

```python
from sapliy_fintech.generated.models.zone_zone import ZoneZone

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneZone from a JSON string
zone_zone_instance = ZoneZone.from_json(json)
# print the JSON string representation of the object
print(ZoneZone.to_json())

# convert the object into a dict
zone_zone_dict = zone_zone_instance.to_dict()
# create an instance of ZoneZone from a dict
zone_zone_from_dict = ZoneZone.from_dict(zone_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


