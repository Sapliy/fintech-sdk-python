# ZoneBulkUpdateMetadataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_ids** | **List[str]** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sapliy_fintech.generated.models.zone_bulk_update_metadata_request import ZoneBulkUpdateMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneBulkUpdateMetadataRequest from a JSON string
zone_bulk_update_metadata_request_instance = ZoneBulkUpdateMetadataRequest.from_json(json)
# print the JSON string representation of the object
print(ZoneBulkUpdateMetadataRequest.to_json())

# convert the object into a dict
zone_bulk_update_metadata_request_dict = zone_bulk_update_metadata_request_instance.to_dict()
# create an instance of ZoneBulkUpdateMetadataRequest from a dict
zone_bulk_update_metadata_request_from_dict = ZoneBulkUpdateMetadataRequest.from_dict(zone_bulk_update_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


