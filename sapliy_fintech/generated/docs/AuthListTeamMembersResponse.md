# AuthListTeamMembersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memberships** | [**List[AuthMembership]**](AuthMembership.md) |  | [optional] 

## Example

```python
from sapliy_fintech.models.auth_list_team_members_response import AuthListTeamMembersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthListTeamMembersResponse from a JSON string
auth_list_team_members_response_instance = AuthListTeamMembersResponse.from_json(json)
# print the JSON string representation of the object
print(AuthListTeamMembersResponse.to_json())

# convert the object into a dict
auth_list_team_members_response_dict = auth_list_team_members_response_instance.to_dict()
# create an instance of AuthListTeamMembersResponse from a dict
auth_list_team_members_response_from_dict = AuthListTeamMembersResponse.from_dict(auth_list_team_members_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


