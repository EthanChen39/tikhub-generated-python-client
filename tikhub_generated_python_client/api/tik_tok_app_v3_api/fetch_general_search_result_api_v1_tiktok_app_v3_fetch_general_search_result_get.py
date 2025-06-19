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
    keyword: str,
    offset: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    sort_type: Union[Unset, int] = 0,
    publish_time: Union[Unset, int] = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["offset"] = offset

    params["count"] = count

    params["sort_type"] = sort_type

    params["publish_time"] = publish_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/app/v3/fetch_general_search_result",
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
    offset: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    sort_type: Union[Unset, int] = 0,
    publish_time: Union[Unset, int] = 0,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的综合搜索结果/Get comprehensive search results of specified keywords

     # [中文]
    ### 用途:
    - 获取指定关键词的综合搜索结果
    ### 参数:
    - keyword: 关键词
    - offset: 偏移量
    - count: 数量
    - sort_type: 0-相关度，1-最多点赞
    - publish_time: 0-不限制，1-最近一天，7-最近一周，30-最近一个月，90-最近三个月，180-最近半年
    ### 返回:
    - 综合搜索结果

    # [English]
    ### Purpose:
    - Get comprehensive search results of specified keywords
    ### Parameters:
    - keyword: Keyword
    - offset: Offset
    - count: Number
    - sort_type: 0-Relatedness, 1-Most likes
    - publish_time: 0-Unlimited, 1-Last day, 7-Last week, 30-Last month, 90-Last three months, 180-Last
    half year
    ### Return:
    - Comprehensive search results

    # [示例/Example]
    keyword = \"中华娘\"
    offset = 0
    count = 20
    sort_type = 0
    publish_time = 0

    Args:
        keyword (str): 关键词/Keyword
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.
        sort_type (Union[Unset, int]): 排序类型/Sort type Default: 0.
        publish_time (Union[Unset, int]): 发布时间/Publish time Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        offset=offset,
        count=count,
        sort_type=sort_type,
        publish_time=publish_time,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    keyword: str,
    offset: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    sort_type: Union[Unset, int] = 0,
    publish_time: Union[Unset, int] = 0,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的综合搜索结果/Get comprehensive search results of specified keywords

     # [中文]
    ### 用途:
    - 获取指定关键词的综合搜索结果
    ### 参数:
    - keyword: 关键词
    - offset: 偏移量
    - count: 数量
    - sort_type: 0-相关度，1-最多点赞
    - publish_time: 0-不限制，1-最近一天，7-最近一周，30-最近一个月，90-最近三个月，180-最近半年
    ### 返回:
    - 综合搜索结果

    # [English]
    ### Purpose:
    - Get comprehensive search results of specified keywords
    ### Parameters:
    - keyword: Keyword
    - offset: Offset
    - count: Number
    - sort_type: 0-Relatedness, 1-Most likes
    - publish_time: 0-Unlimited, 1-Last day, 7-Last week, 30-Last month, 90-Last three months, 180-Last
    half year
    ### Return:
    - Comprehensive search results

    # [示例/Example]
    keyword = \"中华娘\"
    offset = 0
    count = 20
    sort_type = 0
    publish_time = 0

    Args:
        keyword (str): 关键词/Keyword
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.
        sort_type (Union[Unset, int]): 排序类型/Sort type Default: 0.
        publish_time (Union[Unset, int]): 发布时间/Publish time Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        keyword=keyword,
        offset=offset,
        count=count,
        sort_type=sort_type,
        publish_time=publish_time,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    offset: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    sort_type: Union[Unset, int] = 0,
    publish_time: Union[Unset, int] = 0,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的综合搜索结果/Get comprehensive search results of specified keywords

     # [中文]
    ### 用途:
    - 获取指定关键词的综合搜索结果
    ### 参数:
    - keyword: 关键词
    - offset: 偏移量
    - count: 数量
    - sort_type: 0-相关度，1-最多点赞
    - publish_time: 0-不限制，1-最近一天，7-最近一周，30-最近一个月，90-最近三个月，180-最近半年
    ### 返回:
    - 综合搜索结果

    # [English]
    ### Purpose:
    - Get comprehensive search results of specified keywords
    ### Parameters:
    - keyword: Keyword
    - offset: Offset
    - count: Number
    - sort_type: 0-Relatedness, 1-Most likes
    - publish_time: 0-Unlimited, 1-Last day, 7-Last week, 30-Last month, 90-Last three months, 180-Last
    half year
    ### Return:
    - Comprehensive search results

    # [示例/Example]
    keyword = \"中华娘\"
    offset = 0
    count = 20
    sort_type = 0
    publish_time = 0

    Args:
        keyword (str): 关键词/Keyword
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.
        sort_type (Union[Unset, int]): 排序类型/Sort type Default: 0.
        publish_time (Union[Unset, int]): 发布时间/Publish time Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        offset=offset,
        count=count,
        sort_type=sort_type,
        publish_time=publish_time,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
    offset: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
    sort_type: Union[Unset, int] = 0,
    publish_time: Union[Unset, int] = 0,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的综合搜索结果/Get comprehensive search results of specified keywords

     # [中文]
    ### 用途:
    - 获取指定关键词的综合搜索结果
    ### 参数:
    - keyword: 关键词
    - offset: 偏移量
    - count: 数量
    - sort_type: 0-相关度，1-最多点赞
    - publish_time: 0-不限制，1-最近一天，7-最近一周，30-最近一个月，90-最近三个月，180-最近半年
    ### 返回:
    - 综合搜索结果

    # [English]
    ### Purpose:
    - Get comprehensive search results of specified keywords
    ### Parameters:
    - keyword: Keyword
    - offset: Offset
    - count: Number
    - sort_type: 0-Relatedness, 1-Most likes
    - publish_time: 0-Unlimited, 1-Last day, 7-Last week, 30-Last month, 90-Last three months, 180-Last
    half year
    ### Return:
    - Comprehensive search results

    # [示例/Example]
    keyword = \"中华娘\"
    offset = 0
    count = 20
    sort_type = 0
    publish_time = 0

    Args:
        keyword (str): 关键词/Keyword
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.
        sort_type (Union[Unset, int]): 排序类型/Sort type Default: 0.
        publish_time (Union[Unset, int]): 发布时间/Publish time Default: 0.

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
            offset=offset,
            count=count,
            sort_type=sort_type,
            publish_time=publish_time,
        )
    ).parsed
