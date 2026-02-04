# LedgerCreateAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**zone_id** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from sapliy_fintech.generated.models.ledger_create_account_request import LedgerCreateAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerCreateAccountRequest from a JSON string
ledger_create_account_request_instance = LedgerCreateAccountRequest.from_json(json)
# print the JSON string representation of the object
print(LedgerCreateAccountRequest.to_json())

# convert the object into a dict
ledger_create_account_request_dict = ledger_create_account_request_instance.to_dict()
# create an instance of LedgerCreateAccountRequest from a dict
ledger_create_account_request_from_dict = LedgerCreateAccountRequest.from_dict(ledger_create_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


