# AuthGetAuditLogsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**List[AuthAuditLog]**](AuthAuditLog.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from sapliyio_fintech.models.auth_get_audit_logs_response import AuthGetAuditLogsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthGetAuditLogsResponse from a JSON string
auth_get_audit_logs_response_instance = AuthGetAuditLogsResponse.from_json(json)
# print the JSON string representation of the object
print(AuthGetAuditLogsResponse.to_json())

# convert the object into a dict
auth_get_audit_logs_response_dict = auth_get_audit_logs_response_instance.to_dict()
# create an instance of AuthGetAuditLogsResponse from a dict
auth_get_audit_logs_response_from_dict = AuthGetAuditLogsResponse.from_dict(auth_get_audit_logs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


