# LedgerRecordTransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**reference_id** | **str** |  | [optional] 
**zone_id** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from sapliy_fintech.generated.models.ledger_record_transaction_request import LedgerRecordTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerRecordTransactionRequest from a JSON string
ledger_record_transaction_request_instance = LedgerRecordTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(LedgerRecordTransactionRequest.to_json())

# convert the object into a dict
ledger_record_transaction_request_dict = ledger_record_transaction_request_instance.to_dict()
# create an instance of LedgerRecordTransactionRequest from a dict
ledger_record_transaction_request_from_dict = LedgerRecordTransactionRequest.from_dict(ledger_record_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


