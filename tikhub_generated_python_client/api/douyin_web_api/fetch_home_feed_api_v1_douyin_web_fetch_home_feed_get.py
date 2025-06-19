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
    count: Union[Unset, int] = 10,
    refresh_index: Union[Unset, int] = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["count"] = count

    params["refresh_index"] = refresh_index

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/web/fetch_home_feed",
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
    count: Union[Unset, int] = 10,
    refresh_index: Union[Unset, int] = 0,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取首页推荐数据/Get home feed data

     # [中文]
    ### 用途:
    - 获取首页推荐数据
    ### 参数:
    - count: 数量，默认为10，建议保持不变。
    - refresh_index: 翻页索引，默认为0，然后每次增加1用于翻页。
    ### 返回:
    - Feed数据

    # [English]
    ### Purpose:
    - Get home feed data
    ### Parameters:
    - count: Number, default is 10, it is recommended to keep it unchanged.
    - refresh_index: Paging index, default is 0, then increase by 1 each time for paging.
    ### Return:
    - Feed data

    # [示例/Example]
    count = 10
    refresh_index = 0

    Args:
        count (Union[Unset, int]): 数量/Number Default: 10.
        refresh_index (Union[Unset, int]): 翻页索引/Paging index Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
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
    count: Union[Unset, int] = 10,
    refresh_index: Union[Unset, int] = 0,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取首页推荐数据/Get home feed data

     # [中文]
    ### 用途:
    - 获取首页推荐数据
    ### 参数:
    - count: 数量，默认为10，建议保持不变。
    - refresh_index: 翻页索引，默认为0，然后每次增加1用于翻页。
    ### 返回:
    - Feed数据

    # [English]
    ### Purpose:
    - Get home feed data
    ### Parameters:
    - count: Number, default is 10, it is recommended to keep it unchanged.
    - refresh_index: Paging index, default is 0, then increase by 1 each time for paging.
    ### Return:
    - Feed data

    # [示例/Example]
    count = 10
    refresh_index = 0

    Args:
        count (Union[Unset, int]): 数量/Number Default: 10.
        refresh_index (Union[Unset, int]): 翻页索引/Paging index Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        count=count,
        refresh_index=refresh_index,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    count: Union[Unset, int] = 10,
    refresh_index: Union[Unset, int] = 0,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取首页推荐数据/Get home feed data

     # [中文]
    ### 用途:
    - 获取首页推荐数据
    ### 参数:
    - count: 数量，默认为10，建议保持不变。
    - refresh_index: 翻页索引，默认为0，然后每次增加1用于翻页。
    ### 返回:
    - Feed数据

    # [English]
    ### Purpose:
    - Get home feed data
    ### Parameters:
    - count: Number, default is 10, it is recommended to keep it unchanged.
    - refresh_index: Paging index, default is 0, then increase by 1 each time for paging.
    ### Return:
    - Feed data

    # [示例/Example]
    count = 10
    refresh_index = 0

    Args:
        count (Union[Unset, int]): 数量/Number Default: 10.
        refresh_index (Union[Unset, int]): 翻页索引/Paging index Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        count=count,
        refresh_index=refresh_index,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    count: Union[Unset, int] = 10,
    refresh_index: Union[Unset, int] = 0,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取首页推荐数据/Get home feed data

     # [中文]
    ### 用途:
    - 获取首页推荐数据
    ### 参数:
    - count: 数量，默认为10，建议保持不变。
    - refresh_index: 翻页索引，默认为0，然后每次增加1用于翻页。
    ### 返回:
    - Feed数据

    # [English]
    ### Purpose:
    - Get home feed data
    ### Parameters:
    - count: Number, default is 10, it is recommended to keep it unchanged.
    - refresh_index: Paging index, default is 0, then increase by 1 each time for paging.
    ### Return:
    - Feed data

    # [示例/Example]
    count = 10
    refresh_index = 0

    Args:
        count (Union[Unset, int]): 数量/Number Default: 10.
        refresh_index (Union[Unset, int]): 翻页索引/Paging index Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            count=count,
            refresh_index=refresh_index,
        )
    ).parsed
