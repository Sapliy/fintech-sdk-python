# AutomationFlowNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**position** | **object** |  | [optional] 
**data** | **object** |  | [optional] 

## Example

```python
from sapliyio_fintech.generated.models.automation_flow_node import AutomationFlowNode

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationFlowNode from a JSON string
automation_flow_node_instance = AutomationFlowNode.from_json(json)
# print the JSON string representation of the object
print(AutomationFlowNode.to_json())

# convert the object into a dict
automation_flow_node_dict = automation_flow_node_instance.to_dict()
# create an instance of AutomationFlowNode from a dict
automation_flow_node_from_dict = AutomationFlowNode.from_dict(automation_flow_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


