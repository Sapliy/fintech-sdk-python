# sapliy_fintech.generated.AuthServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_service_add_team_member**](AuthServiceApi.md#auth_service_add_team_member) | **POST** /v1/auth/teams/members | 
[**auth_service_create_sso_provider**](AuthServiceApi.md#auth_service_create_sso_provider) | **POST** /v1/auth/sso/providers | 
[**auth_service_get_audit_logs**](AuthServiceApi.md#auth_service_get_audit_logs) | **GET** /v1/auth/audit_logs | 
[**auth_service_get_sso_provider**](AuthServiceApi.md#auth_service_get_sso_provider) | **GET** /v1/auth/sso/providers/{id} | 
[**auth_service_initiate_sso**](AuthServiceApi.md#auth_service_initiate_sso) | **POST** /v1/auth/sso/initiate | 
[**auth_service_list_team_members**](AuthServiceApi.md#auth_service_list_team_members) | **GET** /v1/auth/teams/{orgId}/members | 
[**auth_service_remove_team_member**](AuthServiceApi.md#auth_service_remove_team_member) | **DELETE** /v1/auth/teams/members | 
[**auth_service_validate_key**](AuthServiceApi.md#auth_service_validate_key) | **POST** /v1/auth/validate | 
[**auth_service_validate_token**](AuthServiceApi.md#auth_service_validate_token) | **POST** /v1/auth/validate_token | 


# **auth_service_add_team_member**
> AuthMembership auth_service_add_team_member(body)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.auth_add_team_member_request import AuthAddTeamMemberRequest
from sapliy_fintech.generated.models.auth_membership import AuthMembership
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
    api_instance = sapliy_fintech.generated.AuthServiceApi(api_client)
    body = sapliy_fintech.generated.AuthAddTeamMemberRequest() # AuthAddTeamMemberRequest | 

    try:
        api_response = api_instance.auth_service_add_team_member(body)
        print("The response of AuthServiceApi->auth_service_add_team_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthServiceApi->auth_service_add_team_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthAddTeamMemberRequest**](AuthAddTeamMemberRequest.md)|  | 

### Return type

[**AuthMembership**](AuthMembership.md)

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

# **auth_service_create_sso_provider**
> AuthSSOProvider auth_service_create_sso_provider(body)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.auth_create_sso_provider_request import AuthCreateSSOProviderRequest
from sapliy_fintech.generated.models.auth_sso_provider import AuthSSOProvider
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
    api_instance = sapliy_fintech.generated.AuthServiceApi(api_client)
    body = sapliy_fintech.generated.AuthCreateSSOProviderRequest() # AuthCreateSSOProviderRequest | 

    try:
        api_response = api_instance.auth_service_create_sso_provider(body)
        print("The response of AuthServiceApi->auth_service_create_sso_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthServiceApi->auth_service_create_sso_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthCreateSSOProviderRequest**](AuthCreateSSOProviderRequest.md)|  | 

### Return type

[**AuthSSOProvider**](AuthSSOProvider.md)

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

# **auth_service_get_audit_logs**
> AuthGetAuditLogsResponse auth_service_get_audit_logs(org_id=org_id, limit=limit, offset=offset, action=action)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.auth_get_audit_logs_response import AuthGetAuditLogsResponse
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
    api_instance = sapliy_fintech.generated.AuthServiceApi(api_client)
    org_id = 'org_id_example' # str |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    action = 'action_example' # str |  (optional)

    try:
        api_response = api_instance.auth_service_get_audit_logs(org_id=org_id, limit=limit, offset=offset, action=action)
        print("The response of AuthServiceApi->auth_service_get_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthServiceApi->auth_service_get_audit_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **action** | **str**|  | [optional] 

### Return type

[**AuthGetAuditLogsResponse**](AuthGetAuditLogsResponse.md)

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

# **auth_service_get_sso_provider**
> AuthSSOProvider auth_service_get_sso_provider(id)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.auth_sso_provider import AuthSSOProvider
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
    api_instance = sapliy_fintech.generated.AuthServiceApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.auth_service_get_sso_provider(id)
        print("The response of AuthServiceApi->auth_service_get_sso_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthServiceApi->auth_service_get_sso_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**AuthSSOProvider**](AuthSSOProvider.md)

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

# **auth_service_initiate_sso**
> AuthInitiateSSOResponse auth_service_initiate_sso(body)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.auth_initiate_sso_request import AuthInitiateSSORequest
from sapliy_fintech.generated.models.auth_initiate_sso_response import AuthInitiateSSOResponse
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
    api_instance = sapliy_fintech.generated.AuthServiceApi(api_client)
    body = sapliy_fintech.generated.AuthInitiateSSORequest() # AuthInitiateSSORequest | 

    try:
        api_response = api_instance.auth_service_initiate_sso(body)
        print("The response of AuthServiceApi->auth_service_initiate_sso:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthServiceApi->auth_service_initiate_sso: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthInitiateSSORequest**](AuthInitiateSSORequest.md)|  | 

### Return type

[**AuthInitiateSSOResponse**](AuthInitiateSSOResponse.md)

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

# **auth_service_list_team_members**
> AuthListTeamMembersResponse auth_service_list_team_members(org_id)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.auth_list_team_members_response import AuthListTeamMembersResponse
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
    api_instance = sapliy_fintech.generated.AuthServiceApi(api_client)
    org_id = 'org_id_example' # str | 

    try:
        api_response = api_instance.auth_service_list_team_members(org_id)
        print("The response of AuthServiceApi->auth_service_list_team_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthServiceApi->auth_service_list_team_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 

### Return type

[**AuthListTeamMembersResponse**](AuthListTeamMembersResponse.md)

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

# **auth_service_remove_team_member**
> AuthRemoveTeamMemberResponse auth_service_remove_team_member(org_id=org_id, user_id=user_id)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.auth_remove_team_member_response import AuthRemoveTeamMemberResponse
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
    api_instance = sapliy_fintech.generated.AuthServiceApi(api_client)
    org_id = 'org_id_example' # str |  (optional)
    user_id = 'user_id_example' # str |  (optional)

    try:
        api_response = api_instance.auth_service_remove_team_member(org_id=org_id, user_id=user_id)
        print("The response of AuthServiceApi->auth_service_remove_team_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthServiceApi->auth_service_remove_team_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | [optional] 
 **user_id** | **str**|  | [optional] 

### Return type

[**AuthRemoveTeamMemberResponse**](AuthRemoveTeamMemberResponse.md)

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

# **auth_service_validate_key**
> AuthValidateKeyResponse auth_service_validate_key(body)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.auth_validate_key_request import AuthValidateKeyRequest
from sapliy_fintech.generated.models.auth_validate_key_response import AuthValidateKeyResponse
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
    api_instance = sapliy_fintech.generated.AuthServiceApi(api_client)
    body = sapliy_fintech.generated.AuthValidateKeyRequest() # AuthValidateKeyRequest | 

    try:
        api_response = api_instance.auth_service_validate_key(body)
        print("The response of AuthServiceApi->auth_service_validate_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthServiceApi->auth_service_validate_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthValidateKeyRequest**](AuthValidateKeyRequest.md)|  | 

### Return type

[**AuthValidateKeyResponse**](AuthValidateKeyResponse.md)

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

# **auth_service_validate_token**
> AuthValidateTokenResponse auth_service_validate_token(body)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.auth_validate_token_request import AuthValidateTokenRequest
from sapliy_fintech.generated.models.auth_validate_token_response import AuthValidateTokenResponse
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
    api_instance = sapliy_fintech.generated.AuthServiceApi(api_client)
    body = sapliy_fintech.generated.AuthValidateTokenRequest() # AuthValidateTokenRequest | 

    try:
        api_response = api_instance.auth_service_validate_token(body)
        print("The response of AuthServiceApi->auth_service_validate_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthServiceApi->auth_service_validate_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthValidateTokenRequest**](AuthValidateTokenRequest.md)|  | 

### Return type

[**AuthValidateTokenResponse**](AuthValidateTokenResponse.md)

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

