from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyFetchUserLikeVideosApiV1DouyinWebFetchUserLikeVideosPost")


@_attrs_define
class BodyFetchUserLikeVideosApiV1DouyinWebFetchUserLikeVideosPost:
    """
    Attributes:
        sec_user_id (str): 用户sec_user_id/User sec_user_id
        max_cursor (Union[Unset, int]): 最大游标/Maximum cursor Default: 0.
        counts (Union[Unset, int]): 每页数量/Number per page Default: 20.
        cookie (Union[Unset, str]): 用户网页版抖音Cookie/Your web version of Douyin Cookie
    """

    sec_user_id: str
    max_cursor: Union[Unset, int] = 0
    counts: Union[Unset, int] = 20
    cookie: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sec_user_id = self.sec_user_id

        max_cursor = self.max_cursor

        counts = self.counts

        cookie = self.cookie

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sec_user_id": sec_user_id,
            }
        )
        if max_cursor is not UNSET:
            field_dict["max_cursor"] = max_cursor
        if counts is not UNSET:
            field_dict["counts"] = counts
        if cookie is not UNSET:
            field_dict["cookie"] = cookie

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sec_user_id = d.pop("sec_user_id")

        max_cursor = d.pop("max_cursor", UNSET)

        counts = d.pop("counts", UNSET)

        cookie = d.pop("cookie", UNSET)

        body_fetch_user_like_videos_api_v1_douyin_web_fetch_user_like_videos_post = cls(
            sec_user_id=sec_user_id,
            max_cursor=max_cursor,
            counts=counts,
            cookie=cookie,
        )

        body_fetch_user_like_videos_api_v1_douyin_web_fetch_user_like_videos_post.additional_properties = d
        return body_fetch_user_like_videos_api_v1_douyin_web_fetch_user_like_videos_post

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
