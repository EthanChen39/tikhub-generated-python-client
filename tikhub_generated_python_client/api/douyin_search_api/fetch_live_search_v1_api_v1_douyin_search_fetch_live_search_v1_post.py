from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.live_search_v1_request import LiveSearchV1Request
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: LiveSearchV1Request,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/search/fetch_live_search_v1",
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
    body: LiveSearchV1Request,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取直播搜索 V1/Fetch live search V1

     # [中文]
    ### 用途:
    - 获取抖音 App 中直播搜索结果。
    - 返回正在直播的房间信息，包括主播资料、直播间封面、观众人数、拉流地址等。

    ### 备注:
    - 仅返回直播类型内容。
    - 初次请求时 `cursor` 传0，`search_id` 传空字符串。
    - 翻页请求时，使用上一次响应返回的 `cursor` 和 `search_id`。

    ### 参数:
    - keyword: 搜索关键词，如 \"游戏\"
    - cursor: 翻页游标（首次请求传0）
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
    - content_type: 内容类型（固定传直播类型）
    - search_id: 搜索ID（翻页时使用）

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
    - `cursor`: 下一页游标
    - `has_more`: 是否有更多数据（1=有，0=无）
    - `data[]`: 直播房间列表
      - `type`: 返回内容类型（固定为1）
      - `lives`:
        - `aweme_id`: 直播对应的内容ID
        - `group_id`: 群组ID（与aweme_id类似，可用于跳转）
        - `author`:
          - `uid`: 主播用户ID
          - `nickname`: 主播昵称
          - `short_id`: 主播短ID
          - `avatar_thumb.url_list`: 缩略头像URL列表
          - `avatar_medium.url_list`: 中等头像URL列表
          - `avatar_larger.url_list`: 高清头像URL列表
          - `room_id`: 当前直播间ID
          - `room_cover.url_list`: 直播封面图URL列表
        - `video`:
          - `tags[]`: 直播标签（如“游戏”、“聊天”等）
            - `title`: 标签标题
            - `url.url_list`: 标签图标URL列表
        - `rawdata`: 直播详细数据（结构化JSON字符串，可解析得到以下信息）
          - `title`: 直播标题
          - `user_count`: 当前在线观众数
          - `stream_url`: 拉流信息
            - `flv_pull_url`: 拉流地址列表（不同清晰度）
              - `SD1`: 标清
              - `SD2`: 高清
              - `HD1`: 超清
              - `FULL_HD1`: 蓝光
              - `ORIGION`: 原画
            - `hls_pull_url`: HLS播放地址（部分直播间可能存在）
          - `cover.url_list`: 直播间封面图
          - `size`: 分辨率（如1920x1080）
          - `stats.total_user`: 在线观众数

    - `extra`:
      - `now`: 当前服务器时间戳
      - `logid`: 请求日志ID
      - `search_request_id`: 搜索请求唯一ID

    # [English]
    ### Purpose:
    - Fetch live stream search results from Douyin App.
    - Returns information about live rooms including streamer profile, cover image, viewer count, and
    stream URLs.

    ### Notes:
    - Only live streaming content is returned.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - Use the last response's `cursor` and `search_id` for pagination.

    ### Parameters:
    - keyword: Search keyword, e.g., \"games\"
    - cursor: Pagination cursor (0 for first request)
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
    - `has_more`: Whether there are more results (1=Yes, 0=No)
    - `data[]`: List of live stream rooms
      - `type`: Result type (fixed to 1)
      - `lives`:
        - `aweme_id`: Related content ID
        - `group_id`: Group ID
        - `author`:
          - `uid`: Streamer's user ID
          - `nickname`: Streamer's nickname
          - `short_id`: Streamer's short ID
          - `avatar_thumb.url_list`: Thumbnail avatar URLs
          - `avatar_medium.url_list`: Medium avatar URLs
          - `avatar_larger.url_list`: Large avatar URLs
          - `room_id`: Room ID
          - `room_cover.url_list`: Room cover image URLs
        - `video`:
          - `tags[]`: Live tags (e.g., \"Gaming\", \"Chatting\")
            - `title`: Tag title
            - `url.url_list`: Tag icon URLs
        - `rawdata`: Raw live room data (as JSON string)
          - `title`: Live title
          - `user_count`: Current viewer count
          - `stream_url`: Stream URLs
            - `flv_pull_url`: FLV stream URLs by resolution
            - `hls_pull_url`: HLS stream URL (optional)
          - `cover.url_list`: Room cover image
          - `size`: Resolution (e.g., 1920x1080)
          - `stats.total_user`: Viewer count
    - `extra`:
      - `now`: Current server timestamp
      - `logid`: Request log ID
      - `search_request_id`: Unique search session ID

    Args:
        body (LiveSearchV1Request):

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
    body: LiveSearchV1Request,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取直播搜索 V1/Fetch live search V1

     # [中文]
    ### 用途:
    - 获取抖音 App 中直播搜索结果。
    - 返回正在直播的房间信息，包括主播资料、直播间封面、观众人数、拉流地址等。

    ### 备注:
    - 仅返回直播类型内容。
    - 初次请求时 `cursor` 传0，`search_id` 传空字符串。
    - 翻页请求时，使用上一次响应返回的 `cursor` 和 `search_id`。

    ### 参数:
    - keyword: 搜索关键词，如 \"游戏\"
    - cursor: 翻页游标（首次请求传0）
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
    - content_type: 内容类型（固定传直播类型）
    - search_id: 搜索ID（翻页时使用）

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
    - `cursor`: 下一页游标
    - `has_more`: 是否有更多数据（1=有，0=无）
    - `data[]`: 直播房间列表
      - `type`: 返回内容类型（固定为1）
      - `lives`:
        - `aweme_id`: 直播对应的内容ID
        - `group_id`: 群组ID（与aweme_id类似，可用于跳转）
        - `author`:
          - `uid`: 主播用户ID
          - `nickname`: 主播昵称
          - `short_id`: 主播短ID
          - `avatar_thumb.url_list`: 缩略头像URL列表
          - `avatar_medium.url_list`: 中等头像URL列表
          - `avatar_larger.url_list`: 高清头像URL列表
          - `room_id`: 当前直播间ID
          - `room_cover.url_list`: 直播封面图URL列表
        - `video`:
          - `tags[]`: 直播标签（如“游戏”、“聊天”等）
            - `title`: 标签标题
            - `url.url_list`: 标签图标URL列表
        - `rawdata`: 直播详细数据（结构化JSON字符串，可解析得到以下信息）
          - `title`: 直播标题
          - `user_count`: 当前在线观众数
          - `stream_url`: 拉流信息
            - `flv_pull_url`: 拉流地址列表（不同清晰度）
              - `SD1`: 标清
              - `SD2`: 高清
              - `HD1`: 超清
              - `FULL_HD1`: 蓝光
              - `ORIGION`: 原画
            - `hls_pull_url`: HLS播放地址（部分直播间可能存在）
          - `cover.url_list`: 直播间封面图
          - `size`: 分辨率（如1920x1080）
          - `stats.total_user`: 在线观众数

    - `extra`:
      - `now`: 当前服务器时间戳
      - `logid`: 请求日志ID
      - `search_request_id`: 搜索请求唯一ID

    # [English]
    ### Purpose:
    - Fetch live stream search results from Douyin App.
    - Returns information about live rooms including streamer profile, cover image, viewer count, and
    stream URLs.

    ### Notes:
    - Only live streaming content is returned.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - Use the last response's `cursor` and `search_id` for pagination.

    ### Parameters:
    - keyword: Search keyword, e.g., \"games\"
    - cursor: Pagination cursor (0 for first request)
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
    - `has_more`: Whether there are more results (1=Yes, 0=No)
    - `data[]`: List of live stream rooms
      - `type`: Result type (fixed to 1)
      - `lives`:
        - `aweme_id`: Related content ID
        - `group_id`: Group ID
        - `author`:
          - `uid`: Streamer's user ID
          - `nickname`: Streamer's nickname
          - `short_id`: Streamer's short ID
          - `avatar_thumb.url_list`: Thumbnail avatar URLs
          - `avatar_medium.url_list`: Medium avatar URLs
          - `avatar_larger.url_list`: Large avatar URLs
          - `room_id`: Room ID
          - `room_cover.url_list`: Room cover image URLs
        - `video`:
          - `tags[]`: Live tags (e.g., \"Gaming\", \"Chatting\")
            - `title`: Tag title
            - `url.url_list`: Tag icon URLs
        - `rawdata`: Raw live room data (as JSON string)
          - `title`: Live title
          - `user_count`: Current viewer count
          - `stream_url`: Stream URLs
            - `flv_pull_url`: FLV stream URLs by resolution
            - `hls_pull_url`: HLS stream URL (optional)
          - `cover.url_list`: Room cover image
          - `size`: Resolution (e.g., 1920x1080)
          - `stats.total_user`: Viewer count
    - `extra`:
      - `now`: Current server timestamp
      - `logid`: Request log ID
      - `search_request_id`: Unique search session ID

    Args:
        body (LiveSearchV1Request):

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
    body: LiveSearchV1Request,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取直播搜索 V1/Fetch live search V1

     # [中文]
    ### 用途:
    - 获取抖音 App 中直播搜索结果。
    - 返回正在直播的房间信息，包括主播资料、直播间封面、观众人数、拉流地址等。

    ### 备注:
    - 仅返回直播类型内容。
    - 初次请求时 `cursor` 传0，`search_id` 传空字符串。
    - 翻页请求时，使用上一次响应返回的 `cursor` 和 `search_id`。

    ### 参数:
    - keyword: 搜索关键词，如 \"游戏\"
    - cursor: 翻页游标（首次请求传0）
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
    - content_type: 内容类型（固定传直播类型）
    - search_id: 搜索ID（翻页时使用）

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
    - `cursor`: 下一页游标
    - `has_more`: 是否有更多数据（1=有，0=无）
    - `data[]`: 直播房间列表
      - `type`: 返回内容类型（固定为1）
      - `lives`:
        - `aweme_id`: 直播对应的内容ID
        - `group_id`: 群组ID（与aweme_id类似，可用于跳转）
        - `author`:
          - `uid`: 主播用户ID
          - `nickname`: 主播昵称
          - `short_id`: 主播短ID
          - `avatar_thumb.url_list`: 缩略头像URL列表
          - `avatar_medium.url_list`: 中等头像URL列表
          - `avatar_larger.url_list`: 高清头像URL列表
          - `room_id`: 当前直播间ID
          - `room_cover.url_list`: 直播封面图URL列表
        - `video`:
          - `tags[]`: 直播标签（如“游戏”、“聊天”等）
            - `title`: 标签标题
            - `url.url_list`: 标签图标URL列表
        - `rawdata`: 直播详细数据（结构化JSON字符串，可解析得到以下信息）
          - `title`: 直播标题
          - `user_count`: 当前在线观众数
          - `stream_url`: 拉流信息
            - `flv_pull_url`: 拉流地址列表（不同清晰度）
              - `SD1`: 标清
              - `SD2`: 高清
              - `HD1`: 超清
              - `FULL_HD1`: 蓝光
              - `ORIGION`: 原画
            - `hls_pull_url`: HLS播放地址（部分直播间可能存在）
          - `cover.url_list`: 直播间封面图
          - `size`: 分辨率（如1920x1080）
          - `stats.total_user`: 在线观众数

    - `extra`:
      - `now`: 当前服务器时间戳
      - `logid`: 请求日志ID
      - `search_request_id`: 搜索请求唯一ID

    # [English]
    ### Purpose:
    - Fetch live stream search results from Douyin App.
    - Returns information about live rooms including streamer profile, cover image, viewer count, and
    stream URLs.

    ### Notes:
    - Only live streaming content is returned.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - Use the last response's `cursor` and `search_id` for pagination.

    ### Parameters:
    - keyword: Search keyword, e.g., \"games\"
    - cursor: Pagination cursor (0 for first request)
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
    - `has_more`: Whether there are more results (1=Yes, 0=No)
    - `data[]`: List of live stream rooms
      - `type`: Result type (fixed to 1)
      - `lives`:
        - `aweme_id`: Related content ID
        - `group_id`: Group ID
        - `author`:
          - `uid`: Streamer's user ID
          - `nickname`: Streamer's nickname
          - `short_id`: Streamer's short ID
          - `avatar_thumb.url_list`: Thumbnail avatar URLs
          - `avatar_medium.url_list`: Medium avatar URLs
          - `avatar_larger.url_list`: Large avatar URLs
          - `room_id`: Room ID
          - `room_cover.url_list`: Room cover image URLs
        - `video`:
          - `tags[]`: Live tags (e.g., \"Gaming\", \"Chatting\")
            - `title`: Tag title
            - `url.url_list`: Tag icon URLs
        - `rawdata`: Raw live room data (as JSON string)
          - `title`: Live title
          - `user_count`: Current viewer count
          - `stream_url`: Stream URLs
            - `flv_pull_url`: FLV stream URLs by resolution
            - `hls_pull_url`: HLS stream URL (optional)
          - `cover.url_list`: Room cover image
          - `size`: Resolution (e.g., 1920x1080)
          - `stats.total_user`: Viewer count
    - `extra`:
      - `now`: Current server timestamp
      - `logid`: Request log ID
      - `search_request_id`: Unique search session ID

    Args:
        body (LiveSearchV1Request):

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
    body: LiveSearchV1Request,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取直播搜索 V1/Fetch live search V1

     # [中文]
    ### 用途:
    - 获取抖音 App 中直播搜索结果。
    - 返回正在直播的房间信息，包括主播资料、直播间封面、观众人数、拉流地址等。

    ### 备注:
    - 仅返回直播类型内容。
    - 初次请求时 `cursor` 传0，`search_id` 传空字符串。
    - 翻页请求时，使用上一次响应返回的 `cursor` 和 `search_id`。

    ### 参数:
    - keyword: 搜索关键词，如 \"游戏\"
    - cursor: 翻页游标（首次请求传0）
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
    - content_type: 内容类型（固定传直播类型）
    - search_id: 搜索ID（翻页时使用）

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
    - `cursor`: 下一页游标
    - `has_more`: 是否有更多数据（1=有，0=无）
    - `data[]`: 直播房间列表
      - `type`: 返回内容类型（固定为1）
      - `lives`:
        - `aweme_id`: 直播对应的内容ID
        - `group_id`: 群组ID（与aweme_id类似，可用于跳转）
        - `author`:
          - `uid`: 主播用户ID
          - `nickname`: 主播昵称
          - `short_id`: 主播短ID
          - `avatar_thumb.url_list`: 缩略头像URL列表
          - `avatar_medium.url_list`: 中等头像URL列表
          - `avatar_larger.url_list`: 高清头像URL列表
          - `room_id`: 当前直播间ID
          - `room_cover.url_list`: 直播封面图URL列表
        - `video`:
          - `tags[]`: 直播标签（如“游戏”、“聊天”等）
            - `title`: 标签标题
            - `url.url_list`: 标签图标URL列表
        - `rawdata`: 直播详细数据（结构化JSON字符串，可解析得到以下信息）
          - `title`: 直播标题
          - `user_count`: 当前在线观众数
          - `stream_url`: 拉流信息
            - `flv_pull_url`: 拉流地址列表（不同清晰度）
              - `SD1`: 标清
              - `SD2`: 高清
              - `HD1`: 超清
              - `FULL_HD1`: 蓝光
              - `ORIGION`: 原画
            - `hls_pull_url`: HLS播放地址（部分直播间可能存在）
          - `cover.url_list`: 直播间封面图
          - `size`: 分辨率（如1920x1080）
          - `stats.total_user`: 在线观众数

    - `extra`:
      - `now`: 当前服务器时间戳
      - `logid`: 请求日志ID
      - `search_request_id`: 搜索请求唯一ID

    # [English]
    ### Purpose:
    - Fetch live stream search results from Douyin App.
    - Returns information about live rooms including streamer profile, cover image, viewer count, and
    stream URLs.

    ### Notes:
    - Only live streaming content is returned.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - Use the last response's `cursor` and `search_id` for pagination.

    ### Parameters:
    - keyword: Search keyword, e.g., \"games\"
    - cursor: Pagination cursor (0 for first request)
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
    - `has_more`: Whether there are more results (1=Yes, 0=No)
    - `data[]`: List of live stream rooms
      - `type`: Result type (fixed to 1)
      - `lives`:
        - `aweme_id`: Related content ID
        - `group_id`: Group ID
        - `author`:
          - `uid`: Streamer's user ID
          - `nickname`: Streamer's nickname
          - `short_id`: Streamer's short ID
          - `avatar_thumb.url_list`: Thumbnail avatar URLs
          - `avatar_medium.url_list`: Medium avatar URLs
          - `avatar_larger.url_list`: Large avatar URLs
          - `room_id`: Room ID
          - `room_cover.url_list`: Room cover image URLs
        - `video`:
          - `tags[]`: Live tags (e.g., \"Gaming\", \"Chatting\")
            - `title`: Tag title
            - `url.url_list`: Tag icon URLs
        - `rawdata`: Raw live room data (as JSON string)
          - `title`: Live title
          - `user_count`: Current viewer count
          - `stream_url`: Stream URLs
            - `flv_pull_url`: FLV stream URLs by resolution
            - `hls_pull_url`: HLS stream URL (optional)
          - `cover.url_list`: Room cover image
          - `size`: Resolution (e.g., 1920x1080)
          - `stats.total_user`: Viewer count
    - `extra`:
      - `now`: Current server timestamp
      - `logid`: Request log ID
      - `search_request_id`: Unique search session ID

    Args:
        body (LiveSearchV1Request):

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
