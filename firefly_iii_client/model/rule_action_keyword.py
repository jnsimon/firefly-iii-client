# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 2.0.12
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from firefly_iii_client import schemas  # noqa: F401


class RuleActionKeyword(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The type of thing this action will do. A limited set is possible.
    """


    class MetaOapg:
        format = 'string'
        enum_value_to_name = {
            "user_action": "USER_ACTION",
            "set_category": "SET_CATEGORY",
            "clear_category": "CLEAR_CATEGORY",
            "set_budget": "SET_BUDGET",
            "clear_budget": "CLEAR_BUDGET",
            "add_tag": "ADD_TAG",
            "remove_tag": "REMOVE_TAG",
            "remove_all_tags": "REMOVE_ALL_TAGS",
            "set_description": "SET_DESCRIPTION",
            "append_description": "APPEND_DESCRIPTION",
            "prepend_description": "PREPEND_DESCRIPTION",
            "set_source_account": "SET_SOURCE_ACCOUNT",
            "set_destination_account": "SET_DESTINATION_ACCOUNT",
            "set_notes": "SET_NOTES",
            "append_notes": "APPEND_NOTES",
            "prepend_notes": "PREPEND_NOTES",
            "clear_notes": "CLEAR_NOTES",
            "link_to_bill": "LINK_TO_BILL",
            "convert_withdrawal": "CONVERT_WITHDRAWAL",
            "convert_deposit": "CONVERT_DEPOSIT",
            "convert_transfer": "CONVERT_TRANSFER",
            "delete_transaction": "DELETE_TRANSACTION",
        }
    
    @schemas.classproperty
    def USER_ACTION(cls):
        return cls("user_action")
    
    @schemas.classproperty
    def SET_CATEGORY(cls):
        return cls("set_category")
    
    @schemas.classproperty
    def CLEAR_CATEGORY(cls):
        return cls("clear_category")
    
    @schemas.classproperty
    def SET_BUDGET(cls):
        return cls("set_budget")
    
    @schemas.classproperty
    def CLEAR_BUDGET(cls):
        return cls("clear_budget")
    
    @schemas.classproperty
    def ADD_TAG(cls):
        return cls("add_tag")
    
    @schemas.classproperty
    def REMOVE_TAG(cls):
        return cls("remove_tag")
    
    @schemas.classproperty
    def REMOVE_ALL_TAGS(cls):
        return cls("remove_all_tags")
    
    @schemas.classproperty
    def SET_DESCRIPTION(cls):
        return cls("set_description")
    
    @schemas.classproperty
    def APPEND_DESCRIPTION(cls):
        return cls("append_description")
    
    @schemas.classproperty
    def PREPEND_DESCRIPTION(cls):
        return cls("prepend_description")
    
    @schemas.classproperty
    def SET_SOURCE_ACCOUNT(cls):
        return cls("set_source_account")
    
    @schemas.classproperty
    def SET_DESTINATION_ACCOUNT(cls):
        return cls("set_destination_account")
    
    @schemas.classproperty
    def SET_NOTES(cls):
        return cls("set_notes")
    
    @schemas.classproperty
    def APPEND_NOTES(cls):
        return cls("append_notes")
    
    @schemas.classproperty
    def PREPEND_NOTES(cls):
        return cls("prepend_notes")
    
    @schemas.classproperty
    def CLEAR_NOTES(cls):
        return cls("clear_notes")
    
    @schemas.classproperty
    def LINK_TO_BILL(cls):
        return cls("link_to_bill")
    
    @schemas.classproperty
    def CONVERT_WITHDRAWAL(cls):
        return cls("convert_withdrawal")
    
    @schemas.classproperty
    def CONVERT_DEPOSIT(cls):
        return cls("convert_deposit")
    
    @schemas.classproperty
    def CONVERT_TRANSFER(cls):
        return cls("convert_transfer")
    
    @schemas.classproperty
    def DELETE_TRANSACTION(cls):
        return cls("delete_transaction")
