# SearchWithinGroupSlimResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bookmarks** | [**List[ScoreSlimChunks]**](ScoreSlimChunks.md) |  | 
**group** | [**ChunkGroup**](ChunkGroup.md) |  | 
**total_pages** | **int** |  | 

## Example

```python
from trieve_py_client.models.search_within_group_slim_results import SearchWithinGroupSlimResults

# TODO update the JSON string below
json = "{}"
# create an instance of SearchWithinGroupSlimResults from a JSON string
search_within_group_slim_results_instance = SearchWithinGroupSlimResults.from_json(json)
# print the JSON string representation of the object
print(SearchWithinGroupSlimResults.to_json())

# convert the object into a dict
search_within_group_slim_results_dict = search_within_group_slim_results_instance.to_dict()
# create an instance of SearchWithinGroupSlimResults from a dict
search_within_group_slim_results_form_dict = search_within_group_slim_results.from_dict(search_within_group_slim_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


