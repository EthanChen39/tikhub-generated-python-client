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
    limit: Union[Unset, int] = 5,
    rank_type: Union[Unset, str] = "popular",
    country_code: Union[Unset, str] = "US",
    filter_by_checked: Union[Unset, bool] = False,
    commercial_music: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["period"] = period

    params["page"] = page

    params["limit"] = limit

    params["rank_type"] = rank_type

    params["country_code"] = country_code

    params["filter_by_checked"] = filter_by_checked

    params["commercial_music"] = commercial_music

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/search_sound_hint",
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
    limit: Union[Unset, int] = 5,
    rank_type: Union[Unset, str] = "popular",
    country_code: Union[Unset, str] = "US",
    filter_by_checked: Union[Unset, bool] = False,
    commercial_music: Union[Unset, bool] = False,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索音乐提示/Search sound hints

     # [中文]
    ### 用途:
    - 获取音乐搜索的自动完成提示和推荐
    - 帮助用户快速找到相关音乐
    - 提供搜索建议优化音乐选择

    ### 参数:
    - keyword: 搜索关键词
    - period: 时间范围（天）
    - page: 页码，默认1
    - limit: 每页数量，默认5
    - rank_type: 排行类型，\"popular\"=热门，\"surging\"=上升最快
    - country_code: 国家代码
    - filter_by_checked: 是否只看已验证音乐
    - commercial_music: 是否只看商业音乐

    ### 返回内容说明:
    - `sound_list`: 音乐提示列表
      - `title`: 音乐标题
      - `author`: 音乐作者
      - `match_type`: 匹配类型（标题/作者/标签）
      - `popularity`: 热度评分

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_sound_hint\",
      \"params\": {
        \"keyword\": \"taylor swift\",
        \"limit\": 5
      },
      \"data\": {
        \"sound_list\": [
          {
            \"title\": \"Anti-Hero\",
            \"author\": \"Taylor Swift\",
            \"match_type\": \"artist\",
            \"popularity\": 98
          },
          {
            \"title\": \"Blank Space\",
            \"author\": \"Taylor Swift\",
            \"match_type\": \"artist\",
            \"popularity\": 95
          }
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get auto-complete hints and recommendations for music search
    - Help users quickly find relevant music
    - Provide search suggestions to optimize music selection

    ### Parameters:
    - keyword: Search keyword
    - period: Time period in days
    - page: Page number, default 1
    - limit: Items per page, default 5
    - rank_type: Ranking type, \"popular\"=Popular, \"surging\"=Fastest rising
    - country_code: Country code
    - filter_by_checked: Only show verified music
    - commercial_music: Only show commercial music

    ### Return Description:
    - `sound_list`: Music hint list
      - `title`: Music title
      - `author`: Music author
      - `match_type`: Match type (title/artist/tag)
      - `popularity`: Popularity score

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_sound_hint\",
      \"params\": {
        \"keyword\": \"taylor swift\",
        \"limit\": 5
      },
      \"data\": {
        \"sound_list\": [
          {
            \"title\": \"Anti-Hero\",
            \"author\": \"Taylor Swift\",
            \"match_type\": \"artist\",
            \"popularity\": 98
          },
          {
            \"title\": \"Blank Space\",
            \"author\": \"Taylor Swift\",
            \"match_type\": \"artist\",
            \"popularity\": 95
          }
        ]
      }
    }
    ```

    Args:
        keyword (str): 搜索关键词/Search keyword
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 7.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 5.
        rank_type (Union[Unset, str]): 排行类型/Rank type (popular, surging) Default: 'popular'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.
        filter_by_checked (Union[Unset, bool]): 是否只看已验证/Only verified Default: False.
        commercial_music (Union[Unset, bool]): 是否商业音乐/Commercial music only Default: False.

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
        country_code=country_code,
        filter_by_checked=filter_by_checked,
        commercial_music=commercial_music,
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
    limit: Union[Unset, int] = 5,
    rank_type: Union[Unset, str] = "popular",
    country_code: Union[Unset, str] = "US",
    filter_by_checked: Union[Unset, bool] = False,
    commercial_music: Union[Unset, bool] = False,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索音乐提示/Search sound hints

     # [中文]
    ### 用途:
    - 获取音乐搜索的自动完成提示和推荐
    - 帮助用户快速找到相关音乐
    - 提供搜索建议优化音乐选择

    ### 参数:
    - keyword: 搜索关键词
    - period: 时间范围（天）
    - page: 页码，默认1
    - limit: 每页数量，默认5
    - rank_type: 排行类型，\"popular\"=热门，\"surging\"=上升最快
    - country_code: 国家代码
    - filter_by_checked: 是否只看已验证音乐
    - commercial_music: 是否只看商业音乐

    ### 返回内容说明:
    - `sound_list`: 音乐提示列表
      - `title`: 音乐标题
      - `author`: 音乐作者
      - `match_type`: 匹配类型（标题/作者/标签）
      - `popularity`: 热度评分

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_sound_hint\",
      \"params\": {
        \"keyword\": \"taylor swift\",
        \"limit\": 5
      },
      \"data\": {
        \"sound_list\": [
          {
            \"title\": \"Anti-Hero\",
            \"author\": \"Taylor Swift\",
            \"match_type\": \"artist\",
            \"popularity\": 98
          },
          {
            \"title\": \"Blank Space\",
            \"author\": \"Taylor Swift\",
            \"match_type\": \"artist\",
            \"popularity\": 95
          }
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get auto-complete hints and recommendations for music search
    - Help users quickly find relevant music
    - Provide search suggestions to optimize music selection

    ### Parameters:
    - keyword: Search keyword
    - period: Time period in days
    - page: Page number, default 1
    - limit: Items per page, default 5
    - rank_type: Ranking type, \"popular\"=Popular, \"surging\"=Fastest rising
    - country_code: Country code
    - filter_by_checked: Only show verified music
    - commercial_music: Only show commercial music

    ### Return Description:
    - `sound_list`: Music hint list
      - `title`: Music title
      - `author`: Music author
      - `match_type`: Match type (title/artist/tag)
      - `popularity`: Popularity score

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_sound_hint\",
      \"params\": {
        \"keyword\": \"taylor swift\",
        \"limit\": 5
      },
      \"data\": {
        \"sound_list\": [
          {
            \"title\": \"Anti-Hero\",
            \"author\": \"Taylor Swift\",
            \"match_type\": \"artist\",
            \"popularity\": 98
          },
          {
            \"title\": \"Blank Space\",
            \"author\": \"Taylor Swift\",
            \"match_type\": \"artist\",
            \"popularity\": 95
          }
        ]
      }
    }
    ```

    Args:
        keyword (str): 搜索关键词/Search keyword
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 7.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 5.
        rank_type (Union[Unset, str]): 排行类型/Rank type (popular, surging) Default: 'popular'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.
        filter_by_checked (Union[Unset, bool]): 是否只看已验证/Only verified Default: False.
        commercial_music (Union[Unset, bool]): 是否商业音乐/Commercial music only Default: False.

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
        country_code=country_code,
        filter_by_checked=filter_by_checked,
        commercial_music=commercial_music,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    period: Union[Unset, int] = 7,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 5,
    rank_type: Union[Unset, str] = "popular",
    country_code: Union[Unset, str] = "US",
    filter_by_checked: Union[Unset, bool] = False,
    commercial_music: Union[Unset, bool] = False,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索音乐提示/Search sound hints

     # [中文]
    ### 用途:
    - 获取音乐搜索的自动完成提示和推荐
    - 帮助用户快速找到相关音乐
    - 提供搜索建议优化音乐选择

    ### 参数:
    - keyword: 搜索关键词
    - period: 时间范围（天）
    - page: 页码，默认1
    - limit: 每页数量，默认5
    - rank_type: 排行类型，\"popular\"=热门，\"surging\"=上升最快
    - country_code: 国家代码
    - filter_by_checked: 是否只看已验证音乐
    - commercial_music: 是否只看商业音乐

    ### 返回内容说明:
    - `sound_list`: 音乐提示列表
      - `title`: 音乐标题
      - `author`: 音乐作者
      - `match_type`: 匹配类型（标题/作者/标签）
      - `popularity`: 热度评分

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_sound_hint\",
      \"params\": {
        \"keyword\": \"taylor swift\",
        \"limit\": 5
      },
      \"data\": {
        \"sound_list\": [
          {
            \"title\": \"Anti-Hero\",
            \"author\": \"Taylor Swift\",
            \"match_type\": \"artist\",
            \"popularity\": 98
          },
          {
            \"title\": \"Blank Space\",
            \"author\": \"Taylor Swift\",
            \"match_type\": \"artist\",
            \"popularity\": 95
          }
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get auto-complete hints and recommendations for music search
    - Help users quickly find relevant music
    - Provide search suggestions to optimize music selection

    ### Parameters:
    - keyword: Search keyword
    - period: Time period in days
    - page: Page number, default 1
    - limit: Items per page, default 5
    - rank_type: Ranking type, \"popular\"=Popular, \"surging\"=Fastest rising
    - country_code: Country code
    - filter_by_checked: Only show verified music
    - commercial_music: Only show commercial music

    ### Return Description:
    - `sound_list`: Music hint list
      - `title`: Music title
      - `author`: Music author
      - `match_type`: Match type (title/artist/tag)
      - `popularity`: Popularity score

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_sound_hint\",
      \"params\": {
        \"keyword\": \"taylor swift\",
        \"limit\": 5
      },
      \"data\": {
        \"sound_list\": [
          {
            \"title\": \"Anti-Hero\",
            \"author\": \"Taylor Swift\",
            \"match_type\": \"artist\",
            \"popularity\": 98
          },
          {
            \"title\": \"Blank Space\",
            \"author\": \"Taylor Swift\",
            \"match_type\": \"artist\",
            \"popularity\": 95
          }
        ]
      }
    }
    ```

    Args:
        keyword (str): 搜索关键词/Search keyword
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 7.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 5.
        rank_type (Union[Unset, str]): 排行类型/Rank type (popular, surging) Default: 'popular'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.
        filter_by_checked (Union[Unset, bool]): 是否只看已验证/Only verified Default: False.
        commercial_music (Union[Unset, bool]): 是否商业音乐/Commercial music only Default: False.

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
        country_code=country_code,
        filter_by_checked=filter_by_checked,
        commercial_music=commercial_music,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
    period: Union[Unset, int] = 7,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 5,
    rank_type: Union[Unset, str] = "popular",
    country_code: Union[Unset, str] = "US",
    filter_by_checked: Union[Unset, bool] = False,
    commercial_music: Union[Unset, bool] = False,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索音乐提示/Search sound hints

     # [中文]
    ### 用途:
    - 获取音乐搜索的自动完成提示和推荐
    - 帮助用户快速找到相关音乐
    - 提供搜索建议优化音乐选择

    ### 参数:
    - keyword: 搜索关键词
    - period: 时间范围（天）
    - page: 页码，默认1
    - limit: 每页数量，默认5
    - rank_type: 排行类型，\"popular\"=热门，\"surging\"=上升最快
    - country_code: 国家代码
    - filter_by_checked: 是否只看已验证音乐
    - commercial_music: 是否只看商业音乐

    ### 返回内容说明:
    - `sound_list`: 音乐提示列表
      - `title`: 音乐标题
      - `author`: 音乐作者
      - `match_type`: 匹配类型（标题/作者/标签）
      - `popularity`: 热度评分

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_sound_hint\",
      \"params\": {
        \"keyword\": \"taylor swift\",
        \"limit\": 5
      },
      \"data\": {
        \"sound_list\": [
          {
            \"title\": \"Anti-Hero\",
            \"author\": \"Taylor Swift\",
            \"match_type\": \"artist\",
            \"popularity\": 98
          },
          {
            \"title\": \"Blank Space\",
            \"author\": \"Taylor Swift\",
            \"match_type\": \"artist\",
            \"popularity\": 95
          }
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get auto-complete hints and recommendations for music search
    - Help users quickly find relevant music
    - Provide search suggestions to optimize music selection

    ### Parameters:
    - keyword: Search keyword
    - period: Time period in days
    - page: Page number, default 1
    - limit: Items per page, default 5
    - rank_type: Ranking type, \"popular\"=Popular, \"surging\"=Fastest rising
    - country_code: Country code
    - filter_by_checked: Only show verified music
    - commercial_music: Only show commercial music

    ### Return Description:
    - `sound_list`: Music hint list
      - `title`: Music title
      - `author`: Music author
      - `match_type`: Match type (title/artist/tag)
      - `popularity`: Popularity score

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_sound_hint\",
      \"params\": {
        \"keyword\": \"taylor swift\",
        \"limit\": 5
      },
      \"data\": {
        \"sound_list\": [
          {
            \"title\": \"Anti-Hero\",
            \"author\": \"Taylor Swift\",
            \"match_type\": \"artist\",
            \"popularity\": 98
          },
          {
            \"title\": \"Blank Space\",
            \"author\": \"Taylor Swift\",
            \"match_type\": \"artist\",
            \"popularity\": 95
          }
        ]
      }
    }
    ```

    Args:
        keyword (str): 搜索关键词/Search keyword
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 7.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 5.
        rank_type (Union[Unset, str]): 排行类型/Rank type (popular, surging) Default: 'popular'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.
        filter_by_checked (Union[Unset, bool]): 是否只看已验证/Only verified Default: False.
        commercial_music (Union[Unset, bool]): 是否商业音乐/Commercial music only Default: False.

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
            country_code=country_code,
            filter_by_checked=filter_by_checked,
            commercial_music=commercial_music,
        )
    ).parsed
