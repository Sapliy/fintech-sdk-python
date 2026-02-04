# LedgerBulkRecordResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responses** | [**List[LedgerRecordTransactionResponse]**](LedgerRecordTransactionResponse.md) |  | [optional] 

## Example

```python
from sapliy_fintech.generated.models.ledger_bulk_record_response import LedgerBulkRecordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerBulkRecordResponse from a JSON string
ledger_bulk_record_response_instance = LedgerBulkRecordResponse.from_json(json)
# print the JSON string representation of the object
print(LedgerBulkRecordResponse.to_json())

# convert the object into a dict
ledger_bulk_record_response_dict = ledger_bulk_record_response_instance.to_dict()
# create an instance of LedgerBulkRecordResponse from a dict
ledger_bulk_record_response_from_dict = LedgerBulkRecordResponse.from_dict(ledger_bulk_record_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


