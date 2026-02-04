# sapliy_fintech.generated.ZoneServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zone_service_bulk_update_metadata**](ZoneServiceApi.md#zone_service_bulk_update_metadata) | **POST** /v1/zones/bulk-metadata | 
[**zone_service_create_zone**](ZoneServiceApi.md#zone_service_create_zone) | **POST** /v1/zones | 
[**zone_service_get_zone**](ZoneServiceApi.md#zone_service_get_zone) | **GET** /v1/zones/{id} | 
[**zone_service_list_zones**](ZoneServiceApi.md#zone_service_list_zones) | **GET** /v1/zones | 
[**zone_service_update_zone**](ZoneServiceApi.md#zone_service_update_zone) | **PUT** /v1/zones/{id} | 


# **zone_service_bulk_update_metadata**
> ZoneBulkUpdateMetadataResponse zone_service_bulk_update_metadata(body)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.zone_bulk_update_metadata_request import ZoneBulkUpdateMetadataRequest
from sapliy_fintech.generated.models.zone_bulk_update_metadata_response import ZoneBulkUpdateMetadataResponse
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
    api_instance = sapliy_fintech.generated.ZoneServiceApi(api_client)
    body = sapliy_fintech.generated.ZoneBulkUpdateMetadataRequest() # ZoneBulkUpdateMetadataRequest | 

    try:
        api_response = api_instance.zone_service_bulk_update_metadata(body)
        print("The response of ZoneServiceApi->zone_service_bulk_update_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZoneServiceApi->zone_service_bulk_update_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ZoneBulkUpdateMetadataRequest**](ZoneBulkUpdateMetadataRequest.md)|  | 

### Return type

[**ZoneBulkUpdateMetadataResponse**](ZoneBulkUpdateMetadataResponse.md)

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

# **zone_service_create_zone**
> ZoneZone zone_service_create_zone(body)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.zone_create_zone_request import ZoneCreateZoneRequest
from sapliy_fintech.generated.models.zone_zone import ZoneZone
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
    api_instance = sapliy_fintech.generated.ZoneServiceApi(api_client)
    body = sapliy_fintech.generated.ZoneCreateZoneRequest() # ZoneCreateZoneRequest | 

    try:
        api_response = api_instance.zone_service_create_zone(body)
        print("The response of ZoneServiceApi->zone_service_create_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZoneServiceApi->zone_service_create_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ZoneCreateZoneRequest**](ZoneCreateZoneRequest.md)|  | 

### Return type

[**ZoneZone**](ZoneZone.md)

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

# **zone_service_get_zone**
> ZoneZone zone_service_get_zone(id)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.zone_zone import ZoneZone
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
    api_instance = sapliy_fintech.generated.ZoneServiceApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.zone_service_get_zone(id)
        print("The response of ZoneServiceApi->zone_service_get_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZoneServiceApi->zone_service_get_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ZoneZone**](ZoneZone.md)

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

# **zone_service_list_zones**
> ZoneListZonesResponse zone_service_list_zones(org_id=org_id)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.zone_list_zones_response import ZoneListZonesResponse
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
    api_instance = sapliy_fintech.generated.ZoneServiceApi(api_client)
    org_id = 'org_id_example' # str |  (optional)

    try:
        api_response = api_instance.zone_service_list_zones(org_id=org_id)
        print("The response of ZoneServiceApi->zone_service_list_zones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZoneServiceApi->zone_service_list_zones: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | [optional] 

### Return type

[**ZoneListZonesResponse**](ZoneListZonesResponse.md)

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

# **zone_service_update_zone**
> ZoneZone zone_service_update_zone(id, body)

### Example


```python
import sapliy_fintech.generated
from sapliy_fintech.generated.models.zone_service_update_zone_body import ZoneServiceUpdateZoneBody
from sapliy_fintech.generated.models.zone_zone import ZoneZone
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
    api_instance = sapliy_fintech.generated.ZoneServiceApi(api_client)
    id = 'id_example' # str | 
    body = sapliy_fintech.generated.ZoneServiceUpdateZoneBody() # ZoneServiceUpdateZoneBody | 

    try:
        api_response = api_instance.zone_service_update_zone(id, body)
        print("The response of ZoneServiceApi->zone_service_update_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZoneServiceApi->zone_service_update_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**ZoneServiceUpdateZoneBody**](ZoneServiceUpdateZoneBody.md)|  | 

### Return type

[**ZoneZone**](ZoneZone.md)

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

