# sapliyio_fintech.generated.WalletsApi

All URIs are relative to *https://api.sapliy.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_wallet**](WalletsApi.md#get_wallet) | **GET** /v1/wallets/{user_id} | Get Wallet Balance
[**v1_wallets_topup_post**](WalletsApi.md#v1_wallets_topup_post) | **POST** /v1/wallets/topup | Top up a wallet
[**v1_wallets_transfer_post**](WalletsApi.md#v1_wallets_transfer_post) | **POST** /v1/wallets/transfer | Transfer between wallets


# **get_wallet**
> Wallet get_wallet(user_id, x_zone_id, x_zone_mode=x_zone_mode)

Get Wallet Balance

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.wallet import Wallet
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
    api_instance = sapliyio_fintech.generated.WalletsApi(api_client)
    user_id = 'user_id_example' # str | 
    x_zone_id = 'x_zone_id_example' # str | The ID of the zone for this request.
    x_zone_mode = 'x_zone_mode_example' # str | The mode of the zone (live or test). (optional)

    try:
        # Get Wallet Balance
        api_response = api_instance.get_wallet(user_id, x_zone_id, x_zone_mode=x_zone_mode)
        print("The response of WalletsApi->get_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **x_zone_id** | **str**| The ID of the zone for this request. | 
 **x_zone_mode** | **str**| The mode of the zone (live or test). | [optional] 

### Return type

[**Wallet**](Wallet.md)

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

# **v1_wallets_topup_post**
> V1WalletsTopupPost200Response v1_wallets_topup_post(v1_wallets_topup_post_request)

Top up a wallet

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.v1_wallets_topup_post200_response import V1WalletsTopupPost200Response
from sapliyio_fintech.generated.models.v1_wallets_topup_post_request import V1WalletsTopupPostRequest
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
    api_instance = sapliyio_fintech.generated.WalletsApi(api_client)
    v1_wallets_topup_post_request = sapliyio_fintech.generated.V1WalletsTopupPostRequest() # V1WalletsTopupPostRequest | 

    try:
        # Top up a wallet
        api_response = api_instance.v1_wallets_topup_post(v1_wallets_topup_post_request)
        print("The response of WalletsApi->v1_wallets_topup_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->v1_wallets_topup_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_wallets_topup_post_request** | [**V1WalletsTopupPostRequest**](V1WalletsTopupPostRequest.md)|  | 

### Return type

[**V1WalletsTopupPost200Response**](V1WalletsTopupPost200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_wallets_transfer_post**
> V1WalletsTopupPost200Response v1_wallets_transfer_post(v1_wallets_transfer_post_request)

Transfer between wallets

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.v1_wallets_topup_post200_response import V1WalletsTopupPost200Response
from sapliyio_fintech.generated.models.v1_wallets_transfer_post_request import V1WalletsTransferPostRequest
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
    api_instance = sapliyio_fintech.generated.WalletsApi(api_client)
    v1_wallets_transfer_post_request = sapliyio_fintech.generated.V1WalletsTransferPostRequest() # V1WalletsTransferPostRequest | 

    try:
        # Transfer between wallets
        api_response = api_instance.v1_wallets_transfer_post(v1_wallets_transfer_post_request)
        print("The response of WalletsApi->v1_wallets_transfer_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->v1_wallets_transfer_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_wallets_transfer_post_request** | [**V1WalletsTransferPostRequest**](V1WalletsTransferPostRequest.md)|  | 

### Return type

[**V1WalletsTopupPost200Response**](V1WalletsTopupPost200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

