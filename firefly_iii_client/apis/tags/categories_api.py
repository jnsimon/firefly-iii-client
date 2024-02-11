# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 2.0.12
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""

from firefly_iii_client.paths.v1_categories_id.delete import DeleteCategory
from firefly_iii_client.paths.v1_categories_id.get import GetCategory
from firefly_iii_client.paths.v1_categories_id_attachments.get import ListAttachmentByCategory
from firefly_iii_client.paths.v1_categories.get import ListCategory
from firefly_iii_client.paths.v1_categories_id_transactions.get import ListTransactionByCategory
from firefly_iii_client.paths.v1_categories.post import StoreCategory
from firefly_iii_client.paths.v1_categories_id.put import UpdateCategory


class CategoriesApi(
    DeleteCategory,
    GetCategory,
    ListAttachmentByCategory,
    ListCategory,
    ListTransactionByCategory,
    StoreCategory,
    UpdateCategory,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
