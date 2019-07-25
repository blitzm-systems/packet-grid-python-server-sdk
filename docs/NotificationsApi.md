# blitzm_packetgrid_sdk.NotificationsApi

All URIs are relative to *http://http:/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send**](NotificationsApi.md#send) | **POST** /notifications/send/ | 


# **send**
> DispatchReport send(command, idempotency_key=idempotency_key)



### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import blitzm_packetgrid_sdk
from blitzm_packetgrid_sdk.rest import ApiException
from pprint import pprint
configuration = blitzm_packetgrid_sdk.Configuration()
# Configure API key authorization: Token
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = blitzm_packetgrid_sdk.NotificationsApi(blitzm_packetgrid_sdk.ApiClient(configuration))
command = blitzm_packetgrid_sdk.SendNotification() # SendNotification | 
idempotency_key = 'idempotency_key_example' # str | This header can optionally be provided to ensure duplicate requests are ignored. The value of this header must be key (string) that uniquely identifies the API request. If the service receives a request with a duplicate Idempotency-Key value it will return a cached response to ensure that any side effects the request might have are not duplicated. Idempotency-Keys are cached for 24 hours. API Clients are advised to make use of Idempotency-Keys for API requests that implement failure-retries.  (optional)

try:
    api_response = api_instance.send(command, idempotency_key=idempotency_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | [**SendNotification**](SendNotification.md)|  | 
 **idempotency_key** | **str**| This header can optionally be provided to ensure duplicate requests are ignored. The value of this header must be key (string) that uniquely identifies the API request. If the service receives a request with a duplicate Idempotency-Key value it will return a cached response to ensure that any side effects the request might have are not duplicated. Idempotency-Keys are cached for 24 hours. API Clients are advised to make use of Idempotency-Keys for API requests that implement failure-retries.  | [optional] 

### Return type

[**DispatchReport**](DispatchReport.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

