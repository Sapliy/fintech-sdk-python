# AuthAuditLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**action** | **str** |  | [optional] 
**resource_type** | **str** |  | [optional] 
**resource_id** | **str** |  | [optional] 
**metadata** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 

## Example

```python
from sapliyio_fintech.models.auth_audit_log import AuthAuditLog

# TODO update the JSON string below
json = "{}"
# create an instance of AuthAuditLog from a JSON string
auth_audit_log_instance = AuthAuditLog.from_json(json)
# print the JSON string representation of the object
print(AuthAuditLog.to_json())

# convert the object into a dict
auth_audit_log_dict = auth_audit_log_instance.to_dict()
# create an instance of AuthAuditLog from a dict
auth_audit_log_from_dict = AuthAuditLog.from_dict(auth_audit_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


