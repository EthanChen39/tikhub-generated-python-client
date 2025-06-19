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
    user_agent: Union[Unset, str] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["user_agent"] = user_agent

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/web/generate_ttwid",
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
    user_agent: Union[Unset, str] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """生成ttwid/Generate ttwid

     # [中文]
    ### 用途:
    - 生成ttwid
    ### 返回:
    - ttwid

    # [English]
    ### Purpose:
    - Generate ttwid
    ### Return:
    - ttwid

    Args:
        user_agent (Union[Unset, str]):  Default: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64;
            rv:125.0) Gecko/20100101 Firefox/125.0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        user_agent=user_agent,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_agent: Union[Unset, str] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """生成ttwid/Generate ttwid

     # [中文]
    ### 用途:
    - 生成ttwid
    ### 返回:
    - ttwid

    # [English]
    ### Purpose:
    - Generate ttwid
    ### Return:
    - ttwid

    Args:
        user_agent (Union[Unset, str]):  Default: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64;
            rv:125.0) Gecko/20100101 Firefox/125.0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        user_agent=user_agent,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_agent: Union[Unset, str] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """生成ttwid/Generate ttwid

     # [中文]
    ### 用途:
    - 生成ttwid
    ### 返回:
    - ttwid

    # [English]
    ### Purpose:
    - Generate ttwid
    ### Return:
    - ttwid

    Args:
        user_agent (Union[Unset, str]):  Default: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64;
            rv:125.0) Gecko/20100101 Firefox/125.0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        user_agent=user_agent,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_agent: Union[Unset, str] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """生成ttwid/Generate ttwid

     # [中文]
    ### 用途:
    - 生成ttwid
    ### 返回:
    - ttwid

    # [English]
    ### Purpose:
    - Generate ttwid
    ### Return:
    - ttwid

    Args:
        user_agent (Union[Unset, str]):  Default: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64;
            rv:125.0) Gecko/20100101 Firefox/125.0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_agent=user_agent,
        )
    ).parsed
