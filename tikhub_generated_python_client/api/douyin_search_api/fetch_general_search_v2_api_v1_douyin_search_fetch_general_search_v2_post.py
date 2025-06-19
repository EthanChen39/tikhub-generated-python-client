from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.general_search_v2_request import GeneralSearchV2Request
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: GeneralSearchV2Request,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/search/fetch_general_search_v2",
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
    body: GeneralSearchV2Request,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取综合搜索 V2/Fetch general search V2

     # [中文]
    ### 用途:
    - 获取抖音 App 中综合搜索栏的搜索结果（非单独视频搜索）。
    - 此接口稳定性可能不如 V1版本，作为备用接口。
    - 支持关键词、排序方式、发布时间、视频时长、内容类型等筛选条件。
    - 支持翻页查询，通过 `cursor` 和 `search_id` 分页。

    ### 备注:
    - 初次请求时 `cursor` 传入 0，`search_id` 传空字符串。
    - 返回的内容包含视频、作者、话题标签、播放信息、音乐、互动数据等丰富信息。

    ### 参数:
    - keyword: 搜索关键词，如 \"猫咪\"
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
    - `data`: 搜索结果列表
    - `type`: 结果类型（通常为 `1`）
    - `aweme_info`: 视频详细信息
    - `aweme_id`: 视频ID
    - `desc`: 视频描述内容
    - `author`: 作者信息
      - `uid`: 用户唯一ID
      - `nickname`: 用户昵称
      - `is_verified`: 是否认证用户（True=已认证，False=未认证）
      - `region`: 用户地区，如 \"CN\"
      - `avatar_thumb.url_list`: 缩略头像地址列表
      - `avatar_medium.url_list`: 中等尺寸头像地址列表
      - `avatar_larger.url_list`: 高清头像地址列表
    - `music`: 背景音乐信息
      - `id_str`: 音乐ID
      - `title`: 音乐标题，如\"原创声音\"
      - `author`: 音乐作者昵称
      - `play_url.url_list`: 音乐播放地址列表
    - `cha_list`: 关联话题标签列表
      - `cha_name`: 话题名（例如 \"#猫宝宝\"）
      - `share_url`: 话题分享链接
    - `video`: 视频播放与封面信息
      - `play_addr.url_list`: 视频播放地址列表
      - `cover.url_list`: 视频封面地址列表
      - `dynamic_cover.url_list`: 动态封面地址列表
      - `origin_cover.url_list`: 原始封面地址列表
      - `width`: 视频宽度（像素）
      - `height`: 视频高度（像素）
      - `ratio`: 视频分辨率比例（如540p）
      - `duration`: 视频时长（单位：毫秒）
      - `download_addr.url_list`: 带水印下载地址
    - `statistics`: 视频统计信息
      - `comment_count`: 评论数
      - `digg_count`: 点赞数
      - `share_count`: 分享数
      - `play_count`: 播放次数
      - `collect_count`: 收藏次数
    - `status`: 视频发布状态
      - `is_delete`: 是否被删除
      - `is_private`: 是否设为私密
      - `allow_share`: 是否允许分享
      - `allow_comment`: 是否允许评论
    - `share_url`: 视频外部分享链接

    # [English]
    ### Purpose:
    - Fetch search results from Douyin App's general search tab (not standalone video search).
    - This API may be less stable than V1, serving as a backup.
    - Supports filtering by keyword, sort type, publish time, video duration, and content type.
    - Supports pagination through `cursor` and `search_id`.

    ### Notes:
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - The response contains rich information including video details, author info, music, hashtags,
    playback info, and interaction metrics.

    ### Parameters:
    - keyword: Search keyword, e.g., \"cat\"
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
    - `data`: List of search result items
    - `type`: Result type (usually `1`)
    - `aweme_info`: Video detailed information
    - `aweme_id`: Video ID
    - `desc`: Video description
    - `author`:
      - `uid`: Author's user ID
      - `nickname`: Author's nickname
      - `is_verified`: Whether the author is verified
      - `region`: Author's region
      - `avatar_thumb.url_list`: List of thumbnail avatar URLs
      - `avatar_medium.url_list`: List of medium size avatar URLs
      - `avatar_larger.url_list`: List of large size avatar URLs
    - `music`:
      - `id_str`: Music ID
      - `title`: Music title
      - `author`: Music creator's name
      - `play_url.url_list`: List of music play URLs
    - `cha_list`:
      - `cha_name`: Hashtag name
      - `share_url`: Hashtag share URL
    - `video`:
      - `play_addr.url_list`: List of video play URLs
      - `cover.url_list`: List of cover image URLs
      - `dynamic_cover.url_list`: List of dynamic cover URLs
      - `origin_cover.url_list`: List of original cover URLs
      - `width`: Video width (pixels)
      - `height`: Video height (pixels)
      - `ratio`: Resolution ratio (e.g., 540p)
      - `duration`: Duration in milliseconds
      - `download_addr.url_list`: List of video download URLs
    - `statistics`:
      - `comment_count`: Number of comments
      - `digg_count`: Number of likes
      - `share_count`: Number of shares
      - `play_count`: Number of plays
      - `collect_count`: Number of collects
    - `status`:
      - `is_delete`: Whether the video is deleted
      - `is_private`: Whether the video is private
      - `allow_share`: Whether sharing is allowed
      - `allow_comment`: Whether commenting is allowed
    - `share_url`: External share link

    Args:
        body (GeneralSearchV2Request):

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
    body: GeneralSearchV2Request,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取综合搜索 V2/Fetch general search V2

     # [中文]
    ### 用途:
    - 获取抖音 App 中综合搜索栏的搜索结果（非单独视频搜索）。
    - 此接口稳定性可能不如 V1版本，作为备用接口。
    - 支持关键词、排序方式、发布时间、视频时长、内容类型等筛选条件。
    - 支持翻页查询，通过 `cursor` 和 `search_id` 分页。

    ### 备注:
    - 初次请求时 `cursor` 传入 0，`search_id` 传空字符串。
    - 返回的内容包含视频、作者、话题标签、播放信息、音乐、互动数据等丰富信息。

    ### 参数:
    - keyword: 搜索关键词，如 \"猫咪\"
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
    - `data`: 搜索结果列表
    - `type`: 结果类型（通常为 `1`）
    - `aweme_info`: 视频详细信息
    - `aweme_id`: 视频ID
    - `desc`: 视频描述内容
    - `author`: 作者信息
      - `uid`: 用户唯一ID
      - `nickname`: 用户昵称
      - `is_verified`: 是否认证用户（True=已认证，False=未认证）
      - `region`: 用户地区，如 \"CN\"
      - `avatar_thumb.url_list`: 缩略头像地址列表
      - `avatar_medium.url_list`: 中等尺寸头像地址列表
      - `avatar_larger.url_list`: 高清头像地址列表
    - `music`: 背景音乐信息
      - `id_str`: 音乐ID
      - `title`: 音乐标题，如\"原创声音\"
      - `author`: 音乐作者昵称
      - `play_url.url_list`: 音乐播放地址列表
    - `cha_list`: 关联话题标签列表
      - `cha_name`: 话题名（例如 \"#猫宝宝\"）
      - `share_url`: 话题分享链接
    - `video`: 视频播放与封面信息
      - `play_addr.url_list`: 视频播放地址列表
      - `cover.url_list`: 视频封面地址列表
      - `dynamic_cover.url_list`: 动态封面地址列表
      - `origin_cover.url_list`: 原始封面地址列表
      - `width`: 视频宽度（像素）
      - `height`: 视频高度（像素）
      - `ratio`: 视频分辨率比例（如540p）
      - `duration`: 视频时长（单位：毫秒）
      - `download_addr.url_list`: 带水印下载地址
    - `statistics`: 视频统计信息
      - `comment_count`: 评论数
      - `digg_count`: 点赞数
      - `share_count`: 分享数
      - `play_count`: 播放次数
      - `collect_count`: 收藏次数
    - `status`: 视频发布状态
      - `is_delete`: 是否被删除
      - `is_private`: 是否设为私密
      - `allow_share`: 是否允许分享
      - `allow_comment`: 是否允许评论
    - `share_url`: 视频外部分享链接

    # [English]
    ### Purpose:
    - Fetch search results from Douyin App's general search tab (not standalone video search).
    - This API may be less stable than V1, serving as a backup.
    - Supports filtering by keyword, sort type, publish time, video duration, and content type.
    - Supports pagination through `cursor` and `search_id`.

    ### Notes:
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - The response contains rich information including video details, author info, music, hashtags,
    playback info, and interaction metrics.

    ### Parameters:
    - keyword: Search keyword, e.g., \"cat\"
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
    - `data`: List of search result items
    - `type`: Result type (usually `1`)
    - `aweme_info`: Video detailed information
    - `aweme_id`: Video ID
    - `desc`: Video description
    - `author`:
      - `uid`: Author's user ID
      - `nickname`: Author's nickname
      - `is_verified`: Whether the author is verified
      - `region`: Author's region
      - `avatar_thumb.url_list`: List of thumbnail avatar URLs
      - `avatar_medium.url_list`: List of medium size avatar URLs
      - `avatar_larger.url_list`: List of large size avatar URLs
    - `music`:
      - `id_str`: Music ID
      - `title`: Music title
      - `author`: Music creator's name
      - `play_url.url_list`: List of music play URLs
    - `cha_list`:
      - `cha_name`: Hashtag name
      - `share_url`: Hashtag share URL
    - `video`:
      - `play_addr.url_list`: List of video play URLs
      - `cover.url_list`: List of cover image URLs
      - `dynamic_cover.url_list`: List of dynamic cover URLs
      - `origin_cover.url_list`: List of original cover URLs
      - `width`: Video width (pixels)
      - `height`: Video height (pixels)
      - `ratio`: Resolution ratio (e.g., 540p)
      - `duration`: Duration in milliseconds
      - `download_addr.url_list`: List of video download URLs
    - `statistics`:
      - `comment_count`: Number of comments
      - `digg_count`: Number of likes
      - `share_count`: Number of shares
      - `play_count`: Number of plays
      - `collect_count`: Number of collects
    - `status`:
      - `is_delete`: Whether the video is deleted
      - `is_private`: Whether the video is private
      - `allow_share`: Whether sharing is allowed
      - `allow_comment`: Whether commenting is allowed
    - `share_url`: External share link

    Args:
        body (GeneralSearchV2Request):

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
    body: GeneralSearchV2Request,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取综合搜索 V2/Fetch general search V2

     # [中文]
    ### 用途:
    - 获取抖音 App 中综合搜索栏的搜索结果（非单独视频搜索）。
    - 此接口稳定性可能不如 V1版本，作为备用接口。
    - 支持关键词、排序方式、发布时间、视频时长、内容类型等筛选条件。
    - 支持翻页查询，通过 `cursor` 和 `search_id` 分页。

    ### 备注:
    - 初次请求时 `cursor` 传入 0，`search_id` 传空字符串。
    - 返回的内容包含视频、作者、话题标签、播放信息、音乐、互动数据等丰富信息。

    ### 参数:
    - keyword: 搜索关键词，如 \"猫咪\"
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
    - `data`: 搜索结果列表
    - `type`: 结果类型（通常为 `1`）
    - `aweme_info`: 视频详细信息
    - `aweme_id`: 视频ID
    - `desc`: 视频描述内容
    - `author`: 作者信息
      - `uid`: 用户唯一ID
      - `nickname`: 用户昵称
      - `is_verified`: 是否认证用户（True=已认证，False=未认证）
      - `region`: 用户地区，如 \"CN\"
      - `avatar_thumb.url_list`: 缩略头像地址列表
      - `avatar_medium.url_list`: 中等尺寸头像地址列表
      - `avatar_larger.url_list`: 高清头像地址列表
    - `music`: 背景音乐信息
      - `id_str`: 音乐ID
      - `title`: 音乐标题，如\"原创声音\"
      - `author`: 音乐作者昵称
      - `play_url.url_list`: 音乐播放地址列表
    - `cha_list`: 关联话题标签列表
      - `cha_name`: 话题名（例如 \"#猫宝宝\"）
      - `share_url`: 话题分享链接
    - `video`: 视频播放与封面信息
      - `play_addr.url_list`: 视频播放地址列表
      - `cover.url_list`: 视频封面地址列表
      - `dynamic_cover.url_list`: 动态封面地址列表
      - `origin_cover.url_list`: 原始封面地址列表
      - `width`: 视频宽度（像素）
      - `height`: 视频高度（像素）
      - `ratio`: 视频分辨率比例（如540p）
      - `duration`: 视频时长（单位：毫秒）
      - `download_addr.url_list`: 带水印下载地址
    - `statistics`: 视频统计信息
      - `comment_count`: 评论数
      - `digg_count`: 点赞数
      - `share_count`: 分享数
      - `play_count`: 播放次数
      - `collect_count`: 收藏次数
    - `status`: 视频发布状态
      - `is_delete`: 是否被删除
      - `is_private`: 是否设为私密
      - `allow_share`: 是否允许分享
      - `allow_comment`: 是否允许评论
    - `share_url`: 视频外部分享链接

    # [English]
    ### Purpose:
    - Fetch search results from Douyin App's general search tab (not standalone video search).
    - This API may be less stable than V1, serving as a backup.
    - Supports filtering by keyword, sort type, publish time, video duration, and content type.
    - Supports pagination through `cursor` and `search_id`.

    ### Notes:
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - The response contains rich information including video details, author info, music, hashtags,
    playback info, and interaction metrics.

    ### Parameters:
    - keyword: Search keyword, e.g., \"cat\"
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
    - `data`: List of search result items
    - `type`: Result type (usually `1`)
    - `aweme_info`: Video detailed information
    - `aweme_id`: Video ID
    - `desc`: Video description
    - `author`:
      - `uid`: Author's user ID
      - `nickname`: Author's nickname
      - `is_verified`: Whether the author is verified
      - `region`: Author's region
      - `avatar_thumb.url_list`: List of thumbnail avatar URLs
      - `avatar_medium.url_list`: List of medium size avatar URLs
      - `avatar_larger.url_list`: List of large size avatar URLs
    - `music`:
      - `id_str`: Music ID
      - `title`: Music title
      - `author`: Music creator's name
      - `play_url.url_list`: List of music play URLs
    - `cha_list`:
      - `cha_name`: Hashtag name
      - `share_url`: Hashtag share URL
    - `video`:
      - `play_addr.url_list`: List of video play URLs
      - `cover.url_list`: List of cover image URLs
      - `dynamic_cover.url_list`: List of dynamic cover URLs
      - `origin_cover.url_list`: List of original cover URLs
      - `width`: Video width (pixels)
      - `height`: Video height (pixels)
      - `ratio`: Resolution ratio (e.g., 540p)
      - `duration`: Duration in milliseconds
      - `download_addr.url_list`: List of video download URLs
    - `statistics`:
      - `comment_count`: Number of comments
      - `digg_count`: Number of likes
      - `share_count`: Number of shares
      - `play_count`: Number of plays
      - `collect_count`: Number of collects
    - `status`:
      - `is_delete`: Whether the video is deleted
      - `is_private`: Whether the video is private
      - `allow_share`: Whether sharing is allowed
      - `allow_comment`: Whether commenting is allowed
    - `share_url`: External share link

    Args:
        body (GeneralSearchV2Request):

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
    body: GeneralSearchV2Request,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取综合搜索 V2/Fetch general search V2

     # [中文]
    ### 用途:
    - 获取抖音 App 中综合搜索栏的搜索结果（非单独视频搜索）。
    - 此接口稳定性可能不如 V1版本，作为备用接口。
    - 支持关键词、排序方式、发布时间、视频时长、内容类型等筛选条件。
    - 支持翻页查询，通过 `cursor` 和 `search_id` 分页。

    ### 备注:
    - 初次请求时 `cursor` 传入 0，`search_id` 传空字符串。
    - 返回的内容包含视频、作者、话题标签、播放信息、音乐、互动数据等丰富信息。

    ### 参数:
    - keyword: 搜索关键词，如 \"猫咪\"
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
    - `data`: 搜索结果列表
    - `type`: 结果类型（通常为 `1`）
    - `aweme_info`: 视频详细信息
    - `aweme_id`: 视频ID
    - `desc`: 视频描述内容
    - `author`: 作者信息
      - `uid`: 用户唯一ID
      - `nickname`: 用户昵称
      - `is_verified`: 是否认证用户（True=已认证，False=未认证）
      - `region`: 用户地区，如 \"CN\"
      - `avatar_thumb.url_list`: 缩略头像地址列表
      - `avatar_medium.url_list`: 中等尺寸头像地址列表
      - `avatar_larger.url_list`: 高清头像地址列表
    - `music`: 背景音乐信息
      - `id_str`: 音乐ID
      - `title`: 音乐标题，如\"原创声音\"
      - `author`: 音乐作者昵称
      - `play_url.url_list`: 音乐播放地址列表
    - `cha_list`: 关联话题标签列表
      - `cha_name`: 话题名（例如 \"#猫宝宝\"）
      - `share_url`: 话题分享链接
    - `video`: 视频播放与封面信息
      - `play_addr.url_list`: 视频播放地址列表
      - `cover.url_list`: 视频封面地址列表
      - `dynamic_cover.url_list`: 动态封面地址列表
      - `origin_cover.url_list`: 原始封面地址列表
      - `width`: 视频宽度（像素）
      - `height`: 视频高度（像素）
      - `ratio`: 视频分辨率比例（如540p）
      - `duration`: 视频时长（单位：毫秒）
      - `download_addr.url_list`: 带水印下载地址
    - `statistics`: 视频统计信息
      - `comment_count`: 评论数
      - `digg_count`: 点赞数
      - `share_count`: 分享数
      - `play_count`: 播放次数
      - `collect_count`: 收藏次数
    - `status`: 视频发布状态
      - `is_delete`: 是否被删除
      - `is_private`: 是否设为私密
      - `allow_share`: 是否允许分享
      - `allow_comment`: 是否允许评论
    - `share_url`: 视频外部分享链接

    # [English]
    ### Purpose:
    - Fetch search results from Douyin App's general search tab (not standalone video search).
    - This API may be less stable than V1, serving as a backup.
    - Supports filtering by keyword, sort type, publish time, video duration, and content type.
    - Supports pagination through `cursor` and `search_id`.

    ### Notes:
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - The response contains rich information including video details, author info, music, hashtags,
    playback info, and interaction metrics.

    ### Parameters:
    - keyword: Search keyword, e.g., \"cat\"
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
    - `data`: List of search result items
    - `type`: Result type (usually `1`)
    - `aweme_info`: Video detailed information
    - `aweme_id`: Video ID
    - `desc`: Video description
    - `author`:
      - `uid`: Author's user ID
      - `nickname`: Author's nickname
      - `is_verified`: Whether the author is verified
      - `region`: Author's region
      - `avatar_thumb.url_list`: List of thumbnail avatar URLs
      - `avatar_medium.url_list`: List of medium size avatar URLs
      - `avatar_larger.url_list`: List of large size avatar URLs
    - `music`:
      - `id_str`: Music ID
      - `title`: Music title
      - `author`: Music creator's name
      - `play_url.url_list`: List of music play URLs
    - `cha_list`:
      - `cha_name`: Hashtag name
      - `share_url`: Hashtag share URL
    - `video`:
      - `play_addr.url_list`: List of video play URLs
      - `cover.url_list`: List of cover image URLs
      - `dynamic_cover.url_list`: List of dynamic cover URLs
      - `origin_cover.url_list`: List of original cover URLs
      - `width`: Video width (pixels)
      - `height`: Video height (pixels)
      - `ratio`: Resolution ratio (e.g., 540p)
      - `duration`: Duration in milliseconds
      - `download_addr.url_list`: List of video download URLs
    - `statistics`:
      - `comment_count`: Number of comments
      - `digg_count`: Number of likes
      - `share_count`: Number of shares
      - `play_count`: Number of plays
      - `collect_count`: Number of collects
    - `status`:
      - `is_delete`: Whether the video is deleted
      - `is_private`: Whether the video is private
      - `allow_share`: Whether sharing is allowed
      - `allow_comment`: Whether commenting is allowed
    - `share_url`: External share link

    Args:
        body (GeneralSearchV2Request):

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
