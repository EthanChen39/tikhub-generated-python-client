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
    ch_id: str,
    cursor: Union[Unset, int] = 0,
    sort_type: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ch_id"] = ch_id

    params["cursor"] = cursor

    params["sort_type"] = sort_type

    params["count"] = count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/app/v3/fetch_hashtag_video_list",
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
    ch_id: str,
    cursor: Union[Unset, int] = 0,
    sort_type: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取指定话题的作品数据/Get video list of specified hashtag

     # [中文]
    ### 用途:
    - 获取指定话题的作品数据
    ### 参数:
    - ch_id: 话题id
    - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
    - sort_type: 0:综合排序 1:最多点赞 2:最新发布
    - count: 数量，请保持默认，否则会出现BUG。
    ### 返回:
    - 话题作品数据

    # [English]
    ### Purpose:
    - Get video list of specified hashtag
    ### Parameters:
    - ch_id: Hashtag id
    - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the
    first response.
    - sort_type: 0: Comprehensive sorting 1: Most likes 2: Latest release
    - count: Number Please keep the default, otherwise there will be BUG.
    ### Return:
    - Hashtag video list data

    # [示例/Example]
    ch_id = 1575791821492238
    cursor = 0
    sort_type = 0
    count = 10

    Args:
        ch_id (str): 话题id/Hashtag id
        cursor (Union[Unset, int]): 游标/Cursor Default: 0.
        sort_type (Union[Unset, int]): 排序类型/Sort type Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        ch_id=ch_id,
        cursor=cursor,
        sort_type=sort_type,
        count=count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ch_id: str,
    cursor: Union[Unset, int] = 0,
    sort_type: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取指定话题的作品数据/Get video list of specified hashtag

     # [中文]
    ### 用途:
    - 获取指定话题的作品数据
    ### 参数:
    - ch_id: 话题id
    - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
    - sort_type: 0:综合排序 1:最多点赞 2:最新发布
    - count: 数量，请保持默认，否则会出现BUG。
    ### 返回:
    - 话题作品数据

    # [English]
    ### Purpose:
    - Get video list of specified hashtag
    ### Parameters:
    - ch_id: Hashtag id
    - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the
    first response.
    - sort_type: 0: Comprehensive sorting 1: Most likes 2: Latest release
    - count: Number Please keep the default, otherwise there will be BUG.
    ### Return:
    - Hashtag video list data

    # [示例/Example]
    ch_id = 1575791821492238
    cursor = 0
    sort_type = 0
    count = 10

    Args:
        ch_id (str): 话题id/Hashtag id
        cursor (Union[Unset, int]): 游标/Cursor Default: 0.
        sort_type (Union[Unset, int]): 排序类型/Sort type Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        ch_id=ch_id,
        cursor=cursor,
        sort_type=sort_type,
        count=count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ch_id: str,
    cursor: Union[Unset, int] = 0,
    sort_type: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取指定话题的作品数据/Get video list of specified hashtag

     # [中文]
    ### 用途:
    - 获取指定话题的作品数据
    ### 参数:
    - ch_id: 话题id
    - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
    - sort_type: 0:综合排序 1:最多点赞 2:最新发布
    - count: 数量，请保持默认，否则会出现BUG。
    ### 返回:
    - 话题作品数据

    # [English]
    ### Purpose:
    - Get video list of specified hashtag
    ### Parameters:
    - ch_id: Hashtag id
    - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the
    first response.
    - sort_type: 0: Comprehensive sorting 1: Most likes 2: Latest release
    - count: Number Please keep the default, otherwise there will be BUG.
    ### Return:
    - Hashtag video list data

    # [示例/Example]
    ch_id = 1575791821492238
    cursor = 0
    sort_type = 0
    count = 10

    Args:
        ch_id (str): 话题id/Hashtag id
        cursor (Union[Unset, int]): 游标/Cursor Default: 0.
        sort_type (Union[Unset, int]): 排序类型/Sort type Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        ch_id=ch_id,
        cursor=cursor,
        sort_type=sort_type,
        count=count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ch_id: str,
    cursor: Union[Unset, int] = 0,
    sort_type: Union[Unset, int] = 0,
    count: Union[Unset, int] = 10,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取指定话题的作品数据/Get video list of specified hashtag

     # [中文]
    ### 用途:
    - 获取指定话题的作品数据
    ### 参数:
    - ch_id: 话题id
    - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
    - sort_type: 0:综合排序 1:最多点赞 2:最新发布
    - count: 数量，请保持默认，否则会出现BUG。
    ### 返回:
    - 话题作品数据

    # [English]
    ### Purpose:
    - Get video list of specified hashtag
    ### Parameters:
    - ch_id: Hashtag id
    - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the
    first response.
    - sort_type: 0: Comprehensive sorting 1: Most likes 2: Latest release
    - count: Number Please keep the default, otherwise there will be BUG.
    ### Return:
    - Hashtag video list data

    # [示例/Example]
    ch_id = 1575791821492238
    cursor = 0
    sort_type = 0
    count = 10

    Args:
        ch_id (str): 话题id/Hashtag id
        cursor (Union[Unset, int]): 游标/Cursor Default: 0.
        sort_type (Union[Unset, int]): 排序类型/Sort type Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            ch_id=ch_id,
            cursor=cursor,
            sort_type=sort_type,
            count=count,
        )
    ).parsed
