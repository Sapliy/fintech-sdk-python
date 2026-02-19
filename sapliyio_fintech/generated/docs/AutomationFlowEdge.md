# AutomationFlowEdge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**source** | **str** |  | 
**target** | **str** |  | 
**source_handle** | **str** |  | [optional] 

## Example

```python
from sapliyio_fintech.generated.models.automation_flow_edge import AutomationFlowEdge

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationFlowEdge from a JSON string
automation_flow_edge_instance = AutomationFlowEdge.from_json(json)
# print the JSON string representation of the object
print(AutomationFlowEdge.to_json())

# convert the object into a dict
automation_flow_edge_dict = automation_flow_edge_instance.to_dict()
# create an instance of AutomationFlowEdge from a dict
automation_flow_edge_from_dict = AutomationFlowEdge.from_dict(automation_flow_edge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


