from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    clip_id: str,
    period: Union[Unset, int] = 120,
    country_code: Union[Unset, str] = "US",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["clip_id"] = clip_id

    params["period"] = period

    params["country_code"] = country_code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/get_sound_detail",
        "params": params,
    }

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
    clip_id: str,
    period: Union[Unset, int] = 120,
    country_code: Union[Unset, str] = "US",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取音乐详情/Get sound detail

     # [中文]
    ### 用途:
    - 获取特定音乐的详细信息和使用数据
    - 分析音乐的受众分布、使用趋势等多维度数据
    - 帮助选择合适的背景音乐提升广告效果

    ### 参数:
    - clip_id: 音乐ID，必填参数
    - period: 时间范围（天），如7、30、120天
    - country_code: 国家代码，如US、UK、JP等

    ### 返回内容说明:
    - `disliked`: 是否不喜欢（可能为null）
    - `like_count`: 点赞数（可能为null）
    - `liked`: 是否点赞（可能为null）
    - `sound`: 音乐详细信息
      - `audience_ages`: 受众年龄分布
        - `age_level`: 年龄级别
        - `score`: 分数
      - `audience_countries`: 受众国家分布
        - `country_info`: 国家信息
          - `id`: 国家ID
          - `label`: 国家标签
          - `value`: 国家名称
        - `score`: 分数
      - `audience_interests`: 受众兴趣分布
        - `interest_info`: 兴趣信息
        - `score`: 分数
      - `author`: 音乐作者
      - `clip_id`: 片段ID
      - `country_code`: 国家代码
      - `cover`: 封面图URL
      - `duration`: 时长（秒）
      - `if_cml`: 是否商业音乐
      - `is_search`: 是否搜索结果
      - `link`: 音乐链接
      - `longevity`: 持久度信息
        - `popular_days`: 流行天数
        - `current_popularity`: 当前流行度
      - `music_url`: 音乐播放URL（可能为null）
      - `on_list_times`: 上榜次数（可能为null）
      - `promoted`: 是否推广
      - `rank`: 排名（可能为null）
      - `rank_diff`: 排名变化（可能为null）
      - `related_items`: 相关视频列表
        - `item_id`: 视频ID
        - `cover_uri`: 封面URI
      - `song_id`: 歌曲ID
      - `title`: 音乐标题
      - `trend`: 趋势数据
        - `time`: 时间戳
        - `value`: 数值
      - `url_title`: URL标题

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_detail\",
      \"params\": {
        \"clip_id\": \"7251810329461147649\",
        \"period\": 120,
        \"country_code\": \"US\"
      },
      \"data\": {
        \"sound\": {
          \"title\": \"Upbeat Summer Vibes\",
          \"author\": \"Music Producer\",
          \"duration\": 30,
          \"music_url\": \"https://music.tiktok.com/xxx\",
          \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/xxx\",
          \"audience_ages\": [
            {\"age_level\": \"18-24\", \"percentage\": 45.2},
            {\"age_level\": \"25-34\", \"percentage\": 32.8}
          ],
          \"audience_countries\": [
            {\"country\": \"US\", \"percentage\": 35.6},
            {\"country\": \"UK\", \"percentage\": 18.4}
          ],
          \"related_items\": [\"7213258221116751874\", \"7213258221116751875\"],
          \"usage_trend\": [
            {\"date\": \"2025-01-01\", \"count\": 1234},
            {\"date\": \"2025-01-02\", \"count\": 1456}
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get detailed information and usage data for specific music
    - Analyze multi-dimensional data like audience distribution and usage trends
    - Help select appropriate background music to enhance ad effectiveness

    ### Parameters:
    - clip_id: Sound clip ID, required parameter
    - period: Time period in days, e.g., 7, 30, 120 days
    - country_code: Country code, e.g., US, UK, JP

    ### Return Description:
    - `sound`: Sound detailed information
      - `title`: Music title
      - `author`: Music author/artist
      - `duration`: Duration in seconds
      - `music_url`: Music playback URL
      - `cover_url`: Cover image URL
      - `audience_ages`: Audience age distribution
        - `age_level`: Age range
        - `percentage`: Share percentage
      - `audience_countries`: Audience country distribution
        - `country`: Country code
        - `percentage`: Share percentage
      - `related_items`: List of popular video IDs using this music
      - `usage_trend`: Usage trend data

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_detail\",
      \"params\": {
        \"clip_id\": \"7251810329461147649\",
        \"period\": 120,
        \"country_code\": \"US\"
      },
      \"data\": {
        \"sound\": {
          \"title\": \"Upbeat Summer Vibes\",
          \"author\": \"Music Producer\",
          \"duration\": 30,
          \"music_url\": \"https://music.tiktok.com/xxx\",
          \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/xxx\",
          \"audience_ages\": [
            {\"age_level\": \"18-24\", \"percentage\": 45.2},
            {\"age_level\": \"25-34\", \"percentage\": 32.8}
          ],
          \"audience_countries\": [
            {\"country\": \"US\", \"percentage\": 35.6},
            {\"country\": \"UK\", \"percentage\": 18.4}
          ],
          \"related_items\": [\"7213258221116751874\", \"7213258221116751875\"],
          \"usage_trend\": [
            {\"date\": \"2025-01-01\", \"count\": 1234},
            {\"date\": \"2025-01-02\", \"count\": 1456}
          ]
        }
      }
    }
    ```

    Args:
        clip_id (str): 音乐ID/Sound clip ID
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 120.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        clip_id=clip_id,
        period=period,
        country_code=country_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    clip_id: str,
    period: Union[Unset, int] = 120,
    country_code: Union[Unset, str] = "US",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取音乐详情/Get sound detail

     # [中文]
    ### 用途:
    - 获取特定音乐的详细信息和使用数据
    - 分析音乐的受众分布、使用趋势等多维度数据
    - 帮助选择合适的背景音乐提升广告效果

    ### 参数:
    - clip_id: 音乐ID，必填参数
    - period: 时间范围（天），如7、30、120天
    - country_code: 国家代码，如US、UK、JP等

    ### 返回内容说明:
    - `disliked`: 是否不喜欢（可能为null）
    - `like_count`: 点赞数（可能为null）
    - `liked`: 是否点赞（可能为null）
    - `sound`: 音乐详细信息
      - `audience_ages`: 受众年龄分布
        - `age_level`: 年龄级别
        - `score`: 分数
      - `audience_countries`: 受众国家分布
        - `country_info`: 国家信息
          - `id`: 国家ID
          - `label`: 国家标签
          - `value`: 国家名称
        - `score`: 分数
      - `audience_interests`: 受众兴趣分布
        - `interest_info`: 兴趣信息
        - `score`: 分数
      - `author`: 音乐作者
      - `clip_id`: 片段ID
      - `country_code`: 国家代码
      - `cover`: 封面图URL
      - `duration`: 时长（秒）
      - `if_cml`: 是否商业音乐
      - `is_search`: 是否搜索结果
      - `link`: 音乐链接
      - `longevity`: 持久度信息
        - `popular_days`: 流行天数
        - `current_popularity`: 当前流行度
      - `music_url`: 音乐播放URL（可能为null）
      - `on_list_times`: 上榜次数（可能为null）
      - `promoted`: 是否推广
      - `rank`: 排名（可能为null）
      - `rank_diff`: 排名变化（可能为null）
      - `related_items`: 相关视频列表
        - `item_id`: 视频ID
        - `cover_uri`: 封面URI
      - `song_id`: 歌曲ID
      - `title`: 音乐标题
      - `trend`: 趋势数据
        - `time`: 时间戳
        - `value`: 数值
      - `url_title`: URL标题

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_detail\",
      \"params\": {
        \"clip_id\": \"7251810329461147649\",
        \"period\": 120,
        \"country_code\": \"US\"
      },
      \"data\": {
        \"sound\": {
          \"title\": \"Upbeat Summer Vibes\",
          \"author\": \"Music Producer\",
          \"duration\": 30,
          \"music_url\": \"https://music.tiktok.com/xxx\",
          \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/xxx\",
          \"audience_ages\": [
            {\"age_level\": \"18-24\", \"percentage\": 45.2},
            {\"age_level\": \"25-34\", \"percentage\": 32.8}
          ],
          \"audience_countries\": [
            {\"country\": \"US\", \"percentage\": 35.6},
            {\"country\": \"UK\", \"percentage\": 18.4}
          ],
          \"related_items\": [\"7213258221116751874\", \"7213258221116751875\"],
          \"usage_trend\": [
            {\"date\": \"2025-01-01\", \"count\": 1234},
            {\"date\": \"2025-01-02\", \"count\": 1456}
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get detailed information and usage data for specific music
    - Analyze multi-dimensional data like audience distribution and usage trends
    - Help select appropriate background music to enhance ad effectiveness

    ### Parameters:
    - clip_id: Sound clip ID, required parameter
    - period: Time period in days, e.g., 7, 30, 120 days
    - country_code: Country code, e.g., US, UK, JP

    ### Return Description:
    - `sound`: Sound detailed information
      - `title`: Music title
      - `author`: Music author/artist
      - `duration`: Duration in seconds
      - `music_url`: Music playback URL
      - `cover_url`: Cover image URL
      - `audience_ages`: Audience age distribution
        - `age_level`: Age range
        - `percentage`: Share percentage
      - `audience_countries`: Audience country distribution
        - `country`: Country code
        - `percentage`: Share percentage
      - `related_items`: List of popular video IDs using this music
      - `usage_trend`: Usage trend data

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_detail\",
      \"params\": {
        \"clip_id\": \"7251810329461147649\",
        \"period\": 120,
        \"country_code\": \"US\"
      },
      \"data\": {
        \"sound\": {
          \"title\": \"Upbeat Summer Vibes\",
          \"author\": \"Music Producer\",
          \"duration\": 30,
          \"music_url\": \"https://music.tiktok.com/xxx\",
          \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/xxx\",
          \"audience_ages\": [
            {\"age_level\": \"18-24\", \"percentage\": 45.2},
            {\"age_level\": \"25-34\", \"percentage\": 32.8}
          ],
          \"audience_countries\": [
            {\"country\": \"US\", \"percentage\": 35.6},
            {\"country\": \"UK\", \"percentage\": 18.4}
          ],
          \"related_items\": [\"7213258221116751874\", \"7213258221116751875\"],
          \"usage_trend\": [
            {\"date\": \"2025-01-01\", \"count\": 1234},
            {\"date\": \"2025-01-02\", \"count\": 1456}
          ]
        }
      }
    }
    ```

    Args:
        clip_id (str): 音乐ID/Sound clip ID
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 120.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        clip_id=clip_id,
        period=period,
        country_code=country_code,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    clip_id: str,
    period: Union[Unset, int] = 120,
    country_code: Union[Unset, str] = "US",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取音乐详情/Get sound detail

     # [中文]
    ### 用途:
    - 获取特定音乐的详细信息和使用数据
    - 分析音乐的受众分布、使用趋势等多维度数据
    - 帮助选择合适的背景音乐提升广告效果

    ### 参数:
    - clip_id: 音乐ID，必填参数
    - period: 时间范围（天），如7、30、120天
    - country_code: 国家代码，如US、UK、JP等

    ### 返回内容说明:
    - `disliked`: 是否不喜欢（可能为null）
    - `like_count`: 点赞数（可能为null）
    - `liked`: 是否点赞（可能为null）
    - `sound`: 音乐详细信息
      - `audience_ages`: 受众年龄分布
        - `age_level`: 年龄级别
        - `score`: 分数
      - `audience_countries`: 受众国家分布
        - `country_info`: 国家信息
          - `id`: 国家ID
          - `label`: 国家标签
          - `value`: 国家名称
        - `score`: 分数
      - `audience_interests`: 受众兴趣分布
        - `interest_info`: 兴趣信息
        - `score`: 分数
      - `author`: 音乐作者
      - `clip_id`: 片段ID
      - `country_code`: 国家代码
      - `cover`: 封面图URL
      - `duration`: 时长（秒）
      - `if_cml`: 是否商业音乐
      - `is_search`: 是否搜索结果
      - `link`: 音乐链接
      - `longevity`: 持久度信息
        - `popular_days`: 流行天数
        - `current_popularity`: 当前流行度
      - `music_url`: 音乐播放URL（可能为null）
      - `on_list_times`: 上榜次数（可能为null）
      - `promoted`: 是否推广
      - `rank`: 排名（可能为null）
      - `rank_diff`: 排名变化（可能为null）
      - `related_items`: 相关视频列表
        - `item_id`: 视频ID
        - `cover_uri`: 封面URI
      - `song_id`: 歌曲ID
      - `title`: 音乐标题
      - `trend`: 趋势数据
        - `time`: 时间戳
        - `value`: 数值
      - `url_title`: URL标题

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_detail\",
      \"params\": {
        \"clip_id\": \"7251810329461147649\",
        \"period\": 120,
        \"country_code\": \"US\"
      },
      \"data\": {
        \"sound\": {
          \"title\": \"Upbeat Summer Vibes\",
          \"author\": \"Music Producer\",
          \"duration\": 30,
          \"music_url\": \"https://music.tiktok.com/xxx\",
          \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/xxx\",
          \"audience_ages\": [
            {\"age_level\": \"18-24\", \"percentage\": 45.2},
            {\"age_level\": \"25-34\", \"percentage\": 32.8}
          ],
          \"audience_countries\": [
            {\"country\": \"US\", \"percentage\": 35.6},
            {\"country\": \"UK\", \"percentage\": 18.4}
          ],
          \"related_items\": [\"7213258221116751874\", \"7213258221116751875\"],
          \"usage_trend\": [
            {\"date\": \"2025-01-01\", \"count\": 1234},
            {\"date\": \"2025-01-02\", \"count\": 1456}
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get detailed information and usage data for specific music
    - Analyze multi-dimensional data like audience distribution and usage trends
    - Help select appropriate background music to enhance ad effectiveness

    ### Parameters:
    - clip_id: Sound clip ID, required parameter
    - period: Time period in days, e.g., 7, 30, 120 days
    - country_code: Country code, e.g., US, UK, JP

    ### Return Description:
    - `sound`: Sound detailed information
      - `title`: Music title
      - `author`: Music author/artist
      - `duration`: Duration in seconds
      - `music_url`: Music playback URL
      - `cover_url`: Cover image URL
      - `audience_ages`: Audience age distribution
        - `age_level`: Age range
        - `percentage`: Share percentage
      - `audience_countries`: Audience country distribution
        - `country`: Country code
        - `percentage`: Share percentage
      - `related_items`: List of popular video IDs using this music
      - `usage_trend`: Usage trend data

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_detail\",
      \"params\": {
        \"clip_id\": \"7251810329461147649\",
        \"period\": 120,
        \"country_code\": \"US\"
      },
      \"data\": {
        \"sound\": {
          \"title\": \"Upbeat Summer Vibes\",
          \"author\": \"Music Producer\",
          \"duration\": 30,
          \"music_url\": \"https://music.tiktok.com/xxx\",
          \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/xxx\",
          \"audience_ages\": [
            {\"age_level\": \"18-24\", \"percentage\": 45.2},
            {\"age_level\": \"25-34\", \"percentage\": 32.8}
          ],
          \"audience_countries\": [
            {\"country\": \"US\", \"percentage\": 35.6},
            {\"country\": \"UK\", \"percentage\": 18.4}
          ],
          \"related_items\": [\"7213258221116751874\", \"7213258221116751875\"],
          \"usage_trend\": [
            {\"date\": \"2025-01-01\", \"count\": 1234},
            {\"date\": \"2025-01-02\", \"count\": 1456}
          ]
        }
      }
    }
    ```

    Args:
        clip_id (str): 音乐ID/Sound clip ID
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 120.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        clip_id=clip_id,
        period=period,
        country_code=country_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    clip_id: str,
    period: Union[Unset, int] = 120,
    country_code: Union[Unset, str] = "US",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取音乐详情/Get sound detail

     # [中文]
    ### 用途:
    - 获取特定音乐的详细信息和使用数据
    - 分析音乐的受众分布、使用趋势等多维度数据
    - 帮助选择合适的背景音乐提升广告效果

    ### 参数:
    - clip_id: 音乐ID，必填参数
    - period: 时间范围（天），如7、30、120天
    - country_code: 国家代码，如US、UK、JP等

    ### 返回内容说明:
    - `disliked`: 是否不喜欢（可能为null）
    - `like_count`: 点赞数（可能为null）
    - `liked`: 是否点赞（可能为null）
    - `sound`: 音乐详细信息
      - `audience_ages`: 受众年龄分布
        - `age_level`: 年龄级别
        - `score`: 分数
      - `audience_countries`: 受众国家分布
        - `country_info`: 国家信息
          - `id`: 国家ID
          - `label`: 国家标签
          - `value`: 国家名称
        - `score`: 分数
      - `audience_interests`: 受众兴趣分布
        - `interest_info`: 兴趣信息
        - `score`: 分数
      - `author`: 音乐作者
      - `clip_id`: 片段ID
      - `country_code`: 国家代码
      - `cover`: 封面图URL
      - `duration`: 时长（秒）
      - `if_cml`: 是否商业音乐
      - `is_search`: 是否搜索结果
      - `link`: 音乐链接
      - `longevity`: 持久度信息
        - `popular_days`: 流行天数
        - `current_popularity`: 当前流行度
      - `music_url`: 音乐播放URL（可能为null）
      - `on_list_times`: 上榜次数（可能为null）
      - `promoted`: 是否推广
      - `rank`: 排名（可能为null）
      - `rank_diff`: 排名变化（可能为null）
      - `related_items`: 相关视频列表
        - `item_id`: 视频ID
        - `cover_uri`: 封面URI
      - `song_id`: 歌曲ID
      - `title`: 音乐标题
      - `trend`: 趋势数据
        - `time`: 时间戳
        - `value`: 数值
      - `url_title`: URL标题

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_detail\",
      \"params\": {
        \"clip_id\": \"7251810329461147649\",
        \"period\": 120,
        \"country_code\": \"US\"
      },
      \"data\": {
        \"sound\": {
          \"title\": \"Upbeat Summer Vibes\",
          \"author\": \"Music Producer\",
          \"duration\": 30,
          \"music_url\": \"https://music.tiktok.com/xxx\",
          \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/xxx\",
          \"audience_ages\": [
            {\"age_level\": \"18-24\", \"percentage\": 45.2},
            {\"age_level\": \"25-34\", \"percentage\": 32.8}
          ],
          \"audience_countries\": [
            {\"country\": \"US\", \"percentage\": 35.6},
            {\"country\": \"UK\", \"percentage\": 18.4}
          ],
          \"related_items\": [\"7213258221116751874\", \"7213258221116751875\"],
          \"usage_trend\": [
            {\"date\": \"2025-01-01\", \"count\": 1234},
            {\"date\": \"2025-01-02\", \"count\": 1456}
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get detailed information and usage data for specific music
    - Analyze multi-dimensional data like audience distribution and usage trends
    - Help select appropriate background music to enhance ad effectiveness

    ### Parameters:
    - clip_id: Sound clip ID, required parameter
    - period: Time period in days, e.g., 7, 30, 120 days
    - country_code: Country code, e.g., US, UK, JP

    ### Return Description:
    - `sound`: Sound detailed information
      - `title`: Music title
      - `author`: Music author/artist
      - `duration`: Duration in seconds
      - `music_url`: Music playback URL
      - `cover_url`: Cover image URL
      - `audience_ages`: Audience age distribution
        - `age_level`: Age range
        - `percentage`: Share percentage
      - `audience_countries`: Audience country distribution
        - `country`: Country code
        - `percentage`: Share percentage
      - `related_items`: List of popular video IDs using this music
      - `usage_trend`: Usage trend data

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_detail\",
      \"params\": {
        \"clip_id\": \"7251810329461147649\",
        \"period\": 120,
        \"country_code\": \"US\"
      },
      \"data\": {
        \"sound\": {
          \"title\": \"Upbeat Summer Vibes\",
          \"author\": \"Music Producer\",
          \"duration\": 30,
          \"music_url\": \"https://music.tiktok.com/xxx\",
          \"cover_url\": \"https://p16-sign-sg.tiktokcdn.com/xxx\",
          \"audience_ages\": [
            {\"age_level\": \"18-24\", \"percentage\": 45.2},
            {\"age_level\": \"25-34\", \"percentage\": 32.8}
          ],
          \"audience_countries\": [
            {\"country\": \"US\", \"percentage\": 35.6},
            {\"country\": \"UK\", \"percentage\": 18.4}
          ],
          \"related_items\": [\"7213258221116751874\", \"7213258221116751875\"],
          \"usage_trend\": [
            {\"date\": \"2025-01-01\", \"count\": 1234},
            {\"date\": \"2025-01-02\", \"count\": 1456}
          ]
        }
      }
    }
    ```

    Args:
        clip_id (str): 音乐ID/Sound clip ID
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 120.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            clip_id=clip_id,
            period=period,
            country_code=country_code,
        )
    ).parsed
