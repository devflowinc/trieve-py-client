# ChunkMetadataWithFileData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_html** | **str** |  | [optional] 
**content** | **str** |  | 
**created_at** | **datetime** |  | 
**file_id** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**id** | **str** |  | 
**link** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**qdrant_point_id** | **str** |  | 
**tag_set** | **str** |  | [optional] 
**time_stamp** | **datetime** |  | [optional] 
**tracking_id** | **str** |  | [optional] 
**updated_at** | **datetime** |  | 
**weight** | **float** |  | 

## Example

```python
from trieve_python_client.models.chunk_metadata_with_file_data import ChunkMetadataWithFileData

# TODO update the JSON string below
json = "{}"
# create an instance of ChunkMetadataWithFileData from a JSON string
chunk_metadata_with_file_data_instance = ChunkMetadataWithFileData.from_json(json)
# print the JSON string representation of the object
print(ChunkMetadataWithFileData.to_json())

# convert the object into a dict
chunk_metadata_with_file_data_dict = chunk_metadata_with_file_data_instance.to_dict()
# create an instance of ChunkMetadataWithFileData from a dict
chunk_metadata_with_file_data_form_dict = chunk_metadata_with_file_data.from_dict(chunk_metadata_with_file_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


