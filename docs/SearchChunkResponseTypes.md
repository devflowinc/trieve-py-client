# SearchChunkResponseTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score_chunks** | [**List[ScoreChunkDTO]**](ScoreChunkDTO.md) |  | 
**total_chunk_pages** | **int** |  | 

## Example

```python
from trieve_python_client.models.search_chunk_response_types import SearchChunkResponseTypes

# TODO update the JSON string below
json = "{}"
# create an instance of SearchChunkResponseTypes from a JSON string
search_chunk_response_types_instance = SearchChunkResponseTypes.from_json(json)
# print the JSON string representation of the object
print(SearchChunkResponseTypes.to_json())

# convert the object into a dict
search_chunk_response_types_dict = search_chunk_response_types_instance.to_dict()
# create an instance of SearchChunkResponseTypes from a dict
search_chunk_response_types_form_dict = search_chunk_response_types.from_dict(search_chunk_response_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


