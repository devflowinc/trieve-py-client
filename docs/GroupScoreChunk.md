# GroupScoreChunk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** |  | 
**group_tracking_id** | **str** |  | [optional] 
**metadata** | [**List[ScoreChunkDTO]**](ScoreChunkDTO.md) |  | 

## Example

```python
from trieve_py_client.models.group_score_chunk import GroupScoreChunk

# TODO update the JSON string below
json = "{}"
# create an instance of GroupScoreChunk from a JSON string
group_score_chunk_instance = GroupScoreChunk.from_json(json)
# print the JSON string representation of the object
print(GroupScoreChunk.to_json())

# convert the object into a dict
group_score_chunk_dict = group_score_chunk_instance.to_dict()
# create an instance of GroupScoreChunk from a dict
group_score_chunk_form_dict = group_score_chunk.from_dict(group_score_chunk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


