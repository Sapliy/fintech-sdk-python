# sapliyio_fintech.generated.AuthApi

All URIs are relative to *https://api.sapliy.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_auth_login_post**](AuthApi.md#v1_auth_login_post) | **POST** /v1/auth/login | Login
[**v1_auth_register_post**](AuthApi.md#v1_auth_register_post) | **POST** /v1/auth/register | Register a new user


# **v1_auth_login_post**
> V1AuthRegisterPost201Response v1_auth_login_post(v1_auth_register_post_request)

Login

### Example


```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.v1_auth_register_post201_response import V1AuthRegisterPost201Response
from sapliyio_fintech.generated.models.v1_auth_register_post_request import V1AuthRegisterPostRequest
from sapliyio_fintech.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sapliy.io
# See configuration.py for a list of all supported configuration parameters.
configuration = sapliyio_fintech.generated.Configuration(
    host = "https://api.sapliy.io"
)


# Enter a context with an instance of the API client
with sapliyio_fintech.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sapliyio_fintech.generated.AuthApi(api_client)
    v1_auth_register_post_request = sapliyio_fintech.generated.V1AuthRegisterPostRequest() # V1AuthRegisterPostRequest | 

    try:
        # Login
        api_response = api_instance.v1_auth_login_post(v1_auth_register_post_request)
        print("The response of AuthApi->v1_auth_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->v1_auth_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_auth_register_post_request** | [**V1AuthRegisterPostRequest**](V1AuthRegisterPostRequest.md)|  | 

### Return type

[**V1AuthRegisterPost201Response**](V1AuthRegisterPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_register_post**
> V1AuthRegisterPost201Response v1_auth_register_post(v1_auth_register_post_request)

Register a new user

### Example


```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.v1_auth_register_post201_response import V1AuthRegisterPost201Response
from sapliyio_fintech.generated.models.v1_auth_register_post_request import V1AuthRegisterPostRequest
from sapliyio_fintech.generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sapliy.io
# See configuration.py for a list of all supported configuration parameters.
configuration = sapliyio_fintech.generated.Configuration(
    host = "https://api.sapliy.io"
)


# Enter a context with an instance of the API client
with sapliyio_fintech.generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sapliyio_fintech.generated.AuthApi(api_client)
    v1_auth_register_post_request = sapliyio_fintech.generated.V1AuthRegisterPostRequest() # V1AuthRegisterPostRequest | 

    try:
        # Register a new user
        api_response = api_instance.v1_auth_register_post(v1_auth_register_post_request)
        print("The response of AuthApi->v1_auth_register_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->v1_auth_register_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_auth_register_post_request** | [**V1AuthRegisterPostRequest**](V1AuthRegisterPostRequest.md)|  | 

### Return type

[**V1AuthRegisterPost201Response**](V1AuthRegisterPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

