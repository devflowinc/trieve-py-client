# ClientDatasetConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_chunk_feature** | **bool** |  | [optional] 
**date_range_value** | **str** |  | [optional] 
**document_upload_feature** | **bool** |  | [optional] 
**file_name_key** | **str** |  | 
**filter_items** | **object** |  | [optional] 
**frontmatter_vals** | **str** |  | [optional] 
**image_range_end_key** | **str** |  | [optional] 
**image_range_start_key** | **str** |  | [optional] 
**lines_before_show_more** | **int** |  | [optional] 
**search_queries** | **str** |  | [optional] 
**suggested_queries** | **str** |  | [optional] 

## Example

```python
from trieve_py_client.models.client_dataset_configuration import ClientDatasetConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ClientDatasetConfiguration from a JSON string
client_dataset_configuration_instance = ClientDatasetConfiguration.from_json(json)
# print the JSON string representation of the object
print(ClientDatasetConfiguration.to_json())

# convert the object into a dict
client_dataset_configuration_dict = client_dataset_configuration_instance.to_dict()
# create an instance of ClientDatasetConfiguration from a dict
client_dataset_configuration_form_dict = client_dataset_configuration.from_dict(client_dataset_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


