from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...models.video_search_v2_request import VideoSearchV2Request
from ...types import Response


def _get_kwargs(
    *,
    body: VideoSearchV2Request,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/search/fetch_video_search_v2",
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
    body: VideoSearchV2Request,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频搜索 V2/Fetch video search V2

     # [中文]
    ### 用途:
    - 获取抖音 App 中通过关键词搜索到的视频内容（V2版本接口）。
    - 相较于 V1，返回字段更加详细，包括作者资料、视频多清晰度播放源、标签列表等。

    ### 备注:
    - 初次请求时 `cursor` 传入0，`search_id`传空字符串。
    - 返回的视频内容丰富，可用于推荐展示、内容抓取、智能分析等应用场景。

    ### 参数:
    - keyword: 搜索关键词，如 \"机器人\"
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
        \"keyword\": \"机器人\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"0\",
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `business_data[]`: 搜索返回的数据列表
      - `data_id`: 数据编号（字符串，如 \"0\"）
      - `type`: 数据类型（1=视频）
      - `data`:
        - `type`: 同上（1）
        - `aweme_info`: 视频详细信息
          - 基础信息:
            - `aweme_id`: 视频ID
            - `desc`: 视频描述
            - `create_time`: 发布时间（时间戳）
          - 作者信息 (`author`):
            - `uid`: 用户唯一ID
            - `short_id`: 用户短ID
            - `nickname`: 用户昵称
            - `signature`: 个性签名
            - `follower_count`: 粉丝数
            - `is_verified`: 是否认证
            - `region`: 地区，如 \"CN\"
            - `avatar_thumb.url_list`: 小头像URL列表
            - `avatar_medium.url_list`: 中头像URL列表
            - `avatar_larger.url_list`: 大头像URL列表
            - `enterprise_verify_reason`: 企业认证信息（如\"店铺账号\"）
          - 背景音乐 (`music`):
            - `id_str`: 音乐ID
            - `title`: 音乐标题
            - `author`: 音乐创作者昵称
            - `play_url.url_list`: 音乐播放链接列表
          - 视频播放信息 (`video`):
            - `play_addr.url_list`: 播放地址列表（支持高清播放）
            - `cover.url_list`: 封面图片列表
            - `dynamic_cover.url_list`: 动态封面列表
            - `origin_cover.url_list`: 原始封面列表
            - `duration`: 时长（毫秒）
            - `ratio`: 分辨率（如\"720p\"）
            - `bit_rate[]`: 多码率播放信息
              - `gear_name`: 清晰度名称（如\"540_2_2\"）
              - `bit_rate`: 码率（单位bps）
              - `play_addr.url_list`: 对应清晰度播放地址列表
          - 标签列表 (`cha_list[]`):
            - `cha_name`: 话题名（如 \"#宇树科技\"）
            - `cid`: 话题ID
            - `share_url`: 话题分享链接
          - 统计信息 (`statistics`):
            - `comment_count`: 评论数
            - `digg_count`: 点赞数
            - `share_count`: 分享数
            - `play_count`: 播放次数
            - `collect_count`: 收藏次数
          - 状态信息 (`status`):
            - `is_delete`: 是否被删除
            - `is_private`: 是否私密
            - `allow_share`: 是否允许分享
            - `allow_comment`: 是否允许评论
          - 其他字段:
            - `share_url`: 视频外链
            - `user_digged`: 当前用户是否点赞（0=否，1=是）

    - `cursor`: 翻页游标（用于下次请求）
    - `has_more`: 是否还有更多数据（1=有，0=无）

    # [English]
    ### Purpose:
    - Fetch video search results from Douyin App using V2 API version.
    - Compared to V1, returns more detailed information including author details, multi-resolution video
    sources, and hashtags.

    ### Notes:
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - The response contains rich video data, suitable for display, content scraping, or intelligent
    analysis.

    ### Parameters:
    - keyword: Search keyword, e.g., \"robot\"
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
        \"keyword\": \"robot\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"0\",
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `business_data[]`: List of returned data items
      - `data_id`: Data ID (string, e.g., \"0\")
      - `type`: Data type (1=Video)
      - `data`:
        - `type`: Same as above (1)
        - `aweme_info`: Detailed video information
          - Basic Info:
            - `aweme_id`: Video ID
            - `desc`: Video description
            - `create_time`: Creation timestamp
          - Author Info (`author`):
            - `uid`: Unique User ID
            - `short_id`: Short ID
            - `nickname`: Nickname
            - `signature`: Bio
            - `follower_count`: Follower count
            - `is_verified`: Whether verified
            - `region`: Region, e.g., \"CN\"
            - `avatar_thumb.url_list`: Thumbnail avatar URLs
            - `avatar_medium.url_list`: Medium avatar URLs
            - `avatar_larger.url_list`: Large avatar URLs
            - `enterprise_verify_reason`: Enterprise verification info
          - Music (`music`):
            - `id_str`: Music ID
            - `title`: Music title
            - `author`: Music creator nickname
            - `play_url.url_list`: List of play URLs
          - Video (`video`):
            - `play_addr.url_list`: Play URLs (supports HD)
            - `cover.url_list`: Cover images
            - `dynamic_cover.url_list`: Dynamic covers
            - `origin_cover.url_list`: Original covers
            - `duration`: Duration (milliseconds)
            - `ratio`: Resolution (e.g., \"720p\")
            - `bit_rate[]`: Multiple bitrates
              - `gear_name`: Gear name
              - `bit_rate`: Bitrate (bps)
              - `play_addr.url_list`: Play URLs
          - Hashtags (`cha_list[]`):
            - `cha_name`: Hashtag name (e.g., \"#UnitreeRobot\")
            - `cid`: Hashtag ID
            - `share_url`: Hashtag share link
          - Statistics (`statistics`):
            - `comment_count`: Number of comments
            - `digg_count`: Number of likes
            - `share_count`: Number of shares
            - `play_count`: Number of plays
            - `collect_count`: Number of collects
          - Status (`status`):
            - `is_delete`: Whether deleted
            - `is_private`: Whether private
            - `allow_share`: Whether sharing is allowed
            - `allow_comment`: Whether commenting is allowed
          - Other fields:
            - `share_url`: Video external share link
            - `user_digged`: Whether the user has liked (0=No, 1=Yes)

    - `cursor`: Cursor for next page
    - `has_more`: Whether more data is available (1=Yes, 0=No)

    Args:
        body (VideoSearchV2Request):

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
    body: VideoSearchV2Request,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频搜索 V2/Fetch video search V2

     # [中文]
    ### 用途:
    - 获取抖音 App 中通过关键词搜索到的视频内容（V2版本接口）。
    - 相较于 V1，返回字段更加详细，包括作者资料、视频多清晰度播放源、标签列表等。

    ### 备注:
    - 初次请求时 `cursor` 传入0，`search_id`传空字符串。
    - 返回的视频内容丰富，可用于推荐展示、内容抓取、智能分析等应用场景。

    ### 参数:
    - keyword: 搜索关键词，如 \"机器人\"
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
        \"keyword\": \"机器人\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"0\",
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `business_data[]`: 搜索返回的数据列表
      - `data_id`: 数据编号（字符串，如 \"0\"）
      - `type`: 数据类型（1=视频）
      - `data`:
        - `type`: 同上（1）
        - `aweme_info`: 视频详细信息
          - 基础信息:
            - `aweme_id`: 视频ID
            - `desc`: 视频描述
            - `create_time`: 发布时间（时间戳）
          - 作者信息 (`author`):
            - `uid`: 用户唯一ID
            - `short_id`: 用户短ID
            - `nickname`: 用户昵称
            - `signature`: 个性签名
            - `follower_count`: 粉丝数
            - `is_verified`: 是否认证
            - `region`: 地区，如 \"CN\"
            - `avatar_thumb.url_list`: 小头像URL列表
            - `avatar_medium.url_list`: 中头像URL列表
            - `avatar_larger.url_list`: 大头像URL列表
            - `enterprise_verify_reason`: 企业认证信息（如\"店铺账号\"）
          - 背景音乐 (`music`):
            - `id_str`: 音乐ID
            - `title`: 音乐标题
            - `author`: 音乐创作者昵称
            - `play_url.url_list`: 音乐播放链接列表
          - 视频播放信息 (`video`):
            - `play_addr.url_list`: 播放地址列表（支持高清播放）
            - `cover.url_list`: 封面图片列表
            - `dynamic_cover.url_list`: 动态封面列表
            - `origin_cover.url_list`: 原始封面列表
            - `duration`: 时长（毫秒）
            - `ratio`: 分辨率（如\"720p\"）
            - `bit_rate[]`: 多码率播放信息
              - `gear_name`: 清晰度名称（如\"540_2_2\"）
              - `bit_rate`: 码率（单位bps）
              - `play_addr.url_list`: 对应清晰度播放地址列表
          - 标签列表 (`cha_list[]`):
            - `cha_name`: 话题名（如 \"#宇树科技\"）
            - `cid`: 话题ID
            - `share_url`: 话题分享链接
          - 统计信息 (`statistics`):
            - `comment_count`: 评论数
            - `digg_count`: 点赞数
            - `share_count`: 分享数
            - `play_count`: 播放次数
            - `collect_count`: 收藏次数
          - 状态信息 (`status`):
            - `is_delete`: 是否被删除
            - `is_private`: 是否私密
            - `allow_share`: 是否允许分享
            - `allow_comment`: 是否允许评论
          - 其他字段:
            - `share_url`: 视频外链
            - `user_digged`: 当前用户是否点赞（0=否，1=是）

    - `cursor`: 翻页游标（用于下次请求）
    - `has_more`: 是否还有更多数据（1=有，0=无）

    # [English]
    ### Purpose:
    - Fetch video search results from Douyin App using V2 API version.
    - Compared to V1, returns more detailed information including author details, multi-resolution video
    sources, and hashtags.

    ### Notes:
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - The response contains rich video data, suitable for display, content scraping, or intelligent
    analysis.

    ### Parameters:
    - keyword: Search keyword, e.g., \"robot\"
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
        \"keyword\": \"robot\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"0\",
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `business_data[]`: List of returned data items
      - `data_id`: Data ID (string, e.g., \"0\")
      - `type`: Data type (1=Video)
      - `data`:
        - `type`: Same as above (1)
        - `aweme_info`: Detailed video information
          - Basic Info:
            - `aweme_id`: Video ID
            - `desc`: Video description
            - `create_time`: Creation timestamp
          - Author Info (`author`):
            - `uid`: Unique User ID
            - `short_id`: Short ID
            - `nickname`: Nickname
            - `signature`: Bio
            - `follower_count`: Follower count
            - `is_verified`: Whether verified
            - `region`: Region, e.g., \"CN\"
            - `avatar_thumb.url_list`: Thumbnail avatar URLs
            - `avatar_medium.url_list`: Medium avatar URLs
            - `avatar_larger.url_list`: Large avatar URLs
            - `enterprise_verify_reason`: Enterprise verification info
          - Music (`music`):
            - `id_str`: Music ID
            - `title`: Music title
            - `author`: Music creator nickname
            - `play_url.url_list`: List of play URLs
          - Video (`video`):
            - `play_addr.url_list`: Play URLs (supports HD)
            - `cover.url_list`: Cover images
            - `dynamic_cover.url_list`: Dynamic covers
            - `origin_cover.url_list`: Original covers
            - `duration`: Duration (milliseconds)
            - `ratio`: Resolution (e.g., \"720p\")
            - `bit_rate[]`: Multiple bitrates
              - `gear_name`: Gear name
              - `bit_rate`: Bitrate (bps)
              - `play_addr.url_list`: Play URLs
          - Hashtags (`cha_list[]`):
            - `cha_name`: Hashtag name (e.g., \"#UnitreeRobot\")
            - `cid`: Hashtag ID
            - `share_url`: Hashtag share link
          - Statistics (`statistics`):
            - `comment_count`: Number of comments
            - `digg_count`: Number of likes
            - `share_count`: Number of shares
            - `play_count`: Number of plays
            - `collect_count`: Number of collects
          - Status (`status`):
            - `is_delete`: Whether deleted
            - `is_private`: Whether private
            - `allow_share`: Whether sharing is allowed
            - `allow_comment`: Whether commenting is allowed
          - Other fields:
            - `share_url`: Video external share link
            - `user_digged`: Whether the user has liked (0=No, 1=Yes)

    - `cursor`: Cursor for next page
    - `has_more`: Whether more data is available (1=Yes, 0=No)

    Args:
        body (VideoSearchV2Request):

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
    body: VideoSearchV2Request,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频搜索 V2/Fetch video search V2

     # [中文]
    ### 用途:
    - 获取抖音 App 中通过关键词搜索到的视频内容（V2版本接口）。
    - 相较于 V1，返回字段更加详细，包括作者资料、视频多清晰度播放源、标签列表等。

    ### 备注:
    - 初次请求时 `cursor` 传入0，`search_id`传空字符串。
    - 返回的视频内容丰富，可用于推荐展示、内容抓取、智能分析等应用场景。

    ### 参数:
    - keyword: 搜索关键词，如 \"机器人\"
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
        \"keyword\": \"机器人\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"0\",
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `business_data[]`: 搜索返回的数据列表
      - `data_id`: 数据编号（字符串，如 \"0\"）
      - `type`: 数据类型（1=视频）
      - `data`:
        - `type`: 同上（1）
        - `aweme_info`: 视频详细信息
          - 基础信息:
            - `aweme_id`: 视频ID
            - `desc`: 视频描述
            - `create_time`: 发布时间（时间戳）
          - 作者信息 (`author`):
            - `uid`: 用户唯一ID
            - `short_id`: 用户短ID
            - `nickname`: 用户昵称
            - `signature`: 个性签名
            - `follower_count`: 粉丝数
            - `is_verified`: 是否认证
            - `region`: 地区，如 \"CN\"
            - `avatar_thumb.url_list`: 小头像URL列表
            - `avatar_medium.url_list`: 中头像URL列表
            - `avatar_larger.url_list`: 大头像URL列表
            - `enterprise_verify_reason`: 企业认证信息（如\"店铺账号\"）
          - 背景音乐 (`music`):
            - `id_str`: 音乐ID
            - `title`: 音乐标题
            - `author`: 音乐创作者昵称
            - `play_url.url_list`: 音乐播放链接列表
          - 视频播放信息 (`video`):
            - `play_addr.url_list`: 播放地址列表（支持高清播放）
            - `cover.url_list`: 封面图片列表
            - `dynamic_cover.url_list`: 动态封面列表
            - `origin_cover.url_list`: 原始封面列表
            - `duration`: 时长（毫秒）
            - `ratio`: 分辨率（如\"720p\"）
            - `bit_rate[]`: 多码率播放信息
              - `gear_name`: 清晰度名称（如\"540_2_2\"）
              - `bit_rate`: 码率（单位bps）
              - `play_addr.url_list`: 对应清晰度播放地址列表
          - 标签列表 (`cha_list[]`):
            - `cha_name`: 话题名（如 \"#宇树科技\"）
            - `cid`: 话题ID
            - `share_url`: 话题分享链接
          - 统计信息 (`statistics`):
            - `comment_count`: 评论数
            - `digg_count`: 点赞数
            - `share_count`: 分享数
            - `play_count`: 播放次数
            - `collect_count`: 收藏次数
          - 状态信息 (`status`):
            - `is_delete`: 是否被删除
            - `is_private`: 是否私密
            - `allow_share`: 是否允许分享
            - `allow_comment`: 是否允许评论
          - 其他字段:
            - `share_url`: 视频外链
            - `user_digged`: 当前用户是否点赞（0=否，1=是）

    - `cursor`: 翻页游标（用于下次请求）
    - `has_more`: 是否还有更多数据（1=有，0=无）

    # [English]
    ### Purpose:
    - Fetch video search results from Douyin App using V2 API version.
    - Compared to V1, returns more detailed information including author details, multi-resolution video
    sources, and hashtags.

    ### Notes:
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - The response contains rich video data, suitable for display, content scraping, or intelligent
    analysis.

    ### Parameters:
    - keyword: Search keyword, e.g., \"robot\"
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
        \"keyword\": \"robot\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"0\",
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `business_data[]`: List of returned data items
      - `data_id`: Data ID (string, e.g., \"0\")
      - `type`: Data type (1=Video)
      - `data`:
        - `type`: Same as above (1)
        - `aweme_info`: Detailed video information
          - Basic Info:
            - `aweme_id`: Video ID
            - `desc`: Video description
            - `create_time`: Creation timestamp
          - Author Info (`author`):
            - `uid`: Unique User ID
            - `short_id`: Short ID
            - `nickname`: Nickname
            - `signature`: Bio
            - `follower_count`: Follower count
            - `is_verified`: Whether verified
            - `region`: Region, e.g., \"CN\"
            - `avatar_thumb.url_list`: Thumbnail avatar URLs
            - `avatar_medium.url_list`: Medium avatar URLs
            - `avatar_larger.url_list`: Large avatar URLs
            - `enterprise_verify_reason`: Enterprise verification info
          - Music (`music`):
            - `id_str`: Music ID
            - `title`: Music title
            - `author`: Music creator nickname
            - `play_url.url_list`: List of play URLs
          - Video (`video`):
            - `play_addr.url_list`: Play URLs (supports HD)
            - `cover.url_list`: Cover images
            - `dynamic_cover.url_list`: Dynamic covers
            - `origin_cover.url_list`: Original covers
            - `duration`: Duration (milliseconds)
            - `ratio`: Resolution (e.g., \"720p\")
            - `bit_rate[]`: Multiple bitrates
              - `gear_name`: Gear name
              - `bit_rate`: Bitrate (bps)
              - `play_addr.url_list`: Play URLs
          - Hashtags (`cha_list[]`):
            - `cha_name`: Hashtag name (e.g., \"#UnitreeRobot\")
            - `cid`: Hashtag ID
            - `share_url`: Hashtag share link
          - Statistics (`statistics`):
            - `comment_count`: Number of comments
            - `digg_count`: Number of likes
            - `share_count`: Number of shares
            - `play_count`: Number of plays
            - `collect_count`: Number of collects
          - Status (`status`):
            - `is_delete`: Whether deleted
            - `is_private`: Whether private
            - `allow_share`: Whether sharing is allowed
            - `allow_comment`: Whether commenting is allowed
          - Other fields:
            - `share_url`: Video external share link
            - `user_digged`: Whether the user has liked (0=No, 1=Yes)

    - `cursor`: Cursor for next page
    - `has_more`: Whether more data is available (1=Yes, 0=No)

    Args:
        body (VideoSearchV2Request):

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
    body: VideoSearchV2Request,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频搜索 V2/Fetch video search V2

     # [中文]
    ### 用途:
    - 获取抖音 App 中通过关键词搜索到的视频内容（V2版本接口）。
    - 相较于 V1，返回字段更加详细，包括作者资料、视频多清晰度播放源、标签列表等。

    ### 备注:
    - 初次请求时 `cursor` 传入0，`search_id`传空字符串。
    - 返回的视频内容丰富，可用于推荐展示、内容抓取、智能分析等应用场景。

    ### 参数:
    - keyword: 搜索关键词，如 \"机器人\"
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
        \"keyword\": \"机器人\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"0\",
        \"search_id\": \"\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `business_data[]`: 搜索返回的数据列表
      - `data_id`: 数据编号（字符串，如 \"0\"）
      - `type`: 数据类型（1=视频）
      - `data`:
        - `type`: 同上（1）
        - `aweme_info`: 视频详细信息
          - 基础信息:
            - `aweme_id`: 视频ID
            - `desc`: 视频描述
            - `create_time`: 发布时间（时间戳）
          - 作者信息 (`author`):
            - `uid`: 用户唯一ID
            - `short_id`: 用户短ID
            - `nickname`: 用户昵称
            - `signature`: 个性签名
            - `follower_count`: 粉丝数
            - `is_verified`: 是否认证
            - `region`: 地区，如 \"CN\"
            - `avatar_thumb.url_list`: 小头像URL列表
            - `avatar_medium.url_list`: 中头像URL列表
            - `avatar_larger.url_list`: 大头像URL列表
            - `enterprise_verify_reason`: 企业认证信息（如\"店铺账号\"）
          - 背景音乐 (`music`):
            - `id_str`: 音乐ID
            - `title`: 音乐标题
            - `author`: 音乐创作者昵称
            - `play_url.url_list`: 音乐播放链接列表
          - 视频播放信息 (`video`):
            - `play_addr.url_list`: 播放地址列表（支持高清播放）
            - `cover.url_list`: 封面图片列表
            - `dynamic_cover.url_list`: 动态封面列表
            - `origin_cover.url_list`: 原始封面列表
            - `duration`: 时长（毫秒）
            - `ratio`: 分辨率（如\"720p\"）
            - `bit_rate[]`: 多码率播放信息
              - `gear_name`: 清晰度名称（如\"540_2_2\"）
              - `bit_rate`: 码率（单位bps）
              - `play_addr.url_list`: 对应清晰度播放地址列表
          - 标签列表 (`cha_list[]`):
            - `cha_name`: 话题名（如 \"#宇树科技\"）
            - `cid`: 话题ID
            - `share_url`: 话题分享链接
          - 统计信息 (`statistics`):
            - `comment_count`: 评论数
            - `digg_count`: 点赞数
            - `share_count`: 分享数
            - `play_count`: 播放次数
            - `collect_count`: 收藏次数
          - 状态信息 (`status`):
            - `is_delete`: 是否被删除
            - `is_private`: 是否私密
            - `allow_share`: 是否允许分享
            - `allow_comment`: 是否允许评论
          - 其他字段:
            - `share_url`: 视频外链
            - `user_digged`: 当前用户是否点赞（0=否，1=是）

    - `cursor`: 翻页游标（用于下次请求）
    - `has_more`: 是否还有更多数据（1=有，0=无）

    # [English]
    ### Purpose:
    - Fetch video search results from Douyin App using V2 API version.
    - Compared to V1, returns more detailed information including author details, multi-resolution video
    sources, and hashtags.

    ### Notes:
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.
    - The response contains rich video data, suitable for display, content scraping, or intelligent
    analysis.

    ### Parameters:
    - keyword: Search keyword, e.g., \"robot\"
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
        \"keyword\": \"robot\",
        \"cursor\": 0,
        \"sort_type\": \"0\",
        \"publish_time\": \"0\",
        \"filter_duration\": \"0\",
        \"content_type\": \"0\",
        \"search_id\": \"\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `business_data[]`: List of returned data items
      - `data_id`: Data ID (string, e.g., \"0\")
      - `type`: Data type (1=Video)
      - `data`:
        - `type`: Same as above (1)
        - `aweme_info`: Detailed video information
          - Basic Info:
            - `aweme_id`: Video ID
            - `desc`: Video description
            - `create_time`: Creation timestamp
          - Author Info (`author`):
            - `uid`: Unique User ID
            - `short_id`: Short ID
            - `nickname`: Nickname
            - `signature`: Bio
            - `follower_count`: Follower count
            - `is_verified`: Whether verified
            - `region`: Region, e.g., \"CN\"
            - `avatar_thumb.url_list`: Thumbnail avatar URLs
            - `avatar_medium.url_list`: Medium avatar URLs
            - `avatar_larger.url_list`: Large avatar URLs
            - `enterprise_verify_reason`: Enterprise verification info
          - Music (`music`):
            - `id_str`: Music ID
            - `title`: Music title
            - `author`: Music creator nickname
            - `play_url.url_list`: List of play URLs
          - Video (`video`):
            - `play_addr.url_list`: Play URLs (supports HD)
            - `cover.url_list`: Cover images
            - `dynamic_cover.url_list`: Dynamic covers
            - `origin_cover.url_list`: Original covers
            - `duration`: Duration (milliseconds)
            - `ratio`: Resolution (e.g., \"720p\")
            - `bit_rate[]`: Multiple bitrates
              - `gear_name`: Gear name
              - `bit_rate`: Bitrate (bps)
              - `play_addr.url_list`: Play URLs
          - Hashtags (`cha_list[]`):
            - `cha_name`: Hashtag name (e.g., \"#UnitreeRobot\")
            - `cid`: Hashtag ID
            - `share_url`: Hashtag share link
          - Statistics (`statistics`):
            - `comment_count`: Number of comments
            - `digg_count`: Number of likes
            - `share_count`: Number of shares
            - `play_count`: Number of plays
            - `collect_count`: Number of collects
          - Status (`status`):
            - `is_delete`: Whether deleted
            - `is_private`: Whether private
            - `allow_share`: Whether sharing is allowed
            - `allow_comment`: Whether commenting is allowed
          - Other fields:
            - `share_url`: Video external share link
            - `user_digged`: Whether the user has liked (0=No, 1=Yes)

    - `cursor`: Cursor for next page
    - `has_more`: Whether more data is available (1=Yes, 0=No)

    Args:
        body (VideoSearchV2Request):

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
