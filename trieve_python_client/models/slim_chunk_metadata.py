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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class SlimChunkMetadata(BaseModel):
    """
    SlimChunkMetadata
    """ # noqa: E501
    created_at: datetime
    id: StrictStr
    link: Optional[StrictStr] = None
    metadata: Optional[Any] = None
    qdrant_point_id: Optional[StrictStr] = None
    tag_set: Optional[StrictStr] = None
    time_stamp: Optional[datetime] = None
    tracking_id: Optional[StrictStr] = None
    updated_at: datetime
    weight: Union[StrictFloat, StrictInt]
    __properties: ClassVar[List[str]] = ["created_at", "id", "link", "metadata", "qdrant_point_id", "tag_set", "time_stamp", "tracking_id", "updated_at", "weight"]

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
        """Create an instance of SlimChunkMetadata from a JSON string"""
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
        # set to None if link (nullable) is None
        # and model_fields_set contains the field
        if self.link is None and "link" in self.model_fields_set:
            _dict['link'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if qdrant_point_id (nullable) is None
        # and model_fields_set contains the field
        if self.qdrant_point_id is None and "qdrant_point_id" in self.model_fields_set:
            _dict['qdrant_point_id'] = None

        # set to None if tag_set (nullable) is None
        # and model_fields_set contains the field
        if self.tag_set is None and "tag_set" in self.model_fields_set:
            _dict['tag_set'] = None

        # set to None if time_stamp (nullable) is None
        # and model_fields_set contains the field
        if self.time_stamp is None and "time_stamp" in self.model_fields_set:
            _dict['time_stamp'] = None

        # set to None if tracking_id (nullable) is None
        # and model_fields_set contains the field
        if self.tracking_id is None and "tracking_id" in self.model_fields_set:
            _dict['tracking_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SlimChunkMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "id": obj.get("id"),
            "link": obj.get("link"),
            "metadata": obj.get("metadata"),
            "qdrant_point_id": obj.get("qdrant_point_id"),
            "tag_set": obj.get("tag_set"),
            "time_stamp": obj.get("time_stamp"),
            "tracking_id": obj.get("tracking_id"),
            "updated_at": obj.get("updated_at"),
            "weight": obj.get("weight")
        })
        return _obj


