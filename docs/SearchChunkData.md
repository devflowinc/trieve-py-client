# SearchChunkData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_bias** | **bool** | Set date_bias to true to bias search results towards more recent chunks. This will work best in hybrid search mode. | [optional] 
**filters** | [**ChunkFilter**](ChunkFilter.md) |  | [optional] 
**get_collisions** | **bool** | Set get_collisions to true to get the collisions for each chunk. This will only apply if environment variable COLLISIONS_ENABLED is set to true. | [optional] 
**highlight_delimiters** | **List[str]** | Set highlight_delimiters to a list of strings to use as delimiters for highlighting. If not specified, this defaults to [\&quot;?\&quot;, \&quot;,\&quot;, \&quot;.\&quot;, \&quot;!\&quot;]. | [optional] 
**highlight_results** | **bool** | Set highlight_results to true to highlight the results. If not specified, this defaults to true. | [optional] 
**page** | **int** | Page of chunks to fetch. Each page is 10 chunks. Support for custom page size is coming soon. | [optional] 
**page_size** | **int** | Page size is the number of chunks to fetch. This can be used to fetch more than 10 chunks at a time. | [optional] 
**query** | **str** | Query is the search query. This can be any string. The query will be used to create an embedding vector and/or SPLADE vector which will be used to find the result set. | 
**quote_negated_words** | **bool** | Turn on quote words and negated words to search for exact phrases and exclude words from the search results. Default is false. | [optional] 
**score_threshold** | **float** | Set score_threshold to a float to filter out chunks with a score below the threshold. | [optional] 
**search_type** | **str** | Can be either \&quot;semantic\&quot;, \&quot;fulltext\&quot;, or \&quot;hybrid\&quot;. \&quot;hybrid\&quot; will pull in one page (10 chunks) of both semantic and full-text results then re-rank them using BAAI/bge-reranker-large. \&quot;semantic\&quot; will pull in one page (10 chunks) of the nearest cosine distant vectors. \&quot;fulltext\&quot; will pull in one page (10 chunks) of full-text results based on SPLADE. | 
**slim_chunks** | **bool** | Set slim_chunks to true to avoid returning the content and chunk_html of the chunks. This is useful for when you want to reduce amount of data over the wire for latency improvement. Default is false. | [optional] 
**use_weights** | **bool** | Set use_weights to true to use the weights of the chunks in the result set in order to sort them. If not specified, this defaults to true. | [optional] 

## Example

```python
from trieve_py_client.models.search_chunk_data import SearchChunkData

# TODO update the JSON string below
json = "{}"
# create an instance of SearchChunkData from a JSON string
search_chunk_data_instance = SearchChunkData.from_json(json)
# print the JSON string representation of the object
print(SearchChunkData.to_json())

# convert the object into a dict
search_chunk_data_dict = search_chunk_data_instance.to_dict()
# create an instance of SearchChunkData from a dict
search_chunk_data_form_dict = search_chunk_data.from_dict(search_chunk_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


