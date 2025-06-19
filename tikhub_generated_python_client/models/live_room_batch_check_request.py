from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LiveRoomBatchCheckRequest")


@_attrs_define
class LiveRoomBatchCheckRequest:
    """
    Attributes:
        room_ids (Union[Unset, list[str]]): 多个直播间ID组成的数组 / List of TikTok live room IDs
    """

    room_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        room_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.room_ids, Unset):
            room_ids = self.room_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if room_ids is not UNSET:
            field_dict["room_ids"] = room_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        room_ids = cast(list[str], d.pop("room_ids", UNSET))

        live_room_batch_check_request = cls(
            room_ids=room_ids,
        )

        live_room_batch_check_request.additional_properties = d
        return live_room_batch_check_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
