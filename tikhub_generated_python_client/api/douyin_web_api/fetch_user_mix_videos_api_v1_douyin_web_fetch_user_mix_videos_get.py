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
    mix_id: str,
    max_cursor: Union[Unset, int] = 0,
    counts: Union[Unset, int] = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["mix_id"] = mix_id

    params["max_cursor"] = max_cursor

    params["counts"] = counts

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/web/fetch_user_mix_videos",
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
    mix_id: str,
    max_cursor: Union[Unset, int] = 0,
    counts: Union[Unset, int] = 20,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户合辑作品数据/Get user mix video data

     # [中文]
    ### 用途:
    - 获取用户合辑作品数据
    ### 参数:
    - mix_id: 合辑id
    - max_cursor: 最大游标
    - count: 最大数量
    ### 返回:
    - 用户作品数据

    # [English]
    ### Purpose:
    - Get user mix video data
    ### Parameters:
    - mix_id: Mix id
    - max_cursor: Maximum cursor
    - count: Maximum number
    ### Return:
    - User video data

    # [示例/Example]
    url = https://www.douyin.com/collection/7348687990509553679
    mix_id = \"7348687990509553679\"
    max_cursor = 0
    counts = 20

    Args:
        mix_id (str): 合辑id/Mix id
        max_cursor (Union[Unset, int]): 最大游标/Maximum cursor Default: 0.
        counts (Union[Unset, int]): 每页数量/Number per page Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        mix_id=mix_id,
        max_cursor=max_cursor,
        counts=counts,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    mix_id: str,
    max_cursor: Union[Unset, int] = 0,
    counts: Union[Unset, int] = 20,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户合辑作品数据/Get user mix video data

     # [中文]
    ### 用途:
    - 获取用户合辑作品数据
    ### 参数:
    - mix_id: 合辑id
    - max_cursor: 最大游标
    - count: 最大数量
    ### 返回:
    - 用户作品数据

    # [English]
    ### Purpose:
    - Get user mix video data
    ### Parameters:
    - mix_id: Mix id
    - max_cursor: Maximum cursor
    - count: Maximum number
    ### Return:
    - User video data

    # [示例/Example]
    url = https://www.douyin.com/collection/7348687990509553679
    mix_id = \"7348687990509553679\"
    max_cursor = 0
    counts = 20

    Args:
        mix_id (str): 合辑id/Mix id
        max_cursor (Union[Unset, int]): 最大游标/Maximum cursor Default: 0.
        counts (Union[Unset, int]): 每页数量/Number per page Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        mix_id=mix_id,
        max_cursor=max_cursor,
        counts=counts,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    mix_id: str,
    max_cursor: Union[Unset, int] = 0,
    counts: Union[Unset, int] = 20,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户合辑作品数据/Get user mix video data

     # [中文]
    ### 用途:
    - 获取用户合辑作品数据
    ### 参数:
    - mix_id: 合辑id
    - max_cursor: 最大游标
    - count: 最大数量
    ### 返回:
    - 用户作品数据

    # [English]
    ### Purpose:
    - Get user mix video data
    ### Parameters:
    - mix_id: Mix id
    - max_cursor: Maximum cursor
    - count: Maximum number
    ### Return:
    - User video data

    # [示例/Example]
    url = https://www.douyin.com/collection/7348687990509553679
    mix_id = \"7348687990509553679\"
    max_cursor = 0
    counts = 20

    Args:
        mix_id (str): 合辑id/Mix id
        max_cursor (Union[Unset, int]): 最大游标/Maximum cursor Default: 0.
        counts (Union[Unset, int]): 每页数量/Number per page Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        mix_id=mix_id,
        max_cursor=max_cursor,
        counts=counts,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    mix_id: str,
    max_cursor: Union[Unset, int] = 0,
    counts: Union[Unset, int] = 20,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户合辑作品数据/Get user mix video data

     # [中文]
    ### 用途:
    - 获取用户合辑作品数据
    ### 参数:
    - mix_id: 合辑id
    - max_cursor: 最大游标
    - count: 最大数量
    ### 返回:
    - 用户作品数据

    # [English]
    ### Purpose:
    - Get user mix video data
    ### Parameters:
    - mix_id: Mix id
    - max_cursor: Maximum cursor
    - count: Maximum number
    ### Return:
    - User video data

    # [示例/Example]
    url = https://www.douyin.com/collection/7348687990509553679
    mix_id = \"7348687990509553679\"
    max_cursor = 0
    counts = 20

    Args:
        mix_id (str): 合辑id/Mix id
        max_cursor (Union[Unset, int]): 最大游标/Maximum cursor Default: 0.
        counts (Union[Unset, int]): 每页数量/Number per page Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            mix_id=mix_id,
            max_cursor=max_cursor,
            counts=counts,
        )
    ).parsed
