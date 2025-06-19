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
    keyword: str,
    period: Union[Unset, int] = 7,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    rank_type: Union[Unset, str] = "popular",
    new_on_board: Union[Unset, bool] = False,
    commercial_music: Union[Unset, bool] = False,
    country_code: Union[Unset, str] = "US",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

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
        "url": "/api/v1/tiktok/ads/search_sound",
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
    keyword: str,
    period: Union[Unset, int] = 7,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    rank_type: Union[Unset, str] = "popular",
    new_on_board: Union[Unset, bool] = False,
    commercial_music: Union[Unset, bool] = False,
    country_code: Union[Unset, str] = "US",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索音乐/Search sounds

     # [中文]
    ### 用途:
    - 搜索符合条件的音乐列表
    - 支持按关键词、热度、商业类型等多维度筛选
    - 为广告配乐选择提供全面的搜索功能

    ### 参数:
    - keyword: 搜索关键词
    - period: 时间范围（天），如7、30、120天
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - rank_type: 排行类型，\"popular\"=热门，\"surging\"=上升最快
    - new_on_board: 是否只看新上榜音乐
    - commercial_music: 是否只看商业音乐
    - country_code: 国家代码

    ### 返回内容说明:
    - `sound_list`: 音乐列表
      - `id`: 音乐ID
      - `title`: 音乐标题
      - `author`: 音乐作者
      - `duration`: 时长（秒）
      - `trend`: 趋势数据
      - `related_items`: 使用该音乐的视频数量
      - `is_commercial`: 是否商业音乐
    - `pagination`: 分页信息

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_sound\",
      \"params\": {
        \"keyword\": \"taylor swift\",
        \"period\": 7,
        \"page\": 1
      },
      \"data\": {
        \"sound_list\": [
          {
            \"id\": \"7156826385225353217\",
            \"title\": \"Karma\",
            \"author\": \"Taylor Swift\",
            \"duration\": 30,
            \"trend\": [
              {\"time\": 1746000000, \"value\": 15000}
            ],
            \"related_items\": 5678,
            \"is_commercial\": true
          }
        ],
        \"pagination\": {
          \"page\": 1,
          \"size\": 20,
          \"total\": 156,
          \"has_more\": true
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Search for music lists matching criteria
    - Support multi-dimensional filtering by keyword, popularity, commercial type, etc.
    - Provide comprehensive search functionality for ad soundtrack selection

    ### Parameters:
    - keyword: Search keyword
    - period: Time period in days, e.g., 7, 30, 120 days
    - page: Page number, default 1
    - limit: Items per page, default 20
    - rank_type: Ranking type, \"popular\"=Popular, \"surging\"=Fastest rising
    - new_on_board: Only show newly trending music
    - commercial_music: Only show commercial music
    - country_code: Country code

    ### Return Description:
    - `sound_list`: Music list
      - `id`: Music ID
      - `title`: Music title
      - `author`: Music author
      - `duration`: Duration in seconds
      - `trend`: Trend data
      - `related_items`: Number of videos using this music
      - `is_commercial`: Whether commercial music
    - `pagination`: Pagination info

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_sound\",
      \"params\": {
        \"keyword\": \"taylor swift\",
        \"period\": 7,
        \"page\": 1
      },
      \"data\": {
        \"sound_list\": [
          {
            \"id\": \"7156826385225353217\",
            \"title\": \"Karma\",
            \"author\": \"Taylor Swift\",
            \"duration\": 30,
            \"trend\": [
              {\"time\": 1746000000, \"value\": 15000}
            ],
            \"related_items\": 5678,
            \"is_commercial\": true
          }
        ],
        \"pagination\": {
          \"page\": 1,
          \"size\": 20,
          \"total\": 156,
          \"has_more\": true
        }
      }
    }
    ```

    Args:
        keyword (str): 搜索关键词/Search keyword
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 7.
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
        keyword=keyword,
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
    keyword: str,
    period: Union[Unset, int] = 7,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    rank_type: Union[Unset, str] = "popular",
    new_on_board: Union[Unset, bool] = False,
    commercial_music: Union[Unset, bool] = False,
    country_code: Union[Unset, str] = "US",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索音乐/Search sounds

     # [中文]
    ### 用途:
    - 搜索符合条件的音乐列表
    - 支持按关键词、热度、商业类型等多维度筛选
    - 为广告配乐选择提供全面的搜索功能

    ### 参数:
    - keyword: 搜索关键词
    - period: 时间范围（天），如7、30、120天
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - rank_type: 排行类型，\"popular\"=热门，\"surging\"=上升最快
    - new_on_board: 是否只看新上榜音乐
    - commercial_music: 是否只看商业音乐
    - country_code: 国家代码

    ### 返回内容说明:
    - `sound_list`: 音乐列表
      - `id`: 音乐ID
      - `title`: 音乐标题
      - `author`: 音乐作者
      - `duration`: 时长（秒）
      - `trend`: 趋势数据
      - `related_items`: 使用该音乐的视频数量
      - `is_commercial`: 是否商业音乐
    - `pagination`: 分页信息

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_sound\",
      \"params\": {
        \"keyword\": \"taylor swift\",
        \"period\": 7,
        \"page\": 1
      },
      \"data\": {
        \"sound_list\": [
          {
            \"id\": \"7156826385225353217\",
            \"title\": \"Karma\",
            \"author\": \"Taylor Swift\",
            \"duration\": 30,
            \"trend\": [
              {\"time\": 1746000000, \"value\": 15000}
            ],
            \"related_items\": 5678,
            \"is_commercial\": true
          }
        ],
        \"pagination\": {
          \"page\": 1,
          \"size\": 20,
          \"total\": 156,
          \"has_more\": true
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Search for music lists matching criteria
    - Support multi-dimensional filtering by keyword, popularity, commercial type, etc.
    - Provide comprehensive search functionality for ad soundtrack selection

    ### Parameters:
    - keyword: Search keyword
    - period: Time period in days, e.g., 7, 30, 120 days
    - page: Page number, default 1
    - limit: Items per page, default 20
    - rank_type: Ranking type, \"popular\"=Popular, \"surging\"=Fastest rising
    - new_on_board: Only show newly trending music
    - commercial_music: Only show commercial music
    - country_code: Country code

    ### Return Description:
    - `sound_list`: Music list
      - `id`: Music ID
      - `title`: Music title
      - `author`: Music author
      - `duration`: Duration in seconds
      - `trend`: Trend data
      - `related_items`: Number of videos using this music
      - `is_commercial`: Whether commercial music
    - `pagination`: Pagination info

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_sound\",
      \"params\": {
        \"keyword\": \"taylor swift\",
        \"period\": 7,
        \"page\": 1
      },
      \"data\": {
        \"sound_list\": [
          {
            \"id\": \"7156826385225353217\",
            \"title\": \"Karma\",
            \"author\": \"Taylor Swift\",
            \"duration\": 30,
            \"trend\": [
              {\"time\": 1746000000, \"value\": 15000}
            ],
            \"related_items\": 5678,
            \"is_commercial\": true
          }
        ],
        \"pagination\": {
          \"page\": 1,
          \"size\": 20,
          \"total\": 156,
          \"has_more\": true
        }
      }
    }
    ```

    Args:
        keyword (str): 搜索关键词/Search keyword
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 7.
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
        keyword=keyword,
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
    keyword: str,
    period: Union[Unset, int] = 7,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    rank_type: Union[Unset, str] = "popular",
    new_on_board: Union[Unset, bool] = False,
    commercial_music: Union[Unset, bool] = False,
    country_code: Union[Unset, str] = "US",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索音乐/Search sounds

     # [中文]
    ### 用途:
    - 搜索符合条件的音乐列表
    - 支持按关键词、热度、商业类型等多维度筛选
    - 为广告配乐选择提供全面的搜索功能

    ### 参数:
    - keyword: 搜索关键词
    - period: 时间范围（天），如7、30、120天
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - rank_type: 排行类型，\"popular\"=热门，\"surging\"=上升最快
    - new_on_board: 是否只看新上榜音乐
    - commercial_music: 是否只看商业音乐
    - country_code: 国家代码

    ### 返回内容说明:
    - `sound_list`: 音乐列表
      - `id`: 音乐ID
      - `title`: 音乐标题
      - `author`: 音乐作者
      - `duration`: 时长（秒）
      - `trend`: 趋势数据
      - `related_items`: 使用该音乐的视频数量
      - `is_commercial`: 是否商业音乐
    - `pagination`: 分页信息

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_sound\",
      \"params\": {
        \"keyword\": \"taylor swift\",
        \"period\": 7,
        \"page\": 1
      },
      \"data\": {
        \"sound_list\": [
          {
            \"id\": \"7156826385225353217\",
            \"title\": \"Karma\",
            \"author\": \"Taylor Swift\",
            \"duration\": 30,
            \"trend\": [
              {\"time\": 1746000000, \"value\": 15000}
            ],
            \"related_items\": 5678,
            \"is_commercial\": true
          }
        ],
        \"pagination\": {
          \"page\": 1,
          \"size\": 20,
          \"total\": 156,
          \"has_more\": true
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Search for music lists matching criteria
    - Support multi-dimensional filtering by keyword, popularity, commercial type, etc.
    - Provide comprehensive search functionality for ad soundtrack selection

    ### Parameters:
    - keyword: Search keyword
    - period: Time period in days, e.g., 7, 30, 120 days
    - page: Page number, default 1
    - limit: Items per page, default 20
    - rank_type: Ranking type, \"popular\"=Popular, \"surging\"=Fastest rising
    - new_on_board: Only show newly trending music
    - commercial_music: Only show commercial music
    - country_code: Country code

    ### Return Description:
    - `sound_list`: Music list
      - `id`: Music ID
      - `title`: Music title
      - `author`: Music author
      - `duration`: Duration in seconds
      - `trend`: Trend data
      - `related_items`: Number of videos using this music
      - `is_commercial`: Whether commercial music
    - `pagination`: Pagination info

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_sound\",
      \"params\": {
        \"keyword\": \"taylor swift\",
        \"period\": 7,
        \"page\": 1
      },
      \"data\": {
        \"sound_list\": [
          {
            \"id\": \"7156826385225353217\",
            \"title\": \"Karma\",
            \"author\": \"Taylor Swift\",
            \"duration\": 30,
            \"trend\": [
              {\"time\": 1746000000, \"value\": 15000}
            ],
            \"related_items\": 5678,
            \"is_commercial\": true
          }
        ],
        \"pagination\": {
          \"page\": 1,
          \"size\": 20,
          \"total\": 156,
          \"has_more\": true
        }
      }
    }
    ```

    Args:
        keyword (str): 搜索关键词/Search keyword
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 7.
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
        keyword=keyword,
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
    keyword: str,
    period: Union[Unset, int] = 7,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    rank_type: Union[Unset, str] = "popular",
    new_on_board: Union[Unset, bool] = False,
    commercial_music: Union[Unset, bool] = False,
    country_code: Union[Unset, str] = "US",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索音乐/Search sounds

     # [中文]
    ### 用途:
    - 搜索符合条件的音乐列表
    - 支持按关键词、热度、商业类型等多维度筛选
    - 为广告配乐选择提供全面的搜索功能

    ### 参数:
    - keyword: 搜索关键词
    - period: 时间范围（天），如7、30、120天
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - rank_type: 排行类型，\"popular\"=热门，\"surging\"=上升最快
    - new_on_board: 是否只看新上榜音乐
    - commercial_music: 是否只看商业音乐
    - country_code: 国家代码

    ### 返回内容说明:
    - `sound_list`: 音乐列表
      - `id`: 音乐ID
      - `title`: 音乐标题
      - `author`: 音乐作者
      - `duration`: 时长（秒）
      - `trend`: 趋势数据
      - `related_items`: 使用该音乐的视频数量
      - `is_commercial`: 是否商业音乐
    - `pagination`: 分页信息

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_sound\",
      \"params\": {
        \"keyword\": \"taylor swift\",
        \"period\": 7,
        \"page\": 1
      },
      \"data\": {
        \"sound_list\": [
          {
            \"id\": \"7156826385225353217\",
            \"title\": \"Karma\",
            \"author\": \"Taylor Swift\",
            \"duration\": 30,
            \"trend\": [
              {\"time\": 1746000000, \"value\": 15000}
            ],
            \"related_items\": 5678,
            \"is_commercial\": true
          }
        ],
        \"pagination\": {
          \"page\": 1,
          \"size\": 20,
          \"total\": 156,
          \"has_more\": true
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Search for music lists matching criteria
    - Support multi-dimensional filtering by keyword, popularity, commercial type, etc.
    - Provide comprehensive search functionality for ad soundtrack selection

    ### Parameters:
    - keyword: Search keyword
    - period: Time period in days, e.g., 7, 30, 120 days
    - page: Page number, default 1
    - limit: Items per page, default 20
    - rank_type: Ranking type, \"popular\"=Popular, \"surging\"=Fastest rising
    - new_on_board: Only show newly trending music
    - commercial_music: Only show commercial music
    - country_code: Country code

    ### Return Description:
    - `sound_list`: Music list
      - `id`: Music ID
      - `title`: Music title
      - `author`: Music author
      - `duration`: Duration in seconds
      - `trend`: Trend data
      - `related_items`: Number of videos using this music
      - `is_commercial`: Whether commercial music
    - `pagination`: Pagination info

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_sound\",
      \"params\": {
        \"keyword\": \"taylor swift\",
        \"period\": 7,
        \"page\": 1
      },
      \"data\": {
        \"sound_list\": [
          {
            \"id\": \"7156826385225353217\",
            \"title\": \"Karma\",
            \"author\": \"Taylor Swift\",
            \"duration\": 30,
            \"trend\": [
              {\"time\": 1746000000, \"value\": 15000}
            ],
            \"related_items\": 5678,
            \"is_commercial\": true
          }
        ],
        \"pagination\": {
          \"page\": 1,
          \"size\": 20,
          \"total\": 156,
          \"has_more\": true
        }
      }
    }
    ```

    Args:
        keyword (str): 搜索关键词/Search keyword
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 7.
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
            keyword=keyword,
            period=period,
            page=page,
            limit=limit,
            rank_type=rank_type,
            new_on_board=new_on_board,
            commercial_music=commercial_music,
            country_code=country_code,
        )
    ).parsed
