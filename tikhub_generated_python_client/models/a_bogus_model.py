from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ABogusModel")


@_attrs_define
class ABogusModel:
    """
    Attributes:
        url (str): 请求的API URL，需要使用urlencode(url, safe='*')进行编码 | The requested API URL, needs to be encoded using
            urlencode(url, safe='*') Example: https://www.douyin.com/aweme/v1/web/general/search/single/?device_platform=web
            app&aid=6383&channel=channel_pc_web&search_channel=aweme_general&enable_history=1&keyword=%E4%B8%AD%E5%8D%8E%E5%
            A8%98&search_source=normal_search&query_correct_type=1&is_filter_search=0&from_group_id=7346905902554844468&offs
            et=0&count=15&need_filter_settings=1&pc_client_type=1&version_code=190600&version_name=19.6.0&cookie_enabled=tru
            e&screen_width=1280&screen_height=800&browser_language=zh-CN&browser_platform=Win32&browser_name=Firefox&browser
            _version=124.0&browser_online=true&engine_name=Gecko&engine_version=124.0&os_name=Windows&os_version=10&cpu_core
            _num=16&device_memory=&platform=PC&webid=7348962975497324070&msToken=YCTVM6YGmjFdIpQAN9ykXLBXiSiuHdZkOkEQWTeqVOH
            BEPmOcM0lNwE0Kd9vgHPMPigSndZDHfAq9k-6lDmH3Jqz6mHHxmn-BzQjmLMIfLIPgirgnOixM9x4PwgcNQ%3D%3D.
        data (str): POST请求API时的载荷数据，需要使用urlencode(data, safe='*')进行编码 | The payload data when requesting the API with
            POST, needs to be encoded using urlencode(data, safe='*')
        user_agent (str): 请求API时的User-Agent | User-Agent when requesting the API Example: Mozilla/5.0 (Windows NT 10.0;
            Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36.
        index_0 (Union[Unset, int]): 加密明文列表的第一个值，无特殊要求，默认为0 Default: 0.
        index_1 (Union[Unset, int]): 加密明文列表的第一个值，无特殊要求，默认为1 Default: 1.
        index_2 (Union[Unset, int]): 加密明文列表的第一个值，无特殊要求，默认为14 Default: 14.
    """

    url: str
    data: str
    user_agent: str
    index_0: Union[Unset, int] = 0
    index_1: Union[Unset, int] = 1
    index_2: Union[Unset, int] = 14
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        data = self.data

        user_agent = self.user_agent

        index_0 = self.index_0

        index_1 = self.index_1

        index_2 = self.index_2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "data": data,
                "user_agent": user_agent,
            }
        )
        if index_0 is not UNSET:
            field_dict["index_0"] = index_0
        if index_1 is not UNSET:
            field_dict["index_1"] = index_1
        if index_2 is not UNSET:
            field_dict["index_2"] = index_2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        data = d.pop("data")

        user_agent = d.pop("user_agent")

        index_0 = d.pop("index_0", UNSET)

        index_1 = d.pop("index_1", UNSET)

        index_2 = d.pop("index_2", UNSET)

        a_bogus_model = cls(
            url=url,
            data=data,
            user_agent=user_agent,
            index_0=index_0,
            index_1=index_1,
            index_2=index_2,
        )

        a_bogus_model.additional_properties = d
        return a_bogus_model

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
