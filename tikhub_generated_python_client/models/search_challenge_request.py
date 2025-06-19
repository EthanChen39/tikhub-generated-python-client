from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchChallengeRequest")


@_attrs_define
class SearchChallengeRequest:
    """
    Attributes:
        keyword (Union[Unset, str]): 搜索关键词/Search keyword Default: '游戏'.
        cursor (Union[Unset, int]): 游标/Cursor Default: 0.
        count (Union[Unset, int]): 数量/Count Default: 30.
        cookie (Union[Unset, str]): 用户自行提供的Cookie/User provided Cookie Default: ''.
    """

    keyword: Union[Unset, str] = "游戏"
    cursor: Union[Unset, int] = 0
    count: Union[Unset, int] = 30
    cookie: Union[Unset, str] = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keyword = self.keyword

        cursor = self.cursor

        count = self.count

        cookie = self.cookie

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
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
        keyword = d.pop("keyword", UNSET)

        cursor = d.pop("cursor", UNSET)

        count = d.pop("count", UNSET)

        cookie = d.pop("cookie", UNSET)

        search_challenge_request = cls(
            keyword=keyword,
            cursor=cursor,
            count=count,
            cookie=cookie,
        )

        search_challenge_request.additional_properties = d
        return search_challenge_request

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
