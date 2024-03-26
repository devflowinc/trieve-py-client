# trieve_python_client.EventsApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_events**](EventsApi.md#get_events) | **POST** /api/events | Get events for the dataset


# **get_events**
> EventReturn get_events(tr_dataset, get_events_data)

Get events for the dataset

Get events for the dataset  Get events for the auth'ed user. Currently, this is only for events belonging to the auth'ed user. Soon, we plan to associate events to datasets instead of users.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_python_client
from trieve_python_client.models.event_return import EventReturn
from trieve_python_client.models.get_events_data import GetEventsData
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
    api_instance = trieve_python_client.EventsApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    get_events_data = trieve_python_client.GetEventsData() # GetEventsData | JSON request payload to get events for a dataset

    try:
        # Get events for the dataset
        api_response = api_instance.get_events(tr_dataset, get_events_data)
        print("The response of EventsApi->get_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **get_events_data** | [**GetEventsData**](GetEventsData.md)| JSON request payload to get events for a dataset | 

### Return type

[**EventReturn**](EventReturn.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Events for the dataset |  -  |
**400** | Service error relating to getting events for the dataset |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

