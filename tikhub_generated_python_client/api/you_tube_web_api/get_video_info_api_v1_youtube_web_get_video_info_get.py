from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...models.url_access_mode import UrlAccessMode
from ...models.videos_audios_mode import VideosAudiosMode
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    video_id: str,
    url_access: Union[Unset, UrlAccessMode] = UrlAccessMode.NORMAL,
    lang: Union[Unset, str] = "en-US",
    videos: Union[Unset, VideosAudiosMode] = VideosAudiosMode.AUTO,
    audios: Union[Unset, VideosAudiosMode] = VideosAudiosMode.AUTO,
    subtitles: Union[Unset, bool] = True,
    related: Union[Unset, bool] = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["video_id"] = video_id

    json_url_access: Union[Unset, str] = UNSET
    if not isinstance(url_access, Unset):
        json_url_access = url_access.value

    params["url_access"] = json_url_access

    params["lang"] = lang

    json_videos: Union[Unset, str] = UNSET
    if not isinstance(videos, Unset):
        json_videos = videos.value

    params["videos"] = json_videos

    json_audios: Union[Unset, str] = UNSET
    if not isinstance(audios, Unset):
        json_audios = audios.value

    params["audios"] = json_audios

    params["subtitles"] = subtitles

    params["related"] = related

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/youtube/web/get_video_info",
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
    video_id: str,
    url_access: Union[Unset, UrlAccessMode] = UrlAccessMode.NORMAL,
    lang: Union[Unset, str] = "en-US",
    videos: Union[Unset, VideosAudiosMode] = VideosAudiosMode.AUTO,
    audios: Union[Unset, VideosAudiosMode] = VideosAudiosMode.AUTO,
    subtitles: Union[Unset, bool] = True,
    related: Union[Unset, bool] = True,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频信息/Get video information

     # [中文]
    ### 用途:
    - 获取视频元数据及下载信息
    ### 详细参数:
    - url_access:
        - normal: 包含音视频直链
        - blocked: 不包含直链
    - videos/audios:
        - auto: 根据url_access自动选择（normal→true，blocked→false）
        - true: 返回简化格式信息
        - raw: 返回原始格式信息
        - false: 不包含该类型数据
    ### 返回:
    - 视频元数据 + 请求参数对应的资源信息

    # [English]
    ### Purpose:
    - Get video metadata and download information
    ### Parameters Detail:
    - url_access:
        - normal: Include direct URLs
        - blocked: Exclude direct URLs
    - videos/audios:
        - auto: Auto-select based on url_access (normal→true，blocked→false)
        - true: Simplified format
        - raw: Original format
        - false: Exclude this type
    ### Returns:
    - Video metadata + requested resource information

    # [示例/Example]
    video_id = \"LuIL5JATZsc\"
    url_access = \"blocked\"
    lang = \"zh-CN\"

    video_id = \"LuIL5JATZsc\"
    url_access = \"normal\"
    lang = \"en-US\"
    videos = \"auto\"
    audios = \"auto\"
    subtitles = True

    Args:
        video_id (str): 视频ID/Video ID
        url_access (Union[Unset, UrlAccessMode]):  Default: UrlAccessMode.NORMAL.
        lang (Union[Unset, str]): 语言代码（IETF标签），默认en-US / Language code Default: 'en-US'.
        videos (Union[Unset, VideosAudiosMode]):  Default: VideosAudiosMode.AUTO.
        audios (Union[Unset, VideosAudiosMode]):  Default: VideosAudiosMode.AUTO.
        subtitles (Union[Unset, bool]): 是否获取字幕 / Include subtitles Default: True.
        related (Union[Unset, bool]): 是否获取相关视频 / Include related content Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        video_id=video_id,
        url_access=url_access,
        lang=lang,
        videos=videos,
        audios=audios,
        subtitles=subtitles,
        related=related,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    video_id: str,
    url_access: Union[Unset, UrlAccessMode] = UrlAccessMode.NORMAL,
    lang: Union[Unset, str] = "en-US",
    videos: Union[Unset, VideosAudiosMode] = VideosAudiosMode.AUTO,
    audios: Union[Unset, VideosAudiosMode] = VideosAudiosMode.AUTO,
    subtitles: Union[Unset, bool] = True,
    related: Union[Unset, bool] = True,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频信息/Get video information

     # [中文]
    ### 用途:
    - 获取视频元数据及下载信息
    ### 详细参数:
    - url_access:
        - normal: 包含音视频直链
        - blocked: 不包含直链
    - videos/audios:
        - auto: 根据url_access自动选择（normal→true，blocked→false）
        - true: 返回简化格式信息
        - raw: 返回原始格式信息
        - false: 不包含该类型数据
    ### 返回:
    - 视频元数据 + 请求参数对应的资源信息

    # [English]
    ### Purpose:
    - Get video metadata and download information
    ### Parameters Detail:
    - url_access:
        - normal: Include direct URLs
        - blocked: Exclude direct URLs
    - videos/audios:
        - auto: Auto-select based on url_access (normal→true，blocked→false)
        - true: Simplified format
        - raw: Original format
        - false: Exclude this type
    ### Returns:
    - Video metadata + requested resource information

    # [示例/Example]
    video_id = \"LuIL5JATZsc\"
    url_access = \"blocked\"
    lang = \"zh-CN\"

    video_id = \"LuIL5JATZsc\"
    url_access = \"normal\"
    lang = \"en-US\"
    videos = \"auto\"
    audios = \"auto\"
    subtitles = True

    Args:
        video_id (str): 视频ID/Video ID
        url_access (Union[Unset, UrlAccessMode]):  Default: UrlAccessMode.NORMAL.
        lang (Union[Unset, str]): 语言代码（IETF标签），默认en-US / Language code Default: 'en-US'.
        videos (Union[Unset, VideosAudiosMode]):  Default: VideosAudiosMode.AUTO.
        audios (Union[Unset, VideosAudiosMode]):  Default: VideosAudiosMode.AUTO.
        subtitles (Union[Unset, bool]): 是否获取字幕 / Include subtitles Default: True.
        related (Union[Unset, bool]): 是否获取相关视频 / Include related content Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        video_id=video_id,
        url_access=url_access,
        lang=lang,
        videos=videos,
        audios=audios,
        subtitles=subtitles,
        related=related,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    video_id: str,
    url_access: Union[Unset, UrlAccessMode] = UrlAccessMode.NORMAL,
    lang: Union[Unset, str] = "en-US",
    videos: Union[Unset, VideosAudiosMode] = VideosAudiosMode.AUTO,
    audios: Union[Unset, VideosAudiosMode] = VideosAudiosMode.AUTO,
    subtitles: Union[Unset, bool] = True,
    related: Union[Unset, bool] = True,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频信息/Get video information

     # [中文]
    ### 用途:
    - 获取视频元数据及下载信息
    ### 详细参数:
    - url_access:
        - normal: 包含音视频直链
        - blocked: 不包含直链
    - videos/audios:
        - auto: 根据url_access自动选择（normal→true，blocked→false）
        - true: 返回简化格式信息
        - raw: 返回原始格式信息
        - false: 不包含该类型数据
    ### 返回:
    - 视频元数据 + 请求参数对应的资源信息

    # [English]
    ### Purpose:
    - Get video metadata and download information
    ### Parameters Detail:
    - url_access:
        - normal: Include direct URLs
        - blocked: Exclude direct URLs
    - videos/audios:
        - auto: Auto-select based on url_access (normal→true，blocked→false)
        - true: Simplified format
        - raw: Original format
        - false: Exclude this type
    ### Returns:
    - Video metadata + requested resource information

    # [示例/Example]
    video_id = \"LuIL5JATZsc\"
    url_access = \"blocked\"
    lang = \"zh-CN\"

    video_id = \"LuIL5JATZsc\"
    url_access = \"normal\"
    lang = \"en-US\"
    videos = \"auto\"
    audios = \"auto\"
    subtitles = True

    Args:
        video_id (str): 视频ID/Video ID
        url_access (Union[Unset, UrlAccessMode]):  Default: UrlAccessMode.NORMAL.
        lang (Union[Unset, str]): 语言代码（IETF标签），默认en-US / Language code Default: 'en-US'.
        videos (Union[Unset, VideosAudiosMode]):  Default: VideosAudiosMode.AUTO.
        audios (Union[Unset, VideosAudiosMode]):  Default: VideosAudiosMode.AUTO.
        subtitles (Union[Unset, bool]): 是否获取字幕 / Include subtitles Default: True.
        related (Union[Unset, bool]): 是否获取相关视频 / Include related content Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        video_id=video_id,
        url_access=url_access,
        lang=lang,
        videos=videos,
        audios=audios,
        subtitles=subtitles,
        related=related,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    video_id: str,
    url_access: Union[Unset, UrlAccessMode] = UrlAccessMode.NORMAL,
    lang: Union[Unset, str] = "en-US",
    videos: Union[Unset, VideosAudiosMode] = VideosAudiosMode.AUTO,
    audios: Union[Unset, VideosAudiosMode] = VideosAudiosMode.AUTO,
    subtitles: Union[Unset, bool] = True,
    related: Union[Unset, bool] = True,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频信息/Get video information

     # [中文]
    ### 用途:
    - 获取视频元数据及下载信息
    ### 详细参数:
    - url_access:
        - normal: 包含音视频直链
        - blocked: 不包含直链
    - videos/audios:
        - auto: 根据url_access自动选择（normal→true，blocked→false）
        - true: 返回简化格式信息
        - raw: 返回原始格式信息
        - false: 不包含该类型数据
    ### 返回:
    - 视频元数据 + 请求参数对应的资源信息

    # [English]
    ### Purpose:
    - Get video metadata and download information
    ### Parameters Detail:
    - url_access:
        - normal: Include direct URLs
        - blocked: Exclude direct URLs
    - videos/audios:
        - auto: Auto-select based on url_access (normal→true，blocked→false)
        - true: Simplified format
        - raw: Original format
        - false: Exclude this type
    ### Returns:
    - Video metadata + requested resource information

    # [示例/Example]
    video_id = \"LuIL5JATZsc\"
    url_access = \"blocked\"
    lang = \"zh-CN\"

    video_id = \"LuIL5JATZsc\"
    url_access = \"normal\"
    lang = \"en-US\"
    videos = \"auto\"
    audios = \"auto\"
    subtitles = True

    Args:
        video_id (str): 视频ID/Video ID
        url_access (Union[Unset, UrlAccessMode]):  Default: UrlAccessMode.NORMAL.
        lang (Union[Unset, str]): 语言代码（IETF标签），默认en-US / Language code Default: 'en-US'.
        videos (Union[Unset, VideosAudiosMode]):  Default: VideosAudiosMode.AUTO.
        audios (Union[Unset, VideosAudiosMode]):  Default: VideosAudiosMode.AUTO.
        subtitles (Union[Unset, bool]): 是否获取字幕 / Include subtitles Default: True.
        related (Union[Unset, bool]): 是否获取相关视频 / Include related content Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            video_id=video_id,
            url_access=url_access,
            lang=lang,
            videos=videos,
            audios=audios,
            subtitles=subtitles,
            related=related,
        )
    ).parsed
