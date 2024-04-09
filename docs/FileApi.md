# trieve_py_client.FileApi

All URIs are relative to *https://api.trieve.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_file_handler**](FileApi.md#delete_file_handler) | **DELETE** /api/file/{file_id} | Delete File
[**get_dataset_files_handler**](FileApi.md#get_dataset_files_handler) | **GET** /api/dataset/files/{dataset_id}/{page} | Get Files for Dataset
[**get_file_handler**](FileApi.md#get_file_handler) | **GET** /api/file/{file_id} | Get File
[**upload_file_handler**](FileApi.md#upload_file_handler) | **POST** /api/file | Upload File


# **delete_file_handler**
> delete_file_handler(tr_dataset, file_id, delete_chunks)

Delete File

Delete File  Delete a file from S3 attached to the server based on its id. This will disassociate chunks from the file, but only delete them all together if you specify delete_chunks to be true. Auth'ed user must be an admin or owner of the dataset's organization to delete a file.

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
    api_instance = trieve_py_client.FileApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    file_id = 'file_id_example' # str | The id of the file to delete
    delete_chunks = True # bool | Whether or not to delete the chunks associated with the file

    try:
        # Delete File
        api_instance.delete_file_handler(tr_dataset, file_id, delete_chunks)
    except Exception as e:
        print("Exception when calling FileApi->delete_file_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **file_id** | **str**| The id of the file to delete | 
 **delete_chunks** | **bool**| Whether or not to delete the chunks associated with the file | 

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
**204** | Confirmation that the file has been deleted |  -  |
**400** | Service error relating to finding or deleting the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_files_handler**
> List[File] get_dataset_files_handler(tr_dataset, dataset_id, page)

Get Files for Dataset

Get Files for Dataset  Get all files which belong to a given dataset specified by the dataset_id parameter. 10 files are returned per page.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.file import File
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
    api_instance = trieve_py_client.FileApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    dataset_id = 'dataset_id_example' # str | The id of the dataset to fetch files for.
    page = 56 # int | The page number of files you wish to fetch. Each page contains at most 10 files.

    try:
        # Get Files for Dataset
        api_response = api_instance.get_dataset_files_handler(tr_dataset, dataset_id, page)
        print("The response of FileApi->get_dataset_files_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->get_dataset_files_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **dataset_id** | **str**| The id of the dataset to fetch files for. | 
 **page** | **int**| The page number of files you wish to fetch. Each page contains at most 10 files. | 

### Return type

[**List[File]**](File.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON body representing the files in the current dataset |  -  |
**400** | Service error relating to getting the files in the current datase |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_handler**
> FileDTO get_file_handler(tr_dataset, file_id)

Get File

Get File  Download a file based on its id.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.file_dto import FileDTO
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
    api_instance = trieve_py_client.FileApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    file_id = 'file_id_example' # str | The id of the file to fetch

    try:
        # Get File
        api_response = api_instance.get_file_handler(tr_dataset, file_id)
        print("The response of FileApi->get_file_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->get_file_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **file_id** | **str**| The id of the file to fetch | 

### Return type

[**FileDTO**](FileDTO.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The signed s3 url corresponding to the file_id requested |  -  |
**400** | Service error relating to finding the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file_handler**
> UploadFileResult upload_file_handler(tr_dataset, upload_file_data)

Upload File

Upload File  Upload a file to S3 attached to the server. The file will be converted to HTML with tika and chunked algorithmically, images will be OCR'ed with tesseract. The resulting chunks will be indexed and searchable. Optionally, you can only upload the file and manually create chunks associated to the file after. See docs.trieve.ai and/or contact us for more details and tips. Auth'ed user must be an admin or owner of the dataset's organization to upload a file.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_py_client
from trieve_py_client.models.upload_file_data import UploadFileData
from trieve_py_client.models.upload_file_result import UploadFileResult
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
    api_instance = trieve_py_client.FileApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    upload_file_data = trieve_py_client.UploadFileData() # UploadFileData | JSON request payload to upload a file

    try:
        # Upload File
        api_response = api_instance.upload_file_handler(tr_dataset, upload_file_data)
        print("The response of FileApi->upload_file_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->upload_file_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **upload_file_data** | [**UploadFileData**](UploadFileData.md)| JSON request payload to upload a file | 

### Return type

[**UploadFileResult**](UploadFileResult.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirmation that the file is uploading |  -  |
**400** | Service error relating to uploading the file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

