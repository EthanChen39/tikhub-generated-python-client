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
    product_id: str,
    cursor: Union[Unset, int] = 0,
    size: Union[Unset, int] = 10,
    filter_id: Union[Unset, int] = 0,
    sort_type: Union[Unset, int] = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["product_id"] = product_id

    params["cursor"] = cursor

    params["size"] = size

    params["filter_id"] = filter_id

    params["sort_type"] = sort_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/app/v3/fetch_product_review",
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
    product_id: str,
    cursor: Union[Unset, int] = 0,
    size: Union[Unset, int] = 10,
    filter_id: Union[Unset, int] = 0,
    sort_type: Union[Unset, int] = 0,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取商品评价数据/Get product review data

     # [中文]
    ### 用途:
    - 获取商品评价数据
    ### 参数:
    - product_id: 商品id
    - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
    - size: 数量
    - filter_id: 筛选条件
        - 0: 全部评价
        - 1: 1星评价
        - 2: 2星评价
        - 3: 3星评价
        - 4: 4星评价
        - 5: 5星评价
        - 102: 有图评价
        - 104: 已购买的评价
    - sort_type: 排序条件
        - 1: 相关度
        - 2: 从新到旧
    ### 返回:
    - 商品评价数据

    # [English]
    ### Purpose:
    - Get product review data
    ### Parameters:
    - product_id: Product id
    - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the
    first response.
    - size: Count number
    - filter_id: Filter condition
        - 0: All reviews
        - 1: 1-star review
        - 2: 2-star review
        - 3: 3-star review
        - 4: 4-star review
        - 5: 5-star review
        - 102: Reviews with pictures
        - 104: Reviews of purchased products
    - sort_type: Sorting conditions
        - 1: Relevance
        - 2: New to old
    ### Return:
    - Product review data

    # [示例/Example]
    product_id = \"1729448812983194615\"
    cursor = 0
    size = 10
    filter_id = 0
    sort_type = 0

    Args:
        product_id (str): 商品id/Product id
        cursor (Union[Unset, int]): 游标/Cursor Default: 0.
        size (Union[Unset, int]): 数量/Number Default: 10.
        filter_id (Union[Unset, int]): 筛选条件/Filter condition Default: 0.
        sort_type (Union[Unset, int]): 排序条件/Sorting conditions Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        cursor=cursor,
        size=size,
        filter_id=filter_id,
        sort_type=sort_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    product_id: str,
    cursor: Union[Unset, int] = 0,
    size: Union[Unset, int] = 10,
    filter_id: Union[Unset, int] = 0,
    sort_type: Union[Unset, int] = 0,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取商品评价数据/Get product review data

     # [中文]
    ### 用途:
    - 获取商品评价数据
    ### 参数:
    - product_id: 商品id
    - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
    - size: 数量
    - filter_id: 筛选条件
        - 0: 全部评价
        - 1: 1星评价
        - 2: 2星评价
        - 3: 3星评价
        - 4: 4星评价
        - 5: 5星评价
        - 102: 有图评价
        - 104: 已购买的评价
    - sort_type: 排序条件
        - 1: 相关度
        - 2: 从新到旧
    ### 返回:
    - 商品评价数据

    # [English]
    ### Purpose:
    - Get product review data
    ### Parameters:
    - product_id: Product id
    - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the
    first response.
    - size: Count number
    - filter_id: Filter condition
        - 0: All reviews
        - 1: 1-star review
        - 2: 2-star review
        - 3: 3-star review
        - 4: 4-star review
        - 5: 5-star review
        - 102: Reviews with pictures
        - 104: Reviews of purchased products
    - sort_type: Sorting conditions
        - 1: Relevance
        - 2: New to old
    ### Return:
    - Product review data

    # [示例/Example]
    product_id = \"1729448812983194615\"
    cursor = 0
    size = 10
    filter_id = 0
    sort_type = 0

    Args:
        product_id (str): 商品id/Product id
        cursor (Union[Unset, int]): 游标/Cursor Default: 0.
        size (Union[Unset, int]): 数量/Number Default: 10.
        filter_id (Union[Unset, int]): 筛选条件/Filter condition Default: 0.
        sort_type (Union[Unset, int]): 排序条件/Sorting conditions Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        product_id=product_id,
        cursor=cursor,
        size=size,
        filter_id=filter_id,
        sort_type=sort_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    product_id: str,
    cursor: Union[Unset, int] = 0,
    size: Union[Unset, int] = 10,
    filter_id: Union[Unset, int] = 0,
    sort_type: Union[Unset, int] = 0,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取商品评价数据/Get product review data

     # [中文]
    ### 用途:
    - 获取商品评价数据
    ### 参数:
    - product_id: 商品id
    - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
    - size: 数量
    - filter_id: 筛选条件
        - 0: 全部评价
        - 1: 1星评价
        - 2: 2星评价
        - 3: 3星评价
        - 4: 4星评价
        - 5: 5星评价
        - 102: 有图评价
        - 104: 已购买的评价
    - sort_type: 排序条件
        - 1: 相关度
        - 2: 从新到旧
    ### 返回:
    - 商品评价数据

    # [English]
    ### Purpose:
    - Get product review data
    ### Parameters:
    - product_id: Product id
    - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the
    first response.
    - size: Count number
    - filter_id: Filter condition
        - 0: All reviews
        - 1: 1-star review
        - 2: 2-star review
        - 3: 3-star review
        - 4: 4-star review
        - 5: 5-star review
        - 102: Reviews with pictures
        - 104: Reviews of purchased products
    - sort_type: Sorting conditions
        - 1: Relevance
        - 2: New to old
    ### Return:
    - Product review data

    # [示例/Example]
    product_id = \"1729448812983194615\"
    cursor = 0
    size = 10
    filter_id = 0
    sort_type = 0

    Args:
        product_id (str): 商品id/Product id
        cursor (Union[Unset, int]): 游标/Cursor Default: 0.
        size (Union[Unset, int]): 数量/Number Default: 10.
        filter_id (Union[Unset, int]): 筛选条件/Filter condition Default: 0.
        sort_type (Union[Unset, int]): 排序条件/Sorting conditions Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        cursor=cursor,
        size=size,
        filter_id=filter_id,
        sort_type=sort_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    product_id: str,
    cursor: Union[Unset, int] = 0,
    size: Union[Unset, int] = 10,
    filter_id: Union[Unset, int] = 0,
    sort_type: Union[Unset, int] = 0,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取商品评价数据/Get product review data

     # [中文]
    ### 用途:
    - 获取商品评价数据
    ### 参数:
    - product_id: 商品id
    - cursor: 游标，用于翻页，第一页为0，第二页为第一次响应中的cursor值。
    - size: 数量
    - filter_id: 筛选条件
        - 0: 全部评价
        - 1: 1星评价
        - 2: 2星评价
        - 3: 3星评价
        - 4: 4星评价
        - 5: 5星评价
        - 102: 有图评价
        - 104: 已购买的评价
    - sort_type: 排序条件
        - 1: 相关度
        - 2: 从新到旧
    ### 返回:
    - 商品评价数据

    # [English]
    ### Purpose:
    - Get product review data
    ### Parameters:
    - product_id: Product id
    - cursor: Cursor, used for paging, the first page is 0, the second page is the cursor value in the
    first response.
    - size: Count number
    - filter_id: Filter condition
        - 0: All reviews
        - 1: 1-star review
        - 2: 2-star review
        - 3: 3-star review
        - 4: 4-star review
        - 5: 5-star review
        - 102: Reviews with pictures
        - 104: Reviews of purchased products
    - sort_type: Sorting conditions
        - 1: Relevance
        - 2: New to old
    ### Return:
    - Product review data

    # [示例/Example]
    product_id = \"1729448812983194615\"
    cursor = 0
    size = 10
    filter_id = 0
    sort_type = 0

    Args:
        product_id (str): 商品id/Product id
        cursor (Union[Unset, int]): 游标/Cursor Default: 0.
        size (Union[Unset, int]): 数量/Number Default: 10.
        filter_id (Union[Unset, int]): 筛选条件/Filter condition Default: 0.
        sort_type (Union[Unset, int]): 排序条件/Sorting conditions Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            product_id=product_id,
            cursor=cursor,
            size=size,
            filter_id=filter_id,
            sort_type=sort_type,
        )
    ).parsed
