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


class AttachmentStore(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "filename",
            "attachable_id",
            "attachable_type",
        }
        
        class properties:
            attachable_id = schemas.StrSchema
        
            @staticmethod
            def attachable_type() -> typing.Type['AttachableType']:
                return AttachableType
            filename = schemas.StrSchema
            
            
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
            title = schemas.StrSchema
            __annotations__ = {
                "attachable_id": attachable_id,
                "attachable_type": attachable_type,
                "filename": filename,
                "notes": notes,
                "title": title,
            }
    
    filename: MetaOapg.properties.filename
    attachable_id: MetaOapg.properties.attachable_id
    attachable_type: 'AttachableType'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachable_id"]) -> MetaOapg.properties.attachable_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachable_type"]) -> 'AttachableType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filename"]) -> MetaOapg.properties.filename: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["attachable_id", "attachable_type", "filename", "notes", "title", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachable_id"]) -> MetaOapg.properties.attachable_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachable_type"]) -> 'AttachableType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filename"]) -> MetaOapg.properties.filename: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["attachable_id", "attachable_type", "filename", "notes", "title", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        filename: typing.Union[MetaOapg.properties.filename, str, ],
        attachable_id: typing.Union[MetaOapg.properties.attachable_id, str, ],
        attachable_type: 'AttachableType',
        notes: typing.Union[MetaOapg.properties.notes, None, str, schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AttachmentStore':
        return super().__new__(
            cls,
            *_args,
            filename=filename,
            attachable_id=attachable_id,
            attachable_type=attachable_type,
            notes=notes,
            title=title,
            _configuration=_configuration,
            **kwargs,
        )

from firefly_iii_client.model.attachable_type import AttachableType
