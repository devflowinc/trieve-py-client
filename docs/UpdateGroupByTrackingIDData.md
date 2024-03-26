# UpdateGroupByTrackingIDData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description to assign to the chunk_group. Convenience field for you to avoid having to remember what the group is for. If not provided, the description will not be updated. | [optional] 
**name** | **str** | Name to assign to the chunk_group. Does not need to be unique. If not provided, the name will not be updated. | [optional] 
**tracking_id** | **str** | Tracking Id of the chunk_group to update. | 

## Example

```python
from trieve_python_client.models.update_group_by_tracking_id_data import UpdateGroupByTrackingIDData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGroupByTrackingIDData from a JSON string
update_group_by_tracking_id_data_instance = UpdateGroupByTrackingIDData.from_json(json)
# print the JSON string representation of the object
print(UpdateGroupByTrackingIDData.to_json())

# convert the object into a dict
update_group_by_tracking_id_data_dict = update_group_by_tracking_id_data_instance.to_dict()
# create an instance of UpdateGroupByTrackingIDData from a dict
update_group_by_tracking_id_data_form_dict = update_group_by_tracking_id_data.from_dict(update_group_by_tracking_id_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


