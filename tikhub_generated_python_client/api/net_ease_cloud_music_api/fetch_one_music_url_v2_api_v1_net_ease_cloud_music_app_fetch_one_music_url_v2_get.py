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
    level: Union[Unset, str] = "exhigh",
    encode_type: Union[Unset, str] = "mp3",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["music_id"] = music_id

    params["level"] = level

    params["encodeType"] = encode_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/net_ease_cloud_music/app/fetch_one_music_url_v2",
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
    level: Union[Unset, str] = "exhigh",
    encode_type: Union[Unset, str] = "mp3",
) -> Response[Union[Any, HTTPValidationError]]:
    r"""获取单一歌曲播放地址V2（支持更多参数）/Fetch one music URL V2 (support more parameters)

     # [中文]
    ### 用途:
    - 获取单个音乐播放地址，此接口支持更多参数。
    ### 参数:
    - music_id: 音乐ID
    - level: 音质等级，分五个等级，标准，较高，极高，无损，hires，后两个等级不一定有支持的音源。
        - 标准：standard
        - 较高：higher
        - 极高：exhigh
        - 无损：lossLess
        - hires：hires
    - encodeType: 编码类型，分六种类型。
        - aac：aac
        - mp3：mp3（默认）
        - flac：flac
        - alac：alac
        - ape：ape
        - wav：wav
    ### 返回:
    - 音乐播放地址

    # [English]
    ### Purpose:
    - Fetch single music URL, this interface supports more parameters.
    ### Parameters:
    - music_id: Music ID
    - level: Quality level, divided into five levels, standard, higher, exhigh, lossLess, hires, the
    last two levels may not have supported audio sources.
        - standard
        - higher
        - exhigh
        - lossLess
        - hires
    - encodeType: Encoding type, divided into six types.
        - aac
        - mp3 (default)
        - flac
        - alac
        - ape
        - wav
    ### Returns:
    - Music URL

    # [示例/Example]
    music_id = \"2135155051\"
    level = \"exhigh\"
    encodeType = \"mp3\"

    Args:
        music_id (str): 歌曲ID/Music ID
        level (Union[Unset, str]): 音质等级/Quality level Default: 'exhigh'.
        encode_type (Union[Unset, str]): 编码类型/Encoding type Default: 'mp3'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        music_id=music_id,
        level=level,
        encode_type=encode_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    music_id: str,
    level: Union[Unset, str] = "exhigh",
    encode_type: Union[Unset, str] = "mp3",
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""获取单一歌曲播放地址V2（支持更多参数）/Fetch one music URL V2 (support more parameters)

     # [中文]
    ### 用途:
    - 获取单个音乐播放地址，此接口支持更多参数。
    ### 参数:
    - music_id: 音乐ID
    - level: 音质等级，分五个等级，标准，较高，极高，无损，hires，后两个等级不一定有支持的音源。
        - 标准：standard
        - 较高：higher
        - 极高：exhigh
        - 无损：lossLess
        - hires：hires
    - encodeType: 编码类型，分六种类型。
        - aac：aac
        - mp3：mp3（默认）
        - flac：flac
        - alac：alac
        - ape：ape
        - wav：wav
    ### 返回:
    - 音乐播放地址

    # [English]
    ### Purpose:
    - Fetch single music URL, this interface supports more parameters.
    ### Parameters:
    - music_id: Music ID
    - level: Quality level, divided into five levels, standard, higher, exhigh, lossLess, hires, the
    last two levels may not have supported audio sources.
        - standard
        - higher
        - exhigh
        - lossLess
        - hires
    - encodeType: Encoding type, divided into six types.
        - aac
        - mp3 (default)
        - flac
        - alac
        - ape
        - wav
    ### Returns:
    - Music URL

    # [示例/Example]
    music_id = \"2135155051\"
    level = \"exhigh\"
    encodeType = \"mp3\"

    Args:
        music_id (str): 歌曲ID/Music ID
        level (Union[Unset, str]): 音质等级/Quality level Default: 'exhigh'.
        encode_type (Union[Unset, str]): 编码类型/Encoding type Default: 'mp3'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        music_id=music_id,
        level=level,
        encode_type=encode_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    music_id: str,
    level: Union[Unset, str] = "exhigh",
    encode_type: Union[Unset, str] = "mp3",
) -> Response[Union[Any, HTTPValidationError]]:
    r"""获取单一歌曲播放地址V2（支持更多参数）/Fetch one music URL V2 (support more parameters)

     # [中文]
    ### 用途:
    - 获取单个音乐播放地址，此接口支持更多参数。
    ### 参数:
    - music_id: 音乐ID
    - level: 音质等级，分五个等级，标准，较高，极高，无损，hires，后两个等级不一定有支持的音源。
        - 标准：standard
        - 较高：higher
        - 极高：exhigh
        - 无损：lossLess
        - hires：hires
    - encodeType: 编码类型，分六种类型。
        - aac：aac
        - mp3：mp3（默认）
        - flac：flac
        - alac：alac
        - ape：ape
        - wav：wav
    ### 返回:
    - 音乐播放地址

    # [English]
    ### Purpose:
    - Fetch single music URL, this interface supports more parameters.
    ### Parameters:
    - music_id: Music ID
    - level: Quality level, divided into five levels, standard, higher, exhigh, lossLess, hires, the
    last two levels may not have supported audio sources.
        - standard
        - higher
        - exhigh
        - lossLess
        - hires
    - encodeType: Encoding type, divided into six types.
        - aac
        - mp3 (default)
        - flac
        - alac
        - ape
        - wav
    ### Returns:
    - Music URL

    # [示例/Example]
    music_id = \"2135155051\"
    level = \"exhigh\"
    encodeType = \"mp3\"

    Args:
        music_id (str): 歌曲ID/Music ID
        level (Union[Unset, str]): 音质等级/Quality level Default: 'exhigh'.
        encode_type (Union[Unset, str]): 编码类型/Encoding type Default: 'mp3'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        music_id=music_id,
        level=level,
        encode_type=encode_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    music_id: str,
    level: Union[Unset, str] = "exhigh",
    encode_type: Union[Unset, str] = "mp3",
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""获取单一歌曲播放地址V2（支持更多参数）/Fetch one music URL V2 (support more parameters)

     # [中文]
    ### 用途:
    - 获取单个音乐播放地址，此接口支持更多参数。
    ### 参数:
    - music_id: 音乐ID
    - level: 音质等级，分五个等级，标准，较高，极高，无损，hires，后两个等级不一定有支持的音源。
        - 标准：standard
        - 较高：higher
        - 极高：exhigh
        - 无损：lossLess
        - hires：hires
    - encodeType: 编码类型，分六种类型。
        - aac：aac
        - mp3：mp3（默认）
        - flac：flac
        - alac：alac
        - ape：ape
        - wav：wav
    ### 返回:
    - 音乐播放地址

    # [English]
    ### Purpose:
    - Fetch single music URL, this interface supports more parameters.
    ### Parameters:
    - music_id: Music ID
    - level: Quality level, divided into five levels, standard, higher, exhigh, lossLess, hires, the
    last two levels may not have supported audio sources.
        - standard
        - higher
        - exhigh
        - lossLess
        - hires
    - encodeType: Encoding type, divided into six types.
        - aac
        - mp3 (default)
        - flac
        - alac
        - ape
        - wav
    ### Returns:
    - Music URL

    # [示例/Example]
    music_id = \"2135155051\"
    level = \"exhigh\"
    encodeType = \"mp3\"

    Args:
        music_id (str): 歌曲ID/Music ID
        level (Union[Unset, str]): 音质等级/Quality level Default: 'exhigh'.
        encode_type (Union[Unset, str]): 编码类型/Encoding type Default: 'mp3'.

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
            level=level,
            encode_type=encode_type,
        )
    ).parsed
