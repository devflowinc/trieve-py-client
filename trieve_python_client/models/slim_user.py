# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.5.5
    Contact: developers@trieve.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from trieve_python_client.models.organization import Organization
from trieve_python_client.models.user_organization import UserOrganization
from typing import Optional, Set
from typing_extensions import Self

class SlimUser(BaseModel):
    """
    SlimUser
    """ # noqa: E501
    email: StrictStr
    id: StrictStr
    name: Optional[StrictStr] = None
    orgs: List[Organization]
    user_orgs: List[UserOrganization]
    __properties: ClassVar[List[str]] = ["email", "id", "name", "orgs", "user_orgs"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SlimUser from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in orgs (list)
        _items = []
        if self.orgs:
            for _item in self.orgs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['orgs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in user_orgs (list)
        _items = []
        if self.user_orgs:
            for _item in self.user_orgs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['user_orgs'] = _items
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SlimUser from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "email": obj.get("email"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "orgs": [Organization.from_dict(_item) for _item in obj["orgs"]] if obj.get("orgs") is not None else None,
            "user_orgs": [UserOrganization.from_dict(_item) for _item in obj["user_orgs"]] if obj.get("user_orgs") is not None else None
        })
        return _obj


