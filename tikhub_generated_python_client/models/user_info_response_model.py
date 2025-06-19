from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_key_data import APIKeyData
    from ..models.user_data import UserData


T = TypeVar("T", bound="UserInfoResponseModel")


@_attrs_define
class UserInfoResponseModel:
    """
    Attributes:
        api_key_data (APIKeyData):
        user_data (UserData):
        code (Union[Unset, int]): HTTP status code | HTTP状态码 Default: 200.
        router (Union[Unset, str]): The endpoint that generated this response | 生成此响应的端点 Default: ''.
    """

    api_key_data: "APIKeyData"
    user_data: "UserData"
    code: Union[Unset, int] = 200
    router: Union[Unset, str] = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key_data = self.api_key_data.to_dict()

        user_data = self.user_data.to_dict()

        code = self.code

        router = self.router

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "api_key_data": api_key_data,
                "user_data": user_data,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if router is not UNSET:
            field_dict["router"] = router

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key_data import APIKeyData
        from ..models.user_data import UserData

        d = dict(src_dict)
        api_key_data = APIKeyData.from_dict(d.pop("api_key_data"))

        user_data = UserData.from_dict(d.pop("user_data"))

        code = d.pop("code", UNSET)

        router = d.pop("router", UNSET)

        user_info_response_model = cls(
            api_key_data=api_key_data,
            user_data=user_data,
            code=code,
            router=router,
        )

        user_info_response_model.additional_properties = d
        return user_info_response_model

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
