# LedgerEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**amount** | **int** |  | 

## Example

```python
from sapliyio_fintech.generated.models.ledger_entry import LedgerEntry

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerEntry from a JSON string
ledger_entry_instance = LedgerEntry.from_json(json)
# print the JSON string representation of the object
print(LedgerEntry.to_json())

# convert the object into a dict
ledger_entry_dict = ledger_entry_instance.to_dict()
# create an instance of LedgerEntry from a dict
ledger_entry_from_dict = LedgerEntry.from_dict(ledger_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


