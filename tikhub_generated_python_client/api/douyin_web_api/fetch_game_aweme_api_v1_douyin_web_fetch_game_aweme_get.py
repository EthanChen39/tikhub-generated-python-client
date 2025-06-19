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
    count: int,
    refresh_index: Union[Unset, int] = 1,
    cookie: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["count"] = count

    params["refresh_index"] = refresh_index

    params["cookie"] = cookie

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/web/fetch_game_aweme",
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
    count: int,
    refresh_index: Union[Unset, int] = 1,
    cookie: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """游戏作品推荐/Game Video

     # [中文]
    ### 用途:
    - 知识作品
    ### 参数:
    - count: 每页数量，默认为16
    - refresh_index: 翻页索引，默认为1
    - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题
    - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie

    ### 返回:
    - 游戏作品数据

    # [English]
    ### Purpose:
    - Knowledge Video
    ### Parameters:
    - count: Number per page, default is 16
    - refresh_index: Paging index, default is 1
    - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may
    be a problem of data duplication when paging
    - Guest cookie acquisition interface:
    https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie

    ### Return:
    - Game Video data

    Args:
        count (int): 每页数量/Number per page
        refresh_index (Union[Unset, int]): 翻页索引/Paging index Default: 1.
        cookie (Union[Unset, str]): 用户自行提供的Cookie/User provided Cookie

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        count=count,
        refresh_index=refresh_index,
        cookie=cookie,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    count: int,
    refresh_index: Union[Unset, int] = 1,
    cookie: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """游戏作品推荐/Game Video

     # [中文]
    ### 用途:
    - 知识作品
    ### 参数:
    - count: 每页数量，默认为16
    - refresh_index: 翻页索引，默认为1
    - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题
    - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie

    ### 返回:
    - 游戏作品数据

    # [English]
    ### Purpose:
    - Knowledge Video
    ### Parameters:
    - count: Number per page, default is 16
    - refresh_index: Paging index, default is 1
    - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may
    be a problem of data duplication when paging
    - Guest cookie acquisition interface:
    https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie

    ### Return:
    - Game Video data

    Args:
        count (int): 每页数量/Number per page
        refresh_index (Union[Unset, int]): 翻页索引/Paging index Default: 1.
        cookie (Union[Unset, str]): 用户自行提供的Cookie/User provided Cookie

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        count=count,
        refresh_index=refresh_index,
        cookie=cookie,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    count: int,
    refresh_index: Union[Unset, int] = 1,
    cookie: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """游戏作品推荐/Game Video

     # [中文]
    ### 用途:
    - 知识作品
    ### 参数:
    - count: 每页数量，默认为16
    - refresh_index: 翻页索引，默认为1
    - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题
    - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie

    ### 返回:
    - 游戏作品数据

    # [English]
    ### Purpose:
    - Knowledge Video
    ### Parameters:
    - count: Number per page, default is 16
    - refresh_index: Paging index, default is 1
    - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may
    be a problem of data duplication when paging
    - Guest cookie acquisition interface:
    https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie

    ### Return:
    - Game Video data

    Args:
        count (int): 每页数量/Number per page
        refresh_index (Union[Unset, int]): 翻页索引/Paging index Default: 1.
        cookie (Union[Unset, str]): 用户自行提供的Cookie/User provided Cookie

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        count=count,
        refresh_index=refresh_index,
        cookie=cookie,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    count: int,
    refresh_index: Union[Unset, int] = 1,
    cookie: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """游戏作品推荐/Game Video

     # [中文]
    ### 用途:
    - 知识作品
    ### 参数:
    - count: 每页数量，默认为16
    - refresh_index: 翻页索引，默认为1
    - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题
    - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie

    ### 返回:
    - 游戏作品数据

    # [English]
    ### Purpose:
    - Knowledge Video
    ### Parameters:
    - count: Number per page, default is 16
    - refresh_index: Paging index, default is 1
    - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may
    be a problem of data duplication when paging
    - Guest cookie acquisition interface:
    https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie

    ### Return:
    - Game Video data

    Args:
        count (int): 每页数量/Number per page
        refresh_index (Union[Unset, int]): 翻页索引/Paging index Default: 1.
        cookie (Union[Unset, str]): 用户自行提供的Cookie/User provided Cookie

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            count=count,
            refresh_index=refresh_index,
            cookie=cookie,
        )
    ).parsed
