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

from trieve_python_client.api.dataset_api import DatasetApi


class TestDatasetApi(unittest.TestCase):
    """DatasetApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DatasetApi()

    def tearDown(self) -> None:
        pass

    def test_create_dataset(self) -> None:
        """Test case for create_dataset

        Create dataset
        """
        pass

    def test_delete_dataset(self) -> None:
        """Test case for delete_dataset

        Delete Dataset
        """
        pass

    def test_get_client_dataset_config(self) -> None:
        """Test case for get_client_dataset_config

        Get Client Configuration
        """
        pass

    def test_get_dataset(self) -> None:
        """Test case for get_dataset

        Get Dataset
        """
        pass

    def test_get_datasets_from_organization(self) -> None:
        """Test case for get_datasets_from_organization

        Get Datasets from Organization
        """
        pass

    def test_update_dataset(self) -> None:
        """Test case for update_dataset

        Update Dataset
        """
        pass


if __name__ == '__main__':
    unittest.main()