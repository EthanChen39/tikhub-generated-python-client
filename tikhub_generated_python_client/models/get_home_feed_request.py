from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetHomeFeedRequest")


@_attrs_define
class GetHomeFeedRequest:
    """
    Attributes:
        feed_type (Union[Unset, str]): 推荐类型/Feed type Default: '0'.
        need_filter_image (Union[Unset, bool]): 是否只看图文笔记/Whether to view only image notes Default: False.
        cookie (Union[Unset, str]): 用户自行提供的已登录的网页Cookie/User provided logged-in web Cookie Default: ''.
        proxy (Union[Unset, str]): 代理，格式：http://用户名:密码@IP:端口/Proxy, format: http://username:password@IP:port Default:
            ''.
    """

    feed_type: Union[Unset, str] = "0"
    need_filter_image: Union[Unset, bool] = False
    cookie: Union[Unset, str] = ""
    proxy: Union[Unset, str] = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feed_type = self.feed_type

        need_filter_image = self.need_filter_image

        cookie = self.cookie

        proxy = self.proxy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if feed_type is not UNSET:
            field_dict["feed_type"] = feed_type
        if need_filter_image is not UNSET:
            field_dict["need_filter_image"] = need_filter_image
        if cookie is not UNSET:
            field_dict["cookie"] = cookie
        if proxy is not UNSET:
            field_dict["proxy"] = proxy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        feed_type = d.pop("feed_type", UNSET)

        need_filter_image = d.pop("need_filter_image", UNSET)

        cookie = d.pop("cookie", UNSET)

        proxy = d.pop("proxy", UNSET)

        get_home_feed_request = cls(
            feed_type=feed_type,
            need_filter_image=need_filter_image,
            cookie=cookie,
            proxy=proxy,
        )

        get_home_feed_request.additional_properties = d
        return get_home_feed_request

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
