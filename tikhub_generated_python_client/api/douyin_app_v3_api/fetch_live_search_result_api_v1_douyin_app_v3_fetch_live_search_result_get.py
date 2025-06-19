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
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["cursor"] = cursor

    params["count"] = count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/app/v3/fetch_live_search_result",
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
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的直播搜索结果（弃用，替代接口见下方文档说明）/Get live search results of specified keywords (deprecated, see the
    documentation below for alternative interfaces)

     # [中文]
    ### 用途:
    - 获取指定关键词的直播搜索结果
    - 该接口已弃用，替代接口为：https://api.tikhub.io/#/Douyin-Search-API
    ### 参数:
    - keyword: 关键词
    - cursor: 偏移量，从0开始，每次请求从上次请求返回响应中的cursor中获取。
    - count: 数量，请保持默认，否则会出现BUG。
    ### 返回:
    - 直播搜索结果

    # [English]
    ### Purpose:
    - Get live search results of specified keywords
    - This interface has been deprecated, and the alternative interface is:
    https://api.tikhub.io/#/Douyin-Search-API
    ### Parameters:
    - keyword: Keyword
    - cursor: Offset, starting from 0, each request gets from the cursor in the response returned by the
    last request.
    - count: Number Please keep the default, otherwise there will be BUG.
    ### Return:
    - Live search results

    # [示例/Example]
    keyword = \"小米商城\"
    cursor = 0
    count = 20

    Args:
        keyword (str): 关键词/Keyword
        cursor (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
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
    keyword: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的直播搜索结果（弃用，替代接口见下方文档说明）/Get live search results of specified keywords (deprecated, see the
    documentation below for alternative interfaces)

     # [中文]
    ### 用途:
    - 获取指定关键词的直播搜索结果
    - 该接口已弃用，替代接口为：https://api.tikhub.io/#/Douyin-Search-API
    ### 参数:
    - keyword: 关键词
    - cursor: 偏移量，从0开始，每次请求从上次请求返回响应中的cursor中获取。
    - count: 数量，请保持默认，否则会出现BUG。
    ### 返回:
    - 直播搜索结果

    # [English]
    ### Purpose:
    - Get live search results of specified keywords
    - This interface has been deprecated, and the alternative interface is:
    https://api.tikhub.io/#/Douyin-Search-API
    ### Parameters:
    - keyword: Keyword
    - cursor: Offset, starting from 0, each request gets from the cursor in the response returned by the
    last request.
    - count: Number Please keep the default, otherwise there will be BUG.
    ### Return:
    - Live search results

    # [示例/Example]
    keyword = \"小米商城\"
    cursor = 0
    count = 20

    Args:
        keyword (str): 关键词/Keyword
        cursor (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.

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
        count=count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的直播搜索结果（弃用，替代接口见下方文档说明）/Get live search results of specified keywords (deprecated, see the
    documentation below for alternative interfaces)

     # [中文]
    ### 用途:
    - 获取指定关键词的直播搜索结果
    - 该接口已弃用，替代接口为：https://api.tikhub.io/#/Douyin-Search-API
    ### 参数:
    - keyword: 关键词
    - cursor: 偏移量，从0开始，每次请求从上次请求返回响应中的cursor中获取。
    - count: 数量，请保持默认，否则会出现BUG。
    ### 返回:
    - 直播搜索结果

    # [English]
    ### Purpose:
    - Get live search results of specified keywords
    - This interface has been deprecated, and the alternative interface is:
    https://api.tikhub.io/#/Douyin-Search-API
    ### Parameters:
    - keyword: Keyword
    - cursor: Offset, starting from 0, each request gets from the cursor in the response returned by the
    last request.
    - count: Number Please keep the default, otherwise there will be BUG.
    ### Return:
    - Live search results

    # [示例/Example]
    keyword = \"小米商城\"
    cursor = 0
    count = 20

    Args:
        keyword (str): 关键词/Keyword
        cursor (Union[Unset, int]): 偏移量/Offset Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        cursor=cursor,
        count=count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 20,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的直播搜索结果（弃用，替代接口见下方文档说明）/Get live search results of specified keywords (deprecated, see the
    documentation below for alternative interfaces)

     # [中文]
    ### 用途:
    - 获取指定关键词的直播搜索结果
    - 该接口已弃用，替代接口为：https://api.tikhub.io/#/Douyin-Search-API
    ### 参数:
    - keyword: 关键词
    - cursor: 偏移量，从0开始，每次请求从上次请求返回响应中的cursor中获取。
    - count: 数量，请保持默认，否则会出现BUG。
    ### 返回:
    - 直播搜索结果

    # [English]
    ### Purpose:
    - Get live search results of specified keywords
    - This interface has been deprecated, and the alternative interface is:
    https://api.tikhub.io/#/Douyin-Search-API
    ### Parameters:
    - keyword: Keyword
    - cursor: Offset, starting from 0, each request gets from the cursor in the response returned by the
    last request.
    - count: Number Please keep the default, otherwise there will be BUG.
    ### Return:
    - Live search results

    # [示例/Example]
    keyword = \"小米商城\"
    cursor = 0
    count = 20

    Args:
        keyword (str): 关键词/Keyword
        cursor (Union[Unset, int]): 偏移量/Offset Default: 0.
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
            keyword=keyword,
            cursor=cursor,
            count=count,
        )
    ).parsed
