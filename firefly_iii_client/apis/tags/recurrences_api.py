# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 2.0.12
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""

from firefly_iii_client.paths.v1_recurrences_id.delete import DeleteRecurrence
from firefly_iii_client.paths.v1_recurrences_id.get import GetRecurrence
from firefly_iii_client.paths.v1_recurrences.get import ListRecurrence
from firefly_iii_client.paths.v1_recurrences_id_transactions.get import ListTransactionByRecurrence
from firefly_iii_client.paths.v1_recurrences.post import StoreRecurrence
from firefly_iii_client.paths.v1_recurrences_id.put import UpdateRecurrence


class RecurrencesApi(
    DeleteRecurrence,
    GetRecurrence,
    ListRecurrence,
    ListTransactionByRecurrence,
    StoreRecurrence,
    UpdateRecurrence,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
