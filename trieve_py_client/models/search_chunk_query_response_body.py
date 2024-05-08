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

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List
from trieve_py_client.models.score_chunk_dto import ScoreChunkDTO
from typing import Optional, Set
from typing_extensions import Self

class SearchChunkQueryResponseBody(BaseModel):
    """
    SearchChunkQueryResponseBody
    """ # noqa: E501
    score_chunks: List[ScoreChunkDTO]
    total_chunk_pages: StrictInt
    __properties: ClassVar[List[str]] = ["score_chunks", "total_chunk_pages"]

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
        """Create an instance of SearchChunkQueryResponseBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in score_chunks (list)
        _items = []
        if self.score_chunks:
            for _item in self.score_chunks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['score_chunks'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SearchChunkQueryResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "score_chunks": [ScoreChunkDTO.from_dict(_item) for _item in obj["score_chunks"]] if obj.get("score_chunks") is not None else None,
            "total_chunk_pages": obj.get("total_chunk_pages")
        })
        return _obj


