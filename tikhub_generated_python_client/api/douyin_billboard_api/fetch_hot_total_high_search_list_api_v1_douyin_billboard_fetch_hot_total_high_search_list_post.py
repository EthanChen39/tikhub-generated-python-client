from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_fetch_hot_total_high_search_list_api_v1_douyin_billboard_fetch_hot_total_high_search_list_post import (
    BodyFetchHotTotalHighSearchListApiV1DouyinBillboardFetchHotTotalHighSearchListPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: BodyFetchHotTotalHighSearchListApiV1DouyinBillboardFetchHotTotalHighSearchListPost,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/billboard/fetch_hot_total_high_search_list",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: BodyFetchHotTotalHighSearchListApiV1DouyinBillboardFetchHotTotalHighSearchListPost,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取热度飙升的搜索榜/Fetch search list with rising popularity

     # [中文]
    ### 用途:
    - 获取热度飙升的搜索榜
    ### 参数:
    - page_num: 页码
    - page_size: 每页数量
    - date_window: 时间窗口，1 按小时 2 按天
    - keyword: 搜索关键字
    ### 返回:
    - 热度飙升的搜索榜

    # [English]
    ### Purpose:
    - Get the search list with rising popularity
    ### Parameters:
    - page_num: Page number
    - page_size: Number of items per page
    - date_window: Time window, 1 by hour 2 by day
    - keyword: Search keyword
    ### Return:
    - Search list with rising popularity

    Args:
        body (BodyFetchHotTotalHighSearchListApiV1DouyinBillboardFetchHotTotalHighSearchListPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BodyFetchHotTotalHighSearchListApiV1DouyinBillboardFetchHotTotalHighSearchListPost,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取热度飙升的搜索榜/Fetch search list with rising popularity

     # [中文]
    ### 用途:
    - 获取热度飙升的搜索榜
    ### 参数:
    - page_num: 页码
    - page_size: 每页数量
    - date_window: 时间窗口，1 按小时 2 按天
    - keyword: 搜索关键字
    ### 返回:
    - 热度飙升的搜索榜

    # [English]
    ### Purpose:
    - Get the search list with rising popularity
    ### Parameters:
    - page_num: Page number
    - page_size: Number of items per page
    - date_window: Time window, 1 by hour 2 by day
    - keyword: Search keyword
    ### Return:
    - Search list with rising popularity

    Args:
        body (BodyFetchHotTotalHighSearchListApiV1DouyinBillboardFetchHotTotalHighSearchListPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyFetchHotTotalHighSearchListApiV1DouyinBillboardFetchHotTotalHighSearchListPost,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取热度飙升的搜索榜/Fetch search list with rising popularity

     # [中文]
    ### 用途:
    - 获取热度飙升的搜索榜
    ### 参数:
    - page_num: 页码
    - page_size: 每页数量
    - date_window: 时间窗口，1 按小时 2 按天
    - keyword: 搜索关键字
    ### 返回:
    - 热度飙升的搜索榜

    # [English]
    ### Purpose:
    - Get the search list with rising popularity
    ### Parameters:
    - page_num: Page number
    - page_size: Number of items per page
    - date_window: Time window, 1 by hour 2 by day
    - keyword: Search keyword
    ### Return:
    - Search list with rising popularity

    Args:
        body (BodyFetchHotTotalHighSearchListApiV1DouyinBillboardFetchHotTotalHighSearchListPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BodyFetchHotTotalHighSearchListApiV1DouyinBillboardFetchHotTotalHighSearchListPost,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取热度飙升的搜索榜/Fetch search list with rising popularity

     # [中文]
    ### 用途:
    - 获取热度飙升的搜索榜
    ### 参数:
    - page_num: 页码
    - page_size: 每页数量
    - date_window: 时间窗口，1 按小时 2 按天
    - keyword: 搜索关键字
    ### 返回:
    - 热度飙升的搜索榜

    # [English]
    ### Purpose:
    - Get the search list with rising popularity
    ### Parameters:
    - page_num: Page number
    - page_size: Number of items per page
    - date_window: Time window, 1 by hour 2 by day
    - keyword: Search keyword
    ### Return:
    - Search list with rising popularity

    Args:
        body (BodyFetchHotTotalHighSearchListApiV1DouyinBillboardFetchHotTotalHighSearchListPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
