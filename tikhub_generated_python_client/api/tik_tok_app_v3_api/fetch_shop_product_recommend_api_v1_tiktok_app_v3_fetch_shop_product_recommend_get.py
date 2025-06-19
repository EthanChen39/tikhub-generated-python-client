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
    scroll_param: Union[Unset, str] = "",
    page_size: Union[Unset, int] = 10,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["seller_id"] = seller_id

    params["scroll_param"] = scroll_param

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/app/v3/fetch_shop_product_recommend",
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
    scroll_param: Union[Unset, str] = "",
    page_size: Union[Unset, int] = 10,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取商家商品推荐数据/Get shop product recommend data

     # [中文]
    ### 用途:
    - 获取商家商品推荐数据
    ### 参数:
    - seller_id: 商家id,店铺id
    - scroll_param: 滚动参数，用于加载更多商品数据
    - page_size: 每页数量
    ### 返回:
    - 商家商品推荐数据

    # [English]
    ### Purpose:
    - Get shop product recommend data
    ### Parameters:
    - seller_id: Seller id, shop id
    - scroll_param: Scroll parameter, used to load more product data
    - page_size: Number per page
    ### Return:
    - Shop product recommend data

    # [示例/Example]
    seller_id = \"8646929864612614278\"
    scroll_param = \"\"
    page_size = 10

    Args:
        seller_id (str): 商家id,店铺id/Seller id, shop id
        scroll_param (Union[Unset, str]): 滚动参数，用于加载更多商品数据/Scroll parameter, used to load more
            product data Default: ''.
        page_size (Union[Unset, int]): 每页数量/Number per page Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        seller_id=seller_id,
        scroll_param=scroll_param,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    seller_id: str,
    scroll_param: Union[Unset, str] = "",
    page_size: Union[Unset, int] = 10,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取商家商品推荐数据/Get shop product recommend data

     # [中文]
    ### 用途:
    - 获取商家商品推荐数据
    ### 参数:
    - seller_id: 商家id,店铺id
    - scroll_param: 滚动参数，用于加载更多商品数据
    - page_size: 每页数量
    ### 返回:
    - 商家商品推荐数据

    # [English]
    ### Purpose:
    - Get shop product recommend data
    ### Parameters:
    - seller_id: Seller id, shop id
    - scroll_param: Scroll parameter, used to load more product data
    - page_size: Number per page
    ### Return:
    - Shop product recommend data

    # [示例/Example]
    seller_id = \"8646929864612614278\"
    scroll_param = \"\"
    page_size = 10

    Args:
        seller_id (str): 商家id,店铺id/Seller id, shop id
        scroll_param (Union[Unset, str]): 滚动参数，用于加载更多商品数据/Scroll parameter, used to load more
            product data Default: ''.
        page_size (Union[Unset, int]): 每页数量/Number per page Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        seller_id=seller_id,
        scroll_param=scroll_param,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    seller_id: str,
    scroll_param: Union[Unset, str] = "",
    page_size: Union[Unset, int] = 10,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取商家商品推荐数据/Get shop product recommend data

     # [中文]
    ### 用途:
    - 获取商家商品推荐数据
    ### 参数:
    - seller_id: 商家id,店铺id
    - scroll_param: 滚动参数，用于加载更多商品数据
    - page_size: 每页数量
    ### 返回:
    - 商家商品推荐数据

    # [English]
    ### Purpose:
    - Get shop product recommend data
    ### Parameters:
    - seller_id: Seller id, shop id
    - scroll_param: Scroll parameter, used to load more product data
    - page_size: Number per page
    ### Return:
    - Shop product recommend data

    # [示例/Example]
    seller_id = \"8646929864612614278\"
    scroll_param = \"\"
    page_size = 10

    Args:
        seller_id (str): 商家id,店铺id/Seller id, shop id
        scroll_param (Union[Unset, str]): 滚动参数，用于加载更多商品数据/Scroll parameter, used to load more
            product data Default: ''.
        page_size (Union[Unset, int]): 每页数量/Number per page Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        seller_id=seller_id,
        scroll_param=scroll_param,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    seller_id: str,
    scroll_param: Union[Unset, str] = "",
    page_size: Union[Unset, int] = 10,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取商家商品推荐数据/Get shop product recommend data

     # [中文]
    ### 用途:
    - 获取商家商品推荐数据
    ### 参数:
    - seller_id: 商家id,店铺id
    - scroll_param: 滚动参数，用于加载更多商品数据
    - page_size: 每页数量
    ### 返回:
    - 商家商品推荐数据

    # [English]
    ### Purpose:
    - Get shop product recommend data
    ### Parameters:
    - seller_id: Seller id, shop id
    - scroll_param: Scroll parameter, used to load more product data
    - page_size: Number per page
    ### Return:
    - Shop product recommend data

    # [示例/Example]
    seller_id = \"8646929864612614278\"
    scroll_param = \"\"
    page_size = 10

    Args:
        seller_id (str): 商家id,店铺id/Seller id, shop id
        scroll_param (Union[Unset, str]): 滚动参数，用于加载更多商品数据/Scroll parameter, used to load more
            product data Default: ''.
        page_size (Union[Unset, int]): 每页数量/Number per page Default: 10.

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
            scroll_param=scroll_param,
            page_size=page_size,
        )
    ).parsed
