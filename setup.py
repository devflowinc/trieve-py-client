# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.6.9
    Contact: developers@trieve.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "trieve_py_client"
VERSION = "0.6.9"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Trieve API",
    author="Trieve Team",
    author_email="developers@trieve.ai",
    url="https://trieve.ai",
    keywords=["OpenAPI", "OpenAPI-Generator", "Trieve API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="BSL",
    long_description_content_type='text/markdown',
    long_description="""\
    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.
    """,  # noqa: E501
    package_data={"trieve_py_client": ["py.typed"]},
)
