from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.live_search_v2_request import LiveSearchV2Request
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: LiveSearchV2Request,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/search/fetch_live_search_v2",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    if response.status_code == 200:
        response_200 = ResponseModel.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: LiveSearchV2Request,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取直播搜索 V2/Fetch live search V2

     # [中文]
    ### 用途:
    - 获取抖音 App 中直播搜索结果（V2 版本）。
    - 此接口稳定性可能不如 V1 版本，但返回的数据更丰富。
    - 返回丰富的直播间信息，包括主播资料、直播标题、封面图、观众数、拉流播放地址等。

    ### 备注:
    - 仅返回直播内容，不包含其他内容。
    - 初次请求时 `cursor` 传入 0，`search_id` 传空字符串。
    - 翻页查询时使用上次响应返回的 `cursor` 和 `search_id`。

    ### 参数:
    - keyword: 搜索关键词，例如 \"游戏\"
    - cursor: 翻页游标（首次请求传 0）
    - sort_type: 排序方式
      - `0`: 综合排序
      - `1`: 最多点赞
      - `2`: 最新发布
    - publish_time: 发布时间筛选
      - `0`: 不限
      - `1`: 最近一天
      - `7`: 最近一周
      - `180`: 最近半年
    - filter_duration: 视频时长过滤
      - `0`: 不限
    - content_type: 内容类型（固定为直播）
    - search_id: 分页用搜索ID

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"游戏\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"1\",
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `cursor`: 翻页用游标
    - `has_more`: 是否还有更多数据（1=有，0=无）
    - `business_data[]`: 直播房间列表，每个房间包含：
      - `type`: 类型标识（固定999）
      - `data`:
        - `card_type_name`: 卡片布局类型（如 \"vertical_normal_living_room\"）
        - `aweme_list[]`: 直播内容列表
          - `aweme_id`: 直播内容ID
          - `group_id`: 分组ID
          - `author`:
            - `uid`: 主播用户ID
            - `nickname`: 主播昵称
            - `short_id`: 短ID
            - `sec_uid`: 加密用户ID
            - `avatar_thumb.url_list`: 小图头像
            - `avatar_medium.url_list`: 中图头像
            - `avatar_larger.url_list`: 高清头像
            - `room_id`: 当前直播间ID
            - `room_cover.url_list`: 直播封面图URL
          - `rawdata` (解析后主要字段):
            - `title`: 直播间标题
            - `user_count`: 当前观看人数
            - `cover.url_list`: 直播间封面
            - `stream_url`:
              - `flv_pull_url`: 拉流地址列表（不同清晰度）
                - `FULL_HD1`: 蓝光
                - `HD1`: 超清
                - `SD1`: 标清
                - `SD2`: 高清
              - `hls_pull_url`: HLS地址（可用于移动端播放）
              - `default_resolution`: 默认播放清晰度
              - `candidate_resolution[]`: 备选清晰度列表
            - `stats.total_user`: 当前直播间在线人数
            - `owner.nickname`: 主播昵称
            - `owner.avatar_thumb.url_list`: 主播缩略头像
            - `size`: 分辨率（如 1280x720）

    - `extra`:
      - `now`: 当前服务器时间戳
      - `search_request_id`: 本次搜索请求ID

    ---

    # [English]
    ### Purpose:
    - Fetch live stream search results (Version 2) from Douyin App.
    - This API may be less stable than Version 1 but returns richer data.
    - Provides detailed information about each live room including host info, room title, cover images,
    viewer counts, and stream URLs.

    ### Notes:
    - Only live streaming content is returned.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - For pagination, use the `cursor` and `search_id` from the last response.

    ### Parameters:
    - keyword: Search keyword, e.g., \"games\"
    - cursor: Pagination cursor (0 for the first request)
    - sort_type: Sorting method
      - `0`: Comprehensive
      - `1`: Most likes
      - `2`: Latest
    - publish_time: Publish time filter
      - `0`: Unlimited
      - `1`: Last day
      - `7`: Last week
      - `180`: Last half year
    - filter_duration: Video duration filter
      - `0`: Unlimited
    - content_type: Content type (fixed for live stream)
    - search_id: Search ID for pagination

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"games\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"1\",
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `cursor`: Cursor for next page
    - `has_more`: Whether more results exist (1=Yes, 0=No)
    - `business_data[]`: List of live rooms
      - `type`: Type indicator (fixed 999)
      - `data`:
        - `card_type_name`: Card layout style
        - `aweme_list[]`: List of live stream content
          - `aweme_id`: Content ID
          - `group_id`: Group ID
          - `author`:
            - `uid`: Streamer's user ID
            - `nickname`: Streamer's nickname
            - `short_id`: Streamer's short ID
            - `sec_uid`: Encrypted user ID
            - `avatar_thumb.url_list`: Thumbnail avatar URLs
            - `avatar_medium.url_list`: Medium size avatar URLs
            - `avatar_larger.url_list`: Large size avatar URLs
            - `room_id`: Live room ID
            - `room_cover.url_list`: Room cover images
          - `rawdata`:
            - `title`: Live room title
            - `user_count`: Viewer count
            - `cover.url_list`: Cover image
            - `stream_url`:
              - `flv_pull_url`: FLV stream URLs
              - `hls_pull_url`: HLS stream URL
              - `default_resolution`: Default resolution
              - `candidate_resolution[]`: Available resolutions
            - `stats.total_user`: Total number of viewers
            - `owner.nickname`: Streamer's nickname
            - `owner.avatar_thumb.url_list`: Streamer's thumbnail avatar
            - `size`: Resolution size (e.g., 1280x720)

    - `extra`:
      - `now`: Server timestamp
      - `search_request_id`: Search request unique ID

    Args:
        body (LiveSearchV2Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: LiveSearchV2Request,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取直播搜索 V2/Fetch live search V2

     # [中文]
    ### 用途:
    - 获取抖音 App 中直播搜索结果（V2 版本）。
    - 此接口稳定性可能不如 V1 版本，但返回的数据更丰富。
    - 返回丰富的直播间信息，包括主播资料、直播标题、封面图、观众数、拉流播放地址等。

    ### 备注:
    - 仅返回直播内容，不包含其他内容。
    - 初次请求时 `cursor` 传入 0，`search_id` 传空字符串。
    - 翻页查询时使用上次响应返回的 `cursor` 和 `search_id`。

    ### 参数:
    - keyword: 搜索关键词，例如 \"游戏\"
    - cursor: 翻页游标（首次请求传 0）
    - sort_type: 排序方式
      - `0`: 综合排序
      - `1`: 最多点赞
      - `2`: 最新发布
    - publish_time: 发布时间筛选
      - `0`: 不限
      - `1`: 最近一天
      - `7`: 最近一周
      - `180`: 最近半年
    - filter_duration: 视频时长过滤
      - `0`: 不限
    - content_type: 内容类型（固定为直播）
    - search_id: 分页用搜索ID

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"游戏\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"1\",
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `cursor`: 翻页用游标
    - `has_more`: 是否还有更多数据（1=有，0=无）
    - `business_data[]`: 直播房间列表，每个房间包含：
      - `type`: 类型标识（固定999）
      - `data`:
        - `card_type_name`: 卡片布局类型（如 \"vertical_normal_living_room\"）
        - `aweme_list[]`: 直播内容列表
          - `aweme_id`: 直播内容ID
          - `group_id`: 分组ID
          - `author`:
            - `uid`: 主播用户ID
            - `nickname`: 主播昵称
            - `short_id`: 短ID
            - `sec_uid`: 加密用户ID
            - `avatar_thumb.url_list`: 小图头像
            - `avatar_medium.url_list`: 中图头像
            - `avatar_larger.url_list`: 高清头像
            - `room_id`: 当前直播间ID
            - `room_cover.url_list`: 直播封面图URL
          - `rawdata` (解析后主要字段):
            - `title`: 直播间标题
            - `user_count`: 当前观看人数
            - `cover.url_list`: 直播间封面
            - `stream_url`:
              - `flv_pull_url`: 拉流地址列表（不同清晰度）
                - `FULL_HD1`: 蓝光
                - `HD1`: 超清
                - `SD1`: 标清
                - `SD2`: 高清
              - `hls_pull_url`: HLS地址（可用于移动端播放）
              - `default_resolution`: 默认播放清晰度
              - `candidate_resolution[]`: 备选清晰度列表
            - `stats.total_user`: 当前直播间在线人数
            - `owner.nickname`: 主播昵称
            - `owner.avatar_thumb.url_list`: 主播缩略头像
            - `size`: 分辨率（如 1280x720）

    - `extra`:
      - `now`: 当前服务器时间戳
      - `search_request_id`: 本次搜索请求ID

    ---

    # [English]
    ### Purpose:
    - Fetch live stream search results (Version 2) from Douyin App.
    - This API may be less stable than Version 1 but returns richer data.
    - Provides detailed information about each live room including host info, room title, cover images,
    viewer counts, and stream URLs.

    ### Notes:
    - Only live streaming content is returned.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - For pagination, use the `cursor` and `search_id` from the last response.

    ### Parameters:
    - keyword: Search keyword, e.g., \"games\"
    - cursor: Pagination cursor (0 for the first request)
    - sort_type: Sorting method
      - `0`: Comprehensive
      - `1`: Most likes
      - `2`: Latest
    - publish_time: Publish time filter
      - `0`: Unlimited
      - `1`: Last day
      - `7`: Last week
      - `180`: Last half year
    - filter_duration: Video duration filter
      - `0`: Unlimited
    - content_type: Content type (fixed for live stream)
    - search_id: Search ID for pagination

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"games\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"1\",
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `cursor`: Cursor for next page
    - `has_more`: Whether more results exist (1=Yes, 0=No)
    - `business_data[]`: List of live rooms
      - `type`: Type indicator (fixed 999)
      - `data`:
        - `card_type_name`: Card layout style
        - `aweme_list[]`: List of live stream content
          - `aweme_id`: Content ID
          - `group_id`: Group ID
          - `author`:
            - `uid`: Streamer's user ID
            - `nickname`: Streamer's nickname
            - `short_id`: Streamer's short ID
            - `sec_uid`: Encrypted user ID
            - `avatar_thumb.url_list`: Thumbnail avatar URLs
            - `avatar_medium.url_list`: Medium size avatar URLs
            - `avatar_larger.url_list`: Large size avatar URLs
            - `room_id`: Live room ID
            - `room_cover.url_list`: Room cover images
          - `rawdata`:
            - `title`: Live room title
            - `user_count`: Viewer count
            - `cover.url_list`: Cover image
            - `stream_url`:
              - `flv_pull_url`: FLV stream URLs
              - `hls_pull_url`: HLS stream URL
              - `default_resolution`: Default resolution
              - `candidate_resolution[]`: Available resolutions
            - `stats.total_user`: Total number of viewers
            - `owner.nickname`: Streamer's nickname
            - `owner.avatar_thumb.url_list`: Streamer's thumbnail avatar
            - `size`: Resolution size (e.g., 1280x720)

    - `extra`:
      - `now`: Server timestamp
      - `search_request_id`: Search request unique ID

    Args:
        body (LiveSearchV2Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: LiveSearchV2Request,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取直播搜索 V2/Fetch live search V2

     # [中文]
    ### 用途:
    - 获取抖音 App 中直播搜索结果（V2 版本）。
    - 此接口稳定性可能不如 V1 版本，但返回的数据更丰富。
    - 返回丰富的直播间信息，包括主播资料、直播标题、封面图、观众数、拉流播放地址等。

    ### 备注:
    - 仅返回直播内容，不包含其他内容。
    - 初次请求时 `cursor` 传入 0，`search_id` 传空字符串。
    - 翻页查询时使用上次响应返回的 `cursor` 和 `search_id`。

    ### 参数:
    - keyword: 搜索关键词，例如 \"游戏\"
    - cursor: 翻页游标（首次请求传 0）
    - sort_type: 排序方式
      - `0`: 综合排序
      - `1`: 最多点赞
      - `2`: 最新发布
    - publish_time: 发布时间筛选
      - `0`: 不限
      - `1`: 最近一天
      - `7`: 最近一周
      - `180`: 最近半年
    - filter_duration: 视频时长过滤
      - `0`: 不限
    - content_type: 内容类型（固定为直播）
    - search_id: 分页用搜索ID

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"游戏\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"1\",
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `cursor`: 翻页用游标
    - `has_more`: 是否还有更多数据（1=有，0=无）
    - `business_data[]`: 直播房间列表，每个房间包含：
      - `type`: 类型标识（固定999）
      - `data`:
        - `card_type_name`: 卡片布局类型（如 \"vertical_normal_living_room\"）
        - `aweme_list[]`: 直播内容列表
          - `aweme_id`: 直播内容ID
          - `group_id`: 分组ID
          - `author`:
            - `uid`: 主播用户ID
            - `nickname`: 主播昵称
            - `short_id`: 短ID
            - `sec_uid`: 加密用户ID
            - `avatar_thumb.url_list`: 小图头像
            - `avatar_medium.url_list`: 中图头像
            - `avatar_larger.url_list`: 高清头像
            - `room_id`: 当前直播间ID
            - `room_cover.url_list`: 直播封面图URL
          - `rawdata` (解析后主要字段):
            - `title`: 直播间标题
            - `user_count`: 当前观看人数
            - `cover.url_list`: 直播间封面
            - `stream_url`:
              - `flv_pull_url`: 拉流地址列表（不同清晰度）
                - `FULL_HD1`: 蓝光
                - `HD1`: 超清
                - `SD1`: 标清
                - `SD2`: 高清
              - `hls_pull_url`: HLS地址（可用于移动端播放）
              - `default_resolution`: 默认播放清晰度
              - `candidate_resolution[]`: 备选清晰度列表
            - `stats.total_user`: 当前直播间在线人数
            - `owner.nickname`: 主播昵称
            - `owner.avatar_thumb.url_list`: 主播缩略头像
            - `size`: 分辨率（如 1280x720）

    - `extra`:
      - `now`: 当前服务器时间戳
      - `search_request_id`: 本次搜索请求ID

    ---

    # [English]
    ### Purpose:
    - Fetch live stream search results (Version 2) from Douyin App.
    - This API may be less stable than Version 1 but returns richer data.
    - Provides detailed information about each live room including host info, room title, cover images,
    viewer counts, and stream URLs.

    ### Notes:
    - Only live streaming content is returned.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - For pagination, use the `cursor` and `search_id` from the last response.

    ### Parameters:
    - keyword: Search keyword, e.g., \"games\"
    - cursor: Pagination cursor (0 for the first request)
    - sort_type: Sorting method
      - `0`: Comprehensive
      - `1`: Most likes
      - `2`: Latest
    - publish_time: Publish time filter
      - `0`: Unlimited
      - `1`: Last day
      - `7`: Last week
      - `180`: Last half year
    - filter_duration: Video duration filter
      - `0`: Unlimited
    - content_type: Content type (fixed for live stream)
    - search_id: Search ID for pagination

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"games\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"1\",
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `cursor`: Cursor for next page
    - `has_more`: Whether more results exist (1=Yes, 0=No)
    - `business_data[]`: List of live rooms
      - `type`: Type indicator (fixed 999)
      - `data`:
        - `card_type_name`: Card layout style
        - `aweme_list[]`: List of live stream content
          - `aweme_id`: Content ID
          - `group_id`: Group ID
          - `author`:
            - `uid`: Streamer's user ID
            - `nickname`: Streamer's nickname
            - `short_id`: Streamer's short ID
            - `sec_uid`: Encrypted user ID
            - `avatar_thumb.url_list`: Thumbnail avatar URLs
            - `avatar_medium.url_list`: Medium size avatar URLs
            - `avatar_larger.url_list`: Large size avatar URLs
            - `room_id`: Live room ID
            - `room_cover.url_list`: Room cover images
          - `rawdata`:
            - `title`: Live room title
            - `user_count`: Viewer count
            - `cover.url_list`: Cover image
            - `stream_url`:
              - `flv_pull_url`: FLV stream URLs
              - `hls_pull_url`: HLS stream URL
              - `default_resolution`: Default resolution
              - `candidate_resolution[]`: Available resolutions
            - `stats.total_user`: Total number of viewers
            - `owner.nickname`: Streamer's nickname
            - `owner.avatar_thumb.url_list`: Streamer's thumbnail avatar
            - `size`: Resolution size (e.g., 1280x720)

    - `extra`:
      - `now`: Server timestamp
      - `search_request_id`: Search request unique ID

    Args:
        body (LiveSearchV2Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: LiveSearchV2Request,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取直播搜索 V2/Fetch live search V2

     # [中文]
    ### 用途:
    - 获取抖音 App 中直播搜索结果（V2 版本）。
    - 此接口稳定性可能不如 V1 版本，但返回的数据更丰富。
    - 返回丰富的直播间信息，包括主播资料、直播标题、封面图、观众数、拉流播放地址等。

    ### 备注:
    - 仅返回直播内容，不包含其他内容。
    - 初次请求时 `cursor` 传入 0，`search_id` 传空字符串。
    - 翻页查询时使用上次响应返回的 `cursor` 和 `search_id`。

    ### 参数:
    - keyword: 搜索关键词，例如 \"游戏\"
    - cursor: 翻页游标（首次请求传 0）
    - sort_type: 排序方式
      - `0`: 综合排序
      - `1`: 最多点赞
      - `2`: 最新发布
    - publish_time: 发布时间筛选
      - `0`: 不限
      - `1`: 最近一天
      - `7`: 最近一周
      - `180`: 最近半年
    - filter_duration: 视频时长过滤
      - `0`: 不限
    - content_type: 内容类型（固定为直播）
    - search_id: 分页用搜索ID

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"游戏\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"1\",
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `cursor`: 翻页用游标
    - `has_more`: 是否还有更多数据（1=有，0=无）
    - `business_data[]`: 直播房间列表，每个房间包含：
      - `type`: 类型标识（固定999）
      - `data`:
        - `card_type_name`: 卡片布局类型（如 \"vertical_normal_living_room\"）
        - `aweme_list[]`: 直播内容列表
          - `aweme_id`: 直播内容ID
          - `group_id`: 分组ID
          - `author`:
            - `uid`: 主播用户ID
            - `nickname`: 主播昵称
            - `short_id`: 短ID
            - `sec_uid`: 加密用户ID
            - `avatar_thumb.url_list`: 小图头像
            - `avatar_medium.url_list`: 中图头像
            - `avatar_larger.url_list`: 高清头像
            - `room_id`: 当前直播间ID
            - `room_cover.url_list`: 直播封面图URL
          - `rawdata` (解析后主要字段):
            - `title`: 直播间标题
            - `user_count`: 当前观看人数
            - `cover.url_list`: 直播间封面
            - `stream_url`:
              - `flv_pull_url`: 拉流地址列表（不同清晰度）
                - `FULL_HD1`: 蓝光
                - `HD1`: 超清
                - `SD1`: 标清
                - `SD2`: 高清
              - `hls_pull_url`: HLS地址（可用于移动端播放）
              - `default_resolution`: 默认播放清晰度
              - `candidate_resolution[]`: 备选清晰度列表
            - `stats.total_user`: 当前直播间在线人数
            - `owner.nickname`: 主播昵称
            - `owner.avatar_thumb.url_list`: 主播缩略头像
            - `size`: 分辨率（如 1280x720）

    - `extra`:
      - `now`: 当前服务器时间戳
      - `search_request_id`: 本次搜索请求ID

    ---

    # [English]
    ### Purpose:
    - Fetch live stream search results (Version 2) from Douyin App.
    - This API may be less stable than Version 1 but returns richer data.
    - Provides detailed information about each live room including host info, room title, cover images,
    viewer counts, and stream URLs.

    ### Notes:
    - Only live streaming content is returned.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - For pagination, use the `cursor` and `search_id` from the last response.

    ### Parameters:
    - keyword: Search keyword, e.g., \"games\"
    - cursor: Pagination cursor (0 for the first request)
    - sort_type: Sorting method
      - `0`: Comprehensive
      - `1`: Most likes
      - `2`: Latest
    - publish_time: Publish time filter
      - `0`: Unlimited
      - `1`: Last day
      - `7`: Last week
      - `180`: Last half year
    - filter_duration: Video duration filter
      - `0`: Unlimited
    - content_type: Content type (fixed for live stream)
    - search_id: Search ID for pagination

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"games\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"1\",
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `cursor`: Cursor for next page
    - `has_more`: Whether more results exist (1=Yes, 0=No)
    - `business_data[]`: List of live rooms
      - `type`: Type indicator (fixed 999)
      - `data`:
        - `card_type_name`: Card layout style
        - `aweme_list[]`: List of live stream content
          - `aweme_id`: Content ID
          - `group_id`: Group ID
          - `author`:
            - `uid`: Streamer's user ID
            - `nickname`: Streamer's nickname
            - `short_id`: Streamer's short ID
            - `sec_uid`: Encrypted user ID
            - `avatar_thumb.url_list`: Thumbnail avatar URLs
            - `avatar_medium.url_list`: Medium size avatar URLs
            - `avatar_larger.url_list`: Large size avatar URLs
            - `room_id`: Live room ID
            - `room_cover.url_list`: Room cover images
          - `rawdata`:
            - `title`: Live room title
            - `user_count`: Viewer count
            - `cover.url_list`: Cover image
            - `stream_url`:
              - `flv_pull_url`: FLV stream URLs
              - `hls_pull_url`: HLS stream URL
              - `default_resolution`: Default resolution
              - `candidate_resolution[]`: Available resolutions
            - `stats.total_user`: Total number of viewers
            - `owner.nickname`: Streamer's nickname
            - `owner.avatar_thumb.url_list`: Streamer's thumbnail avatar
            - `size`: Resolution size (e.g., 1280x720)

    - `extra`:
      - `now`: Server timestamp
      - `search_request_id`: Search request unique ID

    Args:
        body (LiveSearchV2Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
