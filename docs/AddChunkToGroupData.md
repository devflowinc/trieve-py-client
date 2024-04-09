# AddChunkToGroupData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_id** | **str** | Id of the chunk to make a member of the group. | [optional] 
**tracking_id** | **str** | Tracking Id of the chunk to make a member of the group. | [optional] 

## Example

```python
from trieve_py_client.models.add_chunk_to_group_data import AddChunkToGroupData

# TODO update the JSON string below
json = "{}"
# create an instance of AddChunkToGroupData from a JSON string
add_chunk_to_group_data_instance = AddChunkToGroupData.from_json(json)
# print the JSON string representation of the object
print(AddChunkToGroupData.to_json())

# convert the object into a dict
add_chunk_to_group_data_dict = add_chunk_to_group_data_instance.to_dict()
# create an instance of AddChunkToGroupData from a dict
add_chunk_to_group_data_form_dict = add_chunk_to_group_data.from_dict(add_chunk_to_group_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


