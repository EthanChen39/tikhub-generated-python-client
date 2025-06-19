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
    sec_uid: str,
    count: Union[Unset, int] = 30,
    max_cursor: Union[Unset, int] = 0,
    min_cursor: Union[Unset, int] = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["secUid"] = sec_uid

    params["count"] = count

    params["maxCursor"] = max_cursor

    params["minCursor"] = min_cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/web/fetch_user_follow",
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
    sec_uid: str,
    count: Union[Unset, int] = 30,
    max_cursor: Union[Unset, int] = 0,
    min_cursor: Union[Unset, int] = 0,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户的关注列表/Get user followings

     # [中文]
    ### 用途:
    - 获取用户的关注列表
    ### 参数:
    - secUid: 用户secUid
    - count: 每页数量
    - maxCursor: 最大游标
    - minCursor: 最小游标
    ### 返回:
    - 用户的关注列表

    # [English]
    ### Purpose:
    - Get user followings
    ### Parameters:
    - secUid: User secUid
    - count: Number per page
    - maxCursor: Max cursor
    - minCursor: Min cursor
    ### Return:
    - User followings

    # [示例/Example]
    secUid = \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\"
    count = 30
    maxCursor = 0
    minCursor = 0

    Args:
        sec_uid (str): 用户secUid/User secUid
        count (Union[Unset, int]): 每页数量/Number per page Default: 30.
        max_cursor (Union[Unset, int]): 最大游标/Max cursor Default: 0.
        min_cursor (Union[Unset, int]): 最小游标/Min cursor Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        sec_uid=sec_uid,
        count=count,
        max_cursor=max_cursor,
        min_cursor=min_cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    sec_uid: str,
    count: Union[Unset, int] = 30,
    max_cursor: Union[Unset, int] = 0,
    min_cursor: Union[Unset, int] = 0,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户的关注列表/Get user followings

     # [中文]
    ### 用途:
    - 获取用户的关注列表
    ### 参数:
    - secUid: 用户secUid
    - count: 每页数量
    - maxCursor: 最大游标
    - minCursor: 最小游标
    ### 返回:
    - 用户的关注列表

    # [English]
    ### Purpose:
    - Get user followings
    ### Parameters:
    - secUid: User secUid
    - count: Number per page
    - maxCursor: Max cursor
    - minCursor: Min cursor
    ### Return:
    - User followings

    # [示例/Example]
    secUid = \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\"
    count = 30
    maxCursor = 0
    minCursor = 0

    Args:
        sec_uid (str): 用户secUid/User secUid
        count (Union[Unset, int]): 每页数量/Number per page Default: 30.
        max_cursor (Union[Unset, int]): 最大游标/Max cursor Default: 0.
        min_cursor (Union[Unset, int]): 最小游标/Min cursor Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        sec_uid=sec_uid,
        count=count,
        max_cursor=max_cursor,
        min_cursor=min_cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    sec_uid: str,
    count: Union[Unset, int] = 30,
    max_cursor: Union[Unset, int] = 0,
    min_cursor: Union[Unset, int] = 0,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户的关注列表/Get user followings

     # [中文]
    ### 用途:
    - 获取用户的关注列表
    ### 参数:
    - secUid: 用户secUid
    - count: 每页数量
    - maxCursor: 最大游标
    - minCursor: 最小游标
    ### 返回:
    - 用户的关注列表

    # [English]
    ### Purpose:
    - Get user followings
    ### Parameters:
    - secUid: User secUid
    - count: Number per page
    - maxCursor: Max cursor
    - minCursor: Min cursor
    ### Return:
    - User followings

    # [示例/Example]
    secUid = \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\"
    count = 30
    maxCursor = 0
    minCursor = 0

    Args:
        sec_uid (str): 用户secUid/User secUid
        count (Union[Unset, int]): 每页数量/Number per page Default: 30.
        max_cursor (Union[Unset, int]): 最大游标/Max cursor Default: 0.
        min_cursor (Union[Unset, int]): 最小游标/Min cursor Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        sec_uid=sec_uid,
        count=count,
        max_cursor=max_cursor,
        min_cursor=min_cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    sec_uid: str,
    count: Union[Unset, int] = 30,
    max_cursor: Union[Unset, int] = 0,
    min_cursor: Union[Unset, int] = 0,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户的关注列表/Get user followings

     # [中文]
    ### 用途:
    - 获取用户的关注列表
    ### 参数:
    - secUid: 用户secUid
    - count: 每页数量
    - maxCursor: 最大游标
    - minCursor: 最小游标
    ### 返回:
    - 用户的关注列表

    # [English]
    ### Purpose:
    - Get user followings
    ### Parameters:
    - secUid: User secUid
    - count: Number per page
    - maxCursor: Max cursor
    - minCursor: Min cursor
    ### Return:
    - User followings

    # [示例/Example]
    secUid = \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\"
    count = 30
    maxCursor = 0
    minCursor = 0

    Args:
        sec_uid (str): 用户secUid/User secUid
        count (Union[Unset, int]): 每页数量/Number per page Default: 30.
        max_cursor (Union[Unset, int]): 最大游标/Max cursor Default: 0.
        min_cursor (Union[Unset, int]): 最小游标/Min cursor Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            sec_uid=sec_uid,
            count=count,
            max_cursor=max_cursor,
            min_cursor=min_cursor,
        )
    ).parsed
