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
    aweme_id: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["aweme_id"] = aweme_id

    params["cursor"] = cursor

    params["count"] = count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/app/v3/fetch_video_comments",
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
    aweme_id: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个视频评论数据/Get single video comments data

     # [中文]
    ### 用途:
    - 获取单个视频评论数据
    ### 参数:
    - aweme_id: 作品id
    - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
    - count: 数量
    ### 返回:
    - 评论数据

    # [English]
    ### Purpose:
    - Get single video comments data
    ### Parameters:
    - aweme_id: Video id
    - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the
    first response.
    - count: Number
    ### Return:
    - Comments data

    # [示例/Example]
    aweme_id = \"7326156045968067873\"
    cursor = 0
    count = 20

    Args:
        aweme_id (str): 作品id/Video id
        cursor (Union[Unset, int]): 游标/Cursor Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        aweme_id=aweme_id,
        cursor=cursor,
        count=count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    aweme_id: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个视频评论数据/Get single video comments data

     # [中文]
    ### 用途:
    - 获取单个视频评论数据
    ### 参数:
    - aweme_id: 作品id
    - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
    - count: 数量
    ### 返回:
    - 评论数据

    # [English]
    ### Purpose:
    - Get single video comments data
    ### Parameters:
    - aweme_id: Video id
    - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the
    first response.
    - count: Number
    ### Return:
    - Comments data

    # [示例/Example]
    aweme_id = \"7326156045968067873\"
    cursor = 0
    count = 20

    Args:
        aweme_id (str): 作品id/Video id
        cursor (Union[Unset, int]): 游标/Cursor Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        aweme_id=aweme_id,
        cursor=cursor,
        count=count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    aweme_id: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个视频评论数据/Get single video comments data

     # [中文]
    ### 用途:
    - 获取单个视频评论数据
    ### 参数:
    - aweme_id: 作品id
    - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
    - count: 数量
    ### 返回:
    - 评论数据

    # [English]
    ### Purpose:
    - Get single video comments data
    ### Parameters:
    - aweme_id: Video id
    - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the
    first response.
    - count: Number
    ### Return:
    - Comments data

    # [示例/Example]
    aweme_id = \"7326156045968067873\"
    cursor = 0
    count = 20

    Args:
        aweme_id (str): 作品id/Video id
        cursor (Union[Unset, int]): 游标/Cursor Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        aweme_id=aweme_id,
        cursor=cursor,
        count=count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    aweme_id: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单个视频评论数据/Get single video comments data

     # [中文]
    ### 用途:
    - 获取单个视频评论数据
    ### 参数:
    - aweme_id: 作品id
    - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
    - count: 数量
    ### 返回:
    - 评论数据

    # [English]
    ### Purpose:
    - Get single video comments data
    ### Parameters:
    - aweme_id: Video id
    - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the
    first response.
    - count: Number
    ### Return:
    - Comments data

    # [示例/Example]
    aweme_id = \"7326156045968067873\"
    cursor = 0
    count = 20

    Args:
        aweme_id (str): 作品id/Video id
        cursor (Union[Unset, int]): 游标/Cursor Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            aweme_id=aweme_id,
            cursor=cursor,
            count=count,
        )
    ).parsed
