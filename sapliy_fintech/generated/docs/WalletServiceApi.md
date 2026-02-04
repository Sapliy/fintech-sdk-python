# sapliy_fintech.generated.WalletServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wallet_service_create_wallet**](WalletServiceApi.md#wallet_service_create_wallet) | **POST** /v1/wallets | 
[**wallet_service_get_wallet**](WalletServiceApi.md#wallet_service_get_wallet) | **GET** /v1/wallets/{userId} | 
[**wallet_service_top_up**](WalletServiceApi.md#wallet_service_top_up) | **POST** /v1/wallets/top-up | 
[**wallet_service_transfer**](WalletServiceApi.md#wallet_service_transfer) | **POST** /v1/wallets/transfer | 


# **wallet_service_create_wallet**
> WalletWallet wallet_service_create_wallet(body)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.wallet_create_wallet_request import WalletCreateWalletRequest
from sapliy_fintech.generated.models.wallet_wallet import WalletWallet
from sapliy_fintech.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sapliy_fintech.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sapliy_fintech.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sapliy_fintech.generated.WalletServiceApi(api_client)
    body = sapliy_fintech.generated.WalletCreateWalletRequest() # WalletCreateWalletRequest | 

    try:
        api_response = api_instance.wallet_service_create_wallet(body)
        print("The response of WalletServiceApi->wallet_service_create_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletServiceApi->wallet_service_create_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WalletCreateWalletRequest**](WalletCreateWalletRequest.md)|  | 

### Return type

[**WalletWallet**](WalletWallet.md)

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

# **wallet_service_get_wallet**
> WalletWallet wallet_service_get_wallet(user_id)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.wallet_wallet import WalletWallet
from sapliy_fintech.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sapliy_fintech.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sapliy_fintech.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sapliy_fintech.generated.WalletServiceApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        api_response = api_instance.wallet_service_get_wallet(user_id)
        print("The response of WalletServiceApi->wallet_service_get_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletServiceApi->wallet_service_get_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**WalletWallet**](WalletWallet.md)

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

# **wallet_service_top_up**
> WalletTransactionResponse wallet_service_top_up(body)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.wallet_top_up_request import WalletTopUpRequest
from sapliy_fintech.generated.models.wallet_transaction_response import WalletTransactionResponse
from sapliy_fintech.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sapliy_fintech.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sapliy_fintech.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sapliy_fintech.generated.WalletServiceApi(api_client)
    body = sapliy_fintech.generated.WalletTopUpRequest() # WalletTopUpRequest | 

    try:
        api_response = api_instance.wallet_service_top_up(body)
        print("The response of WalletServiceApi->wallet_service_top_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletServiceApi->wallet_service_top_up: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WalletTopUpRequest**](WalletTopUpRequest.md)|  | 

### Return type

[**WalletTransactionResponse**](WalletTransactionResponse.md)

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

# **wallet_service_transfer**
> WalletTransactionResponse wallet_service_transfer(body)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.wallet_transaction_response import WalletTransactionResponse
from sapliy_fintech.generated.models.wallet_transfer_request import WalletTransferRequest
from sapliy_fintech.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sapliy_fintech.generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sapliy_fintech.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sapliy_fintech.generated.WalletServiceApi(api_client)
    body = sapliy_fintech.generated.WalletTransferRequest() # WalletTransferRequest | 

    try:
        api_response = api_instance.wallet_service_transfer(body)
        print("The response of WalletServiceApi->wallet_service_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletServiceApi->wallet_service_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WalletTransferRequest**](WalletTransferRequest.md)|  | 

### Return type

[**WalletTransactionResponse**](WalletTransactionResponse.md)

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

