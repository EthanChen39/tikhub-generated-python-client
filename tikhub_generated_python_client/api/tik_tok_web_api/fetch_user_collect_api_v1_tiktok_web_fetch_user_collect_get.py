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
    cookie: str,
    sec_uid: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 30,
    cover_format: Union[Unset, int] = 2,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["cookie"] = cookie

    params["secUid"] = sec_uid

    params["cursor"] = cursor

    params["count"] = count

    params["coverFormat"] = cover_format

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/web/fetch_user_collect",
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
    cookie: str,
    sec_uid: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 30,
    cover_format: Union[Unset, int] = 2,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户的收藏列表/Get user favorites

     # [中文]
    ### 用途:
    - 获取用户的收藏列表
    - 注意: 该接口目前只能获取自己的收藏列表，需要提供自己账号的cookie。
    ### 参数:
    - cookie: 用户cookie
    - secUid: 用户secUid
    - cursor: 翻页游标
    - count: 每页数量
    - coverFormat: 封面格式
    ### 返回:
    - 用户的收藏列表

    # [English]
    ### Purpose:
    - Get user favorites
    - Note: This interface can currently only get your own favorites list, you need to provide your
    account cookie.
    ### Parameters:
    - cookie: User cookie
    - secUid: User secUid
    - cursor: Page cursor
    - count: Number per page
    - coverFormat: Cover format
    ### Return:
    - User favorites

    # [示例/Example]
    cookie = \"Your_Cookie\"
    secUid = \"Your_SecUid\"
    cursor = 0
    count = 30
    coverFormat = 2

    Args:
        cookie (str): 用户cookie/User cookie
        sec_uid (str): 用户secUid/User secUid
        cursor (Union[Unset, int]): 翻页游标/Page cursor Default: 0.
        count (Union[Unset, int]): 每页数量/Number per page Default: 30.
        cover_format (Union[Unset, int]): 封面格式/Cover format Default: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        cookie=cookie,
        sec_uid=sec_uid,
        cursor=cursor,
        count=count,
        cover_format=cover_format,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cookie: str,
    sec_uid: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 30,
    cover_format: Union[Unset, int] = 2,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户的收藏列表/Get user favorites

     # [中文]
    ### 用途:
    - 获取用户的收藏列表
    - 注意: 该接口目前只能获取自己的收藏列表，需要提供自己账号的cookie。
    ### 参数:
    - cookie: 用户cookie
    - secUid: 用户secUid
    - cursor: 翻页游标
    - count: 每页数量
    - coverFormat: 封面格式
    ### 返回:
    - 用户的收藏列表

    # [English]
    ### Purpose:
    - Get user favorites
    - Note: This interface can currently only get your own favorites list, you need to provide your
    account cookie.
    ### Parameters:
    - cookie: User cookie
    - secUid: User secUid
    - cursor: Page cursor
    - count: Number per page
    - coverFormat: Cover format
    ### Return:
    - User favorites

    # [示例/Example]
    cookie = \"Your_Cookie\"
    secUid = \"Your_SecUid\"
    cursor = 0
    count = 30
    coverFormat = 2

    Args:
        cookie (str): 用户cookie/User cookie
        sec_uid (str): 用户secUid/User secUid
        cursor (Union[Unset, int]): 翻页游标/Page cursor Default: 0.
        count (Union[Unset, int]): 每页数量/Number per page Default: 30.
        cover_format (Union[Unset, int]): 封面格式/Cover format Default: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        cookie=cookie,
        sec_uid=sec_uid,
        cursor=cursor,
        count=count,
        cover_format=cover_format,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cookie: str,
    sec_uid: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 30,
    cover_format: Union[Unset, int] = 2,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户的收藏列表/Get user favorites

     # [中文]
    ### 用途:
    - 获取用户的收藏列表
    - 注意: 该接口目前只能获取自己的收藏列表，需要提供自己账号的cookie。
    ### 参数:
    - cookie: 用户cookie
    - secUid: 用户secUid
    - cursor: 翻页游标
    - count: 每页数量
    - coverFormat: 封面格式
    ### 返回:
    - 用户的收藏列表

    # [English]
    ### Purpose:
    - Get user favorites
    - Note: This interface can currently only get your own favorites list, you need to provide your
    account cookie.
    ### Parameters:
    - cookie: User cookie
    - secUid: User secUid
    - cursor: Page cursor
    - count: Number per page
    - coverFormat: Cover format
    ### Return:
    - User favorites

    # [示例/Example]
    cookie = \"Your_Cookie\"
    secUid = \"Your_SecUid\"
    cursor = 0
    count = 30
    coverFormat = 2

    Args:
        cookie (str): 用户cookie/User cookie
        sec_uid (str): 用户secUid/User secUid
        cursor (Union[Unset, int]): 翻页游标/Page cursor Default: 0.
        count (Union[Unset, int]): 每页数量/Number per page Default: 30.
        cover_format (Union[Unset, int]): 封面格式/Cover format Default: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        cookie=cookie,
        sec_uid=sec_uid,
        cursor=cursor,
        count=count,
        cover_format=cover_format,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cookie: str,
    sec_uid: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 30,
    cover_format: Union[Unset, int] = 2,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户的收藏列表/Get user favorites

     # [中文]
    ### 用途:
    - 获取用户的收藏列表
    - 注意: 该接口目前只能获取自己的收藏列表，需要提供自己账号的cookie。
    ### 参数:
    - cookie: 用户cookie
    - secUid: 用户secUid
    - cursor: 翻页游标
    - count: 每页数量
    - coverFormat: 封面格式
    ### 返回:
    - 用户的收藏列表

    # [English]
    ### Purpose:
    - Get user favorites
    - Note: This interface can currently only get your own favorites list, you need to provide your
    account cookie.
    ### Parameters:
    - cookie: User cookie
    - secUid: User secUid
    - cursor: Page cursor
    - count: Number per page
    - coverFormat: Cover format
    ### Return:
    - User favorites

    # [示例/Example]
    cookie = \"Your_Cookie\"
    secUid = \"Your_SecUid\"
    cursor = 0
    count = 30
    coverFormat = 2

    Args:
        cookie (str): 用户cookie/User cookie
        sec_uid (str): 用户secUid/User secUid
        cursor (Union[Unset, int]): 翻页游标/Page cursor Default: 0.
        count (Union[Unset, int]): 每页数量/Number per page Default: 30.
        cover_format (Union[Unset, int]): 封面格式/Cover format Default: 2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            cookie=cookie,
            sec_uid=sec_uid,
            cursor=cursor,
            count=count,
            cover_format=cover_format,
        )
    ).parsed
