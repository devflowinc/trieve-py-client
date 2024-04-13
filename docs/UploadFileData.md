# UploadFileData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base64_file** | **str** | Base64 encoded file. Convert + to -, / to _, and remove the ending &#x3D; if present. This is the standard base64url encoding. | 
**create_chunks** | **bool** | Create chunks is a boolean which determines whether or not to create chunks from the file. If false, you can manually chunk the file and send the chunks to the create_chunk endpoint with the file_id to associate chunks with the file. Meant mostly for advanced users. | [optional] 
**description** | **str** | Description is an optional convience field so you do not have to remember what the file contains or is about. It will be included on the group resulting from the file which will hold its chunk. | [optional] 
**file_name** | **str** | Name of the file being uploaded, including the extension. | 
**group_tracking_id** | **str** | Group tracking id is an optional field which allows you to specify the tracking id of the group that is created from the file. Chunks created will be created with the tracking id of &#x60;group_tracking_id|&lt;index of chunk&gt;&#x60; | [optional] 
**link** | **str** | Link to the file. This can also be any string. This can be used to filter when searching for the file&#39;s resulting chunks. The link value will not affect embedding creation. | [optional] 
**metadata** | **object** | Metadata is a JSON object which can be used to filter chunks. This is useful for when you want to filter chunks by arbitrary metadata. Unlike with tag filtering, there is a performance hit for filtering on metadata. Will be passed down to the file&#39;s chunks. | [optional] 
**tag_set** | **List[str]** | Tag set is a comma separated list of tags which will be passed down to the chunks made from the file. Tags are used to filter chunks when searching. HNSW indices are created for each tag such that there is no performance loss when filtering on them. | [optional] 
**time_stamp** | **str** | Time stamp should be an ISO 8601 combined date and time without timezone. Time_stamp is used for time window filtering and recency-biasing search results. Will be passed down to the file&#39;s chunks. | [optional] 

## Example

```python
from trieve_py_client.models.upload_file_data import UploadFileData

# TODO update the JSON string below
json = "{}"
# create an instance of UploadFileData from a JSON string
upload_file_data_instance = UploadFileData.from_json(json)
# print the JSON string representation of the object
print(UploadFileData.to_json())

# convert the object into a dict
upload_file_data_dict = upload_file_data_instance.to_dict()
# create an instance of UploadFileData from a dict
upload_file_data_form_dict = upload_file_data.from_dict(upload_file_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


