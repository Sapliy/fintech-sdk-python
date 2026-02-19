# AutomationFlowExecution


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
**steps** | [**List[AutomationFlowExecutionStep]**](AutomationFlowExecutionStep.md) |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**ended_at** | **datetime** |  | [optional] 

## Example

```python
from sapliyio_fintech.generated.models.automation_flow_execution import AutomationFlowExecution

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationFlowExecution from a JSON string
automation_flow_execution_instance = AutomationFlowExecution.from_json(json)
# print the JSON string representation of the object
print(AutomationFlowExecution.to_json())

# convert the object into a dict
automation_flow_execution_dict = automation_flow_execution_instance.to_dict()
# create an instance of AutomationFlowExecution from a dict
automation_flow_execution_from_dict = AutomationFlowExecution.from_dict(automation_flow_execution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


