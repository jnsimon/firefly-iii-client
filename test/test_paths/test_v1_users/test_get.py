# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import firefly_iii_client
from firefly_iii_client.paths.v1_users import get  # noqa: E501
from firefly_iii_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1Users(ApiTestMixin, unittest.TestCase):
    """
    V1Users unit test stubs
        List all users.  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()