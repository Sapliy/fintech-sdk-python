# AutomationFlowExecutionStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | 
**status** | **str** |  | 
**input** | **object** |  | [optional] 
**output** | **object** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from sapliyio_fintech.generated.models.automation_flow_execution_step import AutomationFlowExecutionStep

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationFlowExecutionStep from a JSON string
automation_flow_execution_step_instance = AutomationFlowExecutionStep.from_json(json)
# print the JSON string representation of the object
print(AutomationFlowExecutionStep.to_json())

# convert the object into a dict
automation_flow_execution_step_dict = automation_flow_execution_step_instance.to_dict()
# create an instance of AutomationFlowExecutionStep from a dict
automation_flow_execution_step_from_dict = AutomationFlowExecutionStep.from_dict(automation_flow_execution_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


