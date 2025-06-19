from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    *,
    music_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["music_id"] = music_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/net_ease_cloud_music/app/fetch_one_music_lyric",
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
    music_id: str,
) -> Response[Union[Any, HTTPValidationError]]:
    r"""获取单一歌曲歌词/Fetch one music lyric

     # [中文]
    ### 用途:
    - 获取单个音乐歌词。
    ### 参数:
    - music_id: 音乐ID
    ### 返回:
    - 音乐歌词

    # [English]
    ### Purpose:
    - Fetch single music lyric.
    ### Parameters:
    - music_id: Music ID
    ### Returns:
    - Music lyric

    # [示例/Example]
    music_id = \"2135155051\"

    Args:
        music_id (str): 歌曲ID/Music ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        music_id=music_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    music_id: str,
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""获取单一歌曲歌词/Fetch one music lyric

     # [中文]
    ### 用途:
    - 获取单个音乐歌词。
    ### 参数:
    - music_id: 音乐ID
    ### 返回:
    - 音乐歌词

    # [English]
    ### Purpose:
    - Fetch single music lyric.
    ### Parameters:
    - music_id: Music ID
    ### Returns:
    - Music lyric

    # [示例/Example]
    music_id = \"2135155051\"

    Args:
        music_id (str): 歌曲ID/Music ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        music_id=music_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    music_id: str,
) -> Response[Union[Any, HTTPValidationError]]:
    r"""获取单一歌曲歌词/Fetch one music lyric

     # [中文]
    ### 用途:
    - 获取单个音乐歌词。
    ### 参数:
    - music_id: 音乐ID
    ### 返回:
    - 音乐歌词

    # [English]
    ### Purpose:
    - Fetch single music lyric.
    ### Parameters:
    - music_id: Music ID
    ### Returns:
    - Music lyric

    # [示例/Example]
    music_id = \"2135155051\"

    Args:
        music_id (str): 歌曲ID/Music ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        music_id=music_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    music_id: str,
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""获取单一歌曲歌词/Fetch one music lyric

     # [中文]
    ### 用途:
    - 获取单个音乐歌词。
    ### 参数:
    - music_id: 音乐ID
    ### 返回:
    - 音乐歌词

    # [English]
    ### Purpose:
    - Fetch single music lyric.
    ### Parameters:
    - music_id: Music ID
    ### Returns:
    - Music lyric

    # [示例/Example]
    music_id = \"2135155051\"

    Args:
        music_id (str): 歌曲ID/Music ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            music_id=music_id,
        )
    ).parsed
