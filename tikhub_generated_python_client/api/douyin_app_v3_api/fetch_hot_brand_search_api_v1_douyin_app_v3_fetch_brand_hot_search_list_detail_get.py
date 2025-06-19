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
    category_id: int,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["category_id"] = category_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/app/v3/fetch_brand_hot_search_list_detail",
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
    category_id: int,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取抖音品牌热榜具体分类数据/Get Douyin brand hot search list detail data

     # [中文]
    ### 用途:
    - 获取抖音品牌热榜具体分类数据
    ### 参数:
    - category_id: 分类id
    ### 返回:
    - 品牌热搜榜具体分类数据

    # [English]
    ### Purpose:
    - Get Douyin brand hot search list detail data
    ### Parameters:
    - category_id: Category id
    ### Return:
    - Hot brand search list detail data

    # [示例/Example]
    category_id = 10

    Args:
        category_id (int): 分类id/Category id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        category_id=category_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    category_id: int,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取抖音品牌热榜具体分类数据/Get Douyin brand hot search list detail data

     # [中文]
    ### 用途:
    - 获取抖音品牌热榜具体分类数据
    ### 参数:
    - category_id: 分类id
    ### 返回:
    - 品牌热搜榜具体分类数据

    # [English]
    ### Purpose:
    - Get Douyin brand hot search list detail data
    ### Parameters:
    - category_id: Category id
    ### Return:
    - Hot brand search list detail data

    # [示例/Example]
    category_id = 10

    Args:
        category_id (int): 分类id/Category id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        category_id=category_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    category_id: int,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取抖音品牌热榜具体分类数据/Get Douyin brand hot search list detail data

     # [中文]
    ### 用途:
    - 获取抖音品牌热榜具体分类数据
    ### 参数:
    - category_id: 分类id
    ### 返回:
    - 品牌热搜榜具体分类数据

    # [English]
    ### Purpose:
    - Get Douyin brand hot search list detail data
    ### Parameters:
    - category_id: Category id
    ### Return:
    - Hot brand search list detail data

    # [示例/Example]
    category_id = 10

    Args:
        category_id (int): 分类id/Category id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        category_id=category_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    category_id: int,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取抖音品牌热榜具体分类数据/Get Douyin brand hot search list detail data

     # [中文]
    ### 用途:
    - 获取抖音品牌热榜具体分类数据
    ### 参数:
    - category_id: 分类id
    ### 返回:
    - 品牌热搜榜具体分类数据

    # [English]
    ### Purpose:
    - Get Douyin brand hot search list detail data
    ### Parameters:
    - category_id: Category id
    ### Return:
    - Hot brand search list detail data

    # [示例/Example]
    category_id = 10

    Args:
        category_id (int): 分类id/Category id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            category_id=category_id,
        )
    ).parsed
