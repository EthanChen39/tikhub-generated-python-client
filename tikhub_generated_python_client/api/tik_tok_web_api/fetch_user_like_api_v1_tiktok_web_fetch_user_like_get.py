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
    sec_uid: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    cover_format: Union[Unset, int] = 2,
    post_item_list_request_type: Union[Unset, int] = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["secUid"] = sec_uid

    params["cursor"] = cursor

    params["count"] = count

    params["coverFormat"] = cover_format

    params["post_item_list_request_type"] = post_item_list_request_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/web/fetch_user_like",
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
    sec_uid: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    cover_format: Union[Unset, int] = 2,
    post_item_list_request_type: Union[Unset, int] = 0,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户的点赞列表/Get user likes

     # [中文]
    ### 用途:
    - 获取用户的点赞列表
    - 注意: 该接口需要用户点赞列表为公开状态
    ### 参数:
    - secUid: 用户secUid
    - cursor: 翻页游标
    - count: 每页数量，默认为20，不可变更。
    - coverFormat: 封面格式
    - post_item_list_request_type: 排序方式
        - 0：默认排序
        - 1：热门排序
        - 2：最旧排序
    ### 返回:
    - 用户的点赞列表

    # [English]
    ### Purpose:
    - Get user likes
    - Note: This interface requires that the user's like list be public
    ### Parameters:
    - secUid: User secUid
    - cursor: Page cursor
    - count: Number per page, default is 20, cannot be changed.
    - coverFormat: Cover format
    - post_item_list_request_type: Sort type
        - 0: Default sort
        - 1: Hot sort
        - 2: Oldest sort
    ### Return:
    - User likes

    # [示例/Example]
    secUid = \"MS4wLjABAAAAq1iRXNduFZpY301UkVpJ1eQT60_NiWS9QQSeNqmNQEDJp0pOF8cpleNEdiJx5_IU\"
    cursor = 0
    count = 20
    coverFormat = 2

    Args:
        sec_uid (str): 用户secUid/User secUid
        cursor (Union[Unset, int]): 翻页游标/Page cursor Default: 0.
        count (Union[Unset, int]): 每页数量/Number per page Default: 20.
        cover_format (Union[Unset, int]): 封面格式/Cover format Default: 2.
        post_item_list_request_type (Union[Unset, int]): 排序方式/Sort type Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        sec_uid=sec_uid,
        cursor=cursor,
        count=count,
        cover_format=cover_format,
        post_item_list_request_type=post_item_list_request_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    sec_uid: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    cover_format: Union[Unset, int] = 2,
    post_item_list_request_type: Union[Unset, int] = 0,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户的点赞列表/Get user likes

     # [中文]
    ### 用途:
    - 获取用户的点赞列表
    - 注意: 该接口需要用户点赞列表为公开状态
    ### 参数:
    - secUid: 用户secUid
    - cursor: 翻页游标
    - count: 每页数量，默认为20，不可变更。
    - coverFormat: 封面格式
    - post_item_list_request_type: 排序方式
        - 0：默认排序
        - 1：热门排序
        - 2：最旧排序
    ### 返回:
    - 用户的点赞列表

    # [English]
    ### Purpose:
    - Get user likes
    - Note: This interface requires that the user's like list be public
    ### Parameters:
    - secUid: User secUid
    - cursor: Page cursor
    - count: Number per page, default is 20, cannot be changed.
    - coverFormat: Cover format
    - post_item_list_request_type: Sort type
        - 0: Default sort
        - 1: Hot sort
        - 2: Oldest sort
    ### Return:
    - User likes

    # [示例/Example]
    secUid = \"MS4wLjABAAAAq1iRXNduFZpY301UkVpJ1eQT60_NiWS9QQSeNqmNQEDJp0pOF8cpleNEdiJx5_IU\"
    cursor = 0
    count = 20
    coverFormat = 2

    Args:
        sec_uid (str): 用户secUid/User secUid
        cursor (Union[Unset, int]): 翻页游标/Page cursor Default: 0.
        count (Union[Unset, int]): 每页数量/Number per page Default: 20.
        cover_format (Union[Unset, int]): 封面格式/Cover format Default: 2.
        post_item_list_request_type (Union[Unset, int]): 排序方式/Sort type Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        sec_uid=sec_uid,
        cursor=cursor,
        count=count,
        cover_format=cover_format,
        post_item_list_request_type=post_item_list_request_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    sec_uid: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    cover_format: Union[Unset, int] = 2,
    post_item_list_request_type: Union[Unset, int] = 0,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户的点赞列表/Get user likes

     # [中文]
    ### 用途:
    - 获取用户的点赞列表
    - 注意: 该接口需要用户点赞列表为公开状态
    ### 参数:
    - secUid: 用户secUid
    - cursor: 翻页游标
    - count: 每页数量，默认为20，不可变更。
    - coverFormat: 封面格式
    - post_item_list_request_type: 排序方式
        - 0：默认排序
        - 1：热门排序
        - 2：最旧排序
    ### 返回:
    - 用户的点赞列表

    # [English]
    ### Purpose:
    - Get user likes
    - Note: This interface requires that the user's like list be public
    ### Parameters:
    - secUid: User secUid
    - cursor: Page cursor
    - count: Number per page, default is 20, cannot be changed.
    - coverFormat: Cover format
    - post_item_list_request_type: Sort type
        - 0: Default sort
        - 1: Hot sort
        - 2: Oldest sort
    ### Return:
    - User likes

    # [示例/Example]
    secUid = \"MS4wLjABAAAAq1iRXNduFZpY301UkVpJ1eQT60_NiWS9QQSeNqmNQEDJp0pOF8cpleNEdiJx5_IU\"
    cursor = 0
    count = 20
    coverFormat = 2

    Args:
        sec_uid (str): 用户secUid/User secUid
        cursor (Union[Unset, int]): 翻页游标/Page cursor Default: 0.
        count (Union[Unset, int]): 每页数量/Number per page Default: 20.
        cover_format (Union[Unset, int]): 封面格式/Cover format Default: 2.
        post_item_list_request_type (Union[Unset, int]): 排序方式/Sort type Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        sec_uid=sec_uid,
        cursor=cursor,
        count=count,
        cover_format=cover_format,
        post_item_list_request_type=post_item_list_request_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    sec_uid: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    cover_format: Union[Unset, int] = 2,
    post_item_list_request_type: Union[Unset, int] = 0,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户的点赞列表/Get user likes

     # [中文]
    ### 用途:
    - 获取用户的点赞列表
    - 注意: 该接口需要用户点赞列表为公开状态
    ### 参数:
    - secUid: 用户secUid
    - cursor: 翻页游标
    - count: 每页数量，默认为20，不可变更。
    - coverFormat: 封面格式
    - post_item_list_request_type: 排序方式
        - 0：默认排序
        - 1：热门排序
        - 2：最旧排序
    ### 返回:
    - 用户的点赞列表

    # [English]
    ### Purpose:
    - Get user likes
    - Note: This interface requires that the user's like list be public
    ### Parameters:
    - secUid: User secUid
    - cursor: Page cursor
    - count: Number per page, default is 20, cannot be changed.
    - coverFormat: Cover format
    - post_item_list_request_type: Sort type
        - 0: Default sort
        - 1: Hot sort
        - 2: Oldest sort
    ### Return:
    - User likes

    # [示例/Example]
    secUid = \"MS4wLjABAAAAq1iRXNduFZpY301UkVpJ1eQT60_NiWS9QQSeNqmNQEDJp0pOF8cpleNEdiJx5_IU\"
    cursor = 0
    count = 20
    coverFormat = 2

    Args:
        sec_uid (str): 用户secUid/User secUid
        cursor (Union[Unset, int]): 翻页游标/Page cursor Default: 0.
        count (Union[Unset, int]): 每页数量/Number per page Default: 20.
        cover_format (Union[Unset, int]): 封面格式/Cover format Default: 2.
        post_item_list_request_type (Union[Unset, int]): 排序方式/Sort type Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            sec_uid=sec_uid,
            cursor=cursor,
            count=count,
            cover_format=cover_format,
            post_item_list_request_type=post_item_list_request_type,
        )
    ).parsed
