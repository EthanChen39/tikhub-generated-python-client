from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    music_id: str,
    br: Union[Unset, str] = "192000",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["music_id"] = music_id

    params["br"] = br

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/net_ease_cloud_music/app/fetch_one_music_url_v1",
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
    br: Union[Unset, str] = "192000",
) -> Response[Union[Any, HTTPValidationError]]:
    r"""获取单一歌曲播放地址V1（只能返回MP3格式，支持参数较少）/Fetch one music URL V1 (only MP3 format is supported, with fewer
    parameters)

     # [中文]
    ### 用途:
    - 获取单个音乐播放地址，此接口只能返回MP3格式的音频文件链接。
    ### 参数:
    - music_id: 音乐ID
    - br: 音质码率，分四个等级，128000,192000,320000,999000
    ### 返回:
    - 音乐播放地址

    # [English]
    ### Purpose:
    - Fetch single music URL, this interface can only return MP3 format audio file link.
    ### Parameters:
    - music_id: Music ID
    - br: Bitrate, divided into four levels, 128000,192000,320000,999000
    ### Returns:
    - Music URL

    # [示例/Example]
    music_id = \"2135155051\"
    br = \"192000\"

    Args:
        music_id (str): 歌曲ID/Music ID
        br (Union[Unset, str]): 音质码率/Bitrate Default: '192000'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        music_id=music_id,
        br=br,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    music_id: str,
    br: Union[Unset, str] = "192000",
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""获取单一歌曲播放地址V1（只能返回MP3格式，支持参数较少）/Fetch one music URL V1 (only MP3 format is supported, with fewer
    parameters)

     # [中文]
    ### 用途:
    - 获取单个音乐播放地址，此接口只能返回MP3格式的音频文件链接。
    ### 参数:
    - music_id: 音乐ID
    - br: 音质码率，分四个等级，128000,192000,320000,999000
    ### 返回:
    - 音乐播放地址

    # [English]
    ### Purpose:
    - Fetch single music URL, this interface can only return MP3 format audio file link.
    ### Parameters:
    - music_id: Music ID
    - br: Bitrate, divided into four levels, 128000,192000,320000,999000
    ### Returns:
    - Music URL

    # [示例/Example]
    music_id = \"2135155051\"
    br = \"192000\"

    Args:
        music_id (str): 歌曲ID/Music ID
        br (Union[Unset, str]): 音质码率/Bitrate Default: '192000'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        music_id=music_id,
        br=br,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    music_id: str,
    br: Union[Unset, str] = "192000",
) -> Response[Union[Any, HTTPValidationError]]:
    r"""获取单一歌曲播放地址V1（只能返回MP3格式，支持参数较少）/Fetch one music URL V1 (only MP3 format is supported, with fewer
    parameters)

     # [中文]
    ### 用途:
    - 获取单个音乐播放地址，此接口只能返回MP3格式的音频文件链接。
    ### 参数:
    - music_id: 音乐ID
    - br: 音质码率，分四个等级，128000,192000,320000,999000
    ### 返回:
    - 音乐播放地址

    # [English]
    ### Purpose:
    - Fetch single music URL, this interface can only return MP3 format audio file link.
    ### Parameters:
    - music_id: Music ID
    - br: Bitrate, divided into four levels, 128000,192000,320000,999000
    ### Returns:
    - Music URL

    # [示例/Example]
    music_id = \"2135155051\"
    br = \"192000\"

    Args:
        music_id (str): 歌曲ID/Music ID
        br (Union[Unset, str]): 音质码率/Bitrate Default: '192000'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        music_id=music_id,
        br=br,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    music_id: str,
    br: Union[Unset, str] = "192000",
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""获取单一歌曲播放地址V1（只能返回MP3格式，支持参数较少）/Fetch one music URL V1 (only MP3 format is supported, with fewer
    parameters)

     # [中文]
    ### 用途:
    - 获取单个音乐播放地址，此接口只能返回MP3格式的音频文件链接。
    ### 参数:
    - music_id: 音乐ID
    - br: 音质码率，分四个等级，128000,192000,320000,999000
    ### 返回:
    - 音乐播放地址

    # [English]
    ### Purpose:
    - Fetch single music URL, this interface can only return MP3 format audio file link.
    ### Parameters:
    - music_id: Music ID
    - br: Bitrate, divided into four levels, 128000,192000,320000,999000
    ### Returns:
    - Music URL

    # [示例/Example]
    music_id = \"2135155051\"
    br = \"192000\"

    Args:
        music_id (str): 歌曲ID/Music ID
        br (Union[Unset, str]): 音质码率/Bitrate Default: '192000'.

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
            br=br,
        )
    ).parsed
