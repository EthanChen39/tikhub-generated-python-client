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
    word_id: str,
    query_day: int,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["word_id"] = word_id

    params["query_day"] = query_day

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/billboard/fetch_hot_total_hot_word_detail_list",
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
    word_id: str,
    query_day: int,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取内容词详情/Fetch content word details

     # [中文]
    ### 用途:
    - 获取内容词详情
    ### 参数:
    - keyword: 搜索关键字
    - word_id: 内容词id
    - query_day: 查询日期，格式为YYYYMMDD
    ### 返回:
    - 内容词详情

    # [English]
    ### Purpose:
    - Get the details of content words
    ### Parameters:
    - keyword: Search keyword
    - word_id: Content word id
    - query_day: Query date, format is YYYYMMDD
    ### Return:
    - Details of content words

    Args:
        keyword (str): 搜索关键字
        word_id (str): 内容词id
        query_day (int): 查询日期，格式为YYYYMMDD，需为当日

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        word_id=word_id,
        query_day=query_day,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    keyword: str,
    word_id: str,
    query_day: int,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取内容词详情/Fetch content word details

     # [中文]
    ### 用途:
    - 获取内容词详情
    ### 参数:
    - keyword: 搜索关键字
    - word_id: 内容词id
    - query_day: 查询日期，格式为YYYYMMDD
    ### 返回:
    - 内容词详情

    # [English]
    ### Purpose:
    - Get the details of content words
    ### Parameters:
    - keyword: Search keyword
    - word_id: Content word id
    - query_day: Query date, format is YYYYMMDD
    ### Return:
    - Details of content words

    Args:
        keyword (str): 搜索关键字
        word_id (str): 内容词id
        query_day (int): 查询日期，格式为YYYYMMDD，需为当日

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        keyword=keyword,
        word_id=word_id,
        query_day=query_day,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    word_id: str,
    query_day: int,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取内容词详情/Fetch content word details

     # [中文]
    ### 用途:
    - 获取内容词详情
    ### 参数:
    - keyword: 搜索关键字
    - word_id: 内容词id
    - query_day: 查询日期，格式为YYYYMMDD
    ### 返回:
    - 内容词详情

    # [English]
    ### Purpose:
    - Get the details of content words
    ### Parameters:
    - keyword: Search keyword
    - word_id: Content word id
    - query_day: Query date, format is YYYYMMDD
    ### Return:
    - Details of content words

    Args:
        keyword (str): 搜索关键字
        word_id (str): 内容词id
        query_day (int): 查询日期，格式为YYYYMMDD，需为当日

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        word_id=word_id,
        query_day=query_day,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
    word_id: str,
    query_day: int,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取内容词详情/Fetch content word details

     # [中文]
    ### 用途:
    - 获取内容词详情
    ### 参数:
    - keyword: 搜索关键字
    - word_id: 内容词id
    - query_day: 查询日期，格式为YYYYMMDD
    ### 返回:
    - 内容词详情

    # [English]
    ### Purpose:
    - Get the details of content words
    ### Parameters:
    - keyword: Search keyword
    - word_id: Content word id
    - query_day: Query date, format is YYYYMMDD
    ### Return:
    - Details of content words

    Args:
        keyword (str): 搜索关键字
        word_id (str): 内容词id
        query_day (int): 查询日期，格式为YYYYMMDD，需为当日

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
            word_id=word_id,
            query_day=query_day,
        )
    ).parsed
