# LedgerRecordTransactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from sapliy_fintech.models.ledger_record_transaction_response import LedgerRecordTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerRecordTransactionResponse from a JSON string
ledger_record_transaction_response_instance = LedgerRecordTransactionResponse.from_json(json)
# print the JSON string representation of the object
print(LedgerRecordTransactionResponse.to_json())

# convert the object into a dict
ledger_record_transaction_response_dict = ledger_record_transaction_response_instance.to_dict()
# create an instance of LedgerRecordTransactionResponse from a dict
ledger_record_transaction_response_from_dict = LedgerRecordTransactionResponse.from_dict(ledger_record_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


