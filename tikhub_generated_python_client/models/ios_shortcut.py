from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IOSShortcut")


@_attrs_define
class IOSShortcut:
    """
    Attributes:
        version (str):
        update (str):
        link (str):
        link_en (str):
        note (str):
        note_en (str):
    """

    version: str
    update: str
    link: str
    link_en: str
    note: str
    note_en: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        update = self.update

        link = self.link

        link_en = self.link_en

        note = self.note

        note_en = self.note_en

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "update": update,
                "link": link,
                "link_en": link_en,
                "note": note,
                "note_en": note_en,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version = d.pop("version")

        update = d.pop("update")

        link = d.pop("link")

        link_en = d.pop("link_en")

        note = d.pop("note")

        note_en = d.pop("note_en")

        ios_shortcut = cls(
            version=version,
            update=update,
            link=link,
            link_en=link_en,
            note=note,
            note_en=note_en,
        )

        ios_shortcut.additional_properties = d
        return ios_shortcut

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
