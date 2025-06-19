from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyFetchHotTotalHighSearchListApiV1DouyinBillboardFetchHotTotalHighSearchListPost")


@_attrs_define
class BodyFetchHotTotalHighSearchListApiV1DouyinBillboardFetchHotTotalHighSearchListPost:
    """
    Attributes:
        page_num (Union[Unset, int]): 页码 Default: 1.
        page_size (Union[Unset, int]): 每页数量 Default: 10.
        date_window (Union[Unset, int]): 时间窗口，1 按小时 2 按天 Default: 24.
        keyword (Union[Unset, str]): 搜索关键字 Default: '抖音'.
    """

    page_num: Union[Unset, int] = 1
    page_size: Union[Unset, int] = 10
    date_window: Union[Unset, int] = 24
    keyword: Union[Unset, str] = "抖音"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_num = self.page_num

        page_size = self.page_size

        date_window = self.date_window

        keyword = self.keyword

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_num is not UNSET:
            field_dict["page_num"] = page_num
        if page_size is not UNSET:
            field_dict["page_size"] = page_size
        if date_window is not UNSET:
            field_dict["date_window"] = date_window
        if keyword is not UNSET:
            field_dict["keyword"] = keyword

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page_num = d.pop("page_num", UNSET)

        page_size = d.pop("page_size", UNSET)

        date_window = d.pop("date_window", UNSET)

        keyword = d.pop("keyword", UNSET)

        body_fetch_hot_total_high_search_list_api_v1_douyin_billboard_fetch_hot_total_high_search_list_post = cls(
            page_num=page_num,
            page_size=page_size,
            date_window=date_window,
            keyword=keyword,
        )

        body_fetch_hot_total_high_search_list_api_v1_douyin_billboard_fetch_hot_total_high_search_list_post.additional_properties = d
        return body_fetch_hot_total_high_search_list_api_v1_douyin_billboard_fetch_hot_total_high_search_list_post

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
