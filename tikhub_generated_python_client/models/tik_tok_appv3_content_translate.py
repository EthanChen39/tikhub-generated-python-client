from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TikTokAPPV3ContentTranslate")


@_attrs_define
class TikTokAPPV3ContentTranslate:
    """
    Attributes:
        trg_lang (Union[Unset, str]): 目标语言ISO639-1代码，例如：zh-Hans/ Target language ISO639-1 code, e.g. zh-Hans Default:
            'zh-Hans'.
        src_content (Union[Unset, str]): 源语言内容，也就是需要翻译的内容/ Source language content, i.e. the content to be translated
            Default: 'Hello, welcome to TikHub!'.
    """

    trg_lang: Union[Unset, str] = "zh-Hans"
    src_content: Union[Unset, str] = "Hello, welcome to TikHub!"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trg_lang = self.trg_lang

        src_content = self.src_content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if trg_lang is not UNSET:
            field_dict["trg_lang"] = trg_lang
        if src_content is not UNSET:
            field_dict["src_content"] = src_content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        trg_lang = d.pop("trg_lang", UNSET)

        src_content = d.pop("src_content", UNSET)

        tik_tok_appv3_content_translate = cls(
            trg_lang=trg_lang,
            src_content=src_content,
        )

        tik_tok_appv3_content_translate.additional_properties = d
        return tik_tok_appv3_content_translate

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
