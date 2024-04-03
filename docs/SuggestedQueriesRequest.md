# SuggestedQueriesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The query to base the generated suggested queries off of. | 

## Example

```python
from trieve_py_client.models.suggested_queries_request import SuggestedQueriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestedQueriesRequest from a JSON string
suggested_queries_request_instance = SuggestedQueriesRequest.from_json(json)
# print the JSON string representation of the object
print(SuggestedQueriesRequest.to_json())

# convert the object into a dict
suggested_queries_request_dict = suggested_queries_request_instance.to_dict()
# create an instance of SuggestedQueriesRequest from a dict
suggested_queries_request_form_dict = suggested_queries_request.from_dict(suggested_queries_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


