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
    region: Union[Unset, str] = "US",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["product_id"] = product_id

    params["region"] = region

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/app/v3/fetch_product_detail_v3",
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
    region: Union[Unset, str] = "US",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取商品详情数据V3 / Get product detail data V3

     # [中文]
    ### 用途:
    - 获取商品详情数据V3。如果商品详情数据V2无法获取，可以尝试使用此接口。

    ### 参数:
    - product_id: 商品id，有时候需要从 `product_id_str` 字段中获取，也可以从商品分享链接中获取。
    - region: 商品的国家/地区代码，默认值为 \"US\"。

    ### 支持的国家/地区代码（按区域分组）：
    - 东南亚 Southeast Asia:
      ID（印度尼西亚）, SG（新加坡）, MY（马来西亚）, PH（菲律宾）, TH（泰国）
    - 北美 North America:
      US（美国）, MX（墨西哥）
    - 欧洲 Europe:
      IE（爱尔兰）, GB（英国）, ES（西班牙）
    - 越南 Vietnam:
      VN（越南）

    ### 返回:
    - 商品详情数据V3

    # [English]
    ### Purpose:
    - Get product detail data V3. If product detail data V2 cannot be retrieved, try this version.

    ### Parameters:
    - product_id: Product ID. Sometimes needs to be extracted from `product_id_str` field, or can be
    obtained from the product share link.
    - region: Country code of the product, default is \"US\".

    ### Supported region codes (grouped by area):
    - Southeast Asia:
      ID (Indonesia), SG (Singapore), MY (Malaysia), PH (Philippines), TH (Thailand)
    - North America:
      US (United States), MX (Mexico)
    - Europe:
      IE (Ireland), GB (United Kingdom), ES (Spain)
    - Vietnam:
      VN (Vietnam)

    ### Return:
    - Product detail data V3

    # [示例 / Example]
    product_id = \"1729385239712731370\"
    region = \"US\"

    Args:
        product_id (str): 商品id / Product ID
        region (Union[Unset, str]): 商品的国家/地区代码/ Country/region code of the product Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        region=region,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    product_id: str,
    region: Union[Unset, str] = "US",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取商品详情数据V3 / Get product detail data V3

     # [中文]
    ### 用途:
    - 获取商品详情数据V3。如果商品详情数据V2无法获取，可以尝试使用此接口。

    ### 参数:
    - product_id: 商品id，有时候需要从 `product_id_str` 字段中获取，也可以从商品分享链接中获取。
    - region: 商品的国家/地区代码，默认值为 \"US\"。

    ### 支持的国家/地区代码（按区域分组）：
    - 东南亚 Southeast Asia:
      ID（印度尼西亚）, SG（新加坡）, MY（马来西亚）, PH（菲律宾）, TH（泰国）
    - 北美 North America:
      US（美国）, MX（墨西哥）
    - 欧洲 Europe:
      IE（爱尔兰）, GB（英国）, ES（西班牙）
    - 越南 Vietnam:
      VN（越南）

    ### 返回:
    - 商品详情数据V3

    # [English]
    ### Purpose:
    - Get product detail data V3. If product detail data V2 cannot be retrieved, try this version.

    ### Parameters:
    - product_id: Product ID. Sometimes needs to be extracted from `product_id_str` field, or can be
    obtained from the product share link.
    - region: Country code of the product, default is \"US\".

    ### Supported region codes (grouped by area):
    - Southeast Asia:
      ID (Indonesia), SG (Singapore), MY (Malaysia), PH (Philippines), TH (Thailand)
    - North America:
      US (United States), MX (Mexico)
    - Europe:
      IE (Ireland), GB (United Kingdom), ES (Spain)
    - Vietnam:
      VN (Vietnam)

    ### Return:
    - Product detail data V3

    # [示例 / Example]
    product_id = \"1729385239712731370\"
    region = \"US\"

    Args:
        product_id (str): 商品id / Product ID
        region (Union[Unset, str]): 商品的国家/地区代码/ Country/region code of the product Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        product_id=product_id,
        region=region,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    product_id: str,
    region: Union[Unset, str] = "US",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取商品详情数据V3 / Get product detail data V3

     # [中文]
    ### 用途:
    - 获取商品详情数据V3。如果商品详情数据V2无法获取，可以尝试使用此接口。

    ### 参数:
    - product_id: 商品id，有时候需要从 `product_id_str` 字段中获取，也可以从商品分享链接中获取。
    - region: 商品的国家/地区代码，默认值为 \"US\"。

    ### 支持的国家/地区代码（按区域分组）：
    - 东南亚 Southeast Asia:
      ID（印度尼西亚）, SG（新加坡）, MY（马来西亚）, PH（菲律宾）, TH（泰国）
    - 北美 North America:
      US（美国）, MX（墨西哥）
    - 欧洲 Europe:
      IE（爱尔兰）, GB（英国）, ES（西班牙）
    - 越南 Vietnam:
      VN（越南）

    ### 返回:
    - 商品详情数据V3

    # [English]
    ### Purpose:
    - Get product detail data V3. If product detail data V2 cannot be retrieved, try this version.

    ### Parameters:
    - product_id: Product ID. Sometimes needs to be extracted from `product_id_str` field, or can be
    obtained from the product share link.
    - region: Country code of the product, default is \"US\".

    ### Supported region codes (grouped by area):
    - Southeast Asia:
      ID (Indonesia), SG (Singapore), MY (Malaysia), PH (Philippines), TH (Thailand)
    - North America:
      US (United States), MX (Mexico)
    - Europe:
      IE (Ireland), GB (United Kingdom), ES (Spain)
    - Vietnam:
      VN (Vietnam)

    ### Return:
    - Product detail data V3

    # [示例 / Example]
    product_id = \"1729385239712731370\"
    region = \"US\"

    Args:
        product_id (str): 商品id / Product ID
        region (Union[Unset, str]): 商品的国家/地区代码/ Country/region code of the product Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        region=region,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    product_id: str,
    region: Union[Unset, str] = "US",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取商品详情数据V3 / Get product detail data V3

     # [中文]
    ### 用途:
    - 获取商品详情数据V3。如果商品详情数据V2无法获取，可以尝试使用此接口。

    ### 参数:
    - product_id: 商品id，有时候需要从 `product_id_str` 字段中获取，也可以从商品分享链接中获取。
    - region: 商品的国家/地区代码，默认值为 \"US\"。

    ### 支持的国家/地区代码（按区域分组）：
    - 东南亚 Southeast Asia:
      ID（印度尼西亚）, SG（新加坡）, MY（马来西亚）, PH（菲律宾）, TH（泰国）
    - 北美 North America:
      US（美国）, MX（墨西哥）
    - 欧洲 Europe:
      IE（爱尔兰）, GB（英国）, ES（西班牙）
    - 越南 Vietnam:
      VN（越南）

    ### 返回:
    - 商品详情数据V3

    # [English]
    ### Purpose:
    - Get product detail data V3. If product detail data V2 cannot be retrieved, try this version.

    ### Parameters:
    - product_id: Product ID. Sometimes needs to be extracted from `product_id_str` field, or can be
    obtained from the product share link.
    - region: Country code of the product, default is \"US\".

    ### Supported region codes (grouped by area):
    - Southeast Asia:
      ID (Indonesia), SG (Singapore), MY (Malaysia), PH (Philippines), TH (Thailand)
    - North America:
      US (United States), MX (Mexico)
    - Europe:
      IE (Ireland), GB (United Kingdom), ES (Spain)
    - Vietnam:
      VN (Vietnam)

    ### Return:
    - Product detail data V3

    # [示例 / Example]
    product_id = \"1729385239712731370\"
    region = \"US\"

    Args:
        product_id (str): 商品id / Product ID
        region (Union[Unset, str]): 商品的国家/地区代码/ Country/region code of the product Default: 'US'.

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
            region=region,
        )
    ).parsed
