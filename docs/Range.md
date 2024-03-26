# Range


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gt** | **float** |  | [optional] 
**gte** | **float** |  | [optional] 
**lt** | **float** |  | [optional] 
**lte** | **float** |  | [optional] 

## Example

```python
from trieve_python_client.models.range import Range

# TODO update the JSON string below
json = "{}"
# create an instance of Range from a JSON string
range_instance = Range.from_json(json)
# print the JSON string representation of the object
print(Range.to_json())

# convert the object into a dict
range_dict = range_instance.to_dict()
# create an instance of Range from a dict
range_form_dict = range.from_dict(range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


