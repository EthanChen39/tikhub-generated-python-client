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
    period: Union[Unset, int] = 30,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    rank_type: Union[Unset, str] = "popular",
    new_on_board: Union[Unset, bool] = False,
    commercial_music: Union[Unset, bool] = False,
    country_code: Union[Unset, str] = "US",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["period"] = period

    params["page"] = page

    params["limit"] = limit

    params["rank_type"] = rank_type

    params["new_on_board"] = new_on_board

    params["commercial_music"] = commercial_music

    params["country_code"] = country_code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/get_sound_rank_list",
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
    period: Union[Unset, int] = 30,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    rank_type: Union[Unset, str] = "popular",
    new_on_board: Union[Unset, bool] = False,
    commercial_music: Union[Unset, bool] = False,
    country_code: Union[Unset, str] = "US",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取热门音乐排行榜/Get popular sound rankings

     # [中文]
    ### 用途:
    - 获取TikTok广告中的热门音乐排行榜，了解当前流行的音乐素材
    - 分析音乐的使用量、增长趋势等数据，发现潜力音乐
    - 帮助广告主选择合适的背景音乐，提升广告吸引力和传播效果

    ### 参数:
    - period: 时间范围（天），如7、30、120天
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - rank_type: 排行类型，\"popular\"=热门，\"surging\"=上升最快
    - new_on_board: 是否只看新上榜音乐，默认False
    - commercial_music: 是否只看商业音乐，默认False
    - country_code: 国家代码，如US、UK、JP等

    ### 返回内容说明:
    - `pagination`: 分页信息
      - `page`: 当前页
      - `size`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多
    - `sound_list`: 音乐列表
      - `author`: 音乐作者
      - `clip_id`: 片段ID
      - `cml_mid`: 商业音乐ID
      - `country_code`: 国家代码
      - `cover`: 封面图URL
      - `duration`: 时长（秒）
      - `if_cml`: 是否商业音乐
      - `is_search`: 是否搜索结果
      - `link`: 音乐链接
      - `music_url`: 音乐播放URL
      - `on_list_times`: 上榜次数（可能为null）
      - `promoted`: 是否推广
      - `rank`: 排名
      - `rank_diff`: 排名变化
      - `rank_diff_type`: 排名变化类型
      - `related_items`: 相关视频列表
        - `item_id`: 视频ID
        - `cover_uri`: 封面URI
      - `song_id`: 歌曲ID
      - `title`: 音乐标题
      - `trend`: 趋势数据
        - `time`: 时间戳
        - `value`: 该时间点的值
      - `url_title`: URL标题

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_rank_list\",
      \"params\": {
        \"period\": \"30\",
        \"page\": \"1\",
        \"limit\": \"20\",
        \"rank_type\": \"popular\",
        \"new_on_board\": \"false\",
        \"commercial_music\": \"false\",
        \"country_code\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 99,
            \"has_more\": true
          },
          \"sound_list\": [
            {
              \"author\": \"CYRIL & MOONLGHT & The La's\",
              \"clip_id\": \"7424014547218565904\",
              \"cml_mid\": \"7512350022513852432\",
              \"country_code\": \"US\",
              \"cover\": \"https://p16-sg.tiktokcdn.com/aweme/720x720/tos-
    alisg-v-2774/osxQt9H6AFAPAzveAQL4SQgGreoyVe6IDaCCXQ.jpeg\",
              \"duration\": 22,
              \"if_cml\": true,
              \"is_search\": false,
              \"link\": \"https://www.tiktok.com/music/x-7424014547218565904\",
              \"music_url\": \"https://sf16-ies-music-sg.tiktokcdn.com/obj/tos-alisg-
    ve-2774/o0W7XTIwoABiiicgwksz8EfQKFBPAA1M4Oq0kj\",
              \"on_list_times\": null,
              \"promoted\": false,
              \"rank\": 1,
              \"rank_diff\": 0,
              \"rank_diff_type\": 2,
              \"related_items\": [
                {
                  \"item_id\": 7512619474084711723,
                  \"cover_uri\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068c799-us/osLDIJAZvBbnB4E0gCiaBbHnigExB8CUIGvI4~tplv-noop.image\"
                }
              ],
              \"song_id\": \"7503950818010335233\",
              \"title\": \"There She Goes\",
              \"trend\": [
                {
                  \"time\": 1740787200,
                  \"value\": 0.15
                }
              ],
              \"url_title\": \"There She Goes (CYRIL Remix)\"
            }
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get popular music rankings in TikTok ads to understand current trending audio materials
    - Analyze usage and growth trend data for music to discover potential sounds
    - Help advertisers choose appropriate background music to enhance ad appeal and virality

    ### Parameters:
    - period: Time period in days, e.g., 7, 30, 120 days
    - page: Page number, default 1
    - limit: Items per page, default 20
    - rank_type: Ranking type, \"popular\"=Popular, \"surging\"=Fastest rising
    - new_on_board: Only show newly trending music, default False
    - commercial_music: Only show commercial music, default False
    - country_code: Country code, e.g., US, UK, JP

    ### Return Description:
    - `pagination`: Pagination info
      - `page`: Current page
      - `size`: Items per page
      - `total`: Total count
      - `has_more`: Whether there are more items
    - `sound_list`: Music list
      - `author`: Music author
      - `clip_id`: Clip ID
      - `cml_mid`: Commercial music ID
      - `country_code`: Country code
      - `cover`: Cover image URL
      - `duration`: Duration in seconds
      - `if_cml`: Whether commercial music
      - `is_search`: Whether search result
      - `link`: Music link
      - `music_url`: Music playback URL
      - `on_list_times`: Times on list (may be null)
      - `promoted`: Whether promoted
      - `rank`: Ranking
      - `rank_diff`: Rank difference
      - `rank_diff_type`: Rank difference type
      - `related_items`: Related video list
        - `item_id`: Video ID
        - `cover_uri`: Cover URI
      - `song_id`: Song ID
      - `title`: Music title
      - `trend`: Trend data
        - `time`: Timestamp
        - `value`: Value at that time point
      - `url_title`: URL title

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_rank_list\",
      \"params\": {
        \"period\": \"30\",
        \"page\": \"1\",
        \"limit\": \"20\",
        \"rank_type\": \"popular\",
        \"new_on_board\": \"false\",
        \"commercial_music\": \"false\",
        \"country_code\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 99,
            \"has_more\": true
          },
          \"sound_list\": [
            {
              \"author\": \"CYRIL & MOONLGHT & The La's\",
              \"clip_id\": \"7424014547218565904\",
              \"cml_mid\": \"7512350022513852432\",
              \"country_code\": \"US\",
              \"cover\": \"https://p16-sg.tiktokcdn.com/aweme/720x720/tos-
    alisg-v-2774/osxQt9H6AFAPAzveAQL4SQgGreoyVe6IDaCCXQ.jpeg\",
              \"duration\": 22,
              \"if_cml\": true,
              \"is_search\": false,
              \"link\": \"https://www.tiktok.com/music/x-7424014547218565904\",
              \"music_url\": \"https://sf16-ies-music-sg.tiktokcdn.com/obj/tos-alisg-
    ve-2774/o0W7XTIwoABiiicgwksz8EfQKFBPAA1M4Oq0kj\",
              \"on_list_times\": null,
              \"promoted\": false,
              \"rank\": 1,
              \"rank_diff\": 0,
              \"rank_diff_type\": 2,
              \"related_items\": [
                {
                  \"item_id\": 7512619474084711723,
                  \"cover_uri\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068c799-us/osLDIJAZvBbnB4E0gCiaBbHnigExB8CUIGvI4~tplv-noop.image\"
                }
              ],
              \"song_id\": \"7503950818010335233\",
              \"title\": \"There She Goes\",
              \"trend\": [
                {
                  \"time\": 1740787200,
                  \"value\": 0.15
                }
              ],
              \"url_title\": \"There She Goes (CYRIL Remix)\"
            }
          ]
        }
      }
    }
    ```

    Args:
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 30.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        rank_type (Union[Unset, str]): 排行类型/Rank type (popular, surging) Default: 'popular'.
        new_on_board (Union[Unset, bool]): 是否只看新上榜/Only new on board Default: False.
        commercial_music (Union[Unset, bool]): 是否商业音乐/Commercial music only Default: False.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        period=period,
        page=page,
        limit=limit,
        rank_type=rank_type,
        new_on_board=new_on_board,
        commercial_music=commercial_music,
        country_code=country_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    period: Union[Unset, int] = 30,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    rank_type: Union[Unset, str] = "popular",
    new_on_board: Union[Unset, bool] = False,
    commercial_music: Union[Unset, bool] = False,
    country_code: Union[Unset, str] = "US",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取热门音乐排行榜/Get popular sound rankings

     # [中文]
    ### 用途:
    - 获取TikTok广告中的热门音乐排行榜，了解当前流行的音乐素材
    - 分析音乐的使用量、增长趋势等数据，发现潜力音乐
    - 帮助广告主选择合适的背景音乐，提升广告吸引力和传播效果

    ### 参数:
    - period: 时间范围（天），如7、30、120天
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - rank_type: 排行类型，\"popular\"=热门，\"surging\"=上升最快
    - new_on_board: 是否只看新上榜音乐，默认False
    - commercial_music: 是否只看商业音乐，默认False
    - country_code: 国家代码，如US、UK、JP等

    ### 返回内容说明:
    - `pagination`: 分页信息
      - `page`: 当前页
      - `size`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多
    - `sound_list`: 音乐列表
      - `author`: 音乐作者
      - `clip_id`: 片段ID
      - `cml_mid`: 商业音乐ID
      - `country_code`: 国家代码
      - `cover`: 封面图URL
      - `duration`: 时长（秒）
      - `if_cml`: 是否商业音乐
      - `is_search`: 是否搜索结果
      - `link`: 音乐链接
      - `music_url`: 音乐播放URL
      - `on_list_times`: 上榜次数（可能为null）
      - `promoted`: 是否推广
      - `rank`: 排名
      - `rank_diff`: 排名变化
      - `rank_diff_type`: 排名变化类型
      - `related_items`: 相关视频列表
        - `item_id`: 视频ID
        - `cover_uri`: 封面URI
      - `song_id`: 歌曲ID
      - `title`: 音乐标题
      - `trend`: 趋势数据
        - `time`: 时间戳
        - `value`: 该时间点的值
      - `url_title`: URL标题

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_rank_list\",
      \"params\": {
        \"period\": \"30\",
        \"page\": \"1\",
        \"limit\": \"20\",
        \"rank_type\": \"popular\",
        \"new_on_board\": \"false\",
        \"commercial_music\": \"false\",
        \"country_code\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 99,
            \"has_more\": true
          },
          \"sound_list\": [
            {
              \"author\": \"CYRIL & MOONLGHT & The La's\",
              \"clip_id\": \"7424014547218565904\",
              \"cml_mid\": \"7512350022513852432\",
              \"country_code\": \"US\",
              \"cover\": \"https://p16-sg.tiktokcdn.com/aweme/720x720/tos-
    alisg-v-2774/osxQt9H6AFAPAzveAQL4SQgGreoyVe6IDaCCXQ.jpeg\",
              \"duration\": 22,
              \"if_cml\": true,
              \"is_search\": false,
              \"link\": \"https://www.tiktok.com/music/x-7424014547218565904\",
              \"music_url\": \"https://sf16-ies-music-sg.tiktokcdn.com/obj/tos-alisg-
    ve-2774/o0W7XTIwoABiiicgwksz8EfQKFBPAA1M4Oq0kj\",
              \"on_list_times\": null,
              \"promoted\": false,
              \"rank\": 1,
              \"rank_diff\": 0,
              \"rank_diff_type\": 2,
              \"related_items\": [
                {
                  \"item_id\": 7512619474084711723,
                  \"cover_uri\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068c799-us/osLDIJAZvBbnB4E0gCiaBbHnigExB8CUIGvI4~tplv-noop.image\"
                }
              ],
              \"song_id\": \"7503950818010335233\",
              \"title\": \"There She Goes\",
              \"trend\": [
                {
                  \"time\": 1740787200,
                  \"value\": 0.15
                }
              ],
              \"url_title\": \"There She Goes (CYRIL Remix)\"
            }
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get popular music rankings in TikTok ads to understand current trending audio materials
    - Analyze usage and growth trend data for music to discover potential sounds
    - Help advertisers choose appropriate background music to enhance ad appeal and virality

    ### Parameters:
    - period: Time period in days, e.g., 7, 30, 120 days
    - page: Page number, default 1
    - limit: Items per page, default 20
    - rank_type: Ranking type, \"popular\"=Popular, \"surging\"=Fastest rising
    - new_on_board: Only show newly trending music, default False
    - commercial_music: Only show commercial music, default False
    - country_code: Country code, e.g., US, UK, JP

    ### Return Description:
    - `pagination`: Pagination info
      - `page`: Current page
      - `size`: Items per page
      - `total`: Total count
      - `has_more`: Whether there are more items
    - `sound_list`: Music list
      - `author`: Music author
      - `clip_id`: Clip ID
      - `cml_mid`: Commercial music ID
      - `country_code`: Country code
      - `cover`: Cover image URL
      - `duration`: Duration in seconds
      - `if_cml`: Whether commercial music
      - `is_search`: Whether search result
      - `link`: Music link
      - `music_url`: Music playback URL
      - `on_list_times`: Times on list (may be null)
      - `promoted`: Whether promoted
      - `rank`: Ranking
      - `rank_diff`: Rank difference
      - `rank_diff_type`: Rank difference type
      - `related_items`: Related video list
        - `item_id`: Video ID
        - `cover_uri`: Cover URI
      - `song_id`: Song ID
      - `title`: Music title
      - `trend`: Trend data
        - `time`: Timestamp
        - `value`: Value at that time point
      - `url_title`: URL title

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_rank_list\",
      \"params\": {
        \"period\": \"30\",
        \"page\": \"1\",
        \"limit\": \"20\",
        \"rank_type\": \"popular\",
        \"new_on_board\": \"false\",
        \"commercial_music\": \"false\",
        \"country_code\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 99,
            \"has_more\": true
          },
          \"sound_list\": [
            {
              \"author\": \"CYRIL & MOONLGHT & The La's\",
              \"clip_id\": \"7424014547218565904\",
              \"cml_mid\": \"7512350022513852432\",
              \"country_code\": \"US\",
              \"cover\": \"https://p16-sg.tiktokcdn.com/aweme/720x720/tos-
    alisg-v-2774/osxQt9H6AFAPAzveAQL4SQgGreoyVe6IDaCCXQ.jpeg\",
              \"duration\": 22,
              \"if_cml\": true,
              \"is_search\": false,
              \"link\": \"https://www.tiktok.com/music/x-7424014547218565904\",
              \"music_url\": \"https://sf16-ies-music-sg.tiktokcdn.com/obj/tos-alisg-
    ve-2774/o0W7XTIwoABiiicgwksz8EfQKFBPAA1M4Oq0kj\",
              \"on_list_times\": null,
              \"promoted\": false,
              \"rank\": 1,
              \"rank_diff\": 0,
              \"rank_diff_type\": 2,
              \"related_items\": [
                {
                  \"item_id\": 7512619474084711723,
                  \"cover_uri\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068c799-us/osLDIJAZvBbnB4E0gCiaBbHnigExB8CUIGvI4~tplv-noop.image\"
                }
              ],
              \"song_id\": \"7503950818010335233\",
              \"title\": \"There She Goes\",
              \"trend\": [
                {
                  \"time\": 1740787200,
                  \"value\": 0.15
                }
              ],
              \"url_title\": \"There She Goes (CYRIL Remix)\"
            }
          ]
        }
      }
    }
    ```

    Args:
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 30.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        rank_type (Union[Unset, str]): 排行类型/Rank type (popular, surging) Default: 'popular'.
        new_on_board (Union[Unset, bool]): 是否只看新上榜/Only new on board Default: False.
        commercial_music (Union[Unset, bool]): 是否商业音乐/Commercial music only Default: False.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        period=period,
        page=page,
        limit=limit,
        rank_type=rank_type,
        new_on_board=new_on_board,
        commercial_music=commercial_music,
        country_code=country_code,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    period: Union[Unset, int] = 30,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    rank_type: Union[Unset, str] = "popular",
    new_on_board: Union[Unset, bool] = False,
    commercial_music: Union[Unset, bool] = False,
    country_code: Union[Unset, str] = "US",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取热门音乐排行榜/Get popular sound rankings

     # [中文]
    ### 用途:
    - 获取TikTok广告中的热门音乐排行榜，了解当前流行的音乐素材
    - 分析音乐的使用量、增长趋势等数据，发现潜力音乐
    - 帮助广告主选择合适的背景音乐，提升广告吸引力和传播效果

    ### 参数:
    - period: 时间范围（天），如7、30、120天
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - rank_type: 排行类型，\"popular\"=热门，\"surging\"=上升最快
    - new_on_board: 是否只看新上榜音乐，默认False
    - commercial_music: 是否只看商业音乐，默认False
    - country_code: 国家代码，如US、UK、JP等

    ### 返回内容说明:
    - `pagination`: 分页信息
      - `page`: 当前页
      - `size`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多
    - `sound_list`: 音乐列表
      - `author`: 音乐作者
      - `clip_id`: 片段ID
      - `cml_mid`: 商业音乐ID
      - `country_code`: 国家代码
      - `cover`: 封面图URL
      - `duration`: 时长（秒）
      - `if_cml`: 是否商业音乐
      - `is_search`: 是否搜索结果
      - `link`: 音乐链接
      - `music_url`: 音乐播放URL
      - `on_list_times`: 上榜次数（可能为null）
      - `promoted`: 是否推广
      - `rank`: 排名
      - `rank_diff`: 排名变化
      - `rank_diff_type`: 排名变化类型
      - `related_items`: 相关视频列表
        - `item_id`: 视频ID
        - `cover_uri`: 封面URI
      - `song_id`: 歌曲ID
      - `title`: 音乐标题
      - `trend`: 趋势数据
        - `time`: 时间戳
        - `value`: 该时间点的值
      - `url_title`: URL标题

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_rank_list\",
      \"params\": {
        \"period\": \"30\",
        \"page\": \"1\",
        \"limit\": \"20\",
        \"rank_type\": \"popular\",
        \"new_on_board\": \"false\",
        \"commercial_music\": \"false\",
        \"country_code\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 99,
            \"has_more\": true
          },
          \"sound_list\": [
            {
              \"author\": \"CYRIL & MOONLGHT & The La's\",
              \"clip_id\": \"7424014547218565904\",
              \"cml_mid\": \"7512350022513852432\",
              \"country_code\": \"US\",
              \"cover\": \"https://p16-sg.tiktokcdn.com/aweme/720x720/tos-
    alisg-v-2774/osxQt9H6AFAPAzveAQL4SQgGreoyVe6IDaCCXQ.jpeg\",
              \"duration\": 22,
              \"if_cml\": true,
              \"is_search\": false,
              \"link\": \"https://www.tiktok.com/music/x-7424014547218565904\",
              \"music_url\": \"https://sf16-ies-music-sg.tiktokcdn.com/obj/tos-alisg-
    ve-2774/o0W7XTIwoABiiicgwksz8EfQKFBPAA1M4Oq0kj\",
              \"on_list_times\": null,
              \"promoted\": false,
              \"rank\": 1,
              \"rank_diff\": 0,
              \"rank_diff_type\": 2,
              \"related_items\": [
                {
                  \"item_id\": 7512619474084711723,
                  \"cover_uri\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068c799-us/osLDIJAZvBbnB4E0gCiaBbHnigExB8CUIGvI4~tplv-noop.image\"
                }
              ],
              \"song_id\": \"7503950818010335233\",
              \"title\": \"There She Goes\",
              \"trend\": [
                {
                  \"time\": 1740787200,
                  \"value\": 0.15
                }
              ],
              \"url_title\": \"There She Goes (CYRIL Remix)\"
            }
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get popular music rankings in TikTok ads to understand current trending audio materials
    - Analyze usage and growth trend data for music to discover potential sounds
    - Help advertisers choose appropriate background music to enhance ad appeal and virality

    ### Parameters:
    - period: Time period in days, e.g., 7, 30, 120 days
    - page: Page number, default 1
    - limit: Items per page, default 20
    - rank_type: Ranking type, \"popular\"=Popular, \"surging\"=Fastest rising
    - new_on_board: Only show newly trending music, default False
    - commercial_music: Only show commercial music, default False
    - country_code: Country code, e.g., US, UK, JP

    ### Return Description:
    - `pagination`: Pagination info
      - `page`: Current page
      - `size`: Items per page
      - `total`: Total count
      - `has_more`: Whether there are more items
    - `sound_list`: Music list
      - `author`: Music author
      - `clip_id`: Clip ID
      - `cml_mid`: Commercial music ID
      - `country_code`: Country code
      - `cover`: Cover image URL
      - `duration`: Duration in seconds
      - `if_cml`: Whether commercial music
      - `is_search`: Whether search result
      - `link`: Music link
      - `music_url`: Music playback URL
      - `on_list_times`: Times on list (may be null)
      - `promoted`: Whether promoted
      - `rank`: Ranking
      - `rank_diff`: Rank difference
      - `rank_diff_type`: Rank difference type
      - `related_items`: Related video list
        - `item_id`: Video ID
        - `cover_uri`: Cover URI
      - `song_id`: Song ID
      - `title`: Music title
      - `trend`: Trend data
        - `time`: Timestamp
        - `value`: Value at that time point
      - `url_title`: URL title

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_rank_list\",
      \"params\": {
        \"period\": \"30\",
        \"page\": \"1\",
        \"limit\": \"20\",
        \"rank_type\": \"popular\",
        \"new_on_board\": \"false\",
        \"commercial_music\": \"false\",
        \"country_code\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 99,
            \"has_more\": true
          },
          \"sound_list\": [
            {
              \"author\": \"CYRIL & MOONLGHT & The La's\",
              \"clip_id\": \"7424014547218565904\",
              \"cml_mid\": \"7512350022513852432\",
              \"country_code\": \"US\",
              \"cover\": \"https://p16-sg.tiktokcdn.com/aweme/720x720/tos-
    alisg-v-2774/osxQt9H6AFAPAzveAQL4SQgGreoyVe6IDaCCXQ.jpeg\",
              \"duration\": 22,
              \"if_cml\": true,
              \"is_search\": false,
              \"link\": \"https://www.tiktok.com/music/x-7424014547218565904\",
              \"music_url\": \"https://sf16-ies-music-sg.tiktokcdn.com/obj/tos-alisg-
    ve-2774/o0W7XTIwoABiiicgwksz8EfQKFBPAA1M4Oq0kj\",
              \"on_list_times\": null,
              \"promoted\": false,
              \"rank\": 1,
              \"rank_diff\": 0,
              \"rank_diff_type\": 2,
              \"related_items\": [
                {
                  \"item_id\": 7512619474084711723,
                  \"cover_uri\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068c799-us/osLDIJAZvBbnB4E0gCiaBbHnigExB8CUIGvI4~tplv-noop.image\"
                }
              ],
              \"song_id\": \"7503950818010335233\",
              \"title\": \"There She Goes\",
              \"trend\": [
                {
                  \"time\": 1740787200,
                  \"value\": 0.15
                }
              ],
              \"url_title\": \"There She Goes (CYRIL Remix)\"
            }
          ]
        }
      }
    }
    ```

    Args:
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 30.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        rank_type (Union[Unset, str]): 排行类型/Rank type (popular, surging) Default: 'popular'.
        new_on_board (Union[Unset, bool]): 是否只看新上榜/Only new on board Default: False.
        commercial_music (Union[Unset, bool]): 是否商业音乐/Commercial music only Default: False.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        period=period,
        page=page,
        limit=limit,
        rank_type=rank_type,
        new_on_board=new_on_board,
        commercial_music=commercial_music,
        country_code=country_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    period: Union[Unset, int] = 30,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    rank_type: Union[Unset, str] = "popular",
    new_on_board: Union[Unset, bool] = False,
    commercial_music: Union[Unset, bool] = False,
    country_code: Union[Unset, str] = "US",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取热门音乐排行榜/Get popular sound rankings

     # [中文]
    ### 用途:
    - 获取TikTok广告中的热门音乐排行榜，了解当前流行的音乐素材
    - 分析音乐的使用量、增长趋势等数据，发现潜力音乐
    - 帮助广告主选择合适的背景音乐，提升广告吸引力和传播效果

    ### 参数:
    - period: 时间范围（天），如7、30、120天
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - rank_type: 排行类型，\"popular\"=热门，\"surging\"=上升最快
    - new_on_board: 是否只看新上榜音乐，默认False
    - commercial_music: 是否只看商业音乐，默认False
    - country_code: 国家代码，如US、UK、JP等

    ### 返回内容说明:
    - `pagination`: 分页信息
      - `page`: 当前页
      - `size`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多
    - `sound_list`: 音乐列表
      - `author`: 音乐作者
      - `clip_id`: 片段ID
      - `cml_mid`: 商业音乐ID
      - `country_code`: 国家代码
      - `cover`: 封面图URL
      - `duration`: 时长（秒）
      - `if_cml`: 是否商业音乐
      - `is_search`: 是否搜索结果
      - `link`: 音乐链接
      - `music_url`: 音乐播放URL
      - `on_list_times`: 上榜次数（可能为null）
      - `promoted`: 是否推广
      - `rank`: 排名
      - `rank_diff`: 排名变化
      - `rank_diff_type`: 排名变化类型
      - `related_items`: 相关视频列表
        - `item_id`: 视频ID
        - `cover_uri`: 封面URI
      - `song_id`: 歌曲ID
      - `title`: 音乐标题
      - `trend`: 趋势数据
        - `time`: 时间戳
        - `value`: 该时间点的值
      - `url_title`: URL标题

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_rank_list\",
      \"params\": {
        \"period\": \"30\",
        \"page\": \"1\",
        \"limit\": \"20\",
        \"rank_type\": \"popular\",
        \"new_on_board\": \"false\",
        \"commercial_music\": \"false\",
        \"country_code\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 99,
            \"has_more\": true
          },
          \"sound_list\": [
            {
              \"author\": \"CYRIL & MOONLGHT & The La's\",
              \"clip_id\": \"7424014547218565904\",
              \"cml_mid\": \"7512350022513852432\",
              \"country_code\": \"US\",
              \"cover\": \"https://p16-sg.tiktokcdn.com/aweme/720x720/tos-
    alisg-v-2774/osxQt9H6AFAPAzveAQL4SQgGreoyVe6IDaCCXQ.jpeg\",
              \"duration\": 22,
              \"if_cml\": true,
              \"is_search\": false,
              \"link\": \"https://www.tiktok.com/music/x-7424014547218565904\",
              \"music_url\": \"https://sf16-ies-music-sg.tiktokcdn.com/obj/tos-alisg-
    ve-2774/o0W7XTIwoABiiicgwksz8EfQKFBPAA1M4Oq0kj\",
              \"on_list_times\": null,
              \"promoted\": false,
              \"rank\": 1,
              \"rank_diff\": 0,
              \"rank_diff_type\": 2,
              \"related_items\": [
                {
                  \"item_id\": 7512619474084711723,
                  \"cover_uri\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068c799-us/osLDIJAZvBbnB4E0gCiaBbHnigExB8CUIGvI4~tplv-noop.image\"
                }
              ],
              \"song_id\": \"7503950818010335233\",
              \"title\": \"There She Goes\",
              \"trend\": [
                {
                  \"time\": 1740787200,
                  \"value\": 0.15
                }
              ],
              \"url_title\": \"There She Goes (CYRIL Remix)\"
            }
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get popular music rankings in TikTok ads to understand current trending audio materials
    - Analyze usage and growth trend data for music to discover potential sounds
    - Help advertisers choose appropriate background music to enhance ad appeal and virality

    ### Parameters:
    - period: Time period in days, e.g., 7, 30, 120 days
    - page: Page number, default 1
    - limit: Items per page, default 20
    - rank_type: Ranking type, \"popular\"=Popular, \"surging\"=Fastest rising
    - new_on_board: Only show newly trending music, default False
    - commercial_music: Only show commercial music, default False
    - country_code: Country code, e.g., US, UK, JP

    ### Return Description:
    - `pagination`: Pagination info
      - `page`: Current page
      - `size`: Items per page
      - `total`: Total count
      - `has_more`: Whether there are more items
    - `sound_list`: Music list
      - `author`: Music author
      - `clip_id`: Clip ID
      - `cml_mid`: Commercial music ID
      - `country_code`: Country code
      - `cover`: Cover image URL
      - `duration`: Duration in seconds
      - `if_cml`: Whether commercial music
      - `is_search`: Whether search result
      - `link`: Music link
      - `music_url`: Music playback URL
      - `on_list_times`: Times on list (may be null)
      - `promoted`: Whether promoted
      - `rank`: Ranking
      - `rank_diff`: Rank difference
      - `rank_diff_type`: Rank difference type
      - `related_items`: Related video list
        - `item_id`: Video ID
        - `cover_uri`: Cover URI
      - `song_id`: Song ID
      - `title`: Music title
      - `trend`: Trend data
        - `time`: Timestamp
        - `value`: Value at that time point
      - `url_title`: URL title

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_rank_list\",
      \"params\": {
        \"period\": \"30\",
        \"page\": \"1\",
        \"limit\": \"20\",
        \"rank_type\": \"popular\",
        \"new_on_board\": \"false\",
        \"commercial_music\": \"false\",
        \"country_code\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 99,
            \"has_more\": true
          },
          \"sound_list\": [
            {
              \"author\": \"CYRIL & MOONLGHT & The La's\",
              \"clip_id\": \"7424014547218565904\",
              \"cml_mid\": \"7512350022513852432\",
              \"country_code\": \"US\",
              \"cover\": \"https://p16-sg.tiktokcdn.com/aweme/720x720/tos-
    alisg-v-2774/osxQt9H6AFAPAzveAQL4SQgGreoyVe6IDaCCXQ.jpeg\",
              \"duration\": 22,
              \"if_cml\": true,
              \"is_search\": false,
              \"link\": \"https://www.tiktok.com/music/x-7424014547218565904\",
              \"music_url\": \"https://sf16-ies-music-sg.tiktokcdn.com/obj/tos-alisg-
    ve-2774/o0W7XTIwoABiiicgwksz8EfQKFBPAA1M4Oq0kj\",
              \"on_list_times\": null,
              \"promoted\": false,
              \"rank\": 1,
              \"rank_diff\": 0,
              \"rank_diff_type\": 2,
              \"related_items\": [
                {
                  \"item_id\": 7512619474084711723,
                  \"cover_uri\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068c799-us/osLDIJAZvBbnB4E0gCiaBbHnigExB8CUIGvI4~tplv-noop.image\"
                }
              ],
              \"song_id\": \"7503950818010335233\",
              \"title\": \"There She Goes\",
              \"trend\": [
                {
                  \"time\": 1740787200,
                  \"value\": 0.15
                }
              ],
              \"url_title\": \"There She Goes (CYRIL Remix)\"
            }
          ]
        }
      }
    }
    ```

    Args:
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 30.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        rank_type (Union[Unset, str]): 排行类型/Rank type (popular, surging) Default: 'popular'.
        new_on_board (Union[Unset, bool]): 是否只看新上榜/Only new on board Default: False.
        commercial_music (Union[Unset, bool]): 是否商业音乐/Commercial music only Default: False.
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
            period=period,
            page=page,
            limit=limit,
            rank_type=rank_type,
            new_on_board=new_on_board,
            commercial_music=commercial_music,
            country_code=country_code,
        )
    ).parsed
