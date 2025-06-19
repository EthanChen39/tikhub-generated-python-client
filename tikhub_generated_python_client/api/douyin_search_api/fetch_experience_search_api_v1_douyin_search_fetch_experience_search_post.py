from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.experience_search_request import ExperienceSearchRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: ExperienceSearchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/search/fetch_experience_search",
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
    body: ExperienceSearchRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取经验搜索/Fetch experience search

     # [中文]
    ### 用途:
    - 获取抖音 App 中经验（知识/教程）内容的搜索结果。
    - 支持通过关键词检索，与经验类内容（如攻略、教程、分享等）相关的视频信息。

    ### 备注:
    - 此接口专注于经验类内容，不包含其他类型的内容。
    - 初次请求时，`cursor` 应传 0，`search_id` 传空字符串，翻页时使用上次响应返回的 cursor 和 search_id。
    - 返回的结果中包含视频详情、作者信息、背景音乐、话题标签、播放地址、互动数据等。

    ### 参数:
    - keyword: 搜索关键词，例如 \"游戏攻略\"
    - cursor: 翻页游标，首次请求传 0
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
    - content_type: 内容类型筛选（通常固定为视频）
    - search_id: 分页查询时需要传上次响应返回的 `search_id`

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"游戏攻略\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 1,
        \"search_id\": \"\"
    }

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - business_data: 搜索结果业务数据列表
      - data_id: 数据块ID
      - type: 数据类型（如 999 表示内容列表）
      - data:
        - height: 显示区域高度
        - aweme_list: 视频列表
          - aweme_id: 视频ID
          - desc: 视频描述内容
          - create_time: 视频发布时间（时间戳）
          - author: 作者信息
            - uid: 作者UID
            - nickname: 作者昵称
            - avatar_thumb.url_list: 作者头像缩略图
            - is_verified: 是否是认证账号
            - follower_count: 粉丝数
          - music: 背景音乐信息
            - id_str: 音乐ID
            - title: 音乐标题
            - author: 音乐作者昵称
          - cha_list: 关联的话题标签列表
            - cha_name: 话题名称
          - video: 视频播放信息
            - play_addr.url_list: 视频播放地址列表
            - cover.url_list: 视频封面图地址
            - width: 视频宽度
            - height: 视频高度
            - duration: 视频时长（单位毫秒）
          - statistics: 视频互动数据
            - digg_count: 点赞数
            - comment_count: 评论数
            - share_count: 分享数
            - play_count: 播放次数
          - status: 视频状态信息
            - is_delete: 是否已删除
            - is_private: 是否私密
          - share_url: 视频外部分享链接

    # [English]
    ### Purpose:
    - Fetch experience (knowledge/tutorial) content search results from Douyin App.
    - Retrieves video results related to knowledge sharing, tutorials, or tips based on the input
    keyword.

    ### Notes:
    - This API focuses on experience-related videos and does not include other content types.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request; for pagination, use
    the previous cursor and search_id.
    - The response includes rich information such as video details, author profile, background music,
    hashtags, video URLs, and engagement statistics.

    ### Parameters:
    - keyword: Search keyword, e.g., \"gaming guide\"
    - cursor: Pagination cursor (0 for first page)
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
    - content_type: Content type filter (usually fixed to video)
    - search_id: Search ID for pagination

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"gaming guide\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 1,
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - business_data: List of business data blocks
      - data_id: Data block ID
      - type: Data type (e.g., 999 for content list)
      - data:
        - height: Display height
        - aweme_list: List of videos
          - aweme_id: Video ID
          - desc: Video description
          - create_time: Creation timestamp
          - author: Author profile
            - uid: User ID
            - nickname: User nickname
            - avatar_thumb.url_list: Thumbnail avatar URLs
            - is_verified: Whether the author is verified
            - follower_count: Number of followers
          - music: Background music information
            - id_str: Music ID
            - title: Music title
            - author: Music author's name
          - cha_list: Associated hashtags
            - cha_name: Hashtag name
          - video: Video playback info
            - play_addr.url_list: List of video play URLs
            - cover.url_list: List of video cover image URLs
            - width: Video width
            - height: Video height
            - duration: Video duration in milliseconds
          - statistics: Video engagement data
            - digg_count: Number of likes
            - comment_count: Number of comments
            - share_count: Number of shares
            - play_count: Number of plays
          - status: Video status information
            - is_delete: Whether the video was deleted
            - is_private: Whether the video is private
          - share_url: External share link of the video

    Args:
        body (ExperienceSearchRequest):

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
    body: ExperienceSearchRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取经验搜索/Fetch experience search

     # [中文]
    ### 用途:
    - 获取抖音 App 中经验（知识/教程）内容的搜索结果。
    - 支持通过关键词检索，与经验类内容（如攻略、教程、分享等）相关的视频信息。

    ### 备注:
    - 此接口专注于经验类内容，不包含其他类型的内容。
    - 初次请求时，`cursor` 应传 0，`search_id` 传空字符串，翻页时使用上次响应返回的 cursor 和 search_id。
    - 返回的结果中包含视频详情、作者信息、背景音乐、话题标签、播放地址、互动数据等。

    ### 参数:
    - keyword: 搜索关键词，例如 \"游戏攻略\"
    - cursor: 翻页游标，首次请求传 0
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
    - content_type: 内容类型筛选（通常固定为视频）
    - search_id: 分页查询时需要传上次响应返回的 `search_id`

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"游戏攻略\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 1,
        \"search_id\": \"\"
    }

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - business_data: 搜索结果业务数据列表
      - data_id: 数据块ID
      - type: 数据类型（如 999 表示内容列表）
      - data:
        - height: 显示区域高度
        - aweme_list: 视频列表
          - aweme_id: 视频ID
          - desc: 视频描述内容
          - create_time: 视频发布时间（时间戳）
          - author: 作者信息
            - uid: 作者UID
            - nickname: 作者昵称
            - avatar_thumb.url_list: 作者头像缩略图
            - is_verified: 是否是认证账号
            - follower_count: 粉丝数
          - music: 背景音乐信息
            - id_str: 音乐ID
            - title: 音乐标题
            - author: 音乐作者昵称
          - cha_list: 关联的话题标签列表
            - cha_name: 话题名称
          - video: 视频播放信息
            - play_addr.url_list: 视频播放地址列表
            - cover.url_list: 视频封面图地址
            - width: 视频宽度
            - height: 视频高度
            - duration: 视频时长（单位毫秒）
          - statistics: 视频互动数据
            - digg_count: 点赞数
            - comment_count: 评论数
            - share_count: 分享数
            - play_count: 播放次数
          - status: 视频状态信息
            - is_delete: 是否已删除
            - is_private: 是否私密
          - share_url: 视频外部分享链接

    # [English]
    ### Purpose:
    - Fetch experience (knowledge/tutorial) content search results from Douyin App.
    - Retrieves video results related to knowledge sharing, tutorials, or tips based on the input
    keyword.

    ### Notes:
    - This API focuses on experience-related videos and does not include other content types.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request; for pagination, use
    the previous cursor and search_id.
    - The response includes rich information such as video details, author profile, background music,
    hashtags, video URLs, and engagement statistics.

    ### Parameters:
    - keyword: Search keyword, e.g., \"gaming guide\"
    - cursor: Pagination cursor (0 for first page)
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
    - content_type: Content type filter (usually fixed to video)
    - search_id: Search ID for pagination

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"gaming guide\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 1,
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - business_data: List of business data blocks
      - data_id: Data block ID
      - type: Data type (e.g., 999 for content list)
      - data:
        - height: Display height
        - aweme_list: List of videos
          - aweme_id: Video ID
          - desc: Video description
          - create_time: Creation timestamp
          - author: Author profile
            - uid: User ID
            - nickname: User nickname
            - avatar_thumb.url_list: Thumbnail avatar URLs
            - is_verified: Whether the author is verified
            - follower_count: Number of followers
          - music: Background music information
            - id_str: Music ID
            - title: Music title
            - author: Music author's name
          - cha_list: Associated hashtags
            - cha_name: Hashtag name
          - video: Video playback info
            - play_addr.url_list: List of video play URLs
            - cover.url_list: List of video cover image URLs
            - width: Video width
            - height: Video height
            - duration: Video duration in milliseconds
          - statistics: Video engagement data
            - digg_count: Number of likes
            - comment_count: Number of comments
            - share_count: Number of shares
            - play_count: Number of plays
          - status: Video status information
            - is_delete: Whether the video was deleted
            - is_private: Whether the video is private
          - share_url: External share link of the video

    Args:
        body (ExperienceSearchRequest):

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
    body: ExperienceSearchRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取经验搜索/Fetch experience search

     # [中文]
    ### 用途:
    - 获取抖音 App 中经验（知识/教程）内容的搜索结果。
    - 支持通过关键词检索，与经验类内容（如攻略、教程、分享等）相关的视频信息。

    ### 备注:
    - 此接口专注于经验类内容，不包含其他类型的内容。
    - 初次请求时，`cursor` 应传 0，`search_id` 传空字符串，翻页时使用上次响应返回的 cursor 和 search_id。
    - 返回的结果中包含视频详情、作者信息、背景音乐、话题标签、播放地址、互动数据等。

    ### 参数:
    - keyword: 搜索关键词，例如 \"游戏攻略\"
    - cursor: 翻页游标，首次请求传 0
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
    - content_type: 内容类型筛选（通常固定为视频）
    - search_id: 分页查询时需要传上次响应返回的 `search_id`

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"游戏攻略\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 1,
        \"search_id\": \"\"
    }

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - business_data: 搜索结果业务数据列表
      - data_id: 数据块ID
      - type: 数据类型（如 999 表示内容列表）
      - data:
        - height: 显示区域高度
        - aweme_list: 视频列表
          - aweme_id: 视频ID
          - desc: 视频描述内容
          - create_time: 视频发布时间（时间戳）
          - author: 作者信息
            - uid: 作者UID
            - nickname: 作者昵称
            - avatar_thumb.url_list: 作者头像缩略图
            - is_verified: 是否是认证账号
            - follower_count: 粉丝数
          - music: 背景音乐信息
            - id_str: 音乐ID
            - title: 音乐标题
            - author: 音乐作者昵称
          - cha_list: 关联的话题标签列表
            - cha_name: 话题名称
          - video: 视频播放信息
            - play_addr.url_list: 视频播放地址列表
            - cover.url_list: 视频封面图地址
            - width: 视频宽度
            - height: 视频高度
            - duration: 视频时长（单位毫秒）
          - statistics: 视频互动数据
            - digg_count: 点赞数
            - comment_count: 评论数
            - share_count: 分享数
            - play_count: 播放次数
          - status: 视频状态信息
            - is_delete: 是否已删除
            - is_private: 是否私密
          - share_url: 视频外部分享链接

    # [English]
    ### Purpose:
    - Fetch experience (knowledge/tutorial) content search results from Douyin App.
    - Retrieves video results related to knowledge sharing, tutorials, or tips based on the input
    keyword.

    ### Notes:
    - This API focuses on experience-related videos and does not include other content types.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request; for pagination, use
    the previous cursor and search_id.
    - The response includes rich information such as video details, author profile, background music,
    hashtags, video URLs, and engagement statistics.

    ### Parameters:
    - keyword: Search keyword, e.g., \"gaming guide\"
    - cursor: Pagination cursor (0 for first page)
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
    - content_type: Content type filter (usually fixed to video)
    - search_id: Search ID for pagination

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"gaming guide\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 1,
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - business_data: List of business data blocks
      - data_id: Data block ID
      - type: Data type (e.g., 999 for content list)
      - data:
        - height: Display height
        - aweme_list: List of videos
          - aweme_id: Video ID
          - desc: Video description
          - create_time: Creation timestamp
          - author: Author profile
            - uid: User ID
            - nickname: User nickname
            - avatar_thumb.url_list: Thumbnail avatar URLs
            - is_verified: Whether the author is verified
            - follower_count: Number of followers
          - music: Background music information
            - id_str: Music ID
            - title: Music title
            - author: Music author's name
          - cha_list: Associated hashtags
            - cha_name: Hashtag name
          - video: Video playback info
            - play_addr.url_list: List of video play URLs
            - cover.url_list: List of video cover image URLs
            - width: Video width
            - height: Video height
            - duration: Video duration in milliseconds
          - statistics: Video engagement data
            - digg_count: Number of likes
            - comment_count: Number of comments
            - share_count: Number of shares
            - play_count: Number of plays
          - status: Video status information
            - is_delete: Whether the video was deleted
            - is_private: Whether the video is private
          - share_url: External share link of the video

    Args:
        body (ExperienceSearchRequest):

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
    body: ExperienceSearchRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取经验搜索/Fetch experience search

     # [中文]
    ### 用途:
    - 获取抖音 App 中经验（知识/教程）内容的搜索结果。
    - 支持通过关键词检索，与经验类内容（如攻略、教程、分享等）相关的视频信息。

    ### 备注:
    - 此接口专注于经验类内容，不包含其他类型的内容。
    - 初次请求时，`cursor` 应传 0，`search_id` 传空字符串，翻页时使用上次响应返回的 cursor 和 search_id。
    - 返回的结果中包含视频详情、作者信息、背景音乐、话题标签、播放地址、互动数据等。

    ### 参数:
    - keyword: 搜索关键词，例如 \"游戏攻略\"
    - cursor: 翻页游标，首次请求传 0
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
    - content_type: 内容类型筛选（通常固定为视频）
    - search_id: 分页查询时需要传上次响应返回的 `search_id`

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"游戏攻略\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 1,
        \"search_id\": \"\"
    }

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - business_data: 搜索结果业务数据列表
      - data_id: 数据块ID
      - type: 数据类型（如 999 表示内容列表）
      - data:
        - height: 显示区域高度
        - aweme_list: 视频列表
          - aweme_id: 视频ID
          - desc: 视频描述内容
          - create_time: 视频发布时间（时间戳）
          - author: 作者信息
            - uid: 作者UID
            - nickname: 作者昵称
            - avatar_thumb.url_list: 作者头像缩略图
            - is_verified: 是否是认证账号
            - follower_count: 粉丝数
          - music: 背景音乐信息
            - id_str: 音乐ID
            - title: 音乐标题
            - author: 音乐作者昵称
          - cha_list: 关联的话题标签列表
            - cha_name: 话题名称
          - video: 视频播放信息
            - play_addr.url_list: 视频播放地址列表
            - cover.url_list: 视频封面图地址
            - width: 视频宽度
            - height: 视频高度
            - duration: 视频时长（单位毫秒）
          - statistics: 视频互动数据
            - digg_count: 点赞数
            - comment_count: 评论数
            - share_count: 分享数
            - play_count: 播放次数
          - status: 视频状态信息
            - is_delete: 是否已删除
            - is_private: 是否私密
          - share_url: 视频外部分享链接

    # [English]
    ### Purpose:
    - Fetch experience (knowledge/tutorial) content search results from Douyin App.
    - Retrieves video results related to knowledge sharing, tutorials, or tips based on the input
    keyword.

    ### Notes:
    - This API focuses on experience-related videos and does not include other content types.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request; for pagination, use
    the previous cursor and search_id.
    - The response includes rich information such as video details, author profile, background music,
    hashtags, video URLs, and engagement statistics.

    ### Parameters:
    - keyword: Search keyword, e.g., \"gaming guide\"
    - cursor: Pagination cursor (0 for first page)
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
    - content_type: Content type filter (usually fixed to video)
    - search_id: Search ID for pagination

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"gaming guide\",
        \"cursor\": 0,
        \"sort_type\": 0,
        \"publish_time\": 0,
        \"filter_duration\": 0,
        \"content_type\": 1,
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - business_data: List of business data blocks
      - data_id: Data block ID
      - type: Data type (e.g., 999 for content list)
      - data:
        - height: Display height
        - aweme_list: List of videos
          - aweme_id: Video ID
          - desc: Video description
          - create_time: Creation timestamp
          - author: Author profile
            - uid: User ID
            - nickname: User nickname
            - avatar_thumb.url_list: Thumbnail avatar URLs
            - is_verified: Whether the author is verified
            - follower_count: Number of followers
          - music: Background music information
            - id_str: Music ID
            - title: Music title
            - author: Music author's name
          - cha_list: Associated hashtags
            - cha_name: Hashtag name
          - video: Video playback info
            - play_addr.url_list: List of video play URLs
            - cover.url_list: List of video cover image URLs
            - width: Video width
            - height: Video height
            - duration: Video duration in milliseconds
          - statistics: Video engagement data
            - digg_count: Number of likes
            - comment_count: Number of comments
            - share_count: Number of shares
            - play_count: Number of plays
          - status: Video status information
            - is_delete: Whether the video was deleted
            - is_private: Whether the video is private
          - share_url: External share link of the video

    Args:
        body (ExperienceSearchRequest):

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
