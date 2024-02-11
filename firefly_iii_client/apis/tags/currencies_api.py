# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 2.0.12
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""

from firefly_iii_client.paths.v1_currencies_code_default.post import DefaultCurrency
from firefly_iii_client.paths.v1_currencies_code.delete import DeleteCurrency
from firefly_iii_client.paths.v1_currencies_code_disable.post import DisableCurrency
from firefly_iii_client.paths.v1_currencies_code_enable.post import EnableCurrency
from firefly_iii_client.paths.v1_currencies_code.get import GetCurrency
from firefly_iii_client.paths.v1_currencies_default.get import GetDefaultCurrency
from firefly_iii_client.paths.v1_currencies_code_accounts.get import ListAccountByCurrency
from firefly_iii_client.paths.v1_currencies_code_available_budgets.get import ListAvailableBudgetByCurrency
from firefly_iii_client.paths.v1_currencies_code_bills.get import ListBillByCurrency
from firefly_iii_client.paths.v1_currencies_code_budget_limits.get import ListBudgetLimitByCurrency
from firefly_iii_client.paths.v1_currencies.get import ListCurrency
from firefly_iii_client.paths.v1_currencies_code_recurrences.get import ListRecurrenceByCurrency
from firefly_iii_client.paths.v1_currencies_code_rules.get import ListRuleByCurrency
from firefly_iii_client.paths.v1_currencies_code_transactions.get import ListTransactionByCurrency
from firefly_iii_client.paths.v1_currencies.post import StoreCurrency
from firefly_iii_client.paths.v1_currencies_code.put import UpdateCurrency


class CurrenciesApi(
    DefaultCurrency,
    DeleteCurrency,
    DisableCurrency,
    EnableCurrency,
    GetCurrency,
    GetDefaultCurrency,
    ListAccountByCurrency,
    ListAvailableBudgetByCurrency,
    ListBillByCurrency,
    ListBudgetLimitByCurrency,
    ListCurrency,
    ListRecurrenceByCurrency,
    ListRuleByCurrency,
    ListTransactionByCurrency,
    StoreCurrency,
    UpdateCurrency,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
