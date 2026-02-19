# AutomationFlow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**org_id** | **str** |  | [optional] 
**zone_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**version** | **int** |  | [optional] 
**trigger** | [**AutomationFlowTrigger**](AutomationFlowTrigger.md) |  | [optional] 
**nodes** | [**List[AutomationFlowNode]**](AutomationFlowNode.md) |  | [optional] 
**edges** | [**List[AutomationFlowEdge]**](AutomationFlowEdge.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sapliyio_fintech.generated.models.automation_flow import AutomationFlow

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationFlow from a JSON string
automation_flow_instance = AutomationFlow.from_json(json)
# print the JSON string representation of the object
print(AutomationFlow.to_json())

# convert the object into a dict
automation_flow_dict = automation_flow_instance.to_dict()
# create an instance of AutomationFlow from a dict
automation_flow_from_dict = AutomationFlow.from_dict(automation_flow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


