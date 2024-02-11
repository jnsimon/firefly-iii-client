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


class PiggyBankEvent(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            amount = schemas.StrSchema
            created_at = schemas.DateTimeSchema
            currency_code = schemas.StrSchema
            currency_decimal_places = schemas.Int32Schema
            currency_id = schemas.StrSchema
            currency_symbol = schemas.StrSchema
            
            
            class transaction_group_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'string'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'transaction_group_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class transaction_journal_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'string'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'transaction_journal_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            updated_at = schemas.DateTimeSchema
            __annotations__ = {
                "amount": amount,
                "created_at": created_at,
                "currency_code": currency_code,
                "currency_decimal_places": currency_decimal_places,
                "currency_id": currency_id,
                "currency_symbol": currency_symbol,
                "transaction_group_id": transaction_group_id,
                "transaction_journal_id": transaction_journal_id,
                "updated_at": updated_at,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_code"]) -> MetaOapg.properties.currency_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_decimal_places"]) -> MetaOapg.properties.currency_decimal_places: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_id"]) -> MetaOapg.properties.currency_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_symbol"]) -> MetaOapg.properties.currency_symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_group_id"]) -> MetaOapg.properties.transaction_group_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_journal_id"]) -> MetaOapg.properties.transaction_journal_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount", "created_at", "currency_code", "currency_decimal_places", "currency_id", "currency_symbol", "transaction_group_id", "transaction_journal_id", "updated_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_code"]) -> typing.Union[MetaOapg.properties.currency_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_decimal_places"]) -> typing.Union[MetaOapg.properties.currency_decimal_places, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_id"]) -> typing.Union[MetaOapg.properties.currency_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_symbol"]) -> typing.Union[MetaOapg.properties.currency_symbol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_group_id"]) -> typing.Union[MetaOapg.properties.transaction_group_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_journal_id"]) -> typing.Union[MetaOapg.properties.transaction_journal_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount", "created_at", "currency_code", "currency_decimal_places", "currency_id", "currency_symbol", "transaction_group_id", "transaction_journal_id", "updated_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, str, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        currency_code: typing.Union[MetaOapg.properties.currency_code, str, schemas.Unset] = schemas.unset,
        currency_decimal_places: typing.Union[MetaOapg.properties.currency_decimal_places, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        currency_id: typing.Union[MetaOapg.properties.currency_id, str, schemas.Unset] = schemas.unset,
        currency_symbol: typing.Union[MetaOapg.properties.currency_symbol, str, schemas.Unset] = schemas.unset,
        transaction_group_id: typing.Union[MetaOapg.properties.transaction_group_id, None, str, schemas.Unset] = schemas.unset,
        transaction_journal_id: typing.Union[MetaOapg.properties.transaction_journal_id, None, str, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PiggyBankEvent':
        return super().__new__(
            cls,
            *_args,
            amount=amount,
            created_at=created_at,
            currency_code=currency_code,
            currency_decimal_places=currency_decimal_places,
            currency_id=currency_id,
            currency_symbol=currency_symbol,
            transaction_group_id=transaction_group_id,
            transaction_journal_id=transaction_journal_id,
            updated_at=updated_at,
            _configuration=_configuration,
            **kwargs,
        )
