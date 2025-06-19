from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChallengePostRequest")


@_attrs_define
class ChallengePostRequest:
    """
    Attributes:
        challenge_id (Union[Unset, str]): 话题ID/Challenge ID Default: '1608846127610893'.
        sort_type (Union[Unset, int]): 排序类型/Sort type Default: 0.
        cursor (Union[Unset, int]): 游标/Cursor Default: 0.
        count (Union[Unset, int]): 数量/Count Default: 20.
        cookie (Union[Unset, str]): 用户自行提供的Cookie/User provided Cookie Default: ''.
    """

    challenge_id: Union[Unset, str] = "1608846127610893"
    sort_type: Union[Unset, int] = 0
    cursor: Union[Unset, int] = 0
    count: Union[Unset, int] = 20
    cookie: Union[Unset, str] = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        challenge_id = self.challenge_id

        sort_type = self.sort_type

        cursor = self.cursor

        count = self.count

        cookie = self.cookie

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if challenge_id is not UNSET:
            field_dict["challenge_id"] = challenge_id
        if sort_type is not UNSET:
            field_dict["sort_type"] = sort_type
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if count is not UNSET:
            field_dict["count"] = count
        if cookie is not UNSET:
            field_dict["cookie"] = cookie

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        challenge_id = d.pop("challenge_id", UNSET)

        sort_type = d.pop("sort_type", UNSET)

        cursor = d.pop("cursor", UNSET)

        count = d.pop("count", UNSET)

        cookie = d.pop("cookie", UNSET)

        challenge_post_request = cls(
            challenge_id=challenge_id,
            sort_type=sort_type,
            cursor=cursor,
            count=count,
            cookie=cookie,
        )

        challenge_post_request.additional_properties = d
        return challenge_post_request

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
