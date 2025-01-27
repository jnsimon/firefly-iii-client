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


class TransactionLinkUpdate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            inward_id = schemas.StrSchema
            link_type_id = schemas.StrSchema
            link_type_name = schemas.StrSchema
            
            
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
            outward_id = schemas.StrSchema
            __annotations__ = {
                "inward_id": inward_id,
                "link_type_id": link_type_id,
                "link_type_name": link_type_name,
                "notes": notes,
                "outward_id": outward_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inward_id"]) -> MetaOapg.properties.inward_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link_type_id"]) -> MetaOapg.properties.link_type_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link_type_name"]) -> MetaOapg.properties.link_type_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["outward_id"]) -> MetaOapg.properties.outward_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["inward_id", "link_type_id", "link_type_name", "notes", "outward_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inward_id"]) -> typing.Union[MetaOapg.properties.inward_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link_type_id"]) -> typing.Union[MetaOapg.properties.link_type_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link_type_name"]) -> typing.Union[MetaOapg.properties.link_type_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["outward_id"]) -> typing.Union[MetaOapg.properties.outward_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["inward_id", "link_type_id", "link_type_name", "notes", "outward_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        inward_id: typing.Union[MetaOapg.properties.inward_id, str, schemas.Unset] = schemas.unset,
        link_type_id: typing.Union[MetaOapg.properties.link_type_id, str, schemas.Unset] = schemas.unset,
        link_type_name: typing.Union[MetaOapg.properties.link_type_name, str, schemas.Unset] = schemas.unset,
        notes: typing.Union[MetaOapg.properties.notes, None, str, schemas.Unset] = schemas.unset,
        outward_id: typing.Union[MetaOapg.properties.outward_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TransactionLinkUpdate':
        return super().__new__(
            cls,
            *_args,
            inward_id=inward_id,
            link_type_id=link_type_id,
            link_type_name=link_type_name,
            notes=notes,
            outward_id=outward_id,
            _configuration=_configuration,
            **kwargs,
        )
