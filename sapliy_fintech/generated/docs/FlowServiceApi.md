# sapliy_fintech.generated.FlowServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**flow_service_bulk_update_flows**](FlowServiceApi.md#flow_service_bulk_update_flows) | **POST** /v1/flows/bulk-update | 
[**flow_service_create_flow**](FlowServiceApi.md#flow_service_create_flow) | **POST** /v1/flows | 
[**flow_service_get_execution**](FlowServiceApi.md#flow_service_get_execution) | **GET** /v1/flows/executions/{id} | 
[**flow_service_get_flow**](FlowServiceApi.md#flow_service_get_flow) | **GET** /v1/flows/{id} | 
[**flow_service_list_flows**](FlowServiceApi.md#flow_service_list_flows) | **GET** /v1/flows | 
[**flow_service_resume_execution**](FlowServiceApi.md#flow_service_resume_execution) | **POST** /v1/flows/executions/{executionId}/resume | 
[**flow_service_update_flow**](FlowServiceApi.md#flow_service_update_flow) | **PUT** /v1/flows/{id} | 


# **flow_service_bulk_update_flows**
> FlowBulkUpdateFlowsResponse flow_service_bulk_update_flows(body)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.flow_bulk_update_flows_request import FlowBulkUpdateFlowsRequest
from sapliy_fintech.generated.models.flow_bulk_update_flows_response import FlowBulkUpdateFlowsResponse
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
    api_instance = sapliy_fintech.generated.FlowServiceApi(api_client)
    body = sapliy_fintech.generated.FlowBulkUpdateFlowsRequest() # FlowBulkUpdateFlowsRequest | 

    try:
        api_response = api_instance.flow_service_bulk_update_flows(body)
        print("The response of FlowServiceApi->flow_service_bulk_update_flows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowServiceApi->flow_service_bulk_update_flows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FlowBulkUpdateFlowsRequest**](FlowBulkUpdateFlowsRequest.md)|  | 

### Return type

[**FlowBulkUpdateFlowsResponse**](FlowBulkUpdateFlowsResponse.md)

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

# **flow_service_create_flow**
> FlowFlow flow_service_create_flow(body)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.flow_create_flow_request import FlowCreateFlowRequest
from sapliy_fintech.generated.models.flow_flow import FlowFlow
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
    api_instance = sapliy_fintech.generated.FlowServiceApi(api_client)
    body = sapliy_fintech.generated.FlowCreateFlowRequest() # FlowCreateFlowRequest | 

    try:
        api_response = api_instance.flow_service_create_flow(body)
        print("The response of FlowServiceApi->flow_service_create_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowServiceApi->flow_service_create_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FlowCreateFlowRequest**](FlowCreateFlowRequest.md)|  | 

### Return type

[**FlowFlow**](FlowFlow.md)

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

# **flow_service_get_execution**
> FlowFlowExecution flow_service_get_execution(id)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.flow_flow_execution import FlowFlowExecution
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
    api_instance = sapliy_fintech.generated.FlowServiceApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.flow_service_get_execution(id)
        print("The response of FlowServiceApi->flow_service_get_execution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowServiceApi->flow_service_get_execution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FlowFlowExecution**](FlowFlowExecution.md)

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

# **flow_service_get_flow**
> FlowFlow flow_service_get_flow(id)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.flow_flow import FlowFlow
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
    api_instance = sapliy_fintech.generated.FlowServiceApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.flow_service_get_flow(id)
        print("The response of FlowServiceApi->flow_service_get_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowServiceApi->flow_service_get_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FlowFlow**](FlowFlow.md)

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

# **flow_service_list_flows**
> FlowListFlowsResponse flow_service_list_flows(zone_id=zone_id)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.flow_list_flows_response import FlowListFlowsResponse
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
    api_instance = sapliy_fintech.generated.FlowServiceApi(api_client)
    zone_id = 'zone_id_example' # str |  (optional)

    try:
        api_response = api_instance.flow_service_list_flows(zone_id=zone_id)
        print("The response of FlowServiceApi->flow_service_list_flows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowServiceApi->flow_service_list_flows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**|  | [optional] 

### Return type

[**FlowListFlowsResponse**](FlowListFlowsResponse.md)

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

# **flow_service_resume_execution**
> FlowResumeExecutionResponse flow_service_resume_execution(execution_id, body)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.flow_resume_execution_response import FlowResumeExecutionResponse
from sapliy_fintech.generated.models.flow_service_resume_execution_body import FlowServiceResumeExecutionBody
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
    api_instance = sapliy_fintech.generated.FlowServiceApi(api_client)
    execution_id = 'execution_id_example' # str | 
    body = sapliy_fintech.generated.FlowServiceResumeExecutionBody() # FlowServiceResumeExecutionBody | 

    try:
        api_response = api_instance.flow_service_resume_execution(execution_id, body)
        print("The response of FlowServiceApi->flow_service_resume_execution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowServiceApi->flow_service_resume_execution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**|  | 
 **body** | [**FlowServiceResumeExecutionBody**](FlowServiceResumeExecutionBody.md)|  | 

### Return type

[**FlowResumeExecutionResponse**](FlowResumeExecutionResponse.md)

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

# **flow_service_update_flow**
> FlowFlow flow_service_update_flow(id, body)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.flow_flow import FlowFlow
from sapliy_fintech.generated.models.flow_service_update_flow_body import FlowServiceUpdateFlowBody
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
    api_instance = sapliy_fintech.generated.FlowServiceApi(api_client)
    id = 'id_example' # str | 
    body = sapliy_fintech.generated.FlowServiceUpdateFlowBody() # FlowServiceUpdateFlowBody | 

    try:
        api_response = api_instance.flow_service_update_flow(id, body)
        print("The response of FlowServiceApi->flow_service_update_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowServiceApi->flow_service_update_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**FlowServiceUpdateFlowBody**](FlowServiceUpdateFlowBody.md)|  | 

### Return type

[**FlowFlow**](FlowFlow.md)

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

