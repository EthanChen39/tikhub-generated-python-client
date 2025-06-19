from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_showcase_product_list_request import GetShowcaseProductListRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: GetShowcaseProductListRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tiktok/creator/get_showcase_product_list",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: GetShowcaseProductListRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取橱窗商品列表/Get Showcase Product List

     # [中文]
    ### 用途:
    - 获取 TikTok Shop 创作者账号橱窗中正在展示的商品列表。
    - 可用于商品管理、数据分析、查看当前推广商品等场景。

    ### 备注:
    - 仅适用于已开通橱窗功能的 TikTok Shop 创作者账号。
    - 支持分页查询，通过 `count` 和 `offset` 控制数据量。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - count: 每页返回商品数量，默认 20
    - offset: 分页偏移量，默认 0
    - proxy: 可选 HTTP 代理地址
        - 示例: `http://username:password@host:port`

    ### 返回内容说明:
    - `products` (List[Dict]): 商品列表，每项包含以下字段：
      - `product_id` (str): 商品ID
      - `title` (str): 商品标题
      - `format_available_price` (str): 商品展示价格（格式化后的字符串，如 `$7.94`）
      - `seller_info` (dict):
        - `seller_id` (str): 卖家ID
        - `shop_name` (str): 店铺名称
      - `cover` (dict): 主图信息
        - `url_list` (List[str]): 主图 URL 列表（300x300）
      - `images` (List[dict]): 图片列表
        - 每张图片包含 `url_list` (原图 URL)
      - `source` (str): 商品来源渠道（如 `Affiliate`）
      - `stock_status` (int): 库存状态（1: 有货）
      - `review_status` (int): 审核状态（1: 通过）
      - `affiliate_info` (dict): 联盟佣金信息
        - `commission_with_currency` (str): 佣金金额（如 `$0.95`）
        - `commission_rate` (int): 佣金比例（如 1200 = 12%）
      - `category_info` (dict): 类目信息
        - `name` (str): 主分类名（如 `Beauty & Personal Care`）

    ### 示例请求体:
    ```json
    {
      \"cookie\": \"your_cookie_string\",
      \"count\": 20,
      \"offset\": 0
    }
    ```

    ### 示例返回数据片段:
    ```json
    {
      \"products\": [
        {
          \"product_id\": \"1730905148396180014\",
          \"title\": \"Car Paint Care Spray\",
          \"format_available_price\": \"$7.94\",
          \"seller_info\": {
            \"seller_id\": \"7496108716782225966\",
            \"shop_name\": \"moon moon shop shop\"
          },
          \"cover\": {
            \"url_list\": [
              \"https://example.com/xxx.jpg\"
            ]
          },
          \"images\": [
            {
              \"url_list\": [
                \"https://example.com/xxx.jpg\"
              ]
            }
          ],
          \"source\": \"Affiliate\",
          \"stock_status\": 1,
          \"review_status\": 1,
          \"affiliate_info\": {
            \"commission_with_currency\": \"$0.95\",
            \"commission_rate\": 1200
          },
          \"category_info\": {
            \"name\": \"Beauty & Personal Care\"
          }
        }
      ]
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve the list of products currently displayed in a TikTok Shop creator's showcase.
    - Useful for product management, analytics, and monitoring promoted items.

    ### Notes:
    - Only available for TikTok creator accounts with the showcase feature enabled.
    - Supports pagination via `count` and `offset`.

    ### Parameters:
    - cookie: User Cookie string for authentication
    - count: Number of products per page (default 20)
    - offset: Pagination offset (default 0)
    - proxy: Optional HTTP proxy address
        - Example: `http://username:password@host:port`

    ### Return Structure:
    - `products` (List[Dict]): List of showcased products, including:
      - `product_id`, `title`, `format_available_price`, `seller_info`, `cover`, `images`, `source`,
    `stock_status`, `review_status`, `affiliate_info`, `category_info`.

    ### Example Request:
    ```json
    {
      \"cookie\": \"your_cookie_string\",
      \"count\": 20,
      \"offset\": 0
    }
    ```

    ### Example Response Snippet:
    ```json
    {
      \"products\": [
        {
          \"product_id\": \"1730905148396180014\",
          \"title\": \"Car Paint Care Spray\",
          \"format_available_price\": \"$7.94\",
          \"seller_info\": {
            \"seller_id\": \"7496108716782225966\",
            \"shop_name\": \"moon moon shop shop\"
          },
          \"cover\": {
            \"url_list\": [
              \"https://example.com/xxx.jpg\"
            ]
          },
          \"images\": [...],
          \"source\": \"Affiliate\",
          \"stock_status\": 1,
          \"review_status\": 1,
          \"affiliate_info\": {
            \"commission_with_currency\": \"$0.95\",
            \"commission_rate\": 1200
          },
          \"category_info\": {
            \"name\": \"Beauty & Personal Care\"
          }
        }
      ]
    }
    ```

    Args:
        body (GetShowcaseProductListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: GetShowcaseProductListRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取橱窗商品列表/Get Showcase Product List

     # [中文]
    ### 用途:
    - 获取 TikTok Shop 创作者账号橱窗中正在展示的商品列表。
    - 可用于商品管理、数据分析、查看当前推广商品等场景。

    ### 备注:
    - 仅适用于已开通橱窗功能的 TikTok Shop 创作者账号。
    - 支持分页查询，通过 `count` 和 `offset` 控制数据量。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - count: 每页返回商品数量，默认 20
    - offset: 分页偏移量，默认 0
    - proxy: 可选 HTTP 代理地址
        - 示例: `http://username:password@host:port`

    ### 返回内容说明:
    - `products` (List[Dict]): 商品列表，每项包含以下字段：
      - `product_id` (str): 商品ID
      - `title` (str): 商品标题
      - `format_available_price` (str): 商品展示价格（格式化后的字符串，如 `$7.94`）
      - `seller_info` (dict):
        - `seller_id` (str): 卖家ID
        - `shop_name` (str): 店铺名称
      - `cover` (dict): 主图信息
        - `url_list` (List[str]): 主图 URL 列表（300x300）
      - `images` (List[dict]): 图片列表
        - 每张图片包含 `url_list` (原图 URL)
      - `source` (str): 商品来源渠道（如 `Affiliate`）
      - `stock_status` (int): 库存状态（1: 有货）
      - `review_status` (int): 审核状态（1: 通过）
      - `affiliate_info` (dict): 联盟佣金信息
        - `commission_with_currency` (str): 佣金金额（如 `$0.95`）
        - `commission_rate` (int): 佣金比例（如 1200 = 12%）
      - `category_info` (dict): 类目信息
        - `name` (str): 主分类名（如 `Beauty & Personal Care`）

    ### 示例请求体:
    ```json
    {
      \"cookie\": \"your_cookie_string\",
      \"count\": 20,
      \"offset\": 0
    }
    ```

    ### 示例返回数据片段:
    ```json
    {
      \"products\": [
        {
          \"product_id\": \"1730905148396180014\",
          \"title\": \"Car Paint Care Spray\",
          \"format_available_price\": \"$7.94\",
          \"seller_info\": {
            \"seller_id\": \"7496108716782225966\",
            \"shop_name\": \"moon moon shop shop\"
          },
          \"cover\": {
            \"url_list\": [
              \"https://example.com/xxx.jpg\"
            ]
          },
          \"images\": [
            {
              \"url_list\": [
                \"https://example.com/xxx.jpg\"
              ]
            }
          ],
          \"source\": \"Affiliate\",
          \"stock_status\": 1,
          \"review_status\": 1,
          \"affiliate_info\": {
            \"commission_with_currency\": \"$0.95\",
            \"commission_rate\": 1200
          },
          \"category_info\": {
            \"name\": \"Beauty & Personal Care\"
          }
        }
      ]
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve the list of products currently displayed in a TikTok Shop creator's showcase.
    - Useful for product management, analytics, and monitoring promoted items.

    ### Notes:
    - Only available for TikTok creator accounts with the showcase feature enabled.
    - Supports pagination via `count` and `offset`.

    ### Parameters:
    - cookie: User Cookie string for authentication
    - count: Number of products per page (default 20)
    - offset: Pagination offset (default 0)
    - proxy: Optional HTTP proxy address
        - Example: `http://username:password@host:port`

    ### Return Structure:
    - `products` (List[Dict]): List of showcased products, including:
      - `product_id`, `title`, `format_available_price`, `seller_info`, `cover`, `images`, `source`,
    `stock_status`, `review_status`, `affiliate_info`, `category_info`.

    ### Example Request:
    ```json
    {
      \"cookie\": \"your_cookie_string\",
      \"count\": 20,
      \"offset\": 0
    }
    ```

    ### Example Response Snippet:
    ```json
    {
      \"products\": [
        {
          \"product_id\": \"1730905148396180014\",
          \"title\": \"Car Paint Care Spray\",
          \"format_available_price\": \"$7.94\",
          \"seller_info\": {
            \"seller_id\": \"7496108716782225966\",
            \"shop_name\": \"moon moon shop shop\"
          },
          \"cover\": {
            \"url_list\": [
              \"https://example.com/xxx.jpg\"
            ]
          },
          \"images\": [...],
          \"source\": \"Affiliate\",
          \"stock_status\": 1,
          \"review_status\": 1,
          \"affiliate_info\": {
            \"commission_with_currency\": \"$0.95\",
            \"commission_rate\": 1200
          },
          \"category_info\": {
            \"name\": \"Beauty & Personal Care\"
          }
        }
      ]
    }
    ```

    Args:
        body (GetShowcaseProductListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GetShowcaseProductListRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取橱窗商品列表/Get Showcase Product List

     # [中文]
    ### 用途:
    - 获取 TikTok Shop 创作者账号橱窗中正在展示的商品列表。
    - 可用于商品管理、数据分析、查看当前推广商品等场景。

    ### 备注:
    - 仅适用于已开通橱窗功能的 TikTok Shop 创作者账号。
    - 支持分页查询，通过 `count` 和 `offset` 控制数据量。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - count: 每页返回商品数量，默认 20
    - offset: 分页偏移量，默认 0
    - proxy: 可选 HTTP 代理地址
        - 示例: `http://username:password@host:port`

    ### 返回内容说明:
    - `products` (List[Dict]): 商品列表，每项包含以下字段：
      - `product_id` (str): 商品ID
      - `title` (str): 商品标题
      - `format_available_price` (str): 商品展示价格（格式化后的字符串，如 `$7.94`）
      - `seller_info` (dict):
        - `seller_id` (str): 卖家ID
        - `shop_name` (str): 店铺名称
      - `cover` (dict): 主图信息
        - `url_list` (List[str]): 主图 URL 列表（300x300）
      - `images` (List[dict]): 图片列表
        - 每张图片包含 `url_list` (原图 URL)
      - `source` (str): 商品来源渠道（如 `Affiliate`）
      - `stock_status` (int): 库存状态（1: 有货）
      - `review_status` (int): 审核状态（1: 通过）
      - `affiliate_info` (dict): 联盟佣金信息
        - `commission_with_currency` (str): 佣金金额（如 `$0.95`）
        - `commission_rate` (int): 佣金比例（如 1200 = 12%）
      - `category_info` (dict): 类目信息
        - `name` (str): 主分类名（如 `Beauty & Personal Care`）

    ### 示例请求体:
    ```json
    {
      \"cookie\": \"your_cookie_string\",
      \"count\": 20,
      \"offset\": 0
    }
    ```

    ### 示例返回数据片段:
    ```json
    {
      \"products\": [
        {
          \"product_id\": \"1730905148396180014\",
          \"title\": \"Car Paint Care Spray\",
          \"format_available_price\": \"$7.94\",
          \"seller_info\": {
            \"seller_id\": \"7496108716782225966\",
            \"shop_name\": \"moon moon shop shop\"
          },
          \"cover\": {
            \"url_list\": [
              \"https://example.com/xxx.jpg\"
            ]
          },
          \"images\": [
            {
              \"url_list\": [
                \"https://example.com/xxx.jpg\"
              ]
            }
          ],
          \"source\": \"Affiliate\",
          \"stock_status\": 1,
          \"review_status\": 1,
          \"affiliate_info\": {
            \"commission_with_currency\": \"$0.95\",
            \"commission_rate\": 1200
          },
          \"category_info\": {
            \"name\": \"Beauty & Personal Care\"
          }
        }
      ]
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve the list of products currently displayed in a TikTok Shop creator's showcase.
    - Useful for product management, analytics, and monitoring promoted items.

    ### Notes:
    - Only available for TikTok creator accounts with the showcase feature enabled.
    - Supports pagination via `count` and `offset`.

    ### Parameters:
    - cookie: User Cookie string for authentication
    - count: Number of products per page (default 20)
    - offset: Pagination offset (default 0)
    - proxy: Optional HTTP proxy address
        - Example: `http://username:password@host:port`

    ### Return Structure:
    - `products` (List[Dict]): List of showcased products, including:
      - `product_id`, `title`, `format_available_price`, `seller_info`, `cover`, `images`, `source`,
    `stock_status`, `review_status`, `affiliate_info`, `category_info`.

    ### Example Request:
    ```json
    {
      \"cookie\": \"your_cookie_string\",
      \"count\": 20,
      \"offset\": 0
    }
    ```

    ### Example Response Snippet:
    ```json
    {
      \"products\": [
        {
          \"product_id\": \"1730905148396180014\",
          \"title\": \"Car Paint Care Spray\",
          \"format_available_price\": \"$7.94\",
          \"seller_info\": {
            \"seller_id\": \"7496108716782225966\",
            \"shop_name\": \"moon moon shop shop\"
          },
          \"cover\": {
            \"url_list\": [
              \"https://example.com/xxx.jpg\"
            ]
          },
          \"images\": [...],
          \"source\": \"Affiliate\",
          \"stock_status\": 1,
          \"review_status\": 1,
          \"affiliate_info\": {
            \"commission_with_currency\": \"$0.95\",
            \"commission_rate\": 1200
          },
          \"category_info\": {
            \"name\": \"Beauty & Personal Care\"
          }
        }
      ]
    }
    ```

    Args:
        body (GetShowcaseProductListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: GetShowcaseProductListRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取橱窗商品列表/Get Showcase Product List

     # [中文]
    ### 用途:
    - 获取 TikTok Shop 创作者账号橱窗中正在展示的商品列表。
    - 可用于商品管理、数据分析、查看当前推广商品等场景。

    ### 备注:
    - 仅适用于已开通橱窗功能的 TikTok Shop 创作者账号。
    - 支持分页查询，通过 `count` 和 `offset` 控制数据量。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - count: 每页返回商品数量，默认 20
    - offset: 分页偏移量，默认 0
    - proxy: 可选 HTTP 代理地址
        - 示例: `http://username:password@host:port`

    ### 返回内容说明:
    - `products` (List[Dict]): 商品列表，每项包含以下字段：
      - `product_id` (str): 商品ID
      - `title` (str): 商品标题
      - `format_available_price` (str): 商品展示价格（格式化后的字符串，如 `$7.94`）
      - `seller_info` (dict):
        - `seller_id` (str): 卖家ID
        - `shop_name` (str): 店铺名称
      - `cover` (dict): 主图信息
        - `url_list` (List[str]): 主图 URL 列表（300x300）
      - `images` (List[dict]): 图片列表
        - 每张图片包含 `url_list` (原图 URL)
      - `source` (str): 商品来源渠道（如 `Affiliate`）
      - `stock_status` (int): 库存状态（1: 有货）
      - `review_status` (int): 审核状态（1: 通过）
      - `affiliate_info` (dict): 联盟佣金信息
        - `commission_with_currency` (str): 佣金金额（如 `$0.95`）
        - `commission_rate` (int): 佣金比例（如 1200 = 12%）
      - `category_info` (dict): 类目信息
        - `name` (str): 主分类名（如 `Beauty & Personal Care`）

    ### 示例请求体:
    ```json
    {
      \"cookie\": \"your_cookie_string\",
      \"count\": 20,
      \"offset\": 0
    }
    ```

    ### 示例返回数据片段:
    ```json
    {
      \"products\": [
        {
          \"product_id\": \"1730905148396180014\",
          \"title\": \"Car Paint Care Spray\",
          \"format_available_price\": \"$7.94\",
          \"seller_info\": {
            \"seller_id\": \"7496108716782225966\",
            \"shop_name\": \"moon moon shop shop\"
          },
          \"cover\": {
            \"url_list\": [
              \"https://example.com/xxx.jpg\"
            ]
          },
          \"images\": [
            {
              \"url_list\": [
                \"https://example.com/xxx.jpg\"
              ]
            }
          ],
          \"source\": \"Affiliate\",
          \"stock_status\": 1,
          \"review_status\": 1,
          \"affiliate_info\": {
            \"commission_with_currency\": \"$0.95\",
            \"commission_rate\": 1200
          },
          \"category_info\": {
            \"name\": \"Beauty & Personal Care\"
          }
        }
      ]
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve the list of products currently displayed in a TikTok Shop creator's showcase.
    - Useful for product management, analytics, and monitoring promoted items.

    ### Notes:
    - Only available for TikTok creator accounts with the showcase feature enabled.
    - Supports pagination via `count` and `offset`.

    ### Parameters:
    - cookie: User Cookie string for authentication
    - count: Number of products per page (default 20)
    - offset: Pagination offset (default 0)
    - proxy: Optional HTTP proxy address
        - Example: `http://username:password@host:port`

    ### Return Structure:
    - `products` (List[Dict]): List of showcased products, including:
      - `product_id`, `title`, `format_available_price`, `seller_info`, `cover`, `images`, `source`,
    `stock_status`, `review_status`, `affiliate_info`, `category_info`.

    ### Example Request:
    ```json
    {
      \"cookie\": \"your_cookie_string\",
      \"count\": 20,
      \"offset\": 0
    }
    ```

    ### Example Response Snippet:
    ```json
    {
      \"products\": [
        {
          \"product_id\": \"1730905148396180014\",
          \"title\": \"Car Paint Care Spray\",
          \"format_available_price\": \"$7.94\",
          \"seller_info\": {
            \"seller_id\": \"7496108716782225966\",
            \"shop_name\": \"moon moon shop shop\"
          },
          \"cover\": {
            \"url_list\": [
              \"https://example.com/xxx.jpg\"
            ]
          },
          \"images\": [...],
          \"source\": \"Affiliate\",
          \"stock_status\": 1,
          \"review_status\": 1,
          \"affiliate_info\": {
            \"commission_with_currency\": \"$0.95\",
            \"commission_rate\": 1200
          },
          \"category_info\": {
            \"name\": \"Beauty & Personal Care\"
          }
        }
      ]
    }
    ```

    Args:
        body (GetShowcaseProductListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
