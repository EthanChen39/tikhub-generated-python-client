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
    endpoint: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["endpoint"] = endpoint

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tikhub/user/get_endpoint_info",
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
    endpoint: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取一个端点的信息/Get information of an endpoint

     # [中文]
    ### 用途:
    - 获取一个端点的信息
    ### 参数:
    - endpoint: 请求的端点
    ### 返回:
    - 端点信息

    # [English]
    ### Purpose:
    - Get information of an endpoint
    ### Parameters:
    - endpoint: Requested endpoint
    ### Return:
    - Endpoint information

    Args:
        endpoint (str): 请求的端点/Requested endpoint

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        endpoint=endpoint,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    endpoint: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取一个端点的信息/Get information of an endpoint

     # [中文]
    ### 用途:
    - 获取一个端点的信息
    ### 参数:
    - endpoint: 请求的端点
    ### 返回:
    - 端点信息

    # [English]
    ### Purpose:
    - Get information of an endpoint
    ### Parameters:
    - endpoint: Requested endpoint
    ### Return:
    - Endpoint information

    Args:
        endpoint (str): 请求的端点/Requested endpoint

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        endpoint=endpoint,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    endpoint: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取一个端点的信息/Get information of an endpoint

     # [中文]
    ### 用途:
    - 获取一个端点的信息
    ### 参数:
    - endpoint: 请求的端点
    ### 返回:
    - 端点信息

    # [English]
    ### Purpose:
    - Get information of an endpoint
    ### Parameters:
    - endpoint: Requested endpoint
    ### Return:
    - Endpoint information

    Args:
        endpoint (str): 请求的端点/Requested endpoint

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        endpoint=endpoint,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    endpoint: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取一个端点的信息/Get information of an endpoint

     # [中文]
    ### 用途:
    - 获取一个端点的信息
    ### 参数:
    - endpoint: 请求的端点
    ### 返回:
    - 端点信息

    # [English]
    ### Purpose:
    - Get information of an endpoint
    ### Parameters:
    - endpoint: Requested endpoint
    ### Return:
    - Endpoint information

    Args:
        endpoint (str): 请求的端点/Requested endpoint

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            endpoint=endpoint,
        )
    ).parsed
