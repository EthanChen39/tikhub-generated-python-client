from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    mlog_id: str,
    resolution: Union[Unset, str] = "1080",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["mlogId"] = mlog_id

    params["resolution"] = resolution

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/net_ease_cloud_music/app/fetch_music_log_video_url",
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
    mlog_id: str,
    resolution: Union[Unset, str] = "1080",
) -> Response[Union[Any, HTTPValidationError]]:
    r"""Mlog（音乐视频）播放地址/Mlog (music video) playback address

     # [中文]
    ### 用途:
    - 获取Mlog（音乐视频）播放地址。
    ### 参数:
    - mlogId: Mlog ID，可以在APP中点击分享按钮获取链接，链接中包含mlogId。
    - resolution: 分辨率，默认为1080，保持默认即可。
    ### 返回:
    - Mlog播放地址（有时候会有水印，根据视频源而定。）

    # [English]
    ### Purpose:
    - Fetch Mlog (music video) playback address.
    ### Parameters:
    - mlogId: Mlog ID, you can get the link by clicking the share button in the APP, the link contains
    mlogId.
    - resolution: Resolution, default is 1080, keep the default.
    ### Returns:
    - Mlog playback address (sometimes there will be a watermark, depending on the video source.)

    # [示例/Example]
    > 分享链接/Share link: https://fn.music.163.com/g/mlog/mlog-
    mobile/landing/mlog?id=a1qQQOQNVueO2g7&type=2
    mlogId = \"a1qQQOQNVueO2g7\"

    Args:
        mlog_id (str): Mlog ID/Mlog ID
        resolution (Union[Unset, str]): 分辨率/Resolution Default: '1080'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        mlog_id=mlog_id,
        resolution=resolution,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    mlog_id: str,
    resolution: Union[Unset, str] = "1080",
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""Mlog（音乐视频）播放地址/Mlog (music video) playback address

     # [中文]
    ### 用途:
    - 获取Mlog（音乐视频）播放地址。
    ### 参数:
    - mlogId: Mlog ID，可以在APP中点击分享按钮获取链接，链接中包含mlogId。
    - resolution: 分辨率，默认为1080，保持默认即可。
    ### 返回:
    - Mlog播放地址（有时候会有水印，根据视频源而定。）

    # [English]
    ### Purpose:
    - Fetch Mlog (music video) playback address.
    ### Parameters:
    - mlogId: Mlog ID, you can get the link by clicking the share button in the APP, the link contains
    mlogId.
    - resolution: Resolution, default is 1080, keep the default.
    ### Returns:
    - Mlog playback address (sometimes there will be a watermark, depending on the video source.)

    # [示例/Example]
    > 分享链接/Share link: https://fn.music.163.com/g/mlog/mlog-
    mobile/landing/mlog?id=a1qQQOQNVueO2g7&type=2
    mlogId = \"a1qQQOQNVueO2g7\"

    Args:
        mlog_id (str): Mlog ID/Mlog ID
        resolution (Union[Unset, str]): 分辨率/Resolution Default: '1080'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        mlog_id=mlog_id,
        resolution=resolution,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    mlog_id: str,
    resolution: Union[Unset, str] = "1080",
) -> Response[Union[Any, HTTPValidationError]]:
    r"""Mlog（音乐视频）播放地址/Mlog (music video) playback address

     # [中文]
    ### 用途:
    - 获取Mlog（音乐视频）播放地址。
    ### 参数:
    - mlogId: Mlog ID，可以在APP中点击分享按钮获取链接，链接中包含mlogId。
    - resolution: 分辨率，默认为1080，保持默认即可。
    ### 返回:
    - Mlog播放地址（有时候会有水印，根据视频源而定。）

    # [English]
    ### Purpose:
    - Fetch Mlog (music video) playback address.
    ### Parameters:
    - mlogId: Mlog ID, you can get the link by clicking the share button in the APP, the link contains
    mlogId.
    - resolution: Resolution, default is 1080, keep the default.
    ### Returns:
    - Mlog playback address (sometimes there will be a watermark, depending on the video source.)

    # [示例/Example]
    > 分享链接/Share link: https://fn.music.163.com/g/mlog/mlog-
    mobile/landing/mlog?id=a1qQQOQNVueO2g7&type=2
    mlogId = \"a1qQQOQNVueO2g7\"

    Args:
        mlog_id (str): Mlog ID/Mlog ID
        resolution (Union[Unset, str]): 分辨率/Resolution Default: '1080'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        mlog_id=mlog_id,
        resolution=resolution,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    mlog_id: str,
    resolution: Union[Unset, str] = "1080",
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""Mlog（音乐视频）播放地址/Mlog (music video) playback address

     # [中文]
    ### 用途:
    - 获取Mlog（音乐视频）播放地址。
    ### 参数:
    - mlogId: Mlog ID，可以在APP中点击分享按钮获取链接，链接中包含mlogId。
    - resolution: 分辨率，默认为1080，保持默认即可。
    ### 返回:
    - Mlog播放地址（有时候会有水印，根据视频源而定。）

    # [English]
    ### Purpose:
    - Fetch Mlog (music video) playback address.
    ### Parameters:
    - mlogId: Mlog ID, you can get the link by clicking the share button in the APP, the link contains
    mlogId.
    - resolution: Resolution, default is 1080, keep the default.
    ### Returns:
    - Mlog playback address (sometimes there will be a watermark, depending on the video source.)

    # [示例/Example]
    > 分享链接/Share link: https://fn.music.163.com/g/mlog/mlog-
    mobile/landing/mlog?id=a1qQQOQNVueO2g7&type=2
    mlogId = \"a1qQQOQNVueO2g7\"

    Args:
        mlog_id (str): Mlog ID/Mlog ID
        resolution (Union[Unset, str]): 分辨率/Resolution Default: '1080'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            mlog_id=mlog_id,
            resolution=resolution,
        )
    ).parsed
