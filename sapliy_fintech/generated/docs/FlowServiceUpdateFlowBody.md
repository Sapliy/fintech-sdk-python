# FlowServiceUpdateFlowBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**nodes_json** | **str** |  | [optional] 
**edges_json** | **str** |  | [optional] 

## Example

```python
from sapliy_fintech.generated.models.flow_service_update_flow_body import FlowServiceUpdateFlowBody

# TODO update the JSON string below
json = "{}"
# create an instance of FlowServiceUpdateFlowBody from a JSON string
flow_service_update_flow_body_instance = FlowServiceUpdateFlowBody.from_json(json)
# print the JSON string representation of the object
print(FlowServiceUpdateFlowBody.to_json())

# convert the object into a dict
flow_service_update_flow_body_dict = flow_service_update_flow_body_instance.to_dict()
# create an instance of FlowServiceUpdateFlowBody from a dict
flow_service_update_flow_body_from_dict = FlowServiceUpdateFlowBody.from_dict(flow_service_update_flow_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


