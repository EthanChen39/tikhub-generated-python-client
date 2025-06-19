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
    pn: Union[Unset, int] = 1,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["pn"] = pn

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/bilibili/web/fetch_com_popular",
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
    pn: Union[Unset, int] = 1,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取综合热门视频信息/Get comprehensive popular video information

     # [中文]
    ### 用途:
    - 获取综合热门视频信息
    ### 参数:
    - pn: 页码
    ### 返回:
    - 综合热门视频信息

    # [English]
    ### Purpose:
    - Get comprehensive popular video information
    ### Parameters:
    - pn: Page number
    ### Return:
    - comprehensive popular video information

    # [示例/Example]
    pn = 1

    Args:
        pn (Union[Unset, int]): 页码/Page number Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        pn=pn,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    pn: Union[Unset, int] = 1,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取综合热门视频信息/Get comprehensive popular video information

     # [中文]
    ### 用途:
    - 获取综合热门视频信息
    ### 参数:
    - pn: 页码
    ### 返回:
    - 综合热门视频信息

    # [English]
    ### Purpose:
    - Get comprehensive popular video information
    ### Parameters:
    - pn: Page number
    ### Return:
    - comprehensive popular video information

    # [示例/Example]
    pn = 1

    Args:
        pn (Union[Unset, int]): 页码/Page number Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        pn=pn,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    pn: Union[Unset, int] = 1,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取综合热门视频信息/Get comprehensive popular video information

     # [中文]
    ### 用途:
    - 获取综合热门视频信息
    ### 参数:
    - pn: 页码
    ### 返回:
    - 综合热门视频信息

    # [English]
    ### Purpose:
    - Get comprehensive popular video information
    ### Parameters:
    - pn: Page number
    ### Return:
    - comprehensive popular video information

    # [示例/Example]
    pn = 1

    Args:
        pn (Union[Unset, int]): 页码/Page number Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        pn=pn,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    pn: Union[Unset, int] = 1,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取综合热门视频信息/Get comprehensive popular video information

     # [中文]
    ### 用途:
    - 获取综合热门视频信息
    ### 参数:
    - pn: 页码
    ### 返回:
    - 综合热门视频信息

    # [English]
    ### Purpose:
    - Get comprehensive popular video information
    ### Parameters:
    - pn: Page number
    ### Return:
    - comprehensive popular video information

    # [示例/Example]
    pn = 1

    Args:
        pn (Union[Unset, int]): 页码/Page number Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            pn=pn,
        )
    ).parsed
