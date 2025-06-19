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
    keyword: str,
    cursor: int,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/billboard/fetch_hot_account_search_list",
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
    keyword: str,
    cursor: int,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """搜索用户名或抖音号/Fetch account search list

     # [中文]
    ### 用途:
    - 获取搜索用户名或抖音号
    ### 参数:
    - keyword: 搜索的用户名或抖音号
    - cursor: 游标，默认空
    ### 返回:
    - 搜索结果

    # [English]
    ### Purpose:
    - Get the search username or Douyin number
    ### Parameters:
    - keyword: Search username or Douyin number
    - cursor: Cursor, default empty
    ### Return:
    - Search result

    Args:
        keyword (str): 搜索的用户名或抖音号
        cursor (int): 游标，默认空

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    keyword: str,
    cursor: int,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """搜索用户名或抖音号/Fetch account search list

     # [中文]
    ### 用途:
    - 获取搜索用户名或抖音号
    ### 参数:
    - keyword: 搜索的用户名或抖音号
    - cursor: 游标，默认空
    ### 返回:
    - 搜索结果

    # [English]
    ### Purpose:
    - Get the search username or Douyin number
    ### Parameters:
    - keyword: Search username or Douyin number
    - cursor: Cursor, default empty
    ### Return:
    - Search result

    Args:
        keyword (str): 搜索的用户名或抖音号
        cursor (int): 游标，默认空

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        keyword=keyword,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    cursor: int,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """搜索用户名或抖音号/Fetch account search list

     # [中文]
    ### 用途:
    - 获取搜索用户名或抖音号
    ### 参数:
    - keyword: 搜索的用户名或抖音号
    - cursor: 游标，默认空
    ### 返回:
    - 搜索结果

    # [English]
    ### Purpose:
    - Get the search username or Douyin number
    ### Parameters:
    - keyword: Search username or Douyin number
    - cursor: Cursor, default empty
    ### Return:
    - Search result

    Args:
        keyword (str): 搜索的用户名或抖音号
        cursor (int): 游标，默认空

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
    cursor: int,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """搜索用户名或抖音号/Fetch account search list

     # [中文]
    ### 用途:
    - 获取搜索用户名或抖音号
    ### 参数:
    - keyword: 搜索的用户名或抖音号
    - cursor: 游标，默认空
    ### 返回:
    - 搜索结果

    # [English]
    ### Purpose:
    - Get the search username or Douyin number
    ### Parameters:
    - keyword: Search username or Douyin number
    - cursor: Cursor, default empty
    ### Return:
    - Search result

    Args:
        keyword (str): 搜索的用户名或抖音号
        cursor (int): 游标，默认空

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            keyword=keyword,
            cursor=cursor,
        )
    ).parsed
