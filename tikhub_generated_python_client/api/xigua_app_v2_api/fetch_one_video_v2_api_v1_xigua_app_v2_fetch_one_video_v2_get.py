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
    item_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["item_id"] = item_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/xigua/app/v2/fetch_one_video_v2",
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
    item_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个作品数据 V2/Get single video data V2

     # [中文]
    ### 用途:
    - 获取单个作品数据（信息全面，包含标题等信息，但是不包含相关视频推荐信息）
    ### 参数:
    - item_id: 作品id
    ### 返回:
    - 作品数据，其中包含视频链接的Base64编码播放地址，需要前端解码后使用，或者使用 /fetch_one_video_play_url 获取播放链接。

    # [English]
    ### Purpose:
    - Get single video data (more comprehensive information, including title and other information, but
    not including information about related video recommendations)
    ### Parameters:
    - item_id: Video id
    ### Return:
    - Video data, which contains the Base64 encoded playback address of the video link, which needs to
    be decoded and used by the front end, or use /fetch_one_video_play_url to get the playback link.

    # [示例/Example]
    item_id: \"7354954305222377999\"

    Args:
        item_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    item_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个作品数据 V2/Get single video data V2

     # [中文]
    ### 用途:
    - 获取单个作品数据（信息全面，包含标题等信息，但是不包含相关视频推荐信息）
    ### 参数:
    - item_id: 作品id
    ### 返回:
    - 作品数据，其中包含视频链接的Base64编码播放地址，需要前端解码后使用，或者使用 /fetch_one_video_play_url 获取播放链接。

    # [English]
    ### Purpose:
    - Get single video data (more comprehensive information, including title and other information, but
    not including information about related video recommendations)
    ### Parameters:
    - item_id: Video id
    ### Return:
    - Video data, which contains the Base64 encoded playback address of the video link, which needs to
    be decoded and used by the front end, or use /fetch_one_video_play_url to get the playback link.

    # [示例/Example]
    item_id: \"7354954305222377999\"

    Args:
        item_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        item_id=item_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    item_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个作品数据 V2/Get single video data V2

     # [中文]
    ### 用途:
    - 获取单个作品数据（信息全面，包含标题等信息，但是不包含相关视频推荐信息）
    ### 参数:
    - item_id: 作品id
    ### 返回:
    - 作品数据，其中包含视频链接的Base64编码播放地址，需要前端解码后使用，或者使用 /fetch_one_video_play_url 获取播放链接。

    # [English]
    ### Purpose:
    - Get single video data (more comprehensive information, including title and other information, but
    not including information about related video recommendations)
    ### Parameters:
    - item_id: Video id
    ### Return:
    - Video data, which contains the Base64 encoded playback address of the video link, which needs to
    be decoded and used by the front end, or use /fetch_one_video_play_url to get the playback link.

    # [示例/Example]
    item_id: \"7354954305222377999\"

    Args:
        item_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    item_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个作品数据 V2/Get single video data V2

     # [中文]
    ### 用途:
    - 获取单个作品数据（信息全面，包含标题等信息，但是不包含相关视频推荐信息）
    ### 参数:
    - item_id: 作品id
    ### 返回:
    - 作品数据，其中包含视频链接的Base64编码播放地址，需要前端解码后使用，或者使用 /fetch_one_video_play_url 获取播放链接。

    # [English]
    ### Purpose:
    - Get single video data (more comprehensive information, including title and other information, but
    not including information about related video recommendations)
    ### Parameters:
    - item_id: Video id
    ### Return:
    - Video data, which contains the Base64 encoded playback address of the video link, which needs to
    be decoded and used by the front end, or use /fetch_one_video_play_url to get the playback link.

    # [示例/Example]
    item_id: \"7354954305222377999\"

    Args:
        item_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            item_id=item_id,
        )
    ).parsed
