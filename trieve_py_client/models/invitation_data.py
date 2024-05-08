# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.8.0
    Contact: developers@trieve.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class InvitationData(BaseModel):
    """
    InvitationData
    """ # noqa: E501
    app_url: StrictStr = Field(description="The url of the app that the user will be directed to in order to set their password. Usually admin.trieve.ai, but may differ for local dev or self-hosted setups.")
    email: StrictStr = Field(description="The email of the user to invite. Must be a valid email as they will be sent an email to register.")
    organization_id: StrictStr = Field(description="The id of the organization to invite the user to.")
    redirect_uri: StrictStr = Field(description="The url that the user will be redirected to after setting their password.")
    user_role: StrictInt = Field(description="The role the user will have in the organization. 0 = User, 1 = Admin, 2 = Owner.")
    __properties: ClassVar[List[str]] = ["app_url", "email", "organization_id", "redirect_uri", "user_role"]

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
        """Create an instance of InvitationData from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InvitationData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "app_url": obj.get("app_url"),
            "email": obj.get("email"),
            "organization_id": obj.get("organization_id"),
            "redirect_uri": obj.get("redirect_uri"),
            "user_role": obj.get("user_role")
        })
        return _obj


