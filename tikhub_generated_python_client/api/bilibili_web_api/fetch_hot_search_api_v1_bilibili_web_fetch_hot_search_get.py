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
    limit: Any,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/bilibili/web/fetch_hot_search",
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
    limit: Any,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取热门搜索信息/Get hot search data

     # [中文]
    ### 用途:
    - 获取热门搜索信息
    ### 参数:
    - limit: 返回数量
    ### 返回:
    - 热门搜索信息
    ### 说明:
    - limit默认为10，上限为50

    # [English]
    ### Purpose:
    - Get hot search data
    ### Parameters:
    - limit: Return number
    ### Return:
    - Hot search data
    ### Note:
    - limit default is 10, maximum is 50

    # [示例/Example]
    limit = 10

    Args:
        limit (Any): 返回数量/Return number

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: Any,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取热门搜索信息/Get hot search data

     # [中文]
    ### 用途:
    - 获取热门搜索信息
    ### 参数:
    - limit: 返回数量
    ### 返回:
    - 热门搜索信息
    ### 说明:
    - limit默认为10，上限为50

    # [English]
    ### Purpose:
    - Get hot search data
    ### Parameters:
    - limit: Return number
    ### Return:
    - Hot search data
    ### Note:
    - limit default is 10, maximum is 50

    # [示例/Example]
    limit = 10

    Args:
        limit (Any): 返回数量/Return number

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: Any,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取热门搜索信息/Get hot search data

     # [中文]
    ### 用途:
    - 获取热门搜索信息
    ### 参数:
    - limit: 返回数量
    ### 返回:
    - 热门搜索信息
    ### 说明:
    - limit默认为10，上限为50

    # [English]
    ### Purpose:
    - Get hot search data
    ### Parameters:
    - limit: Return number
    ### Return:
    - Hot search data
    ### Note:
    - limit default is 10, maximum is 50

    # [示例/Example]
    limit = 10

    Args:
        limit (Any): 返回数量/Return number

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: Any,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取热门搜索信息/Get hot search data

     # [中文]
    ### 用途:
    - 获取热门搜索信息
    ### 参数:
    - limit: 返回数量
    ### 返回:
    - 热门搜索信息
    ### 说明:
    - limit默认为10，上限为50

    # [English]
    ### Purpose:
    - Get hot search data
    ### Parameters:
    - limit: Return number
    ### Return:
    - Hot search data
    ### Note:
    - limit default is 10, maximum is 50

    # [示例/Example]
    limit = 10

    Args:
        limit (Any): 返回数量/Return number

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
        )
    ).parsed
