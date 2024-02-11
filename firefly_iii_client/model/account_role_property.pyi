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


class AccountRoleProperty(
    schemas.EnumBase,
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Is only mandatory when the type is asset.
    """


    class MetaOapg:
        format = 'string'
        enum_value_to_name = {
            "defaultAsset": "DEFAULT_ASSET",
            "sharedAsset": "SHARED_ASSET",
            "savingAsset": "SAVING_ASSET",
            "ccAsset": "CC_ASSET",
            "cashWalletAsset": "CASH_WALLET_ASSET",
            "null": "NONE",
        }
    
    @schemas.classproperty
    def DEFAULT_ASSET(cls):
        return cls("defaultAsset")
    
    @schemas.classproperty
    def SHARED_ASSET(cls):
        return cls("sharedAsset")
    
    @schemas.classproperty
    def SAVING_ASSET(cls):
        return cls("savingAsset")
    
    @schemas.classproperty
    def CC_ASSET(cls):
        return cls("ccAsset")
    
    @schemas.classproperty
    def CASH_WALLET_ASSET(cls):
        return cls("cashWalletAsset")
    
    @schemas.classproperty
    def NONE(cls):
        return cls("null")


    def __new__(
        cls,
        *_args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AccountRoleProperty':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
        )