# UpdateDatasetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_configuration** | **object** | The new client configuration of the dataset, can be arbitrary JSON. See docs.trieve.ai for more information. If not provided, the client configuration will not be updated. | [optional] 
**dataset_id** | **str** | The id of the dataset you want to update. | 
**dataset_name** | **str** | The new name of the dataset. Must be unique within the organization. If not provided, the name will not be updated. | [optional] 
**server_configuration** | **object** | The new server configuration of the dataset, can be arbitrary JSON. See docs.trieve.ai for more information. If not provided, the server configuration will not be updated. | [optional] 

## Example

```python
from trieve_py_client.models.update_dataset_request import UpdateDatasetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDatasetRequest from a JSON string
update_dataset_request_instance = UpdateDatasetRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDatasetRequest.to_json())

# convert the object into a dict
update_dataset_request_dict = update_dataset_request_instance.to_dict()
# create an instance of UpdateDatasetRequest from a dict
update_dataset_request_form_dict = update_dataset_request.from_dict(update_dataset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


