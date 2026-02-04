# FlowCreateFlowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**nodes_json** | **str** |  | [optional] 
**edges_json** | **str** |  | [optional] 

## Example

```python
from sapliy_fintech.generated.models.flow_create_flow_request import FlowCreateFlowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowCreateFlowRequest from a JSON string
flow_create_flow_request_instance = FlowCreateFlowRequest.from_json(json)
# print the JSON string representation of the object
print(FlowCreateFlowRequest.to_json())

# convert the object into a dict
flow_create_flow_request_dict = flow_create_flow_request_instance.to_dict()
# create an instance of FlowCreateFlowRequest from a dict
flow_create_flow_request_from_dict = FlowCreateFlowRequest.from_dict(flow_create_flow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


