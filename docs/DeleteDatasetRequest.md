# DeleteDatasetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **str** | The id of the dataset you want to delete. | 

## Example

```python
from trieve_python_client.models.delete_dataset_request import DeleteDatasetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDatasetRequest from a JSON string
delete_dataset_request_instance = DeleteDatasetRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteDatasetRequest.to_json())

# convert the object into a dict
delete_dataset_request_dict = delete_dataset_request_instance.to_dict()
# create an instance of DeleteDatasetRequest from a dict
delete_dataset_request_form_dict = delete_dataset_request.from_dict(delete_dataset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


