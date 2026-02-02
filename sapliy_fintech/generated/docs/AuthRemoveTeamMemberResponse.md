# AuthRemoveTeamMemberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 

## Example

```python
from sapliy_fintech.models.auth_remove_team_member_response import AuthRemoveTeamMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthRemoveTeamMemberResponse from a JSON string
auth_remove_team_member_response_instance = AuthRemoveTeamMemberResponse.from_json(json)
# print the JSON string representation of the object
print(AuthRemoveTeamMemberResponse.to_json())

# convert the object into a dict
auth_remove_team_member_response_dict = auth_remove_team_member_response_instance.to_dict()
# create an instance of AuthRemoveTeamMemberResponse from a dict
auth_remove_team_member_response_from_dict = AuthRemoveTeamMemberResponse.from_dict(auth_remove_team_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


