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

from trieve_python_client.models.update_user_data import UpdateUserData

class TestUpdateUserData(unittest.TestCase):
    """UpdateUserData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateUserData:
        """Test UpdateUserData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateUserData`
        """
        model = UpdateUserData()
        if include_optional:
            return UpdateUserData(
                name = '',
                organization_id = '',
                role = 56,
                user_id = '',
                username = '',
                visible_email = True,
                website = ''
            )
        else:
            return UpdateUserData(
                organization_id = '',
        )
        """

    def testUpdateUserData(self):
        """Test UpdateUserData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()