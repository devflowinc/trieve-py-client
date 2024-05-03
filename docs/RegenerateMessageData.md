# RegenerateMessageData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**highlight_citations** | **bool** | Whether or not to highlight the citations in the response. If this is set to true or not included, the citations will be highlighted. If this is set to false, the citations will not be highlighted. Default is true. | [optional] 
**highlight_delimiters** | **List[str]** | The delimiters to use for highlighting the citations. If this is not included, the default delimiters will be used. Default is &#x60;[\&quot;.\&quot;, \&quot;!\&quot;, \&quot;?\&quot;, \&quot;\\n\&quot;, \&quot;\\t\&quot;, \&quot;,\&quot;]&#x60;. | [optional] 
**stream_response** | **bool** | Whether or not to stream the response. If this is set to true or not included, the response will be a stream. If this is set to false, the response will be a normal JSON response. Default is true. | [optional] 
**topic_id** | **str** | The id of the topic to regenerate the last message for. | 

## Example

```python
from trieve_py_client.models.regenerate_message_data import RegenerateMessageData

# TODO update the JSON string below
json = "{}"
# create an instance of RegenerateMessageData from a JSON string
regenerate_message_data_instance = RegenerateMessageData.from_json(json)
# print the JSON string representation of the object
print(RegenerateMessageData.to_json())

# convert the object into a dict
regenerate_message_data_dict = regenerate_message_data_instance.to_dict()
# create an instance of RegenerateMessageData from a dict
regenerate_message_data_form_dict = regenerate_message_data.from_dict(regenerate_message_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


