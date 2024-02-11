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


class BillStore(
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
            currency_code = schemas.StrSchema
            currency_id = schemas.StrSchema
            end_date = schemas.DateTimeSchema
            extension_date = schemas.DateTimeSchema
            
            
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
            skip = schemas.Int32Schema
            __annotations__ = {
                "amount_max": amount_max,
                "amount_min": amount_min,
                "date": date,
                "name": name,
                "repeat_freq": repeat_freq,
                "active": active,
                "currency_code": currency_code,
                "currency_id": currency_id,
                "end_date": end_date,
                "extension_date": extension_date,
                "notes": notes,
                "object_group_id": object_group_id,
                "object_group_title": object_group_title,
                "skip": skip,
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
    def __getitem__(self, name: typing_extensions.Literal["currency_code"]) -> MetaOapg.properties.currency_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_id"]) -> MetaOapg.properties.currency_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extension_date"]) -> MetaOapg.properties.extension_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object_group_id"]) -> MetaOapg.properties.object_group_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object_group_title"]) -> MetaOapg.properties.object_group_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["skip"]) -> MetaOapg.properties.skip: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount_max", "amount_min", "date", "name", "repeat_freq", "active", "currency_code", "currency_id", "end_date", "extension_date", "notes", "object_group_id", "object_group_title", "skip", ], str]):
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
    def get_item_oapg(self, name: typing_extensions.Literal["currency_code"]) -> typing.Union[MetaOapg.properties.currency_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_id"]) -> typing.Union[MetaOapg.properties.currency_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_date"]) -> typing.Union[MetaOapg.properties.end_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extension_date"]) -> typing.Union[MetaOapg.properties.extension_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object_group_id"]) -> typing.Union[MetaOapg.properties.object_group_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object_group_title"]) -> typing.Union[MetaOapg.properties.object_group_title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["skip"]) -> typing.Union[MetaOapg.properties.skip, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount_max", "amount_min", "date", "name", "repeat_freq", "active", "currency_code", "currency_id", "end_date", "extension_date", "notes", "object_group_id", "object_group_title", "skip", ], str]):
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
        currency_code: typing.Union[MetaOapg.properties.currency_code, str, schemas.Unset] = schemas.unset,
        currency_id: typing.Union[MetaOapg.properties.currency_id, str, schemas.Unset] = schemas.unset,
        end_date: typing.Union[MetaOapg.properties.end_date, str, datetime, schemas.Unset] = schemas.unset,
        extension_date: typing.Union[MetaOapg.properties.extension_date, str, datetime, schemas.Unset] = schemas.unset,
        notes: typing.Union[MetaOapg.properties.notes, None, str, schemas.Unset] = schemas.unset,
        object_group_id: typing.Union[MetaOapg.properties.object_group_id, None, str, schemas.Unset] = schemas.unset,
        object_group_title: typing.Union[MetaOapg.properties.object_group_title, None, str, schemas.Unset] = schemas.unset,
        skip: typing.Union[MetaOapg.properties.skip, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BillStore':
        return super().__new__(
            cls,
            *_args,
            date=date,
            name=name,
            amount_max=amount_max,
            amount_min=amount_min,
            repeat_freq=repeat_freq,
            active=active,
            currency_code=currency_code,
            currency_id=currency_id,
            end_date=end_date,
            extension_date=extension_date,
            notes=notes,
            object_group_id=object_group_id,
            object_group_title=object_group_title,
            skip=skip,
            _configuration=_configuration,
            **kwargs,
        )

from firefly_iii_client.model.bill_repeat_frequency import BillRepeatFrequency