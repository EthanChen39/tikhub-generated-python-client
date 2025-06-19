from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.body_recaptcha_v2_api_v1_captcha_recaptcha_v2_post_proxy import (
        BodyRecaptchaV2ApiV1CaptchaRecaptchaV2PostProxy,
    )


T = TypeVar("T", bound="BodyRecaptchaV2ApiV1CaptchaRecaptchaV2Post")


@_attrs_define
class BodyRecaptchaV2ApiV1CaptchaRecaptchaV2Post:
    """
    Attributes:
        sitekey (str): Sitekey
        url (str): URL
        proxy (Union[Unset, BodyRecaptchaV2ApiV1CaptchaRecaptchaV2PostProxy]): Proxy
    """

    sitekey: str
    url: str
    proxy: Union[Unset, "BodyRecaptchaV2ApiV1CaptchaRecaptchaV2PostProxy"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sitekey = self.sitekey

        url = self.url

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
        if proxy is not UNSET:
            field_dict["proxy"] = proxy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.body_recaptcha_v2_api_v1_captcha_recaptcha_v2_post_proxy import (
            BodyRecaptchaV2ApiV1CaptchaRecaptchaV2PostProxy,
        )

        d = dict(src_dict)
        sitekey = d.pop("sitekey")

        url = d.pop("url")

        _proxy = d.pop("proxy", UNSET)
        proxy: Union[Unset, BodyRecaptchaV2ApiV1CaptchaRecaptchaV2PostProxy]
        if isinstance(_proxy, Unset):
            proxy = UNSET
        else:
            proxy = BodyRecaptchaV2ApiV1CaptchaRecaptchaV2PostProxy.from_dict(_proxy)

        body_recaptcha_v2_api_v1_captcha_recaptcha_v2_post = cls(
            sitekey=sitekey,
            url=url,
            proxy=proxy,
        )

        body_recaptcha_v2_api_v1_captcha_recaptcha_v2_post.additional_properties = d
        return body_recaptcha_v2_api_v1_captcha_recaptcha_v2_post

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
