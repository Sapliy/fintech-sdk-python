# AutomationFlowTrigger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**event_type** | **str** |  | [optional] 
**config** | **object** |  | [optional] 

## Example

```python
from sapliyio_fintech.generated.models.automation_flow_trigger import AutomationFlowTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationFlowTrigger from a JSON string
automation_flow_trigger_instance = AutomationFlowTrigger.from_json(json)
# print the JSON string representation of the object
print(AutomationFlowTrigger.to_json())

# convert the object into a dict
automation_flow_trigger_dict = automation_flow_trigger_instance.to_dict()
# create an instance of AutomationFlowTrigger from a dict
automation_flow_trigger_from_dict = AutomationFlowTrigger.from_dict(automation_flow_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


