# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 2.0.12
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""

from firefly_iii_client.paths.v1_autocomplete_accounts.get import GetAccountsAc
from firefly_iii_client.paths.v1_autocomplete_bills.get import GetBillsAc
from firefly_iii_client.paths.v1_autocomplete_budgets.get import GetBudgetsAc
from firefly_iii_client.paths.v1_autocomplete_categories.get import GetCategoriesAc
from firefly_iii_client.paths.v1_autocomplete_currencies.get import GetCurrenciesAc
from firefly_iii_client.paths.v1_autocomplete_currencies_with_code.get import GetCurrenciesCodeAc
from firefly_iii_client.paths.v1_autocomplete_object_groups.get import GetObjectGroupsAc
from firefly_iii_client.paths.v1_autocomplete_piggy_banks.get import GetPiggiesAc
from firefly_iii_client.paths.v1_autocomplete_piggy_banks_with_balance.get import GetPiggiesBalanceAc
from firefly_iii_client.paths.v1_autocomplete_recurring.get import GetRecurringAc
from firefly_iii_client.paths.v1_autocomplete_rule_groups.get import GetRuleGroupsAc
from firefly_iii_client.paths.v1_autocomplete_rules.get import GetRulesAc
from firefly_iii_client.paths.v1_autocomplete_tags.get import GetTagAc
from firefly_iii_client.paths.v1_autocomplete_transaction_types.get import GetTransactionTypesAc
from firefly_iii_client.paths.v1_autocomplete_transactions.get import GetTransactionsAc
from firefly_iii_client.paths.v1_autocomplete_transactions_with_id.get import GetTransactionsIdac


class AutocompleteApi(
    GetAccountsAc,
    GetBillsAc,
    GetBudgetsAc,
    GetCategoriesAc,
    GetCurrenciesAc,
    GetCurrenciesCodeAc,
    GetObjectGroupsAc,
    GetPiggiesAc,
    GetPiggiesBalanceAc,
    GetRecurringAc,
    GetRuleGroupsAc,
    GetRulesAc,
    GetTagAc,
    GetTransactionTypesAc,
    GetTransactionsAc,
    GetTransactionsIdac,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
