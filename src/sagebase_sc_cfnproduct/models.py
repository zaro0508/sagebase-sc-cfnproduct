# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]
    typeConfiguration: Optional["TypeConfigurationModel"]


@dataclass
class ResourceModel(BaseModel):
    TPSCode: Optional[str]
    Title: Optional[str]
    CoverSheetIncluded: Optional[bool]
    DueDate: Optional[str]
    ApprovalDate: Optional[str]
    Memo: Optional["_Memo"]
    SecondCopyOfMemo: Optional["_Memo"]
    TestCode: Optional[str]
    Authors: Optional[Sequence[str]]
    Tags: Optional[AbstractSet["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            TPSCode=json_data.get("TPSCode"),
            Title=json_data.get("Title"),
            CoverSheetIncluded=json_data.get("CoverSheetIncluded"),
            DueDate=json_data.get("DueDate"),
            ApprovalDate=json_data.get("ApprovalDate"),
            Memo=Memo._deserialize(json_data.get("Memo")),
            SecondCopyOfMemo=Memo._deserialize(json_data.get("SecondCopyOfMemo")),
            TestCode=json_data.get("TestCode"),
            Authors=json_data.get("Authors"),
            Tags=set_or_none(json_data.get("Tags")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Memo(BaseModel):
    Heading: Optional[str]
    Body: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Memo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Memo"]:
        if not json_data:
            return None
        return cls(
            Heading=json_data.get("Heading"),
            Body=json_data.get("Body"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Memo = Memo


@dataclass
class Tag(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


@dataclass
class TypeConfigurationModel(BaseModel):

    @classmethod
    def _deserialize(
        cls: Type["_TypeConfigurationModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TypeConfigurationModel"]:
        if not json_data:
            return None
        return cls(
        )


# work around possible type aliasing issues when variable has same name as a model
_TypeConfigurationModel = TypeConfigurationModel
