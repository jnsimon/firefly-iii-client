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


class RuleStore(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "trigger",
            "rule_group_id",
            "title",
            "triggers",
            "actions",
        }
        
        class properties:
            
            
            class actions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['RuleActionStore']:
                        return RuleActionStore
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['RuleActionStore'], typing.List['RuleActionStore']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'actions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'RuleActionStore':
                    return super().__getitem__(i)
            rule_group_id = schemas.StrSchema
            title = schemas.StrSchema
        
            @staticmethod
            def trigger() -> typing.Type['RuleTriggerType']:
                return RuleTriggerType
            
            
            class triggers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['RuleTriggerStore']:
                        return RuleTriggerStore
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['RuleTriggerStore'], typing.List['RuleTriggerStore']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'triggers':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'RuleTriggerStore':
                    return super().__getitem__(i)
            active = schemas.BoolSchema
            description = schemas.StrSchema
            order = schemas.Int32Schema
            rule_group_title = schemas.StrSchema
            stop_processing = schemas.BoolSchema
            strict = schemas.BoolSchema
            __annotations__ = {
                "actions": actions,
                "rule_group_id": rule_group_id,
                "title": title,
                "trigger": trigger,
                "triggers": triggers,
                "active": active,
                "description": description,
                "order": order,
                "rule_group_title": rule_group_title,
                "stop_processing": stop_processing,
                "strict": strict,
            }
    
    trigger: 'RuleTriggerType'
    rule_group_id: MetaOapg.properties.rule_group_id
    title: MetaOapg.properties.title
    triggers: MetaOapg.properties.triggers
    actions: MetaOapg.properties.actions
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actions"]) -> MetaOapg.properties.actions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rule_group_id"]) -> MetaOapg.properties.rule_group_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trigger"]) -> 'RuleTriggerType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["triggers"]) -> MetaOapg.properties.triggers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rule_group_title"]) -> MetaOapg.properties.rule_group_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stop_processing"]) -> MetaOapg.properties.stop_processing: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["strict"]) -> MetaOapg.properties.strict: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["actions", "rule_group_id", "title", "trigger", "triggers", "active", "description", "order", "rule_group_title", "stop_processing", "strict", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actions"]) -> MetaOapg.properties.actions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rule_group_id"]) -> MetaOapg.properties.rule_group_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trigger"]) -> 'RuleTriggerType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["triggers"]) -> MetaOapg.properties.triggers: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union[MetaOapg.properties.active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> typing.Union[MetaOapg.properties.order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rule_group_title"]) -> typing.Union[MetaOapg.properties.rule_group_title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stop_processing"]) -> typing.Union[MetaOapg.properties.stop_processing, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["strict"]) -> typing.Union[MetaOapg.properties.strict, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["actions", "rule_group_id", "title", "trigger", "triggers", "active", "description", "order", "rule_group_title", "stop_processing", "strict", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        trigger: 'RuleTriggerType',
        rule_group_id: typing.Union[MetaOapg.properties.rule_group_id, str, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        triggers: typing.Union[MetaOapg.properties.triggers, list, tuple, ],
        actions: typing.Union[MetaOapg.properties.actions, list, tuple, ],
        active: typing.Union[MetaOapg.properties.active, bool, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        order: typing.Union[MetaOapg.properties.order, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        rule_group_title: typing.Union[MetaOapg.properties.rule_group_title, str, schemas.Unset] = schemas.unset,
        stop_processing: typing.Union[MetaOapg.properties.stop_processing, bool, schemas.Unset] = schemas.unset,
        strict: typing.Union[MetaOapg.properties.strict, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RuleStore':
        return super().__new__(
            cls,
            *_args,
            trigger=trigger,
            rule_group_id=rule_group_id,
            title=title,
            triggers=triggers,
            actions=actions,
            active=active,
            description=description,
            order=order,
            rule_group_title=rule_group_title,
            stop_processing=stop_processing,
            strict=strict,
            _configuration=_configuration,
            **kwargs,
        )

from firefly_iii_client.model.rule_action_store import RuleActionStore
from firefly_iii_client.model.rule_trigger_store import RuleTriggerStore
from firefly_iii_client.model.rule_trigger_type import RuleTriggerType
