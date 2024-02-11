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


class Bill(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "date",
            "name",
            "amount_max",
            "amount_min",
            "repeat_freq",
        }
        
        class properties:
            amount_max = schemas.StrSchema
            amount_min = schemas.StrSchema
            date = schemas.DateTimeSchema
            name = schemas.StrSchema
        
            @staticmethod
            def repeat_freq() -> typing.Type['BillRepeatFrequency']:
                return BillRepeatFrequency
            active = schemas.BoolSchema
            created_at = schemas.DateTimeSchema
            currency_code = schemas.StrSchema
            currency_decimal_places = schemas.Int32Schema
            currency_id = schemas.StrSchema
            currency_symbol = schemas.StrSchema
            
            
            class end_date(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'end_date':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class extension_date(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'extension_date':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class next_expected_match(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'next_expected_match':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class next_expected_match_diff(
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
                ) -> 'next_expected_match_diff':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class notes(
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
                ) -> 'notes':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class object_group_id(
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
                ) -> 'object_group_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class object_group_order(
                schemas.Int32Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int32'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'object_group_order':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class object_group_title(
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
                ) -> 'object_group_title':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            order = schemas.Int32Schema
            
            
            class paid_dates(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                date = schemas.DateTimeSchema
                                transaction_group_id = schemas.StrSchema
                                transaction_journal_id = schemas.StrSchema
                                __annotations__ = {
                                    "date": date,
                                    "transaction_group_id": transaction_group_id,
                                    "transaction_journal_id": transaction_journal_id,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["transaction_group_id"]) -> MetaOapg.properties.transaction_group_id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["transaction_journal_id"]) -> MetaOapg.properties.transaction_journal_id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["date", "transaction_group_id", "transaction_journal_id", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> typing.Union[MetaOapg.properties.date, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["transaction_group_id"]) -> typing.Union[MetaOapg.properties.transaction_group_id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["transaction_journal_id"]) -> typing.Union[MetaOapg.properties.transaction_journal_id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["date", "transaction_group_id", "transaction_journal_id", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            date: typing.Union[MetaOapg.properties.date, str, datetime, schemas.Unset] = schemas.unset,
                            transaction_group_id: typing.Union[MetaOapg.properties.transaction_group_id, str, schemas.Unset] = schemas.unset,
                            transaction_journal_id: typing.Union[MetaOapg.properties.transaction_journal_id, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                date=date,
                                transaction_group_id=transaction_group_id,
                                transaction_journal_id=transaction_journal_id,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'paid_dates':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class pay_dates(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.DateTimeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, datetime, ]], typing.List[typing.Union[MetaOapg.items, str, datetime, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'pay_dates':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            skip = schemas.Int32Schema
            updated_at = schemas.DateTimeSchema
            __annotations__ = {
                "amount_max": amount_max,
                "amount_min": amount_min,
                "date": date,
                "name": name,
                "repeat_freq": repeat_freq,
                "active": active,
                "created_at": created_at,
                "currency_code": currency_code,
                "currency_decimal_places": currency_decimal_places,
                "currency_id": currency_id,
                "currency_symbol": currency_symbol,
                "end_date": end_date,
                "extension_date": extension_date,
                "next_expected_match": next_expected_match,
                "next_expected_match_diff": next_expected_match_diff,
                "notes": notes,
                "object_group_id": object_group_id,
                "object_group_order": object_group_order,
                "object_group_title": object_group_title,
                "order": order,
                "paid_dates": paid_dates,
                "pay_dates": pay_dates,
                "skip": skip,
                "updated_at": updated_at,
            }
    
    date: MetaOapg.properties.date
    name: MetaOapg.properties.name
    amount_max: MetaOapg.properties.amount_max
    amount_min: MetaOapg.properties.amount_min
    repeat_freq: 'BillRepeatFrequency'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount_max"]) -> MetaOapg.properties.amount_max: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount_min"]) -> MetaOapg.properties.amount_min: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["repeat_freq"]) -> 'BillRepeatFrequency': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
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
    def __getitem__(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extension_date"]) -> MetaOapg.properties.extension_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next_expected_match"]) -> MetaOapg.properties.next_expected_match: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next_expected_match_diff"]) -> MetaOapg.properties.next_expected_match_diff: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object_group_id"]) -> MetaOapg.properties.object_group_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object_group_order"]) -> MetaOapg.properties.object_group_order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object_group_title"]) -> MetaOapg.properties.object_group_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paid_dates"]) -> MetaOapg.properties.paid_dates: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pay_dates"]) -> MetaOapg.properties.pay_dates: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["skip"]) -> MetaOapg.properties.skip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount_max", "amount_min", "date", "name", "repeat_freq", "active", "created_at", "currency_code", "currency_decimal_places", "currency_id", "currency_symbol", "end_date", "extension_date", "next_expected_match", "next_expected_match_diff", "notes", "object_group_id", "object_group_order", "object_group_title", "order", "paid_dates", "pay_dates", "skip", "updated_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount_max"]) -> MetaOapg.properties.amount_max: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount_min"]) -> MetaOapg.properties.amount_min: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["repeat_freq"]) -> 'BillRepeatFrequency': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union[MetaOapg.properties.active, schemas.Unset]: ...
    
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
    def get_item_oapg(self, name: typing_extensions.Literal["end_date"]) -> typing.Union[MetaOapg.properties.end_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extension_date"]) -> typing.Union[MetaOapg.properties.extension_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next_expected_match"]) -> typing.Union[MetaOapg.properties.next_expected_match, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next_expected_match_diff"]) -> typing.Union[MetaOapg.properties.next_expected_match_diff, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object_group_id"]) -> typing.Union[MetaOapg.properties.object_group_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object_group_order"]) -> typing.Union[MetaOapg.properties.object_group_order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object_group_title"]) -> typing.Union[MetaOapg.properties.object_group_title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> typing.Union[MetaOapg.properties.order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paid_dates"]) -> typing.Union[MetaOapg.properties.paid_dates, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pay_dates"]) -> typing.Union[MetaOapg.properties.pay_dates, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["skip"]) -> typing.Union[MetaOapg.properties.skip, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount_max", "amount_min", "date", "name", "repeat_freq", "active", "created_at", "currency_code", "currency_decimal_places", "currency_id", "currency_symbol", "end_date", "extension_date", "next_expected_match", "next_expected_match_diff", "notes", "object_group_id", "object_group_order", "object_group_title", "order", "paid_dates", "pay_dates", "skip", "updated_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        date: typing.Union[MetaOapg.properties.date, str, datetime, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        amount_max: typing.Union[MetaOapg.properties.amount_max, str, ],
        amount_min: typing.Union[MetaOapg.properties.amount_min, str, ],
        repeat_freq: 'BillRepeatFrequency',
        active: typing.Union[MetaOapg.properties.active, bool, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        currency_code: typing.Union[MetaOapg.properties.currency_code, str, schemas.Unset] = schemas.unset,
        currency_decimal_places: typing.Union[MetaOapg.properties.currency_decimal_places, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        currency_id: typing.Union[MetaOapg.properties.currency_id, str, schemas.Unset] = schemas.unset,
        currency_symbol: typing.Union[MetaOapg.properties.currency_symbol, str, schemas.Unset] = schemas.unset,
        end_date: typing.Union[MetaOapg.properties.end_date, None, str, datetime, schemas.Unset] = schemas.unset,
        extension_date: typing.Union[MetaOapg.properties.extension_date, None, str, datetime, schemas.Unset] = schemas.unset,
        next_expected_match: typing.Union[MetaOapg.properties.next_expected_match, None, str, datetime, schemas.Unset] = schemas.unset,
        next_expected_match_diff: typing.Union[MetaOapg.properties.next_expected_match_diff, None, str, schemas.Unset] = schemas.unset,
        notes: typing.Union[MetaOapg.properties.notes, None, str, schemas.Unset] = schemas.unset,
        object_group_id: typing.Union[MetaOapg.properties.object_group_id, None, str, schemas.Unset] = schemas.unset,
        object_group_order: typing.Union[MetaOapg.properties.object_group_order, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        object_group_title: typing.Union[MetaOapg.properties.object_group_title, None, str, schemas.Unset] = schemas.unset,
        order: typing.Union[MetaOapg.properties.order, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        paid_dates: typing.Union[MetaOapg.properties.paid_dates, list, tuple, schemas.Unset] = schemas.unset,
        pay_dates: typing.Union[MetaOapg.properties.pay_dates, list, tuple, schemas.Unset] = schemas.unset,
        skip: typing.Union[MetaOapg.properties.skip, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Bill':
        return super().__new__(
            cls,
            *_args,
            date=date,
            name=name,
            amount_max=amount_max,
            amount_min=amount_min,
            repeat_freq=repeat_freq,
            active=active,
            created_at=created_at,
            currency_code=currency_code,
            currency_decimal_places=currency_decimal_places,
            currency_id=currency_id,
            currency_symbol=currency_symbol,
            end_date=end_date,
            extension_date=extension_date,
            next_expected_match=next_expected_match,
            next_expected_match_diff=next_expected_match_diff,
            notes=notes,
            object_group_id=object_group_id,
            object_group_order=object_group_order,
            object_group_title=object_group_title,
            order=order,
            paid_dates=paid_dates,
            pay_dates=pay_dates,
            skip=skip,
            updated_at=updated_at,
            _configuration=_configuration,
            **kwargs,
        )

from firefly_iii_client.model.bill_repeat_frequency import BillRepeatFrequency
