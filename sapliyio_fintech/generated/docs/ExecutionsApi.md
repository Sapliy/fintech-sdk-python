# sapliyio_fintech.generated.ExecutionsApi

All URIs are relative to *https://api.sapliy.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_execution**](ExecutionsApi.md#get_execution) | **GET** /v1/executions/{executionId} | Get Execution details
[**resume_execution**](ExecutionsApi.md#resume_execution) | **POST** /v1/executions/{executionId}/resume | Resume a paused Execution


# **get_execution**
> AutomationFlowExecution get_execution(execution_id)

Get Execution details

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.automation_flow_execution import AutomationFlowExecution
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
    api_instance = sapliyio_fintech.generated.ExecutionsApi(api_client)
    execution_id = 'execution_id_example' # str | 

    try:
        # Get Execution details
        api_response = api_instance.get_execution(execution_id)
        print("The response of ExecutionsApi->get_execution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExecutionsApi->get_execution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**|  | 

### Return type

[**AutomationFlowExecution**](AutomationFlowExecution.md)

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

# **resume_execution**
> ResumeExecution200Response resume_execution(execution_id, request_body=request_body)

Resume a paused Execution

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.resume_execution200_response import ResumeExecution200Response
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
    api_instance = sapliyio_fintech.generated.ExecutionsApi(api_client)
    execution_id = 'execution_id_example' # str | 
    request_body = None # Dict[str, object] |  (optional)

    try:
        # Resume a paused Execution
        api_response = api_instance.resume_execution(execution_id, request_body=request_body)
        print("The response of ExecutionsApi->resume_execution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExecutionsApi->resume_execution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | [optional] 

### Return type

[**ResumeExecution200Response**](ResumeExecution200Response.md)

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

