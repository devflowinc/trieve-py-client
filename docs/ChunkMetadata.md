# ChunkMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_html** | **str** |  | [optional] 
**content** | **str** |  | 
**created_at** | **datetime** |  | 
**dataset_id** | **str** |  | 
**id** | **str** |  | 
**link** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**qdrant_point_id** | **str** |  | [optional] 
**tag_set** | **str** |  | [optional] 
**time_stamp** | **datetime** |  | [optional] 
**tracking_id** | **str** |  | [optional] 
**updated_at** | **datetime** |  | 
**weight** | **float** |  | 

## Example

```python
from trieve_python_client.models.chunk_metadata import ChunkMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ChunkMetadata from a JSON string
chunk_metadata_instance = ChunkMetadata.from_json(json)
# print the JSON string representation of the object
print(ChunkMetadata.to_json())

# convert the object into a dict
chunk_metadata_dict = chunk_metadata_instance.to_dict()
# create an instance of ChunkMetadata from a dict
chunk_metadata_form_dict = chunk_metadata.from_dict(chunk_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


