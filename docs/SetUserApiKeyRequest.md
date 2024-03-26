# SetUserApiKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name which will be assigned to the new api key. | 
**role** | **int** | The role which will be assigned to the new api key. Either 0 (read), 1 (read and write at the level of the currently auth&#39;ed user). The auth&#39;ed user must have a role greater than or equal to the role being assigned which means they must be an admin (1) or owner (2) of the organization to assign write permissions with a role of 1. | 

## Example

```python
from trieve_python_client.models.set_user_api_key_request import SetUserApiKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetUserApiKeyRequest from a JSON string
set_user_api_key_request_instance = SetUserApiKeyRequest.from_json(json)
# print the JSON string representation of the object
print(SetUserApiKeyRequest.to_json())

# convert the object into a dict
set_user_api_key_request_dict = set_user_api_key_request_instance.to_dict()
# create an instance of SetUserApiKeyRequest from a dict
set_user_api_key_request_form_dict = set_user_api_key_request.from_dict(set_user_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


