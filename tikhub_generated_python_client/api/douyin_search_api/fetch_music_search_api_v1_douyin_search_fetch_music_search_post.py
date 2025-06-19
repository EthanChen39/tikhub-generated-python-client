from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.music_search_request import MusicSearchRequest
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: MusicSearchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/search/fetch_music_search",
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
    body: MusicSearchRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取音乐搜索/Fetch music search

     # [中文]
    ### 用途:
    - 获取抖音 App 中音乐内容的搜索结果。
    - 支持关键词、排序方式、筛选条件等。

    ### 备注:
    - 本接口专注于音乐类内容搜索，不包含其他类型内容。
    - 初次请求时 `cursor` 传 0，`search_id` 传空字符串。
    - 返回内容包含音乐基本信息、作者信息、封面、播放地址、标签等。

    ### 参数:
    - keyword: 搜索关键词，例如 \"游戏背景音乐\"
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
        \"keyword\": \"游戏背景音乐\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 0,
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `music`: 音乐结果列表
      - `id_str`: 音乐ID（字符串格式）
      - `title`: 音乐标题
      - `author`: 音乐作者昵称
      - `album`: 所属专辑（如果有）
      - `play_url.url_list`: 音乐播放地址列表
      - `duration`: 音乐时长（秒）
      - `cover_thumb.url_list`: 缩略封面图片列表
      - `cover_medium.url_list`: 中尺寸封面图片列表
      - `cover_large.url_list`: 高清封面图片列表
      - `user_count`: 使用该音乐的作品数量
      - `is_original`: 是否原创音乐
      - `is_commerce_music`: 是否为商业授权音乐
      - `lyric_url`: 歌词文件链接（如果有）
      - `strong_beat_url.url_list`: 音乐节奏点文件链接
      - `tags`: 音乐标签
        - 如：主题（如游戏、Vlog）、情绪（如Funny）、风格（如8-bit, Electronic）
      - `artists`: 音乐关联的创作者列表（如果有）
        - `artist_name`: 艺人昵称
        - `uid`: 艺人UID
      - `cover_color_hsv`: 封面主色调HSV值
      - `can_background_play`: 是否支持后台播放

    # [English]
    ### Purpose:
    - Fetch music content search results from Douyin App.
    - Supports filtering by keyword, sort type, etc.

    ### Notes:
    - This API focuses on music content search, excluding other types.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - Response includes music basic info, artist info, covers, play URLs, tags, etc.

    ### Parameters:
    - keyword: Search keyword, e.g., \"game background music\"
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
        - `1-5`: 1 to 5 minutes
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
        \"keyword\": \"game background music\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 0,
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `music`: List of music search results
      - `id_str`: Music ID (as string)
      - `title`: Music title
      - `author`: Music author's nickname
      - `album`: Album name (if any)
      - `play_url.url_list`: List of music play URLs
      - `duration`: Duration in seconds
      - `cover_thumb.url_list`: List of thumbnail cover URLs
      - `cover_medium.url_list`: List of medium-sized cover URLs
      - `cover_large.url_list`: List of large-sized cover URLs
      - `user_count`: Number of videos using this music
      - `is_original`: Whether it is original music
      - `is_commerce_music`: Whether it is commercial music
      - `lyric_url`: Lyrics file URL (if available)
      - `strong_beat_url.url_list`: Beat timing file URLs
      - `tags`: Music tags
        - Themes (e.g., Game, Vlog), Moods (e.g., Funny), Genres (e.g., 8-bit, Electronic)
      - `artists`: List of associated artists (if any)
        - `artist_name`: Artist name
        - `uid`: Artist UID
      - `cover_color_hsv`: Dominant HSV color of the cover
      - `can_background_play`: Whether background playback is supported

    Args:
        body (MusicSearchRequest):

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
    body: MusicSearchRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取音乐搜索/Fetch music search

     # [中文]
    ### 用途:
    - 获取抖音 App 中音乐内容的搜索结果。
    - 支持关键词、排序方式、筛选条件等。

    ### 备注:
    - 本接口专注于音乐类内容搜索，不包含其他类型内容。
    - 初次请求时 `cursor` 传 0，`search_id` 传空字符串。
    - 返回内容包含音乐基本信息、作者信息、封面、播放地址、标签等。

    ### 参数:
    - keyword: 搜索关键词，例如 \"游戏背景音乐\"
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
        \"keyword\": \"游戏背景音乐\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 0,
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `music`: 音乐结果列表
      - `id_str`: 音乐ID（字符串格式）
      - `title`: 音乐标题
      - `author`: 音乐作者昵称
      - `album`: 所属专辑（如果有）
      - `play_url.url_list`: 音乐播放地址列表
      - `duration`: 音乐时长（秒）
      - `cover_thumb.url_list`: 缩略封面图片列表
      - `cover_medium.url_list`: 中尺寸封面图片列表
      - `cover_large.url_list`: 高清封面图片列表
      - `user_count`: 使用该音乐的作品数量
      - `is_original`: 是否原创音乐
      - `is_commerce_music`: 是否为商业授权音乐
      - `lyric_url`: 歌词文件链接（如果有）
      - `strong_beat_url.url_list`: 音乐节奏点文件链接
      - `tags`: 音乐标签
        - 如：主题（如游戏、Vlog）、情绪（如Funny）、风格（如8-bit, Electronic）
      - `artists`: 音乐关联的创作者列表（如果有）
        - `artist_name`: 艺人昵称
        - `uid`: 艺人UID
      - `cover_color_hsv`: 封面主色调HSV值
      - `can_background_play`: 是否支持后台播放

    # [English]
    ### Purpose:
    - Fetch music content search results from Douyin App.
    - Supports filtering by keyword, sort type, etc.

    ### Notes:
    - This API focuses on music content search, excluding other types.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - Response includes music basic info, artist info, covers, play URLs, tags, etc.

    ### Parameters:
    - keyword: Search keyword, e.g., \"game background music\"
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
        - `1-5`: 1 to 5 minutes
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
        \"keyword\": \"game background music\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 0,
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `music`: List of music search results
      - `id_str`: Music ID (as string)
      - `title`: Music title
      - `author`: Music author's nickname
      - `album`: Album name (if any)
      - `play_url.url_list`: List of music play URLs
      - `duration`: Duration in seconds
      - `cover_thumb.url_list`: List of thumbnail cover URLs
      - `cover_medium.url_list`: List of medium-sized cover URLs
      - `cover_large.url_list`: List of large-sized cover URLs
      - `user_count`: Number of videos using this music
      - `is_original`: Whether it is original music
      - `is_commerce_music`: Whether it is commercial music
      - `lyric_url`: Lyrics file URL (if available)
      - `strong_beat_url.url_list`: Beat timing file URLs
      - `tags`: Music tags
        - Themes (e.g., Game, Vlog), Moods (e.g., Funny), Genres (e.g., 8-bit, Electronic)
      - `artists`: List of associated artists (if any)
        - `artist_name`: Artist name
        - `uid`: Artist UID
      - `cover_color_hsv`: Dominant HSV color of the cover
      - `can_background_play`: Whether background playback is supported

    Args:
        body (MusicSearchRequest):

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
    body: MusicSearchRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取音乐搜索/Fetch music search

     # [中文]
    ### 用途:
    - 获取抖音 App 中音乐内容的搜索结果。
    - 支持关键词、排序方式、筛选条件等。

    ### 备注:
    - 本接口专注于音乐类内容搜索，不包含其他类型内容。
    - 初次请求时 `cursor` 传 0，`search_id` 传空字符串。
    - 返回内容包含音乐基本信息、作者信息、封面、播放地址、标签等。

    ### 参数:
    - keyword: 搜索关键词，例如 \"游戏背景音乐\"
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
        \"keyword\": \"游戏背景音乐\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 0,
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `music`: 音乐结果列表
      - `id_str`: 音乐ID（字符串格式）
      - `title`: 音乐标题
      - `author`: 音乐作者昵称
      - `album`: 所属专辑（如果有）
      - `play_url.url_list`: 音乐播放地址列表
      - `duration`: 音乐时长（秒）
      - `cover_thumb.url_list`: 缩略封面图片列表
      - `cover_medium.url_list`: 中尺寸封面图片列表
      - `cover_large.url_list`: 高清封面图片列表
      - `user_count`: 使用该音乐的作品数量
      - `is_original`: 是否原创音乐
      - `is_commerce_music`: 是否为商业授权音乐
      - `lyric_url`: 歌词文件链接（如果有）
      - `strong_beat_url.url_list`: 音乐节奏点文件链接
      - `tags`: 音乐标签
        - 如：主题（如游戏、Vlog）、情绪（如Funny）、风格（如8-bit, Electronic）
      - `artists`: 音乐关联的创作者列表（如果有）
        - `artist_name`: 艺人昵称
        - `uid`: 艺人UID
      - `cover_color_hsv`: 封面主色调HSV值
      - `can_background_play`: 是否支持后台播放

    # [English]
    ### Purpose:
    - Fetch music content search results from Douyin App.
    - Supports filtering by keyword, sort type, etc.

    ### Notes:
    - This API focuses on music content search, excluding other types.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - Response includes music basic info, artist info, covers, play URLs, tags, etc.

    ### Parameters:
    - keyword: Search keyword, e.g., \"game background music\"
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
        - `1-5`: 1 to 5 minutes
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
        \"keyword\": \"game background music\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 0,
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `music`: List of music search results
      - `id_str`: Music ID (as string)
      - `title`: Music title
      - `author`: Music author's nickname
      - `album`: Album name (if any)
      - `play_url.url_list`: List of music play URLs
      - `duration`: Duration in seconds
      - `cover_thumb.url_list`: List of thumbnail cover URLs
      - `cover_medium.url_list`: List of medium-sized cover URLs
      - `cover_large.url_list`: List of large-sized cover URLs
      - `user_count`: Number of videos using this music
      - `is_original`: Whether it is original music
      - `is_commerce_music`: Whether it is commercial music
      - `lyric_url`: Lyrics file URL (if available)
      - `strong_beat_url.url_list`: Beat timing file URLs
      - `tags`: Music tags
        - Themes (e.g., Game, Vlog), Moods (e.g., Funny), Genres (e.g., 8-bit, Electronic)
      - `artists`: List of associated artists (if any)
        - `artist_name`: Artist name
        - `uid`: Artist UID
      - `cover_color_hsv`: Dominant HSV color of the cover
      - `can_background_play`: Whether background playback is supported

    Args:
        body (MusicSearchRequest):

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
    body: MusicSearchRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取音乐搜索/Fetch music search

     # [中文]
    ### 用途:
    - 获取抖音 App 中音乐内容的搜索结果。
    - 支持关键词、排序方式、筛选条件等。

    ### 备注:
    - 本接口专注于音乐类内容搜索，不包含其他类型内容。
    - 初次请求时 `cursor` 传 0，`search_id` 传空字符串。
    - 返回内容包含音乐基本信息、作者信息、封面、播放地址、标签等。

    ### 参数:
    - keyword: 搜索关键词，例如 \"游戏背景音乐\"
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
        \"keyword\": \"游戏背景音乐\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 0,
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `music`: 音乐结果列表
      - `id_str`: 音乐ID（字符串格式）
      - `title`: 音乐标题
      - `author`: 音乐作者昵称
      - `album`: 所属专辑（如果有）
      - `play_url.url_list`: 音乐播放地址列表
      - `duration`: 音乐时长（秒）
      - `cover_thumb.url_list`: 缩略封面图片列表
      - `cover_medium.url_list`: 中尺寸封面图片列表
      - `cover_large.url_list`: 高清封面图片列表
      - `user_count`: 使用该音乐的作品数量
      - `is_original`: 是否原创音乐
      - `is_commerce_music`: 是否为商业授权音乐
      - `lyric_url`: 歌词文件链接（如果有）
      - `strong_beat_url.url_list`: 音乐节奏点文件链接
      - `tags`: 音乐标签
        - 如：主题（如游戏、Vlog）、情绪（如Funny）、风格（如8-bit, Electronic）
      - `artists`: 音乐关联的创作者列表（如果有）
        - `artist_name`: 艺人昵称
        - `uid`: 艺人UID
      - `cover_color_hsv`: 封面主色调HSV值
      - `can_background_play`: 是否支持后台播放

    # [English]
    ### Purpose:
    - Fetch music content search results from Douyin App.
    - Supports filtering by keyword, sort type, etc.

    ### Notes:
    - This API focuses on music content search, excluding other types.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - Response includes music basic info, artist info, covers, play URLs, tags, etc.

    ### Parameters:
    - keyword: Search keyword, e.g., \"game background music\"
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
        - `1-5`: 1 to 5 minutes
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
        \"keyword\": \"game background music\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 0,
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `music`: List of music search results
      - `id_str`: Music ID (as string)
      - `title`: Music title
      - `author`: Music author's nickname
      - `album`: Album name (if any)
      - `play_url.url_list`: List of music play URLs
      - `duration`: Duration in seconds
      - `cover_thumb.url_list`: List of thumbnail cover URLs
      - `cover_medium.url_list`: List of medium-sized cover URLs
      - `cover_large.url_list`: List of large-sized cover URLs
      - `user_count`: Number of videos using this music
      - `is_original`: Whether it is original music
      - `is_commerce_music`: Whether it is commercial music
      - `lyric_url`: Lyrics file URL (if available)
      - `strong_beat_url.url_list`: Beat timing file URLs
      - `tags`: Music tags
        - Themes (e.g., Game, Vlog), Moods (e.g., Funny), Genres (e.g., 8-bit, Electronic)
      - `artists`: List of associated artists (if any)
        - `artist_name`: Artist name
        - `uid`: Artist UID
      - `cover_color_hsv`: Dominant HSV color of the cover
      - `can_background_play`: Whether background playback is supported

    Args:
        body (MusicSearchRequest):

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
