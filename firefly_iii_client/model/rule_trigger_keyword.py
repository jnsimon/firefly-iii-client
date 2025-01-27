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


class RuleTriggerKeyword(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The type of thing this trigger responds to. A limited set is possible
    """


    class MetaOapg:
        format = 'string'
        enum_value_to_name = {
            "from_account_starts": "FROM_ACCOUNT_STARTS",
            "from_account_ends": "FROM_ACCOUNT_ENDS",
            "from_account_is": "FROM_ACCOUNT_IS",
            "from_account_contains": "FROM_ACCOUNT_CONTAINS",
            "to_account_starts": "TO_ACCOUNT_STARTS",
            "to_account_ends": "TO_ACCOUNT_ENDS",
            "to_account_is": "TO_ACCOUNT_IS",
            "to_account_contains": "TO_ACCOUNT_CONTAINS",
            "amount_less": "AMOUNT_LESS",
            "amount_exactly": "AMOUNT_EXACTLY",
            "amount_more": "AMOUNT_MORE",
            "description_starts": "DESCRIPTION_STARTS",
            "description_ends": "DESCRIPTION_ENDS",
            "description_contains": "DESCRIPTION_CONTAINS",
            "description_is": "DESCRIPTION_IS",
            "transaction_type": "TRANSACTION_TYPE",
            "category_is": "CATEGORY_IS",
            "budget_is": "BUDGET_IS",
            "tag_is": "TAG_IS",
            "currency_is": "CURRENCY_IS",
            "has_attachments": "HAS_ATTACHMENTS",
            "has_no_category": "HAS_NO_CATEGORY",
            "has_any_category": "HAS_ANY_CATEGORY",
            "has_no_budget": "HAS_NO_BUDGET",
            "has_any_budget": "HAS_ANY_BUDGET",
            "has_no_tag": "HAS_NO_TAG",
            "has_any_tag": "HAS_ANY_TAG",
            "notes_contains": "NOTES_CONTAINS",
            "notes_start": "NOTES_START",
            "notes_end": "NOTES_END",
            "notes_are": "NOTES_ARE",
            "no_notes": "NO_NOTES",
            "any_notes": "ANY_NOTES",
            "source_account_is": "SOURCE_ACCOUNT_IS",
            "destination_account_is": "DESTINATION_ACCOUNT_IS",
            "source_account_starts": "SOURCE_ACCOUNT_STARTS",
        }
    
    @schemas.classproperty
    def FROM_ACCOUNT_STARTS(cls):
        return cls("from_account_starts")
    
    @schemas.classproperty
    def FROM_ACCOUNT_ENDS(cls):
        return cls("from_account_ends")
    
    @schemas.classproperty
    def FROM_ACCOUNT_IS(cls):
        return cls("from_account_is")
    
    @schemas.classproperty
    def FROM_ACCOUNT_CONTAINS(cls):
        return cls("from_account_contains")
    
    @schemas.classproperty
    def TO_ACCOUNT_STARTS(cls):
        return cls("to_account_starts")
    
    @schemas.classproperty
    def TO_ACCOUNT_ENDS(cls):
        return cls("to_account_ends")
    
    @schemas.classproperty
    def TO_ACCOUNT_IS(cls):
        return cls("to_account_is")
    
    @schemas.classproperty
    def TO_ACCOUNT_CONTAINS(cls):
        return cls("to_account_contains")
    
    @schemas.classproperty
    def AMOUNT_LESS(cls):
        return cls("amount_less")
    
    @schemas.classproperty
    def AMOUNT_EXACTLY(cls):
        return cls("amount_exactly")
    
    @schemas.classproperty
    def AMOUNT_MORE(cls):
        return cls("amount_more")
    
    @schemas.classproperty
    def DESCRIPTION_STARTS(cls):
        return cls("description_starts")
    
    @schemas.classproperty
    def DESCRIPTION_ENDS(cls):
        return cls("description_ends")
    
    @schemas.classproperty
    def DESCRIPTION_CONTAINS(cls):
        return cls("description_contains")
    
    @schemas.classproperty
    def DESCRIPTION_IS(cls):
        return cls("description_is")
    
    @schemas.classproperty
    def TRANSACTION_TYPE(cls):
        return cls("transaction_type")
    
    @schemas.classproperty
    def CATEGORY_IS(cls):
        return cls("category_is")
    
    @schemas.classproperty
    def BUDGET_IS(cls):
        return cls("budget_is")
    
    @schemas.classproperty
    def TAG_IS(cls):
        return cls("tag_is")
    
    @schemas.classproperty
    def CURRENCY_IS(cls):
        return cls("currency_is")
    
    @schemas.classproperty
    def HAS_ATTACHMENTS(cls):
        return cls("has_attachments")
    
    @schemas.classproperty
    def HAS_NO_CATEGORY(cls):
        return cls("has_no_category")
    
    @schemas.classproperty
    def HAS_ANY_CATEGORY(cls):
        return cls("has_any_category")
    
    @schemas.classproperty
    def HAS_NO_BUDGET(cls):
        return cls("has_no_budget")
    
    @schemas.classproperty
    def HAS_ANY_BUDGET(cls):
        return cls("has_any_budget")
    
    @schemas.classproperty
    def HAS_NO_TAG(cls):
        return cls("has_no_tag")
    
    @schemas.classproperty
    def HAS_ANY_TAG(cls):
        return cls("has_any_tag")
    
    @schemas.classproperty
    def NOTES_CONTAINS(cls):
        return cls("notes_contains")
    
    @schemas.classproperty
    def NOTES_START(cls):
        return cls("notes_start")
    
    @schemas.classproperty
    def NOTES_END(cls):
        return cls("notes_end")
    
    @schemas.classproperty
    def NOTES_ARE(cls):
        return cls("notes_are")
    
    @schemas.classproperty
    def NO_NOTES(cls):
        return cls("no_notes")
    
    @schemas.classproperty
    def ANY_NOTES(cls):
        return cls("any_notes")
    
    @schemas.classproperty
    def SOURCE_ACCOUNT_IS(cls):
        return cls("source_account_is")
    
    @schemas.classproperty
    def DESTINATION_ACCOUNT_IS(cls):
        return cls("destination_account_is")
    
    @schemas.classproperty
    def SOURCE_ACCOUNT_STARTS(cls):
        return cls("source_account_starts")
