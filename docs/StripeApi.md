# trieve_python_client.StripeApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_subscription**](StripeApi.md#cancel_subscription) | **DELETE** /api/stripe/subscription/{subscription_id} | Cancel Subscription
[**direct_to_payment_link**](StripeApi.md#direct_to_payment_link) | **GET** /api/stripe/payment_link/{plan_id}/{organization_id} | Checkout
[**get_all_plans**](StripeApi.md#get_all_plans) | **GET** /api/stripe/plans | Get All Plans
[**update_subscription_plan**](StripeApi.md#update_subscription_plan) | **PATCH** /api/stripe/subscription_plan/{subscription_id}/{plan_id} | Update Subscription Plan


# **cancel_subscription**
> cancel_subscription(tr_organization, subscription_id)

Cancel Subscription

Cancel Subscription  Cancel a subscription by its id

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_python_client
from trieve_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8090
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_python_client.Configuration(
    host = "http://localhost:8090"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with trieve_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_python_client.StripeApi(api_client)
    tr_organization = 'tr_organization_example' # str | The organization id to use for the request
    subscription_id = 'subscription_id_example' # str | id of the subscription you want to cancel

    try:
        # Cancel Subscription
        api_instance.cancel_subscription(tr_organization, subscription_id)
    except Exception as e:
        print("Exception when calling StripeApi->cancel_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_organization** | **str**| The organization id to use for the request | 
 **subscription_id** | **str**| id of the subscription you want to cancel | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirmation that the subscription was cancelled |  -  |
**400** | Service error relating to creating a URL for a stripe checkout page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **direct_to_payment_link**
> direct_to_payment_link(plan_id, organization_id)

Checkout

Checkout  Get a direct link to the stripe checkout page for the plan and organization

### Example


```python
import trieve_python_client
from trieve_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8090
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_python_client.Configuration(
    host = "http://localhost:8090"
)


# Enter a context with an instance of the API client
with trieve_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_python_client.StripeApi(api_client)
    plan_id = 'plan_id_example' # str | id of the plan you want to subscribe to
    organization_id = 'organization_id_example' # str | id of the organization you want to subscribe to the plan

    try:
        # Checkout
        api_instance.direct_to_payment_link(plan_id, organization_id)
    except Exception as e:
        print("Exception when calling StripeApi->direct_to_payment_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**| id of the plan you want to subscribe to | 
 **organization_id** | **str**| id of the organization you want to subscribe to the plan | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**303** | SeeOther response redirecting user to stripe checkout page |  -  |
**400** | Service error relating to creating a URL for a stripe checkout page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_plans**
> List[StripePlan] get_all_plans()

Get All Plans

Get All Plans  Get a list of all plans

### Example


```python
import trieve_python_client
from trieve_python_client.models.stripe_plan import StripePlan
from trieve_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8090
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_python_client.Configuration(
    host = "http://localhost:8090"
)


# Enter a context with an instance of the API client
with trieve_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_python_client.StripeApi(api_client)

    try:
        # Get All Plans
        api_response = api_instance.get_all_plans()
        print("The response of StripeApi->get_all_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->get_all_plans: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[StripePlan]**](StripePlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all plans |  -  |
**400** | Service error relating to getting all plans |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscription_plan**
> update_subscription_plan(tr_organization, subscription_id, plan_id)

Update Subscription Plan

Update Subscription Plan  Update a subscription to a new plan

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_python_client
from trieve_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8090
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_python_client.Configuration(
    host = "http://localhost:8090"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with trieve_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_python_client.StripeApi(api_client)
    tr_organization = 'tr_organization_example' # str | The organization id to use for the request
    subscription_id = 'subscription_id_example' # str | id of the subscription you want to update
    plan_id = 'plan_id_example' # str | id of the plan you want to subscribe to

    try:
        # Update Subscription Plan
        api_instance.update_subscription_plan(tr_organization, subscription_id, plan_id)
    except Exception as e:
        print("Exception when calling StripeApi->update_subscription_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_organization** | **str**| The organization id to use for the request | 
 **subscription_id** | **str**| id of the subscription you want to update | 
 **plan_id** | **str**| id of the plan you want to subscribe to | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirmation that the subscription was updated to the new plan |  -  |
**400** | Service error relating to updating the subscription to the new plan |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

