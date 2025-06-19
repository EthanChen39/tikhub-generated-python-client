from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.challenge_search_v1_request import ChallengeSearchV1Request
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: ChallengeSearchV1Request,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/search/fetch_challenge_search_v1",
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
    body: ChallengeSearchV1Request,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取话题搜索 V1/Fetch hashtag search V1

     # [中文]
    ### 用途:
    - 获取抖音 App 中的话题（挑战/标签）搜索结果。
    - 根据关键词返回关联的话题列表，包含话题热度、封面、参与人数等信息。

    ### 备注:
    - 仅返回话题类型内容。
    - 初次请求时 `cursor` 传 0，`search_id` 传空字符串。
    - 翻页查询时使用上次响应返回的 `cursor` 和 `search_id`。

    ### 参数:
    - keyword: 搜索关键词，例如 \"美食\"
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
        \"keyword\": \"美食\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 0,
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `cursor`: 翻页游标（用于下次请求）
    - `has_more`: 是否还有更多数据（1=有，0=无）
    - `challenge_list[]`: 话题列表
      - `challenge_info`:
        - `cid`: 话题ID
        - `cha_name`: 话题名称（如 \"#美食探店\"）
        - `desc`: 话题描述（通常为空）
        - `schema`: 抖音内部跳转链接（schema协议）
        - `share_info`:
          - `share_url`: 话题分享H5链接
          - `share_title`: 分享标题
          - `share_desc`: 分享描述
        - `view_count`: 话题总浏览量
        - `user_count`: 话题参与人数
        - `hashtag_profile`: 话题封面图URL
        - `challenge_status`: 话题状态（1=正常，0=异常）
      - `author`:
        - `uid`: 创建者用户ID
        - `nickname`: 创建者昵称
        - `follower_count`: 粉丝数量
        - `is_verified`: 是否认证
        - `region`: 地区
        - `avatar_thumb.url_list`: 小头像URL列表
        - `avatar_medium.url_list`: 中头像URL列表
        - `avatar_larger.url_list`: 高清头像URL列表

    - `extra`:
      - `now`: 当前服务器时间戳（毫秒）
      - `search_request_id`: 搜索请求唯一ID

    # [English]
    ### Purpose:
    - Fetch hashtag/challenge search results from Douyin App.
    - Returns related hashtag topics including name, view count, participants, and cover images.

    ### Notes:
    - Only hashtag type content is returned.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - For pagination, use `cursor` and `search_id` from the last response.

    ### Parameters:
    - keyword: Search keyword, e.g., \"food\"
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
        \"keyword\": \"food\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 0,
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `cursor`: Cursor for next page
    - `has_more`: Whether more results are available (1=Yes, 0=No)
    - `challenge_list[]`: List of hashtags
      - `challenge_info`:
        - `cid`: Challenge ID
        - `cha_name`: Challenge name (e.g., \"#FoodHunt\")
        - `desc`: Challenge description
        - `schema`: Deep link for Douyin App
        - `share_info`:
          - `share_url`: H5 shareable link
          - `share_title`: Share title
          - `share_desc`: Share description
        - `view_count`: Total view count
        - `user_count`: Total participant count
        - `hashtag_profile`: Cover image URL
        - `challenge_status`: Challenge status (1=Normal, 0=Abnormal)
      - `author`:
        - `uid`: Author's user ID
        - `nickname`: Author's nickname
        - `follower_count`: Follower count
        - `is_verified`: Verified status
        - `region`: Region
        - `avatar_thumb.url_list`: Thumbnail avatar URLs
        - `avatar_medium.url_list`: Medium avatar URLs
        - `avatar_larger.url_list`: Large avatar URLs

    - `extra`:
      - `now`: Server timestamp
      - `search_request_id`: Unique search session ID

    Args:
        body (ChallengeSearchV1Request):

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
    body: ChallengeSearchV1Request,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取话题搜索 V1/Fetch hashtag search V1

     # [中文]
    ### 用途:
    - 获取抖音 App 中的话题（挑战/标签）搜索结果。
    - 根据关键词返回关联的话题列表，包含话题热度、封面、参与人数等信息。

    ### 备注:
    - 仅返回话题类型内容。
    - 初次请求时 `cursor` 传 0，`search_id` 传空字符串。
    - 翻页查询时使用上次响应返回的 `cursor` 和 `search_id`。

    ### 参数:
    - keyword: 搜索关键词，例如 \"美食\"
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
        \"keyword\": \"美食\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 0,
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `cursor`: 翻页游标（用于下次请求）
    - `has_more`: 是否还有更多数据（1=有，0=无）
    - `challenge_list[]`: 话题列表
      - `challenge_info`:
        - `cid`: 话题ID
        - `cha_name`: 话题名称（如 \"#美食探店\"）
        - `desc`: 话题描述（通常为空）
        - `schema`: 抖音内部跳转链接（schema协议）
        - `share_info`:
          - `share_url`: 话题分享H5链接
          - `share_title`: 分享标题
          - `share_desc`: 分享描述
        - `view_count`: 话题总浏览量
        - `user_count`: 话题参与人数
        - `hashtag_profile`: 话题封面图URL
        - `challenge_status`: 话题状态（1=正常，0=异常）
      - `author`:
        - `uid`: 创建者用户ID
        - `nickname`: 创建者昵称
        - `follower_count`: 粉丝数量
        - `is_verified`: 是否认证
        - `region`: 地区
        - `avatar_thumb.url_list`: 小头像URL列表
        - `avatar_medium.url_list`: 中头像URL列表
        - `avatar_larger.url_list`: 高清头像URL列表

    - `extra`:
      - `now`: 当前服务器时间戳（毫秒）
      - `search_request_id`: 搜索请求唯一ID

    # [English]
    ### Purpose:
    - Fetch hashtag/challenge search results from Douyin App.
    - Returns related hashtag topics including name, view count, participants, and cover images.

    ### Notes:
    - Only hashtag type content is returned.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - For pagination, use `cursor` and `search_id` from the last response.

    ### Parameters:
    - keyword: Search keyword, e.g., \"food\"
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
        \"keyword\": \"food\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 0,
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `cursor`: Cursor for next page
    - `has_more`: Whether more results are available (1=Yes, 0=No)
    - `challenge_list[]`: List of hashtags
      - `challenge_info`:
        - `cid`: Challenge ID
        - `cha_name`: Challenge name (e.g., \"#FoodHunt\")
        - `desc`: Challenge description
        - `schema`: Deep link for Douyin App
        - `share_info`:
          - `share_url`: H5 shareable link
          - `share_title`: Share title
          - `share_desc`: Share description
        - `view_count`: Total view count
        - `user_count`: Total participant count
        - `hashtag_profile`: Cover image URL
        - `challenge_status`: Challenge status (1=Normal, 0=Abnormal)
      - `author`:
        - `uid`: Author's user ID
        - `nickname`: Author's nickname
        - `follower_count`: Follower count
        - `is_verified`: Verified status
        - `region`: Region
        - `avatar_thumb.url_list`: Thumbnail avatar URLs
        - `avatar_medium.url_list`: Medium avatar URLs
        - `avatar_larger.url_list`: Large avatar URLs

    - `extra`:
      - `now`: Server timestamp
      - `search_request_id`: Unique search session ID

    Args:
        body (ChallengeSearchV1Request):

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
    body: ChallengeSearchV1Request,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取话题搜索 V1/Fetch hashtag search V1

     # [中文]
    ### 用途:
    - 获取抖音 App 中的话题（挑战/标签）搜索结果。
    - 根据关键词返回关联的话题列表，包含话题热度、封面、参与人数等信息。

    ### 备注:
    - 仅返回话题类型内容。
    - 初次请求时 `cursor` 传 0，`search_id` 传空字符串。
    - 翻页查询时使用上次响应返回的 `cursor` 和 `search_id`。

    ### 参数:
    - keyword: 搜索关键词，例如 \"美食\"
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
        \"keyword\": \"美食\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 0,
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `cursor`: 翻页游标（用于下次请求）
    - `has_more`: 是否还有更多数据（1=有，0=无）
    - `challenge_list[]`: 话题列表
      - `challenge_info`:
        - `cid`: 话题ID
        - `cha_name`: 话题名称（如 \"#美食探店\"）
        - `desc`: 话题描述（通常为空）
        - `schema`: 抖音内部跳转链接（schema协议）
        - `share_info`:
          - `share_url`: 话题分享H5链接
          - `share_title`: 分享标题
          - `share_desc`: 分享描述
        - `view_count`: 话题总浏览量
        - `user_count`: 话题参与人数
        - `hashtag_profile`: 话题封面图URL
        - `challenge_status`: 话题状态（1=正常，0=异常）
      - `author`:
        - `uid`: 创建者用户ID
        - `nickname`: 创建者昵称
        - `follower_count`: 粉丝数量
        - `is_verified`: 是否认证
        - `region`: 地区
        - `avatar_thumb.url_list`: 小头像URL列表
        - `avatar_medium.url_list`: 中头像URL列表
        - `avatar_larger.url_list`: 高清头像URL列表

    - `extra`:
      - `now`: 当前服务器时间戳（毫秒）
      - `search_request_id`: 搜索请求唯一ID

    # [English]
    ### Purpose:
    - Fetch hashtag/challenge search results from Douyin App.
    - Returns related hashtag topics including name, view count, participants, and cover images.

    ### Notes:
    - Only hashtag type content is returned.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - For pagination, use `cursor` and `search_id` from the last response.

    ### Parameters:
    - keyword: Search keyword, e.g., \"food\"
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
        \"keyword\": \"food\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 0,
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `cursor`: Cursor for next page
    - `has_more`: Whether more results are available (1=Yes, 0=No)
    - `challenge_list[]`: List of hashtags
      - `challenge_info`:
        - `cid`: Challenge ID
        - `cha_name`: Challenge name (e.g., \"#FoodHunt\")
        - `desc`: Challenge description
        - `schema`: Deep link for Douyin App
        - `share_info`:
          - `share_url`: H5 shareable link
          - `share_title`: Share title
          - `share_desc`: Share description
        - `view_count`: Total view count
        - `user_count`: Total participant count
        - `hashtag_profile`: Cover image URL
        - `challenge_status`: Challenge status (1=Normal, 0=Abnormal)
      - `author`:
        - `uid`: Author's user ID
        - `nickname`: Author's nickname
        - `follower_count`: Follower count
        - `is_verified`: Verified status
        - `region`: Region
        - `avatar_thumb.url_list`: Thumbnail avatar URLs
        - `avatar_medium.url_list`: Medium avatar URLs
        - `avatar_larger.url_list`: Large avatar URLs

    - `extra`:
      - `now`: Server timestamp
      - `search_request_id`: Unique search session ID

    Args:
        body (ChallengeSearchV1Request):

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
    body: ChallengeSearchV1Request,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取话题搜索 V1/Fetch hashtag search V1

     # [中文]
    ### 用途:
    - 获取抖音 App 中的话题（挑战/标签）搜索结果。
    - 根据关键词返回关联的话题列表，包含话题热度、封面、参与人数等信息。

    ### 备注:
    - 仅返回话题类型内容。
    - 初次请求时 `cursor` 传 0，`search_id` 传空字符串。
    - 翻页查询时使用上次响应返回的 `cursor` 和 `search_id`。

    ### 参数:
    - keyword: 搜索关键词，例如 \"美食\"
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
        \"keyword\": \"美食\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 0,
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `cursor`: 翻页游标（用于下次请求）
    - `has_more`: 是否还有更多数据（1=有，0=无）
    - `challenge_list[]`: 话题列表
      - `challenge_info`:
        - `cid`: 话题ID
        - `cha_name`: 话题名称（如 \"#美食探店\"）
        - `desc`: 话题描述（通常为空）
        - `schema`: 抖音内部跳转链接（schema协议）
        - `share_info`:
          - `share_url`: 话题分享H5链接
          - `share_title`: 分享标题
          - `share_desc`: 分享描述
        - `view_count`: 话题总浏览量
        - `user_count`: 话题参与人数
        - `hashtag_profile`: 话题封面图URL
        - `challenge_status`: 话题状态（1=正常，0=异常）
      - `author`:
        - `uid`: 创建者用户ID
        - `nickname`: 创建者昵称
        - `follower_count`: 粉丝数量
        - `is_verified`: 是否认证
        - `region`: 地区
        - `avatar_thumb.url_list`: 小头像URL列表
        - `avatar_medium.url_list`: 中头像URL列表
        - `avatar_larger.url_list`: 高清头像URL列表

    - `extra`:
      - `now`: 当前服务器时间戳（毫秒）
      - `search_request_id`: 搜索请求唯一ID

    # [English]
    ### Purpose:
    - Fetch hashtag/challenge search results from Douyin App.
    - Returns related hashtag topics including name, view count, participants, and cover images.

    ### Notes:
    - Only hashtag type content is returned.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - For pagination, use `cursor` and `search_id` from the last response.

    ### Parameters:
    - keyword: Search keyword, e.g., \"food\"
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
        \"keyword\": \"food\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 0,
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `cursor`: Cursor for next page
    - `has_more`: Whether more results are available (1=Yes, 0=No)
    - `challenge_list[]`: List of hashtags
      - `challenge_info`:
        - `cid`: Challenge ID
        - `cha_name`: Challenge name (e.g., \"#FoodHunt\")
        - `desc`: Challenge description
        - `schema`: Deep link for Douyin App
        - `share_info`:
          - `share_url`: H5 shareable link
          - `share_title`: Share title
          - `share_desc`: Share description
        - `view_count`: Total view count
        - `user_count`: Total participant count
        - `hashtag_profile`: Cover image URL
        - `challenge_status`: Challenge status (1=Normal, 0=Abnormal)
      - `author`:
        - `uid`: Author's user ID
        - `nickname`: Author's nickname
        - `follower_count`: Follower count
        - `is_verified`: Verified status
        - `region`: Region
        - `avatar_thumb.url_list`: Thumbnail avatar URLs
        - `avatar_medium.url_list`: Medium avatar URLs
        - `avatar_larger.url_list`: Large avatar URLs

    - `extra`:
      - `now`: Server timestamp
      - `search_request_id`: Unique search session ID

    Args:
        body (ChallengeSearchV1Request):

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
