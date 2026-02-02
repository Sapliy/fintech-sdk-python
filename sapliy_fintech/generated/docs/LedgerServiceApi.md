# sapliy_fintech.LedgerServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ledger_service_get_account**](LedgerServiceApi.md#ledger_service_get_account) | **GET** /v1/ledger/accounts/{accountId} | 
[**ledger_service_record_transaction**](LedgerServiceApi.md#ledger_service_record_transaction) | **POST** /v1/ledger/transactions | 


# **ledger_service_get_account**
> LedgerGetAccountResponse ledger_service_get_account(account_id)

### Example


```python
import sapliy_fintech
from sapliy_fintech.models.ledger_get_account_response import LedgerGetAccountResponse
from sapliy_fintech.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sapliy_fintech.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sapliy_fintech.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sapliy_fintech.LedgerServiceApi(api_client)
    account_id = 'account_id_example' # str | 

    try:
        api_response = api_instance.ledger_service_get_account(account_id)
        print("The response of LedgerServiceApi->ledger_service_get_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerServiceApi->ledger_service_get_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

### Return type

[**LedgerGetAccountResponse**](LedgerGetAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ledger_service_record_transaction**
> LedgerRecordTransactionResponse ledger_service_record_transaction(body)

### Example


```python
import sapliy_fintech
from sapliy_fintech.models.ledger_record_transaction_request import LedgerRecordTransactionRequest
from sapliy_fintech.models.ledger_record_transaction_response import LedgerRecordTransactionResponse
from sapliy_fintech.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sapliy_fintech.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sapliy_fintech.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sapliy_fintech.LedgerServiceApi(api_client)
    body = sapliy_fintech.LedgerRecordTransactionRequest() # LedgerRecordTransactionRequest | 

    try:
        api_response = api_instance.ledger_service_record_transaction(body)
        print("The response of LedgerServiceApi->ledger_service_record_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerServiceApi->ledger_service_record_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LedgerRecordTransactionRequest**](LedgerRecordTransactionRequest.md)|  | 

### Return type

[**LedgerRecordTransactionResponse**](LedgerRecordTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

