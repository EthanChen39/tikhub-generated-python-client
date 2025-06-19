from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    *,
    artist_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["artist_id"] = artist_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/net_ease_cloud_music/app/fetch_artist_detail",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    artist_id: str,
) -> Response[Union[Any, HTTPValidationError]]:
    r"""获取歌手信息/Fetch artist detail

     # [中文]
    ### 用途:
    - 获取歌手信息。
    ### 参数:
    - artist_id: 歌手ID。
    ### 返回:
    - 歌手信息

    # [English]
    ### Purpose:
    - Fetch artist detail.
    ### Parameters:
    - artist_id: Artist ID.
    ### Returns:
    - Artist detail

    # [示例/Example]
    artist_id = \"12213291\"

    Args:
        artist_id (str): 歌手ID/Artist ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        artist_id=artist_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    artist_id: str,
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""获取歌手信息/Fetch artist detail

     # [中文]
    ### 用途:
    - 获取歌手信息。
    ### 参数:
    - artist_id: 歌手ID。
    ### 返回:
    - 歌手信息

    # [English]
    ### Purpose:
    - Fetch artist detail.
    ### Parameters:
    - artist_id: Artist ID.
    ### Returns:
    - Artist detail

    # [示例/Example]
    artist_id = \"12213291\"

    Args:
        artist_id (str): 歌手ID/Artist ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        artist_id=artist_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    artist_id: str,
) -> Response[Union[Any, HTTPValidationError]]:
    r"""获取歌手信息/Fetch artist detail

     # [中文]
    ### 用途:
    - 获取歌手信息。
    ### 参数:
    - artist_id: 歌手ID。
    ### 返回:
    - 歌手信息

    # [English]
    ### Purpose:
    - Fetch artist detail.
    ### Parameters:
    - artist_id: Artist ID.
    ### Returns:
    - Artist detail

    # [示例/Example]
    artist_id = \"12213291\"

    Args:
        artist_id (str): 歌手ID/Artist ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        artist_id=artist_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    artist_id: str,
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""获取歌手信息/Fetch artist detail

     # [中文]
    ### 用途:
    - 获取歌手信息。
    ### 参数:
    - artist_id: 歌手ID。
    ### 返回:
    - 歌手信息

    # [English]
    ### Purpose:
    - Fetch artist detail.
    ### Parameters:
    - artist_id: Artist ID.
    ### Returns:
    - Artist detail

    # [示例/Example]
    artist_id = \"12213291\"

    Args:
        artist_id (str): 歌手ID/Artist ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            artist_id=artist_id,
        )
    ).parsed
