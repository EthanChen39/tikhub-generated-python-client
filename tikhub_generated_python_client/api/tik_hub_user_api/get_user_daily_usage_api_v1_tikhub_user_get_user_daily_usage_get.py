from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tikhub/user/get_user_daily_usage",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ResponseModel]:
    if response.status_code == 200:
        response_200 = ResponseModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ResponseModel]:
    """获取用户每日使用情况/Get user daily usage

     # [中文]
    ### 用途:
    - 请求头中携带API Key请求此端点可以查询当前账户每日使用情况。
    ### 参数:
    - 请求头：{'Authorization': 'Bearer API Key'}
    ### 返回:
    - 用户每日使用情况

    # [English]
    ### Purpose:
    - Request this endpoint with API Key in the header to query the current account daily usage.
    ### Parameters:
    - Headers: {'Authorization': 'Bearer API Key'}
    ### Return:
    - User daily usage

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseModel]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[ResponseModel]:
    """获取用户每日使用情况/Get user daily usage

     # [中文]
    ### 用途:
    - 请求头中携带API Key请求此端点可以查询当前账户每日使用情况。
    ### 参数:
    - 请求头：{'Authorization': 'Bearer API Key'}
    ### 返回:
    - 用户每日使用情况

    # [English]
    ### Purpose:
    - Request this endpoint with API Key in the header to query the current account daily usage.
    ### Parameters:
    - Headers: {'Authorization': 'Bearer API Key'}
    ### Return:
    - User daily usage

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseModel
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ResponseModel]:
    """获取用户每日使用情况/Get user daily usage

     # [中文]
    ### 用途:
    - 请求头中携带API Key请求此端点可以查询当前账户每日使用情况。
    ### 参数:
    - 请求头：{'Authorization': 'Bearer API Key'}
    ### 返回:
    - 用户每日使用情况

    # [English]
    ### Purpose:
    - Request this endpoint with API Key in the header to query the current account daily usage.
    ### Parameters:
    - Headers: {'Authorization': 'Bearer API Key'}
    ### Return:
    - User daily usage

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseModel]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[ResponseModel]:
    """获取用户每日使用情况/Get user daily usage

     # [中文]
    ### 用途:
    - 请求头中携带API Key请求此端点可以查询当前账户每日使用情况。
    ### 参数:
    - 请求头：{'Authorization': 'Bearer API Key'}
    ### 返回:
    - 用户每日使用情况

    # [English]
    ### Purpose:
    - Request this endpoint with API Key in the header to query the current account daily usage.
    ### Parameters:
    - Headers: {'Authorization': 'Bearer API Key'}
    ### Return:
    - User daily usage

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
