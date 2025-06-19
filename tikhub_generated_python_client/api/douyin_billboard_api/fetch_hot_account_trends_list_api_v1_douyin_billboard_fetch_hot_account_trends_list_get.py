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
    sec_uid: str,
    option: str,
    date_window: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["sec_uid"] = sec_uid

    params["option"] = option

    params["date_window"] = date_window

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/billboard/fetch_hot_account_trends_list",
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
    option: str,
    date_window: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取账号粉丝数据趋势/Fetch account fan data trend

     # [中文]
    ### 用途:
    - 获取账号粉丝数据趋势
    ### 参数:
    - sec_uid: 用户sec_id
    - option: 选项，2 新增点赞量 3 新增作品量 4 新增评论量 5 新增分享量
    - date_window: 时间窗口，1 按小时 2 按天
    ### 返回:
    - 账号粉丝数据趋势

    # [English]
    ### Purpose:
    - Get the account fan data trend
    ### Parameters:
    - sec_uid: User sec_id
    - option: Option, 2 New like 3 New work 4 New comment 5 New share
    - date_window: Time window, 1 by hour 2 by day
    ### Return:
    - Account fan data trend

    Args:
        sec_uid (str): 用户sec_id
        option (str): 选项，2 新增点赞量 3 新增作品量 4 新增评论量 5 新增分享量
        date_window (str): 时间窗口，1 按小时 2 按天

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        sec_uid=sec_uid,
        option=option,
        date_window=date_window,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    sec_uid: str,
    option: str,
    date_window: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取账号粉丝数据趋势/Fetch account fan data trend

     # [中文]
    ### 用途:
    - 获取账号粉丝数据趋势
    ### 参数:
    - sec_uid: 用户sec_id
    - option: 选项，2 新增点赞量 3 新增作品量 4 新增评论量 5 新增分享量
    - date_window: 时间窗口，1 按小时 2 按天
    ### 返回:
    - 账号粉丝数据趋势

    # [English]
    ### Purpose:
    - Get the account fan data trend
    ### Parameters:
    - sec_uid: User sec_id
    - option: Option, 2 New like 3 New work 4 New comment 5 New share
    - date_window: Time window, 1 by hour 2 by day
    ### Return:
    - Account fan data trend

    Args:
        sec_uid (str): 用户sec_id
        option (str): 选项，2 新增点赞量 3 新增作品量 4 新增评论量 5 新增分享量
        date_window (str): 时间窗口，1 按小时 2 按天

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        sec_uid=sec_uid,
        option=option,
        date_window=date_window,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    sec_uid: str,
    option: str,
    date_window: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取账号粉丝数据趋势/Fetch account fan data trend

     # [中文]
    ### 用途:
    - 获取账号粉丝数据趋势
    ### 参数:
    - sec_uid: 用户sec_id
    - option: 选项，2 新增点赞量 3 新增作品量 4 新增评论量 5 新增分享量
    - date_window: 时间窗口，1 按小时 2 按天
    ### 返回:
    - 账号粉丝数据趋势

    # [English]
    ### Purpose:
    - Get the account fan data trend
    ### Parameters:
    - sec_uid: User sec_id
    - option: Option, 2 New like 3 New work 4 New comment 5 New share
    - date_window: Time window, 1 by hour 2 by day
    ### Return:
    - Account fan data trend

    Args:
        sec_uid (str): 用户sec_id
        option (str): 选项，2 新增点赞量 3 新增作品量 4 新增评论量 5 新增分享量
        date_window (str): 时间窗口，1 按小时 2 按天

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        sec_uid=sec_uid,
        option=option,
        date_window=date_window,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    sec_uid: str,
    option: str,
    date_window: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取账号粉丝数据趋势/Fetch account fan data trend

     # [中文]
    ### 用途:
    - 获取账号粉丝数据趋势
    ### 参数:
    - sec_uid: 用户sec_id
    - option: 选项，2 新增点赞量 3 新增作品量 4 新增评论量 5 新增分享量
    - date_window: 时间窗口，1 按小时 2 按天
    ### 返回:
    - 账号粉丝数据趋势

    # [English]
    ### Purpose:
    - Get the account fan data trend
    ### Parameters:
    - sec_uid: User sec_id
    - option: Option, 2 New like 3 New work 4 New comment 5 New share
    - date_window: Time window, 1 by hour 2 by day
    ### Return:
    - Account fan data trend

    Args:
        sec_uid (str): 用户sec_id
        option (str): 选项，2 新增点赞量 3 新增作品量 4 新增评论量 5 新增分享量
        date_window (str): 时间窗口，1 按小时 2 按天

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
            option=option,
            date_window=date_window,
        )
    ).parsed
