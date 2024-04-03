# CreateTopicData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_user_message** | **str** | The first message which will belong to the topic. The topic name is generated based on this message similar to how it works in the OpenAI chat UX if a name is not explicitly provided on the name request body key. | [optional] 
**model** | **str** | The model to use for the assistant&#39;s messages. This can be any model from the openrouter model list. If no model is provided, the gpt-3.5-turbo will be used. | [optional] 
**name** | **str** | The name of the topic. If this is not provided, the topic name is generated from the first_user_message. | [optional] 

## Example

```python
from trieve_py_client.models.create_topic_data import CreateTopicData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTopicData from a JSON string
create_topic_data_instance = CreateTopicData.from_json(json)
# print the JSON string representation of the object
print(CreateTopicData.to_json())

# convert the object into a dict
create_topic_data_dict = create_topic_data_instance.to_dict()
# create an instance of CreateTopicData from a dict
create_topic_data_form_dict = create_topic_data.from_dict(create_topic_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


