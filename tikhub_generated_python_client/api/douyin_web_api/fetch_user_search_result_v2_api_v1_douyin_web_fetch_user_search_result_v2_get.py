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
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/web/fetch_user_search_result_v2",
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
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的用户搜索结果 V2 (已弃用，替代接口请参考下方文档)/Get user search results of specified keywords V2 (deprecated,
    please refer to the following document for replacement interface)

     # [中文]
    ### 用途:
    - 获取指定关键词的用户搜索结果V2
    - 推荐默认使用专门的搜索接口，稳定性更好：https://api.tikhub.io/#/Douyin-Search-API
    ### 参数:
    - keyword: 关键词
    - cursor: 游标，第一次请求时为0，后续从返回数据中获取，用于翻页。
    ### 返回:
    - 用户搜索结果V2

    # [English]
    ### Purpose:
    - Get user search results of specified keywords V2
    - It is recommended to use the dedicated search interface by default, which is more stable:
    https://api.tikhub.io/#/Douyin-Search-API
    ### Parameters:
    - keyword: Keyword
    - cursor: Cursor, 0 for the first request, get from the returned data later, used for paging.
    ### Return:
    - User search results V2

    # [示例/Example]
    keyword = \"中华娘\"
    cursor = 0

    Args:
        keyword (str): 关键词/Keyword
        cursor (Union[Unset, int]): 游标/Cursor Default: 0.

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
    cursor: Union[Unset, int] = 0,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的用户搜索结果 V2 (已弃用，替代接口请参考下方文档)/Get user search results of specified keywords V2 (deprecated,
    please refer to the following document for replacement interface)

     # [中文]
    ### 用途:
    - 获取指定关键词的用户搜索结果V2
    - 推荐默认使用专门的搜索接口，稳定性更好：https://api.tikhub.io/#/Douyin-Search-API
    ### 参数:
    - keyword: 关键词
    - cursor: 游标，第一次请求时为0，后续从返回数据中获取，用于翻页。
    ### 返回:
    - 用户搜索结果V2

    # [English]
    ### Purpose:
    - Get user search results of specified keywords V2
    - It is recommended to use the dedicated search interface by default, which is more stable:
    https://api.tikhub.io/#/Douyin-Search-API
    ### Parameters:
    - keyword: Keyword
    - cursor: Cursor, 0 for the first request, get from the returned data later, used for paging.
    ### Return:
    - User search results V2

    # [示例/Example]
    keyword = \"中华娘\"
    cursor = 0

    Args:
        keyword (str): 关键词/Keyword
        cursor (Union[Unset, int]): 游标/Cursor Default: 0.

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
    cursor: Union[Unset, int] = 0,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的用户搜索结果 V2 (已弃用，替代接口请参考下方文档)/Get user search results of specified keywords V2 (deprecated,
    please refer to the following document for replacement interface)

     # [中文]
    ### 用途:
    - 获取指定关键词的用户搜索结果V2
    - 推荐默认使用专门的搜索接口，稳定性更好：https://api.tikhub.io/#/Douyin-Search-API
    ### 参数:
    - keyword: 关键词
    - cursor: 游标，第一次请求时为0，后续从返回数据中获取，用于翻页。
    ### 返回:
    - 用户搜索结果V2

    # [English]
    ### Purpose:
    - Get user search results of specified keywords V2
    - It is recommended to use the dedicated search interface by default, which is more stable:
    https://api.tikhub.io/#/Douyin-Search-API
    ### Parameters:
    - keyword: Keyword
    - cursor: Cursor, 0 for the first request, get from the returned data later, used for paging.
    ### Return:
    - User search results V2

    # [示例/Example]
    keyword = \"中华娘\"
    cursor = 0

    Args:
        keyword (str): 关键词/Keyword
        cursor (Union[Unset, int]): 游标/Cursor Default: 0.

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
    cursor: Union[Unset, int] = 0,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取指定关键词的用户搜索结果 V2 (已弃用，替代接口请参考下方文档)/Get user search results of specified keywords V2 (deprecated,
    please refer to the following document for replacement interface)

     # [中文]
    ### 用途:
    - 获取指定关键词的用户搜索结果V2
    - 推荐默认使用专门的搜索接口，稳定性更好：https://api.tikhub.io/#/Douyin-Search-API
    ### 参数:
    - keyword: 关键词
    - cursor: 游标，第一次请求时为0，后续从返回数据中获取，用于翻页。
    ### 返回:
    - 用户搜索结果V2

    # [English]
    ### Purpose:
    - Get user search results of specified keywords V2
    - It is recommended to use the dedicated search interface by default, which is more stable:
    https://api.tikhub.io/#/Douyin-Search-API
    ### Parameters:
    - keyword: Keyword
    - cursor: Cursor, 0 for the first request, get from the returned data later, used for paging.
    ### Return:
    - User search results V2

    # [示例/Example]
    keyword = \"中华娘\"
    cursor = 0

    Args:
        keyword (str): 关键词/Keyword
        cursor (Union[Unset, int]): 游标/Cursor Default: 0.

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
