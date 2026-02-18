# FlowExecution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**flow_id** | **str** |  | 
**flow_version** | **int** |  | [optional] 
**trigger_id** | **str** |  | [optional] 
**status** | **str** |  | 
**current_node_id** | **str** |  | [optional] 
**input** | **object** |  | [optional] 
**output** | **object** |  | [optional] 
**steps** | [**List[ExecutionStep]**](ExecutionStep.md) |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**ended_at** | **datetime** |  | [optional] 

## Example

```python
from sapliyio_fintech.generated.models.flow_execution import FlowExecution

# TODO update the JSON string below
json = "{}"
# create an instance of FlowExecution from a JSON string
flow_execution_instance = FlowExecution.from_json(json)
# print the JSON string representation of the object
print(FlowExecution.to_json())

# convert the object into a dict
flow_execution_dict = flow_execution_instance.to_dict()
# create an instance of FlowExecution from a dict
flow_execution_from_dict = FlowExecution.from_dict(flow_execution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


