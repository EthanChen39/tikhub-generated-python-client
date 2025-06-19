from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.xhs_web_sign_request_model_data import XhsWebSignRequestModelData


T = TypeVar("T", bound="XhsWebSignRequestModel")


@_attrs_define
class XhsWebSignRequestModel:
    """
    Attributes:
        path (Union[Unset, str]): 请求接口的路径/Request API path Default: '/api/sns/web/v1/homefeed'.
        data (Union[Unset, XhsWebSignRequestModelData]): 请求API的荷载数据/Payload data of request API
        cookie (Union[Unset, str]): 请求接口的Cookie/Request API cookie Default: 'web_session=030037a04eafd37791e6e4bd05204a8
            cf2af05;acw_tc=0a00d79f17363096679345838efb77751cc087fb039dd1691dc954824410f6;abRequestId=384480ae-5196-5818-
            a835-42e6278de9f0;webBuild=4.47.1;xsecappid=xhs-pc-web;a1=194441ef694PayUbdUvgp0dSHfIcACsNsLud0Lgru50000354513;w
            ebId=6cf10a564b9b07d129729b65e0d1785a;sec_poison_id=32964532-d414-4beb-914f-98811853b75f'.
    """

    path: Union[Unset, str] = "/api/sns/web/v1/homefeed"
    data: Union[Unset, "XhsWebSignRequestModelData"] = UNSET
    cookie: Union[Unset, str] = (
        "web_session=030037a04eafd37791e6e4bd05204a8cf2af05;acw_tc=0a00d79f17363096679345838efb77751cc087fb039dd1691dc954824410f6;abRequestId=384480ae-5196-5818-a835-42e6278de9f0;webBuild=4.47.1;xsecappid=xhs-pc-web;a1=194441ef694PayUbdUvgp0dSHfIcACsNsLud0Lgru50000354513;webId=6cf10a564b9b07d129729b65e0d1785a;sec_poison_id=32964532-d414-4beb-914f-98811853b75f"
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        cookie = self.cookie

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if data is not UNSET:
            field_dict["data"] = data
        if cookie is not UNSET:
            field_dict["cookie"] = cookie

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.xhs_web_sign_request_model_data import XhsWebSignRequestModelData

        d = dict(src_dict)
        path = d.pop("path", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, XhsWebSignRequestModelData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = XhsWebSignRequestModelData.from_dict(_data)

        cookie = d.pop("cookie", UNSET)

        xhs_web_sign_request_model = cls(
            path=path,
            data=data,
            cookie=cookie,
        )

        xhs_web_sign_request_model.additional_properties = d
        return xhs_web_sign_request_model

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
