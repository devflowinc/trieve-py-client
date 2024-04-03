# ScoreSlimChunks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[SlimChunkMetadata]**](SlimChunkMetadata.md) |  | 
**score** | **float** |  | 

## Example

```python
from trieve_py_client.models.score_slim_chunks import ScoreSlimChunks

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreSlimChunks from a JSON string
score_slim_chunks_instance = ScoreSlimChunks.from_json(json)
# print the JSON string representation of the object
print(ScoreSlimChunks.to_json())

# convert the object into a dict
score_slim_chunks_dict = score_slim_chunks_instance.to_dict()
# create an instance of ScoreSlimChunks from a dict
score_slim_chunks_form_dict = score_slim_chunks.from_dict(score_slim_chunks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


