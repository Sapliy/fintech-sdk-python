# sapliyio_fintech.NotificationServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notification_service_create_webhook_endpoint**](NotificationServiceApi.md#notification_service_create_webhook_endpoint) | **POST** /v1/webhooks/endpoints | 
[**notification_service_delete_webhook_endpoint**](NotificationServiceApi.md#notification_service_delete_webhook_endpoint) | **DELETE** /v1/webhooks/endpoints/{id} | 
[**notification_service_get_notification_history**](NotificationServiceApi.md#notification_service_get_notification_history) | **GET** /v1/notifications | 
[**notification_service_list_webhook_endpoints**](NotificationServiceApi.md#notification_service_list_webhook_endpoints) | **GET** /v1/webhooks/endpoints | 


# **notification_service_create_webhook_endpoint**
> NotificationsWebhookEndpoint notification_service_create_webhook_endpoint(body)

### Example


```python
import sapliyio_fintech
from sapliyio_fintech.models.notifications_create_webhook_endpoint_request import NotificationsCreateWebhookEndpointRequest
from sapliyio_fintech.models.notifications_webhook_endpoint import NotificationsWebhookEndpoint
from sapliyio_fintech.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sapliyio_fintech.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sapliyio_fintech.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sapliyio_fintech.NotificationServiceApi(api_client)
    body = sapliyio_fintech.NotificationsCreateWebhookEndpointRequest() # NotificationsCreateWebhookEndpointRequest | 

    try:
        api_response = api_instance.notification_service_create_webhook_endpoint(body)
        print("The response of NotificationServiceApi->notification_service_create_webhook_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationServiceApi->notification_service_create_webhook_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationsCreateWebhookEndpointRequest**](NotificationsCreateWebhookEndpointRequest.md)|  | 

### Return type

[**NotificationsWebhookEndpoint**](NotificationsWebhookEndpoint.md)

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

# **notification_service_delete_webhook_endpoint**
> NotificationsDeleteWebhookEndpointResponse notification_service_delete_webhook_endpoint(id)

### Example


```python
import sapliyio_fintech
from sapliyio_fintech.models.notifications_delete_webhook_endpoint_response import NotificationsDeleteWebhookEndpointResponse
from sapliyio_fintech.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sapliyio_fintech.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sapliyio_fintech.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sapliyio_fintech.NotificationServiceApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.notification_service_delete_webhook_endpoint(id)
        print("The response of NotificationServiceApi->notification_service_delete_webhook_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationServiceApi->notification_service_delete_webhook_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**NotificationsDeleteWebhookEndpointResponse**](NotificationsDeleteWebhookEndpointResponse.md)

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

# **notification_service_get_notification_history**
> NotificationsGetNotificationHistoryResponse notification_service_get_notification_history(user_id=user_id, limit=limit, offset=offset)

### Example


```python
import sapliyio_fintech
from sapliyio_fintech.models.notifications_get_notification_history_response import NotificationsGetNotificationHistoryResponse
from sapliyio_fintech.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sapliyio_fintech.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sapliyio_fintech.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sapliyio_fintech.NotificationServiceApi(api_client)
    user_id = 'user_id_example' # str |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)

    try:
        api_response = api_instance.notification_service_get_notification_history(user_id=user_id, limit=limit, offset=offset)
        print("The response of NotificationServiceApi->notification_service_get_notification_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationServiceApi->notification_service_get_notification_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

[**NotificationsGetNotificationHistoryResponse**](NotificationsGetNotificationHistoryResponse.md)

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

# **notification_service_list_webhook_endpoints**
> NotificationsListWebhookEndpointsResponse notification_service_list_webhook_endpoints()

### Example


```python
import sapliyio_fintech
from sapliyio_fintech.models.notifications_list_webhook_endpoints_response import NotificationsListWebhookEndpointsResponse
from sapliyio_fintech.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sapliyio_fintech.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sapliyio_fintech.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sapliyio_fintech.NotificationServiceApi(api_client)

    try:
        api_response = api_instance.notification_service_list_webhook_endpoints()
        print("The response of NotificationServiceApi->notification_service_list_webhook_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationServiceApi->notification_service_list_webhook_endpoints: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NotificationsListWebhookEndpointsResponse**](NotificationsListWebhookEndpointsResponse.md)

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

