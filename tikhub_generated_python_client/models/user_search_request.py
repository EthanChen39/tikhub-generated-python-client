from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserSearchRequest")


@_attrs_define
class UserSearchRequest:
    """
    Attributes:
        keyword (Union[Unset, str]): 关键词 / Keyword Default: '猫咪'.
        cursor (Union[Unset, int]): 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last
            response Default: 0.
        douyin_user_fans (Union[Unset, str]): 粉丝数过滤：空=不限 0_1k=1千以下 1k_5k=1千到5千 5k_10k=5千到1万 10k_100k=1万到10万
            100k_1M=10万到100万 1M_=100万以上 / Fans filter: empty=No limit, 0_1k=Under 1k, etc. Default: ''.
        douyin_user_type (Union[Unset, str]): 用户类型过滤：空=不限 300=创作者 900=小店 700=音乐人 800=明星 / User type filter: empty=No
            limit, 300=Creator, 900=Shop, 700=Musician, 800=Celebrity Default: ''.
        search_id (Union[Unset, str]): 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last
            response Default: ''.
    """

    keyword: Union[Unset, str] = "猫咪"
    cursor: Union[Unset, int] = 0
    douyin_user_fans: Union[Unset, str] = ""
    douyin_user_type: Union[Unset, str] = ""
    search_id: Union[Unset, str] = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keyword = self.keyword

        cursor = self.cursor

        douyin_user_fans = self.douyin_user_fans

        douyin_user_type = self.douyin_user_type

        search_id = self.search_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if douyin_user_fans is not UNSET:
            field_dict["douyin_user_fans"] = douyin_user_fans
        if douyin_user_type is not UNSET:
            field_dict["douyin_user_type"] = douyin_user_type
        if search_id is not UNSET:
            field_dict["search_id"] = search_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keyword = d.pop("keyword", UNSET)

        cursor = d.pop("cursor", UNSET)

        douyin_user_fans = d.pop("douyin_user_fans", UNSET)

        douyin_user_type = d.pop("douyin_user_type", UNSET)

        search_id = d.pop("search_id", UNSET)

        user_search_request = cls(
            keyword=keyword,
            cursor=cursor,
            douyin_user_fans=douyin_user_fans,
            douyin_user_type=douyin_user_type,
            search_id=search_id,
        )

        user_search_request.additional_properties = d
        return user_search_request

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
