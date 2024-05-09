# GroupScoreSlimChunks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** |  | 
**group_name** | **str** |  | [optional] 
**group_tracking_id** | **str** |  | [optional] 
**metadata** | [**List[ScoreSlimChunks]**](ScoreSlimChunks.md) |  | 

## Example

```python
from trieve_py_client.models.group_score_slim_chunks import GroupScoreSlimChunks

# TODO update the JSON string below
json = "{}"
# create an instance of GroupScoreSlimChunks from a JSON string
group_score_slim_chunks_instance = GroupScoreSlimChunks.from_json(json)
# print the JSON string representation of the object
print(GroupScoreSlimChunks.to_json())

# convert the object into a dict
group_score_slim_chunks_dict = group_score_slim_chunks_instance.to_dict()
# create an instance of GroupScoreSlimChunks from a dict
group_score_slim_chunks_form_dict = group_score_slim_chunks.from_dict(group_score_slim_chunks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


