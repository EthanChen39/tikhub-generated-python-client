from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    tag_id: int,
    count: Union[Unset, int] = 10,
    refresh_index: Union[Unset, int] = 1,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["tag_id"] = tag_id

    params["count"] = count

    params["refresh_index"] = refresh_index

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/web/fetch_video_channel_result",
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
    tag_id: int,
    count: Union[Unset, int] = 10,
    refresh_index: Union[Unset, int] = 1,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """抖音视频频道数据/Douyin video channel data

     # [中文]
    ### 用途:
    - 抖音视频频道数据
    - https://www.douyin.com/channel/300205
    ### 参数:
    - tag_id: 标签id，从URL中获取
    - count: 数量
    - refresh_index: 刷新索引
    ### 返回:
    - 视频频道数据

    # [English]
    ### Purpose:
    - Douyin video channel data
    - https://www.douyin.com/channel/300205
    ### Parameters:
    - tag_id: Tag id, get from the URL
    - count: Number
    - refresh_index: Refresh index
    ### Return:
    - Video channel data

    # [示例/Example]
    tag_id = 300203
    count = 10
    refresh_index = 1

    Args:
        tag_id (int): 标签id/Tag id
        count (Union[Unset, int]): 数量/Number Default: 10.
        refresh_index (Union[Unset, int]): 刷新索引/Refresh index Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        tag_id=tag_id,
        count=count,
        refresh_index=refresh_index,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    tag_id: int,
    count: Union[Unset, int] = 10,
    refresh_index: Union[Unset, int] = 1,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """抖音视频频道数据/Douyin video channel data

     # [中文]
    ### 用途:
    - 抖音视频频道数据
    - https://www.douyin.com/channel/300205
    ### 参数:
    - tag_id: 标签id，从URL中获取
    - count: 数量
    - refresh_index: 刷新索引
    ### 返回:
    - 视频频道数据

    # [English]
    ### Purpose:
    - Douyin video channel data
    - https://www.douyin.com/channel/300205
    ### Parameters:
    - tag_id: Tag id, get from the URL
    - count: Number
    - refresh_index: Refresh index
    ### Return:
    - Video channel data

    # [示例/Example]
    tag_id = 300203
    count = 10
    refresh_index = 1

    Args:
        tag_id (int): 标签id/Tag id
        count (Union[Unset, int]): 数量/Number Default: 10.
        refresh_index (Union[Unset, int]): 刷新索引/Refresh index Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        tag_id=tag_id,
        count=count,
        refresh_index=refresh_index,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    tag_id: int,
    count: Union[Unset, int] = 10,
    refresh_index: Union[Unset, int] = 1,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """抖音视频频道数据/Douyin video channel data

     # [中文]
    ### 用途:
    - 抖音视频频道数据
    - https://www.douyin.com/channel/300205
    ### 参数:
    - tag_id: 标签id，从URL中获取
    - count: 数量
    - refresh_index: 刷新索引
    ### 返回:
    - 视频频道数据

    # [English]
    ### Purpose:
    - Douyin video channel data
    - https://www.douyin.com/channel/300205
    ### Parameters:
    - tag_id: Tag id, get from the URL
    - count: Number
    - refresh_index: Refresh index
    ### Return:
    - Video channel data

    # [示例/Example]
    tag_id = 300203
    count = 10
    refresh_index = 1

    Args:
        tag_id (int): 标签id/Tag id
        count (Union[Unset, int]): 数量/Number Default: 10.
        refresh_index (Union[Unset, int]): 刷新索引/Refresh index Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        tag_id=tag_id,
        count=count,
        refresh_index=refresh_index,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    tag_id: int,
    count: Union[Unset, int] = 10,
    refresh_index: Union[Unset, int] = 1,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """抖音视频频道数据/Douyin video channel data

     # [中文]
    ### 用途:
    - 抖音视频频道数据
    - https://www.douyin.com/channel/300205
    ### 参数:
    - tag_id: 标签id，从URL中获取
    - count: 数量
    - refresh_index: 刷新索引
    ### 返回:
    - 视频频道数据

    # [English]
    ### Purpose:
    - Douyin video channel data
    - https://www.douyin.com/channel/300205
    ### Parameters:
    - tag_id: Tag id, get from the URL
    - count: Number
    - refresh_index: Refresh index
    ### Return:
    - Video channel data

    # [示例/Example]
    tag_id = 300203
    count = 10
    refresh_index = 1

    Args:
        tag_id (int): 标签id/Tag id
        count (Union[Unset, int]): 数量/Number Default: 10.
        refresh_index (Union[Unset, int]): 刷新索引/Refresh index Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            tag_id=tag_id,
            count=count,
            refresh_index=refresh_index,
        )
    ).parsed
