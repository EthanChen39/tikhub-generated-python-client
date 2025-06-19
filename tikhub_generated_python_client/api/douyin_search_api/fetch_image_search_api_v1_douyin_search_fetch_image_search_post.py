from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.image_search_request import ImageSearchRequest
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: ImageSearchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/search/fetch_image_search",
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
    body: ImageSearchRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取图片搜索/Fetch image search

     # [中文]
    ### 用途:
    - 获取抖音 App 中图片内容搜索的结果。
    - 主要返回带有多张图片的帖子（图片合集）。

    ### 备注:
    - 仅返回图片类型的内容，适用于图片展示类应用场景。
    - 初次请求 `cursor` 传 0，`search_id` 传空字符串。
    - 翻页时使用上一次响应中的 `cursor` 和 `search_id`。

    ### 参数:
    - keyword: 搜索关键词，如 \"猫咪\"
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
    - filter_duration: 视频时长筛选
      - `0`: 不限
    - content_type: 内容类型（固定传 2 表示图片内容）
    - search_id: 搜索ID（翻页使用）

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"猫咪\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"2\",
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `cursor`: 下一页游标
    - `has_more`: 是否还有更多数据（1=有，0=无）
    - `data[]`: 图片内容列表
      - `aweme_info`:
        - `aweme_id`: 内容ID
        - `desc`: 帖子描述文字
        - `create_time`: 创建时间戳
        - `author`:
          - `uid`: 作者ID
          - `nickname`: 昵称
          - `is_verified`: 是否认证
          - `avatar_thumb.url_list`: 缩略头像URL列表
          - `avatar_medium.url_list`: 中等头像URL列表
          - `avatar_larger.url_list`: 高清头像URL列表
        - `image_post_info`:
          - `images[]`: 图片列表
            - `url_list`: 图片地址数组（通常包含webp/jpg）
            - `width`: 图片宽度（像素）
            - `height`: 图片高度（像素）
        - `statistics`:
          - `comment_count`: 评论数
          - `digg_count`: 点赞数
          - `share_count`: 分享数
          - `play_count`: 播放数
          - `collect_count`: 收藏数
        - `status`:
          - `is_delete`: 是否删除
          - `is_private`: 是否私密
        - `share_url`: 外部分享链接

    - `extra`:
      - `now`: 当前服务器时间戳
      - `logid`: 请求日志ID
      - `search_request_id`: 搜索请求ID

    # [English]
    ### Purpose:
    - Fetch image-based search results from Douyin App.
    - Mainly returns posts containing image collections.

    ### Notes:
    - Only image posts are returned. Suitable for gallery-style applications.
    - For the first request, set `cursor` to 0 and `search_id` to an empty string.
    - For pagination, use the `cursor` and `search_id` from the last response.

    ### Parameters:
    - keyword: Search keyword, e.g., \"cat\"
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
    - content_type: Content type (Fixed to 2 for images)
    - search_id: Search ID for pagination

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"cat\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"2\",
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `cursor`: Cursor for next page
    - `has_more`: Whether there are more results (1=Yes, 0=No)
    - `data[]`: List of image posts
      - `aweme_info`:
        - `aweme_id`: Content ID
        - `desc`: Post description
        - `create_time`: Creation timestamp
        - `author`:
          - `uid`: Author ID
          - `nickname`: Nickname
          - `is_verified`: Verified status
          - `avatar_thumb.url_list`: Thumbnail avatar URLs
          - `avatar_medium.url_list`: Medium avatar URLs
          - `avatar_larger.url_list`: High-res avatar URLs
        - `image_post_info`:
          - `images[]`: List of images
            - `url_list`: Image URLs (webp/jpg)
            - `width`: Width (pixels)
            - `height`: Height (pixels)
        - `statistics`:
          - `comment_count`: Comment count
          - `digg_count`: Like count
          - `share_count`: Share count
          - `play_count`: Play count
          - `collect_count`: Collect count
        - `status`:
          - `is_delete`: Whether deleted
          - `is_private`: Whether private
        - `share_url`: Shareable external link
    - `extra`:
      - `now`: Current server timestamp
      - `logid`: Request log ID
      - `search_request_id`: Search session ID

    Args:
        body (ImageSearchRequest):

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
    body: ImageSearchRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取图片搜索/Fetch image search

     # [中文]
    ### 用途:
    - 获取抖音 App 中图片内容搜索的结果。
    - 主要返回带有多张图片的帖子（图片合集）。

    ### 备注:
    - 仅返回图片类型的内容，适用于图片展示类应用场景。
    - 初次请求 `cursor` 传 0，`search_id` 传空字符串。
    - 翻页时使用上一次响应中的 `cursor` 和 `search_id`。

    ### 参数:
    - keyword: 搜索关键词，如 \"猫咪\"
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
    - filter_duration: 视频时长筛选
      - `0`: 不限
    - content_type: 内容类型（固定传 2 表示图片内容）
    - search_id: 搜索ID（翻页使用）

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"猫咪\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"2\",
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `cursor`: 下一页游标
    - `has_more`: 是否还有更多数据（1=有，0=无）
    - `data[]`: 图片内容列表
      - `aweme_info`:
        - `aweme_id`: 内容ID
        - `desc`: 帖子描述文字
        - `create_time`: 创建时间戳
        - `author`:
          - `uid`: 作者ID
          - `nickname`: 昵称
          - `is_verified`: 是否认证
          - `avatar_thumb.url_list`: 缩略头像URL列表
          - `avatar_medium.url_list`: 中等头像URL列表
          - `avatar_larger.url_list`: 高清头像URL列表
        - `image_post_info`:
          - `images[]`: 图片列表
            - `url_list`: 图片地址数组（通常包含webp/jpg）
            - `width`: 图片宽度（像素）
            - `height`: 图片高度（像素）
        - `statistics`:
          - `comment_count`: 评论数
          - `digg_count`: 点赞数
          - `share_count`: 分享数
          - `play_count`: 播放数
          - `collect_count`: 收藏数
        - `status`:
          - `is_delete`: 是否删除
          - `is_private`: 是否私密
        - `share_url`: 外部分享链接

    - `extra`:
      - `now`: 当前服务器时间戳
      - `logid`: 请求日志ID
      - `search_request_id`: 搜索请求ID

    # [English]
    ### Purpose:
    - Fetch image-based search results from Douyin App.
    - Mainly returns posts containing image collections.

    ### Notes:
    - Only image posts are returned. Suitable for gallery-style applications.
    - For the first request, set `cursor` to 0 and `search_id` to an empty string.
    - For pagination, use the `cursor` and `search_id` from the last response.

    ### Parameters:
    - keyword: Search keyword, e.g., \"cat\"
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
    - content_type: Content type (Fixed to 2 for images)
    - search_id: Search ID for pagination

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"cat\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"2\",
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `cursor`: Cursor for next page
    - `has_more`: Whether there are more results (1=Yes, 0=No)
    - `data[]`: List of image posts
      - `aweme_info`:
        - `aweme_id`: Content ID
        - `desc`: Post description
        - `create_time`: Creation timestamp
        - `author`:
          - `uid`: Author ID
          - `nickname`: Nickname
          - `is_verified`: Verified status
          - `avatar_thumb.url_list`: Thumbnail avatar URLs
          - `avatar_medium.url_list`: Medium avatar URLs
          - `avatar_larger.url_list`: High-res avatar URLs
        - `image_post_info`:
          - `images[]`: List of images
            - `url_list`: Image URLs (webp/jpg)
            - `width`: Width (pixels)
            - `height`: Height (pixels)
        - `statistics`:
          - `comment_count`: Comment count
          - `digg_count`: Like count
          - `share_count`: Share count
          - `play_count`: Play count
          - `collect_count`: Collect count
        - `status`:
          - `is_delete`: Whether deleted
          - `is_private`: Whether private
        - `share_url`: Shareable external link
    - `extra`:
      - `now`: Current server timestamp
      - `logid`: Request log ID
      - `search_request_id`: Search session ID

    Args:
        body (ImageSearchRequest):

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
    body: ImageSearchRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取图片搜索/Fetch image search

     # [中文]
    ### 用途:
    - 获取抖音 App 中图片内容搜索的结果。
    - 主要返回带有多张图片的帖子（图片合集）。

    ### 备注:
    - 仅返回图片类型的内容，适用于图片展示类应用场景。
    - 初次请求 `cursor` 传 0，`search_id` 传空字符串。
    - 翻页时使用上一次响应中的 `cursor` 和 `search_id`。

    ### 参数:
    - keyword: 搜索关键词，如 \"猫咪\"
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
    - filter_duration: 视频时长筛选
      - `0`: 不限
    - content_type: 内容类型（固定传 2 表示图片内容）
    - search_id: 搜索ID（翻页使用）

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"猫咪\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"2\",
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `cursor`: 下一页游标
    - `has_more`: 是否还有更多数据（1=有，0=无）
    - `data[]`: 图片内容列表
      - `aweme_info`:
        - `aweme_id`: 内容ID
        - `desc`: 帖子描述文字
        - `create_time`: 创建时间戳
        - `author`:
          - `uid`: 作者ID
          - `nickname`: 昵称
          - `is_verified`: 是否认证
          - `avatar_thumb.url_list`: 缩略头像URL列表
          - `avatar_medium.url_list`: 中等头像URL列表
          - `avatar_larger.url_list`: 高清头像URL列表
        - `image_post_info`:
          - `images[]`: 图片列表
            - `url_list`: 图片地址数组（通常包含webp/jpg）
            - `width`: 图片宽度（像素）
            - `height`: 图片高度（像素）
        - `statistics`:
          - `comment_count`: 评论数
          - `digg_count`: 点赞数
          - `share_count`: 分享数
          - `play_count`: 播放数
          - `collect_count`: 收藏数
        - `status`:
          - `is_delete`: 是否删除
          - `is_private`: 是否私密
        - `share_url`: 外部分享链接

    - `extra`:
      - `now`: 当前服务器时间戳
      - `logid`: 请求日志ID
      - `search_request_id`: 搜索请求ID

    # [English]
    ### Purpose:
    - Fetch image-based search results from Douyin App.
    - Mainly returns posts containing image collections.

    ### Notes:
    - Only image posts are returned. Suitable for gallery-style applications.
    - For the first request, set `cursor` to 0 and `search_id` to an empty string.
    - For pagination, use the `cursor` and `search_id` from the last response.

    ### Parameters:
    - keyword: Search keyword, e.g., \"cat\"
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
    - content_type: Content type (Fixed to 2 for images)
    - search_id: Search ID for pagination

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"cat\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"2\",
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `cursor`: Cursor for next page
    - `has_more`: Whether there are more results (1=Yes, 0=No)
    - `data[]`: List of image posts
      - `aweme_info`:
        - `aweme_id`: Content ID
        - `desc`: Post description
        - `create_time`: Creation timestamp
        - `author`:
          - `uid`: Author ID
          - `nickname`: Nickname
          - `is_verified`: Verified status
          - `avatar_thumb.url_list`: Thumbnail avatar URLs
          - `avatar_medium.url_list`: Medium avatar URLs
          - `avatar_larger.url_list`: High-res avatar URLs
        - `image_post_info`:
          - `images[]`: List of images
            - `url_list`: Image URLs (webp/jpg)
            - `width`: Width (pixels)
            - `height`: Height (pixels)
        - `statistics`:
          - `comment_count`: Comment count
          - `digg_count`: Like count
          - `share_count`: Share count
          - `play_count`: Play count
          - `collect_count`: Collect count
        - `status`:
          - `is_delete`: Whether deleted
          - `is_private`: Whether private
        - `share_url`: Shareable external link
    - `extra`:
      - `now`: Current server timestamp
      - `logid`: Request log ID
      - `search_request_id`: Search session ID

    Args:
        body (ImageSearchRequest):

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
    body: ImageSearchRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取图片搜索/Fetch image search

     # [中文]
    ### 用途:
    - 获取抖音 App 中图片内容搜索的结果。
    - 主要返回带有多张图片的帖子（图片合集）。

    ### 备注:
    - 仅返回图片类型的内容，适用于图片展示类应用场景。
    - 初次请求 `cursor` 传 0，`search_id` 传空字符串。
    - 翻页时使用上一次响应中的 `cursor` 和 `search_id`。

    ### 参数:
    - keyword: 搜索关键词，如 \"猫咪\"
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
    - filter_duration: 视频时长筛选
      - `0`: 不限
    - content_type: 内容类型（固定传 2 表示图片内容）
    - search_id: 搜索ID（翻页使用）

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"猫咪\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"2\",
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `cursor`: 下一页游标
    - `has_more`: 是否还有更多数据（1=有，0=无）
    - `data[]`: 图片内容列表
      - `aweme_info`:
        - `aweme_id`: 内容ID
        - `desc`: 帖子描述文字
        - `create_time`: 创建时间戳
        - `author`:
          - `uid`: 作者ID
          - `nickname`: 昵称
          - `is_verified`: 是否认证
          - `avatar_thumb.url_list`: 缩略头像URL列表
          - `avatar_medium.url_list`: 中等头像URL列表
          - `avatar_larger.url_list`: 高清头像URL列表
        - `image_post_info`:
          - `images[]`: 图片列表
            - `url_list`: 图片地址数组（通常包含webp/jpg）
            - `width`: 图片宽度（像素）
            - `height`: 图片高度（像素）
        - `statistics`:
          - `comment_count`: 评论数
          - `digg_count`: 点赞数
          - `share_count`: 分享数
          - `play_count`: 播放数
          - `collect_count`: 收藏数
        - `status`:
          - `is_delete`: 是否删除
          - `is_private`: 是否私密
        - `share_url`: 外部分享链接

    - `extra`:
      - `now`: 当前服务器时间戳
      - `logid`: 请求日志ID
      - `search_request_id`: 搜索请求ID

    # [English]
    ### Purpose:
    - Fetch image-based search results from Douyin App.
    - Mainly returns posts containing image collections.

    ### Notes:
    - Only image posts are returned. Suitable for gallery-style applications.
    - For the first request, set `cursor` to 0 and `search_id` to an empty string.
    - For pagination, use the `cursor` and `search_id` from the last response.

    ### Parameters:
    - keyword: Search keyword, e.g., \"cat\"
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
    - content_type: Content type (Fixed to 2 for images)
    - search_id: Search ID for pagination

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"cat\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"2\",
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `cursor`: Cursor for next page
    - `has_more`: Whether there are more results (1=Yes, 0=No)
    - `data[]`: List of image posts
      - `aweme_info`:
        - `aweme_id`: Content ID
        - `desc`: Post description
        - `create_time`: Creation timestamp
        - `author`:
          - `uid`: Author ID
          - `nickname`: Nickname
          - `is_verified`: Verified status
          - `avatar_thumb.url_list`: Thumbnail avatar URLs
          - `avatar_medium.url_list`: Medium avatar URLs
          - `avatar_larger.url_list`: High-res avatar URLs
        - `image_post_info`:
          - `images[]`: List of images
            - `url_list`: Image URLs (webp/jpg)
            - `width`: Width (pixels)
            - `height`: Height (pixels)
        - `statistics`:
          - `comment_count`: Comment count
          - `digg_count`: Like count
          - `share_count`: Share count
          - `play_count`: Play count
          - `collect_count`: Collect count
        - `status`:
          - `is_delete`: Whether deleted
          - `is_private`: Whether private
        - `share_url`: Shareable external link
    - `extra`:
      - `now`: Current server timestamp
      - `logid`: Request log ID
      - `search_request_id`: Search session ID

    Args:
        body (ImageSearchRequest):

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
