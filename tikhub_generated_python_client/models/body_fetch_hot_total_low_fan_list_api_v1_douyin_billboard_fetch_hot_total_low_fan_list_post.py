from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.body_fetch_hot_total_low_fan_list_api_v1_douyin_billboard_fetch_hot_total_low_fan_list_post_tags_item import (
        BodyFetchHotTotalLowFanListApiV1DouyinBillboardFetchHotTotalLowFanListPostTagsItem,
    )


T = TypeVar("T", bound="BodyFetchHotTotalLowFanListApiV1DouyinBillboardFetchHotTotalLowFanListPost")


@_attrs_define
class BodyFetchHotTotalLowFanListApiV1DouyinBillboardFetchHotTotalLowFanListPost:
    """
    Attributes:
        page (Union[Unset, int]): 页码 Default: 1.
        page_size (Union[Unset, int]): 每页数量 Default: 10.
        date_window (Union[Unset, int]): 时间窗口，1 按小时 2 按天 Default: 24.
        tags (Union[Unset, list['BodyFetchHotTotalLowFanListApiV1DouyinBillboardFetchHotTotalLowFanListPostTagsItem']]):
            子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]}
    """

    page: Union[Unset, int] = 1
    page_size: Union[Unset, int] = 10
    date_window: Union[Unset, int] = 24
    tags: Union[Unset, list["BodyFetchHotTotalLowFanListApiV1DouyinBillboardFetchHotTotalLowFanListPostTagsItem"]] = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        page_size = self.page_size

        date_window = self.date_window

        tags: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["page_size"] = page_size
        if date_window is not UNSET:
            field_dict["date_window"] = date_window
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.body_fetch_hot_total_low_fan_list_api_v1_douyin_billboard_fetch_hot_total_low_fan_list_post_tags_item import (
            BodyFetchHotTotalLowFanListApiV1DouyinBillboardFetchHotTotalLowFanListPostTagsItem,
        )

        d = dict(src_dict)
        page = d.pop("page", UNSET)

        page_size = d.pop("page_size", UNSET)

        date_window = d.pop("date_window", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = BodyFetchHotTotalLowFanListApiV1DouyinBillboardFetchHotTotalLowFanListPostTagsItem.from_dict(
                tags_item_data
            )

            tags.append(tags_item)

        body_fetch_hot_total_low_fan_list_api_v1_douyin_billboard_fetch_hot_total_low_fan_list_post = cls(
            page=page,
            page_size=page_size,
            date_window=date_window,
            tags=tags,
        )

        body_fetch_hot_total_low_fan_list_api_v1_douyin_billboard_fetch_hot_total_low_fan_list_post.additional_properties = d
        return body_fetch_hot_total_low_fan_list_api_v1_douyin_billboard_fetch_hot_total_low_fan_list_post

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
