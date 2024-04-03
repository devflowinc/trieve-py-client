# UpdateUserData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | In the sense of a legal name, not a username. The new name to assign to the user, if not provided, the current name will be used. | [optional] 
**organization_id** | **str** | The id of the organization to update the user for. | 
**role** | **int** | Either 0 (user), 1 (admin), or 2 (owner). If not provided, the current role will be used. The auth&#39;ed user must have a role greater than or equal to the role being assigned. | [optional] 
**user_id** | **str** | The id of the user to update, if not provided, the auth&#39;ed user will be updated. If provided, the auth&#39;ed user must be an admin (1) or owner (2) of the organization. | [optional] 

## Example

```python
from trieve_py_client.models.update_user_data import UpdateUserData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserData from a JSON string
update_user_data_instance = UpdateUserData.from_json(json)
# print the JSON string representation of the object
print(UpdateUserData.to_json())

# convert the object into a dict
update_user_data_dict = update_user_data_instance.to_dict()
# create an instance of UpdateUserData from a dict
update_user_data_form_dict = update_user_data.from_dict(update_user_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


