# SearchGroupSlimChunksResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bookmarks** | [**List[ScoreSlimChunks]**](ScoreSlimChunks.md) |  | 
**group** | [**ChunkGroup**](ChunkGroup.md) |  | 
**total_pages** | **int** |  | 

## Example

```python
from trieve_python_client.models.search_group_slim_chunks_result import SearchGroupSlimChunksResult

# TODO update the JSON string below
json = "{}"
# create an instance of SearchGroupSlimChunksResult from a JSON string
search_group_slim_chunks_result_instance = SearchGroupSlimChunksResult.from_json(json)
# print the JSON string representation of the object
print(SearchGroupSlimChunksResult.to_json())

# convert the object into a dict
search_group_slim_chunks_result_dict = search_group_slim_chunks_result_instance.to_dict()
# create an instance of SearchGroupSlimChunksResult from a dict
search_group_slim_chunks_result_form_dict = search_group_slim_chunks_result.from_dict(search_group_slim_chunks_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


