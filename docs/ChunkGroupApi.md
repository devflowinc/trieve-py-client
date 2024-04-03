# trieve_py_client.ChunkGroupApi

All URIs are relative to *https://api.trieve.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_chunk_to_group**](ChunkGroupApi.md#add_chunk_to_group) | **POST** /api/chunk_group/chunk/{group_id} | Add Chunk to Group
[**add_chunk_to_group_by_tracking_id**](ChunkGroupApi.md#add_chunk_to_group_by_tracking_id) | **POST** /api/chunk_group/tracking_id/{tracking_id} | Add Chunk to Group by Tracking ID
[**create_chunk_group**](ChunkGroupApi.md#create_chunk_group) | **POST** /api/chunk_group | Create Chunk Group
[**delete_chunk_group**](ChunkGroupApi.md#delete_chunk_group) | **DELETE** /api/chunk_group/{group_id} | Delete Group
[**delete_group_by_tracking_id**](ChunkGroupApi.md#delete_group_by_tracking_id) | **DELETE** /api/chunk_group/tracking_id/{tracking_id} | Delete Group by Tracking ID
[**get_chunk_group**](ChunkGroupApi.md#get_chunk_group) | **GET** /api/chunk_group/{group_id} | Get Group
[**get_chunks_in_group**](ChunkGroupApi.md#get_chunks_in_group) | **GET** /api/chunk_group/{group_id}/{page} | Get Chunks in Group
[**get_chunks_in_group_by_tracking_id**](ChunkGroupApi.md#get_chunks_in_group_by_tracking_id) | **GET** /api/chunk_group/tracking_id/{group_tracking_id}/{page} | Get Chunks in Group by Tracking ID
[**get_group_by_tracking_id**](ChunkGroupApi.md#get_group_by_tracking_id) | **GET** /api/chunk_group/tracking_id/{tracking_id} | Get Group by Tracking ID
[**get_groups_chunk_is_in**](ChunkGroupApi.md#get_groups_chunk_is_in) | **POST** /api/chunk_group/chunks | Get Groups for Chunks
[**get_recommended_groups**](ChunkGroupApi.md#get_recommended_groups) | **POST** /api/chunk_group/recommend | Get Recommended Groups
[**get_specific_dataset_chunk_groups**](ChunkGroupApi.md#get_specific_dataset_chunk_groups) | **GET** /api/dataset/groups/{dataset_id}/{page} | Get Groups for Dataset
[**remove_chunk_from_group**](ChunkGroupApi.md#remove_chunk_from_group) | **DELETE** /api/chunk_group/chunk/{group_id} | Remove Chunk from Group
[**search_over_groups**](ChunkGroupApi.md#search_over_groups) | **POST** /api/chunk_group/group_oriented_search | Search Over Groups
[**search_within_group**](ChunkGroupApi.md#search_within_group) | **POST** /api/chunk_group/search | Search Within Group
[**update_chunk_group**](ChunkGroupApi.md#update_chunk_group) | **PUT** /api/chunk_group | Update Group
[**update_group_by_tracking_id**](ChunkGroupApi.md#update_group_by_tracking_id) | **PUT** /api/chunk_group/tracking_id/{tracking_id} | Update Group by Tracking ID


# **add_chunk_to_group**
> add_chunk_to_group(tr_dataset, group_id, add_chunk_to_group_data)

Add Chunk to Group

Add Chunk to Group  Route to add a chunk to a group.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.add_chunk_to_group_data import AddChunkToGroupData
from trieve_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trieve.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_py_client.Configuration(
    host = "https://api.trieve.ai"
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
with trieve_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_py_client.ChunkGroupApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    group_id = 'group_id_example' # str | Id of the group to add the chunk to as a bookmark
    add_chunk_to_group_data = trieve_py_client.AddChunkToGroupData() # AddChunkToGroupData | JSON request payload to add a chunk to a group (bookmark it)

    try:
        # Add Chunk to Group
        api_instance.add_chunk_to_group(tr_dataset, group_id, add_chunk_to_group_data)
    except Exception as e:
        print("Exception when calling ChunkGroupApi->add_chunk_to_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **group_id** | **str**| Id of the group to add the chunk to as a bookmark | 
 **add_chunk_to_group_data** | [**AddChunkToGroupData**](AddChunkToGroupData.md)| JSON request payload to add a chunk to a group (bookmark it) | 

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
**204** | Confirmation that the chunk was added to the group (bookmark&#39;ed). |  -  |
**400** | Service error relating to getting the groups that the chunk is in. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_chunk_to_group_by_tracking_id**
> add_chunk_to_group_by_tracking_id(tr_dataset, tracking_id, add_chunk_to_group_data)

Add Chunk to Group by Tracking ID

Add Chunk to Group by Tracking ID  Route to add a chunk to a group by tracking id.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.add_chunk_to_group_data import AddChunkToGroupData
from trieve_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trieve.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_py_client.Configuration(
    host = "https://api.trieve.ai"
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
with trieve_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_py_client.ChunkGroupApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    tracking_id = 'tracking_id_example' # str | Id of the group to add the chunk to as a bookmark
    add_chunk_to_group_data = trieve_py_client.AddChunkToGroupData() # AddChunkToGroupData | JSON request payload to add a chunk to a group (bookmark it)

    try:
        # Add Chunk to Group by Tracking ID
        api_instance.add_chunk_to_group_by_tracking_id(tr_dataset, tracking_id, add_chunk_to_group_data)
    except Exception as e:
        print("Exception when calling ChunkGroupApi->add_chunk_to_group_by_tracking_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **tracking_id** | **str**| Id of the group to add the chunk to as a bookmark | 
 **add_chunk_to_group_data** | [**AddChunkToGroupData**](AddChunkToGroupData.md)| JSON request payload to add a chunk to a group (bookmark it) | 

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
**204** | Confirmation that the chunk was added to the group (bookmark&#39;ed). |  -  |
**400** | Service error relating to getting the groups that the chunk is in. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_chunk_group**
> ChunkGroup create_chunk_group(tr_dataset, create_chunk_group_data)

Create Chunk Group

Create Chunk Group  Create a new chunk_group. This is a way to group chunks together. If you try to create a chunk_group with the same tracking_id as an existing chunk_group, this operation will fail.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.chunk_group import ChunkGroup
from trieve_py_client.models.create_chunk_group_data import CreateChunkGroupData
from trieve_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trieve.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_py_client.Configuration(
    host = "https://api.trieve.ai"
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
with trieve_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_py_client.ChunkGroupApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    create_chunk_group_data = trieve_py_client.CreateChunkGroupData() # CreateChunkGroupData | JSON request payload to cretea a chunkGroup

    try:
        # Create Chunk Group
        api_response = api_instance.create_chunk_group(tr_dataset, create_chunk_group_data)
        print("The response of ChunkGroupApi->create_chunk_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkGroupApi->create_chunk_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **create_chunk_group_data** | [**CreateChunkGroupData**](CreateChunkGroupData.md)| JSON request payload to cretea a chunkGroup | 

### Return type

[**ChunkGroup**](ChunkGroup.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the created chunkGroup |  -  |
**400** | Service error relating to creating the chunkGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_chunk_group**
> delete_chunk_group(tr_dataset, group_id, delete_chunks)

Delete Group

Delete Group  This will delete a chunk_group. This will not delete the chunks that are in the group. We will soon support deleting a chunk_group along with its member chunks.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trieve.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_py_client.Configuration(
    host = "https://api.trieve.ai"
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
with trieve_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_py_client.ChunkGroupApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    group_id = 'group_id_example' # str | Id of the group you want to fetch.
    delete_chunks = True # bool | Delete the chunks within the group

    try:
        # Delete Group
        api_instance.delete_chunk_group(tr_dataset, group_id, delete_chunks)
    except Exception as e:
        print("Exception when calling ChunkGroupApi->delete_chunk_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **group_id** | **str**| Id of the group you want to fetch. | 
 **delete_chunks** | **bool**| Delete the chunks within the group | 

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
**204** | Confirmation that the chunkGroup was deleted |  -  |
**400** | Service error relating to deleting the chunkGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_by_tracking_id**
> delete_group_by_tracking_id(tr_dataset, tracking_id)

Delete Group by Tracking ID

Delete Group by Tracking ID  Delete a chunk_group with the given tracking id.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trieve.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_py_client.Configuration(
    host = "https://api.trieve.ai"
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
with trieve_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_py_client.ChunkGroupApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    tracking_id = 'tracking_id_example' # str | Tracking id of the chunk_group to delete

    try:
        # Delete Group by Tracking ID
        api_instance.delete_group_by_tracking_id(tr_dataset, tracking_id)
    except Exception as e:
        print("Exception when calling ChunkGroupApi->delete_group_by_tracking_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **tracking_id** | **str**| Tracking id of the chunk_group to delete | 

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
**204** | Confirmation that the chunkGroup was deleted |  -  |
**400** | Service error relating to deleting the chunkGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chunk_group**
> ChunkGroup get_chunk_group(tr_dataset, group_id)

Get Group

Get Group  Fetch the group with the given id. get_group

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.chunk_group import ChunkGroup
from trieve_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trieve.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_py_client.Configuration(
    host = "https://api.trieve.ai"
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
with trieve_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_py_client.ChunkGroupApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    group_id = 'group_id_example' # str | Id of the group you want to fetch.

    try:
        # Get Group
        api_response = api_instance.get_chunk_group(tr_dataset, group_id)
        print("The response of ChunkGroupApi->get_chunk_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkGroupApi->get_chunk_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **group_id** | **str**| Id of the group you want to fetch. | 

### Return type

[**ChunkGroup**](ChunkGroup.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON body representing the group with the given tracking id |  -  |
**400** | Service error relating to getting the group with the given tracking id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chunks_in_group**
> BookmarkData get_chunks_in_group(tr_dataset, group_id, page)

Get Chunks in Group

Get Chunks in Group  Route to get all chunks for a group. The response is paginated, with each page containing 10 chunks. Support for custom page size is coming soon.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.bookmark_data import BookmarkData
from trieve_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trieve.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_py_client.Configuration(
    host = "https://api.trieve.ai"
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
with trieve_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_py_client.ChunkGroupApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    group_id = 'group_id_example' # str | Id of the group you want to fetch.
    page = 56 # int | The page of chunks to get from the group

    try:
        # Get Chunks in Group
        api_response = api_instance.get_chunks_in_group(tr_dataset, group_id, page)
        print("The response of ChunkGroupApi->get_chunks_in_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkGroupApi->get_chunks_in_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **group_id** | **str**| Id of the group you want to fetch. | 
 **page** | **int**| The page of chunks to get from the group | 

### Return type

[**BookmarkData**](BookmarkData.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chunks present within the specified group |  -  |
**400** | Service error relating to getting the groups that the chunk is in |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chunks_in_group_by_tracking_id**
> BookmarkData get_chunks_in_group_by_tracking_id(tr_dataset, group_tracking_id, page)

Get Chunks in Group by Tracking ID

Get Chunks in Group by Tracking ID  Route to get all chunks for a group. The response is paginated, with each page containing 10 chunks. Support for custom page size is coming soon.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.bookmark_data import BookmarkData
from trieve_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trieve.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_py_client.Configuration(
    host = "https://api.trieve.ai"
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
with trieve_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_py_client.ChunkGroupApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    group_tracking_id = 'group_tracking_id_example' # str | The id of the group to get the chunks from
    page = 56 # int | The page of chunks to get from the group

    try:
        # Get Chunks in Group by Tracking ID
        api_response = api_instance.get_chunks_in_group_by_tracking_id(tr_dataset, group_tracking_id, page)
        print("The response of ChunkGroupApi->get_chunks_in_group_by_tracking_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkGroupApi->get_chunks_in_group_by_tracking_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **group_tracking_id** | **str**| The id of the group to get the chunks from | 
 **page** | **int**| The page of chunks to get from the group | 

### Return type

[**BookmarkData**](BookmarkData.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chunks present within the specified group |  -  |
**400** | Service error relating to getting the groups that the chunk is in |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_by_tracking_id**
> ChunkGroup get_group_by_tracking_id(tr_dataset, tracking_id)

Get Group by Tracking ID

Get Group by Tracking ID  Fetch the group with the given tracking id. get_group_by_tracking_id

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.chunk_group import ChunkGroup
from trieve_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trieve.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_py_client.Configuration(
    host = "https://api.trieve.ai"
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
with trieve_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_py_client.ChunkGroupApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    tracking_id = 'tracking_id_example' # str | The tracking id of the group to fetch.

    try:
        # Get Group by Tracking ID
        api_response = api_instance.get_group_by_tracking_id(tr_dataset, tracking_id)
        print("The response of ChunkGroupApi->get_group_by_tracking_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkGroupApi->get_group_by_tracking_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **tracking_id** | **str**| The tracking id of the group to fetch. | 

### Return type

[**ChunkGroup**](ChunkGroup.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON body representing the group with the given tracking id |  -  |
**400** | Service error relating to getting the group with the given tracking id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups_chunk_is_in**
> List[BookmarkGroupResult] get_groups_chunk_is_in(tr_dataset, get_groups_for_chunks_data)

Get Groups for Chunks

Get Groups for Chunks  Route to get the groups that a chunk is in.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.bookmark_group_result import BookmarkGroupResult
from trieve_py_client.models.get_groups_for_chunks_data import GetGroupsForChunksData
from trieve_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trieve.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_py_client.Configuration(
    host = "https://api.trieve.ai"
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
with trieve_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_py_client.ChunkGroupApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    get_groups_for_chunks_data = trieve_py_client.GetGroupsForChunksData() # GetGroupsForChunksData | JSON request payload to get the groups that a chunk is in

    try:
        # Get Groups for Chunks
        api_response = api_instance.get_groups_chunk_is_in(tr_dataset, get_groups_for_chunks_data)
        print("The response of ChunkGroupApi->get_groups_chunk_is_in:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkGroupApi->get_groups_chunk_is_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **get_groups_for_chunks_data** | [**GetGroupsForChunksData**](GetGroupsForChunksData.md)| JSON request payload to get the groups that a chunk is in | 

### Return type

[**List[BookmarkGroupResult]**](BookmarkGroupResult.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON body representing the groups that the chunk is in |  -  |
**400** | Service error relating to getting the groups that the chunk is in |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommended_groups**
> RecommendGroupChunkResponseTypes get_recommended_groups(tr_dataset, reccomend_group_chunks_request)

Get Recommended Groups

Get Recommended Groups  Route to get recommended groups. This route will return groups which are similar to the groups in the request body.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.reccomend_group_chunks_request import ReccomendGroupChunksRequest
from trieve_py_client.models.recommend_group_chunk_response_types import RecommendGroupChunkResponseTypes
from trieve_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trieve.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_py_client.Configuration(
    host = "https://api.trieve.ai"
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
with trieve_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_py_client.ChunkGroupApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    reccomend_group_chunks_request = trieve_py_client.ReccomendGroupChunksRequest() # ReccomendGroupChunksRequest | JSON request payload to get recommendations of chunks similar to the chunks in the request

    try:
        # Get Recommended Groups
        api_response = api_instance.get_recommended_groups(tr_dataset, reccomend_group_chunks_request)
        print("The response of ChunkGroupApi->get_recommended_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkGroupApi->get_recommended_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **reccomend_group_chunks_request** | [**ReccomendGroupChunksRequest**](ReccomendGroupChunksRequest.md)| JSON request payload to get recommendations of chunks similar to the chunks in the request | 

### Return type

[**RecommendGroupChunkResponseTypes**](RecommendGroupChunkResponseTypes.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON body representing the groups which are similar to the groups in the request |  -  |
**400** | Service error relating to to getting similar chunks |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_specific_dataset_chunk_groups**
> GroupData get_specific_dataset_chunk_groups(tr_dataset, dataset_id, page)

Get Groups for Dataset

Get Groups for Dataset  Fetch the groups which belong to a dataset specified by its id.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.group_data import GroupData
from trieve_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trieve.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_py_client.Configuration(
    host = "https://api.trieve.ai"
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
with trieve_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_py_client.ChunkGroupApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    dataset_id = 'dataset_id_example' # str | The id of the dataset to fetch groups for.
    page = 56 # int | The page of groups to fetch. Each page contains 10 groups. Support for custom page size is coming soon.

    try:
        # Get Groups for Dataset
        api_response = api_instance.get_specific_dataset_chunk_groups(tr_dataset, dataset_id, page)
        print("The response of ChunkGroupApi->get_specific_dataset_chunk_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkGroupApi->get_specific_dataset_chunk_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **dataset_id** | **str**| The id of the dataset to fetch groups for. | 
 **page** | **int**| The page of groups to fetch. Each page contains 10 groups. Support for custom page size is coming soon. | 

### Return type

[**GroupData**](GroupData.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON body representing the groups created by the given dataset |  -  |
**400** | Service error relating to getting the groups created by the given dataset |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_chunk_from_group**
> remove_chunk_from_group(tr_dataset, group_id, create_chunk_group_data)

Remove Chunk from Group

Remove Chunk from Group  Route to remove a chunk from a group.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.create_chunk_group_data import CreateChunkGroupData
from trieve_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trieve.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_py_client.Configuration(
    host = "https://api.trieve.ai"
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
with trieve_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_py_client.ChunkGroupApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    group_id = 'group_id_example' # str | Id of the group to remove the bookmark'ed chunk from
    create_chunk_group_data = trieve_py_client.CreateChunkGroupData() # CreateChunkGroupData | JSON request payload to cretea a chunkGroup

    try:
        # Remove Chunk from Group
        api_instance.remove_chunk_from_group(tr_dataset, group_id, create_chunk_group_data)
    except Exception as e:
        print("Exception when calling ChunkGroupApi->remove_chunk_from_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **group_id** | **str**| Id of the group to remove the bookmark&#39;ed chunk from | 
 **create_chunk_group_data** | [**CreateChunkGroupData**](CreateChunkGroupData.md)| JSON request payload to cretea a chunkGroup | 

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
**204** | Confirmation that the chunk was removed to the group |  -  |
**400** | Service error relating to removing the chunk from the group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_over_groups**
> SearchOverGroupsResponseTypes search_over_groups(tr_dataset, search_over_groups_data)

Search Over Groups

Search Over Groups  This route allows you to get groups as results instead of chunks. Each group returned will have the matching chunks sorted by similarity within the group. This is useful for when you want to get groups of chunks which are similar to the search query. If choosing hybrid search, the results will be re-ranked using BAAI/bge-reranker-large. Compatible with semantic, fulltext, or hybrid search modes.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.search_over_groups_data import SearchOverGroupsData
from trieve_py_client.models.search_over_groups_response_types import SearchOverGroupsResponseTypes
from trieve_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trieve.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_py_client.Configuration(
    host = "https://api.trieve.ai"
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
with trieve_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_py_client.ChunkGroupApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    search_over_groups_data = trieve_py_client.SearchOverGroupsData() # SearchOverGroupsData | JSON request payload to semantically search over groups

    try:
        # Search Over Groups
        api_response = api_instance.search_over_groups(tr_dataset, search_over_groups_data)
        print("The response of ChunkGroupApi->search_over_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkGroupApi->search_over_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **search_over_groups_data** | [**SearchOverGroupsData**](SearchOverGroupsData.md)| JSON request payload to semantically search over groups | 

### Return type

[**SearchOverGroupsResponseTypes**](SearchOverGroupsResponseTypes.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group chunks which are similar to the embedding vector of the search query |  -  |
**400** | Service error relating to getting the groups that the chunk is in |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_within_group**
> SearchWithinGroupResponseTypes search_within_group(tr_dataset, search_within_group_data)

Search Within Group

Search Within Group  This route allows you to search only within a group. This is useful for when you only want search results to contain chunks which are members of a specific group. If choosing hybrid search, the results will be re-ranked using BAAI/bge-reranker-large.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.search_within_group_data import SearchWithinGroupData
from trieve_py_client.models.search_within_group_response_types import SearchWithinGroupResponseTypes
from trieve_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trieve.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_py_client.Configuration(
    host = "https://api.trieve.ai"
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
with trieve_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_py_client.ChunkGroupApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    search_within_group_data = trieve_py_client.SearchWithinGroupData() # SearchWithinGroupData | JSON request payload to semantically search a group

    try:
        # Search Within Group
        api_response = api_instance.search_within_group(tr_dataset, search_within_group_data)
        print("The response of ChunkGroupApi->search_within_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkGroupApi->search_within_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **search_within_group_data** | [**SearchWithinGroupData**](SearchWithinGroupData.md)| JSON request payload to semantically search a group | 

### Return type

[**SearchWithinGroupResponseTypes**](SearchWithinGroupResponseTypes.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group chunks which are similar to the embedding vector of the search query |  -  |
**400** | Service error relating to getting the groups that the chunk is in |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_chunk_group**
> update_chunk_group(tr_dataset, update_chunk_group_data)

Update Group

Update Group  Update a chunk_group. If you try to change the tracking_id to one that already exists, this operation will fail.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.update_chunk_group_data import UpdateChunkGroupData
from trieve_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trieve.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_py_client.Configuration(
    host = "https://api.trieve.ai"
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
with trieve_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_py_client.ChunkGroupApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    update_chunk_group_data = trieve_py_client.UpdateChunkGroupData() # UpdateChunkGroupData | JSON request payload to update a chunkGroup

    try:
        # Update Group
        api_instance.update_chunk_group(tr_dataset, update_chunk_group_data)
    except Exception as e:
        print("Exception when calling ChunkGroupApi->update_chunk_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **update_chunk_group_data** | [**UpdateChunkGroupData**](UpdateChunkGroupData.md)| JSON request payload to update a chunkGroup | 

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
**204** | Confirmation that the chunkGroup was updated |  -  |
**400** | Service error relating to updating the chunkGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_by_tracking_id**
> update_group_by_tracking_id(tr_dataset, tracking_id, update_group_by_tracking_id_data)

Update Group by Tracking ID

Update Group by Tracking ID  Update a chunk_group with the given tracking id.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.update_group_by_tracking_id_data import UpdateGroupByTrackingIDData
from trieve_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trieve.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_py_client.Configuration(
    host = "https://api.trieve.ai"
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
with trieve_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_py_client.ChunkGroupApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    tracking_id = 'tracking_id_example' # str | Tracking id of the chunk_group to update
    update_group_by_tracking_id_data = trieve_py_client.UpdateGroupByTrackingIDData() # UpdateGroupByTrackingIDData | JSON request payload to update a chunkGroup

    try:
        # Update Group by Tracking ID
        api_instance.update_group_by_tracking_id(tr_dataset, tracking_id, update_group_by_tracking_id_data)
    except Exception as e:
        print("Exception when calling ChunkGroupApi->update_group_by_tracking_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **tracking_id** | **str**| Tracking id of the chunk_group to update | 
 **update_group_by_tracking_id_data** | [**UpdateGroupByTrackingIDData**](UpdateGroupByTrackingIDData.md)| JSON request payload to update a chunkGroup | 

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
**204** | Confirmation that the chunkGroup was updated |  -  |
**400** | Service error relating to updating the chunkGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

