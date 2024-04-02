# GroupScoreChunkDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** |  | 
**group_tracking_id** | **str** |  | [optional] 
**metadata** | [**List[ScoreChunkDTO]**](ScoreChunkDTO.md) |  | 

## Example

```python
from trieve_python_client.models.group_score_chunk_dto import GroupScoreChunkDTO

# TODO update the JSON string below
json = "{}"
# create an instance of GroupScoreChunkDTO from a JSON string
group_score_chunk_dto_instance = GroupScoreChunkDTO.from_json(json)
# print the JSON string representation of the object
print(GroupScoreChunkDTO.to_json())

# convert the object into a dict
group_score_chunk_dto_dict = group_score_chunk_dto_instance.to_dict()
# create an instance of GroupScoreChunkDTO from a dict
group_score_chunk_dto_form_dict = group_score_chunk_dto.from_dict(group_score_chunk_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


