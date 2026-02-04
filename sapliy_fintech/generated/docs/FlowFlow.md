# FlowFlow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**zone_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**nodes_json** | **str** |  | [optional] 
**edges_json** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sapliy_fintech.generated.models.flow_flow import FlowFlow

# TODO update the JSON string below
json = "{}"
# create an instance of FlowFlow from a JSON string
flow_flow_instance = FlowFlow.from_json(json)
# print the JSON string representation of the object
print(FlowFlow.to_json())

# convert the object into a dict
flow_flow_dict = flow_flow_instance.to_dict()
# create an instance of FlowFlow from a dict
flow_flow_from_dict = FlowFlow.from_dict(flow_flow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


