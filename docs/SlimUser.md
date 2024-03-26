# SlimUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**orgs** | [**List[Organization]**](Organization.md) |  | 
**user_orgs** | [**List[UserOrganization]**](UserOrganization.md) |  | 
**username** | **str** |  | [optional] 
**visible_email** | **bool** |  | 
**website** | **str** |  | [optional] 

## Example

```python
from trieve_python_client.models.slim_user import SlimUser

# TODO update the JSON string below
json = "{}"
# create an instance of SlimUser from a JSON string
slim_user_instance = SlimUser.from_json(json)
# print the JSON string representation of the object
print(SlimUser.to_json())

# convert the object into a dict
slim_user_dict = slim_user_instance.to_dict()
# create an instance of SlimUser from a dict
slim_user_form_dict = slim_user.from_dict(slim_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


