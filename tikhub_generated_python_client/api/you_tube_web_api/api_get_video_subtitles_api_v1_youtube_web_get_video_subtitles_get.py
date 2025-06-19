from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...models.subtitle_format import SubtitleFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    subtitle_url: str,
    format_: Union[Unset, SubtitleFormat] = SubtitleFormat.SRT,
    fix_overlap: Union[Unset, bool] = True,
    target_lang: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["subtitle_url"] = subtitle_url

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params["fix_overlap"] = fix_overlap

    json_target_lang: Union[None, Unset, str]
    if isinstance(target_lang, Unset):
        json_target_lang = UNSET
    else:
        json_target_lang = target_lang
    params["target_lang"] = json_target_lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/youtube/web/get_video_subtitles",
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
    subtitle_url: str,
    format_: Union[Unset, SubtitleFormat] = SubtitleFormat.SRT,
    fix_overlap: Union[Unset, bool] = True,
    target_lang: Union[None, Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频字幕/Get video subtitles

     # [中文]
    ### 用途:
    - 获取视频字幕内容
    ### 使用流程:
    1. 先调用获取视频详情接口，从字幕数据中获取subtitleUrl
    2. 使用该URL作为本接口参数
    ### 参数说明:
    - fix_overlap: 特别适用于自动生成的字幕，会自动分割重叠的时间段

    # [English]
    ### Purpose:
    - Get video subtitle content
    ### Workflow:
    1. First call get_video_info to obtain subtitleUrl
    2. Use that URL as parameter here
    ### Parameter Notes:
    - fix_overlap: Especially useful for auto-generated subtitles, will split overlapping time ranges

    # [示例/Example]
    subtitle_url = \"https://www.youtube.com/api/timedtext?v=G33j5Qi4rE8...\"
    target_lang = \"zh-CN\"

    Args:
        subtitle_url (str): 字幕URL（需先调用获取视频详情接口） / Subtitle URL from video details
        format_ (Union[Unset, SubtitleFormat]):  Default: SubtitleFormat.SRT.
        fix_overlap (Union[Unset, bool]): 修复重叠字幕（默认开启） / Fix overlapping subtitles Default: True.
        target_lang (Union[None, Unset, str]): 目标语言代码（留空保持原语言） / Target language code

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        subtitle_url=subtitle_url,
        format_=format_,
        fix_overlap=fix_overlap,
        target_lang=target_lang,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    subtitle_url: str,
    format_: Union[Unset, SubtitleFormat] = SubtitleFormat.SRT,
    fix_overlap: Union[Unset, bool] = True,
    target_lang: Union[None, Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频字幕/Get video subtitles

     # [中文]
    ### 用途:
    - 获取视频字幕内容
    ### 使用流程:
    1. 先调用获取视频详情接口，从字幕数据中获取subtitleUrl
    2. 使用该URL作为本接口参数
    ### 参数说明:
    - fix_overlap: 特别适用于自动生成的字幕，会自动分割重叠的时间段

    # [English]
    ### Purpose:
    - Get video subtitle content
    ### Workflow:
    1. First call get_video_info to obtain subtitleUrl
    2. Use that URL as parameter here
    ### Parameter Notes:
    - fix_overlap: Especially useful for auto-generated subtitles, will split overlapping time ranges

    # [示例/Example]
    subtitle_url = \"https://www.youtube.com/api/timedtext?v=G33j5Qi4rE8...\"
    target_lang = \"zh-CN\"

    Args:
        subtitle_url (str): 字幕URL（需先调用获取视频详情接口） / Subtitle URL from video details
        format_ (Union[Unset, SubtitleFormat]):  Default: SubtitleFormat.SRT.
        fix_overlap (Union[Unset, bool]): 修复重叠字幕（默认开启） / Fix overlapping subtitles Default: True.
        target_lang (Union[None, Unset, str]): 目标语言代码（留空保持原语言） / Target language code

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        subtitle_url=subtitle_url,
        format_=format_,
        fix_overlap=fix_overlap,
        target_lang=target_lang,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    subtitle_url: str,
    format_: Union[Unset, SubtitleFormat] = SubtitleFormat.SRT,
    fix_overlap: Union[Unset, bool] = True,
    target_lang: Union[None, Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频字幕/Get video subtitles

     # [中文]
    ### 用途:
    - 获取视频字幕内容
    ### 使用流程:
    1. 先调用获取视频详情接口，从字幕数据中获取subtitleUrl
    2. 使用该URL作为本接口参数
    ### 参数说明:
    - fix_overlap: 特别适用于自动生成的字幕，会自动分割重叠的时间段

    # [English]
    ### Purpose:
    - Get video subtitle content
    ### Workflow:
    1. First call get_video_info to obtain subtitleUrl
    2. Use that URL as parameter here
    ### Parameter Notes:
    - fix_overlap: Especially useful for auto-generated subtitles, will split overlapping time ranges

    # [示例/Example]
    subtitle_url = \"https://www.youtube.com/api/timedtext?v=G33j5Qi4rE8...\"
    target_lang = \"zh-CN\"

    Args:
        subtitle_url (str): 字幕URL（需先调用获取视频详情接口） / Subtitle URL from video details
        format_ (Union[Unset, SubtitleFormat]):  Default: SubtitleFormat.SRT.
        fix_overlap (Union[Unset, bool]): 修复重叠字幕（默认开启） / Fix overlapping subtitles Default: True.
        target_lang (Union[None, Unset, str]): 目标语言代码（留空保持原语言） / Target language code

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        subtitle_url=subtitle_url,
        format_=format_,
        fix_overlap=fix_overlap,
        target_lang=target_lang,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    subtitle_url: str,
    format_: Union[Unset, SubtitleFormat] = SubtitleFormat.SRT,
    fix_overlap: Union[Unset, bool] = True,
    target_lang: Union[None, Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频字幕/Get video subtitles

     # [中文]
    ### 用途:
    - 获取视频字幕内容
    ### 使用流程:
    1. 先调用获取视频详情接口，从字幕数据中获取subtitleUrl
    2. 使用该URL作为本接口参数
    ### 参数说明:
    - fix_overlap: 特别适用于自动生成的字幕，会自动分割重叠的时间段

    # [English]
    ### Purpose:
    - Get video subtitle content
    ### Workflow:
    1. First call get_video_info to obtain subtitleUrl
    2. Use that URL as parameter here
    ### Parameter Notes:
    - fix_overlap: Especially useful for auto-generated subtitles, will split overlapping time ranges

    # [示例/Example]
    subtitle_url = \"https://www.youtube.com/api/timedtext?v=G33j5Qi4rE8...\"
    target_lang = \"zh-CN\"

    Args:
        subtitle_url (str): 字幕URL（需先调用获取视频详情接口） / Subtitle URL from video details
        format_ (Union[Unset, SubtitleFormat]):  Default: SubtitleFormat.SRT.
        fix_overlap (Union[Unset, bool]): 修复重叠字幕（默认开启） / Fix overlapping subtitles Default: True.
        target_lang (Union[None, Unset, str]): 目标语言代码（留空保持原语言） / Target language code

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            subtitle_url=subtitle_url,
            format_=format_,
            fix_overlap=fix_overlap,
            target_lang=target_lang,
        )
    ).parsed
