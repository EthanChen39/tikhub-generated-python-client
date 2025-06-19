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
    count: Union[Unset, int] = 12,
    sort_type: Union[Unset, int] = 1,
    customer_review_four_star: Union[Unset, bool] = False,
    have_discount: Union[Unset, bool] = False,
    min_price: Union[Unset, str] = "",
    max_price: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["cursor"] = cursor

    params["count"] = count

    params["sort_type"] = sort_type

    params["customer_review_four_star"] = customer_review_four_star

    params["have_discount"] = have_discount

    params["min_price"] = min_price

    params["max_price"] = max_price

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/app/v3/fetch_product_search",
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
    count: Union[Unset, int] = 12,
    sort_type: Union[Unset, int] = 1,
    customer_review_four_star: Union[Unset, bool] = False,
    have_discount: Union[Unset, bool] = False,
    min_price: Union[Unset, str] = "",
    max_price: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取商品搜索结果/Get product search results

     # [中文]
    ### 用途:
    - 获取商品搜索结果
    ### 参数:
    - keyword: 关键词
    - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
    - count: 数量
    - sort_type: 商品排序条件
        - 1: 综合排序
        - 2: 销量排序
        - 3: 价格从高到低
        - 4: 价格从低到高
        - 5: 最新发布
    - customer_review_four_star: 四星以上评价
    - have_discount: 有优惠
    - min_price: 最低价格
    - max_price: 最高价格
    ### 返回:
    - 商品搜索结果

    # [English]
    ### Purpose:
    - Get product search results
    ### Parameters:
    - keyword: Keyword
    - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the
    first response.
    - count: Number
    - sort_type: Product sorting conditions
        - 1: Comprehensive sorting
        - 2: Sales volume sorting
        - 3: Price high to low
        - 4: Price low to high
        - 5: Latest release
    - customer_review_four_star: Four-star or more reviews
    - have_discount: Having discount
    - min_price: Minimum price
    - max_price: Maximum price
    ### Return:
    - Product search results

    # [示例/Example]
    keyword = \"Cat Toy\"
    cursor = 0
    count = 12
    sort_type = 1
    customer_review_four_star = False
    have_discount = False
    min_price = \"10\"
    max_price = \"25\"

    Args:
        keyword (str): 关键词/Keyword
        cursor (Union[Unset, int]): 游标/Cursor Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 12.
        sort_type (Union[Unset, int]): 商品排序条件/Product sorting conditions Default: 1.
        customer_review_four_star (Union[Unset, bool]): 四星以上评价/Four-star or more reviews Default:
            False.
        have_discount (Union[Unset, bool]): 有优惠/Having discount Default: False.
        min_price (Union[Unset, str]): 最低价格/Minimum price Default: ''.
        max_price (Union[Unset, str]): 最高价格/Maximum price Default: ''.

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
        sort_type=sort_type,
        customer_review_four_star=customer_review_four_star,
        have_discount=have_discount,
        min_price=min_price,
        max_price=max_price,
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
    count: Union[Unset, int] = 12,
    sort_type: Union[Unset, int] = 1,
    customer_review_four_star: Union[Unset, bool] = False,
    have_discount: Union[Unset, bool] = False,
    min_price: Union[Unset, str] = "",
    max_price: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取商品搜索结果/Get product search results

     # [中文]
    ### 用途:
    - 获取商品搜索结果
    ### 参数:
    - keyword: 关键词
    - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
    - count: 数量
    - sort_type: 商品排序条件
        - 1: 综合排序
        - 2: 销量排序
        - 3: 价格从高到低
        - 4: 价格从低到高
        - 5: 最新发布
    - customer_review_four_star: 四星以上评价
    - have_discount: 有优惠
    - min_price: 最低价格
    - max_price: 最高价格
    ### 返回:
    - 商品搜索结果

    # [English]
    ### Purpose:
    - Get product search results
    ### Parameters:
    - keyword: Keyword
    - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the
    first response.
    - count: Number
    - sort_type: Product sorting conditions
        - 1: Comprehensive sorting
        - 2: Sales volume sorting
        - 3: Price high to low
        - 4: Price low to high
        - 5: Latest release
    - customer_review_four_star: Four-star or more reviews
    - have_discount: Having discount
    - min_price: Minimum price
    - max_price: Maximum price
    ### Return:
    - Product search results

    # [示例/Example]
    keyword = \"Cat Toy\"
    cursor = 0
    count = 12
    sort_type = 1
    customer_review_four_star = False
    have_discount = False
    min_price = \"10\"
    max_price = \"25\"

    Args:
        keyword (str): 关键词/Keyword
        cursor (Union[Unset, int]): 游标/Cursor Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 12.
        sort_type (Union[Unset, int]): 商品排序条件/Product sorting conditions Default: 1.
        customer_review_four_star (Union[Unset, bool]): 四星以上评价/Four-star or more reviews Default:
            False.
        have_discount (Union[Unset, bool]): 有优惠/Having discount Default: False.
        min_price (Union[Unset, str]): 最低价格/Minimum price Default: ''.
        max_price (Union[Unset, str]): 最高价格/Maximum price Default: ''.

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
        sort_type=sort_type,
        customer_review_four_star=customer_review_four_star,
        have_discount=have_discount,
        min_price=min_price,
        max_price=max_price,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 12,
    sort_type: Union[Unset, int] = 1,
    customer_review_four_star: Union[Unset, bool] = False,
    have_discount: Union[Unset, bool] = False,
    min_price: Union[Unset, str] = "",
    max_price: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取商品搜索结果/Get product search results

     # [中文]
    ### 用途:
    - 获取商品搜索结果
    ### 参数:
    - keyword: 关键词
    - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
    - count: 数量
    - sort_type: 商品排序条件
        - 1: 综合排序
        - 2: 销量排序
        - 3: 价格从高到低
        - 4: 价格从低到高
        - 5: 最新发布
    - customer_review_four_star: 四星以上评价
    - have_discount: 有优惠
    - min_price: 最低价格
    - max_price: 最高价格
    ### 返回:
    - 商品搜索结果

    # [English]
    ### Purpose:
    - Get product search results
    ### Parameters:
    - keyword: Keyword
    - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the
    first response.
    - count: Number
    - sort_type: Product sorting conditions
        - 1: Comprehensive sorting
        - 2: Sales volume sorting
        - 3: Price high to low
        - 4: Price low to high
        - 5: Latest release
    - customer_review_four_star: Four-star or more reviews
    - have_discount: Having discount
    - min_price: Minimum price
    - max_price: Maximum price
    ### Return:
    - Product search results

    # [示例/Example]
    keyword = \"Cat Toy\"
    cursor = 0
    count = 12
    sort_type = 1
    customer_review_four_star = False
    have_discount = False
    min_price = \"10\"
    max_price = \"25\"

    Args:
        keyword (str): 关键词/Keyword
        cursor (Union[Unset, int]): 游标/Cursor Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 12.
        sort_type (Union[Unset, int]): 商品排序条件/Product sorting conditions Default: 1.
        customer_review_four_star (Union[Unset, bool]): 四星以上评价/Four-star or more reviews Default:
            False.
        have_discount (Union[Unset, bool]): 有优惠/Having discount Default: False.
        min_price (Union[Unset, str]): 最低价格/Minimum price Default: ''.
        max_price (Union[Unset, str]): 最高价格/Maximum price Default: ''.

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
        sort_type=sort_type,
        customer_review_four_star=customer_review_four_star,
        have_discount=have_discount,
        min_price=min_price,
        max_price=max_price,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
    cursor: Union[Unset, int] = 0,
    count: Union[Unset, int] = 12,
    sort_type: Union[Unset, int] = 1,
    customer_review_four_star: Union[Unset, bool] = False,
    have_discount: Union[Unset, bool] = False,
    min_price: Union[Unset, str] = "",
    max_price: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取商品搜索结果/Get product search results

     # [中文]
    ### 用途:
    - 获取商品搜索结果
    ### 参数:
    - keyword: 关键词
    - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
    - count: 数量
    - sort_type: 商品排序条件
        - 1: 综合排序
        - 2: 销量排序
        - 3: 价格从高到低
        - 4: 价格从低到高
        - 5: 最新发布
    - customer_review_four_star: 四星以上评价
    - have_discount: 有优惠
    - min_price: 最低价格
    - max_price: 最高价格
    ### 返回:
    - 商品搜索结果

    # [English]
    ### Purpose:
    - Get product search results
    ### Parameters:
    - keyword: Keyword
    - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the
    first response.
    - count: Number
    - sort_type: Product sorting conditions
        - 1: Comprehensive sorting
        - 2: Sales volume sorting
        - 3: Price high to low
        - 4: Price low to high
        - 5: Latest release
    - customer_review_four_star: Four-star or more reviews
    - have_discount: Having discount
    - min_price: Minimum price
    - max_price: Maximum price
    ### Return:
    - Product search results

    # [示例/Example]
    keyword = \"Cat Toy\"
    cursor = 0
    count = 12
    sort_type = 1
    customer_review_four_star = False
    have_discount = False
    min_price = \"10\"
    max_price = \"25\"

    Args:
        keyword (str): 关键词/Keyword
        cursor (Union[Unset, int]): 游标/Cursor Default: 0.
        count (Union[Unset, int]): 数量/Number Default: 12.
        sort_type (Union[Unset, int]): 商品排序条件/Product sorting conditions Default: 1.
        customer_review_four_star (Union[Unset, bool]): 四星以上评价/Four-star or more reviews Default:
            False.
        have_discount (Union[Unset, bool]): 有优惠/Having discount Default: False.
        min_price (Union[Unset, str]): 最低价格/Minimum price Default: ''.
        max_price (Union[Unset, str]): 最高价格/Maximum price Default: ''.

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
            sort_type=sort_type,
            customer_review_four_star=customer_review_four_star,
            have_discount=have_discount,
            min_price=min_price,
            max_price=max_price,
        )
    ).parsed
