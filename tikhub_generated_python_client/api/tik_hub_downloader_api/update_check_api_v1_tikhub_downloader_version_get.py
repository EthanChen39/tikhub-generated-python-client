from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_check_response import UpdateCheckResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tikhub/downloader/version",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UpdateCheckResponse]:
    if response.status_code == 200:
        response_200 = UpdateCheckResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UpdateCheckResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[UpdateCheckResponse]:
    """检查TikHub下载器的版本更新 / Check for TikHub Downloader version updates

     # [中文]

    ### 用途说明:

    - 检查TikHub下载器的版本更新。

    ### 参数说明:

    - 无参数。

    ### 返回结果:

    - `latest_version`: 最新版本号。
    - `update_date`: 更新日期。
    - `download_url`: 下载链接。
    - `upload_note`: 更新说明。

    # [English]

    ### Purpose:

    - Check for TikHub Downloader version updates.

    ### Parameter Description:

    - No parameters.

    ### Return Result:

    - `latest_version`: Latest version number.
    - `update_date`: Update date.
    - `download_url`: Download link.
    - `upload_note`: Update note.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateCheckResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[UpdateCheckResponse]:
    """检查TikHub下载器的版本更新 / Check for TikHub Downloader version updates

     # [中文]

    ### 用途说明:

    - 检查TikHub下载器的版本更新。

    ### 参数说明:

    - 无参数。

    ### 返回结果:

    - `latest_version`: 最新版本号。
    - `update_date`: 更新日期。
    - `download_url`: 下载链接。
    - `upload_note`: 更新说明。

    # [English]

    ### Purpose:

    - Check for TikHub Downloader version updates.

    ### Parameter Description:

    - No parameters.

    ### Return Result:

    - `latest_version`: Latest version number.
    - `update_date`: Update date.
    - `download_url`: Download link.
    - `upload_note`: Update note.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateCheckResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[UpdateCheckResponse]:
    """检查TikHub下载器的版本更新 / Check for TikHub Downloader version updates

     # [中文]

    ### 用途说明:

    - 检查TikHub下载器的版本更新。

    ### 参数说明:

    - 无参数。

    ### 返回结果:

    - `latest_version`: 最新版本号。
    - `update_date`: 更新日期。
    - `download_url`: 下载链接。
    - `upload_note`: 更新说明。

    # [English]

    ### Purpose:

    - Check for TikHub Downloader version updates.

    ### Parameter Description:

    - No parameters.

    ### Return Result:

    - `latest_version`: Latest version number.
    - `update_date`: Update date.
    - `download_url`: Download link.
    - `upload_note`: Update note.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateCheckResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[UpdateCheckResponse]:
    """检查TikHub下载器的版本更新 / Check for TikHub Downloader version updates

     # [中文]

    ### 用途说明:

    - 检查TikHub下载器的版本更新。

    ### 参数说明:

    - 无参数。

    ### 返回结果:

    - `latest_version`: 最新版本号。
    - `update_date`: 更新日期。
    - `download_url`: 下载链接。
    - `upload_note`: 更新说明。

    # [English]

    ### Purpose:

    - Check for TikHub Downloader version updates.

    ### Parameter Description:

    - No parameters.

    ### Return Result:

    - `latest_version`: Latest version number.
    - `update_date`: Update date.
    - `download_url`: Download link.
    - `upload_note`: Update note.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateCheckResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
