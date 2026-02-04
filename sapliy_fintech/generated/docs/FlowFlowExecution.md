# FlowFlowExecution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**flow_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**current_node_id** | **str** |  | [optional] 
**input_json** | **str** |  | [optional] 
**metadata_json** | **str** |  | [optional] 
**steps** | [**List[FlowExecutionStep]**](FlowExecutionStep.md) |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 

## Example

```python
from sapliy_fintech.generated.models.flow_flow_execution import FlowFlowExecution

# TODO update the JSON string below
json = "{}"
# create an instance of FlowFlowExecution from a JSON string
flow_flow_execution_instance = FlowFlowExecution.from_json(json)
# print the JSON string representation of the object
print(FlowFlowExecution.to_json())

# convert the object into a dict
flow_flow_execution_dict = flow_flow_execution_instance.to_dict()
# create an instance of FlowFlowExecution from a dict
flow_flow_execution_from_dict = FlowFlowExecution.from_dict(flow_flow_execution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


