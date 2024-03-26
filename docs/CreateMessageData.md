# CreateMessageData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**highlight_citations** | **bool** | Whether or not to highlight the citations in the response. If this is set to true or not included, the citations will be highlighted. If this is set to false, the citations will not be highlighted. Default is true. | [optional] 
**highlight_delimiters** | **List[str]** | The delimiters to use for highlighting the citations. If this is not included, the default delimiters will be used. Default is &#x60;[\&quot;.\&quot;, \&quot;!\&quot;, \&quot;?\&quot;, \&quot;\\n\&quot;, \&quot;\\t\&quot;, \&quot;,\&quot;]&#x60;. | [optional] 
**model** | **str** | The model to use for the assistant&#39;s messages. This can be any model from the openrouter model list. If no model is provided, gpt-3.5-turbo will be used. | [optional] 
**new_message_content** | **str** | The content of the user message to attach to the topic and then generate an assistant message in response to. | 
**stream_response** | **bool** | Whether or not to stream the response. If this is set to true or not included, the response will be a stream. If this is set to false, the response will be a normal JSON response. Default is true. | [optional] 
**topic_id** | **str** | The ID of the topic to attach the message to. | 

## Example

```python
from trieve_python_client.models.create_message_data import CreateMessageData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMessageData from a JSON string
create_message_data_instance = CreateMessageData.from_json(json)
# print the JSON string representation of the object
print(CreateMessageData.to_json())

# convert the object into a dict
create_message_data_dict = create_message_data_instance.to_dict()
# create an instance of CreateMessageData from a dict
create_message_data_form_dict = create_message_data.from_dict(create_message_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


