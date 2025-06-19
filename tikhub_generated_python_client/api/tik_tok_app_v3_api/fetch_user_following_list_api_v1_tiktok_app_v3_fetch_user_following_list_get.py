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
    sec_user_id: str,
    count: Union[Unset, int] = 20,
    min_time: Union[Unset, int] = 0,
    page_token: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["sec_user_id"] = sec_user_id

    params["count"] = count

    params["min_time"] = min_time

    params["page_token"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/app/v3/fetch_user_following_list",
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
    sec_user_id: str,
    count: Union[Unset, int] = 20,
    min_time: Union[Unset, int] = 0,
    page_token: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定用户的关注列表数据/Get following list of specified user

     # [中文]
    ### 用途:
    - 获取指定用户的关注列表数据
    ### 参数:
    - sec_user_id: 用户sec_user_id
    - count: 数量
    - min_time: 最小时间，用于翻页，第一次请求使用默认值0，后续请求使用上一次请求返回的min_time值。
    - page_token: 翻页token，第一次请求使用默认值\"\"，后续请求使用上一次请求返回的page_token值。
    ### 返回:
    - 关注列表数据

    # [English]
    ### Purpose:
    - Get following list of specified user
    ### Parameters:
    - sec_user_id: User sec_user_id
    - count: Number
    - min_time: Minimum time for paging, use default value 0 for the first request, and use the min_time
    value returned by the last request for subsequent requests.
    - page_token: Page token, use default value \"\" for the first request, and use the page_token value
    returned by the last request for subsequent requests.
    ### Return:
    - Following list data

    # [示例/Example]
    sec_user = \"MS4wLjABAAAAXqqA-cLDC0hfQPIrS5APYNsg04zkl-socWCkqkI3UIOaEe6_Qnokg0GcWpLnMNQP\"
    count = 20
    min_time = 1639642146
    page_token = \"eyJtYXhfY3Vyc29yIjoxNzE4NzIzNTY0LCJtaW5fY3Vyc29yIjoxNjM5NjQyMTQ2LCJmaW5pc2hfaW5zZXJ0X
    21hZiI6dHJ1ZX0=\"

    Args:
        sec_user_id (str): 用户sec_user_id/User sec_user_id
        count (Union[Unset, int]): 数量/Number Default: 20.
        min_time (Union[Unset, int]): 最小时间，用于翻页/Minimum time for paging Default: 0.
        page_token (Union[Unset, str]): 翻页token/Page token Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        sec_user_id=sec_user_id,
        count=count,
        min_time=min_time,
        page_token=page_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    sec_user_id: str,
    count: Union[Unset, int] = 20,
    min_time: Union[Unset, int] = 0,
    page_token: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定用户的关注列表数据/Get following list of specified user

     # [中文]
    ### 用途:
    - 获取指定用户的关注列表数据
    ### 参数:
    - sec_user_id: 用户sec_user_id
    - count: 数量
    - min_time: 最小时间，用于翻页，第一次请求使用默认值0，后续请求使用上一次请求返回的min_time值。
    - page_token: 翻页token，第一次请求使用默认值\"\"，后续请求使用上一次请求返回的page_token值。
    ### 返回:
    - 关注列表数据

    # [English]
    ### Purpose:
    - Get following list of specified user
    ### Parameters:
    - sec_user_id: User sec_user_id
    - count: Number
    - min_time: Minimum time for paging, use default value 0 for the first request, and use the min_time
    value returned by the last request for subsequent requests.
    - page_token: Page token, use default value \"\" for the first request, and use the page_token value
    returned by the last request for subsequent requests.
    ### Return:
    - Following list data

    # [示例/Example]
    sec_user = \"MS4wLjABAAAAXqqA-cLDC0hfQPIrS5APYNsg04zkl-socWCkqkI3UIOaEe6_Qnokg0GcWpLnMNQP\"
    count = 20
    min_time = 1639642146
    page_token = \"eyJtYXhfY3Vyc29yIjoxNzE4NzIzNTY0LCJtaW5fY3Vyc29yIjoxNjM5NjQyMTQ2LCJmaW5pc2hfaW5zZXJ0X
    21hZiI6dHJ1ZX0=\"

    Args:
        sec_user_id (str): 用户sec_user_id/User sec_user_id
        count (Union[Unset, int]): 数量/Number Default: 20.
        min_time (Union[Unset, int]): 最小时间，用于翻页/Minimum time for paging Default: 0.
        page_token (Union[Unset, str]): 翻页token/Page token Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        sec_user_id=sec_user_id,
        count=count,
        min_time=min_time,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    sec_user_id: str,
    count: Union[Unset, int] = 20,
    min_time: Union[Unset, int] = 0,
    page_token: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定用户的关注列表数据/Get following list of specified user

     # [中文]
    ### 用途:
    - 获取指定用户的关注列表数据
    ### 参数:
    - sec_user_id: 用户sec_user_id
    - count: 数量
    - min_time: 最小时间，用于翻页，第一次请求使用默认值0，后续请求使用上一次请求返回的min_time值。
    - page_token: 翻页token，第一次请求使用默认值\"\"，后续请求使用上一次请求返回的page_token值。
    ### 返回:
    - 关注列表数据

    # [English]
    ### Purpose:
    - Get following list of specified user
    ### Parameters:
    - sec_user_id: User sec_user_id
    - count: Number
    - min_time: Minimum time for paging, use default value 0 for the first request, and use the min_time
    value returned by the last request for subsequent requests.
    - page_token: Page token, use default value \"\" for the first request, and use the page_token value
    returned by the last request for subsequent requests.
    ### Return:
    - Following list data

    # [示例/Example]
    sec_user = \"MS4wLjABAAAAXqqA-cLDC0hfQPIrS5APYNsg04zkl-socWCkqkI3UIOaEe6_Qnokg0GcWpLnMNQP\"
    count = 20
    min_time = 1639642146
    page_token = \"eyJtYXhfY3Vyc29yIjoxNzE4NzIzNTY0LCJtaW5fY3Vyc29yIjoxNjM5NjQyMTQ2LCJmaW5pc2hfaW5zZXJ0X
    21hZiI6dHJ1ZX0=\"

    Args:
        sec_user_id (str): 用户sec_user_id/User sec_user_id
        count (Union[Unset, int]): 数量/Number Default: 20.
        min_time (Union[Unset, int]): 最小时间，用于翻页/Minimum time for paging Default: 0.
        page_token (Union[Unset, str]): 翻页token/Page token Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        sec_user_id=sec_user_id,
        count=count,
        min_time=min_time,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    sec_user_id: str,
    count: Union[Unset, int] = 20,
    min_time: Union[Unset, int] = 0,
    page_token: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定用户的关注列表数据/Get following list of specified user

     # [中文]
    ### 用途:
    - 获取指定用户的关注列表数据
    ### 参数:
    - sec_user_id: 用户sec_user_id
    - count: 数量
    - min_time: 最小时间，用于翻页，第一次请求使用默认值0，后续请求使用上一次请求返回的min_time值。
    - page_token: 翻页token，第一次请求使用默认值\"\"，后续请求使用上一次请求返回的page_token值。
    ### 返回:
    - 关注列表数据

    # [English]
    ### Purpose:
    - Get following list of specified user
    ### Parameters:
    - sec_user_id: User sec_user_id
    - count: Number
    - min_time: Minimum time for paging, use default value 0 for the first request, and use the min_time
    value returned by the last request for subsequent requests.
    - page_token: Page token, use default value \"\" for the first request, and use the page_token value
    returned by the last request for subsequent requests.
    ### Return:
    - Following list data

    # [示例/Example]
    sec_user = \"MS4wLjABAAAAXqqA-cLDC0hfQPIrS5APYNsg04zkl-socWCkqkI3UIOaEe6_Qnokg0GcWpLnMNQP\"
    count = 20
    min_time = 1639642146
    page_token = \"eyJtYXhfY3Vyc29yIjoxNzE4NzIzNTY0LCJtaW5fY3Vyc29yIjoxNjM5NjQyMTQ2LCJmaW5pc2hfaW5zZXJ0X
    21hZiI6dHJ1ZX0=\"

    Args:
        sec_user_id (str): 用户sec_user_id/User sec_user_id
        count (Union[Unset, int]): 数量/Number Default: 20.
        min_time (Union[Unset, int]): 最小时间，用于翻页/Minimum time for paging Default: 0.
        page_token (Union[Unset, str]): 翻页token/Page token Default: ''.

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
            count=count,
            min_time=min_time,
            page_token=page_token,
        )
    ).parsed
