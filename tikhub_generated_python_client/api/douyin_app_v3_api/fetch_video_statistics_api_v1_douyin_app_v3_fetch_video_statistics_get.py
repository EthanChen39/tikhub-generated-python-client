from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import UNSET, Response


def _get_kwargs(
    *,
    aweme_ids: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["aweme_ids"] = aweme_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/app/v3/fetch_video_statistics",
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
    aweme_ids: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""根据视频ID获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID
    (like count, download count, play count, share count)

     # [中文]
    ### 用途:
    - 根据视频ID获取作品的统计数据
    - 抖音大多数接口已经不再返回作品的播放数，只能通过此接口获取。
    - 可以获取到的统计有：
        - 点赞数（digg_count）
        - 下载数（download_count）
        - 播放数（play_count）
        - 分享数（share_count）
    ### 参数:
    - aweme_ids: 作品id，支持多个视频id，用逗号隔开即可，不能超过2个，单个也可以，则无需逗号。
    ### 返回:
    - 作品统计数据

    # [English]
    ### Purpose:
    - Get the statistical data of the Post according to the video ID
    - Most of the Douyin interfaces no longer return the number of plays of the Post, and can only be
    obtained through this interface.
    - List of statistics that can be obtained:
        - Like count (digg_count)
        - Download count (download_count)
        - Play count (play_count)
        - Share count (share_count)
    ### Parameters:
    - aweme_ids: Video id, supports multiple video ids, separated by commas, no more than 2, single is
    also possible, no need for commas.
    ### Return:
    - Post statistics data

    # [示例/Example]
    aweme_ids = \"7448118827402972455,7126745726494821640\"

    Args:
        aweme_ids (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        aweme_ids=aweme_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    aweme_ids: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""根据视频ID获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID
    (like count, download count, play count, share count)

     # [中文]
    ### 用途:
    - 根据视频ID获取作品的统计数据
    - 抖音大多数接口已经不再返回作品的播放数，只能通过此接口获取。
    - 可以获取到的统计有：
        - 点赞数（digg_count）
        - 下载数（download_count）
        - 播放数（play_count）
        - 分享数（share_count）
    ### 参数:
    - aweme_ids: 作品id，支持多个视频id，用逗号隔开即可，不能超过2个，单个也可以，则无需逗号。
    ### 返回:
    - 作品统计数据

    # [English]
    ### Purpose:
    - Get the statistical data of the Post according to the video ID
    - Most of the Douyin interfaces no longer return the number of plays of the Post, and can only be
    obtained through this interface.
    - List of statistics that can be obtained:
        - Like count (digg_count)
        - Download count (download_count)
        - Play count (play_count)
        - Share count (share_count)
    ### Parameters:
    - aweme_ids: Video id, supports multiple video ids, separated by commas, no more than 2, single is
    also possible, no need for commas.
    ### Return:
    - Post statistics data

    # [示例/Example]
    aweme_ids = \"7448118827402972455,7126745726494821640\"

    Args:
        aweme_ids (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        aweme_ids=aweme_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    aweme_ids: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""根据视频ID获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID
    (like count, download count, play count, share count)

     # [中文]
    ### 用途:
    - 根据视频ID获取作品的统计数据
    - 抖音大多数接口已经不再返回作品的播放数，只能通过此接口获取。
    - 可以获取到的统计有：
        - 点赞数（digg_count）
        - 下载数（download_count）
        - 播放数（play_count）
        - 分享数（share_count）
    ### 参数:
    - aweme_ids: 作品id，支持多个视频id，用逗号隔开即可，不能超过2个，单个也可以，则无需逗号。
    ### 返回:
    - 作品统计数据

    # [English]
    ### Purpose:
    - Get the statistical data of the Post according to the video ID
    - Most of the Douyin interfaces no longer return the number of plays of the Post, and can only be
    obtained through this interface.
    - List of statistics that can be obtained:
        - Like count (digg_count)
        - Download count (download_count)
        - Play count (play_count)
        - Share count (share_count)
    ### Parameters:
    - aweme_ids: Video id, supports multiple video ids, separated by commas, no more than 2, single is
    also possible, no need for commas.
    ### Return:
    - Post statistics data

    # [示例/Example]
    aweme_ids = \"7448118827402972455,7126745726494821640\"

    Args:
        aweme_ids (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        aweme_ids=aweme_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    aweme_ids: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""根据视频ID获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID
    (like count, download count, play count, share count)

     # [中文]
    ### 用途:
    - 根据视频ID获取作品的统计数据
    - 抖音大多数接口已经不再返回作品的播放数，只能通过此接口获取。
    - 可以获取到的统计有：
        - 点赞数（digg_count）
        - 下载数（download_count）
        - 播放数（play_count）
        - 分享数（share_count）
    ### 参数:
    - aweme_ids: 作品id，支持多个视频id，用逗号隔开即可，不能超过2个，单个也可以，则无需逗号。
    ### 返回:
    - 作品统计数据

    # [English]
    ### Purpose:
    - Get the statistical data of the Post according to the video ID
    - Most of the Douyin interfaces no longer return the number of plays of the Post, and can only be
    obtained through this interface.
    - List of statistics that can be obtained:
        - Like count (digg_count)
        - Download count (download_count)
        - Play count (play_count)
        - Share count (share_count)
    ### Parameters:
    - aweme_ids: Video id, supports multiple video ids, separated by commas, no more than 2, single is
    also possible, no need for commas.
    ### Return:
    - Post statistics data

    # [示例/Example]
    aweme_ids = \"7448118827402972455,7126745726494821640\"

    Args:
        aweme_ids (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            aweme_ids=aweme_ids,
        )
    ).parsed
