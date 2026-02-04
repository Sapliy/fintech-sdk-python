# AuthAddTeamMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**role** | **str** |  | [optional] 

## Example

```python
from sapliy_fintech.generated.models.auth_add_team_member_request import AuthAddTeamMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthAddTeamMemberRequest from a JSON string
auth_add_team_member_request_instance = AuthAddTeamMemberRequest.from_json(json)
# print the JSON string representation of the object
print(AuthAddTeamMemberRequest.to_json())

# convert the object into a dict
auth_add_team_member_request_dict = auth_add_team_member_request_instance.to_dict()
# create an instance of AuthAddTeamMemberRequest from a dict
auth_add_team_member_request_from_dict = AuthAddTeamMemberRequest.from_dict(auth_add_team_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


