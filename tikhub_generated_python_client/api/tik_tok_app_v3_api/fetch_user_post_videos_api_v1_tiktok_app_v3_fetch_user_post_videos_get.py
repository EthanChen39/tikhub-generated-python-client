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
    sec_user_id: Union[Unset, str] = "",
    unique_id: Union[Unset, str] = "",
    max_cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    sort_type: Union[Unset, int] = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["sec_user_id"] = sec_user_id

    params["unique_id"] = unique_id

    params["max_cursor"] = max_cursor

    params["count"] = count

    params["sort_type"] = sort_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/app/v3/fetch_user_post_videos",
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
    sec_user_id: Union[Unset, str] = "",
    unique_id: Union[Unset, str] = "",
    max_cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    sort_type: Union[Unset, int] = 0,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户主页作品数据/Get user homepage video data

     # [中文]
    ### 用途:
    - 获取用户主页作品数据
    ### 参数:
    - sec_user_id: 用户sec_user_id，优先使用sec_user_id获取用户作品数据，如果sec_user_id为空，则使用unique_id获取用户作品数据。
    - max_cursor: 最大游标，用于翻页，第一页为0，第二页为第一次响应中的max_cursor值。
    - count: 最大数量，建议保持默认值20。
    - sort_type: 排序类型，0-最新，1-热门
    - unique_id: 用户unique_id，可选参数，如果sec_user_id为空，则使用unique_id获取用户作品数据，unique_id也是用户的用户名。
    - 关于用户ID的参数，优先级为sec_user_id > unique_id，优先级越高速度越快，并且建议只使用sec_user_id获取用户数据。
    ### 返回:
    - 用户作品数据

    # [English]
    ### Purpose:
    - Get user homepage video data
    ### Parameters:
    - sec_user_id: User sec_user_id, use sec_user_id to get user video data first, if sec_user_id is
    empty, use unique_id to get user video data.
    - max_cursor: Maximum cursor, used for paging, the first page is 0, the second page is the
    max_cursor value in the first response.
    - count: Maximum count number
    - sort_type: Sort type, 0-Latest, 1-Hot
    - unique_id: User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user
    video data, unique_id is also the user's username.
    - About the parameters of user ID, the priority is sec_user_id > unique_id, the higher the priority,
    the faster the speed, and it is recommended to use only sec_user_id to get user data.
    ### Return:
    - User video data

    # [示例/Example]
    sec_user_id = \"MS4wLjABAAAA5u9HhzjGAj-leViCcvZD6b4-qyqHHgr9lVJmcPMzcBUX_Q2NpBeCgz8Uh6KugkfS\"
    max_cursor = 0
    counts = 20
    sort_type = 0
    unique_id = \"tiktok\"

    Args:
        sec_user_id (Union[Unset, str]): 用户sec_user_id/User sec_user_id Default: ''.
        unique_id (Union[Unset, str]): 用户unique_id/User unique_id Default: ''.
        max_cursor (Union[Unset, int]): 最大游标/Maximum cursor Default: 0.
        count (Union[Unset, int]): 每页数量/Number per page Default: 20.
        sort_type (Union[Unset, int]): 排序类型/Sort type Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        sec_user_id=sec_user_id,
        unique_id=unique_id,
        max_cursor=max_cursor,
        count=count,
        sort_type=sort_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    sec_user_id: Union[Unset, str] = "",
    unique_id: Union[Unset, str] = "",
    max_cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    sort_type: Union[Unset, int] = 0,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户主页作品数据/Get user homepage video data

     # [中文]
    ### 用途:
    - 获取用户主页作品数据
    ### 参数:
    - sec_user_id: 用户sec_user_id，优先使用sec_user_id获取用户作品数据，如果sec_user_id为空，则使用unique_id获取用户作品数据。
    - max_cursor: 最大游标，用于翻页，第一页为0，第二页为第一次响应中的max_cursor值。
    - count: 最大数量，建议保持默认值20。
    - sort_type: 排序类型，0-最新，1-热门
    - unique_id: 用户unique_id，可选参数，如果sec_user_id为空，则使用unique_id获取用户作品数据，unique_id也是用户的用户名。
    - 关于用户ID的参数，优先级为sec_user_id > unique_id，优先级越高速度越快，并且建议只使用sec_user_id获取用户数据。
    ### 返回:
    - 用户作品数据

    # [English]
    ### Purpose:
    - Get user homepage video data
    ### Parameters:
    - sec_user_id: User sec_user_id, use sec_user_id to get user video data first, if sec_user_id is
    empty, use unique_id to get user video data.
    - max_cursor: Maximum cursor, used for paging, the first page is 0, the second page is the
    max_cursor value in the first response.
    - count: Maximum count number
    - sort_type: Sort type, 0-Latest, 1-Hot
    - unique_id: User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user
    video data, unique_id is also the user's username.
    - About the parameters of user ID, the priority is sec_user_id > unique_id, the higher the priority,
    the faster the speed, and it is recommended to use only sec_user_id to get user data.
    ### Return:
    - User video data

    # [示例/Example]
    sec_user_id = \"MS4wLjABAAAA5u9HhzjGAj-leViCcvZD6b4-qyqHHgr9lVJmcPMzcBUX_Q2NpBeCgz8Uh6KugkfS\"
    max_cursor = 0
    counts = 20
    sort_type = 0
    unique_id = \"tiktok\"

    Args:
        sec_user_id (Union[Unset, str]): 用户sec_user_id/User sec_user_id Default: ''.
        unique_id (Union[Unset, str]): 用户unique_id/User unique_id Default: ''.
        max_cursor (Union[Unset, int]): 最大游标/Maximum cursor Default: 0.
        count (Union[Unset, int]): 每页数量/Number per page Default: 20.
        sort_type (Union[Unset, int]): 排序类型/Sort type Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        sec_user_id=sec_user_id,
        unique_id=unique_id,
        max_cursor=max_cursor,
        count=count,
        sort_type=sort_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    sec_user_id: Union[Unset, str] = "",
    unique_id: Union[Unset, str] = "",
    max_cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    sort_type: Union[Unset, int] = 0,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户主页作品数据/Get user homepage video data

     # [中文]
    ### 用途:
    - 获取用户主页作品数据
    ### 参数:
    - sec_user_id: 用户sec_user_id，优先使用sec_user_id获取用户作品数据，如果sec_user_id为空，则使用unique_id获取用户作品数据。
    - max_cursor: 最大游标，用于翻页，第一页为0，第二页为第一次响应中的max_cursor值。
    - count: 最大数量，建议保持默认值20。
    - sort_type: 排序类型，0-最新，1-热门
    - unique_id: 用户unique_id，可选参数，如果sec_user_id为空，则使用unique_id获取用户作品数据，unique_id也是用户的用户名。
    - 关于用户ID的参数，优先级为sec_user_id > unique_id，优先级越高速度越快，并且建议只使用sec_user_id获取用户数据。
    ### 返回:
    - 用户作品数据

    # [English]
    ### Purpose:
    - Get user homepage video data
    ### Parameters:
    - sec_user_id: User sec_user_id, use sec_user_id to get user video data first, if sec_user_id is
    empty, use unique_id to get user video data.
    - max_cursor: Maximum cursor, used for paging, the first page is 0, the second page is the
    max_cursor value in the first response.
    - count: Maximum count number
    - sort_type: Sort type, 0-Latest, 1-Hot
    - unique_id: User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user
    video data, unique_id is also the user's username.
    - About the parameters of user ID, the priority is sec_user_id > unique_id, the higher the priority,
    the faster the speed, and it is recommended to use only sec_user_id to get user data.
    ### Return:
    - User video data

    # [示例/Example]
    sec_user_id = \"MS4wLjABAAAA5u9HhzjGAj-leViCcvZD6b4-qyqHHgr9lVJmcPMzcBUX_Q2NpBeCgz8Uh6KugkfS\"
    max_cursor = 0
    counts = 20
    sort_type = 0
    unique_id = \"tiktok\"

    Args:
        sec_user_id (Union[Unset, str]): 用户sec_user_id/User sec_user_id Default: ''.
        unique_id (Union[Unset, str]): 用户unique_id/User unique_id Default: ''.
        max_cursor (Union[Unset, int]): 最大游标/Maximum cursor Default: 0.
        count (Union[Unset, int]): 每页数量/Number per page Default: 20.
        sort_type (Union[Unset, int]): 排序类型/Sort type Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        sec_user_id=sec_user_id,
        unique_id=unique_id,
        max_cursor=max_cursor,
        count=count,
        sort_type=sort_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    sec_user_id: Union[Unset, str] = "",
    unique_id: Union[Unset, str] = "",
    max_cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    sort_type: Union[Unset, int] = 0,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户主页作品数据/Get user homepage video data

     # [中文]
    ### 用途:
    - 获取用户主页作品数据
    ### 参数:
    - sec_user_id: 用户sec_user_id，优先使用sec_user_id获取用户作品数据，如果sec_user_id为空，则使用unique_id获取用户作品数据。
    - max_cursor: 最大游标，用于翻页，第一页为0，第二页为第一次响应中的max_cursor值。
    - count: 最大数量，建议保持默认值20。
    - sort_type: 排序类型，0-最新，1-热门
    - unique_id: 用户unique_id，可选参数，如果sec_user_id为空，则使用unique_id获取用户作品数据，unique_id也是用户的用户名。
    - 关于用户ID的参数，优先级为sec_user_id > unique_id，优先级越高速度越快，并且建议只使用sec_user_id获取用户数据。
    ### 返回:
    - 用户作品数据

    # [English]
    ### Purpose:
    - Get user homepage video data
    ### Parameters:
    - sec_user_id: User sec_user_id, use sec_user_id to get user video data first, if sec_user_id is
    empty, use unique_id to get user video data.
    - max_cursor: Maximum cursor, used for paging, the first page is 0, the second page is the
    max_cursor value in the first response.
    - count: Maximum count number
    - sort_type: Sort type, 0-Latest, 1-Hot
    - unique_id: User unique_id, optional parameter, if sec_user_id is empty, use unique_id to get user
    video data, unique_id is also the user's username.
    - About the parameters of user ID, the priority is sec_user_id > unique_id, the higher the priority,
    the faster the speed, and it is recommended to use only sec_user_id to get user data.
    ### Return:
    - User video data

    # [示例/Example]
    sec_user_id = \"MS4wLjABAAAA5u9HhzjGAj-leViCcvZD6b4-qyqHHgr9lVJmcPMzcBUX_Q2NpBeCgz8Uh6KugkfS\"
    max_cursor = 0
    counts = 20
    sort_type = 0
    unique_id = \"tiktok\"

    Args:
        sec_user_id (Union[Unset, str]): 用户sec_user_id/User sec_user_id Default: ''.
        unique_id (Union[Unset, str]): 用户unique_id/User unique_id Default: ''.
        max_cursor (Union[Unset, int]): 最大游标/Maximum cursor Default: 0.
        count (Union[Unset, int]): 每页数量/Number per page Default: 20.
        sort_type (Union[Unset, int]): 排序类型/Sort type Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            sec_user_id=sec_user_id,
            unique_id=unique_id,
            max_cursor=max_cursor,
            count=count,
            sort_type=sort_type,
        )
    ).parsed
