# trieve_python_client.TopicApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_topic**](TopicApi.md#create_topic) | **POST** /api/topic | Create Topic
[**delete_topic**](TopicApi.md#delete_topic) | **DELETE** /api/topic | Delete Topic
[**get_all_topics_for_user**](TopicApi.md#get_all_topics_for_user) | **GET** /api/topic/user/{user_id} | Get All Topics for User
[**update_topic**](TopicApi.md#update_topic) | **PUT** /api/topic | Update Topic


# **create_topic**
> Topic create_topic(tr_dataset, create_topic_data)

Create Topic

Create Topic  Create a new chat topic. Topics are attached to a user and act as a coordinator for memory of gen-AI chat sessions. We are considering refactoring this resource of the API soon.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_python_client
from trieve_python_client.models.create_topic_data import CreateTopicData
from trieve_python_client.models.topic import Topic
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
    api_instance = trieve_python_client.TopicApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    create_topic_data = trieve_python_client.CreateTopicData() # CreateTopicData | JSON request payload to create chat topic

    try:
        # Create Topic
        api_response = api_instance.create_topic(tr_dataset, create_topic_data)
        print("The response of TopicApi->create_topic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TopicApi->create_topic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **create_topic_data** | [**CreateTopicData**](CreateTopicData.md)| JSON request payload to create chat topic | 

### Return type

[**Topic**](Topic.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The JSON response payload containing the created topic |  -  |
**400** | Topic name empty or a service error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_topic**
> delete_topic(tr_dataset, delete_topic_data)

Delete Topic

Delete Topic  Delete an existing chat topic. When a topic is deleted, all associated chat messages are also deleted.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_python_client
from trieve_python_client.models.delete_topic_data import DeleteTopicData
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
    api_instance = trieve_python_client.TopicApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    delete_topic_data = trieve_python_client.DeleteTopicData() # DeleteTopicData | JSON request payload to delete a chat topic

    try:
        # Delete Topic
        api_instance.delete_topic(tr_dataset, delete_topic_data)
    except Exception as e:
        print("Exception when calling TopicApi->delete_topic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **delete_topic_data** | [**DeleteTopicData**](DeleteTopicData.md)| JSON request payload to delete a chat topic | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Confirmation that the topic was deleted |  -  |
**400** | Service error relating to topic deletion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_topics_for_user**
> List[Topic] get_all_topics_for_user(user_id, tr_dataset)

Get All Topics for User

Get All Topics for User  Get all topics belonging to a the auth'ed user. Soon, we plan to allow specification of the user for this route and include pagination.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_python_client
from trieve_python_client.models.topic import Topic
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
    api_instance = trieve_python_client.TopicApi(api_client)
    user_id = 'user_id_example' # str | The id of the user to get topics for
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request

    try:
        # Get All Topics for User
        api_response = api_instance.get_all_topics_for_user(user_id, tr_dataset)
        print("The response of TopicApi->get_all_topics_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TopicApi->get_all_topics_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user to get topics for | 
 **tr_dataset** | **str**| The dataset id to use for the request | 

### Return type

[**List[Topic]**](Topic.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All topics belonging to a given user |  -  |
**400** | Service error relating to topic get |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_topic**
> update_topic(tr_dataset, update_topic_data)

Update Topic

Update Topic  Update an existing chat topic. Currently, only the name of the topic can be updated.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_python_client
from trieve_python_client.models.update_topic_data import UpdateTopicData
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
    api_instance = trieve_python_client.TopicApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    update_topic_data = trieve_python_client.UpdateTopicData() # UpdateTopicData | JSON request payload to update a chat topic

    try:
        # Update Topic
        api_instance.update_topic(tr_dataset, update_topic_data)
    except Exception as e:
        print("Exception when calling TopicApi->update_topic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **update_topic_data** | [**UpdateTopicData**](UpdateTopicData.md)| JSON request payload to update a chat topic | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Confirmation that the topic was updated |  -  |
**400** | Service error relating to topic update |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

