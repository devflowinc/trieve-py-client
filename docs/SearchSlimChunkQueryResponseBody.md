# SearchSlimChunkQueryResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score_chunks** | [**List[ScoreSlimChunks]**](ScoreSlimChunks.md) |  | 
**total_chunk_pages** | **int** |  | 

## Example

```python
from trieve_python_client.models.search_slim_chunk_query_response_body import SearchSlimChunkQueryResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSlimChunkQueryResponseBody from a JSON string
search_slim_chunk_query_response_body_instance = SearchSlimChunkQueryResponseBody.from_json(json)
# print the JSON string representation of the object
print(SearchSlimChunkQueryResponseBody.to_json())

# convert the object into a dict
search_slim_chunk_query_response_body_dict = search_slim_chunk_query_response_body_instance.to_dict()
# create an instance of SearchSlimChunkQueryResponseBody from a dict
search_slim_chunk_query_response_body_form_dict = search_slim_chunk_query_response_body.from_dict(search_slim_chunk_query_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


