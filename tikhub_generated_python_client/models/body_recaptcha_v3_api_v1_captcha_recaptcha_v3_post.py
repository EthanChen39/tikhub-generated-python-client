from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.body_recaptcha_v3_api_v1_captcha_recaptcha_v3_post_proxy import (
        BodyRecaptchaV3ApiV1CaptchaRecaptchaV3PostProxy,
    )


T = TypeVar("T", bound="BodyRecaptchaV3ApiV1CaptchaRecaptchaV3Post")


@_attrs_define
class BodyRecaptchaV3ApiV1CaptchaRecaptchaV3Post:
    """
    Attributes:
        sitekey (str): Sitekey
        url (str): URL
        action (Union[Unset, str]): Action
        proxy (Union[Unset, BodyRecaptchaV3ApiV1CaptchaRecaptchaV3PostProxy]): Proxy
    """

    sitekey: str
    url: str
    action: Union[Unset, str] = UNSET
    proxy: Union[Unset, "BodyRecaptchaV3ApiV1CaptchaRecaptchaV3PostProxy"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sitekey = self.sitekey

        url = self.url

        action = self.action

        proxy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.proxy, Unset):
            proxy = self.proxy.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sitekey": sitekey,
                "url": url,
            }
        )
        if action is not UNSET:
            field_dict["action"] = action
        if proxy is not UNSET:
            field_dict["proxy"] = proxy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.body_recaptcha_v3_api_v1_captcha_recaptcha_v3_post_proxy import (
            BodyRecaptchaV3ApiV1CaptchaRecaptchaV3PostProxy,
        )

        d = dict(src_dict)
        sitekey = d.pop("sitekey")

        url = d.pop("url")

        action = d.pop("action", UNSET)

        _proxy = d.pop("proxy", UNSET)
        proxy: Union[Unset, BodyRecaptchaV3ApiV1CaptchaRecaptchaV3PostProxy]
        if isinstance(_proxy, Unset):
            proxy = UNSET
        else:
            proxy = BodyRecaptchaV3ApiV1CaptchaRecaptchaV3PostProxy.from_dict(_proxy)

        body_recaptcha_v3_api_v1_captcha_recaptcha_v3_post = cls(
            sitekey=sitekey,
            url=url,
            action=action,
            proxy=proxy,
        )

        body_recaptcha_v3_api_v1_captcha_recaptcha_v3_post.additional_properties = d
        return body_recaptcha_v3_api_v1_captcha_recaptcha_v3_post

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
