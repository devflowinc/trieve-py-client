# trieve_python_client.OrganizationApi

All URIs are relative to *https://api.trieve.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization**](OrganizationApi.md#create_organization) | **POST** /api/organization | Create Organization
[**delete_organization_by_id**](OrganizationApi.md#delete_organization_by_id) | **DELETE** /api/organization/{organization_id} | Delete Organization
[**get_organization_by_id**](OrganizationApi.md#get_organization_by_id) | **GET** /api/organization/{organization_id} | Get Organization
[**get_organization_usage**](OrganizationApi.md#get_organization_usage) | **GET** /api/organization/usage/{organization_id} | Get Organization Usage
[**get_organization_users**](OrganizationApi.md#get_organization_users) | **GET** /api/organization/users/{organization_id} | Get Organization Users
[**update_organization**](OrganizationApi.md#update_organization) | **PUT** /api/organization | Update Organization


# **create_organization**
> Organization create_organization(create_organization_data)

Create Organization

Create Organization  Create a new organization. The auth'ed user who creates the organization will be the default owner of the organization.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_python_client
from trieve_python_client.models.create_organization_data import CreateOrganizationData
from trieve_python_client.models.organization import Organization
from trieve_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trieve.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_python_client.Configuration(
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
with trieve_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_python_client.OrganizationApi(api_client)
    create_organization_data = trieve_python_client.CreateOrganizationData() # CreateOrganizationData | The organization data that you want to create

    try:
        # Create Organization
        api_response = api_instance.create_organization(create_organization_data)
        print("The response of OrganizationApi->create_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->create_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_organization_data** | [**CreateOrganizationData**](CreateOrganizationData.md)| The organization data that you want to create | 

### Return type

[**Organization**](Organization.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created organization object |  -  |
**400** | Service error relating to creating the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_by_id**
> Organization delete_organization_by_id(tr_organization, organization_id)

Delete Organization

Delete Organization  Delete an organization by its id. The auth'ed user must be an owner of the organization to delete it.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_python_client
from trieve_python_client.models.organization import Organization
from trieve_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trieve.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_python_client.Configuration(
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
with trieve_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_python_client.OrganizationApi(api_client)
    tr_organization = 'tr_organization_example' # str | The organization id to use for the request
    organization_id = 'organization_id_example' # str | The id of the organization you want to fetch.

    try:
        # Delete Organization
        api_response = api_instance.delete_organization_by_id(tr_organization, organization_id)
        print("The response of OrganizationApi->delete_organization_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->delete_organization_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_organization** | **str**| The organization id to use for the request | 
 **organization_id** | **str**| The id of the organization you want to fetch. | 

### Return type

[**Organization**](Organization.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirmation that the organization was deleted |  -  |
**400** | Service error relating to deleting the organization by id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_by_id**
> Organization get_organization_by_id(tr_organization, organization_id)

Get Organization

Get Organization  Fetch the details of an organization by its id. The auth'ed user must be an admin or owner of the organization to fetch it.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_python_client
from trieve_python_client.models.organization import Organization
from trieve_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trieve.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_python_client.Configuration(
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
with trieve_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_python_client.OrganizationApi(api_client)
    tr_organization = 'tr_organization_example' # str | The organization id to use for the request
    organization_id = 'organization_id_example' # str | The id of the organization you want to fetch.

    try:
        # Get Organization
        api_response = api_instance.get_organization_by_id(tr_organization, organization_id)
        print("The response of OrganizationApi->get_organization_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->get_organization_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_organization** | **str**| The organization id to use for the request | 
 **organization_id** | **str**| The id of the organization you want to fetch. | 

### Return type

[**Organization**](Organization.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Organization with the id that was requested |  -  |
**400** | Service error relating to finding the organization by id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_usage**
> OrganizationUsageCount get_organization_usage(tr_organization, organization_id)

Get Organization Usage

Get Organization Usage  Fetch the current usage specification of an organization by its id. The auth'ed user must be an admin or owner of the organization to fetch it.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_python_client
from trieve_python_client.models.organization_usage_count import OrganizationUsageCount
from trieve_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trieve.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_python_client.Configuration(
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
with trieve_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_python_client.OrganizationApi(api_client)
    tr_organization = 'tr_organization_example' # str | The organization id to use for the request
    organization_id = 'organization_id_example' # str | The id of the organization you want to fetch the usage of.

    try:
        # Get Organization Usage
        api_response = api_instance.get_organization_usage(tr_organization, organization_id)
        print("The response of OrganizationApi->get_organization_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->get_organization_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_organization** | **str**| The organization id to use for the request | 
 **organization_id** | **str**| The id of the organization you want to fetch the usage of. | 

### Return type

[**OrganizationUsageCount**](OrganizationUsageCount.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current usage of the specified organization |  -  |
**400** | Service error relating to finding the organization&#39;s usage by id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_users**
> List[SlimUser] get_organization_users(tr_organization, organization_id)

Get Organization Users

Get Organization Users  Fetch the users of an organization by its id. The auth'ed user must be an admin or owner of the organization to fetch it.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_python_client
from trieve_python_client.models.slim_user import SlimUser
from trieve_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trieve.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_python_client.Configuration(
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
with trieve_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_python_client.OrganizationApi(api_client)
    tr_organization = 'tr_organization_example' # str | The organization id to use for the request
    organization_id = 'organization_id_example' # str | The id of the organization you want to fetch the users of.

    try:
        # Get Organization Users
        api_response = api_instance.get_organization_users(tr_organization, organization_id)
        print("The response of OrganizationApi->get_organization_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->get_organization_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_organization** | **str**| The organization id to use for the request | 
 **organization_id** | **str**| The id of the organization you want to fetch the users of. | 

### Return type

[**List[SlimUser]**](SlimUser.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of users who belong to the specified by organization |  -  |
**400** | Service error relating to finding the organization&#39;s users by id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization**
> Organization update_organization(tr_organization, update_organization_data)

Update Organization

Update Organization  Update an organization. Only the owner of the organization can update it.

### Example

* Api Key Authentication (ApiKey):

```python
import trieve_python_client
from trieve_python_client.models.organization import Organization
from trieve_python_client.models.update_organization_data import UpdateOrganizationData
from trieve_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trieve.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_python_client.Configuration(
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
with trieve_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_python_client.OrganizationApi(api_client)
    tr_organization = 'tr_organization_example' # str | The organization id to use for the request
    update_organization_data = trieve_python_client.UpdateOrganizationData() # UpdateOrganizationData | The organization data that you want to update

    try:
        # Update Organization
        api_response = api_instance.update_organization(tr_organization, update_organization_data)
        print("The response of OrganizationApi->update_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->update_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_organization** | **str**| The organization id to use for the request | 
 **update_organization_data** | [**UpdateOrganizationData**](UpdateOrganizationData.md)| The organization data that you want to update | 

### Return type

[**Organization**](Organization.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated organization object |  -  |
**400** | Service error relating to updating the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

