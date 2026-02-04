# LedgerCreateAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from sapliy_fintech.generated.models.ledger_create_account_response import LedgerCreateAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerCreateAccountResponse from a JSON string
ledger_create_account_response_instance = LedgerCreateAccountResponse.from_json(json)
# print the JSON string representation of the object
print(LedgerCreateAccountResponse.to_json())

# convert the object into a dict
ledger_create_account_response_dict = ledger_create_account_response_instance.to_dict()
# create an instance of LedgerCreateAccountResponse from a dict
ledger_create_account_response_from_dict = LedgerCreateAccountResponse.from_dict(ledger_create_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


