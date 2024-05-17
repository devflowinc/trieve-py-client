# trieve_py_client.ChunkApi

All URIs are relative to *https://api.trieve.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autocomplete**](ChunkApi.md#autocomplete) | **POST** /api/chunk/autocomplete | Autocomplete
[**create_chunk**](ChunkApi.md#create_chunk) | **POST** /api/chunk | Create or Upsert Chunk or Chunks
[**create_suggested_queries_handler**](ChunkApi.md#create_suggested_queries_handler) | **POST** /api/chunk/gen_suggestions | Generate suggested queries
[**delete_chunk**](ChunkApi.md#delete_chunk) | **DELETE** /api/chunk/{chunk_id} | Delete Chunk
[**delete_chunk_by_tracking_id**](ChunkApi.md#delete_chunk_by_tracking_id) | **DELETE** /api/chunk/tracking_id/{tracking_id} | Delete Chunk By Tracking Id
[**generate_off_chunks**](ChunkApi.md#generate_off_chunks) | **POST** /api/chunk/generate | RAG on Specified Chunks
[**get_chunk_by_id**](ChunkApi.md#get_chunk_by_id) | **GET** /api/chunk/{chunk_id} | Get Chunk By Id
[**get_chunk_by_tracking_id**](ChunkApi.md#get_chunk_by_tracking_id) | **GET** /api/chunk/tracking_id/{tracking_id} | Get Chunk By Tracking Id
[**get_chunks_by_ids**](ChunkApi.md#get_chunks_by_ids) | **POST** /api/chunks | Get Chunks By Ids
[**get_chunks_by_tracking_ids**](ChunkApi.md#get_chunks_by_tracking_ids) | **POST** /api/chunks/tracking | Get Chunks By TrackingIds
[**get_recommended_chunks**](ChunkApi.md#get_recommended_chunks) | **POST** /api/chunk/recommend | Get Recommended Chunks
[**search_chunks**](ChunkApi.md#search_chunks) | **POST** /api/chunk/search | Search
[**update_chunk**](ChunkApi.md#update_chunk) | **PUT** /api/chunk | Update Chunk
[**update_chunk_by_tracking_id**](ChunkApi.md#update_chunk_by_tracking_id) | **PUT** /api/chunk/tracking_id/update | Update Chunk By Tracking Id


# **autocomplete**
> SearchChunkQueryResponseBody autocomplete(tr_dataset, autocomplete_data)

Autocomplete

Autocomplete  This route provides the primary autocomplete functionality for the API. This prioritize prefix matching with semantic or full-text search.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.autocomplete_data import AutocompleteData
from trieve_py_client.models.search_chunk_query_response_body import SearchChunkQueryResponseBody
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
    api_instance = trieve_py_client.ChunkApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    autocomplete_data = trieve_py_client.AutocompleteData() # AutocompleteData | JSON request payload to semantically search for chunks (chunks)

    try:
        # Autocomplete
        api_response = api_instance.autocomplete(tr_dataset, autocomplete_data)
        print("The response of ChunkApi->autocomplete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkApi->autocomplete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **autocomplete_data** | [**AutocompleteData**](AutocompleteData.md)| JSON request payload to semantically search for chunks (chunks) | 

### Return type

[**SearchChunkQueryResponseBody**](SearchChunkQueryResponseBody.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chunks with embedding vectors which are similar to those in the request body |  -  |
**400** | Service error relating to searching |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_chunk**
> ReturnQueuedChunk create_chunk(tr_dataset, create_chunk_data)

Create or Upsert Chunk or Chunks

Create or Upsert Chunk or Chunks  Create a new chunk. If the chunk has the same tracking_id as an existing chunk, the request will fail. Once a chunk is created, it can be searched for using the search endpoint. If uploading in bulk, the maximum amount of chunks that can be uploaded at once is 120 chunks.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.create_chunk_data import CreateChunkData
from trieve_py_client.models.return_queued_chunk import ReturnQueuedChunk
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
    api_instance = trieve_py_client.ChunkApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    create_chunk_data = trieve_py_client.CreateChunkData() # CreateChunkData | JSON request payload to create a new chunk (chunk)

    try:
        # Create or Upsert Chunk or Chunks
        api_response = api_instance.create_chunk(tr_dataset, create_chunk_data)
        print("The response of ChunkApi->create_chunk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkApi->create_chunk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **create_chunk_data** | [**CreateChunkData**](CreateChunkData.md)| JSON request payload to create a new chunk (chunk) | 

### Return type

[**ReturnQueuedChunk**](ReturnQueuedChunk.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON response payload containing the created chunk |  -  |
**400** | Error typically due to deserialization issues |  -  |
**426** | Error when upgrade is needed to process more chunks |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_suggested_queries_handler**
> SuggestedQueriesResponse create_suggested_queries_handler(tr_dataset, suggested_queries_request)

Generate suggested queries

Generate suggested queries  This endpoint will generate 3 suggested queries based off the query provided in the request body and return them as a JSON object.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.suggested_queries_request import SuggestedQueriesRequest
from trieve_py_client.models.suggested_queries_response import SuggestedQueriesResponse
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
    api_instance = trieve_py_client.ChunkApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    suggested_queries_request = trieve_py_client.SuggestedQueriesRequest() # SuggestedQueriesRequest | JSON request payload to get alternative suggested queries

    try:
        # Generate suggested queries
        api_response = api_instance.create_suggested_queries_handler(tr_dataset, suggested_queries_request)
        print("The response of ChunkApi->create_suggested_queries_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkApi->create_suggested_queries_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **suggested_queries_request** | [**SuggestedQueriesRequest**](SuggestedQueriesRequest.md)| JSON request payload to get alternative suggested queries | 

### Return type

[**SuggestedQueriesResponse**](SuggestedQueriesResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object containing a list of alternative suggested queries |  -  |
**400** | Service error relating to to updating chunk, likely due to conflicting tracking_id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_chunk**
> delete_chunk(tr_dataset, chunk_id)

Delete Chunk

Delete Chunk  Delete a chunk by its id. If deleting a root chunk which has a collision, the most recently created collision will become a new root chunk.

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
    api_instance = trieve_py_client.ChunkApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    chunk_id = 'chunk_id_example' # str | Id of the chunk you want to fetch.

    try:
        # Delete Chunk
        api_instance.delete_chunk(tr_dataset, chunk_id)
    except Exception as e:
        print("Exception when calling ChunkApi->delete_chunk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **chunk_id** | **str**| Id of the chunk you want to fetch. | 

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
**204** | Confirmation that the chunk with the id specified was deleted |  -  |
**400** | Service error relating to finding a chunk by tracking_id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_chunk_by_tracking_id**
> delete_chunk_by_tracking_id(tr_dataset, tracking_id)

Delete Chunk By Tracking Id

Delete Chunk By Tracking Id  Delete a chunk by tracking_id. This is useful for when you are coordinating with an external system and want to use the tracking_id to identify the chunk. If deleting a root chunk which has a collision, the most recently created collision will become a new root chunk.

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
    api_instance = trieve_py_client.ChunkApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    tracking_id = 'tracking_id_example' # str | tracking_id of the chunk you want to delete

    try:
        # Delete Chunk By Tracking Id
        api_instance.delete_chunk_by_tracking_id(tr_dataset, tracking_id)
    except Exception as e:
        print("Exception when calling ChunkApi->delete_chunk_by_tracking_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **tracking_id** | **str**| tracking_id of the chunk you want to delete | 

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
**204** | Confirmation that the chunk with the tracking_id specified was deleted |  -  |
**400** | Service error relating to finding a chunk by tracking_id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_off_chunks**
> str generate_off_chunks(tr_dataset, generate_chunks_request)

RAG on Specified Chunks

RAG on Specified Chunks  This endpoint exists as an alternative to the topic+message concept where our API handles chat memory. With this endpoint, the user is responsible for providing the context window and the prompt. See more in the \"search before generate\" page at docs.trieve.ai.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.generate_chunks_request import GenerateChunksRequest
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
    api_instance = trieve_py_client.ChunkApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    generate_chunks_request = trieve_py_client.GenerateChunksRequest() # GenerateChunksRequest | JSON request payload to perform RAG on some chunks (chunks)

    try:
        # RAG on Specified Chunks
        api_response = api_instance.generate_off_chunks(tr_dataset, generate_chunks_request)
        print("The response of ChunkApi->generate_off_chunks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkApi->generate_off_chunks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **generate_chunks_request** | [**GenerateChunksRequest**](GenerateChunksRequest.md)| JSON request payload to perform RAG on some chunks (chunks) | 

### Return type

**str**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This will be a JSON response of a string containing the LLM&#39;s generated inference. Response if not streaming. |  -  |
**400** | Service error relating to to updating chunk, likely due to conflicting tracking_id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chunk_by_id**
> ChunkMetadata get_chunk_by_id(tr_dataset, chunk_id)

Get Chunk By Id

Get Chunk By Id  Get a singular chunk by id.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.chunk_metadata import ChunkMetadata
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
    api_instance = trieve_py_client.ChunkApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    chunk_id = 'chunk_id_example' # str | Id of the chunk you want to fetch.

    try:
        # Get Chunk By Id
        api_response = api_instance.get_chunk_by_id(tr_dataset, chunk_id)
        print("The response of ChunkApi->get_chunk_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkApi->get_chunk_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **chunk_id** | **str**| Id of the chunk you want to fetch. | 

### Return type

[**ChunkMetadata**](ChunkMetadata.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | chunk with the id that you were searching for |  -  |
**400** | Service error relating to fidning a chunk by tracking_id |  -  |
**404** | Chunk not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chunk_by_tracking_id**
> ChunkMetadata get_chunk_by_tracking_id(tr_dataset, tracking_id)

Get Chunk By Tracking Id

Get Chunk By Tracking Id  Get a singular chunk by tracking_id. This is useful for when you are coordinating with an external system and want to use your own id as the primary reference for a chunk.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.chunk_metadata import ChunkMetadata
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
    api_instance = trieve_py_client.ChunkApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    tracking_id = 'tracking_id_example' # str | tracking_id of the chunk you want to fetch

    try:
        # Get Chunk By Tracking Id
        api_response = api_instance.get_chunk_by_tracking_id(tr_dataset, tracking_id)
        print("The response of ChunkApi->get_chunk_by_tracking_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkApi->get_chunk_by_tracking_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **tracking_id** | **str**| tracking_id of the chunk you want to fetch | 

### Return type

[**ChunkMetadata**](ChunkMetadata.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | chunk with the tracking_id that you were searching for |  -  |
**400** | Service error relating to fidning a chunk by tracking_id |  -  |
**404** | Chunk not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chunks_by_ids**
> List[ChunkMetadata] get_chunks_by_ids(tr_dataset, get_chunks_data)

Get Chunks By Ids

Get Chunks By Ids  Get multiple chunks by multiple ids.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.chunk_metadata import ChunkMetadata
from trieve_py_client.models.get_chunks_data import GetChunksData
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
    api_instance = trieve_py_client.ChunkApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    get_chunks_data = trieve_py_client.GetChunksData() # GetChunksData | JSON request payload to get the chunks in the request

    try:
        # Get Chunks By Ids
        api_response = api_instance.get_chunks_by_ids(tr_dataset, get_chunks_data)
        print("The response of ChunkApi->get_chunks_by_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkApi->get_chunks_by_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **get_chunks_data** | [**GetChunksData**](GetChunksData.md)| JSON request payload to get the chunks in the request | 

### Return type

[**List[ChunkMetadata]**](ChunkMetadata.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | chunks with the id that you were searching for |  -  |
**400** | Service error relating to fidning a chunk by tracking_id |  -  |
**404** | Any one of the specified chunks not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chunks_by_tracking_ids**
> ChunkMetadata get_chunks_by_tracking_ids(tr_dataset, get_tracking_chunks_data)

Get Chunks By TrackingIds

Get Chunks By TrackingIds  Get multiple chunks by ids.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.chunk_metadata import ChunkMetadata
from trieve_py_client.models.get_tracking_chunks_data import GetTrackingChunksData
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
    api_instance = trieve_py_client.ChunkApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    get_tracking_chunks_data = trieve_py_client.GetTrackingChunksData() # GetTrackingChunksData | JSON request payload to get the chunks in the request

    try:
        # Get Chunks By TrackingIds
        api_response = api_instance.get_chunks_by_tracking_ids(tr_dataset, get_tracking_chunks_data)
        print("The response of ChunkApi->get_chunks_by_tracking_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkApi->get_chunks_by_tracking_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **get_tracking_chunks_data** | [**GetTrackingChunksData**](GetTrackingChunksData.md)| JSON request payload to get the chunks in the request | 

### Return type

[**ChunkMetadata**](ChunkMetadata.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | chunk with the id that you were searching for |  -  |
**400** | Service error relating to fidning a chunk by tracking_id |  -  |
**404** | Any one of the specified chunks not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommended_chunks**
> List[ChunkMetadataWithScore] get_recommended_chunks(tr_dataset, recommend_chunks_request)

Get Recommended Chunks

Get Recommended Chunks  Get recommendations of chunks similar to the chunks in the request. Think about this as a feature similar to the \"add to playlist\" recommendation feature on Spotify. This request pairs especially well with our groups endpoint.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.chunk_metadata_with_score import ChunkMetadataWithScore
from trieve_py_client.models.recommend_chunks_request import RecommendChunksRequest
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
    api_instance = trieve_py_client.ChunkApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    recommend_chunks_request = trieve_py_client.RecommendChunksRequest() # RecommendChunksRequest | JSON request payload to get recommendations of chunks similar to the chunks in the request

    try:
        # Get Recommended Chunks
        api_response = api_instance.get_recommended_chunks(tr_dataset, recommend_chunks_request)
        print("The response of ChunkApi->get_recommended_chunks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkApi->get_recommended_chunks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **recommend_chunks_request** | [**RecommendChunksRequest**](RecommendChunksRequest.md)| JSON request payload to get recommendations of chunks similar to the chunks in the request | 

### Return type

[**List[ChunkMetadataWithScore]**](ChunkMetadataWithScore.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chunks with embedding vectors which are similar to positives and dissimilar to negatives |  -  |
**400** | Service error relating to to getting similar chunks |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_chunks**
> SearchChunkQueryResponseBody search_chunks(tr_dataset, search_chunk_data)

Search

Search  This route provides the primary search functionality for the API. It can be used to search for chunks by semantic similarity, full-text similarity, or a combination of both. Results' `chunk_html` values will be modified with `<b><mark>` tags for sub-sentence highlighting.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.search_chunk_data import SearchChunkData
from trieve_py_client.models.search_chunk_query_response_body import SearchChunkQueryResponseBody
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
    api_instance = trieve_py_client.ChunkApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    search_chunk_data = trieve_py_client.SearchChunkData() # SearchChunkData | JSON request payload to semantically search for chunks (chunks)

    try:
        # Search
        api_response = api_instance.search_chunks(tr_dataset, search_chunk_data)
        print("The response of ChunkApi->search_chunks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChunkApi->search_chunks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **search_chunk_data** | [**SearchChunkData**](SearchChunkData.md)| JSON request payload to semantically search for chunks (chunks) | 

### Return type

[**SearchChunkQueryResponseBody**](SearchChunkQueryResponseBody.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chunks with embedding vectors which are similar to those in the request body |  -  |
**400** | Service error relating to searching |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_chunk**
> update_chunk(tr_dataset, update_chunk_data)

Update Chunk

Update Chunk  Update a chunk. If you try to change the tracking_id of the chunk to have the same tracking_id as an existing chunk, the request will fail.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.update_chunk_data import UpdateChunkData
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
    api_instance = trieve_py_client.ChunkApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    update_chunk_data = trieve_py_client.UpdateChunkData() # UpdateChunkData | JSON request payload to update a chunk (chunk)

    try:
        # Update Chunk
        api_instance.update_chunk(tr_dataset, update_chunk_data)
    except Exception as e:
        print("Exception when calling ChunkApi->update_chunk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **update_chunk_data** | [**UpdateChunkData**](UpdateChunkData.md)| JSON request payload to update a chunk (chunk) | 

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
**204** | No content Ok response indicating the chunk was updated as requested |  -  |
**400** | Service error relating to to updating chunk, likely due to conflicting tracking_id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_chunk_by_tracking_id**
> update_chunk_by_tracking_id(tr_dataset, update_chunk_by_tracking_id_data)

Update Chunk By Tracking Id

Update Chunk By Tracking Id  Update a chunk by tracking_id. This is useful for when you are coordinating with an external system and want to use the tracking_id to identify the chunk.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.update_chunk_by_tracking_id_data import UpdateChunkByTrackingIdData
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
    api_instance = trieve_py_client.ChunkApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    update_chunk_by_tracking_id_data = trieve_py_client.UpdateChunkByTrackingIdData() # UpdateChunkByTrackingIdData | JSON request payload to update a chunk by tracking_id (chunks)

    try:
        # Update Chunk By Tracking Id
        api_instance.update_chunk_by_tracking_id(tr_dataset, update_chunk_by_tracking_id_data)
    except Exception as e:
        print("Exception when calling ChunkApi->update_chunk_by_tracking_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **update_chunk_by_tracking_id_data** | [**UpdateChunkByTrackingIdData**](UpdateChunkByTrackingIdData.md)| JSON request payload to update a chunk by tracking_id (chunks) | 

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
**204** | Confirmation that the chunk has been updated as per your request |  -  |
**400** | Service error relating to to updating chunk |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

