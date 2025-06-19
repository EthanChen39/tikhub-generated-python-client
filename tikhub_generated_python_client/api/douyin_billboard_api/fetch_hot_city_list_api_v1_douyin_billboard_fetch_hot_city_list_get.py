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
    page: int,
    page_size: int,
    order: str,
    city_code: Union[Unset, str] = "",
    sentence_tag: Union[Unset, str] = "",
    keyword: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    params["order"] = order

    params["city_code"] = city_code

    params["sentence_tag"] = sentence_tag

    params["keyword"] = keyword

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/billboard/fetch_hot_city_list",
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
    page: int,
    page_size: int,
    order: str,
    city_code: Union[Unset, str] = "",
    sentence_tag: Union[Unset, str] = "",
    keyword: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取同城热点榜/Fetch city hot list

     # [中文]
    ### 用途:
    - 获取同城热点榜
    ### 参数:
    - page: 页码
    - page_size: 每页数量
    - order: 排序方式
        - rank 按热度排序
        - rank_diff 按排名变化
    - city_code: 城市编码，从城市列表获取，空为全部
    - sentence_tag: 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部
    - keyword: 热点搜索词
    ### 返回:
    - 同城热点榜

    # [English]
    ### Purpose:
    - Get the city hot list
    ### Parameters:
    - page: Page number
    - page_size: Number of items per page
    - order: Sorting method
        - rank Sort by popularity
        - rank_diff Sort by ranking change
    - city_code: City code, get from city list, empty for all
    - sentence_tag: Hot category tag, get from hot list category, multiple categories separated by
    commas, empty for all
    - keyword: Hot search term
    ### Return:
    - City hot list

    Args:
        page (int): 页码
        page_size (int): 每页数量
        order (str): 排序方式
        city_code (Union[Unset, str]): 城市编码，从城市列表获取，空为全部 Default: ''.
        sentence_tag (Union[Unset, str]): 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部 Default: ''.
        keyword (Union[Unset, str]): 热点搜索词 Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        order=order,
        city_code=city_code,
        sentence_tag=sentence_tag,
        keyword=keyword,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page: int,
    page_size: int,
    order: str,
    city_code: Union[Unset, str] = "",
    sentence_tag: Union[Unset, str] = "",
    keyword: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取同城热点榜/Fetch city hot list

     # [中文]
    ### 用途:
    - 获取同城热点榜
    ### 参数:
    - page: 页码
    - page_size: 每页数量
    - order: 排序方式
        - rank 按热度排序
        - rank_diff 按排名变化
    - city_code: 城市编码，从城市列表获取，空为全部
    - sentence_tag: 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部
    - keyword: 热点搜索词
    ### 返回:
    - 同城热点榜

    # [English]
    ### Purpose:
    - Get the city hot list
    ### Parameters:
    - page: Page number
    - page_size: Number of items per page
    - order: Sorting method
        - rank Sort by popularity
        - rank_diff Sort by ranking change
    - city_code: City code, get from city list, empty for all
    - sentence_tag: Hot category tag, get from hot list category, multiple categories separated by
    commas, empty for all
    - keyword: Hot search term
    ### Return:
    - City hot list

    Args:
        page (int): 页码
        page_size (int): 每页数量
        order (str): 排序方式
        city_code (Union[Unset, str]): 城市编码，从城市列表获取，空为全部 Default: ''.
        sentence_tag (Union[Unset, str]): 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部 Default: ''.
        keyword (Union[Unset, str]): 热点搜索词 Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        order=order,
        city_code=city_code,
        sentence_tag=sentence_tag,
        keyword=keyword,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int,
    page_size: int,
    order: str,
    city_code: Union[Unset, str] = "",
    sentence_tag: Union[Unset, str] = "",
    keyword: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取同城热点榜/Fetch city hot list

     # [中文]
    ### 用途:
    - 获取同城热点榜
    ### 参数:
    - page: 页码
    - page_size: 每页数量
    - order: 排序方式
        - rank 按热度排序
        - rank_diff 按排名变化
    - city_code: 城市编码，从城市列表获取，空为全部
    - sentence_tag: 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部
    - keyword: 热点搜索词
    ### 返回:
    - 同城热点榜

    # [English]
    ### Purpose:
    - Get the city hot list
    ### Parameters:
    - page: Page number
    - page_size: Number of items per page
    - order: Sorting method
        - rank Sort by popularity
        - rank_diff Sort by ranking change
    - city_code: City code, get from city list, empty for all
    - sentence_tag: Hot category tag, get from hot list category, multiple categories separated by
    commas, empty for all
    - keyword: Hot search term
    ### Return:
    - City hot list

    Args:
        page (int): 页码
        page_size (int): 每页数量
        order (str): 排序方式
        city_code (Union[Unset, str]): 城市编码，从城市列表获取，空为全部 Default: ''.
        sentence_tag (Union[Unset, str]): 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部 Default: ''.
        keyword (Union[Unset, str]): 热点搜索词 Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        order=order,
        city_code=city_code,
        sentence_tag=sentence_tag,
        keyword=keyword,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int,
    page_size: int,
    order: str,
    city_code: Union[Unset, str] = "",
    sentence_tag: Union[Unset, str] = "",
    keyword: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取同城热点榜/Fetch city hot list

     # [中文]
    ### 用途:
    - 获取同城热点榜
    ### 参数:
    - page: 页码
    - page_size: 每页数量
    - order: 排序方式
        - rank 按热度排序
        - rank_diff 按排名变化
    - city_code: 城市编码，从城市列表获取，空为全部
    - sentence_tag: 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部
    - keyword: 热点搜索词
    ### 返回:
    - 同城热点榜

    # [English]
    ### Purpose:
    - Get the city hot list
    ### Parameters:
    - page: Page number
    - page_size: Number of items per page
    - order: Sorting method
        - rank Sort by popularity
        - rank_diff Sort by ranking change
    - city_code: City code, get from city list, empty for all
    - sentence_tag: Hot category tag, get from hot list category, multiple categories separated by
    commas, empty for all
    - keyword: Hot search term
    ### Return:
    - City hot list

    Args:
        page (int): 页码
        page_size (int): 每页数量
        order (str): 排序方式
        city_code (Union[Unset, str]): 城市编码，从城市列表获取，空为全部 Default: ''.
        sentence_tag (Union[Unset, str]): 热点分类标签，从热点榜分类获取，多个分类用逗号分隔，空为全部 Default: ''.
        keyword (Union[Unset, str]): 热点搜索词 Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            order=order,
            city_code=city_code,
            sentence_tag=sentence_tag,
            keyword=keyword,
        )
    ).parsed
