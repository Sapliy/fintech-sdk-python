# sapliyio_fintech.generated.EventsApi

All URIs are relative to *https://api.sapliy.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**emit_event**](EventsApi.md#emit_event) | **POST** /v1/events/emit | Emit an Event
[**get_past_events**](EventsApi.md#get_past_events) | **GET** /v1/zones/{zoneId}/events/past | Get Past Events (Webhook Replay)
[**replay_event**](EventsApi.md#replay_event) | **POST** /v1/events/{eventId}/replay | Replay an Event


# **emit_event**
> EmitEvent202Response emit_event(emit_event_request)

Emit an Event

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.emit_event202_response import EmitEvent202Response
from sapliyio_fintech.generated.models.emit_event_request import EmitEventRequest
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
    api_instance = sapliyio_fintech.generated.EventsApi(api_client)
    emit_event_request = sapliyio_fintech.generated.EmitEventRequest() # EmitEventRequest | 

    try:
        # Emit an Event
        api_response = api_instance.emit_event(emit_event_request)
        print("The response of EventsApi->emit_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->emit_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emit_event_request** | [**EmitEventRequest**](EmitEventRequest.md)|  | 

### Return type

[**EmitEvent202Response**](EmitEvent202Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_past_events**
> GetPastEvents200Response get_past_events(zone_id, limit=limit, offset=offset)

Get Past Events (Webhook Replay)

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.get_past_events200_response import GetPastEvents200Response
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
    api_instance = sapliyio_fintech.generated.EventsApi(api_client)
    zone_id = 'zone_id_example' # str | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)

    try:
        # Get Past Events (Webhook Replay)
        api_response = api_instance.get_past_events(zone_id, limit=limit, offset=offset)
        print("The response of EventsApi->get_past_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_past_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

[**GetPastEvents200Response**](GetPastEvents200Response.md)

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

# **replay_event**
> ReplayEvent200Response replay_event(event_id, replay_event_request)

Replay an Event

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.replay_event200_response import ReplayEvent200Response
from sapliyio_fintech.generated.models.replay_event_request import ReplayEventRequest
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
    api_instance = sapliyio_fintech.generated.EventsApi(api_client)
    event_id = 'event_id_example' # str | 
    replay_event_request = sapliyio_fintech.generated.ReplayEventRequest() # ReplayEventRequest | 

    try:
        # Replay an Event
        api_response = api_instance.replay_event(event_id, replay_event_request)
        print("The response of EventsApi->replay_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->replay_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 
 **replay_event_request** | [**ReplayEventRequest**](ReplayEventRequest.md)|  | 

### Return type

[**ReplayEvent200Response**](ReplayEvent200Response.md)

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

