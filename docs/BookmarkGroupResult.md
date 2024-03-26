# BookmarkGroupResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_uuid** | **str** |  | 
**slim_groups** | [**List[SlimGroup]**](SlimGroup.md) |  | 

## Example

```python
from trieve_python_client.models.bookmark_group_result import BookmarkGroupResult

# TODO update the JSON string below
json = "{}"
# create an instance of BookmarkGroupResult from a JSON string
bookmark_group_result_instance = BookmarkGroupResult.from_json(json)
# print the JSON string representation of the object
print(BookmarkGroupResult.to_json())

# convert the object into a dict
bookmark_group_result_dict = bookmark_group_result_instance.to_dict()
# create an instance of BookmarkGroupResult from a dict
bookmark_group_result_form_dict = bookmark_group_result.from_dict(bookmark_group_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


