# FlowListFlowsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flows** | [**List[FlowFlow]**](FlowFlow.md) |  | [optional] 

## Example

```python
from sapliy_fintech.generated.models.flow_list_flows_response import FlowListFlowsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlowListFlowsResponse from a JSON string
flow_list_flows_response_instance = FlowListFlowsResponse.from_json(json)
# print the JSON string representation of the object
print(FlowListFlowsResponse.to_json())

# convert the object into a dict
flow_list_flows_response_dict = flow_list_flows_response_instance.to_dict()
# create an instance of FlowListFlowsResponse from a dict
flow_list_flows_response_from_dict = FlowListFlowsResponse.from_dict(flow_list_flows_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


