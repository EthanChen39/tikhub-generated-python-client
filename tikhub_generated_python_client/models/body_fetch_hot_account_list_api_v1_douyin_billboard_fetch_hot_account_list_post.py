from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.body_fetch_hot_account_list_api_v1_douyin_billboard_fetch_hot_account_list_post_query_tag import (
        BodyFetchHotAccountListApiV1DouyinBillboardFetchHotAccountListPostQueryTag,
    )


T = TypeVar("T", bound="BodyFetchHotAccountListApiV1DouyinBillboardFetchHotAccountListPost")


@_attrs_define
class BodyFetchHotAccountListApiV1DouyinBillboardFetchHotAccountListPost:
    """
    Attributes:
        date_window (Union[Unset, str]): 时间窗口，格式 小时，默认24小时 Default: '24'.
        page_num (Union[Unset, str]): 页码，默认1 Default: '1'.
        page_size (Union[Unset, str]): 每页数量，默认10 Default: '10'.
        query_tag (Union[Unset, BodyFetchHotAccountListApiV1DouyinBillboardFetchHotAccountListPostQueryTag]):
            子级垂类标签，空则为全部，多个标签需传入{"value": "{顶级垂类标签id}", "children": [{"value": "{子级垂类标签id}"}, {"value": "{子级垂类标签id}"}]}
    """

    date_window: Union[Unset, str] = "24"
    page_num: Union[Unset, str] = "1"
    page_size: Union[Unset, str] = "10"
    query_tag: Union[Unset, "BodyFetchHotAccountListApiV1DouyinBillboardFetchHotAccountListPostQueryTag"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_window = self.date_window

        page_num = self.page_num

        page_size = self.page_size

        query_tag: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.query_tag, Unset):
            query_tag = self.query_tag.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_window is not UNSET:
            field_dict["date_window"] = date_window
        if page_num is not UNSET:
            field_dict["page_num"] = page_num
        if page_size is not UNSET:
            field_dict["page_size"] = page_size
        if query_tag is not UNSET:
            field_dict["query_tag"] = query_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.body_fetch_hot_account_list_api_v1_douyin_billboard_fetch_hot_account_list_post_query_tag import (
            BodyFetchHotAccountListApiV1DouyinBillboardFetchHotAccountListPostQueryTag,
        )

        d = dict(src_dict)
        date_window = d.pop("date_window", UNSET)

        page_num = d.pop("page_num", UNSET)

        page_size = d.pop("page_size", UNSET)

        _query_tag = d.pop("query_tag", UNSET)
        query_tag: Union[Unset, BodyFetchHotAccountListApiV1DouyinBillboardFetchHotAccountListPostQueryTag]
        if isinstance(_query_tag, Unset):
            query_tag = UNSET
        else:
            query_tag = BodyFetchHotAccountListApiV1DouyinBillboardFetchHotAccountListPostQueryTag.from_dict(_query_tag)

        body_fetch_hot_account_list_api_v1_douyin_billboard_fetch_hot_account_list_post = cls(
            date_window=date_window,
            page_num=page_num,
            page_size=page_size,
            query_tag=query_tag,
        )

        body_fetch_hot_account_list_api_v1_douyin_billboard_fetch_hot_account_list_post.additional_properties = d
        return body_fetch_hot_account_list_api_v1_douyin_billboard_fetch_hot_account_list_post

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
