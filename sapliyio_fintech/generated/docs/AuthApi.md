# sapliyio_fintech.generated.AuthApi

All URIs are relative to *https://api.sapliy.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_user**](AuthApi.md#login_user) | **POST** /v1/auth/login | Login
[**register_user**](AuthApi.md#register_user) | **POST** /v1/auth/register | Register a new user
[**validate_key**](AuthApi.md#validate_key) | **POST** /v1/auth/validate | Validate an API key


# **login_user**
> RegisterUser201Response login_user(register_user_request)

Login

### Example


```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.register_user201_response import RegisterUser201Response
from sapliyio_fintech.generated.models.register_user_request import RegisterUserRequest
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
    register_user_request = sapliyio_fintech.generated.RegisterUserRequest() # RegisterUserRequest | 

    try:
        # Login
        api_response = api_instance.login_user(register_user_request)
        print("The response of AuthApi->login_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->login_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_user_request** | [**RegisterUserRequest**](RegisterUserRequest.md)|  | 

### Return type

[**RegisterUser201Response**](RegisterUser201Response.md)

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

# **register_user**
> RegisterUser201Response register_user(register_user_request)

Register a new user

### Example


```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.register_user201_response import RegisterUser201Response
from sapliyio_fintech.generated.models.register_user_request import RegisterUserRequest
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
    register_user_request = sapliyio_fintech.generated.RegisterUserRequest() # RegisterUserRequest | 

    try:
        # Register a new user
        api_response = api_instance.register_user(register_user_request)
        print("The response of AuthApi->register_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->register_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_user_request** | [**RegisterUserRequest**](RegisterUserRequest.md)|  | 

### Return type

[**RegisterUser201Response**](RegisterUser201Response.md)

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

# **validate_key**
> ValidateKey200Response validate_key(validate_key_request)

Validate an API key

### Example


```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.validate_key200_response import ValidateKey200Response
from sapliyio_fintech.generated.models.validate_key_request import ValidateKeyRequest
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
    validate_key_request = sapliyio_fintech.generated.ValidateKeyRequest() # ValidateKeyRequest | 

    try:
        # Validate an API key
        api_response = api_instance.validate_key(validate_key_request)
        print("The response of AuthApi->validate_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->validate_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_key_request** | [**ValidateKeyRequest**](ValidateKeyRequest.md)|  | 

### Return type

[**ValidateKey200Response**](ValidateKey200Response.md)

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

