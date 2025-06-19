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
    seller_id: str,
    scroll_params: Union[Unset, str] = "",
    page_size: Union[Unset, int] = 10,
    sort_field: Union[Unset, int] = 1,
    sort_order: Union[Unset, int] = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["seller_id"] = seller_id

    params["scroll_params"] = scroll_params

    params["page_size"] = page_size

    params["sort_field"] = sort_field

    params["sort_order"] = sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/app/v3/fetch_shop_product_list",
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
    seller_id: str,
    scroll_params: Union[Unset, str] = "",
    page_size: Union[Unset, int] = 10,
    sort_field: Union[Unset, int] = 1,
    sort_order: Union[Unset, int] = 0,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取商家商品列表数据/Get shop product list data

     # [中文]
    ### 用途:
    - 获取商家商品列表数据
    ### 参数:
    - seller_id: 商家id,店铺id
    - scroll_params: 滚动参数，用于加载更多商品数据
    - page_size: 每页数量
    - sort_field: 排序字段
        - 1: 综合排序
        - 3: 最新发布
        - 4: 销量最好
        - 5: 价格排序
    - sort_order: 排序方式
        - 0: 默认价格排序
        - 1: 价格从高到低
        - 2: 价格从低到高
    ### 返回:
    - 商家商品列表数据

    # [English]
    ### Purpose:
    - Get shop product list data
    ### Parameters:
    - seller_id: Seller id, shop id
    - scroll_params: Scroll parameter, used to load more product data
    - page_size: Number per page
    - sort_field: Sorting field
        - 1: Comprehensive sorting
        - 3: Latest release
        - 4: Best sales
        - 5: Price sorting
    - sort_order: Sorting method
        - 0: Default price sorting
        - 1: Price high to low
        - 2: Price low to high
    ### Return:
    - Shop product list data

    # [示例/Example]
    seller_id = \"8646929864612614278\"
    scroll_params = \"\"
    page_size = 10
    sort_field = 1
    sort_order = 0

    Args:
        seller_id (str): 商家id,店铺id/Seller id, shop id
        scroll_params (Union[Unset, str]): 滚动参数，用于加载更多商品数据/Scroll parameter, used to load more
            product data Default: ''.
        page_size (Union[Unset, int]): 每页数量/Number per page Default: 10.
        sort_field (Union[Unset, int]): 排序字段/Sorting field Default: 1.
        sort_order (Union[Unset, int]): 排序方式/Sorting method Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        seller_id=seller_id,
        scroll_params=scroll_params,
        page_size=page_size,
        sort_field=sort_field,
        sort_order=sort_order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    seller_id: str,
    scroll_params: Union[Unset, str] = "",
    page_size: Union[Unset, int] = 10,
    sort_field: Union[Unset, int] = 1,
    sort_order: Union[Unset, int] = 0,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取商家商品列表数据/Get shop product list data

     # [中文]
    ### 用途:
    - 获取商家商品列表数据
    ### 参数:
    - seller_id: 商家id,店铺id
    - scroll_params: 滚动参数，用于加载更多商品数据
    - page_size: 每页数量
    - sort_field: 排序字段
        - 1: 综合排序
        - 3: 最新发布
        - 4: 销量最好
        - 5: 价格排序
    - sort_order: 排序方式
        - 0: 默认价格排序
        - 1: 价格从高到低
        - 2: 价格从低到高
    ### 返回:
    - 商家商品列表数据

    # [English]
    ### Purpose:
    - Get shop product list data
    ### Parameters:
    - seller_id: Seller id, shop id
    - scroll_params: Scroll parameter, used to load more product data
    - page_size: Number per page
    - sort_field: Sorting field
        - 1: Comprehensive sorting
        - 3: Latest release
        - 4: Best sales
        - 5: Price sorting
    - sort_order: Sorting method
        - 0: Default price sorting
        - 1: Price high to low
        - 2: Price low to high
    ### Return:
    - Shop product list data

    # [示例/Example]
    seller_id = \"8646929864612614278\"
    scroll_params = \"\"
    page_size = 10
    sort_field = 1
    sort_order = 0

    Args:
        seller_id (str): 商家id,店铺id/Seller id, shop id
        scroll_params (Union[Unset, str]): 滚动参数，用于加载更多商品数据/Scroll parameter, used to load more
            product data Default: ''.
        page_size (Union[Unset, int]): 每页数量/Number per page Default: 10.
        sort_field (Union[Unset, int]): 排序字段/Sorting field Default: 1.
        sort_order (Union[Unset, int]): 排序方式/Sorting method Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        seller_id=seller_id,
        scroll_params=scroll_params,
        page_size=page_size,
        sort_field=sort_field,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    seller_id: str,
    scroll_params: Union[Unset, str] = "",
    page_size: Union[Unset, int] = 10,
    sort_field: Union[Unset, int] = 1,
    sort_order: Union[Unset, int] = 0,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取商家商品列表数据/Get shop product list data

     # [中文]
    ### 用途:
    - 获取商家商品列表数据
    ### 参数:
    - seller_id: 商家id,店铺id
    - scroll_params: 滚动参数，用于加载更多商品数据
    - page_size: 每页数量
    - sort_field: 排序字段
        - 1: 综合排序
        - 3: 最新发布
        - 4: 销量最好
        - 5: 价格排序
    - sort_order: 排序方式
        - 0: 默认价格排序
        - 1: 价格从高到低
        - 2: 价格从低到高
    ### 返回:
    - 商家商品列表数据

    # [English]
    ### Purpose:
    - Get shop product list data
    ### Parameters:
    - seller_id: Seller id, shop id
    - scroll_params: Scroll parameter, used to load more product data
    - page_size: Number per page
    - sort_field: Sorting field
        - 1: Comprehensive sorting
        - 3: Latest release
        - 4: Best sales
        - 5: Price sorting
    - sort_order: Sorting method
        - 0: Default price sorting
        - 1: Price high to low
        - 2: Price low to high
    ### Return:
    - Shop product list data

    # [示例/Example]
    seller_id = \"8646929864612614278\"
    scroll_params = \"\"
    page_size = 10
    sort_field = 1
    sort_order = 0

    Args:
        seller_id (str): 商家id,店铺id/Seller id, shop id
        scroll_params (Union[Unset, str]): 滚动参数，用于加载更多商品数据/Scroll parameter, used to load more
            product data Default: ''.
        page_size (Union[Unset, int]): 每页数量/Number per page Default: 10.
        sort_field (Union[Unset, int]): 排序字段/Sorting field Default: 1.
        sort_order (Union[Unset, int]): 排序方式/Sorting method Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        seller_id=seller_id,
        scroll_params=scroll_params,
        page_size=page_size,
        sort_field=sort_field,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    seller_id: str,
    scroll_params: Union[Unset, str] = "",
    page_size: Union[Unset, int] = 10,
    sort_field: Union[Unset, int] = 1,
    sort_order: Union[Unset, int] = 0,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取商家商品列表数据/Get shop product list data

     # [中文]
    ### 用途:
    - 获取商家商品列表数据
    ### 参数:
    - seller_id: 商家id,店铺id
    - scroll_params: 滚动参数，用于加载更多商品数据
    - page_size: 每页数量
    - sort_field: 排序字段
        - 1: 综合排序
        - 3: 最新发布
        - 4: 销量最好
        - 5: 价格排序
    - sort_order: 排序方式
        - 0: 默认价格排序
        - 1: 价格从高到低
        - 2: 价格从低到高
    ### 返回:
    - 商家商品列表数据

    # [English]
    ### Purpose:
    - Get shop product list data
    ### Parameters:
    - seller_id: Seller id, shop id
    - scroll_params: Scroll parameter, used to load more product data
    - page_size: Number per page
    - sort_field: Sorting field
        - 1: Comprehensive sorting
        - 3: Latest release
        - 4: Best sales
        - 5: Price sorting
    - sort_order: Sorting method
        - 0: Default price sorting
        - 1: Price high to low
        - 2: Price low to high
    ### Return:
    - Shop product list data

    # [示例/Example]
    seller_id = \"8646929864612614278\"
    scroll_params = \"\"
    page_size = 10
    sort_field = 1
    sort_order = 0

    Args:
        seller_id (str): 商家id,店铺id/Seller id, shop id
        scroll_params (Union[Unset, str]): 滚动参数，用于加载更多商品数据/Scroll parameter, used to load more
            product data Default: ''.
        page_size (Union[Unset, int]): 每页数量/Number per page Default: 10.
        sort_field (Union[Unset, int]): 排序字段/Sorting field Default: 1.
        sort_order (Union[Unset, int]): 排序方式/Sorting method Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            seller_id=seller_id,
            scroll_params=scroll_params,
            page_size=page_size,
            sort_field=sort_field,
            sort_order=sort_order,
        )
    ).parsed
