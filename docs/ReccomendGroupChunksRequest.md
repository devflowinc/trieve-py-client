# ReccomendGroupChunksRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**ChunkFilter**](ChunkFilter.md) |  | [optional] 
**group_size** | **int** | The number of chunks to fetch for each group. This is the number of chunks which will be returned in the response for each group. The default is 10. | [optional] 
**limit** | **int** | The number of groups to return. This is the number of groups which will be returned in the response. The default is 10. | [optional] 
**negative_group_ids** | **List[str]** | The  ids of the groups to be used as negative examples for the recommendation. The groups in this array will be used to filter out similar groups. | [optional] 
**negative_group_tracking_ids** | **List[str]** | The  ids of the groups to be used as negative examples for the recommendation. The groups in this array will be used to filter out similar groups. | [optional] 
**positive_group_ids** | **List[str]** | The  ids of the groups to be used as positive examples for the recommendation. The groups in this array will be used to find similar groups. | [optional] 
**positive_group_tracking_ids** | **List[str]** | The  ids of the groups to be used as positive examples for the recommendation. The groups in this array will be used to find similar groups. | [optional] 

## Example

```python
from trieve_python_client.models.reccomend_group_chunks_request import ReccomendGroupChunksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReccomendGroupChunksRequest from a JSON string
reccomend_group_chunks_request_instance = ReccomendGroupChunksRequest.from_json(json)
# print the JSON string representation of the object
print(ReccomendGroupChunksRequest.to_json())

# convert the object into a dict
reccomend_group_chunks_request_dict = reccomend_group_chunks_request_instance.to_dict()
# create an instance of ReccomendGroupChunksRequest from a dict
reccomend_group_chunks_request_form_dict = reccomend_group_chunks_request.from_dict(reccomend_group_chunks_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


