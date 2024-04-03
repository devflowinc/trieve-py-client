# SearchWithinGroupResponseTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bookmarks** | [**List[ScoreSlimChunks]**](ScoreSlimChunks.md) |  | 
**group** | [**ChunkGroup**](ChunkGroup.md) |  | 
**total_pages** | **int** |  | 

## Example

```python
from trieve_python_client.models.search_within_group_response_types import SearchWithinGroupResponseTypes

# TODO update the JSON string below
json = "{}"
# create an instance of SearchWithinGroupResponseTypes from a JSON string
search_within_group_response_types_instance = SearchWithinGroupResponseTypes.from_json(json)
# print the JSON string representation of the object
print(SearchWithinGroupResponseTypes.to_json())

# convert the object into a dict
search_within_group_response_types_dict = search_within_group_response_types_instance.to_dict()
# create an instance of SearchWithinGroupResponseTypes from a dict
search_within_group_response_types_form_dict = search_within_group_response_types.from_dict(search_within_group_response_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


