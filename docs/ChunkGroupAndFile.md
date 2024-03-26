# ChunkGroupAndFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**dataset_id** | **str** |  | 
**description** | **str** |  | 
**file_id** | **str** |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | 
**tracking_id** | **str** |  | [optional] 
**updated_at** | **datetime** |  | 

## Example

```python
from trieve_python_client.models.chunk_group_and_file import ChunkGroupAndFile

# TODO update the JSON string below
json = "{}"
# create an instance of ChunkGroupAndFile from a JSON string
chunk_group_and_file_instance = ChunkGroupAndFile.from_json(json)
# print the JSON string representation of the object
print(ChunkGroupAndFile.to_json())

# convert the object into a dict
chunk_group_and_file_dict = chunk_group_and_file_instance.to_dict()
# create an instance of ChunkGroupAndFile from a dict
chunk_group_and_file_form_dict = chunk_group_and_file.from_dict(chunk_group_and_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


