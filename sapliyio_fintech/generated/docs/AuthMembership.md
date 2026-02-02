# AuthMembership


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 

## Example

```python
from sapliyio_fintech.models.auth_membership import AuthMembership

# TODO update the JSON string below
json = "{}"
# create an instance of AuthMembership from a JSON string
auth_membership_instance = AuthMembership.from_json(json)
# print the JSON string representation of the object
print(AuthMembership.to_json())

# convert the object into a dict
auth_membership_dict = auth_membership_instance.to_dict()
# create an instance of AuthMembership from a dict
auth_membership_from_dict = AuthMembership.from_dict(auth_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


