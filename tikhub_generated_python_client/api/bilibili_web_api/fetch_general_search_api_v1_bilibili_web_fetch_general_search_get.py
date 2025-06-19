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
    order: str,
    page: int,
    page_size: int,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["order"] = order

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/bilibili/web/fetch_general_search",
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
    order: str,
    page: int,
    page_size: int,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取综合搜索信息/Get general search data

     # [中文]
    ### 用途:
    - 获取综合搜索信息
    ### 参数:
    - keyword: 搜索关键词
    - order: 排序方式
        - totalrank 综合排序
        - click 最多播放
        - pubdate 最新发布
        - dm 最多弹幕
        - stow 最多收藏
    - page: 页码
    - page_size: 每页数量
    ### 返回:
    - 综合搜索信息

    # [English]
    ### Purpose:
    - Get general search data
    ### Parameters:
    - keyword: Search keyword
    - order: Order method
        - totalrank Comprehensive sorting
        - click Most played
        - pubdate Latest release
        - dm Most barrage
        - stow Most collection
    - page: Page number
    - page_size: Number per page
    ### Return:
    - General search data

    # [示例/Example]
    keyword = \"火影忍者\"
    order = \"totalrank\"
    page = 1
    page_size = 42

    Args:
        keyword (str): 搜索关键词/Search keyword
        order (str): 排序方式/Order method
        page (int): 页码/Page number
        page_size (int): 每页数量/Number per page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        order=order,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    keyword: str,
    order: str,
    page: int,
    page_size: int,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取综合搜索信息/Get general search data

     # [中文]
    ### 用途:
    - 获取综合搜索信息
    ### 参数:
    - keyword: 搜索关键词
    - order: 排序方式
        - totalrank 综合排序
        - click 最多播放
        - pubdate 最新发布
        - dm 最多弹幕
        - stow 最多收藏
    - page: 页码
    - page_size: 每页数量
    ### 返回:
    - 综合搜索信息

    # [English]
    ### Purpose:
    - Get general search data
    ### Parameters:
    - keyword: Search keyword
    - order: Order method
        - totalrank Comprehensive sorting
        - click Most played
        - pubdate Latest release
        - dm Most barrage
        - stow Most collection
    - page: Page number
    - page_size: Number per page
    ### Return:
    - General search data

    # [示例/Example]
    keyword = \"火影忍者\"
    order = \"totalrank\"
    page = 1
    page_size = 42

    Args:
        keyword (str): 搜索关键词/Search keyword
        order (str): 排序方式/Order method
        page (int): 页码/Page number
        page_size (int): 每页数量/Number per page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        keyword=keyword,
        order=order,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    order: str,
    page: int,
    page_size: int,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取综合搜索信息/Get general search data

     # [中文]
    ### 用途:
    - 获取综合搜索信息
    ### 参数:
    - keyword: 搜索关键词
    - order: 排序方式
        - totalrank 综合排序
        - click 最多播放
        - pubdate 最新发布
        - dm 最多弹幕
        - stow 最多收藏
    - page: 页码
    - page_size: 每页数量
    ### 返回:
    - 综合搜索信息

    # [English]
    ### Purpose:
    - Get general search data
    ### Parameters:
    - keyword: Search keyword
    - order: Order method
        - totalrank Comprehensive sorting
        - click Most played
        - pubdate Latest release
        - dm Most barrage
        - stow Most collection
    - page: Page number
    - page_size: Number per page
    ### Return:
    - General search data

    # [示例/Example]
    keyword = \"火影忍者\"
    order = \"totalrank\"
    page = 1
    page_size = 42

    Args:
        keyword (str): 搜索关键词/Search keyword
        order (str): 排序方式/Order method
        page (int): 页码/Page number
        page_size (int): 每页数量/Number per page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        order=order,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
    order: str,
    page: int,
    page_size: int,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取综合搜索信息/Get general search data

     # [中文]
    ### 用途:
    - 获取综合搜索信息
    ### 参数:
    - keyword: 搜索关键词
    - order: 排序方式
        - totalrank 综合排序
        - click 最多播放
        - pubdate 最新发布
        - dm 最多弹幕
        - stow 最多收藏
    - page: 页码
    - page_size: 每页数量
    ### 返回:
    - 综合搜索信息

    # [English]
    ### Purpose:
    - Get general search data
    ### Parameters:
    - keyword: Search keyword
    - order: Order method
        - totalrank Comprehensive sorting
        - click Most played
        - pubdate Latest release
        - dm Most barrage
        - stow Most collection
    - page: Page number
    - page_size: Number per page
    ### Return:
    - General search data

    # [示例/Example]
    keyword = \"火影忍者\"
    order = \"totalrank\"
    page = 1
    page_size = 42

    Args:
        keyword (str): 搜索关键词/Search keyword
        order (str): 排序方式/Order method
        page (int): 页码/Page number
        page_size (int): 每页数量/Number per page

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
            order=order,
            page=page,
            page_size=page_size,
        )
    ).parsed
