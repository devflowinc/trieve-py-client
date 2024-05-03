# FieldCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | Field is the name of the field to filter on. The field value will be used to check for an exact substring match on the metadata values for each existing chunk. This is useful for when you want to filter chunks by arbitrary metadata. To access fields inside of the metadata that you provide with the card, prefix the field name with &#x60;metadata.&#x60;. | 
**geo_bounding_box** | [**LocationBoundingBox**](LocationBoundingBox.md) |  | [optional] 
**geo_polygon** | [**LocationPolygon**](LocationPolygon.md) |  | [optional] 
**geo_radius** | [**LocationRadius**](LocationRadius.md) |  | [optional] 
**match** | [**List[MatchCondition]**](MatchCondition.md) | Match is the value to match on the field. The match value will be used to check for an exact substring match on the metadata values for each existing chunk. This is useful for when you want to filter chunks by arbitrary metadata. | [optional] 
**range** | [**Range**](Range.md) |  | [optional] 

## Example

```python
from trieve_py_client.models.field_condition import FieldCondition

# TODO update the JSON string below
json = "{}"
# create an instance of FieldCondition from a JSON string
field_condition_instance = FieldCondition.from_json(json)
# print the JSON string representation of the object
print(FieldCondition.to_json())

# convert the object into a dict
field_condition_dict = field_condition_instance.to_dict()
# create an instance of FieldCondition from a dict
field_condition_form_dict = field_condition.from_dict(field_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


