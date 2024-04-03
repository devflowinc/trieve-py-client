# DatasetDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_configuration** | **object** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**organization_id** | **str** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from trieve_py_client.models.dataset_dto import DatasetDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetDTO from a JSON string
dataset_dto_instance = DatasetDTO.from_json(json)
# print the JSON string representation of the object
print(DatasetDTO.to_json())

# convert the object into a dict
dataset_dto_dict = dataset_dto_instance.to_dict()
# create an instance of DatasetDTO from a dict
dataset_dto_form_dict = dataset_dto.from_dict(dataset_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


