# sapliy_fintech.PaymentServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_service_confirm_payment_intent**](PaymentServiceApi.md#payment_service_confirm_payment_intent) | **POST** /v1/payments/intents/{id}/confirm | 
[**payment_service_create_payment_intent**](PaymentServiceApi.md#payment_service_create_payment_intent) | **POST** /v1/payments/intents | 
[**payment_service_refund_payment_intent**](PaymentServiceApi.md#payment_service_refund_payment_intent) | **POST** /v1/payments/intents/{id}/refund | 


# **payment_service_confirm_payment_intent**
> PaymentsPaymentIntent payment_service_confirm_payment_intent(id, body)

### Example


```python
import sapliy_fintech
from sapliy_fintech.models.payment_service_confirm_payment_intent_body import PaymentServiceConfirmPaymentIntentBody
from sapliy_fintech.models.payments_payment_intent import PaymentsPaymentIntent
from sapliy_fintech.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sapliy_fintech.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sapliy_fintech.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sapliy_fintech.PaymentServiceApi(api_client)
    id = 'id_example' # str | 
    body = sapliy_fintech.PaymentServiceConfirmPaymentIntentBody() # PaymentServiceConfirmPaymentIntentBody | 

    try:
        api_response = api_instance.payment_service_confirm_payment_intent(id, body)
        print("The response of PaymentServiceApi->payment_service_confirm_payment_intent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentServiceApi->payment_service_confirm_payment_intent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**PaymentServiceConfirmPaymentIntentBody**](PaymentServiceConfirmPaymentIntentBody.md)|  | 

### Return type

[**PaymentsPaymentIntent**](PaymentsPaymentIntent.md)

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

# **payment_service_create_payment_intent**
> PaymentsPaymentIntent payment_service_create_payment_intent(body)

### Example


```python
import sapliy_fintech
from sapliy_fintech.models.payments_create_payment_intent_request import PaymentsCreatePaymentIntentRequest
from sapliy_fintech.models.payments_payment_intent import PaymentsPaymentIntent
from sapliy_fintech.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sapliy_fintech.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sapliy_fintech.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sapliy_fintech.PaymentServiceApi(api_client)
    body = sapliy_fintech.PaymentsCreatePaymentIntentRequest() # PaymentsCreatePaymentIntentRequest | 

    try:
        api_response = api_instance.payment_service_create_payment_intent(body)
        print("The response of PaymentServiceApi->payment_service_create_payment_intent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentServiceApi->payment_service_create_payment_intent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentsCreatePaymentIntentRequest**](PaymentsCreatePaymentIntentRequest.md)|  | 

### Return type

[**PaymentsPaymentIntent**](PaymentsPaymentIntent.md)

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

# **payment_service_refund_payment_intent**
> PaymentsPaymentIntent payment_service_refund_payment_intent(id, body)

### Example


```python
import sapliy_fintech
from sapliy_fintech.models.payments_payment_intent import PaymentsPaymentIntent
from sapliy_fintech.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sapliy_fintech.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sapliy_fintech.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sapliy_fintech.PaymentServiceApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.payment_service_refund_payment_intent(id, body)
        print("The response of PaymentServiceApi->payment_service_refund_payment_intent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentServiceApi->payment_service_refund_payment_intent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**PaymentsPaymentIntent**](PaymentsPaymentIntent.md)

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

