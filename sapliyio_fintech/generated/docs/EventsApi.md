# sapliyio_fintech.generated.EventsApi

All URIs are relative to *https://api.sapliy.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**emit_event**](EventsApi.md#emit_event) | **POST** /v1/events/emit | Emit an Event


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

