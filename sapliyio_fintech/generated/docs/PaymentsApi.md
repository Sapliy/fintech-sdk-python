# sapliyio_fintech.generated.PaymentsApi

All URIs are relative to *https://api.sapliy.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_payment_intent**](PaymentsApi.md#confirm_payment_intent) | **POST** /v1/payments/intents/{id}/confirm | Confirm a Payment Intent
[**create_payment_intent**](PaymentsApi.md#create_payment_intent) | **POST** /v1/payments | Create a Payment Intent


# **confirm_payment_intent**
> PaymentIntent confirm_payment_intent(id, x_zone_id, x_zone_mode=x_zone_mode, confirm_payment_intent_request=confirm_payment_intent_request)

Confirm a Payment Intent

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.confirm_payment_intent_request import ConfirmPaymentIntentRequest
from sapliyio_fintech.generated.models.payment_intent import PaymentIntent
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
    api_instance = sapliyio_fintech.generated.PaymentsApi(api_client)
    id = 'id_example' # str | 
    x_zone_id = 'x_zone_id_example' # str | The ID of the zone for this request.
    x_zone_mode = 'x_zone_mode_example' # str | The mode of the zone (live or test). (optional)
    confirm_payment_intent_request = sapliyio_fintech.generated.ConfirmPaymentIntentRequest() # ConfirmPaymentIntentRequest |  (optional)

    try:
        # Confirm a Payment Intent
        api_response = api_instance.confirm_payment_intent(id, x_zone_id, x_zone_mode=x_zone_mode, confirm_payment_intent_request=confirm_payment_intent_request)
        print("The response of PaymentsApi->confirm_payment_intent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->confirm_payment_intent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_zone_id** | **str**| The ID of the zone for this request. | 
 **x_zone_mode** | **str**| The mode of the zone (live or test). | [optional] 
 **confirm_payment_intent_request** | [**ConfirmPaymentIntentRequest**](ConfirmPaymentIntentRequest.md)|  | [optional] 

### Return type

[**PaymentIntent**](PaymentIntent.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirmed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payment_intent**
> PaymentIntent create_payment_intent(x_zone_id, create_payment_intent_request, x_zone_mode=x_zone_mode)

Create a Payment Intent

### Example

* Bearer Authentication (ApiKeyAuth):

```python
import sapliyio_fintech.generated
from sapliyio_fintech.generated.models.create_payment_intent_request import CreatePaymentIntentRequest
from sapliyio_fintech.generated.models.payment_intent import PaymentIntent
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
    api_instance = sapliyio_fintech.generated.PaymentsApi(api_client)
    x_zone_id = 'x_zone_id_example' # str | The ID of the zone for this request.
    create_payment_intent_request = sapliyio_fintech.generated.CreatePaymentIntentRequest() # CreatePaymentIntentRequest | 
    x_zone_mode = 'x_zone_mode_example' # str | The mode of the zone (live or test). (optional)

    try:
        # Create a Payment Intent
        api_response = api_instance.create_payment_intent(x_zone_id, create_payment_intent_request, x_zone_mode=x_zone_mode)
        print("The response of PaymentsApi->create_payment_intent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->create_payment_intent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_zone_id** | **str**| The ID of the zone for this request. | 
 **create_payment_intent_request** | [**CreatePaymentIntentRequest**](CreatePaymentIntentRequest.md)|  | 
 **x_zone_mode** | **str**| The mode of the zone (live or test). | [optional] 

### Return type

[**PaymentIntent**](PaymentIntent.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Invalid request parameters. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

