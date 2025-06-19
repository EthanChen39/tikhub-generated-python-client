from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetShowcaseProductListRequest")


@_attrs_define
class GetShowcaseProductListRequest:
    """
    Attributes:
        cookie (Union[Unset, str]): 用户 Cookie 字符串/User Cookie String Default: 'Your_Cookie_String'.
        proxy (Union[None, Unset, str]): 可选 HTTP 代理地址/Optional HTTP Proxy Address Default: ''.
        count (Union[Unset, int]): 每页数量/Page Size Default: 20.
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
    """

    cookie: Union[Unset, str] = "Your_Cookie_String"
    proxy: Union[None, Unset, str] = ""
    count: Union[Unset, int] = 20
    offset: Union[Unset, int] = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cookie = self.cookie

        proxy: Union[None, Unset, str]
        if isinstance(self.proxy, Unset):
            proxy = UNSET
        else:
            proxy = self.proxy

        count = self.count

        offset = self.offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cookie is not UNSET:
            field_dict["cookie"] = cookie
        if proxy is not UNSET:
            field_dict["proxy"] = proxy
        if count is not UNSET:
            field_dict["count"] = count
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cookie = d.pop("cookie", UNSET)

        def _parse_proxy(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        proxy = _parse_proxy(d.pop("proxy", UNSET))

        count = d.pop("count", UNSET)

        offset = d.pop("offset", UNSET)

        get_showcase_product_list_request = cls(
            cookie=cookie,
            proxy=proxy,
            count=count,
            offset=offset,
        )

        get_showcase_product_list_request.additional_properties = d
        return get_showcase_product_list_request

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
