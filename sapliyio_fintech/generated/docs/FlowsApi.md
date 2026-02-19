# sapliyio_fintech.generated.FlowsApi

All URIs are relative to *https://api.sapliy.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_flow**](FlowsApi.md#create_flow) | **POST** /v1/flows | Create a Flow
[**delete_flow**](FlowsApi.md#delete_flow) | **DELETE** /v1/flows/{flowId} | Delete a Flow
[**get_flow**](FlowsApi.md#get_flow) | **GET** /v1/flows/{flowId} | Get Flow details
[**list_flows**](FlowsApi.md#list_flows) | **GET** /v1/zones/{zoneId}/flows | List Flows in a Zone
[**update_flow**](FlowsApi.md#update_flow) | **PUT** /v1/flows/{flowId} | Update a Flow


# **create_flow**
> AutomationFlow create_flow(automation_flow)

Create a Flow

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.automation_flow import AutomationFlow
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
    api_instance = sapliyio_fintech.generated.FlowsApi(api_client)
    automation_flow = sapliyio_fintech.generated.AutomationFlow() # AutomationFlow | 

    try:
        # Create a Flow
        api_response = api_instance.create_flow(automation_flow)
        print("The response of FlowsApi->create_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->create_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **automation_flow** | [**AutomationFlow**](AutomationFlow.md)|  | 

### Return type

[**AutomationFlow**](AutomationFlow.md)

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

# **delete_flow**
> delete_flow(flow_id)

Delete a Flow

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sapliyio_fintech.generated
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
    api_instance = sapliyio_fintech.generated.FlowsApi(api_client)
    flow_id = 'flow_id_example' # str | 

    try:
        # Delete a Flow
        api_instance.delete_flow(flow_id)
    except Exception as e:
        print("Exception when calling FlowsApi->delete_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flow**
> AutomationFlow get_flow(flow_id)

Get Flow details

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.automation_flow import AutomationFlow
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
    api_instance = sapliyio_fintech.generated.FlowsApi(api_client)
    flow_id = 'flow_id_example' # str | 

    try:
        # Get Flow details
        api_response = api_instance.get_flow(flow_id)
        print("The response of FlowsApi->get_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->get_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 

### Return type

[**AutomationFlow**](AutomationFlow.md)

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

# **list_flows**
> ListFlows200Response list_flows(zone_id)

List Flows in a Zone

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.list_flows200_response import ListFlows200Response
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
    api_instance = sapliyio_fintech.generated.FlowsApi(api_client)
    zone_id = 'zone_id_example' # str | 

    try:
        # List Flows in a Zone
        api_response = api_instance.list_flows(zone_id)
        print("The response of FlowsApi->list_flows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->list_flows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**|  | 

### Return type

[**ListFlows200Response**](ListFlows200Response.md)

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

# **update_flow**
> AutomationFlow update_flow(flow_id, automation_flow)

Update a Flow

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.automation_flow import AutomationFlow
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
    api_instance = sapliyio_fintech.generated.FlowsApi(api_client)
    flow_id = 'flow_id_example' # str | 
    automation_flow = sapliyio_fintech.generated.AutomationFlow() # AutomationFlow | 

    try:
        # Update a Flow
        api_response = api_instance.update_flow(flow_id, automation_flow)
        print("The response of FlowsApi->update_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->update_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**|  | 
 **automation_flow** | [**AutomationFlow**](AutomationFlow.md)|  | 

### Return type

[**AutomationFlow**](AutomationFlow.md)

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

