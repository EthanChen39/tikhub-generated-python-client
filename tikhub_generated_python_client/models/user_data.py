from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserData")


@_attrs_define
class UserData:
    """
    Attributes:
        email (str):
        balance (float):
        free_credit (float):
        email_verified (bool):
        account_disabled (bool):
        is_active (bool):
    """

    email: str
    balance: float
    free_credit: float
    email_verified: bool
    account_disabled: bool
    is_active: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        balance = self.balance

        free_credit = self.free_credit

        email_verified = self.email_verified

        account_disabled = self.account_disabled

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "balance": balance,
                "free_credit": free_credit,
                "email_verified": email_verified,
                "account_disabled": account_disabled,
                "is_active": is_active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        balance = d.pop("balance")

        free_credit = d.pop("free_credit")

        email_verified = d.pop("email_verified")

        account_disabled = d.pop("account_disabled")

        is_active = d.pop("is_active")

        user_data = cls(
            email=email,
            balance=balance,
            free_credit=free_credit,
            email_verified=email_verified,
            account_disabled=account_disabled,
            is_active=is_active,
        )

        user_data.additional_properties = d
        return user_data

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
