# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from firefly_iii_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_ABOUT = "/v1/about"
    V1_ABOUT_USER = "/v1/about/user"
    V1_ACCOUNTS = "/v1/accounts"
    V1_ACCOUNTS_ID = "/v1/accounts/{id}"
    V1_ACCOUNTS_ID_ATTACHMENTS = "/v1/accounts/{id}/attachments"
    V1_ACCOUNTS_ID_PIGGYBANKS = "/v1/accounts/{id}/piggy-banks"
    V1_ACCOUNTS_ID_TRANSACTIONS = "/v1/accounts/{id}/transactions"
    V1_ATTACHMENTS = "/v1/attachments"
    V1_ATTACHMENTS_ID = "/v1/attachments/{id}"
    V1_ATTACHMENTS_ID_DOWNLOAD = "/v1/attachments/{id}/download"
    V1_ATTACHMENTS_ID_UPLOAD = "/v1/attachments/{id}/upload"
    V1_AUTOCOMPLETE_ACCOUNTS = "/v1/autocomplete/accounts"
    V1_AUTOCOMPLETE_BILLS = "/v1/autocomplete/bills"
    V1_AUTOCOMPLETE_BUDGETS = "/v1/autocomplete/budgets"
    V1_AUTOCOMPLETE_CATEGORIES = "/v1/autocomplete/categories"
    V1_AUTOCOMPLETE_CURRENCIES = "/v1/autocomplete/currencies"
    V1_AUTOCOMPLETE_CURRENCIESWITHCODE = "/v1/autocomplete/currencies-with-code"
    V1_AUTOCOMPLETE_OBJECTGROUPS = "/v1/autocomplete/object-groups"
    V1_AUTOCOMPLETE_PIGGYBANKS = "/v1/autocomplete/piggy-banks"
    V1_AUTOCOMPLETE_PIGGYBANKSWITHBALANCE = "/v1/autocomplete/piggy-banks-with-balance"
    V1_AUTOCOMPLETE_RECURRING = "/v1/autocomplete/recurring"
    V1_AUTOCOMPLETE_RULEGROUPS = "/v1/autocomplete/rule-groups"
    V1_AUTOCOMPLETE_RULES = "/v1/autocomplete/rules"
    V1_AUTOCOMPLETE_TAGS = "/v1/autocomplete/tags"
    V1_AUTOCOMPLETE_TRANSACTIONTYPES = "/v1/autocomplete/transaction-types"
    V1_AUTOCOMPLETE_TRANSACTIONS = "/v1/autocomplete/transactions"
    V1_AUTOCOMPLETE_TRANSACTIONSWITHID = "/v1/autocomplete/transactions-with-id"
    V1_AVAILABLEBUDGETS = "/v1/available-budgets"
    V1_AVAILABLEBUDGETS_ID = "/v1/available-budgets/{id}"
    V1_BILLS = "/v1/bills"
    V1_BILLS_ID = "/v1/bills/{id}"
    V1_BILLS_ID_ATTACHMENTS = "/v1/bills/{id}/attachments"
    V1_BILLS_ID_RULES = "/v1/bills/{id}/rules"
    V1_BILLS_ID_TRANSACTIONS = "/v1/bills/{id}/transactions"
    V1_BUDGETLIMITS = "/v1/budget-limits"
    V1_BUDGETS = "/v1/budgets"
    V1_BUDGETS_ID = "/v1/budgets/{id}"
    V1_BUDGETS_ID_ATTACHMENTS = "/v1/budgets/{id}/attachments"
    V1_BUDGETS_ID_LIMITS = "/v1/budgets/{id}/limits"
    V1_BUDGETS_ID_LIMITS_LIMIT_ID = "/v1/budgets/{id}/limits/{limitId}"
    V1_BUDGETS_ID_LIMITS_LIMIT_ID_TRANSACTIONS = "/v1/budgets/{id}/limits/{limitId}/transactions"
    V1_BUDGETS_ID_TRANSACTIONS = "/v1/budgets/{id}/transactions"
    V1_CATEGORIES = "/v1/categories"
    V1_CATEGORIES_ID = "/v1/categories/{id}"
    V1_CATEGORIES_ID_ATTACHMENTS = "/v1/categories/{id}/attachments"
    V1_CATEGORIES_ID_TRANSACTIONS = "/v1/categories/{id}/transactions"
    V1_CHART_ACCOUNT_OVERVIEW = "/v1/chart/account/overview"
    V1_CONFIGURATION = "/v1/configuration"
    V1_CONFIGURATION_NAME = "/v1/configuration/{name}"
    V1_CRON_CLI_TOKEN = "/v1/cron/{cliToken}"
    V1_CURRENCIES = "/v1/currencies"
    V1_CURRENCIES_DEFAULT = "/v1/currencies/default"
    V1_CURRENCIES_CODE = "/v1/currencies/{code}"
    V1_CURRENCIES_CODE_ACCOUNTS = "/v1/currencies/{code}/accounts"
    V1_CURRENCIES_CODE_AVAILABLEBUDGETS = "/v1/currencies/{code}/available-budgets"
    V1_CURRENCIES_CODE_BILLS = "/v1/currencies/{code}/bills"
    V1_CURRENCIES_CODE_BUDGET_LIMITS = "/v1/currencies/{code}/budget_limits"
    V1_CURRENCIES_CODE_DEFAULT = "/v1/currencies/{code}/default"
    V1_CURRENCIES_CODE_DISABLE = "/v1/currencies/{code}/disable"
    V1_CURRENCIES_CODE_ENABLE = "/v1/currencies/{code}/enable"
    V1_CURRENCIES_CODE_RECURRENCES = "/v1/currencies/{code}/recurrences"
    V1_CURRENCIES_CODE_RULES = "/v1/currencies/{code}/rules"
    V1_CURRENCIES_CODE_TRANSACTIONS = "/v1/currencies/{code}/transactions"
    V1_DATA_BULK_TRANSACTIONS = "/v1/data/bulk/transactions"
    V1_DATA_DESTROY = "/v1/data/destroy"
    V1_DATA_EXPORT_ACCOUNTS = "/v1/data/export/accounts"
    V1_DATA_EXPORT_BILLS = "/v1/data/export/bills"
    V1_DATA_EXPORT_BUDGETS = "/v1/data/export/budgets"
    V1_DATA_EXPORT_CATEGORIES = "/v1/data/export/categories"
    V1_DATA_EXPORT_PIGGYBANKS = "/v1/data/export/piggy-banks"
    V1_DATA_EXPORT_RECURRING = "/v1/data/export/recurring"
    V1_DATA_EXPORT_RULES = "/v1/data/export/rules"
    V1_DATA_EXPORT_TAGS = "/v1/data/export/tags"
    V1_DATA_EXPORT_TRANSACTIONS = "/v1/data/export/transactions"
    V1_DATA_PURGE = "/v1/data/purge"
    V1_INSIGHT_EXPENSE_ASSET = "/v1/insight/expense/asset"
    V1_INSIGHT_EXPENSE_BILL = "/v1/insight/expense/bill"
    V1_INSIGHT_EXPENSE_BUDGET = "/v1/insight/expense/budget"
    V1_INSIGHT_EXPENSE_CATEGORY = "/v1/insight/expense/category"
    V1_INSIGHT_EXPENSE_EXPENSE = "/v1/insight/expense/expense"
    V1_INSIGHT_EXPENSE_NOBILL = "/v1/insight/expense/no-bill"
    V1_INSIGHT_EXPENSE_NOBUDGET = "/v1/insight/expense/no-budget"
    V1_INSIGHT_EXPENSE_NOCATEGORY = "/v1/insight/expense/no-category"
    V1_INSIGHT_EXPENSE_NOTAG = "/v1/insight/expense/no-tag"
    V1_INSIGHT_EXPENSE_TAG = "/v1/insight/expense/tag"
    V1_INSIGHT_EXPENSE_TOTAL = "/v1/insight/expense/total"
    V1_INSIGHT_INCOME_ASSET = "/v1/insight/income/asset"
    V1_INSIGHT_INCOME_CATEGORY = "/v1/insight/income/category"
    V1_INSIGHT_INCOME_NOCATEGORY = "/v1/insight/income/no-category"
    V1_INSIGHT_INCOME_NOTAG = "/v1/insight/income/no-tag"
    V1_INSIGHT_INCOME_REVENUE = "/v1/insight/income/revenue"
    V1_INSIGHT_INCOME_TAG = "/v1/insight/income/tag"
    V1_INSIGHT_INCOME_TOTAL = "/v1/insight/income/total"
    V1_INSIGHT_TRANSFER_ASSET = "/v1/insight/transfer/asset"
    V1_INSIGHT_TRANSFER_CATEGORY = "/v1/insight/transfer/category"
    V1_INSIGHT_TRANSFER_NOCATEGORY = "/v1/insight/transfer/no-category"
    V1_INSIGHT_TRANSFER_NOTAG = "/v1/insight/transfer/no-tag"
    V1_INSIGHT_TRANSFER_TAG = "/v1/insight/transfer/tag"
    V1_INSIGHT_TRANSFER_TOTAL = "/v1/insight/transfer/total"
    V1_LINKTYPES = "/v1/link-types"
    V1_LINKTYPES_ID = "/v1/link-types/{id}"
    V1_LINKTYPES_ID_TRANSACTIONS = "/v1/link-types/{id}/transactions"
    V1_OBJECTGROUPS = "/v1/object-groups"
    V1_OBJECTGROUPS_ID = "/v1/object-groups/{id}"
    V1_OBJECTGROUPS_ID_BILLS = "/v1/object-groups/{id}/bills"
    V1_OBJECTGROUPS_ID_PIGGYBANKS = "/v1/object-groups/{id}/piggy-banks"
    V1_PIGGYBANKS = "/v1/piggy-banks"
    V1_PIGGYBANKS_ID = "/v1/piggy-banks/{id}"
    V1_PIGGYBANKS_ID_ATTACHMENTS = "/v1/piggy-banks/{id}/attachments"
    V1_PIGGYBANKS_ID_EVENTS = "/v1/piggy-banks/{id}/events"
    V1_PREFERENCES = "/v1/preferences"
    V1_PREFERENCES_NAME = "/v1/preferences/{name}"
    V1_RECURRENCES = "/v1/recurrences"
    V1_RECURRENCES_ID = "/v1/recurrences/{id}"
    V1_RECURRENCES_ID_TRANSACTIONS = "/v1/recurrences/{id}/transactions"
    V1_RULEGROUPS = "/v1/rule-groups"
    V1_RULEGROUPS_ID = "/v1/rule-groups/{id}"
    V1_RULEGROUPS_ID_RULES = "/v1/rule-groups/{id}/rules"
    V1_RULEGROUPS_ID_TEST = "/v1/rule-groups/{id}/test"
    V1_RULEGROUPS_ID_TRIGGER = "/v1/rule-groups/{id}/trigger"
    V1_RULES = "/v1/rules"
    V1_RULES_ID = "/v1/rules/{id}"
    V1_RULES_ID_TEST = "/v1/rules/{id}/test"
    V1_RULES_ID_TRIGGER = "/v1/rules/{id}/trigger"
    V1_SEARCH_ACCOUNTS = "/v1/search/accounts"
    V1_SEARCH_TRANSACTIONS = "/v1/search/transactions"
    V1_SUMMARY_BASIC = "/v1/summary/basic"
    V1_TAGS = "/v1/tags"
    V1_TAGS_TAG = "/v1/tags/{tag}"
    V1_TAGS_TAG_ATTACHMENTS = "/v1/tags/{tag}/attachments"
    V1_TAGS_TAG_TRANSACTIONS = "/v1/tags/{tag}/transactions"
    V1_TRANSACTIONJOURNALS_ID = "/v1/transaction-journals/{id}"
    V1_TRANSACTIONJOURNALS_ID_LINKS = "/v1/transaction-journals/{id}/links"
    V1_TRANSACTIONLINKS = "/v1/transaction-links"
    V1_TRANSACTIONLINKS_ID = "/v1/transaction-links/{id}"
    V1_TRANSACTIONS = "/v1/transactions"
    V1_TRANSACTIONS_ID = "/v1/transactions/{id}"
    V1_TRANSACTIONS_ID_ATTACHMENTS = "/v1/transactions/{id}/attachments"
    V1_TRANSACTIONS_ID_PIGGYBANKEVENTS = "/v1/transactions/{id}/piggy-bank-events"
    V1_USERS = "/v1/users"
    V1_USERS_ID = "/v1/users/{id}"
    V1_WEBHOOKS = "/v1/webhooks"
    V1_WEBHOOKS_ID = "/v1/webhooks/{id}"
    V1_WEBHOOKS_ID_MESSAGES = "/v1/webhooks/{id}/messages"
    V1_WEBHOOKS_ID_MESSAGES_MESSAGE_ID = "/v1/webhooks/{id}/messages/{messageId}"
    V1_WEBHOOKS_ID_MESSAGES_MESSAGE_ID_ATTEMPTS = "/v1/webhooks/{id}/messages/{messageId}/attempts"
    V1_WEBHOOKS_ID_MESSAGES_MESSAGE_ID_ATTEMPTS_ATTEMPT_ID = "/v1/webhooks/{id}/messages/{messageId}/attempts/{attemptId}"
    V1_WEBHOOKS_ID_SUBMIT = "/v1/webhooks/{id}/submit"
    V1_WEBHOOKS_ID_TRIGGERTRANSACTION_TRANSACTION_ID = "/v1/webhooks/{id}/trigger-transaction/{transactionId}"