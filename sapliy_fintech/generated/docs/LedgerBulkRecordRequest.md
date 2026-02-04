# LedgerBulkRecordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[LedgerRecordTransactionRequest]**](LedgerRecordTransactionRequest.md) |  | [optional] 

## Example

```python
from sapliy_fintech.generated.models.ledger_bulk_record_request import LedgerBulkRecordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerBulkRecordRequest from a JSON string
ledger_bulk_record_request_instance = LedgerBulkRecordRequest.from_json(json)
# print the JSON string representation of the object
print(LedgerBulkRecordRequest.to_json())

# convert the object into a dict
ledger_bulk_record_request_dict = ledger_bulk_record_request_instance.to_dict()
# create an instance of LedgerBulkRecordRequest from a dict
ledger_bulk_record_request_from_dict = LedgerBulkRecordRequest.from_dict(ledger_bulk_record_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


