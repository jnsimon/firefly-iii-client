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


class AutocompleteCurrencyArray(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['AutocompleteCurrency']:
            return AutocompleteCurrency

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['AutocompleteCurrency'], typing.List['AutocompleteCurrency']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AutocompleteCurrencyArray':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'AutocompleteCurrency':
        return super().__getitem__(i)

from firefly_iii_client.model.autocomplete_currency import AutocompleteCurrency
