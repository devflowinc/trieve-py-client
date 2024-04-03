# GroupSlimChunksDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** |  | 
**metadata** | [**List[ScoreSlimChunks]**](ScoreSlimChunks.md) |  | 

## Example

```python
from trieve_python_client.models.group_slim_chunks_dto import GroupSlimChunksDTO

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSlimChunksDTO from a JSON string
group_slim_chunks_dto_instance = GroupSlimChunksDTO.from_json(json)
# print the JSON string representation of the object
print(GroupSlimChunksDTO.to_json())

# convert the object into a dict
group_slim_chunks_dto_dict = group_slim_chunks_dto_instance.to_dict()
# create an instance of GroupSlimChunksDTO from a dict
group_slim_chunks_dto_form_dict = group_slim_chunks_dto.from_dict(group_slim_chunks_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


