# SearchOverGroupsSlimChunksResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_chunks** | [**List[GroupSlimChunksDTO]**](GroupSlimChunksDTO.md) |  | 
**total_chunk_pages** | **int** |  | 

## Example

```python
from trieve_python_client.models.search_over_groups_slim_chunks_response_body import SearchOverGroupsSlimChunksResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of SearchOverGroupsSlimChunksResponseBody from a JSON string
search_over_groups_slim_chunks_response_body_instance = SearchOverGroupsSlimChunksResponseBody.from_json(json)
# print the JSON string representation of the object
print(SearchOverGroupsSlimChunksResponseBody.to_json())

# convert the object into a dict
search_over_groups_slim_chunks_response_body_dict = search_over_groups_slim_chunks_response_body_instance.to_dict()
# create an instance of SearchOverGroupsSlimChunksResponseBody from a dict
search_over_groups_slim_chunks_response_body_form_dict = search_over_groups_slim_chunks_response_body.from_dict(search_over_groups_slim_chunks_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


