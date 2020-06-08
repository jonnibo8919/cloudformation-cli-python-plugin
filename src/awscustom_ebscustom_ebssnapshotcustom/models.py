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


@dataclass
class ResourceModel(BaseModel):
    Description: Optional[str]
    OwnerId: Optional[str]
    Encrypted: Optional[bool]
    Progress: Optional[str]
    SnapshotId: Optional[str]
    StartTime: Optional[str]
    State: Optional[str]
    VolumeId: Optional[str]
    VolumeSize: Optional[str]

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
            Description=json_data.get("Description"),
            OwnerId=json_data.get("OwnerId"),
            Encrypted=json_data.get("Encrypted"),
            Progress=json_data.get("Progress"),
            SnapshotId=json_data.get("SnapshotId"),
            StartTime=json_data.get("StartTime"),
            State=json_data.get("State"),
            VolumeId=json_data.get("VolumeId"),
            VolumeSize=json_data.get("VolumeSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


