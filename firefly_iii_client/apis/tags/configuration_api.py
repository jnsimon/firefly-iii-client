# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 2.0.12
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""

from firefly_iii_client.paths.v1_configuration.get import GetConfiguration
from firefly_iii_client.paths.v1_configuration_name.get import GetSingleConfiguration
from firefly_iii_client.paths.v1_configuration_name.put import SetConfiguration


class ConfigurationApi(
    GetConfiguration,
    GetSingleConfiguration,
    SetConfiguration,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
