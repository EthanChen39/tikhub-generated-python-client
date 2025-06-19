from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetVideoToProductStatsRequest")


@_attrs_define
class GetVideoToProductStatsRequest:
    """
    Attributes:
        item_id (str): 视频 ID/Video ID
        product_id (str): 商品 ID/Product ID
        cookie (Union[Unset, str]): 用户 Cookie 字符串/User Cookie String Default: 'Your_Cookie_String'.
        proxy (Union[None, Unset, str]): 可选 HTTP 代理地址/Optional HTTP Proxy Address Default: ''.
        start_date (Union[Unset, str]): 查询开始时间，如 '04-01-2025'/ Query Start Date, e.g. '04-01-2025' Default:
            '04-01-2025'.
    """

    item_id: str
    product_id: str
    cookie: Union[Unset, str] = "Your_Cookie_String"
    proxy: Union[None, Unset, str] = ""
    start_date: Union[Unset, str] = "04-01-2025"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_id = self.item_id

        product_id = self.product_id

        cookie = self.cookie

        proxy: Union[None, Unset, str]
        if isinstance(self.proxy, Unset):
            proxy = UNSET
        else:
            proxy = self.proxy

        start_date = self.start_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item_id": item_id,
                "product_id": product_id,
            }
        )
        if cookie is not UNSET:
            field_dict["cookie"] = cookie
        if proxy is not UNSET:
            field_dict["proxy"] = proxy
        if start_date is not UNSET:
            field_dict["start_date"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_id = d.pop("item_id")

        product_id = d.pop("product_id")

        cookie = d.pop("cookie", UNSET)

        def _parse_proxy(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        proxy = _parse_proxy(d.pop("proxy", UNSET))

        start_date = d.pop("start_date", UNSET)

        get_video_to_product_stats_request = cls(
            item_id=item_id,
            product_id=product_id,
            cookie=cookie,
            proxy=proxy,
            start_date=start_date,
        )

        get_video_to_product_stats_request.additional_properties = d
        return get_video_to_product_stats_request

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
