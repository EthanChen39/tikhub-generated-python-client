from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyFetchHomeFeedApiV1TiktokWebFetchHomeFeedPost")


@_attrs_define
class BodyFetchHomeFeedApiV1TiktokWebFetchHomeFeedPost:
    """
    Attributes:
        count (Union[Unset, int]): 每页数量/Number per page Default: 15.
        cookie (Union[Unset, str]): 用户自己的cookie，可选参数，用于接口返回数据的个性化推荐。/ User's own cookie, optional parameter, used for
            personalized recommendations of interface return data.
    """

    count: Union[Unset, int] = 15
    cookie: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        cookie = self.cookie

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if cookie is not UNSET:
            field_dict["cookie"] = cookie

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        cookie = d.pop("cookie", UNSET)

        body_fetch_home_feed_api_v1_tiktok_web_fetch_home_feed_post = cls(
            count=count,
            cookie=cookie,
        )

        body_fetch_home_feed_api_v1_tiktok_web_fetch_home_feed_post.additional_properties = d
        return body_fetch_home_feed_api_v1_tiktok_web_fetch_home_feed_post

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
