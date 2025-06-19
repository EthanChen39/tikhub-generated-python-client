from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MusicSearchRequest")


@_attrs_define
class MusicSearchRequest:
    """
    Attributes:
        keyword (Union[Unset, str]): 关键词 / Keyword Default: '猫咪'.
        cursor (Union[Unset, int]): 偏移游标，用于翻页，从上一次请求返回的响应中获取 / Offset cursor for pagination, obtained from the last
            response Default: 0.
        sort_type (Union[Unset, str]): 排序方式：0=综合排序 1=最多点赞 2=最新发布 / Sort type: 0=Comprehensive, 1=Most Likes, 2=Latest
            Default: '0'.
        publish_time (Union[Unset, str]): 发布时间筛选：0=不限 1=最近一天 7=最近一周 180=最近半年 / Publish time filter: 0=Unlimited, 1=Last
            day, 7=Last week, 180=Last half year Default: '0'.
        filter_duration (Union[Unset, str]): 视频时长过滤：0=不限 0-1=一分钟以内 1-5=一到五分钟 5-10000=五分钟以上 / Video duration filter:
            0=Unlimited, 0-1=Within 1 minute, 1-5=1 to 5 minutes, 5-10000=More than 5 minutes Default: '0'.
        content_type (Union[Unset, str]): 内容类型：0=不限 1=视频 2=图片 3=文章 / Content type: 0=All, 1=Video, 2=Picture, 3=Article
            Default: '0'.
        search_id (Union[Unset, str]): 搜索ID，用于翻页，从上一次请求返回的响应中获取 / Search ID for pagination, obtained from the last
            response Default: ''.
    """

    keyword: Union[Unset, str] = "猫咪"
    cursor: Union[Unset, int] = 0
    sort_type: Union[Unset, str] = "0"
    publish_time: Union[Unset, str] = "0"
    filter_duration: Union[Unset, str] = "0"
    content_type: Union[Unset, str] = "0"
    search_id: Union[Unset, str] = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keyword = self.keyword

        cursor = self.cursor

        sort_type = self.sort_type

        publish_time = self.publish_time

        filter_duration = self.filter_duration

        content_type = self.content_type

        search_id = self.search_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if sort_type is not UNSET:
            field_dict["sort_type"] = sort_type
        if publish_time is not UNSET:
            field_dict["publish_time"] = publish_time
        if filter_duration is not UNSET:
            field_dict["filter_duration"] = filter_duration
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if search_id is not UNSET:
            field_dict["search_id"] = search_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keyword = d.pop("keyword", UNSET)

        cursor = d.pop("cursor", UNSET)

        sort_type = d.pop("sort_type", UNSET)

        publish_time = d.pop("publish_time", UNSET)

        filter_duration = d.pop("filter_duration", UNSET)

        content_type = d.pop("content_type", UNSET)

        search_id = d.pop("search_id", UNSET)

        music_search_request = cls(
            keyword=keyword,
            cursor=cursor,
            sort_type=sort_type,
            publish_time=publish_time,
            filter_duration=filter_duration,
            content_type=content_type,
            search_id=search_id,
        )

        music_search_request.additional_properties = d
        return music_search_request

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
