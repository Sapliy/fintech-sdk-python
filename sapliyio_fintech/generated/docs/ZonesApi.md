# sapliyio_fintech.generated.ZonesApi

All URIs are relative to *https://api.sapliy.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_zone**](ZonesApi.md#create_zone) | **POST** /v1/zones | Create a Zone
[**list_zones**](ZonesApi.md#list_zones) | **GET** /v1/zones | List or Get Zones


# **create_zone**
> ListZones200ResponseInner create_zone(create_zone_request)

Create a Zone

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.create_zone_request import CreateZoneRequest
from sapliyio_fintech.generated.models.list_zones200_response_inner import ListZones200ResponseInner
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
    api_instance = sapliyio_fintech.generated.ZonesApi(api_client)
    create_zone_request = sapliyio_fintech.generated.CreateZoneRequest() # CreateZoneRequest | 

    try:
        # Create a Zone
        api_response = api_instance.create_zone(create_zone_request)
        print("The response of ZonesApi->create_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonesApi->create_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_zone_request** | [**CreateZoneRequest**](CreateZoneRequest.md)|  | 

### Return type

[**ListZones200ResponseInner**](ListZones200ResponseInner.md)

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

# **list_zones**
> List[ListZones200ResponseInner] list_zones(org_id=org_id, id=id)

List or Get Zones

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.list_zones200_response_inner import ListZones200ResponseInner
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
    api_instance = sapliyio_fintech.generated.ZonesApi(api_client)
    org_id = 'org_id_example' # str |  (optional)
    id = 'id_example' # str |  (optional)

    try:
        # List or Get Zones
        api_response = api_instance.list_zones(org_id=org_id, id=id)
        print("The response of ZonesApi->list_zones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonesApi->list_zones: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 

### Return type

[**List[ListZones200ResponseInner]**](ListZones200ResponseInner.md)

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

