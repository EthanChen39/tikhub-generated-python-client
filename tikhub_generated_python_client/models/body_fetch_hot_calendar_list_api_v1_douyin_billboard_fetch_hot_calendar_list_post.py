from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost")


@_attrs_define
class BodyFetchHotCalendarListApiV1DouyinBillboardFetchHotCalendarListPost:
    """
    Attributes:
        city_code (Union[Unset, str]): 城市编码，从城市列表获取，空为全部 Default: ''.
        category_code (Union[Unset, str]): 热点榜分类编码，从热点榜分类获取，空为全部 Default: ''.
        end_date (Union[Unset, int]): 快照结束时间 格式10位时间戳 Default: 1735488000.
        start_date (Union[Unset, int]): 快照开始时间 格式10位时间戳 Default: 1734902400.
    """

    city_code: Union[Unset, str] = ""
    category_code: Union[Unset, str] = ""
    end_date: Union[Unset, int] = 1735488000
    start_date: Union[Unset, int] = 1734902400
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        city_code = self.city_code

        category_code = self.category_code

        end_date = self.end_date

        start_date = self.start_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if city_code is not UNSET:
            field_dict["city_code"] = city_code
        if category_code is not UNSET:
            field_dict["category_code"] = category_code
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if start_date is not UNSET:
            field_dict["start_date"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        city_code = d.pop("city_code", UNSET)

        category_code = d.pop("category_code", UNSET)

        end_date = d.pop("end_date", UNSET)

        start_date = d.pop("start_date", UNSET)

        body_fetch_hot_calendar_list_api_v1_douyin_billboard_fetch_hot_calendar_list_post = cls(
            city_code=city_code,
            category_code=category_code,
            end_date=end_date,
            start_date=start_date,
        )

        body_fetch_hot_calendar_list_api_v1_douyin_billboard_fetch_hot_calendar_list_post.additional_properties = d
        return body_fetch_hot_calendar_list_api_v1_douyin_billboard_fetch_hot_calendar_list_post

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
