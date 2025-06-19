import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="APIKeyData")


@_attrs_define
class APIKeyData:
    """
    Attributes:
        api_key_name (str):
        api_key_scopes (list[Any]):
        created_at (datetime.datetime):
        expires_at (Union[None, datetime.datetime]):
        api_key_status (int):
    """

    api_key_name: str
    api_key_scopes: list[Any]
    created_at: datetime.datetime
    expires_at: Union[None, datetime.datetime]
    api_key_status: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key_name = self.api_key_name

        api_key_scopes = self.api_key_scopes

        created_at = self.created_at.isoformat()

        expires_at: Union[None, str]
        if isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        api_key_status = self.api_key_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "api_key_name": api_key_name,
                "api_key_scopes": api_key_scopes,
                "created_at": created_at,
                "expires_at": expires_at,
                "api_key_status": api_key_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key_name = d.pop("api_key_name")

        api_key_scopes = cast(list[Any], d.pop("api_key_scopes"))

        created_at = isoparse(d.pop("created_at"))

        def _parse_expires_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        api_key_status = d.pop("api_key_status")

        api_key_data = cls(
            api_key_name=api_key_name,
            api_key_scopes=api_key_scopes,
            created_at=created_at,
            expires_at=expires_at,
            api_key_status=api_key_status,
        )

        api_key_data.additional_properties = d
        return api_key_data

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
