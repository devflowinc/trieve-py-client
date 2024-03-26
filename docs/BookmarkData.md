# BookmarkData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunks** | [**List[ChunkMetadataWithFileData]**](ChunkMetadataWithFileData.md) |  | 
**group** | [**ChunkGroup**](ChunkGroup.md) |  | 
**total_pages** | **int** |  | 

## Example

```python
from trieve_python_client.models.bookmark_data import BookmarkData

# TODO update the JSON string below
json = "{}"
# create an instance of BookmarkData from a JSON string
bookmark_data_instance = BookmarkData.from_json(json)
# print the JSON string representation of the object
print(BookmarkData.to_json())

# convert the object into a dict
bookmark_data_dict = bookmark_data_instance.to_dict()
# create an instance of BookmarkData from a dict
bookmark_data_form_dict = bookmark_data.from_dict(bookmark_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


