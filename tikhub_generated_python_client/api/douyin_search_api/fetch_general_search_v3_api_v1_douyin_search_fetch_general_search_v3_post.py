from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.general_search_v3_request import GeneralSearchV3Request
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: GeneralSearchV3Request,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/search/fetch_general_search_v3",
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
    body: GeneralSearchV3Request,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取综合搜索 V3/Fetch general search V3

     # [中文]
    ### 用途:
    - 获取抖音 App 综合搜索结果（V3版，数据更全）。
    - 支持关键词、排序方式、发布时间、时长、内容类型等筛选。
    - 支持翻页查询，通过 `cursor` 和 `search_id` 进行分页。

    ### 备注:
    - 初次请求时 `cursor` 传 0，`search_id` 传空字符串。
    - 返回数据极为详细，包括视频、作者、音乐、话题、播放源、互动统计等信息。

    ### 参数:
    - keyword: 搜索关键词，如 \"猫咪\"
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
    - filter_duration: 视频时长筛选
        - `0`: 不限
        - `0-1`: 1分钟以内
        - `1-5`: 1-5分钟
        - `5-10000`: 5分钟以上
    - content_type: 内容类型筛选
        - `0`: 不限
        - `1`: 视频
        - `2`: 图片
        - `3`: 文章
    - search_id: 搜索ID（分页时使用）

    ### 请求体示例：
    ```json
    payload = {
      \"keyword\": \"猫咪\",
      \"cursor\": 0,
      \"sort_type\": \"0\",
      \"publish_time\": \"0\",
      \"filter_duration\": \"0\",
      \"content_type\": \"0\",
      \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `status_code`: 响应状态码（0为成功）
    - `data[]`: 搜索结果列表
      - `type`: 结果类型（通常为 `1`）
      - `aweme_info`: 视频详细信息
        - 基本信息:
          - `aweme_id`: 视频ID
          - `desc`: 视频描述
          - `create_time`: 发布时间（时间戳）
        - 作者信息 (`author`):
          - `uid`: 用户ID
          - `nickname`: 昵称
          - `short_id`: 用户短ID
          - `signature`: 用户签名
          - `region`: 地区，如 \"CN\"
          - `is_verified`: 是否认证
          - `avatar_thumb.url_list`: 缩略头像
          - `avatar_medium.url_list`: 中等尺寸头像
          - `avatar_larger.url_list`: 高清头像
        - 音乐信息 (`music`):
          - `id_str`: 音乐ID
          - `title`: 音乐标题
          - `author`: 音乐作者
          - `play_url.url_list`: 音乐播放链接
          - `duration`: 音乐时长（秒）
          - `cover_hd.url_list`: 高清封面图
        - 话题标签 (`cha_list[]`):
          - `cha_name`: 话题名
          - `share_url`: 分享链接
        - 视频播放信息 (`video`):
          - `play_addr.url_list`: 视频播放链接
          - `cover.url_list`: 封面图片
          - `dynamic_cover.url_list`: 动态封面
          - `origin_cover.url_list`: 原始封面
          - `duration`: 视频时长（毫秒）
          - `ratio`: 分辨率比例（如 \"720p\"）
          - `bit_rate[]`: 多清晰度播放源
            - `gear_name`: 清晰度名称（如 \"adapt_540_2\"）
            - `bit_rate`: 码率
            - `play_addr.url_list`: 对应播放链接
        - 互动统计 (`statistics`):
          - `comment_count`: 评论数
          - `digg_count`: 点赞数
          - `share_count`: 分享数
          - `play_count`: 播放数
        - 视频状态 (`status`):
          - `is_delete`: 是否删除
          - `is_private`: 是否私密
          - `allow_share`: 是否允许分享
          - `allow_comment`: 是否允许评论
        - 其他字段:
          - `share_url`: 视频分享链接
          - `user_digged`: 是否已点赞（0=未点赞，1=已点赞）

    # [English]
    ### Purpose:
    - Fetch Douyin App general search results (V3 version, more comprehensive data).
    - Supports filtering by keyword, sort type, publish time, video duration, and content type.
    - Supports pagination via `cursor` and `search_id`.

    ### Notes:
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - The response is rich, including video, author, music, hashtags, multiple play sources, and
    statistics.

    ### Parameters:
    - keyword: Search keyword, e.g., \"cat\"
    - cursor: Pagination cursor (0 for the first page)
    - sort_type: Sort type
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
        - `5-10000`: Over 5 minutes
    - content_type: Content type filter
        - `0`: Unlimited
        - `1`: Video
        - `2`: Picture
        - `3`: Article
    - search_id: Search ID for pagination

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"cat\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"0\",
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `status_code`: Response status code (0 means success)
    - `data[]`: List of search results
      - `type`: Result type (usually `1`)
      - `aweme_info`: Video details
        - Basic Info:
          - `aweme_id`: Video ID
          - `desc`: Video description
          - `create_time`: Publish timestamp
        - Author (`author`):
          - `uid`: User ID
          - `nickname`: Nickname
          - `short_id`: Short ID
          - `signature`: Signature
          - `region`: Region
          - `is_verified`: Verified or not
          - `avatar_thumb.url_list`: Thumbnail avatar
          - `avatar_medium.url_list`: Medium avatar
          - `avatar_larger.url_list`: Large avatar
        - Music (`music`):
          - `id_str`: Music ID
          - `title`: Music title
          - `author`: Music creator
          - `play_url.url_list`: Music play URLs
          - `duration`: Music duration (seconds)
          - `cover_hd.url_list`: HD cover images
        - Hashtags (`cha_list[]`):
          - `cha_name`: Hashtag name
          - `share_url`: Share URL
        - Video (`video`):
          - `play_addr.url_list`: Video play URLs
          - `cover.url_list`: Cover images
          - `dynamic_cover.url_list`: Dynamic cover
          - `origin_cover.url_list`: Original cover
          - `duration`: Duration in milliseconds
          - `ratio`: Resolution (e.g., \"720p\")
          - `bit_rate[]`: Multiple quality sources
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
          - `allow_share`: Allow sharing or not
          - `allow_comment`: Allow commenting or not
        - Other fields:
          - `share_url`: External share URL
          - `user_digged`: Whether user liked (0=No, 1=Yes)

    Args:
        body (GeneralSearchV3Request):

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
    body: GeneralSearchV3Request,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取综合搜索 V3/Fetch general search V3

     # [中文]
    ### 用途:
    - 获取抖音 App 综合搜索结果（V3版，数据更全）。
    - 支持关键词、排序方式、发布时间、时长、内容类型等筛选。
    - 支持翻页查询，通过 `cursor` 和 `search_id` 进行分页。

    ### 备注:
    - 初次请求时 `cursor` 传 0，`search_id` 传空字符串。
    - 返回数据极为详细，包括视频、作者、音乐、话题、播放源、互动统计等信息。

    ### 参数:
    - keyword: 搜索关键词，如 \"猫咪\"
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
    - filter_duration: 视频时长筛选
        - `0`: 不限
        - `0-1`: 1分钟以内
        - `1-5`: 1-5分钟
        - `5-10000`: 5分钟以上
    - content_type: 内容类型筛选
        - `0`: 不限
        - `1`: 视频
        - `2`: 图片
        - `3`: 文章
    - search_id: 搜索ID（分页时使用）

    ### 请求体示例：
    ```json
    payload = {
      \"keyword\": \"猫咪\",
      \"cursor\": 0,
      \"sort_type\": \"0\",
      \"publish_time\": \"0\",
      \"filter_duration\": \"0\",
      \"content_type\": \"0\",
      \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `status_code`: 响应状态码（0为成功）
    - `data[]`: 搜索结果列表
      - `type`: 结果类型（通常为 `1`）
      - `aweme_info`: 视频详细信息
        - 基本信息:
          - `aweme_id`: 视频ID
          - `desc`: 视频描述
          - `create_time`: 发布时间（时间戳）
        - 作者信息 (`author`):
          - `uid`: 用户ID
          - `nickname`: 昵称
          - `short_id`: 用户短ID
          - `signature`: 用户签名
          - `region`: 地区，如 \"CN\"
          - `is_verified`: 是否认证
          - `avatar_thumb.url_list`: 缩略头像
          - `avatar_medium.url_list`: 中等尺寸头像
          - `avatar_larger.url_list`: 高清头像
        - 音乐信息 (`music`):
          - `id_str`: 音乐ID
          - `title`: 音乐标题
          - `author`: 音乐作者
          - `play_url.url_list`: 音乐播放链接
          - `duration`: 音乐时长（秒）
          - `cover_hd.url_list`: 高清封面图
        - 话题标签 (`cha_list[]`):
          - `cha_name`: 话题名
          - `share_url`: 分享链接
        - 视频播放信息 (`video`):
          - `play_addr.url_list`: 视频播放链接
          - `cover.url_list`: 封面图片
          - `dynamic_cover.url_list`: 动态封面
          - `origin_cover.url_list`: 原始封面
          - `duration`: 视频时长（毫秒）
          - `ratio`: 分辨率比例（如 \"720p\"）
          - `bit_rate[]`: 多清晰度播放源
            - `gear_name`: 清晰度名称（如 \"adapt_540_2\"）
            - `bit_rate`: 码率
            - `play_addr.url_list`: 对应播放链接
        - 互动统计 (`statistics`):
          - `comment_count`: 评论数
          - `digg_count`: 点赞数
          - `share_count`: 分享数
          - `play_count`: 播放数
        - 视频状态 (`status`):
          - `is_delete`: 是否删除
          - `is_private`: 是否私密
          - `allow_share`: 是否允许分享
          - `allow_comment`: 是否允许评论
        - 其他字段:
          - `share_url`: 视频分享链接
          - `user_digged`: 是否已点赞（0=未点赞，1=已点赞）

    # [English]
    ### Purpose:
    - Fetch Douyin App general search results (V3 version, more comprehensive data).
    - Supports filtering by keyword, sort type, publish time, video duration, and content type.
    - Supports pagination via `cursor` and `search_id`.

    ### Notes:
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - The response is rich, including video, author, music, hashtags, multiple play sources, and
    statistics.

    ### Parameters:
    - keyword: Search keyword, e.g., \"cat\"
    - cursor: Pagination cursor (0 for the first page)
    - sort_type: Sort type
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
        - `5-10000`: Over 5 minutes
    - content_type: Content type filter
        - `0`: Unlimited
        - `1`: Video
        - `2`: Picture
        - `3`: Article
    - search_id: Search ID for pagination

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"cat\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"0\",
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `status_code`: Response status code (0 means success)
    - `data[]`: List of search results
      - `type`: Result type (usually `1`)
      - `aweme_info`: Video details
        - Basic Info:
          - `aweme_id`: Video ID
          - `desc`: Video description
          - `create_time`: Publish timestamp
        - Author (`author`):
          - `uid`: User ID
          - `nickname`: Nickname
          - `short_id`: Short ID
          - `signature`: Signature
          - `region`: Region
          - `is_verified`: Verified or not
          - `avatar_thumb.url_list`: Thumbnail avatar
          - `avatar_medium.url_list`: Medium avatar
          - `avatar_larger.url_list`: Large avatar
        - Music (`music`):
          - `id_str`: Music ID
          - `title`: Music title
          - `author`: Music creator
          - `play_url.url_list`: Music play URLs
          - `duration`: Music duration (seconds)
          - `cover_hd.url_list`: HD cover images
        - Hashtags (`cha_list[]`):
          - `cha_name`: Hashtag name
          - `share_url`: Share URL
        - Video (`video`):
          - `play_addr.url_list`: Video play URLs
          - `cover.url_list`: Cover images
          - `dynamic_cover.url_list`: Dynamic cover
          - `origin_cover.url_list`: Original cover
          - `duration`: Duration in milliseconds
          - `ratio`: Resolution (e.g., \"720p\")
          - `bit_rate[]`: Multiple quality sources
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
          - `allow_share`: Allow sharing or not
          - `allow_comment`: Allow commenting or not
        - Other fields:
          - `share_url`: External share URL
          - `user_digged`: Whether user liked (0=No, 1=Yes)

    Args:
        body (GeneralSearchV3Request):

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
    body: GeneralSearchV3Request,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取综合搜索 V3/Fetch general search V3

     # [中文]
    ### 用途:
    - 获取抖音 App 综合搜索结果（V3版，数据更全）。
    - 支持关键词、排序方式、发布时间、时长、内容类型等筛选。
    - 支持翻页查询，通过 `cursor` 和 `search_id` 进行分页。

    ### 备注:
    - 初次请求时 `cursor` 传 0，`search_id` 传空字符串。
    - 返回数据极为详细，包括视频、作者、音乐、话题、播放源、互动统计等信息。

    ### 参数:
    - keyword: 搜索关键词，如 \"猫咪\"
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
    - filter_duration: 视频时长筛选
        - `0`: 不限
        - `0-1`: 1分钟以内
        - `1-5`: 1-5分钟
        - `5-10000`: 5分钟以上
    - content_type: 内容类型筛选
        - `0`: 不限
        - `1`: 视频
        - `2`: 图片
        - `3`: 文章
    - search_id: 搜索ID（分页时使用）

    ### 请求体示例：
    ```json
    payload = {
      \"keyword\": \"猫咪\",
      \"cursor\": 0,
      \"sort_type\": \"0\",
      \"publish_time\": \"0\",
      \"filter_duration\": \"0\",
      \"content_type\": \"0\",
      \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `status_code`: 响应状态码（0为成功）
    - `data[]`: 搜索结果列表
      - `type`: 结果类型（通常为 `1`）
      - `aweme_info`: 视频详细信息
        - 基本信息:
          - `aweme_id`: 视频ID
          - `desc`: 视频描述
          - `create_time`: 发布时间（时间戳）
        - 作者信息 (`author`):
          - `uid`: 用户ID
          - `nickname`: 昵称
          - `short_id`: 用户短ID
          - `signature`: 用户签名
          - `region`: 地区，如 \"CN\"
          - `is_verified`: 是否认证
          - `avatar_thumb.url_list`: 缩略头像
          - `avatar_medium.url_list`: 中等尺寸头像
          - `avatar_larger.url_list`: 高清头像
        - 音乐信息 (`music`):
          - `id_str`: 音乐ID
          - `title`: 音乐标题
          - `author`: 音乐作者
          - `play_url.url_list`: 音乐播放链接
          - `duration`: 音乐时长（秒）
          - `cover_hd.url_list`: 高清封面图
        - 话题标签 (`cha_list[]`):
          - `cha_name`: 话题名
          - `share_url`: 分享链接
        - 视频播放信息 (`video`):
          - `play_addr.url_list`: 视频播放链接
          - `cover.url_list`: 封面图片
          - `dynamic_cover.url_list`: 动态封面
          - `origin_cover.url_list`: 原始封面
          - `duration`: 视频时长（毫秒）
          - `ratio`: 分辨率比例（如 \"720p\"）
          - `bit_rate[]`: 多清晰度播放源
            - `gear_name`: 清晰度名称（如 \"adapt_540_2\"）
            - `bit_rate`: 码率
            - `play_addr.url_list`: 对应播放链接
        - 互动统计 (`statistics`):
          - `comment_count`: 评论数
          - `digg_count`: 点赞数
          - `share_count`: 分享数
          - `play_count`: 播放数
        - 视频状态 (`status`):
          - `is_delete`: 是否删除
          - `is_private`: 是否私密
          - `allow_share`: 是否允许分享
          - `allow_comment`: 是否允许评论
        - 其他字段:
          - `share_url`: 视频分享链接
          - `user_digged`: 是否已点赞（0=未点赞，1=已点赞）

    # [English]
    ### Purpose:
    - Fetch Douyin App general search results (V3 version, more comprehensive data).
    - Supports filtering by keyword, sort type, publish time, video duration, and content type.
    - Supports pagination via `cursor` and `search_id`.

    ### Notes:
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - The response is rich, including video, author, music, hashtags, multiple play sources, and
    statistics.

    ### Parameters:
    - keyword: Search keyword, e.g., \"cat\"
    - cursor: Pagination cursor (0 for the first page)
    - sort_type: Sort type
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
        - `5-10000`: Over 5 minutes
    - content_type: Content type filter
        - `0`: Unlimited
        - `1`: Video
        - `2`: Picture
        - `3`: Article
    - search_id: Search ID for pagination

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"cat\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"0\",
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `status_code`: Response status code (0 means success)
    - `data[]`: List of search results
      - `type`: Result type (usually `1`)
      - `aweme_info`: Video details
        - Basic Info:
          - `aweme_id`: Video ID
          - `desc`: Video description
          - `create_time`: Publish timestamp
        - Author (`author`):
          - `uid`: User ID
          - `nickname`: Nickname
          - `short_id`: Short ID
          - `signature`: Signature
          - `region`: Region
          - `is_verified`: Verified or not
          - `avatar_thumb.url_list`: Thumbnail avatar
          - `avatar_medium.url_list`: Medium avatar
          - `avatar_larger.url_list`: Large avatar
        - Music (`music`):
          - `id_str`: Music ID
          - `title`: Music title
          - `author`: Music creator
          - `play_url.url_list`: Music play URLs
          - `duration`: Music duration (seconds)
          - `cover_hd.url_list`: HD cover images
        - Hashtags (`cha_list[]`):
          - `cha_name`: Hashtag name
          - `share_url`: Share URL
        - Video (`video`):
          - `play_addr.url_list`: Video play URLs
          - `cover.url_list`: Cover images
          - `dynamic_cover.url_list`: Dynamic cover
          - `origin_cover.url_list`: Original cover
          - `duration`: Duration in milliseconds
          - `ratio`: Resolution (e.g., \"720p\")
          - `bit_rate[]`: Multiple quality sources
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
          - `allow_share`: Allow sharing or not
          - `allow_comment`: Allow commenting or not
        - Other fields:
          - `share_url`: External share URL
          - `user_digged`: Whether user liked (0=No, 1=Yes)

    Args:
        body (GeneralSearchV3Request):

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
    body: GeneralSearchV3Request,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取综合搜索 V3/Fetch general search V3

     # [中文]
    ### 用途:
    - 获取抖音 App 综合搜索结果（V3版，数据更全）。
    - 支持关键词、排序方式、发布时间、时长、内容类型等筛选。
    - 支持翻页查询，通过 `cursor` 和 `search_id` 进行分页。

    ### 备注:
    - 初次请求时 `cursor` 传 0，`search_id` 传空字符串。
    - 返回数据极为详细，包括视频、作者、音乐、话题、播放源、互动统计等信息。

    ### 参数:
    - keyword: 搜索关键词，如 \"猫咪\"
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
    - filter_duration: 视频时长筛选
        - `0`: 不限
        - `0-1`: 1分钟以内
        - `1-5`: 1-5分钟
        - `5-10000`: 5分钟以上
    - content_type: 内容类型筛选
        - `0`: 不限
        - `1`: 视频
        - `2`: 图片
        - `3`: 文章
    - search_id: 搜索ID（分页时使用）

    ### 请求体示例：
    ```json
    payload = {
      \"keyword\": \"猫咪\",
      \"cursor\": 0,
      \"sort_type\": \"0\",
      \"publish_time\": \"0\",
      \"filter_duration\": \"0\",
      \"content_type\": \"0\",
      \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `status_code`: 响应状态码（0为成功）
    - `data[]`: 搜索结果列表
      - `type`: 结果类型（通常为 `1`）
      - `aweme_info`: 视频详细信息
        - 基本信息:
          - `aweme_id`: 视频ID
          - `desc`: 视频描述
          - `create_time`: 发布时间（时间戳）
        - 作者信息 (`author`):
          - `uid`: 用户ID
          - `nickname`: 昵称
          - `short_id`: 用户短ID
          - `signature`: 用户签名
          - `region`: 地区，如 \"CN\"
          - `is_verified`: 是否认证
          - `avatar_thumb.url_list`: 缩略头像
          - `avatar_medium.url_list`: 中等尺寸头像
          - `avatar_larger.url_list`: 高清头像
        - 音乐信息 (`music`):
          - `id_str`: 音乐ID
          - `title`: 音乐标题
          - `author`: 音乐作者
          - `play_url.url_list`: 音乐播放链接
          - `duration`: 音乐时长（秒）
          - `cover_hd.url_list`: 高清封面图
        - 话题标签 (`cha_list[]`):
          - `cha_name`: 话题名
          - `share_url`: 分享链接
        - 视频播放信息 (`video`):
          - `play_addr.url_list`: 视频播放链接
          - `cover.url_list`: 封面图片
          - `dynamic_cover.url_list`: 动态封面
          - `origin_cover.url_list`: 原始封面
          - `duration`: 视频时长（毫秒）
          - `ratio`: 分辨率比例（如 \"720p\"）
          - `bit_rate[]`: 多清晰度播放源
            - `gear_name`: 清晰度名称（如 \"adapt_540_2\"）
            - `bit_rate`: 码率
            - `play_addr.url_list`: 对应播放链接
        - 互动统计 (`statistics`):
          - `comment_count`: 评论数
          - `digg_count`: 点赞数
          - `share_count`: 分享数
          - `play_count`: 播放数
        - 视频状态 (`status`):
          - `is_delete`: 是否删除
          - `is_private`: 是否私密
          - `allow_share`: 是否允许分享
          - `allow_comment`: 是否允许评论
        - 其他字段:
          - `share_url`: 视频分享链接
          - `user_digged`: 是否已点赞（0=未点赞，1=已点赞）

    # [English]
    ### Purpose:
    - Fetch Douyin App general search results (V3 version, more comprehensive data).
    - Supports filtering by keyword, sort type, publish time, video duration, and content type.
    - Supports pagination via `cursor` and `search_id`.

    ### Notes:
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - The response is rich, including video, author, music, hashtags, multiple play sources, and
    statistics.

    ### Parameters:
    - keyword: Search keyword, e.g., \"cat\"
    - cursor: Pagination cursor (0 for the first page)
    - sort_type: Sort type
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
        - `5-10000`: Over 5 minutes
    - content_type: Content type filter
        - `0`: Unlimited
        - `1`: Video
        - `2`: Picture
        - `3`: Article
    - search_id: Search ID for pagination

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"cat\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"0\",
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `status_code`: Response status code (0 means success)
    - `data[]`: List of search results
      - `type`: Result type (usually `1`)
      - `aweme_info`: Video details
        - Basic Info:
          - `aweme_id`: Video ID
          - `desc`: Video description
          - `create_time`: Publish timestamp
        - Author (`author`):
          - `uid`: User ID
          - `nickname`: Nickname
          - `short_id`: Short ID
          - `signature`: Signature
          - `region`: Region
          - `is_verified`: Verified or not
          - `avatar_thumb.url_list`: Thumbnail avatar
          - `avatar_medium.url_list`: Medium avatar
          - `avatar_larger.url_list`: Large avatar
        - Music (`music`):
          - `id_str`: Music ID
          - `title`: Music title
          - `author`: Music creator
          - `play_url.url_list`: Music play URLs
          - `duration`: Music duration (seconds)
          - `cover_hd.url_list`: HD cover images
        - Hashtags (`cha_list[]`):
          - `cha_name`: Hashtag name
          - `share_url`: Share URL
        - Video (`video`):
          - `play_addr.url_list`: Video play URLs
          - `cover.url_list`: Cover images
          - `dynamic_cover.url_list`: Dynamic cover
          - `origin_cover.url_list`: Original cover
          - `duration`: Duration in milliseconds
          - `ratio`: Resolution (e.g., \"720p\")
          - `bit_rate[]`: Multiple quality sources
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
          - `allow_share`: Allow sharing or not
          - `allow_comment`: Allow commenting or not
        - Other fields:
          - `share_url`: External share URL
          - `user_digged`: Whether user liked (0=No, 1=Yes)

    Args:
        body (GeneralSearchV3Request):

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
