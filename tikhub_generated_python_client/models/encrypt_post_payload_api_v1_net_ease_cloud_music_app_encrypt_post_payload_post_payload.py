from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EncryptPostPayloadApiV1NetEaseCloudMusicAppEncryptPostPayloadPostPayload")


@_attrs_define
class EncryptPostPayloadApiV1NetEaseCloudMusicAppEncryptPostPayloadPostPayload:
    """需要加密的payload/Need to be encrypted payload"""

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        encrypt_post_payload_api_v1_net_ease_cloud_music_app_encrypt_post_payload_post_payload = cls()

        encrypt_post_payload_api_v1_net_ease_cloud_music_app_encrypt_post_payload_post_payload.additional_properties = d
        return encrypt_post_payload_api_v1_net_ease_cloud_music_app_encrypt_post_payload_post_payload

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
