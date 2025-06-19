from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: list[str],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tiktok/web/get_all_unique_id",
    }

    _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: list[str],
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取列表unique_id/Get list unique_id

     # [中文]
    ### 用途:
    - 获取列表unique_id
    ### 参数:
    - url: 用户主页链接 (最多支持20个链接)
    ### 返回:
    - unique_id

    # [English]
    ### Purpose:
    - Get list unique_id
    ### Parameters:
    - url: User homepage link (Support up to 20 links)
    ### Return:
    - unique_id

    # [示例/Example]
    url = [\"https://www.tiktok.com/@tiktok\"]

    Args:
        body (list[str]): 用户主页链接/User homepage link

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: list[str],
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取列表unique_id/Get list unique_id

     # [中文]
    ### 用途:
    - 获取列表unique_id
    ### 参数:
    - url: 用户主页链接 (最多支持20个链接)
    ### 返回:
    - unique_id

    # [English]
    ### Purpose:
    - Get list unique_id
    ### Parameters:
    - url: User homepage link (Support up to 20 links)
    ### Return:
    - unique_id

    # [示例/Example]
    url = [\"https://www.tiktok.com/@tiktok\"]

    Args:
        body (list[str]): 用户主页链接/User homepage link

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: list[str],
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取列表unique_id/Get list unique_id

     # [中文]
    ### 用途:
    - 获取列表unique_id
    ### 参数:
    - url: 用户主页链接 (最多支持20个链接)
    ### 返回:
    - unique_id

    # [English]
    ### Purpose:
    - Get list unique_id
    ### Parameters:
    - url: User homepage link (Support up to 20 links)
    ### Return:
    - unique_id

    # [示例/Example]
    url = [\"https://www.tiktok.com/@tiktok\"]

    Args:
        body (list[str]): 用户主页链接/User homepage link

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: list[str],
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取列表unique_id/Get list unique_id

     # [中文]
    ### 用途:
    - 获取列表unique_id
    ### 参数:
    - url: 用户主页链接 (最多支持20个链接)
    ### 返回:
    - unique_id

    # [English]
    ### Purpose:
    - Get list unique_id
    ### Parameters:
    - url: User homepage link (Support up to 20 links)
    ### Return:
    - unique_id

    # [示例/Example]
    url = [\"https://www.tiktok.com/@tiktok\"]

    Args:
        body (list[str]): 用户主页链接/User homepage link

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
