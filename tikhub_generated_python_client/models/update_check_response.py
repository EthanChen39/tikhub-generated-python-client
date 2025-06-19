from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCheckResponse")


@_attrs_define
class UpdateCheckResponse:
    """
    Attributes:
        latest_version (Union[Unset, str]):  Default: '1.0.0'.
        update_date (Union[Unset, str]):  Default: '2025-03-17'.
        download_url (Union[Unset, str]):  Default: 'https://github.com/TikHub/TikHub-Multi-Functional-
            Downloader/releases/tag/V1.0.0'.
        latest_download_url_win (Union[Unset, str]):  Default: 'https://github.com/TikHub/TikHub-Multi-Functional-
            Downloader/releases/download/V1.0.0/TikHub_Downloader-Windows-1.0.0.exe'.
        latest_download_url_mac (Union[Unset, str]):  Default: 'https://github.com/TikHub/TikHub-Multi-Functional-
            Downloader/archive/refs/tags/V1.0.0.zip'.
        upload_note (Union[Unset, str]):  Default: 'Bug fixes and performance improvements'.
    """

    latest_version: Union[Unset, str] = "1.0.0"
    update_date: Union[Unset, str] = "2025-03-17"
    download_url: Union[Unset, str] = "https://github.com/TikHub/TikHub-Multi-Functional-Downloader/releases/tag/V1.0.0"
    latest_download_url_win: Union[Unset, str] = (
        "https://github.com/TikHub/TikHub-Multi-Functional-Downloader/releases/download/V1.0.0/TikHub_Downloader-Windows-1.0.0.exe"
    )
    latest_download_url_mac: Union[Unset, str] = (
        "https://github.com/TikHub/TikHub-Multi-Functional-Downloader/archive/refs/tags/V1.0.0.zip"
    )
    upload_note: Union[Unset, str] = "Bug fixes and performance improvements"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latest_version = self.latest_version

        update_date = self.update_date

        download_url = self.download_url

        latest_download_url_win = self.latest_download_url_win

        latest_download_url_mac = self.latest_download_url_mac

        upload_note = self.upload_note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latest_version is not UNSET:
            field_dict["latest_version"] = latest_version
        if update_date is not UNSET:
            field_dict["update_date"] = update_date
        if download_url is not UNSET:
            field_dict["download_url"] = download_url
        if latest_download_url_win is not UNSET:
            field_dict["latest_download_url_win"] = latest_download_url_win
        if latest_download_url_mac is not UNSET:
            field_dict["latest_download_url_mac"] = latest_download_url_mac
        if upload_note is not UNSET:
            field_dict["upload_note"] = upload_note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        latest_version = d.pop("latest_version", UNSET)

        update_date = d.pop("update_date", UNSET)

        download_url = d.pop("download_url", UNSET)

        latest_download_url_win = d.pop("latest_download_url_win", UNSET)

        latest_download_url_mac = d.pop("latest_download_url_mac", UNSET)

        upload_note = d.pop("upload_note", UNSET)

        update_check_response = cls(
            latest_version=latest_version,
            update_date=update_date,
            download_url=download_url,
            latest_download_url_win=latest_download_url_win,
            latest_download_url_mac=latest_download_url_mac,
            upload_note=upload_note,
        )

        update_check_response.additional_properties = d
        return update_check_response

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
