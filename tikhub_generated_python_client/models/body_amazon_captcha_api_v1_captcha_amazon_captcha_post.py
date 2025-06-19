from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.body_amazon_captcha_api_v1_captcha_amazon_captcha_post_proxy import (
        BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPostProxy,
    )


T = TypeVar("T", bound="BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost")


@_attrs_define
class BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPost:
    """
    Attributes:
        app_id (str): App ID
        url (str): URL
        proxy (Union[Unset, BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPostProxy]): Proxy
    """

    app_id: str
    url: str
    proxy: Union[Unset, "BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPostProxy"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        url = self.url

        proxy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.proxy, Unset):
            proxy = self.proxy.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_id": app_id,
                "url": url,
            }
        )
        if proxy is not UNSET:
            field_dict["proxy"] = proxy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.body_amazon_captcha_api_v1_captcha_amazon_captcha_post_proxy import (
            BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPostProxy,
        )

        d = dict(src_dict)
        app_id = d.pop("app_id")

        url = d.pop("url")

        _proxy = d.pop("proxy", UNSET)
        proxy: Union[Unset, BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPostProxy]
        if isinstance(_proxy, Unset):
            proxy = UNSET
        else:
            proxy = BodyAmazonCaptchaApiV1CaptchaAmazonCaptchaPostProxy.from_dict(_proxy)

        body_amazon_captcha_api_v1_captcha_amazon_captcha_post = cls(
            app_id=app_id,
            url=url,
            proxy=proxy,
        )

        body_amazon_captcha_api_v1_captcha_amazon_captcha_post.additional_properties = d
        return body_amazon_captcha_api_v1_captcha_amazon_captcha_post

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
