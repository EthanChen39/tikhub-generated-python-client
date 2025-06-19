from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.health_check_response import HealthCheckResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/health/check",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[HealthCheckResponse]:
    if response.status_code == 200:
        response_200 = HealthCheckResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[HealthCheckResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[HealthCheckResponse]:
    """检查服务器是否正确响应请求 / Check if the server responds to requests correctly

     # [中文]

    ### 用途说明:

    - 检查服务器是否正确响应请求。

    ### 参数说明:

    - 无参数。

    ### 返回结果:

    - `status`: 服务器状态，正常为 `ok`。

    # [English]

    ### Purpose:

    - Check if the server responds to requests correctly.

    ### Parameter Description:

    - No parameters.

    ### Return Result:

    - `status`: Server status, normal is `ok`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HealthCheckResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[HealthCheckResponse]:
    """检查服务器是否正确响应请求 / Check if the server responds to requests correctly

     # [中文]

    ### 用途说明:

    - 检查服务器是否正确响应请求。

    ### 参数说明:

    - 无参数。

    ### 返回结果:

    - `status`: 服务器状态，正常为 `ok`。

    # [English]

    ### Purpose:

    - Check if the server responds to requests correctly.

    ### Parameter Description:

    - No parameters.

    ### Return Result:

    - `status`: Server status, normal is `ok`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HealthCheckResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[HealthCheckResponse]:
    """检查服务器是否正确响应请求 / Check if the server responds to requests correctly

     # [中文]

    ### 用途说明:

    - 检查服务器是否正确响应请求。

    ### 参数说明:

    - 无参数。

    ### 返回结果:

    - `status`: 服务器状态，正常为 `ok`。

    # [English]

    ### Purpose:

    - Check if the server responds to requests correctly.

    ### Parameter Description:

    - No parameters.

    ### Return Result:

    - `status`: Server status, normal is `ok`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HealthCheckResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[HealthCheckResponse]:
    """检查服务器是否正确响应请求 / Check if the server responds to requests correctly

     # [中文]

    ### 用途说明:

    - 检查服务器是否正确响应请求。

    ### 参数说明:

    - 无参数。

    ### 返回结果:

    - `status`: 服务器状态，正常为 `ok`。

    # [English]

    ### Purpose:

    - Check if the server responds to requests correctly.

    ### Parameter Description:

    - No parameters.

    ### Return Result:

    - `status`: Server status, normal is `ok`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HealthCheckResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
