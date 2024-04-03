# SlimGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**of_current_dataset** | **bool** |  | 

## Example

```python
from trieve_py_client.models.slim_group import SlimGroup

# TODO update the JSON string below
json = "{}"
# create an instance of SlimGroup from a JSON string
slim_group_instance = SlimGroup.from_json(json)
# print the JSON string representation of the object
print(SlimGroup.to_json())

# convert the object into a dict
slim_group_dict = slim_group_instance.to_dict()
# create an instance of SlimGroup from a dict
slim_group_form_dict = slim_group.from_dict(slim_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


