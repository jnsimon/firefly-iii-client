# firefly_iii_client.model.transaction_split_store.TransactionSplitStore

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**date** | str, datetime,  | str,  | Date of the transaction | value must conform to RFC-3339 date-time
**amount** | str,  | str,  | Amount of the transaction. | 
**description** | str,  | str,  | Description of the transaction. | 
**type** | [**TransactionTypeProperty**](TransactionTypeProperty.md) | [**TransactionTypeProperty**](TransactionTypeProperty.md) |  | 
**bill_id** | None, str,  | NoneClass, str,  | Optional. Use either this or the bill_name | [optional] 
**bill_name** | None, str,  | NoneClass, str,  | Optional. Use either this or the bill_id | [optional] 
**book_date** | None, str, datetime,  | NoneClass, str,  |  | [optional] value must conform to RFC-3339 date-time
**budget_id** | None, str,  | NoneClass, str,  | The budget ID for this transaction. | [optional] 
**budget_name** | None, str,  | NoneClass, str,  | The name of the budget to be used. If the budget name is unknown, the ID will be used or the value will be ignored. | [optional] 
**bunq_payment_id** | None, str,  | NoneClass, str,  | Internal ID of bunq transaction. Field is no longer used but still works. | [optional] 
**category_id** | None, str,  | NoneClass, str,  | The category ID for this transaction. | [optional] 
**category_name** | None, str,  | NoneClass, str,  | The name of the category to be used. If the category is unknown, it will be created. If the ID and the name point to different categories, the ID overrules the name. | [optional] 
**currency_code** | None, str,  | NoneClass, str,  | Currency code. Default is the source account&#x27;s currency, or the user&#x27;s default currency. The value you submit may be overruled by the source or destination account. | [optional] 
**currency_id** | None, str,  | NoneClass, str,  | Currency ID. Default is the source account&#x27;s currency, or the user&#x27;s default currency. The value you submit may be overruled by the source or destination account. | [optional] 
**destination_id** | None, str,  | NoneClass, str,  | ID of the destination account. For a deposit or a transfer, this must always be an asset account. For withdrawals this must be an expense account. | [optional] 
**destination_name** | None, str,  | NoneClass, str,  | Name of the destination account. You can submit the name instead of the ID. For everything except transfers, the account will be auto-generated if unknown, so submitting a name is enough. | [optional] 
**due_date** | None, str, datetime,  | NoneClass, str,  |  | [optional] value must conform to RFC-3339 date-time
**external_id** | None, str,  | NoneClass, str,  | Reference to external ID in other systems. | [optional] 
**external_url** | None, str,  | NoneClass, str,  | External, custom URL for this transaction. | [optional] 
**foreign_amount** | None, str,  | NoneClass, str,  | The amount in a foreign currency. | [optional] 
**foreign_currency_code** | None, str,  | NoneClass, str,  | Currency code of the foreign currency. Default is NULL. Can be used instead of the foreign_currency_id, but this or the ID is required when submitting a foreign amount. | [optional] 
**foreign_currency_id** | None, str,  | NoneClass, str,  | Currency ID of the foreign currency. Default is null. Is required when you submit a foreign amount. | [optional] 
**interest_date** | None, str, datetime,  | NoneClass, str,  |  | [optional] value must conform to RFC-3339 date-time
**internal_reference** | None, str,  | NoneClass, str,  | Reference to internal reference of other systems. | [optional] 
**invoice_date** | None, str, datetime,  | NoneClass, str,  |  | [optional] value must conform to RFC-3339 date-time
**notes** | None, str,  | NoneClass, str,  |  | [optional] 
**order** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Order of this entry in the list of transactions. | [optional] value must be a 32 bit integer
**payment_date** | None, str, datetime,  | NoneClass, str,  |  | [optional] value must conform to RFC-3339 date-time
**piggy_bank_id** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Optional. Use either this or the piggy_bank_name | [optional] value must be a 32 bit integer
**piggy_bank_name** | None, str,  | NoneClass, str,  | Optional. Use either this or the piggy_bank_id | [optional] 
**process_date** | None, str, datetime,  | NoneClass, str,  |  | [optional] value must conform to RFC-3339 date-time
**reconciled** | bool,  | BoolClass,  | If the transaction has been reconciled already. When you set this, the amount can no longer be edited by the user. | [optional] 
**sepa_batch_id** | None, str,  | NoneClass, str,  | SEPA Batch ID | [optional] 
**sepa_cc** | None, str,  | NoneClass, str,  | SEPA Clearing Code | [optional] 
**sepa_ci** | None, str,  | NoneClass, str,  | SEPA Creditor Identifier | [optional] 
**sepa_country** | None, str,  | NoneClass, str,  | SEPA Country | [optional] 
**sepa_ct_id** | None, str,  | NoneClass, str,  | SEPA end-to-end Identifier | [optional] 
**sepa_ct_op** | None, str,  | NoneClass, str,  | SEPA Opposing Account Identifier | [optional] 
**sepa_db** | None, str,  | NoneClass, str,  | SEPA mandate identifier | [optional] 
**sepa_ep** | None, str,  | NoneClass, str,  | SEPA External Purpose indicator | [optional] 
**source_id** | None, str,  | NoneClass, str,  | ID of the source account. For a withdrawal or a transfer, this must always be an asset account. For deposits, this must be a revenue account. | [optional] 
**source_name** | None, str,  | NoneClass, str,  | Name of the source account. For a withdrawal or a transfer, this must always be an asset account. For deposits, this must be a revenue account. Can be used instead of the source_id. If the transaction is a deposit, the source_name can be filled in freely: the account will be created based on the name. | [optional] 
**[tags](#tags)** | list, tuple, None,  | tuple, NoneClass,  | Array of tags. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tags

Array of tags.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | Array of tags. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Tag. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

