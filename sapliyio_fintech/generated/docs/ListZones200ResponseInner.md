# ListZones200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from sapliyio_fintech.generated.models.list_zones200_response_inner import ListZones200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListZones200ResponseInner from a JSON string
list_zones200_response_inner_instance = ListZones200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListZones200ResponseInner.to_json())

# convert the object into a dict
list_zones200_response_inner_dict = list_zones200_response_inner_instance.to_dict()
# create an instance of ListZones200ResponseInner from a dict
list_zones200_response_inner_from_dict = ListZones200ResponseInner.from_dict(list_zones200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


