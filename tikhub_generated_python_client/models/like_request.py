from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LikeRequest")


@_attrs_define
class LikeRequest:
    """
    Attributes:
        aweme_id (Union[Unset, str]): Video ID, which can be obtained from the sharing link, for example:
            https://www.tiktok.com/@username/video/7419966340443819295 Default: '7419966340443819295'.
        cookie (Union[Unset, str]): User Cookie, you can log in to your TikTok account in the browser and then copy the
            Cookie information, please use URL-encoded Cookie string when submitting. Default: 'Your_Cookie_From_Browser'.
        device_id (Union[Unset, str]): Device id, optional, if not filled in, it will be automatically generated, if you
            need to customize the device id, please use the device information interface to get the device id. Default: ''.
        iid (Union[Unset, str]): Device install id, optional, if not filled in, it will be automatically generated, if
            you need to customize the device iid, please use the device information interface to get the device iid.
            Default: ''.
        proxy (Union[Unset, str]): Proxy IP, optional, if not filled in, it will be automatically generated, if you need
            to customize the proxy IP, please use the proxy IP interface to get the proxy IP. Default: ''.
    """

    aweme_id: Union[Unset, str] = "7419966340443819295"
    cookie: Union[Unset, str] = "Your_Cookie_From_Browser"
    device_id: Union[Unset, str] = ""
    iid: Union[Unset, str] = ""
    proxy: Union[Unset, str] = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aweme_id = self.aweme_id

        cookie = self.cookie

        device_id = self.device_id

        iid = self.iid

        proxy = self.proxy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aweme_id is not UNSET:
            field_dict["aweme_id"] = aweme_id
        if cookie is not UNSET:
            field_dict["cookie"] = cookie
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if iid is not UNSET:
            field_dict["iid"] = iid
        if proxy is not UNSET:
            field_dict["proxy"] = proxy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aweme_id = d.pop("aweme_id", UNSET)

        cookie = d.pop("cookie", UNSET)

        device_id = d.pop("device_id", UNSET)

        iid = d.pop("iid", UNSET)

        proxy = d.pop("proxy", UNSET)

        like_request = cls(
            aweme_id=aweme_id,
            cookie=cookie,
            device_id=device_id,
            iid=iid,
            proxy=proxy,
        )

        like_request.additional_properties = d
        return like_request

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
