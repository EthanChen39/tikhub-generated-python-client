from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_video_associated_product_list_request import GetVideoAssociatedProductListRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: GetVideoAssociatedProductListRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tiktok/creator/get_video_associated_product_list",
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
    body: GetVideoAssociatedProductListRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频关联商品列表/Get Video Associated Product List

     # [中文]
    ### 用途:
    - 获取指定视频在 TikTok Shop 中关联展示的商品列表及其推广表现数据。
    - 可用于分析每个视频挂载商品的数量、商品价格区间、商品跳转链接，以及商品销售和推广效果。

    ### 备注:
    - 必须提供 item_ids（视频 ID 列表）。
    - 时间范围默认使用 start_date 所在自然月。
    - 支持单次查询多个视频，返回每个视频关联的所有商品信息及对应商品的推广数据。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
    - item_ids: 视频 ID 列表，例如 [\"7496499484705246507\", \"7496110433699482923\"]
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回内容说明:
    - `segments`（分段数据列表）:
      - `time_selector`: 时间筛选信息（起止时间戳）
      - `filter`: 查询条件（视频 ID 列表）
      - `timed_lists`: 每个时间段下的视频商品关联列表
        - `videoToProductsMap`:
          - `item_id`: 视频 ID
          - `products`: 关联商品列表
            - `id`: 商品 ID
            - `name`: 商品名称
            - `cover_image.thumb_url_list`: 商品图片 URL 列表
            - `product_detail_page_url`: 商品跳转链接
            - `price_min` / `price_max`: 商品价格区间
          - `stats`:
            - `product.id`: 商品 ID
            - 商品销售推广表现（如销量、点击率等）

    ### 示例请求体:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_ids\": [\"7496499484705246507\", \"7496110433699482923\"]
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve the list of products associated with specified videos on TikTok Shop, along with their
    promotional performance data.
    - Useful for analyzing the number of products linked to each video, the product price range, product
    detail page links, and sales performance metrics.

    ### Notes:
    - Requires item_ids (list of video IDs).
    - The time range defaults to the calendar month of the specified start_date.
    - Supports querying multiple videos at once.

    ### Return Description:
    - `segments`:
      - `time_selector`: Time filter information (start/end timestamps)
      - `filter`: Query conditions (video ID list)
      - `timed_lists`: Product list associated with videos in the selected time range
        - `videoToProductsMap`:
          - `item_id`: Video ID
          - `products`:
            - `id`: Product ID
            - `name`: Product name
            - `cover_image.thumb_url_list`: List of product image URLs
            - `product_detail_page_url`: Product detail page link
            - `price_min` / `price_max`: Price range
          - `stats`:
            - `product.id`: Product ID
            - Promotional performance metrics (e.g., sales volume, CTR)

    ### Example Request Body:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_ids\": [\"7496499484705246507\", \"7496110433699482923\"]
    }
    ```

    Args:
        body (GetVideoAssociatedProductListRequest):

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
    body: GetVideoAssociatedProductListRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频关联商品列表/Get Video Associated Product List

     # [中文]
    ### 用途:
    - 获取指定视频在 TikTok Shop 中关联展示的商品列表及其推广表现数据。
    - 可用于分析每个视频挂载商品的数量、商品价格区间、商品跳转链接，以及商品销售和推广效果。

    ### 备注:
    - 必须提供 item_ids（视频 ID 列表）。
    - 时间范围默认使用 start_date 所在自然月。
    - 支持单次查询多个视频，返回每个视频关联的所有商品信息及对应商品的推广数据。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
    - item_ids: 视频 ID 列表，例如 [\"7496499484705246507\", \"7496110433699482923\"]
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回内容说明:
    - `segments`（分段数据列表）:
      - `time_selector`: 时间筛选信息（起止时间戳）
      - `filter`: 查询条件（视频 ID 列表）
      - `timed_lists`: 每个时间段下的视频商品关联列表
        - `videoToProductsMap`:
          - `item_id`: 视频 ID
          - `products`: 关联商品列表
            - `id`: 商品 ID
            - `name`: 商品名称
            - `cover_image.thumb_url_list`: 商品图片 URL 列表
            - `product_detail_page_url`: 商品跳转链接
            - `price_min` / `price_max`: 商品价格区间
          - `stats`:
            - `product.id`: 商品 ID
            - 商品销售推广表现（如销量、点击率等）

    ### 示例请求体:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_ids\": [\"7496499484705246507\", \"7496110433699482923\"]
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve the list of products associated with specified videos on TikTok Shop, along with their
    promotional performance data.
    - Useful for analyzing the number of products linked to each video, the product price range, product
    detail page links, and sales performance metrics.

    ### Notes:
    - Requires item_ids (list of video IDs).
    - The time range defaults to the calendar month of the specified start_date.
    - Supports querying multiple videos at once.

    ### Return Description:
    - `segments`:
      - `time_selector`: Time filter information (start/end timestamps)
      - `filter`: Query conditions (video ID list)
      - `timed_lists`: Product list associated with videos in the selected time range
        - `videoToProductsMap`:
          - `item_id`: Video ID
          - `products`:
            - `id`: Product ID
            - `name`: Product name
            - `cover_image.thumb_url_list`: List of product image URLs
            - `product_detail_page_url`: Product detail page link
            - `price_min` / `price_max`: Price range
          - `stats`:
            - `product.id`: Product ID
            - Promotional performance metrics (e.g., sales volume, CTR)

    ### Example Request Body:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_ids\": [\"7496499484705246507\", \"7496110433699482923\"]
    }
    ```

    Args:
        body (GetVideoAssociatedProductListRequest):

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
    body: GetVideoAssociatedProductListRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频关联商品列表/Get Video Associated Product List

     # [中文]
    ### 用途:
    - 获取指定视频在 TikTok Shop 中关联展示的商品列表及其推广表现数据。
    - 可用于分析每个视频挂载商品的数量、商品价格区间、商品跳转链接，以及商品销售和推广效果。

    ### 备注:
    - 必须提供 item_ids（视频 ID 列表）。
    - 时间范围默认使用 start_date 所在自然月。
    - 支持单次查询多个视频，返回每个视频关联的所有商品信息及对应商品的推广数据。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
    - item_ids: 视频 ID 列表，例如 [\"7496499484705246507\", \"7496110433699482923\"]
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回内容说明:
    - `segments`（分段数据列表）:
      - `time_selector`: 时间筛选信息（起止时间戳）
      - `filter`: 查询条件（视频 ID 列表）
      - `timed_lists`: 每个时间段下的视频商品关联列表
        - `videoToProductsMap`:
          - `item_id`: 视频 ID
          - `products`: 关联商品列表
            - `id`: 商品 ID
            - `name`: 商品名称
            - `cover_image.thumb_url_list`: 商品图片 URL 列表
            - `product_detail_page_url`: 商品跳转链接
            - `price_min` / `price_max`: 商品价格区间
          - `stats`:
            - `product.id`: 商品 ID
            - 商品销售推广表现（如销量、点击率等）

    ### 示例请求体:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_ids\": [\"7496499484705246507\", \"7496110433699482923\"]
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve the list of products associated with specified videos on TikTok Shop, along with their
    promotional performance data.
    - Useful for analyzing the number of products linked to each video, the product price range, product
    detail page links, and sales performance metrics.

    ### Notes:
    - Requires item_ids (list of video IDs).
    - The time range defaults to the calendar month of the specified start_date.
    - Supports querying multiple videos at once.

    ### Return Description:
    - `segments`:
      - `time_selector`: Time filter information (start/end timestamps)
      - `filter`: Query conditions (video ID list)
      - `timed_lists`: Product list associated with videos in the selected time range
        - `videoToProductsMap`:
          - `item_id`: Video ID
          - `products`:
            - `id`: Product ID
            - `name`: Product name
            - `cover_image.thumb_url_list`: List of product image URLs
            - `product_detail_page_url`: Product detail page link
            - `price_min` / `price_max`: Price range
          - `stats`:
            - `product.id`: Product ID
            - Promotional performance metrics (e.g., sales volume, CTR)

    ### Example Request Body:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_ids\": [\"7496499484705246507\", \"7496110433699482923\"]
    }
    ```

    Args:
        body (GetVideoAssociatedProductListRequest):

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
    body: GetVideoAssociatedProductListRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频关联商品列表/Get Video Associated Product List

     # [中文]
    ### 用途:
    - 获取指定视频在 TikTok Shop 中关联展示的商品列表及其推广表现数据。
    - 可用于分析每个视频挂载商品的数量、商品价格区间、商品跳转链接，以及商品销售和推广效果。

    ### 备注:
    - 必须提供 item_ids（视频 ID 列表）。
    - 时间范围默认使用 start_date 所在自然月。
    - 支持单次查询多个视频，返回每个视频关联的所有商品信息及对应商品的推广数据。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
    - item_ids: 视频 ID 列表，例如 [\"7496499484705246507\", \"7496110433699482923\"]
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回内容说明:
    - `segments`（分段数据列表）:
      - `time_selector`: 时间筛选信息（起止时间戳）
      - `filter`: 查询条件（视频 ID 列表）
      - `timed_lists`: 每个时间段下的视频商品关联列表
        - `videoToProductsMap`:
          - `item_id`: 视频 ID
          - `products`: 关联商品列表
            - `id`: 商品 ID
            - `name`: 商品名称
            - `cover_image.thumb_url_list`: 商品图片 URL 列表
            - `product_detail_page_url`: 商品跳转链接
            - `price_min` / `price_max`: 商品价格区间
          - `stats`:
            - `product.id`: 商品 ID
            - 商品销售推广表现（如销量、点击率等）

    ### 示例请求体:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_ids\": [\"7496499484705246507\", \"7496110433699482923\"]
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve the list of products associated with specified videos on TikTok Shop, along with their
    promotional performance data.
    - Useful for analyzing the number of products linked to each video, the product price range, product
    detail page links, and sales performance metrics.

    ### Notes:
    - Requires item_ids (list of video IDs).
    - The time range defaults to the calendar month of the specified start_date.
    - Supports querying multiple videos at once.

    ### Return Description:
    - `segments`:
      - `time_selector`: Time filter information (start/end timestamps)
      - `filter`: Query conditions (video ID list)
      - `timed_lists`: Product list associated with videos in the selected time range
        - `videoToProductsMap`:
          - `item_id`: Video ID
          - `products`:
            - `id`: Product ID
            - `name`: Product name
            - `cover_image.thumb_url_list`: List of product image URLs
            - `product_detail_page_url`: Product detail page link
            - `price_min` / `price_max`: Price range
          - `stats`:
            - `product.id`: Product ID
            - Promotional performance metrics (e.g., sales volume, CTR)

    ### Example Request Body:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_ids\": [\"7496499484705246507\", \"7496110433699482923\"]
    }
    ```

    Args:
        body (GetVideoAssociatedProductListRequest):

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
