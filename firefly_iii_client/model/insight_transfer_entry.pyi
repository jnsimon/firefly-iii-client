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


class InsightTransferEntry(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            currency_code = schemas.StrSchema
            currency_id = schemas.StrSchema
            difference = schemas.StrSchema
            difference_float = schemas.Float64Schema
            id = schemas.StrSchema
            _in = schemas.StrSchema
            in_float = schemas.Float64Schema
            name = schemas.StrSchema
            out = schemas.StrSchema
            out_float = schemas.Float64Schema
            __annotations__ = {
                "currency_code": currency_code,
                "currency_id": currency_id,
                "difference": difference,
                "difference_float": difference_float,
                "id": id,
                "in": _in,
                "in_float": in_float,
                "name": name,
                "out": out,
                "out_float": out_float,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_code"]) -> MetaOapg.properties.currency_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_id"]) -> MetaOapg.properties.currency_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["difference"]) -> MetaOapg.properties.difference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["difference_float"]) -> MetaOapg.properties.difference_float: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["in"]) -> MetaOapg.properties._in: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["in_float"]) -> MetaOapg.properties.in_float: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["out"]) -> MetaOapg.properties.out: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["out_float"]) -> MetaOapg.properties.out_float: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["currency_code", "currency_id", "difference", "difference_float", "id", "in", "in_float", "name", "out", "out_float", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_code"]) -> typing.Union[MetaOapg.properties.currency_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_id"]) -> typing.Union[MetaOapg.properties.currency_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["difference"]) -> typing.Union[MetaOapg.properties.difference, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["difference_float"]) -> typing.Union[MetaOapg.properties.difference_float, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["in"]) -> typing.Union[MetaOapg.properties._in, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["in_float"]) -> typing.Union[MetaOapg.properties.in_float, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["out"]) -> typing.Union[MetaOapg.properties.out, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["out_float"]) -> typing.Union[MetaOapg.properties.out_float, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["currency_code", "currency_id", "difference", "difference_float", "id", "in", "in_float", "name", "out", "out_float", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        currency_code: typing.Union[MetaOapg.properties.currency_code, str, schemas.Unset] = schemas.unset,
        currency_id: typing.Union[MetaOapg.properties.currency_id, str, schemas.Unset] = schemas.unset,
        difference: typing.Union[MetaOapg.properties.difference, str, schemas.Unset] = schemas.unset,
        difference_float: typing.Union[MetaOapg.properties.difference_float, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        in_float: typing.Union[MetaOapg.properties.in_float, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        out: typing.Union[MetaOapg.properties.out, str, schemas.Unset] = schemas.unset,
        out_float: typing.Union[MetaOapg.properties.out_float, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InsightTransferEntry':
        return super().__new__(
            cls,
            *_args,
            currency_code=currency_code,
            currency_id=currency_id,
            difference=difference,
            difference_float=difference_float,
            id=id,
            in_float=in_float,
            name=name,
            out=out,
            out_float=out_float,
            _configuration=_configuration,
            **kwargs,
        )