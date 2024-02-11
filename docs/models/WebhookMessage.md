# firefly_iii_client.model.webhook_message.WebhookMessage

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**errored** | bool,  | BoolClass,  | If this message has errored out. | [optional] 
**message** | None, str,  | NoneClass, str,  | The actual message that is sent or will be sent as JSON string. | [optional] 
**sent** | bool,  | BoolClass,  | If this message is sent yet. | [optional] 
**updated_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**uuid** | str,  | str,  | Long UUID string for identification of this webhook message. | [optional] 
**webhook_id** | str,  | str,  | The ID of the webhook this message belongs to. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

