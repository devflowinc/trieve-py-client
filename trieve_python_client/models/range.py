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

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class Range(BaseModel):
    """
    Range
    """ # noqa: E501
    gt: Optional[Union[StrictFloat, StrictInt]] = None
    gte: Optional[Union[StrictFloat, StrictInt]] = None
    lt: Optional[Union[StrictFloat, StrictInt]] = None
    lte: Optional[Union[StrictFloat, StrictInt]] = None
    __properties: ClassVar[List[str]] = ["gt", "gte", "lt", "lte"]

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
        """Create an instance of Range from a JSON string"""
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
        # set to None if gt (nullable) is None
        # and model_fields_set contains the field
        if self.gt is None and "gt" in self.model_fields_set:
            _dict['gt'] = None

        # set to None if gte (nullable) is None
        # and model_fields_set contains the field
        if self.gte is None and "gte" in self.model_fields_set:
            _dict['gte'] = None

        # set to None if lt (nullable) is None
        # and model_fields_set contains the field
        if self.lt is None and "lt" in self.model_fields_set:
            _dict['lt'] = None

        # set to None if lte (nullable) is None
        # and model_fields_set contains the field
        if self.lte is None and "lte" in self.model_fields_set:
            _dict['lte'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Range from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "gt": obj.get("gt"),
            "gte": obj.get("gte"),
            "lt": obj.get("lt"),
            "lte": obj.get("lte")
        })
        return _obj


