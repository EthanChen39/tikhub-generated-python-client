from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mode_enum import ModeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="TikTokAPPLoginEncryptDecryptRequest")


@_attrs_define
class TikTokAPPLoginEncryptDecryptRequest:
    """
    Example:
        {'mode': 'encrypt', 'password': 'example_password', 'username': 'example_username'}

    Attributes:
        username (Union[Unset, str]): Plaintext or encrypted username Default: 'example_username'.
        password (Union[Unset, str]): Plaintext or encrypted password Default: 'example_password'.
        mode (Union[Unset, ModeEnum]):  Default: ModeEnum.ENCRYPT.
    """

    username: Union[Unset, str] = "example_username"
    password: Union[Unset, str] = "example_password"
    mode: Union[Unset, ModeEnum] = ModeEnum.ENCRYPT
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, ModeEnum]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = ModeEnum(_mode)

        tik_tok_app_login_encrypt_decrypt_request = cls(
            username=username,
            password=password,
            mode=mode,
        )

        tik_tok_app_login_encrypt_decrypt_request.additional_properties = d
        return tik_tok_app_login_encrypt_decrypt_request

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
