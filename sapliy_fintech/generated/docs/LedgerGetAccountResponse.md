# LedgerGetAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**balance** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from sapliy_fintech.generated.models.ledger_get_account_response import LedgerGetAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerGetAccountResponse from a JSON string
ledger_get_account_response_instance = LedgerGetAccountResponse.from_json(json)
# print the JSON string representation of the object
print(LedgerGetAccountResponse.to_json())

# convert the object into a dict
ledger_get_account_response_dict = ledger_get_account_response_instance.to_dict()
# create an instance of LedgerGetAccountResponse from a dict
ledger_get_account_response_from_dict = LedgerGetAccountResponse.from_dict(ledger_get_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


