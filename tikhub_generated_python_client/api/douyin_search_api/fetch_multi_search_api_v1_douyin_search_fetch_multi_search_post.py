from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.multi_search_request import MultiSearchRequest
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: MultiSearchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/search/fetch_multi_search",
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
    body: MultiSearchRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取多重搜索/Fetch multi-type search

     # [中文]
    ### 用途:
    - 获取抖音 App 中多种类型（视频、用户、音乐、话题等）的综合搜索结果。

    ### 备注:
    - 初次请求 `cursor` 传 0，`search_id` 传空字符串。
    - 返回内容丰富，适合搭建搜索聚合页、推荐页等场景。

    ### 参数:
    - keyword: 搜索关键词，如 \"人工智能\"
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
        \"keyword\": \"人工智能\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"0\",
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `cursor`: 下一页翻页游标
    - `has_more`: 是否还有更多数据（1=有，0=无）
    - `business_data[]`: 搜索结果列表
      - `data_id`: 结果数据编号
      - `type`: 结果类型
        - `1`: 视频（aweme_info）
        - `2`: 用户（user_info）
        - `4`: 音乐（music_info）
        - `6`: 话题（cha_info）
      - `data`: 具体数据内容，按type类型解析
        - 如果 type = 1（视频）:
          - `aweme_info`:
            - `aweme_id`: 视频ID
            - `desc`: 视频描述
            - `author`: 作者信息
              - `uid`: 用户ID
              - `nickname`: 用户昵称
              - `avatar_thumb.url_list`: 小头像
              - `is_verified`: 是否认证
              - `region`: 地区
            - `music`: 音乐信息
              - `id_str`: 音乐ID
              - `title`: 音乐标题
            - `video`: 视频播放与封面信息
              - `play_addr.url_list`: 播放地址
              - `cover.url_list`: 封面
              - `duration`: 视频时长（毫秒）
            - `statistics`:
              - `comment_count`: 评论数
              - `digg_count`: 点赞数
              - `share_count`: 分享数
              - `play_count`: 播放数
            - `status`:
              - `is_delete`: 是否被删除
              - `is_private`: 是否私密
            - `share_url`: 视频外链
        - 如果 type = 2（用户）:
          - `user_info`:
            - `uid`: 用户ID
            - `nickname`: 用户昵称
            - `signature`: 个人签名
            - `follower_count`: 粉丝数
            - `avatar_thumb.url_list`: 小头像
            - `region`: 地区
            - `is_verified`: 是否认证
        - 如果 type = 4（音乐）:
          - `music_info`:
            - `id_str`: 音乐ID
            - `title`: 音乐标题
            - `author`: 作者名
            - `play_url.url_list`: 播放地址
        - 如果 type = 6（话题）:
          - `cha_info`:
            - `cha_name`: 话题名
            - `desc`: 话题描述
            - `share_url`: 话题分享链接
            - `user_count`: 话题参与人数
            - `view_count`: 话题浏览次数

    - `extra`:
      - `now`: 当前服务器时间戳
      - `logid`: 请求日志ID

    # [English]
    ### Purpose:
    - Fetch multiple types of search results (videos, users, music, hashtags, etc.) from Douyin App.

    ### Notes:
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - Suitable for search aggregation pages, discovery modules, and recommendations.

    ### Parameters:
    - keyword: Search keyword, e.g., \"Artificial Intelligence\"
    - cursor: Pagination cursor (0 for the first page, use the last response cursor for subsequent
    pages)
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
        - `0-1`: Within 1 minute
        - `1-5`: 1 to 5 minutes
        - `5-10000`: More than 5 minutes
    - content_type: Content type filter
        - `0`: Unlimited
        - `1`: Video
        - `2`: Picture
        - `3`: Article
    - search_id: Search ID used for pagination

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"Artificial Intelligence\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"0\",
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `cursor`: Cursor for the next page
    - `has_more`: Whether there are more results (1=Yes, 0=No)
    - `business_data[]`: List of search result items
      - `data_id`: Data ID
      - `type`: Result type
        - `1`: Video (aweme_info)
        - `2`: User (user_info)
        - `4`: Music (music_info)
        - `6`: Hashtag (cha_info)
      - `data`: Content depending on `type`
        - if type = 1 (video):
          - `aweme_info`: Detailed video info
        - if type = 2 (user):
          - `user_info`: Detailed user info
        - if type = 4 (music):
          - `music_info`: Music details
        - if type = 6 (hashtag):
          - `cha_info`: Hashtag details

    - `extra`:
      - `now`: Current server timestamp
      - `logid`: Request log ID

    Args:
        body (MultiSearchRequest):

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
    body: MultiSearchRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取多重搜索/Fetch multi-type search

     # [中文]
    ### 用途:
    - 获取抖音 App 中多种类型（视频、用户、音乐、话题等）的综合搜索结果。

    ### 备注:
    - 初次请求 `cursor` 传 0，`search_id` 传空字符串。
    - 返回内容丰富，适合搭建搜索聚合页、推荐页等场景。

    ### 参数:
    - keyword: 搜索关键词，如 \"人工智能\"
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
        \"keyword\": \"人工智能\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"0\",
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `cursor`: 下一页翻页游标
    - `has_more`: 是否还有更多数据（1=有，0=无）
    - `business_data[]`: 搜索结果列表
      - `data_id`: 结果数据编号
      - `type`: 结果类型
        - `1`: 视频（aweme_info）
        - `2`: 用户（user_info）
        - `4`: 音乐（music_info）
        - `6`: 话题（cha_info）
      - `data`: 具体数据内容，按type类型解析
        - 如果 type = 1（视频）:
          - `aweme_info`:
            - `aweme_id`: 视频ID
            - `desc`: 视频描述
            - `author`: 作者信息
              - `uid`: 用户ID
              - `nickname`: 用户昵称
              - `avatar_thumb.url_list`: 小头像
              - `is_verified`: 是否认证
              - `region`: 地区
            - `music`: 音乐信息
              - `id_str`: 音乐ID
              - `title`: 音乐标题
            - `video`: 视频播放与封面信息
              - `play_addr.url_list`: 播放地址
              - `cover.url_list`: 封面
              - `duration`: 视频时长（毫秒）
            - `statistics`:
              - `comment_count`: 评论数
              - `digg_count`: 点赞数
              - `share_count`: 分享数
              - `play_count`: 播放数
            - `status`:
              - `is_delete`: 是否被删除
              - `is_private`: 是否私密
            - `share_url`: 视频外链
        - 如果 type = 2（用户）:
          - `user_info`:
            - `uid`: 用户ID
            - `nickname`: 用户昵称
            - `signature`: 个人签名
            - `follower_count`: 粉丝数
            - `avatar_thumb.url_list`: 小头像
            - `region`: 地区
            - `is_verified`: 是否认证
        - 如果 type = 4（音乐）:
          - `music_info`:
            - `id_str`: 音乐ID
            - `title`: 音乐标题
            - `author`: 作者名
            - `play_url.url_list`: 播放地址
        - 如果 type = 6（话题）:
          - `cha_info`:
            - `cha_name`: 话题名
            - `desc`: 话题描述
            - `share_url`: 话题分享链接
            - `user_count`: 话题参与人数
            - `view_count`: 话题浏览次数

    - `extra`:
      - `now`: 当前服务器时间戳
      - `logid`: 请求日志ID

    # [English]
    ### Purpose:
    - Fetch multiple types of search results (videos, users, music, hashtags, etc.) from Douyin App.

    ### Notes:
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - Suitable for search aggregation pages, discovery modules, and recommendations.

    ### Parameters:
    - keyword: Search keyword, e.g., \"Artificial Intelligence\"
    - cursor: Pagination cursor (0 for the first page, use the last response cursor for subsequent
    pages)
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
        - `0-1`: Within 1 minute
        - `1-5`: 1 to 5 minutes
        - `5-10000`: More than 5 minutes
    - content_type: Content type filter
        - `0`: Unlimited
        - `1`: Video
        - `2`: Picture
        - `3`: Article
    - search_id: Search ID used for pagination

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"Artificial Intelligence\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"0\",
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `cursor`: Cursor for the next page
    - `has_more`: Whether there are more results (1=Yes, 0=No)
    - `business_data[]`: List of search result items
      - `data_id`: Data ID
      - `type`: Result type
        - `1`: Video (aweme_info)
        - `2`: User (user_info)
        - `4`: Music (music_info)
        - `6`: Hashtag (cha_info)
      - `data`: Content depending on `type`
        - if type = 1 (video):
          - `aweme_info`: Detailed video info
        - if type = 2 (user):
          - `user_info`: Detailed user info
        - if type = 4 (music):
          - `music_info`: Music details
        - if type = 6 (hashtag):
          - `cha_info`: Hashtag details

    - `extra`:
      - `now`: Current server timestamp
      - `logid`: Request log ID

    Args:
        body (MultiSearchRequest):

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
    body: MultiSearchRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取多重搜索/Fetch multi-type search

     # [中文]
    ### 用途:
    - 获取抖音 App 中多种类型（视频、用户、音乐、话题等）的综合搜索结果。

    ### 备注:
    - 初次请求 `cursor` 传 0，`search_id` 传空字符串。
    - 返回内容丰富，适合搭建搜索聚合页、推荐页等场景。

    ### 参数:
    - keyword: 搜索关键词，如 \"人工智能\"
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
        \"keyword\": \"人工智能\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"0\",
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `cursor`: 下一页翻页游标
    - `has_more`: 是否还有更多数据（1=有，0=无）
    - `business_data[]`: 搜索结果列表
      - `data_id`: 结果数据编号
      - `type`: 结果类型
        - `1`: 视频（aweme_info）
        - `2`: 用户（user_info）
        - `4`: 音乐（music_info）
        - `6`: 话题（cha_info）
      - `data`: 具体数据内容，按type类型解析
        - 如果 type = 1（视频）:
          - `aweme_info`:
            - `aweme_id`: 视频ID
            - `desc`: 视频描述
            - `author`: 作者信息
              - `uid`: 用户ID
              - `nickname`: 用户昵称
              - `avatar_thumb.url_list`: 小头像
              - `is_verified`: 是否认证
              - `region`: 地区
            - `music`: 音乐信息
              - `id_str`: 音乐ID
              - `title`: 音乐标题
            - `video`: 视频播放与封面信息
              - `play_addr.url_list`: 播放地址
              - `cover.url_list`: 封面
              - `duration`: 视频时长（毫秒）
            - `statistics`:
              - `comment_count`: 评论数
              - `digg_count`: 点赞数
              - `share_count`: 分享数
              - `play_count`: 播放数
            - `status`:
              - `is_delete`: 是否被删除
              - `is_private`: 是否私密
            - `share_url`: 视频外链
        - 如果 type = 2（用户）:
          - `user_info`:
            - `uid`: 用户ID
            - `nickname`: 用户昵称
            - `signature`: 个人签名
            - `follower_count`: 粉丝数
            - `avatar_thumb.url_list`: 小头像
            - `region`: 地区
            - `is_verified`: 是否认证
        - 如果 type = 4（音乐）:
          - `music_info`:
            - `id_str`: 音乐ID
            - `title`: 音乐标题
            - `author`: 作者名
            - `play_url.url_list`: 播放地址
        - 如果 type = 6（话题）:
          - `cha_info`:
            - `cha_name`: 话题名
            - `desc`: 话题描述
            - `share_url`: 话题分享链接
            - `user_count`: 话题参与人数
            - `view_count`: 话题浏览次数

    - `extra`:
      - `now`: 当前服务器时间戳
      - `logid`: 请求日志ID

    # [English]
    ### Purpose:
    - Fetch multiple types of search results (videos, users, music, hashtags, etc.) from Douyin App.

    ### Notes:
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - Suitable for search aggregation pages, discovery modules, and recommendations.

    ### Parameters:
    - keyword: Search keyword, e.g., \"Artificial Intelligence\"
    - cursor: Pagination cursor (0 for the first page, use the last response cursor for subsequent
    pages)
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
        - `0-1`: Within 1 minute
        - `1-5`: 1 to 5 minutes
        - `5-10000`: More than 5 minutes
    - content_type: Content type filter
        - `0`: Unlimited
        - `1`: Video
        - `2`: Picture
        - `3`: Article
    - search_id: Search ID used for pagination

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"Artificial Intelligence\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"0\",
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `cursor`: Cursor for the next page
    - `has_more`: Whether there are more results (1=Yes, 0=No)
    - `business_data[]`: List of search result items
      - `data_id`: Data ID
      - `type`: Result type
        - `1`: Video (aweme_info)
        - `2`: User (user_info)
        - `4`: Music (music_info)
        - `6`: Hashtag (cha_info)
      - `data`: Content depending on `type`
        - if type = 1 (video):
          - `aweme_info`: Detailed video info
        - if type = 2 (user):
          - `user_info`: Detailed user info
        - if type = 4 (music):
          - `music_info`: Music details
        - if type = 6 (hashtag):
          - `cha_info`: Hashtag details

    - `extra`:
      - `now`: Current server timestamp
      - `logid`: Request log ID

    Args:
        body (MultiSearchRequest):

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
    body: MultiSearchRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取多重搜索/Fetch multi-type search

     # [中文]
    ### 用途:
    - 获取抖音 App 中多种类型（视频、用户、音乐、话题等）的综合搜索结果。

    ### 备注:
    - 初次请求 `cursor` 传 0，`search_id` 传空字符串。
    - 返回内容丰富，适合搭建搜索聚合页、推荐页等场景。

    ### 参数:
    - keyword: 搜索关键词，如 \"人工智能\"
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
        \"keyword\": \"人工智能\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"0\",
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `cursor`: 下一页翻页游标
    - `has_more`: 是否还有更多数据（1=有，0=无）
    - `business_data[]`: 搜索结果列表
      - `data_id`: 结果数据编号
      - `type`: 结果类型
        - `1`: 视频（aweme_info）
        - `2`: 用户（user_info）
        - `4`: 音乐（music_info）
        - `6`: 话题（cha_info）
      - `data`: 具体数据内容，按type类型解析
        - 如果 type = 1（视频）:
          - `aweme_info`:
            - `aweme_id`: 视频ID
            - `desc`: 视频描述
            - `author`: 作者信息
              - `uid`: 用户ID
              - `nickname`: 用户昵称
              - `avatar_thumb.url_list`: 小头像
              - `is_verified`: 是否认证
              - `region`: 地区
            - `music`: 音乐信息
              - `id_str`: 音乐ID
              - `title`: 音乐标题
            - `video`: 视频播放与封面信息
              - `play_addr.url_list`: 播放地址
              - `cover.url_list`: 封面
              - `duration`: 视频时长（毫秒）
            - `statistics`:
              - `comment_count`: 评论数
              - `digg_count`: 点赞数
              - `share_count`: 分享数
              - `play_count`: 播放数
            - `status`:
              - `is_delete`: 是否被删除
              - `is_private`: 是否私密
            - `share_url`: 视频外链
        - 如果 type = 2（用户）:
          - `user_info`:
            - `uid`: 用户ID
            - `nickname`: 用户昵称
            - `signature`: 个人签名
            - `follower_count`: 粉丝数
            - `avatar_thumb.url_list`: 小头像
            - `region`: 地区
            - `is_verified`: 是否认证
        - 如果 type = 4（音乐）:
          - `music_info`:
            - `id_str`: 音乐ID
            - `title`: 音乐标题
            - `author`: 作者名
            - `play_url.url_list`: 播放地址
        - 如果 type = 6（话题）:
          - `cha_info`:
            - `cha_name`: 话题名
            - `desc`: 话题描述
            - `share_url`: 话题分享链接
            - `user_count`: 话题参与人数
            - `view_count`: 话题浏览次数

    - `extra`:
      - `now`: 当前服务器时间戳
      - `logid`: 请求日志ID

    # [English]
    ### Purpose:
    - Fetch multiple types of search results (videos, users, music, hashtags, etc.) from Douyin App.

    ### Notes:
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - Suitable for search aggregation pages, discovery modules, and recommendations.

    ### Parameters:
    - keyword: Search keyword, e.g., \"Artificial Intelligence\"
    - cursor: Pagination cursor (0 for the first page, use the last response cursor for subsequent
    pages)
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
        - `0-1`: Within 1 minute
        - `1-5`: 1 to 5 minutes
        - `5-10000`: More than 5 minutes
    - content_type: Content type filter
        - `0`: Unlimited
        - `1`: Video
        - `2`: Picture
        - `3`: Article
    - search_id: Search ID used for pagination

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"Artificial Intelligence\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"0\",
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `cursor`: Cursor for the next page
    - `has_more`: Whether there are more results (1=Yes, 0=No)
    - `business_data[]`: List of search result items
      - `data_id`: Data ID
      - `type`: Result type
        - `1`: Video (aweme_info)
        - `2`: User (user_info)
        - `4`: Music (music_info)
        - `6`: Hashtag (cha_info)
      - `data`: Content depending on `type`
        - if type = 1 (video):
          - `aweme_info`: Detailed video info
        - if type = 2 (user):
          - `user_info`: Detailed user info
        - if type = 4 (music):
          - `music_info`: Music details
        - if type = 6 (hashtag):
          - `cha_info`: Hashtag details

    - `extra`:
      - `now`: Current server timestamp
      - `logid`: Request log ID

    Args:
        body (MultiSearchRequest):

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
