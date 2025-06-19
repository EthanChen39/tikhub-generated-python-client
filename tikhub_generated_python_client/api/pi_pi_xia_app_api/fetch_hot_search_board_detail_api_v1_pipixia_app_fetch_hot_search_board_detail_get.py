from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import UNSET, Response


def _get_kwargs(
    *,
    block_type: int,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["block_type"] = block_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/pipixia/app/fetch_hot_search_board_detail",
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
    block_type: int,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取热搜榜单详情/Get hot search board detail

     # [中文]
    ### 用途:
    - 获取热搜榜单详情数据。
    ### 参数:
    - block_type: 榜单类型，可以从`/fetch_hot_search_board_list`接口中获取。
    ### 返回:
    - 热搜榜单详情数据

    # [English]
    ### Purpose:
    - Get hot search board detail data.
    ### Parameters:
    - block_type: Board type, can be obtained from the `/fetch_hot_search_board_list` interface.
    ### Return:
    - Hot search board detail data

    # [示例/Example]
    block_type = 12

    Args:
        block_type (int): 榜单类型/Board type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        block_type=block_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    block_type: int,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取热搜榜单详情/Get hot search board detail

     # [中文]
    ### 用途:
    - 获取热搜榜单详情数据。
    ### 参数:
    - block_type: 榜单类型，可以从`/fetch_hot_search_board_list`接口中获取。
    ### 返回:
    - 热搜榜单详情数据

    # [English]
    ### Purpose:
    - Get hot search board detail data.
    ### Parameters:
    - block_type: Board type, can be obtained from the `/fetch_hot_search_board_list` interface.
    ### Return:
    - Hot search board detail data

    # [示例/Example]
    block_type = 12

    Args:
        block_type (int): 榜单类型/Board type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        block_type=block_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    block_type: int,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取热搜榜单详情/Get hot search board detail

     # [中文]
    ### 用途:
    - 获取热搜榜单详情数据。
    ### 参数:
    - block_type: 榜单类型，可以从`/fetch_hot_search_board_list`接口中获取。
    ### 返回:
    - 热搜榜单详情数据

    # [English]
    ### Purpose:
    - Get hot search board detail data.
    ### Parameters:
    - block_type: Board type, can be obtained from the `/fetch_hot_search_board_list` interface.
    ### Return:
    - Hot search board detail data

    # [示例/Example]
    block_type = 12

    Args:
        block_type (int): 榜单类型/Board type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        block_type=block_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    block_type: int,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取热搜榜单详情/Get hot search board detail

     # [中文]
    ### 用途:
    - 获取热搜榜单详情数据。
    ### 参数:
    - block_type: 榜单类型，可以从`/fetch_hot_search_board_list`接口中获取。
    ### 返回:
    - 热搜榜单详情数据

    # [English]
    ### Purpose:
    - Get hot search board detail data.
    ### Parameters:
    - block_type: Board type, can be obtained from the `/fetch_hot_search_board_list` interface.
    ### Return:
    - Hot search board detail data

    # [示例/Example]
    block_type = 12

    Args:
        block_type (int): 榜单类型/Board type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            block_type=block_type,
        )
    ).parsed
