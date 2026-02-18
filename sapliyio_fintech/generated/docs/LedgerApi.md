# sapliyio_fintech.generated.LedgerApi

All URIs are relative to *https://api.sapliy.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ledger_account**](LedgerApi.md#get_ledger_account) | **GET** /v1/ledger/accounts/{id} | Get Ledger Account details
[**get_ledger_transaction**](LedgerApi.md#get_ledger_transaction) | **GET** /v1/ledger/transactions/{id} | Get Ledger Transaction details
[**v1_ledger_accounts_post**](LedgerApi.md#v1_ledger_accounts_post) | **POST** /v1/ledger/accounts | Create Ledger Account
[**v1_ledger_transactions_post**](LedgerApi.md#v1_ledger_transactions_post) | **POST** /v1/ledger/transactions | Record Transaction


# **get_ledger_account**
> LedgerAccount get_ledger_account(id, x_zone_id)

Get Ledger Account details

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.ledger_account import LedgerAccount
from sapliyio_fintech.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sapliy.io
# See configuration.py for a list of all supported configuration parameters.
configuration = sapliyio_fintech.generated.Configuration(
    host = "https://api.sapliy.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = sapliyio_fintech.generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sapliyio_fintech.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sapliyio_fintech.generated.LedgerApi(api_client)
    id = 'id_example' # str | 
    x_zone_id = 'x_zone_id_example' # str | The ID of the zone for this request.

    try:
        # Get Ledger Account details
        api_response = api_instance.get_ledger_account(id, x_zone_id)
        print("The response of LedgerApi->get_ledger_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerApi->get_ledger_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_zone_id** | **str**| The ID of the zone for this request. | 

### Return type

[**LedgerAccount**](LedgerAccount.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_transaction**
> LedgerTransaction get_ledger_transaction(id, x_zone_id)

Get Ledger Transaction details

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.ledger_transaction import LedgerTransaction
from sapliyio_fintech.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sapliy.io
# See configuration.py for a list of all supported configuration parameters.
configuration = sapliyio_fintech.generated.Configuration(
    host = "https://api.sapliy.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = sapliyio_fintech.generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sapliyio_fintech.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sapliyio_fintech.generated.LedgerApi(api_client)
    id = 'id_example' # str | 
    x_zone_id = 'x_zone_id_example' # str | The ID of the zone for this request.

    try:
        # Get Ledger Transaction details
        api_response = api_instance.get_ledger_transaction(id, x_zone_id)
        print("The response of LedgerApi->get_ledger_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerApi->get_ledger_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_zone_id** | **str**| The ID of the zone for this request. | 

### Return type

[**LedgerTransaction**](LedgerTransaction.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_ledger_accounts_post**
> LedgerAccount v1_ledger_accounts_post(x_zone_id, v1_ledger_accounts_post_request)

Create Ledger Account

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.ledger_account import LedgerAccount
from sapliyio_fintech.generated.models.v1_ledger_accounts_post_request import V1LedgerAccountsPostRequest
from sapliyio_fintech.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sapliy.io
# See configuration.py for a list of all supported configuration parameters.
configuration = sapliyio_fintech.generated.Configuration(
    host = "https://api.sapliy.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = sapliyio_fintech.generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sapliyio_fintech.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sapliyio_fintech.generated.LedgerApi(api_client)
    x_zone_id = 'x_zone_id_example' # str | The ID of the zone for this request.
    v1_ledger_accounts_post_request = sapliyio_fintech.generated.V1LedgerAccountsPostRequest() # V1LedgerAccountsPostRequest | 

    try:
        # Create Ledger Account
        api_response = api_instance.v1_ledger_accounts_post(x_zone_id, v1_ledger_accounts_post_request)
        print("The response of LedgerApi->v1_ledger_accounts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerApi->v1_ledger_accounts_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_zone_id** | **str**| The ID of the zone for this request. | 
 **v1_ledger_accounts_post_request** | [**V1LedgerAccountsPostRequest**](V1LedgerAccountsPostRequest.md)|  | 

### Return type

[**LedgerAccount**](LedgerAccount.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_ledger_transactions_post**
> V1LedgerTransactionsPost201Response v1_ledger_transactions_post(x_zone_id, v1_ledger_transactions_post_request)

Record Transaction

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.v1_ledger_transactions_post201_response import V1LedgerTransactionsPost201Response
from sapliyio_fintech.generated.models.v1_ledger_transactions_post_request import V1LedgerTransactionsPostRequest
from sapliyio_fintech.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sapliy.io
# See configuration.py for a list of all supported configuration parameters.
configuration = sapliyio_fintech.generated.Configuration(
    host = "https://api.sapliy.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: ApiKeyAuth
configuration = sapliyio_fintech.generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sapliyio_fintech.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sapliyio_fintech.generated.LedgerApi(api_client)
    x_zone_id = 'x_zone_id_example' # str | The ID of the zone for this request.
    v1_ledger_transactions_post_request = sapliyio_fintech.generated.V1LedgerTransactionsPostRequest() # V1LedgerTransactionsPostRequest | 

    try:
        # Record Transaction
        api_response = api_instance.v1_ledger_transactions_post(x_zone_id, v1_ledger_transactions_post_request)
        print("The response of LedgerApi->v1_ledger_transactions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerApi->v1_ledger_transactions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_zone_id** | **str**| The ID of the zone for this request. | 
 **v1_ledger_transactions_post_request** | [**V1LedgerTransactionsPostRequest**](V1LedgerTransactionsPostRequest.md)|  | 

### Return type

[**V1LedgerTransactionsPost201Response**](V1LedgerTransactionsPost201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Recorded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

