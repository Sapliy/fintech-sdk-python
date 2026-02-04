# FlowExecutionStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**input_json** | **str** |  | [optional] 
**output_json** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**started_at** | **datetime** |  | [optional] 

## Example

```python
from sapliy_fintech.generated.models.flow_execution_step import FlowExecutionStep

# TODO update the JSON string below
json = "{}"
# create an instance of FlowExecutionStep from a JSON string
flow_execution_step_instance = FlowExecutionStep.from_json(json)
# print the JSON string representation of the object
print(FlowExecutionStep.to_json())

# convert the object into a dict
flow_execution_step_dict = flow_execution_step_instance.to_dict()
# create an instance of FlowExecutionStep from a dict
flow_execution_step_from_dict = FlowExecutionStep.from_dict(flow_execution_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


