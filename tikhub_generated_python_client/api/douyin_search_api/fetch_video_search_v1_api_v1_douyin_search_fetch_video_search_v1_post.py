from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...models.video_search_v1_request import VideoSearchV1Request
from ...types import Response


def _get_kwargs(
    *,
    body: VideoSearchV1Request,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/search/fetch_video_search_v1",
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
    body: VideoSearchV1Request,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频搜索 V1/Fetch video search V1

     # [中文]
    ### 用途:
    - 获取抖音 App 中通过关键词搜索到的视频内容。
    - 专注于视频内容的搜索结果，不包含其他类型。

    ### 备注:
    - 初次请求时 `cursor` 传 0，`search_id` 传空字符串。
    - 返回的视频包含作者信息、播放地址、封面、互动数据等。
    - 同时返回一组关键词推荐 (`guide_search_words`) 用于引导用户继续搜索。

    ### 参数:
    - keyword: 搜索关键词，例如 \"人工智能\"
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

    #### 请求体示例：
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
    - `status_code`: 响应状态码（0表示成功）
    - `cursor`: 下一页的游标
    - `has_more`: 是否还有更多数据（1=有，0=没有）
    - `data[]`: 搜索到的视频内容列表
      - `type`: 结果类型（通常为 `1`）
      - `aweme_info`: 视频详细信息
        - 基本信息:
          - `aweme_id`: 视频ID
          - `desc`: 视频描述文字
          - `create_time`: 发布时间（时间戳）
        - 作者信息 (`author`):
          - `uid`: 用户ID
          - `nickname`: 昵称
          - `is_verified`: 是否认证
          - `region`: 地区，如 \"CN\"
          - `avatar_thumb.url_list`: 缩略头像列表
          - `follower_count`: 粉丝数
          - `enterprise_verify_reason`: 企业认证信息（如\"央视新闻\"）
        - 音乐信息 (`music`):
          - `id_str`: 音乐ID
          - `title`: 音乐标题
          - `author`: 音乐作者
          - `play_url.url_list`: 音乐播放链接
        - 视频播放信息 (`video`):
          - `play_addr.url_list`: 视频播放地址（高清）
          - `cover.url_list`: 视频封面
          - `dynamic_cover.url_list`: 动态封面
          - `origin_cover.url_list`: 原始封面
          - `ratio`: 视频分辨率，如 \"720p\"
          - `duration`: 视频时长（单位：毫秒）
          - `bit_rate[]`: 不同清晰度播放源
            - `gear_name`: 清晰度名称（如\"540_2_2\"）
            - `bit_rate`: 比特率
            - `play_addr.url_list`: 对应播放地址
        - 互动数据 (`statistics`):
          - `comment_count`: 评论数
          - `digg_count`: 点赞数
          - `share_count`: 分享数
          - `play_count`: 播放次数
        - 视频状态 (`status`):
          - `is_delete`: 是否删除
          - `is_private`: 是否私密
          - `allow_share`: 是否允许分享
          - `allow_comment`: 是否允许评论
        - 其他字段:
          - `share_url`: 视频分享外链
          - `user_digged`: 用户是否点赞（0=未点赞，1=已点赞）

    - `guide_search_words[]`: 推荐的搜索关键词
      - `id`: 推荐词ID
      - `word`: 推荐的关键词内容
      - `type`: 推荐类型（通常为 `recom`）
      - `query_id`: 推荐请求ID

    - `extra`:
      - `now`: 当前服务器时间戳（毫秒）
      - `logid`: 日志ID

    # [English]
    ### Purpose:
    - Fetch video content search results from Douyin App based on a keyword.
    - This API is focused on video search results only.

    ### Notes:
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - Each returned video includes rich details: author, video info, music, statistics, etc.
    - Also returns a set of suggested keywords (`guide_search_words`) for user guidance.

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
    - `status_code`: Response status code (0 = success)
    - `cursor`: Cursor for the next page
    - `has_more`: Whether more data is available (1=Yes, 0=No)
    - `data[]`: List of video search results
      - `type`: Result type (usually `1`)
      - `aweme_info`: Detailed video information
        - Basic info:
          - `aweme_id`: Video ID
          - `desc`: Description
          - `create_time`: Publish timestamp
        - Author (`author`):
          - `uid`: User ID
          - `nickname`: Nickname
          - `is_verified`: Whether verified
          - `region`: Region
          - `avatar_thumb.url_list`: Thumbnail avatars
          - `follower_count`: Follower count
          - `enterprise_verify_reason`: Enterprise verification reason
        - Music (`music`):
          - `id_str`: Music ID
          - `title`: Music title
          - `author`: Music creator
          - `play_url.url_list`: Music play URLs
        - Video (`video`):
          - `play_addr.url_list`: Play URLs
          - `cover.url_list`: Cover images
          - `dynamic_cover.url_list`: Dynamic covers
          - `origin_cover.url_list`: Original covers
          - `ratio`: Resolution, e.g., \"720p\"
          - `duration`: Video duration (ms)
          - `bit_rate[]`: Multiple resolution sources
            - `gear_name`: Gear name
            - `bit_rate`: Bit rate
            - `play_addr.url_list`: Play URLs
        - Statistics (`statistics`):
          - `comment_count`: Number of comments
          - `digg_count`: Number of likes
          - `share_count`: Number of shares
          - `play_count`: Number of plays
        - Status (`status`):
          - `is_delete`: Whether deleted
          - `is_private`: Whether private
          - `allow_share`: Whether sharing is allowed
          - `allow_comment`: Whether commenting is allowed
        - Other fields:
          - `share_url`: External share link
          - `user_digged`: Whether liked (0=No, 1=Yes)

    - `guide_search_words[]`: Suggested keywords
      - `id`: Suggestion ID
      - `word`: Suggested keyword
      - `type`: Suggestion type (usually `recom`)
      - `query_id`: Suggestion query ID

    - `extra`:
      - `now`: Current server timestamp
      - `logid`: Log ID

    Args:
        body (VideoSearchV1Request):

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
    body: VideoSearchV1Request,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频搜索 V1/Fetch video search V1

     # [中文]
    ### 用途:
    - 获取抖音 App 中通过关键词搜索到的视频内容。
    - 专注于视频内容的搜索结果，不包含其他类型。

    ### 备注:
    - 初次请求时 `cursor` 传 0，`search_id` 传空字符串。
    - 返回的视频包含作者信息、播放地址、封面、互动数据等。
    - 同时返回一组关键词推荐 (`guide_search_words`) 用于引导用户继续搜索。

    ### 参数:
    - keyword: 搜索关键词，例如 \"人工智能\"
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

    #### 请求体示例：
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
    - `status_code`: 响应状态码（0表示成功）
    - `cursor`: 下一页的游标
    - `has_more`: 是否还有更多数据（1=有，0=没有）
    - `data[]`: 搜索到的视频内容列表
      - `type`: 结果类型（通常为 `1`）
      - `aweme_info`: 视频详细信息
        - 基本信息:
          - `aweme_id`: 视频ID
          - `desc`: 视频描述文字
          - `create_time`: 发布时间（时间戳）
        - 作者信息 (`author`):
          - `uid`: 用户ID
          - `nickname`: 昵称
          - `is_verified`: 是否认证
          - `region`: 地区，如 \"CN\"
          - `avatar_thumb.url_list`: 缩略头像列表
          - `follower_count`: 粉丝数
          - `enterprise_verify_reason`: 企业认证信息（如\"央视新闻\"）
        - 音乐信息 (`music`):
          - `id_str`: 音乐ID
          - `title`: 音乐标题
          - `author`: 音乐作者
          - `play_url.url_list`: 音乐播放链接
        - 视频播放信息 (`video`):
          - `play_addr.url_list`: 视频播放地址（高清）
          - `cover.url_list`: 视频封面
          - `dynamic_cover.url_list`: 动态封面
          - `origin_cover.url_list`: 原始封面
          - `ratio`: 视频分辨率，如 \"720p\"
          - `duration`: 视频时长（单位：毫秒）
          - `bit_rate[]`: 不同清晰度播放源
            - `gear_name`: 清晰度名称（如\"540_2_2\"）
            - `bit_rate`: 比特率
            - `play_addr.url_list`: 对应播放地址
        - 互动数据 (`statistics`):
          - `comment_count`: 评论数
          - `digg_count`: 点赞数
          - `share_count`: 分享数
          - `play_count`: 播放次数
        - 视频状态 (`status`):
          - `is_delete`: 是否删除
          - `is_private`: 是否私密
          - `allow_share`: 是否允许分享
          - `allow_comment`: 是否允许评论
        - 其他字段:
          - `share_url`: 视频分享外链
          - `user_digged`: 用户是否点赞（0=未点赞，1=已点赞）

    - `guide_search_words[]`: 推荐的搜索关键词
      - `id`: 推荐词ID
      - `word`: 推荐的关键词内容
      - `type`: 推荐类型（通常为 `recom`）
      - `query_id`: 推荐请求ID

    - `extra`:
      - `now`: 当前服务器时间戳（毫秒）
      - `logid`: 日志ID

    # [English]
    ### Purpose:
    - Fetch video content search results from Douyin App based on a keyword.
    - This API is focused on video search results only.

    ### Notes:
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - Each returned video includes rich details: author, video info, music, statistics, etc.
    - Also returns a set of suggested keywords (`guide_search_words`) for user guidance.

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
    - `status_code`: Response status code (0 = success)
    - `cursor`: Cursor for the next page
    - `has_more`: Whether more data is available (1=Yes, 0=No)
    - `data[]`: List of video search results
      - `type`: Result type (usually `1`)
      - `aweme_info`: Detailed video information
        - Basic info:
          - `aweme_id`: Video ID
          - `desc`: Description
          - `create_time`: Publish timestamp
        - Author (`author`):
          - `uid`: User ID
          - `nickname`: Nickname
          - `is_verified`: Whether verified
          - `region`: Region
          - `avatar_thumb.url_list`: Thumbnail avatars
          - `follower_count`: Follower count
          - `enterprise_verify_reason`: Enterprise verification reason
        - Music (`music`):
          - `id_str`: Music ID
          - `title`: Music title
          - `author`: Music creator
          - `play_url.url_list`: Music play URLs
        - Video (`video`):
          - `play_addr.url_list`: Play URLs
          - `cover.url_list`: Cover images
          - `dynamic_cover.url_list`: Dynamic covers
          - `origin_cover.url_list`: Original covers
          - `ratio`: Resolution, e.g., \"720p\"
          - `duration`: Video duration (ms)
          - `bit_rate[]`: Multiple resolution sources
            - `gear_name`: Gear name
            - `bit_rate`: Bit rate
            - `play_addr.url_list`: Play URLs
        - Statistics (`statistics`):
          - `comment_count`: Number of comments
          - `digg_count`: Number of likes
          - `share_count`: Number of shares
          - `play_count`: Number of plays
        - Status (`status`):
          - `is_delete`: Whether deleted
          - `is_private`: Whether private
          - `allow_share`: Whether sharing is allowed
          - `allow_comment`: Whether commenting is allowed
        - Other fields:
          - `share_url`: External share link
          - `user_digged`: Whether liked (0=No, 1=Yes)

    - `guide_search_words[]`: Suggested keywords
      - `id`: Suggestion ID
      - `word`: Suggested keyword
      - `type`: Suggestion type (usually `recom`)
      - `query_id`: Suggestion query ID

    - `extra`:
      - `now`: Current server timestamp
      - `logid`: Log ID

    Args:
        body (VideoSearchV1Request):

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
    body: VideoSearchV1Request,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频搜索 V1/Fetch video search V1

     # [中文]
    ### 用途:
    - 获取抖音 App 中通过关键词搜索到的视频内容。
    - 专注于视频内容的搜索结果，不包含其他类型。

    ### 备注:
    - 初次请求时 `cursor` 传 0，`search_id` 传空字符串。
    - 返回的视频包含作者信息、播放地址、封面、互动数据等。
    - 同时返回一组关键词推荐 (`guide_search_words`) 用于引导用户继续搜索。

    ### 参数:
    - keyword: 搜索关键词，例如 \"人工智能\"
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

    #### 请求体示例：
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
    - `status_code`: 响应状态码（0表示成功）
    - `cursor`: 下一页的游标
    - `has_more`: 是否还有更多数据（1=有，0=没有）
    - `data[]`: 搜索到的视频内容列表
      - `type`: 结果类型（通常为 `1`）
      - `aweme_info`: 视频详细信息
        - 基本信息:
          - `aweme_id`: 视频ID
          - `desc`: 视频描述文字
          - `create_time`: 发布时间（时间戳）
        - 作者信息 (`author`):
          - `uid`: 用户ID
          - `nickname`: 昵称
          - `is_verified`: 是否认证
          - `region`: 地区，如 \"CN\"
          - `avatar_thumb.url_list`: 缩略头像列表
          - `follower_count`: 粉丝数
          - `enterprise_verify_reason`: 企业认证信息（如\"央视新闻\"）
        - 音乐信息 (`music`):
          - `id_str`: 音乐ID
          - `title`: 音乐标题
          - `author`: 音乐作者
          - `play_url.url_list`: 音乐播放链接
        - 视频播放信息 (`video`):
          - `play_addr.url_list`: 视频播放地址（高清）
          - `cover.url_list`: 视频封面
          - `dynamic_cover.url_list`: 动态封面
          - `origin_cover.url_list`: 原始封面
          - `ratio`: 视频分辨率，如 \"720p\"
          - `duration`: 视频时长（单位：毫秒）
          - `bit_rate[]`: 不同清晰度播放源
            - `gear_name`: 清晰度名称（如\"540_2_2\"）
            - `bit_rate`: 比特率
            - `play_addr.url_list`: 对应播放地址
        - 互动数据 (`statistics`):
          - `comment_count`: 评论数
          - `digg_count`: 点赞数
          - `share_count`: 分享数
          - `play_count`: 播放次数
        - 视频状态 (`status`):
          - `is_delete`: 是否删除
          - `is_private`: 是否私密
          - `allow_share`: 是否允许分享
          - `allow_comment`: 是否允许评论
        - 其他字段:
          - `share_url`: 视频分享外链
          - `user_digged`: 用户是否点赞（0=未点赞，1=已点赞）

    - `guide_search_words[]`: 推荐的搜索关键词
      - `id`: 推荐词ID
      - `word`: 推荐的关键词内容
      - `type`: 推荐类型（通常为 `recom`）
      - `query_id`: 推荐请求ID

    - `extra`:
      - `now`: 当前服务器时间戳（毫秒）
      - `logid`: 日志ID

    # [English]
    ### Purpose:
    - Fetch video content search results from Douyin App based on a keyword.
    - This API is focused on video search results only.

    ### Notes:
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - Each returned video includes rich details: author, video info, music, statistics, etc.
    - Also returns a set of suggested keywords (`guide_search_words`) for user guidance.

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
    - `status_code`: Response status code (0 = success)
    - `cursor`: Cursor for the next page
    - `has_more`: Whether more data is available (1=Yes, 0=No)
    - `data[]`: List of video search results
      - `type`: Result type (usually `1`)
      - `aweme_info`: Detailed video information
        - Basic info:
          - `aweme_id`: Video ID
          - `desc`: Description
          - `create_time`: Publish timestamp
        - Author (`author`):
          - `uid`: User ID
          - `nickname`: Nickname
          - `is_verified`: Whether verified
          - `region`: Region
          - `avatar_thumb.url_list`: Thumbnail avatars
          - `follower_count`: Follower count
          - `enterprise_verify_reason`: Enterprise verification reason
        - Music (`music`):
          - `id_str`: Music ID
          - `title`: Music title
          - `author`: Music creator
          - `play_url.url_list`: Music play URLs
        - Video (`video`):
          - `play_addr.url_list`: Play URLs
          - `cover.url_list`: Cover images
          - `dynamic_cover.url_list`: Dynamic covers
          - `origin_cover.url_list`: Original covers
          - `ratio`: Resolution, e.g., \"720p\"
          - `duration`: Video duration (ms)
          - `bit_rate[]`: Multiple resolution sources
            - `gear_name`: Gear name
            - `bit_rate`: Bit rate
            - `play_addr.url_list`: Play URLs
        - Statistics (`statistics`):
          - `comment_count`: Number of comments
          - `digg_count`: Number of likes
          - `share_count`: Number of shares
          - `play_count`: Number of plays
        - Status (`status`):
          - `is_delete`: Whether deleted
          - `is_private`: Whether private
          - `allow_share`: Whether sharing is allowed
          - `allow_comment`: Whether commenting is allowed
        - Other fields:
          - `share_url`: External share link
          - `user_digged`: Whether liked (0=No, 1=Yes)

    - `guide_search_words[]`: Suggested keywords
      - `id`: Suggestion ID
      - `word`: Suggested keyword
      - `type`: Suggestion type (usually `recom`)
      - `query_id`: Suggestion query ID

    - `extra`:
      - `now`: Current server timestamp
      - `logid`: Log ID

    Args:
        body (VideoSearchV1Request):

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
    body: VideoSearchV1Request,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频搜索 V1/Fetch video search V1

     # [中文]
    ### 用途:
    - 获取抖音 App 中通过关键词搜索到的视频内容。
    - 专注于视频内容的搜索结果，不包含其他类型。

    ### 备注:
    - 初次请求时 `cursor` 传 0，`search_id` 传空字符串。
    - 返回的视频包含作者信息、播放地址、封面、互动数据等。
    - 同时返回一组关键词推荐 (`guide_search_words`) 用于引导用户继续搜索。

    ### 参数:
    - keyword: 搜索关键词，例如 \"人工智能\"
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

    #### 请求体示例：
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
    - `status_code`: 响应状态码（0表示成功）
    - `cursor`: 下一页的游标
    - `has_more`: 是否还有更多数据（1=有，0=没有）
    - `data[]`: 搜索到的视频内容列表
      - `type`: 结果类型（通常为 `1`）
      - `aweme_info`: 视频详细信息
        - 基本信息:
          - `aweme_id`: 视频ID
          - `desc`: 视频描述文字
          - `create_time`: 发布时间（时间戳）
        - 作者信息 (`author`):
          - `uid`: 用户ID
          - `nickname`: 昵称
          - `is_verified`: 是否认证
          - `region`: 地区，如 \"CN\"
          - `avatar_thumb.url_list`: 缩略头像列表
          - `follower_count`: 粉丝数
          - `enterprise_verify_reason`: 企业认证信息（如\"央视新闻\"）
        - 音乐信息 (`music`):
          - `id_str`: 音乐ID
          - `title`: 音乐标题
          - `author`: 音乐作者
          - `play_url.url_list`: 音乐播放链接
        - 视频播放信息 (`video`):
          - `play_addr.url_list`: 视频播放地址（高清）
          - `cover.url_list`: 视频封面
          - `dynamic_cover.url_list`: 动态封面
          - `origin_cover.url_list`: 原始封面
          - `ratio`: 视频分辨率，如 \"720p\"
          - `duration`: 视频时长（单位：毫秒）
          - `bit_rate[]`: 不同清晰度播放源
            - `gear_name`: 清晰度名称（如\"540_2_2\"）
            - `bit_rate`: 比特率
            - `play_addr.url_list`: 对应播放地址
        - 互动数据 (`statistics`):
          - `comment_count`: 评论数
          - `digg_count`: 点赞数
          - `share_count`: 分享数
          - `play_count`: 播放次数
        - 视频状态 (`status`):
          - `is_delete`: 是否删除
          - `is_private`: 是否私密
          - `allow_share`: 是否允许分享
          - `allow_comment`: 是否允许评论
        - 其他字段:
          - `share_url`: 视频分享外链
          - `user_digged`: 用户是否点赞（0=未点赞，1=已点赞）

    - `guide_search_words[]`: 推荐的搜索关键词
      - `id`: 推荐词ID
      - `word`: 推荐的关键词内容
      - `type`: 推荐类型（通常为 `recom`）
      - `query_id`: 推荐请求ID

    - `extra`:
      - `now`: 当前服务器时间戳（毫秒）
      - `logid`: 日志ID

    # [English]
    ### Purpose:
    - Fetch video content search results from Douyin App based on a keyword.
    - This API is focused on video search results only.

    ### Notes:
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - Each returned video includes rich details: author, video info, music, statistics, etc.
    - Also returns a set of suggested keywords (`guide_search_words`) for user guidance.

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
    - `status_code`: Response status code (0 = success)
    - `cursor`: Cursor for the next page
    - `has_more`: Whether more data is available (1=Yes, 0=No)
    - `data[]`: List of video search results
      - `type`: Result type (usually `1`)
      - `aweme_info`: Detailed video information
        - Basic info:
          - `aweme_id`: Video ID
          - `desc`: Description
          - `create_time`: Publish timestamp
        - Author (`author`):
          - `uid`: User ID
          - `nickname`: Nickname
          - `is_verified`: Whether verified
          - `region`: Region
          - `avatar_thumb.url_list`: Thumbnail avatars
          - `follower_count`: Follower count
          - `enterprise_verify_reason`: Enterprise verification reason
        - Music (`music`):
          - `id_str`: Music ID
          - `title`: Music title
          - `author`: Music creator
          - `play_url.url_list`: Music play URLs
        - Video (`video`):
          - `play_addr.url_list`: Play URLs
          - `cover.url_list`: Cover images
          - `dynamic_cover.url_list`: Dynamic covers
          - `origin_cover.url_list`: Original covers
          - `ratio`: Resolution, e.g., \"720p\"
          - `duration`: Video duration (ms)
          - `bit_rate[]`: Multiple resolution sources
            - `gear_name`: Gear name
            - `bit_rate`: Bit rate
            - `play_addr.url_list`: Play URLs
        - Statistics (`statistics`):
          - `comment_count`: Number of comments
          - `digg_count`: Number of likes
          - `share_count`: Number of shares
          - `play_count`: Number of plays
        - Status (`status`):
          - `is_delete`: Whether deleted
          - `is_private`: Whether private
          - `allow_share`: Whether sharing is allowed
          - `allow_comment`: Whether commenting is allowed
        - Other fields:
          - `share_url`: External share link
          - `user_digged`: Whether liked (0=No, 1=Yes)

    - `guide_search_words[]`: Suggested keywords
      - `id`: Suggestion ID
      - `word`: Suggested keyword
      - `type`: Suggestion type (usually `recom`)
      - `query_id`: Suggestion query ID

    - `extra`:
      - `now`: Current server timestamp
      - `logid`: Log ID

    Args:
        body (VideoSearchV1Request):

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
