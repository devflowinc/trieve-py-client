# SearchGroupsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bookmarks** | [**List[ScoreChunkDTO]**](ScoreChunkDTO.md) |  | 
**group** | [**ChunkGroup**](ChunkGroup.md) |  | 
**total_pages** | **int** |  | 

## Example

```python
from trieve_py_client.models.search_groups_result import SearchGroupsResult

# TODO update the JSON string below
json = "{}"
# create an instance of SearchGroupsResult from a JSON string
search_groups_result_instance = SearchGroupsResult.from_json(json)
# print the JSON string representation of the object
print(SearchGroupsResult.to_json())

# convert the object into a dict
search_groups_result_dict = search_groups_result_instance.to_dict()
# create an instance of SearchGroupsResult from a dict
search_groups_result_form_dict = search_groups_result.from_dict(search_groups_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


