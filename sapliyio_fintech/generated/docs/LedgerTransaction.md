# LedgerTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**reference_id** | **str** |  | 
**description** | **str** |  | [optional] 
**status** | **str** |  | 
**entries** | [**List[LedgerEntry]**](LedgerEntry.md) |  | [optional] 

## Example

```python
from sapliyio_fintech.generated.models.ledger_transaction import LedgerTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerTransaction from a JSON string
ledger_transaction_instance = LedgerTransaction.from_json(json)
# print the JSON string representation of the object
print(LedgerTransaction.to_json())

# convert the object into a dict
ledger_transaction_dict = ledger_transaction_instance.to_dict()
# create an instance of LedgerTransaction from a dict
ledger_transaction_from_dict = LedgerTransaction.from_dict(ledger_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


