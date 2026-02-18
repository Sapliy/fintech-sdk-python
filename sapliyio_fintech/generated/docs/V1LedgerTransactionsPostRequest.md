# V1LedgerTransactionsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_id** | **str** |  | 
**description** | **str** |  | [optional] 
**entries** | [**List[LedgerEntry]**](LedgerEntry.md) |  | 

## Example

```python
from sapliyio_fintech.generated.models.v1_ledger_transactions_post_request import V1LedgerTransactionsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1LedgerTransactionsPostRequest from a JSON string
v1_ledger_transactions_post_request_instance = V1LedgerTransactionsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1LedgerTransactionsPostRequest.to_json())

# convert the object into a dict
v1_ledger_transactions_post_request_dict = v1_ledger_transactions_post_request_instance.to_dict()
# create an instance of V1LedgerTransactionsPostRequest from a dict
v1_ledger_transactions_post_request_from_dict = V1LedgerTransactionsPostRequest.from_dict(v1_ledger_transactions_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


