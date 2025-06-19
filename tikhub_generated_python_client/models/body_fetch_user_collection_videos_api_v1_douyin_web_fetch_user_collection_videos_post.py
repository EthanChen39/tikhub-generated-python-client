from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyFetchUserCollectionVideosApiV1DouyinWebFetchUserCollectionVideosPost")


@_attrs_define
class BodyFetchUserCollectionVideosApiV1DouyinWebFetchUserCollectionVideosPost:
    """
    Attributes:
        cookie (str): 用户网页版抖音Cookie/Your web version of Douyin Cookie
        max_cursor (Union[Unset, int]): 最大游标/Maximum cursor Default: 0.
        counts (Union[Unset, int]): 每页数量/Number per page Default: 20.
    """

    cookie: str
    max_cursor: Union[Unset, int] = 0
    counts: Union[Unset, int] = 20
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cookie = self.cookie

        max_cursor = self.max_cursor

        counts = self.counts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cookie": cookie,
            }
        )
        if max_cursor is not UNSET:
            field_dict["max_cursor"] = max_cursor
        if counts is not UNSET:
            field_dict["counts"] = counts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cookie = d.pop("cookie")

        max_cursor = d.pop("max_cursor", UNSET)

        counts = d.pop("counts", UNSET)

        body_fetch_user_collection_videos_api_v1_douyin_web_fetch_user_collection_videos_post = cls(
            cookie=cookie,
            max_cursor=max_cursor,
            counts=counts,
        )

        body_fetch_user_collection_videos_api_v1_douyin_web_fetch_user_collection_videos_post.additional_properties = d
        return body_fetch_user_collection_videos_api_v1_douyin_web_fetch_user_collection_videos_post

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
