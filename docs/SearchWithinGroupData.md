# SearchWithinGroupData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_bias** | **bool** | Set date_bias to true to bias search results towards more recent chunks. This will work best in hybrid search mode. | [optional] 
**filters** | [**ChunkFilter**](ChunkFilter.md) |  | [optional] 
**group_id** | **str** | Group specifies the group to search within. Results will only consist of chunks which are bookmarks within the specified group. | [optional] 
**group_tracking_id** | **str** | Group_tracking_id specifies the group to search within by tracking id. Results will only consist of chunks which are bookmarks within the specified group. If both group_id and group_tracking_id are provided, group_id will be used. | [optional] 
**highlight_delimiters** | **List[str]** | Set highlight_delimiters to a list of strings to use as delimiters for highlighting. If not specified, this defaults to [\&quot;?\&quot;, \&quot;,\&quot;, \&quot;.\&quot;, \&quot;!\&quot;]. | [optional] 
**highlight_results** | **bool** | Set highlight_results to true to highlight the results. If not specified, this defaults to true. | [optional] 
**page** | **int** | The page of chunks to fetch. Page is 1-indexed. | [optional] 
**page_size** | **int** | The page size is the number of chunks to fetch. This can be used to fetch more than 10 chunks at a time. | [optional] 
**query** | **str** | The query is the search query. This can be any string. The query will be used to create an embedding vector and/or SPLADE vector which will be used to find the result set. | 
**score_threshold** | **float** | Set score_threshold to a float to filter out chunks with a score below the threshold. | [optional] 
**search_type** | **str** | Search_type can be either \&quot;semantic\&quot;, \&quot;fulltext\&quot;, or \&quot;hybrid\&quot;. \&quot;hybrid\&quot; will pull in one page (10 chunks) of both semantic and full-text results then re-rank them using BAAI/bge-reranker-large. \&quot;semantic\&quot; will pull in one page (10 chunks) of the nearest cosine distant vectors. \&quot;fulltext\&quot; will pull in one page (10 chunks) of full-text results based on SPLADE. | 
**slim_chunks** | **bool** | Set slim_chunks to true to avoid returning the content and chunk_html of the chunks. This is useful for when you want to reduce amount of data over the wire for latency improvement. Default is false. | [optional] 
**use_weights** | **bool** | Set use_weights to true to use the weights of the chunks in the result set in order to sort them. If not specified, this defaults to true. | [optional] 

## Example

```python
from trieve_py_client.models.search_within_group_data import SearchWithinGroupData

# TODO update the JSON string below
json = "{}"
# create an instance of SearchWithinGroupData from a JSON string
search_within_group_data_instance = SearchWithinGroupData.from_json(json)
# print the JSON string representation of the object
print(SearchWithinGroupData.to_json())

# convert the object into a dict
search_within_group_data_dict = search_within_group_data_instance.to_dict()
# create an instance of SearchWithinGroupData from a dict
search_within_group_data_form_dict = search_within_group_data.from_dict(search_within_group_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


