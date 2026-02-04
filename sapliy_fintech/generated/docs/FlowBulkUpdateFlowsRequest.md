# FlowBulkUpdateFlowsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_ids** | **List[str]** |  | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from sapliy_fintech.generated.models.flow_bulk_update_flows_request import FlowBulkUpdateFlowsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowBulkUpdateFlowsRequest from a JSON string
flow_bulk_update_flows_request_instance = FlowBulkUpdateFlowsRequest.from_json(json)
# print the JSON string representation of the object
print(FlowBulkUpdateFlowsRequest.to_json())

# convert the object into a dict
flow_bulk_update_flows_request_dict = flow_bulk_update_flows_request_instance.to_dict()
# create an instance of FlowBulkUpdateFlowsRequest from a dict
flow_bulk_update_flows_request_from_dict = FlowBulkUpdateFlowsRequest.from_dict(flow_bulk_update_flows_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


