# UpdateTopicData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new name of the topic. A name is not generated from this field, it is used as-is. | 
**topic_id** | **str** | The id of the topic to target. | 

## Example

```python
from trieve_python_client.models.update_topic_data import UpdateTopicData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTopicData from a JSON string
update_topic_data_instance = UpdateTopicData.from_json(json)
# print the JSON string representation of the object
print(UpdateTopicData.to_json())

# convert the object into a dict
update_topic_data_dict = update_topic_data_instance.to_dict()
# create an instance of UpdateTopicData from a dict
update_topic_data_form_dict = update_topic_data.from_dict(update_topic_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


