# SearchOverGroupsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**ChunkFilter**](ChunkFilter.md) |  | [optional] 
**get_collisions** | **bool** | Set get_collisions to true to get the collisions for each chunk. This will only apply if environment variable COLLISIONS_ENABLED is set to true. | [optional] 
**group_size** | **int** |  | [optional] 
**highlight_delimiters** | **List[str]** | Set highlight_delimiters to a list of strings to use as delimiters for highlighting. If not specified, this defaults to [\&quot;?\&quot;, \&quot;,\&quot;, \&quot;.\&quot;, \&quot;!\&quot;]. | [optional] 
**highlight_results** | **bool** | Set highlight_results to true to highlight the results. If not specified, this defaults to true. | [optional] 
**page** | **int** | Page of chunks to fetch. Each page is 10 chunks. Support for custom page size is coming soon. | [optional] 
**page_size** | **int** | Page size is the number of chunks to fetch. This can be used to fetch more than 10 chunks at a time. | [optional] 
**query** | **str** | Query is the search query. This can be any string. The query will be used to create an embedding vector and/or SPLADE vector which will be used to find the result set. | 
**score_threshold** | **float** | Set score_threshold to a float to filter out chunks with a score below the threshold. | [optional] 
**search_type** | **str** | Can be either \&quot;semantic\&quot;, \&quot;fulltext\&quot;, or \&quot;hybrid\&quot;. \&quot;hybrid\&quot; will pull in one page (10 chunks) of both semantic and full-text results then re-rank them using BAAI/bge-reranker-large. \&quot;semantic\&quot; will pull in one page (10 chunks) of the nearest cosine distant vectors. \&quot;fulltext\&quot; will pull in one page (10 chunks) of full-text results based on SPLADE. | 

## Example

```python
from trieve_python_client.models.search_over_groups_data import SearchOverGroupsData

# TODO update the JSON string below
json = "{}"
# create an instance of SearchOverGroupsData from a JSON string
search_over_groups_data_instance = SearchOverGroupsData.from_json(json)
# print the JSON string representation of the object
print(SearchOverGroupsData.to_json())

# convert the object into a dict
search_over_groups_data_dict = search_over_groups_data_instance.to_dict()
# create an instance of SearchOverGroupsData from a dict
search_over_groups_data_form_dict = search_over_groups_data.from_dict(search_over_groups_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


