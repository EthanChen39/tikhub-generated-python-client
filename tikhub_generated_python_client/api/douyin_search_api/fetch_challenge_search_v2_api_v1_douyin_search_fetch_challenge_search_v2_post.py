from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.challenge_search_v2_request import ChallengeSearchV2Request
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: ChallengeSearchV2Request,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/search/fetch_challenge_search_v2",
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
    body: ChallengeSearchV2Request,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取话题搜索 V2/Fetch hashtag search V2

     # [中文]
    ### 用途:
    - 获取抖音 App 中话题(挑战/标签)搜索的结果，使用 V2 版本 API。
    - 支持关键词搜索，返回匹配的话题详情，包括话题名称、话题封面、浏览量、参与人数等。

    ### 备注:
    - 本接口专注于搜索话题（Challenge/Hashtag）内容，不包含视频或直播等其他类型。
    - 初次请求时 `cursor` 传入 0，`search_id` 传空字符串，后续翻页请使用上一次返回的 `cursor` 和 `search_id`。

    ### 参数:
    - keyword: 搜索关键词，如 \"游戏\"
    - cursor: 翻页游标（首次请求传 0，翻页时使用上次响应的 cursor）
    - sort_type: 排序方式
        - `0`: 综合排序
        - `1`: 最多点赞
        - `2`: 最新发布
    - publish_time: 发布时间筛选
        - `0`: 不限
        - `1`: 最近一天
        - `7`: 最近一周
        - `180`: 最近半年
    - filter_duration: 视频时长筛选
        - `0`: 不限
        - `0-1`: 1 分钟以内
        - `1-5`: 1-5 分钟
        - `5-10000`: 5 分钟以上
    - content_type: 内容类型筛选
        - `0`: 不限
        - `1`: 视频
        - `2`: 图片
        - `3`: 文章
    - search_id: 搜索ID（分页时使用）

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"游戏\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 0,
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `business_data`（话题搜索结果列表）
      - `data_id`: 结果的唯一编号
      - `type`: 数据类型（固定为 `2`）
      - `data.challenge_info`:
        - `cid`: 话题ID
        - `cha_name`: 话题名称
        - `desc`: 话题描述
        - `schema`: 话题跳转链接（aweme://开头，可跳转抖音 App 内话题详情）
        - `hashtag_profile`: 话题封面图 URL
        - `user_count`: 参与人数
        - `view_count`: 话题浏览量
        - `challenge_status`: 话题状态（1=正常，其他=异常）
        - `author`: 创建者信息
          - `uid`: 创建者抖音用户ID
          - `nickname`: 昵称
          - `avatar_thumb.url_list`: 缩略头像URL列表
          - `is_verified`: 是否认证
          - `follower_count`: 粉丝数
        - `share_info`:
          - `share_url`: 话题分享链接
          - `share_title`: 分享标题
          - `share_desc`: 分享描述

    # [English]
    ### Purpose:
    - Fetch hashtag/challenge search results from Douyin App using V2 API.
    - Supports searching by keyword and returns detailed challenge information, including name, cover
    image, view count, and participant count.

    ### Notes:
    - This API focuses on searching challenges (hashtags), not including videos or live streams.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request. For pagination, use
    the cursor and search_id from the last response.

    ### Parameters:
    - keyword: Search keyword, e.g., \"game\"
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
        - `0-1`: Under 1 minute
        - `1-5`: 1-5 minutes
        - `5-10000`: Over 5 minutes
    - content_type: Content type filter
        - `0`: Unlimited
        - `1`: Video
        - `2`: Image
        - `3`: Article
    - search_id: Search ID for pagination

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"game\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 0,
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `business_data` (list of hashtag search results)
      - `data_id`: Unique identifier for the result
      - `type`: Data type (fixed `2`)
      - `data.challenge_info`:
        - `cid`: Challenge ID
        - `cha_name`: Challenge name
        - `desc`: Challenge description
        - `schema`: Challenge detail schema link (aweme:// schema, used to deep link inside Douyin App)
        - `hashtag_profile`: URL of the hashtag cover image
        - `user_count`: Number of participants
        - `view_count`: Number of views
        - `challenge_status`: Status (1 = active, others = abnormal)
        - `author`: Creator info
          - `uid`: User ID
          - `nickname`: Nickname
          - `avatar_thumb.url_list`: Thumbnail avatar URLs
          - `is_verified`: Whether the creator is verified
          - `follower_count`: Number of followers
        - `share_info`:
          - `share_url`: Shareable URL
          - `share_title`: Title for sharing
          - `share_desc`: Description for sharing

    Args:
        body (ChallengeSearchV2Request):

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
    body: ChallengeSearchV2Request,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取话题搜索 V2/Fetch hashtag search V2

     # [中文]
    ### 用途:
    - 获取抖音 App 中话题(挑战/标签)搜索的结果，使用 V2 版本 API。
    - 支持关键词搜索，返回匹配的话题详情，包括话题名称、话题封面、浏览量、参与人数等。

    ### 备注:
    - 本接口专注于搜索话题（Challenge/Hashtag）内容，不包含视频或直播等其他类型。
    - 初次请求时 `cursor` 传入 0，`search_id` 传空字符串，后续翻页请使用上一次返回的 `cursor` 和 `search_id`。

    ### 参数:
    - keyword: 搜索关键词，如 \"游戏\"
    - cursor: 翻页游标（首次请求传 0，翻页时使用上次响应的 cursor）
    - sort_type: 排序方式
        - `0`: 综合排序
        - `1`: 最多点赞
        - `2`: 最新发布
    - publish_time: 发布时间筛选
        - `0`: 不限
        - `1`: 最近一天
        - `7`: 最近一周
        - `180`: 最近半年
    - filter_duration: 视频时长筛选
        - `0`: 不限
        - `0-1`: 1 分钟以内
        - `1-5`: 1-5 分钟
        - `5-10000`: 5 分钟以上
    - content_type: 内容类型筛选
        - `0`: 不限
        - `1`: 视频
        - `2`: 图片
        - `3`: 文章
    - search_id: 搜索ID（分页时使用）

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"游戏\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 0,
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `business_data`（话题搜索结果列表）
      - `data_id`: 结果的唯一编号
      - `type`: 数据类型（固定为 `2`）
      - `data.challenge_info`:
        - `cid`: 话题ID
        - `cha_name`: 话题名称
        - `desc`: 话题描述
        - `schema`: 话题跳转链接（aweme://开头，可跳转抖音 App 内话题详情）
        - `hashtag_profile`: 话题封面图 URL
        - `user_count`: 参与人数
        - `view_count`: 话题浏览量
        - `challenge_status`: 话题状态（1=正常，其他=异常）
        - `author`: 创建者信息
          - `uid`: 创建者抖音用户ID
          - `nickname`: 昵称
          - `avatar_thumb.url_list`: 缩略头像URL列表
          - `is_verified`: 是否认证
          - `follower_count`: 粉丝数
        - `share_info`:
          - `share_url`: 话题分享链接
          - `share_title`: 分享标题
          - `share_desc`: 分享描述

    # [English]
    ### Purpose:
    - Fetch hashtag/challenge search results from Douyin App using V2 API.
    - Supports searching by keyword and returns detailed challenge information, including name, cover
    image, view count, and participant count.

    ### Notes:
    - This API focuses on searching challenges (hashtags), not including videos or live streams.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request. For pagination, use
    the cursor and search_id from the last response.

    ### Parameters:
    - keyword: Search keyword, e.g., \"game\"
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
        - `0-1`: Under 1 minute
        - `1-5`: 1-5 minutes
        - `5-10000`: Over 5 minutes
    - content_type: Content type filter
        - `0`: Unlimited
        - `1`: Video
        - `2`: Image
        - `3`: Article
    - search_id: Search ID for pagination

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"game\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 0,
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `business_data` (list of hashtag search results)
      - `data_id`: Unique identifier for the result
      - `type`: Data type (fixed `2`)
      - `data.challenge_info`:
        - `cid`: Challenge ID
        - `cha_name`: Challenge name
        - `desc`: Challenge description
        - `schema`: Challenge detail schema link (aweme:// schema, used to deep link inside Douyin App)
        - `hashtag_profile`: URL of the hashtag cover image
        - `user_count`: Number of participants
        - `view_count`: Number of views
        - `challenge_status`: Status (1 = active, others = abnormal)
        - `author`: Creator info
          - `uid`: User ID
          - `nickname`: Nickname
          - `avatar_thumb.url_list`: Thumbnail avatar URLs
          - `is_verified`: Whether the creator is verified
          - `follower_count`: Number of followers
        - `share_info`:
          - `share_url`: Shareable URL
          - `share_title`: Title for sharing
          - `share_desc`: Description for sharing

    Args:
        body (ChallengeSearchV2Request):

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
    body: ChallengeSearchV2Request,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取话题搜索 V2/Fetch hashtag search V2

     # [中文]
    ### 用途:
    - 获取抖音 App 中话题(挑战/标签)搜索的结果，使用 V2 版本 API。
    - 支持关键词搜索，返回匹配的话题详情，包括话题名称、话题封面、浏览量、参与人数等。

    ### 备注:
    - 本接口专注于搜索话题（Challenge/Hashtag）内容，不包含视频或直播等其他类型。
    - 初次请求时 `cursor` 传入 0，`search_id` 传空字符串，后续翻页请使用上一次返回的 `cursor` 和 `search_id`。

    ### 参数:
    - keyword: 搜索关键词，如 \"游戏\"
    - cursor: 翻页游标（首次请求传 0，翻页时使用上次响应的 cursor）
    - sort_type: 排序方式
        - `0`: 综合排序
        - `1`: 最多点赞
        - `2`: 最新发布
    - publish_time: 发布时间筛选
        - `0`: 不限
        - `1`: 最近一天
        - `7`: 最近一周
        - `180`: 最近半年
    - filter_duration: 视频时长筛选
        - `0`: 不限
        - `0-1`: 1 分钟以内
        - `1-5`: 1-5 分钟
        - `5-10000`: 5 分钟以上
    - content_type: 内容类型筛选
        - `0`: 不限
        - `1`: 视频
        - `2`: 图片
        - `3`: 文章
    - search_id: 搜索ID（分页时使用）

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"游戏\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 0,
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `business_data`（话题搜索结果列表）
      - `data_id`: 结果的唯一编号
      - `type`: 数据类型（固定为 `2`）
      - `data.challenge_info`:
        - `cid`: 话题ID
        - `cha_name`: 话题名称
        - `desc`: 话题描述
        - `schema`: 话题跳转链接（aweme://开头，可跳转抖音 App 内话题详情）
        - `hashtag_profile`: 话题封面图 URL
        - `user_count`: 参与人数
        - `view_count`: 话题浏览量
        - `challenge_status`: 话题状态（1=正常，其他=异常）
        - `author`: 创建者信息
          - `uid`: 创建者抖音用户ID
          - `nickname`: 昵称
          - `avatar_thumb.url_list`: 缩略头像URL列表
          - `is_verified`: 是否认证
          - `follower_count`: 粉丝数
        - `share_info`:
          - `share_url`: 话题分享链接
          - `share_title`: 分享标题
          - `share_desc`: 分享描述

    # [English]
    ### Purpose:
    - Fetch hashtag/challenge search results from Douyin App using V2 API.
    - Supports searching by keyword and returns detailed challenge information, including name, cover
    image, view count, and participant count.

    ### Notes:
    - This API focuses on searching challenges (hashtags), not including videos or live streams.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request. For pagination, use
    the cursor and search_id from the last response.

    ### Parameters:
    - keyword: Search keyword, e.g., \"game\"
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
        - `0-1`: Under 1 minute
        - `1-5`: 1-5 minutes
        - `5-10000`: Over 5 minutes
    - content_type: Content type filter
        - `0`: Unlimited
        - `1`: Video
        - `2`: Image
        - `3`: Article
    - search_id: Search ID for pagination

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"game\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 0,
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `business_data` (list of hashtag search results)
      - `data_id`: Unique identifier for the result
      - `type`: Data type (fixed `2`)
      - `data.challenge_info`:
        - `cid`: Challenge ID
        - `cha_name`: Challenge name
        - `desc`: Challenge description
        - `schema`: Challenge detail schema link (aweme:// schema, used to deep link inside Douyin App)
        - `hashtag_profile`: URL of the hashtag cover image
        - `user_count`: Number of participants
        - `view_count`: Number of views
        - `challenge_status`: Status (1 = active, others = abnormal)
        - `author`: Creator info
          - `uid`: User ID
          - `nickname`: Nickname
          - `avatar_thumb.url_list`: Thumbnail avatar URLs
          - `is_verified`: Whether the creator is verified
          - `follower_count`: Number of followers
        - `share_info`:
          - `share_url`: Shareable URL
          - `share_title`: Title for sharing
          - `share_desc`: Description for sharing

    Args:
        body (ChallengeSearchV2Request):

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
    body: ChallengeSearchV2Request,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取话题搜索 V2/Fetch hashtag search V2

     # [中文]
    ### 用途:
    - 获取抖音 App 中话题(挑战/标签)搜索的结果，使用 V2 版本 API。
    - 支持关键词搜索，返回匹配的话题详情，包括话题名称、话题封面、浏览量、参与人数等。

    ### 备注:
    - 本接口专注于搜索话题（Challenge/Hashtag）内容，不包含视频或直播等其他类型。
    - 初次请求时 `cursor` 传入 0，`search_id` 传空字符串，后续翻页请使用上一次返回的 `cursor` 和 `search_id`。

    ### 参数:
    - keyword: 搜索关键词，如 \"游戏\"
    - cursor: 翻页游标（首次请求传 0，翻页时使用上次响应的 cursor）
    - sort_type: 排序方式
        - `0`: 综合排序
        - `1`: 最多点赞
        - `2`: 最新发布
    - publish_time: 发布时间筛选
        - `0`: 不限
        - `1`: 最近一天
        - `7`: 最近一周
        - `180`: 最近半年
    - filter_duration: 视频时长筛选
        - `0`: 不限
        - `0-1`: 1 分钟以内
        - `1-5`: 1-5 分钟
        - `5-10000`: 5 分钟以上
    - content_type: 内容类型筛选
        - `0`: 不限
        - `1`: 视频
        - `2`: 图片
        - `3`: 文章
    - search_id: 搜索ID（分页时使用）

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"游戏\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 0,
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `business_data`（话题搜索结果列表）
      - `data_id`: 结果的唯一编号
      - `type`: 数据类型（固定为 `2`）
      - `data.challenge_info`:
        - `cid`: 话题ID
        - `cha_name`: 话题名称
        - `desc`: 话题描述
        - `schema`: 话题跳转链接（aweme://开头，可跳转抖音 App 内话题详情）
        - `hashtag_profile`: 话题封面图 URL
        - `user_count`: 参与人数
        - `view_count`: 话题浏览量
        - `challenge_status`: 话题状态（1=正常，其他=异常）
        - `author`: 创建者信息
          - `uid`: 创建者抖音用户ID
          - `nickname`: 昵称
          - `avatar_thumb.url_list`: 缩略头像URL列表
          - `is_verified`: 是否认证
          - `follower_count`: 粉丝数
        - `share_info`:
          - `share_url`: 话题分享链接
          - `share_title`: 分享标题
          - `share_desc`: 分享描述

    # [English]
    ### Purpose:
    - Fetch hashtag/challenge search results from Douyin App using V2 API.
    - Supports searching by keyword and returns detailed challenge information, including name, cover
    image, view count, and participant count.

    ### Notes:
    - This API focuses on searching challenges (hashtags), not including videos or live streams.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request. For pagination, use
    the cursor and search_id from the last response.

    ### Parameters:
    - keyword: Search keyword, e.g., \"game\"
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
        - `0-1`: Under 1 minute
        - `1-5`: 1-5 minutes
        - `5-10000`: Over 5 minutes
    - content_type: Content type filter
        - `0`: Unlimited
        - `1`: Video
        - `2`: Image
        - `3`: Article
    - search_id: Search ID for pagination

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"game\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 0,
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `business_data` (list of hashtag search results)
      - `data_id`: Unique identifier for the result
      - `type`: Data type (fixed `2`)
      - `data.challenge_info`:
        - `cid`: Challenge ID
        - `cha_name`: Challenge name
        - `desc`: Challenge description
        - `schema`: Challenge detail schema link (aweme:// schema, used to deep link inside Douyin App)
        - `hashtag_profile`: URL of the hashtag cover image
        - `user_count`: Number of participants
        - `view_count`: Number of views
        - `challenge_status`: Status (1 = active, others = abnormal)
        - `author`: Creator info
          - `uid`: User ID
          - `nickname`: Nickname
          - `avatar_thumb.url_list`: Thumbnail avatar URLs
          - `is_verified`: Whether the creator is verified
          - `follower_count`: Number of followers
        - `share_info`:
          - `share_url`: Shareable URL
          - `share_title`: Title for sharing
          - `share_desc`: Description for sharing

    Args:
        body (ChallengeSearchV2Request):

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
