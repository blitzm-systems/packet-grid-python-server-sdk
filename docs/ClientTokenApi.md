# blitzm_packetgrid_sdk.ClientTokenApi

All URIs are relative to *http://http:/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_token**](ClientTokenApi.md#create_client_token) | **POST** /client-tokens/ | create a client token for a mobile device. If a duplicated user_id is provided, the server could probably create a new token or return the existig token. 


# **create_client_token**
> ClientToken create_client_token(body)

create a client token for a mobile device. If a duplicated user_id is provided, the server could probably create a new token or return the existig token. 

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
api_instance = blitzm_packetgrid_sdk.ClientTokenApi(blitzm_packetgrid_sdk.ApiClient(configuration))
body = blitzm_packetgrid_sdk.CreateClientToken() # CreateClientToken | the account id from the client side

try:
    # create a client token for a mobile device. If a duplicated user_id is provided, the server could probably create a new token or return the existig token. 
    api_response = api_instance.create_client_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientTokenApi->create_client_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateClientToken**](CreateClientToken.md)| the account id from the client side | 

### Return type

[**ClientToken**](ClientToken.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

