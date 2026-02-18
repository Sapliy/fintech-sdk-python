# LedgerAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**type** | **str** |  | 
**currency** | **str** |  | 
**balance** | **int** |  | [optional] 

## Example

```python
from sapliyio_fintech.generated.models.ledger_account import LedgerAccount

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerAccount from a JSON string
ledger_account_instance = LedgerAccount.from_json(json)
# print the JSON string representation of the object
print(LedgerAccount.to_json())

# convert the object into a dict
ledger_account_dict = ledger_account_instance.to_dict()
# create an instance of LedgerAccount from a dict
ledger_account_from_dict = LedgerAccount.from_dict(ledger_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


