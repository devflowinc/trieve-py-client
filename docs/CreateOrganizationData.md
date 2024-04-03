# CreateOrganizationData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The arbitrary name which will be used to identify the organization. This name must be unique. | 

## Example

```python
from trieve_py_client.models.create_organization_data import CreateOrganizationData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationData from a JSON string
create_organization_data_instance = CreateOrganizationData.from_json(json)
# print the JSON string representation of the object
print(CreateOrganizationData.to_json())

# convert the object into a dict
create_organization_data_dict = create_organization_data_instance.to_dict()
# create an instance of CreateOrganizationData from a dict
create_organization_data_form_dict = create_organization_data.from_dict(create_organization_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


