# CreateChunkGroupData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description to assign to the chunk_group. Convenience field for you to avoid having to remember what the group is for. | 
**name** | **str** | Name to assign to the chunk_group. Does not need to be unique. | 
**tracking_id** | **str** | Optional tracking id to assign to the chunk_group. This is a unique identifier for the chunk_group. | [optional] 

## Example

```python
from trieve_python_client.models.create_chunk_group_data import CreateChunkGroupData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChunkGroupData from a JSON string
create_chunk_group_data_instance = CreateChunkGroupData.from_json(json)
# print the JSON string representation of the object
print(CreateChunkGroupData.to_json())

# convert the object into a dict
create_chunk_group_data_dict = create_chunk_group_data_instance.to_dict()
# create an instance of CreateChunkGroupData from a dict
create_chunk_group_data_form_dict = create_chunk_group_data.from_dict(create_chunk_group_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


