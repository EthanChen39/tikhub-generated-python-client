from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserSearchRequestV2")


@_attrs_define
class UserSearchRequestV2:
    """
    Attributes:
        keyword (Union[Unset, str]): 关键词 / Keyword Default: '猫咪'.
        cursor (Union[Unset, int]): 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last
            response Default: 0.
    """

    keyword: Union[Unset, str] = "猫咪"
    cursor: Union[Unset, int] = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keyword = self.keyword

        cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keyword = d.pop("keyword", UNSET)

        cursor = d.pop("cursor", UNSET)

        user_search_request_v2 = cls(
            keyword=keyword,
            cursor=cursor,
        )

        user_search_request_v2.additional_properties = d
        return user_search_request_v2

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
