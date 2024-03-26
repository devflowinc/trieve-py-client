# trieve_python_client.DatasetApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dataset**](DatasetApi.md#create_dataset) | **POST** /api/dataset | Create dataset
[**delete_dataset**](DatasetApi.md#delete_dataset) | **DELETE** /api/dataset | Delete Dataset
[**get_client_dataset_config**](DatasetApi.md#get_client_dataset_config) | **GET** /api/dataset/envs | Get Client Configuration
[**get_dataset**](DatasetApi.md#get_dataset) | **GET** /api/dataset/{dataset_id} | Get Dataset
[**get_datasets_from_organization**](DatasetApi.md#get_datasets_from_organization) | **GET** /api/dataset/organization/{organization_id} | Get Datasets from Organization
[**update_dataset**](DatasetApi.md#update_dataset) | **PUT** /api/dataset | Update Dataset


# **create_dataset**
> Dataset create_dataset(tr_organization, create_dataset_request)

Create dataset

Create dataset  Create a new dataset. The auth'ed user must be an owner of the organization to create a dataset.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_python_client
from trieve_python_client.models.create_dataset_request import CreateDatasetRequest
from trieve_python_client.models.dataset import Dataset
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
    api_instance = trieve_python_client.DatasetApi(api_client)
    tr_organization = 'tr_organization_example' # str | The organization id to use for the request
    create_dataset_request = trieve_python_client.CreateDatasetRequest() # CreateDatasetRequest | JSON request payload to create a new dataset

    try:
        # Create dataset
        api_response = api_instance.create_dataset(tr_organization, create_dataset_request)
        print("The response of DatasetApi->create_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->create_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_organization** | **str**| The organization id to use for the request | 
 **create_dataset_request** | [**CreateDatasetRequest**](CreateDatasetRequest.md)| JSON request payload to create a new dataset | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataset created successfully |  -  |
**400** | Service error relating to creating the dataset |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dataset**
> delete_dataset(tr_organization, delete_dataset_request)

Delete Dataset

Delete Dataset  Delete a dataset. The auth'ed user must be an owner of the organization to delete a dataset.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_python_client
from trieve_python_client.models.delete_dataset_request import DeleteDatasetRequest
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
    api_instance = trieve_python_client.DatasetApi(api_client)
    tr_organization = 'tr_organization_example' # str | The organization id to use for the request
    delete_dataset_request = trieve_python_client.DeleteDatasetRequest() # DeleteDatasetRequest | JSON request payload to delete a dataset

    try:
        # Delete Dataset
        api_instance.delete_dataset(tr_organization, delete_dataset_request)
    except Exception as e:
        print("Exception when calling DatasetApi->delete_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_organization** | **str**| The organization id to use for the request | 
 **delete_dataset_request** | [**DeleteDatasetRequest**](DeleteDatasetRequest.md)| JSON request payload to delete a dataset | 

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
**204** | Dataset deleted successfully |  -  |
**400** | Service error relating to deleting the dataset |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_dataset_config**
> ClientDatasetConfiguration get_client_dataset_config(tr_dataset)

Get Client Configuration

Get Client Configuration  Get the client configuration for a dataset. Will use the TR-D

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_python_client
from trieve_python_client.models.client_dataset_configuration import ClientDatasetConfiguration
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
    api_instance = trieve_python_client.DatasetApi(api_client)
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request

    try:
        # Get Client Configuration
        api_response = api_instance.get_client_dataset_config(tr_dataset)
        print("The response of DatasetApi->get_client_dataset_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->get_client_dataset_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_dataset** | **str**| The dataset id to use for the request | 

### Return type

[**ClientDatasetConfiguration**](ClientDatasetConfiguration.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataset environment variables |  -  |
**400** | Service error relating to retrieving the dataset. Typically this only happens when your auth credentials are invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset**
> Dataset get_dataset(tr_organization, tr_dataset, dataset_id)

Get Dataset

Get Dataset  Get a dataset by id. The auth'ed user must be an admin or owner of the organization to get a dataset.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_python_client
from trieve_python_client.models.dataset import Dataset
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
    api_instance = trieve_python_client.DatasetApi(api_client)
    tr_organization = 'tr_organization_example' # str | The organization id to use for the request
    tr_dataset = 'tr_dataset_example' # str | The dataset id to use for the request
    dataset_id = 'dataset_id_example' # str | The id of the dataset you want to retrieve.

    try:
        # Get Dataset
        api_response = api_instance.get_dataset(tr_organization, tr_dataset, dataset_id)
        print("The response of DatasetApi->get_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->get_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_organization** | **str**| The organization id to use for the request | 
 **tr_dataset** | **str**| The dataset id to use for the request | 
 **dataset_id** | **str**| The id of the dataset you want to retrieve. | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataset retrieved successfully |  -  |
**400** | Service error relating to retrieving the dataset |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasets_from_organization**
> List[DatasetAndUsage] get_datasets_from_organization(tr_organization, organization_id)

Get Datasets from Organization

Get Datasets from Organization  Get all datasets for an organization. The auth'ed user must be an admin or owner of the organization to get its datasets.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_python_client
from trieve_python_client.models.dataset_and_usage import DatasetAndUsage
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
    api_instance = trieve_python_client.DatasetApi(api_client)
    tr_organization = 'tr_organization_example' # str | The organization id to use for the request
    organization_id = 'organization_id_example' # str | id of the organization you want to retrieve datasets for

    try:
        # Get Datasets from Organization
        api_response = api_instance.get_datasets_from_organization(tr_organization, organization_id)
        print("The response of DatasetApi->get_datasets_from_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->get_datasets_from_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_organization** | **str**| The organization id to use for the request | 
 **organization_id** | **str**| id of the organization you want to retrieve datasets for | 

### Return type

[**List[DatasetAndUsage]**](DatasetAndUsage.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Datasets retrieved successfully |  -  |
**400** | Service error relating to retrieving the dataset |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dataset**
> Dataset update_dataset(tr_organization, update_dataset_request)

Update Dataset

Update Dataset  Update a dataset. The auth'ed user must be an owner of the organization to update a dataset.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_python_client
from trieve_python_client.models.dataset import Dataset
from trieve_python_client.models.update_dataset_request import UpdateDatasetRequest
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
    api_instance = trieve_python_client.DatasetApi(api_client)
    tr_organization = 'tr_organization_example' # str | The organization id to use for the request
    update_dataset_request = trieve_python_client.UpdateDatasetRequest() # UpdateDatasetRequest | JSON request payload to update a dataset

    try:
        # Update Dataset
        api_response = api_instance.update_dataset(tr_organization, update_dataset_request)
        print("The response of DatasetApi->update_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->update_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_organization** | **str**| The organization id to use for the request | 
 **update_dataset_request** | [**UpdateDatasetRequest**](UpdateDatasetRequest.md)| JSON request payload to update a dataset | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataset updated successfully |  -  |
**400** | Service error relating to updating the dataset |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

