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
    page: int,
    page_size: int,
    keyword: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    params["keyword"] = keyword

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/billboard/fetch_hot_challenge_list",
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
    page: int,
    page_size: int,
    keyword: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取挑战热榜/Fetch hot challenge list

     # [中文]
    ### 用途:
    - 获取挑战榜
    ### 参数:
    - page: 页码
    - page_size: 每页数量
    - keyword: 热点搜索词
    ### 返回:
    - 挑战榜

    # [English]
    ### Purpose:
    - Get the challenge list
    ### Parameters:
    - page: Page number
    - page_size: Number of items per page
    - keyword: Hot search term
    ### Return:
    - Challenge list

    Args:
        page (int): 页码
        page_size (int): 每页数量
        keyword (Union[Unset, str]): 热点搜索词 Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        keyword=keyword,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page: int,
    page_size: int,
    keyword: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取挑战热榜/Fetch hot challenge list

     # [中文]
    ### 用途:
    - 获取挑战榜
    ### 参数:
    - page: 页码
    - page_size: 每页数量
    - keyword: 热点搜索词
    ### 返回:
    - 挑战榜

    # [English]
    ### Purpose:
    - Get the challenge list
    ### Parameters:
    - page: Page number
    - page_size: Number of items per page
    - keyword: Hot search term
    ### Return:
    - Challenge list

    Args:
        page (int): 页码
        page_size (int): 每页数量
        keyword (Union[Unset, str]): 热点搜索词 Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        keyword=keyword,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int,
    page_size: int,
    keyword: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取挑战热榜/Fetch hot challenge list

     # [中文]
    ### 用途:
    - 获取挑战榜
    ### 参数:
    - page: 页码
    - page_size: 每页数量
    - keyword: 热点搜索词
    ### 返回:
    - 挑战榜

    # [English]
    ### Purpose:
    - Get the challenge list
    ### Parameters:
    - page: Page number
    - page_size: Number of items per page
    - keyword: Hot search term
    ### Return:
    - Challenge list

    Args:
        page (int): 页码
        page_size (int): 每页数量
        keyword (Union[Unset, str]): 热点搜索词 Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        keyword=keyword,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int,
    page_size: int,
    keyword: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取挑战热榜/Fetch hot challenge list

     # [中文]
    ### 用途:
    - 获取挑战榜
    ### 参数:
    - page: 页码
    - page_size: 每页数量
    - keyword: 热点搜索词
    ### 返回:
    - 挑战榜

    # [English]
    ### Purpose:
    - Get the challenge list
    ### Parameters:
    - page: Page number
    - page_size: Number of items per page
    - keyword: Hot search term
    ### Return:
    - Challenge list

    Args:
        page (int): 页码
        page_size (int): 每页数量
        keyword (Union[Unset, str]): 热点搜索词 Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            keyword=keyword,
        )
    ).parsed
