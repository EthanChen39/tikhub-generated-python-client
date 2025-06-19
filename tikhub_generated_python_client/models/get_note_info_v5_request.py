from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetNoteInfoV5Request")


@_attrs_define
class GetNoteInfoV5Request:
    """
    Attributes:
        note_id (Union[Unset, str]): 笔记ID/Note ID Default: '67855d09000000001703d449'.
        xsec_token (Union[Unset, str]): X-Sec-Token，可以从搜索接口中获取/X-Sec-Token, can be obtained from the search interface
            Default: 'ABfpRSESmZDRbX-EX7lzEztktMngxPVC9kU-dgQmuQoNo='.
        cookie (Union[Unset, str]): 用户自行提供的已登录的网页Cookie/User provided logged-in web Cookie Default: ''.
        proxy (Union[Unset, str]): 代理，格式：http://用户名:密码@IP:端口/Proxy, format: http://username:password@IP:port Default:
            ''.
    """

    note_id: Union[Unset, str] = "67855d09000000001703d449"
    xsec_token: Union[Unset, str] = "ABfpRSESmZDRbX-EX7lzEztktMngxPVC9kU-dgQmuQoNo="
    cookie: Union[Unset, str] = ""
    proxy: Union[Unset, str] = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        note_id = self.note_id

        xsec_token = self.xsec_token

        cookie = self.cookie

        proxy = self.proxy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if note_id is not UNSET:
            field_dict["note_id"] = note_id
        if xsec_token is not UNSET:
            field_dict["xsec_token"] = xsec_token
        if cookie is not UNSET:
            field_dict["cookie"] = cookie
        if proxy is not UNSET:
            field_dict["proxy"] = proxy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        note_id = d.pop("note_id", UNSET)

        xsec_token = d.pop("xsec_token", UNSET)

        cookie = d.pop("cookie", UNSET)

        proxy = d.pop("proxy", UNSET)

        get_note_info_v5_request = cls(
            note_id=note_id,
            xsec_token=xsec_token,
            cookie=cookie,
            proxy=proxy,
        )

        get_note_info_v5_request.additional_properties = d
        return get_note_info_v5_request

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
