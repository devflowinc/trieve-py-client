# RecommendChunksRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**ChunkFilter**](ChunkFilter.md) |  | [optional] 
**limit** | **int** | The number of chunks to return. This is the number of chunks which will be returned in the response. The default is 10. | [optional] 
**negative_chunk_ids** | **List[str]** | The ids of the chunks to be used as negative examples for the recommendation. The chunks in this array will be used to filter out similar chunks. | [optional] 
**negative_tracking_ids** | **List[str]** | The tracking_ids of the chunks to be used as negative examples for the recommendation. The chunks in this array will be used to filter out similar chunks. | [optional] 
**positive_chunk_ids** | **List[str]** | The ids of the chunks to be used as positive examples for the recommendation. The chunks in this array will be used to find similar chunks. | [optional] 
**positive_tracking_ids** | **List[str]** | The tracking_ids of the chunks to be used as positive examples for the recommendation. The chunks in this array will be used to find similar chunks. | [optional] 

## Example

```python
from trieve_python_client.models.recommend_chunks_request import RecommendChunksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendChunksRequest from a JSON string
recommend_chunks_request_instance = RecommendChunksRequest.from_json(json)
# print the JSON string representation of the object
print(RecommendChunksRequest.to_json())

# convert the object into a dict
recommend_chunks_request_dict = recommend_chunks_request_instance.to_dict()
# create an instance of RecommendChunksRequest from a dict
recommend_chunks_request_form_dict = recommend_chunks_request.from_dict(recommend_chunks_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


