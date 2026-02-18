# V1LedgerAccountsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** |  | 
**currency** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from sapliyio_fintech.generated.models.v1_ledger_accounts_post_request import V1LedgerAccountsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1LedgerAccountsPostRequest from a JSON string
v1_ledger_accounts_post_request_instance = V1LedgerAccountsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1LedgerAccountsPostRequest.to_json())

# convert the object into a dict
v1_ledger_accounts_post_request_dict = v1_ledger_accounts_post_request_instance.to_dict()
# create an instance of V1LedgerAccountsPostRequest from a dict
v1_ledger_accounts_post_request_from_dict = V1LedgerAccountsPostRequest.from_dict(v1_ledger_accounts_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


