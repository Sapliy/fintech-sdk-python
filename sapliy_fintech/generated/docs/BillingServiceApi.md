# sapliy_fintech.generated.BillingServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billing_service_cancel_subscription**](BillingServiceApi.md#billing_service_cancel_subscription) | **POST** /v1/billing/subscriptions/{id}/cancel | 
[**billing_service_create_subscription**](BillingServiceApi.md#billing_service_create_subscription) | **POST** /v1/billing/subscriptions | 
[**billing_service_get_subscription**](BillingServiceApi.md#billing_service_get_subscription) | **GET** /v1/billing/subscriptions/{id} | 
[**billing_service_list_subscriptions**](BillingServiceApi.md#billing_service_list_subscriptions) | **GET** /v1/billing/subscriptions | 


# **billing_service_cancel_subscription**
> BillingSubscription billing_service_cancel_subscription(id, body)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.billing_subscription import BillingSubscription
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
    api_instance = sapliy_fintech.generated.BillingServiceApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.billing_service_cancel_subscription(id, body)
        print("The response of BillingServiceApi->billing_service_cancel_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingServiceApi->billing_service_cancel_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**BillingSubscription**](BillingSubscription.md)

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

# **billing_service_create_subscription**
> BillingSubscription billing_service_create_subscription(body)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.billing_create_subscription_request import BillingCreateSubscriptionRequest
from sapliy_fintech.generated.models.billing_subscription import BillingSubscription
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
    api_instance = sapliy_fintech.generated.BillingServiceApi(api_client)
    body = sapliy_fintech.generated.BillingCreateSubscriptionRequest() # BillingCreateSubscriptionRequest | 

    try:
        api_response = api_instance.billing_service_create_subscription(body)
        print("The response of BillingServiceApi->billing_service_create_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingServiceApi->billing_service_create_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BillingCreateSubscriptionRequest**](BillingCreateSubscriptionRequest.md)|  | 

### Return type

[**BillingSubscription**](BillingSubscription.md)

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

# **billing_service_get_subscription**
> BillingSubscription billing_service_get_subscription(id)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.billing_subscription import BillingSubscription
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
    api_instance = sapliy_fintech.generated.BillingServiceApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.billing_service_get_subscription(id)
        print("The response of BillingServiceApi->billing_service_get_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingServiceApi->billing_service_get_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BillingSubscription**](BillingSubscription.md)

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

# **billing_service_list_subscriptions**
> BillingListSubscriptionsResponse billing_service_list_subscriptions(user_id=user_id, org_id=org_id, limit=limit, offset=offset)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.billing_list_subscriptions_response import BillingListSubscriptionsResponse
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
    api_instance = sapliy_fintech.generated.BillingServiceApi(api_client)
    user_id = 'user_id_example' # str |  (optional)
    org_id = 'org_id_example' # str |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)

    try:
        api_response = api_instance.billing_service_list_subscriptions(user_id=user_id, org_id=org_id, limit=limit, offset=offset)
        print("The response of BillingServiceApi->billing_service_list_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingServiceApi->billing_service_list_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | [optional] 
 **org_id** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

[**BillingListSubscriptionsResponse**](BillingListSubscriptionsResponse.md)

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

