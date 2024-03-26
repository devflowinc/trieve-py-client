# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.5.0
    Contact: developers@trieve.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trieve_python_client.models.auth_query import AuthQuery

class TestAuthQuery(unittest.TestCase):
    """AuthQuery unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthQuery:
        """Test AuthQuery
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthQuery`
        """
        model = AuthQuery()
        if include_optional:
            return AuthQuery(
                inv_code = '',
                organization_id = '',
                redirect_uri = ''
            )
        else:
            return AuthQuery(
        )
        """

    def testAuthQuery(self):
        """Test AuthQuery"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()