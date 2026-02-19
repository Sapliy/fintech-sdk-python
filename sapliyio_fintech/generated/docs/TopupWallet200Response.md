# TopupWallet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from sapliyio_fintech.generated.models.topup_wallet200_response import TopupWallet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TopupWallet200Response from a JSON string
topup_wallet200_response_instance = TopupWallet200Response.from_json(json)
# print the JSON string representation of the object
print(TopupWallet200Response.to_json())

# convert the object into a dict
topup_wallet200_response_dict = topup_wallet200_response_instance.to_dict()
# create an instance of TopupWallet200Response from a dict
topup_wallet200_response_from_dict = TopupWallet200Response.from_dict(topup_wallet200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


