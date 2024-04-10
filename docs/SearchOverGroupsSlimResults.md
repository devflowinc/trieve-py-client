# SearchOverGroupsSlimResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_chunks** | [**List[GroupScoreSlimChunks]**](GroupScoreSlimChunks.md) |  | 
**total_chunk_pages** | **int** |  | 

## Example

```python
from trieve_py_client.models.search_over_groups_slim_results import SearchOverGroupsSlimResults

# TODO update the JSON string below
json = "{}"
# create an instance of SearchOverGroupsSlimResults from a JSON string
search_over_groups_slim_results_instance = SearchOverGroupsSlimResults.from_json(json)
# print the JSON string representation of the object
print(SearchOverGroupsSlimResults.to_json())

# convert the object into a dict
search_over_groups_slim_results_dict = search_over_groups_slim_results_instance.to_dict()
# create an instance of SearchOverGroupsSlimResults from a dict
search_over_groups_slim_results_form_dict = search_over_groups_slim_results.from_dict(search_over_groups_slim_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


