# Flow


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
**trigger** | [**Trigger**](Trigger.md) |  | [optional] 
**nodes** | [**List[Node]**](Node.md) |  | [optional] 
**edges** | [**List[Edge]**](Edge.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sapliyio_fintech.generated.models.flow import Flow

# TODO update the JSON string below
json = "{}"
# create an instance of Flow from a JSON string
flow_instance = Flow.from_json(json)
# print the JSON string representation of the object
print(Flow.to_json())

# convert the object into a dict
flow_dict = flow_instance.to_dict()
# create an instance of Flow from a dict
flow_from_dict = Flow.from_dict(flow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


