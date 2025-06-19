from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tikhub/downloader/redirect_download",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 302:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    """重定向到最新版本的下载链接 / Redirect to the latest version download link

     # [中文]

    ### 用途说明:

    - 该接口用于检测客户端操作系统，并重定向到相应的 GitHub Release 直链，方便用户请求后直接开始下载最新版本的文件。

    ### 参数说明:

    - 无参数。

    ### 返回结果:

    - Windows 用户：重定向到 `.exe` 下载地址。
    - Mac 用户：重定向到 `.zip` 下载地址。
    - 其他用户：重定向到 GitHub Release 页面。

    # [English]

    ### Purpose:

    - This endpoint detects the client operating system and redirects to the corresponding GitHub
    Release direct link, allowing users to start downloading the latest version file immediately.

    ### Parameter Description:

    - No parameters.

    ### Return Result:

    - Windows users: Redirect to `.exe` download URL.
    - Mac users: Redirect to `.zip` download URL.
    - Other users: Redirect to the GitHub Release page.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    """重定向到最新版本的下载链接 / Redirect to the latest version download link

     # [中文]

    ### 用途说明:

    - 该接口用于检测客户端操作系统，并重定向到相应的 GitHub Release 直链，方便用户请求后直接开始下载最新版本的文件。

    ### 参数说明:

    - 无参数。

    ### 返回结果:

    - Windows 用户：重定向到 `.exe` 下载地址。
    - Mac 用户：重定向到 `.zip` 下载地址。
    - 其他用户：重定向到 GitHub Release 页面。

    # [English]

    ### Purpose:

    - This endpoint detects the client operating system and redirects to the corresponding GitHub
    Release direct link, allowing users to start downloading the latest version file immediately.

    ### Parameter Description:

    - No parameters.

    ### Return Result:

    - Windows users: Redirect to `.exe` download URL.
    - Mac users: Redirect to `.zip` download URL.
    - Other users: Redirect to the GitHub Release page.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
