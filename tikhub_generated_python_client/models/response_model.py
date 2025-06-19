from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResponseModel")


@_attrs_define
class ResponseModel:
    """
    Attributes:
        code (Union[Unset, int]): HTTP status code | HTTP状态码 Default: 200.
        router (Union[Unset, str]): The endpoint that generated this response | 生成此响应的端点 Default: ''.
        params (Union[Unset, Any]): The parameters used in the request | 请求中使用的参数 Default: {}.
        data (Union[Any, None, Unset]): The response data | 响应数据
    """

    code: Union[Unset, int] = 200
    router: Union[Unset, str] = ""
    params: Union[Unset, Any] = {}
    data: Union[Any, None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        router = self.router

        params = self.params

        data: Union[Any, None, Unset]
        if isinstance(self.data, Unset):
            data = UNSET
        else:
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if router is not UNSET:
            field_dict["router"] = router
        if params is not UNSET:
            field_dict["params"] = params
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        router = d.pop("router", UNSET)

        params = d.pop("params", UNSET)

        def _parse_data(data: object) -> Union[Any, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[Any, None, Unset], data)

        data = _parse_data(d.pop("data", UNSET))

        response_model = cls(
            code=code,
            router=router,
            params=params,
            data=data,
        )

        response_model.additional_properties = d
        return response_model

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
