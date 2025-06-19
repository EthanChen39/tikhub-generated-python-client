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
    user_id: int,
    offset: Union[Unset, int] = 0,
    count: Union[Unset, int] = 21,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["user_id"] = user_id

    params["offset"] = offset

    params["count"] = count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/app/v3/fetch_user_repost_videos",
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
    user_id: int,
    offset: Union[Unset, int] = 0,
    count: Union[Unset, int] = 21,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取用户转发的作品数据/Get user repost video data

     # [中文]
    ### 用途:
    - 获取用户转发的作品数据
    ### 参数:
    - user_id: 用户id，可以通过 handler_user_profile 端点获取，响应中的关键字为uid。
    - offset: 偏移量
    - count: 数量
    ### 返回:
    - 用户转发作品数据

    # [English]
    ### Purpose:
    - Get user repost video data
    ### Parameters:
    - user_id: User id, which can be obtained through the handler_user_profile endpoint, with the
    keyword uid in the response.
    - offset: Offset
    - count: Number
    ### Return:
    - User repost video data

    # [示例/Example]
    user_id = 107955
    offset = 0
    count = 21

    Args:
        user_id (int): 用户id/User id
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 21.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        offset=offset,
        count=count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: int,
    offset: Union[Unset, int] = 0,
    count: Union[Unset, int] = 21,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取用户转发的作品数据/Get user repost video data

     # [中文]
    ### 用途:
    - 获取用户转发的作品数据
    ### 参数:
    - user_id: 用户id，可以通过 handler_user_profile 端点获取，响应中的关键字为uid。
    - offset: 偏移量
    - count: 数量
    ### 返回:
    - 用户转发作品数据

    # [English]
    ### Purpose:
    - Get user repost video data
    ### Parameters:
    - user_id: User id, which can be obtained through the handler_user_profile endpoint, with the
    keyword uid in the response.
    - offset: Offset
    - count: Number
    ### Return:
    - User repost video data

    # [示例/Example]
    user_id = 107955
    offset = 0
    count = 21

    Args:
        user_id (int): 用户id/User id
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 21.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        offset=offset,
        count=count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: int,
    offset: Union[Unset, int] = 0,
    count: Union[Unset, int] = 21,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取用户转发的作品数据/Get user repost video data

     # [中文]
    ### 用途:
    - 获取用户转发的作品数据
    ### 参数:
    - user_id: 用户id，可以通过 handler_user_profile 端点获取，响应中的关键字为uid。
    - offset: 偏移量
    - count: 数量
    ### 返回:
    - 用户转发作品数据

    # [English]
    ### Purpose:
    - Get user repost video data
    ### Parameters:
    - user_id: User id, which can be obtained through the handler_user_profile endpoint, with the
    keyword uid in the response.
    - offset: Offset
    - count: Number
    ### Return:
    - User repost video data

    # [示例/Example]
    user_id = 107955
    offset = 0
    count = 21

    Args:
        user_id (int): 用户id/User id
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 21.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        offset=offset,
        count=count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: int,
    offset: Union[Unset, int] = 0,
    count: Union[Unset, int] = 21,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取用户转发的作品数据/Get user repost video data

     # [中文]
    ### 用途:
    - 获取用户转发的作品数据
    ### 参数:
    - user_id: 用户id，可以通过 handler_user_profile 端点获取，响应中的关键字为uid。
    - offset: 偏移量
    - count: 数量
    ### 返回:
    - 用户转发作品数据

    # [English]
    ### Purpose:
    - Get user repost video data
    ### Parameters:
    - user_id: User id, which can be obtained through the handler_user_profile endpoint, with the
    keyword uid in the response.
    - offset: Offset
    - count: Number
    ### Return:
    - User repost video data

    # [示例/Example]
    user_id = 107955
    offset = 0
    count = 21

    Args:
        user_id (int): 用户id/User id
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 21.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            offset=offset,
            count=count,
        )
    ).parsed
