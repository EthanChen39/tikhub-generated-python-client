from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_video_to_product_stats_request import GetVideoToProductStatsRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: GetVideoToProductStatsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tiktok/creator/get_video_to_product_stats",
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
    body: GetVideoToProductStatsRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频与商品关联统计数据/Get Video-Product Association Statistics

     # [中文]
    ### 用途:
    - 获取指定 TikTok 视频与指定商品关联的推广详细统计数据。
    - 支持分析视频为商品带来的商品浏览量、点击量、销售量、订单量、商品收入、直接收入等多维度指标。
    - 返回数据按时间段（日/周/月）分段统计，便于观察趋势变化。

    ### 备注:
    - 必须同时提供 item_id（视频 ID）和 product_id（商品 ID）。
    - 时间范围基于 start_date 所在自然月。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
    - item_id: 视频 ID，例如 \"7496499484705246507\"
    - product_id: 商品 ID，例如 \"1731050202505515549\"
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回内容说明:
    - `segments`（数据分段列表）:
      - `time_selector`: 时间筛选参数（period, granularity, start_timestamp, end_timestamp）
      - `filter`: 查询条件（creator_id, item_id, product_id）
      - `timed_stats`: 按时间段分段的统计数据
        - `start_timestamp`: 时间段开始时间戳
        - `end_timestamp`: 时间段结束时间戳
        - `stats`:
          - `item_id`: 视频 ID
          - `product_id`: 商品 ID
          - `product_revenue.amount_formatted`: 商品产生的总收入（格式化字符串，如 \"$100.00\"）
          - `product_revenue.amount`: 商品产生的总收入（数值）
          - `direct_revenue.amount_formatted`: 直接成交产生的收入（格式化字符串）
          - `product_sales_cnt`: 商品销售数量
          - `product_view_cnt`: 商品浏览量
          - `product_click_cnt`: 商品点击量
          - `order_cnt`: 生成订单数量

    ### 示例请求体:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\",
      \"product_id\": \"1731050202505515549\"
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve detailed promotional statistics between a specific TikTok video and a specific product.
    - Supports analyzing metrics such as product views, clicks, sales, order counts, product revenue,
    and direct revenue.
    - The data is segmented by time intervals (daily/weekly/monthly) to observe trends over time.

    ### Notes:
    - Requires both item_id (video ID) and product_id (product ID).
    - The time range is based on the calendar month of the specified start_date.

    ### Return Description:
    - `segments`:
      - `time_selector`: Time filtering parameters (period, granularity, start_timestamp, end_timestamp)
      - `filter`: Query conditions (creator_id, item_id, product_id)
      - `timed_stats`: Segmented statistics list
        - `start_timestamp`: Start timestamp
        - `end_timestamp`: End timestamp
        - `stats`:
          - `item_id`: Video ID
          - `product_id`: Product ID
          - `product_revenue.amount_formatted`: Total product revenue (formatted string, e.g.,
    \"$100.00\")
          - `product_revenue.amount`: Total product revenue (numeric)
          - `direct_revenue.amount_formatted`: Direct sales revenue (formatted string)
          - `product_sales_cnt`: Number of products sold
          - `product_view_cnt`: Number of product views
          - `product_click_cnt`: Number of product clicks
          - `order_cnt`: Number of orders created

    ### Example Request Body:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\",
      \"product_id\": \"1731050202505515549\"
    }
    ```

    Args:
        body (GetVideoToProductStatsRequest):

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
    body: GetVideoToProductStatsRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频与商品关联统计数据/Get Video-Product Association Statistics

     # [中文]
    ### 用途:
    - 获取指定 TikTok 视频与指定商品关联的推广详细统计数据。
    - 支持分析视频为商品带来的商品浏览量、点击量、销售量、订单量、商品收入、直接收入等多维度指标。
    - 返回数据按时间段（日/周/月）分段统计，便于观察趋势变化。

    ### 备注:
    - 必须同时提供 item_id（视频 ID）和 product_id（商品 ID）。
    - 时间范围基于 start_date 所在自然月。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
    - item_id: 视频 ID，例如 \"7496499484705246507\"
    - product_id: 商品 ID，例如 \"1731050202505515549\"
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回内容说明:
    - `segments`（数据分段列表）:
      - `time_selector`: 时间筛选参数（period, granularity, start_timestamp, end_timestamp）
      - `filter`: 查询条件（creator_id, item_id, product_id）
      - `timed_stats`: 按时间段分段的统计数据
        - `start_timestamp`: 时间段开始时间戳
        - `end_timestamp`: 时间段结束时间戳
        - `stats`:
          - `item_id`: 视频 ID
          - `product_id`: 商品 ID
          - `product_revenue.amount_formatted`: 商品产生的总收入（格式化字符串，如 \"$100.00\"）
          - `product_revenue.amount`: 商品产生的总收入（数值）
          - `direct_revenue.amount_formatted`: 直接成交产生的收入（格式化字符串）
          - `product_sales_cnt`: 商品销售数量
          - `product_view_cnt`: 商品浏览量
          - `product_click_cnt`: 商品点击量
          - `order_cnt`: 生成订单数量

    ### 示例请求体:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\",
      \"product_id\": \"1731050202505515549\"
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve detailed promotional statistics between a specific TikTok video and a specific product.
    - Supports analyzing metrics such as product views, clicks, sales, order counts, product revenue,
    and direct revenue.
    - The data is segmented by time intervals (daily/weekly/monthly) to observe trends over time.

    ### Notes:
    - Requires both item_id (video ID) and product_id (product ID).
    - The time range is based on the calendar month of the specified start_date.

    ### Return Description:
    - `segments`:
      - `time_selector`: Time filtering parameters (period, granularity, start_timestamp, end_timestamp)
      - `filter`: Query conditions (creator_id, item_id, product_id)
      - `timed_stats`: Segmented statistics list
        - `start_timestamp`: Start timestamp
        - `end_timestamp`: End timestamp
        - `stats`:
          - `item_id`: Video ID
          - `product_id`: Product ID
          - `product_revenue.amount_formatted`: Total product revenue (formatted string, e.g.,
    \"$100.00\")
          - `product_revenue.amount`: Total product revenue (numeric)
          - `direct_revenue.amount_formatted`: Direct sales revenue (formatted string)
          - `product_sales_cnt`: Number of products sold
          - `product_view_cnt`: Number of product views
          - `product_click_cnt`: Number of product clicks
          - `order_cnt`: Number of orders created

    ### Example Request Body:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\",
      \"product_id\": \"1731050202505515549\"
    }
    ```

    Args:
        body (GetVideoToProductStatsRequest):

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
    body: GetVideoToProductStatsRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频与商品关联统计数据/Get Video-Product Association Statistics

     # [中文]
    ### 用途:
    - 获取指定 TikTok 视频与指定商品关联的推广详细统计数据。
    - 支持分析视频为商品带来的商品浏览量、点击量、销售量、订单量、商品收入、直接收入等多维度指标。
    - 返回数据按时间段（日/周/月）分段统计，便于观察趋势变化。

    ### 备注:
    - 必须同时提供 item_id（视频 ID）和 product_id（商品 ID）。
    - 时间范围基于 start_date 所在自然月。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
    - item_id: 视频 ID，例如 \"7496499484705246507\"
    - product_id: 商品 ID，例如 \"1731050202505515549\"
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回内容说明:
    - `segments`（数据分段列表）:
      - `time_selector`: 时间筛选参数（period, granularity, start_timestamp, end_timestamp）
      - `filter`: 查询条件（creator_id, item_id, product_id）
      - `timed_stats`: 按时间段分段的统计数据
        - `start_timestamp`: 时间段开始时间戳
        - `end_timestamp`: 时间段结束时间戳
        - `stats`:
          - `item_id`: 视频 ID
          - `product_id`: 商品 ID
          - `product_revenue.amount_formatted`: 商品产生的总收入（格式化字符串，如 \"$100.00\"）
          - `product_revenue.amount`: 商品产生的总收入（数值）
          - `direct_revenue.amount_formatted`: 直接成交产生的收入（格式化字符串）
          - `product_sales_cnt`: 商品销售数量
          - `product_view_cnt`: 商品浏览量
          - `product_click_cnt`: 商品点击量
          - `order_cnt`: 生成订单数量

    ### 示例请求体:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\",
      \"product_id\": \"1731050202505515549\"
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve detailed promotional statistics between a specific TikTok video and a specific product.
    - Supports analyzing metrics such as product views, clicks, sales, order counts, product revenue,
    and direct revenue.
    - The data is segmented by time intervals (daily/weekly/monthly) to observe trends over time.

    ### Notes:
    - Requires both item_id (video ID) and product_id (product ID).
    - The time range is based on the calendar month of the specified start_date.

    ### Return Description:
    - `segments`:
      - `time_selector`: Time filtering parameters (period, granularity, start_timestamp, end_timestamp)
      - `filter`: Query conditions (creator_id, item_id, product_id)
      - `timed_stats`: Segmented statistics list
        - `start_timestamp`: Start timestamp
        - `end_timestamp`: End timestamp
        - `stats`:
          - `item_id`: Video ID
          - `product_id`: Product ID
          - `product_revenue.amount_formatted`: Total product revenue (formatted string, e.g.,
    \"$100.00\")
          - `product_revenue.amount`: Total product revenue (numeric)
          - `direct_revenue.amount_formatted`: Direct sales revenue (formatted string)
          - `product_sales_cnt`: Number of products sold
          - `product_view_cnt`: Number of product views
          - `product_click_cnt`: Number of product clicks
          - `order_cnt`: Number of orders created

    ### Example Request Body:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\",
      \"product_id\": \"1731050202505515549\"
    }
    ```

    Args:
        body (GetVideoToProductStatsRequest):

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
    body: GetVideoToProductStatsRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频与商品关联统计数据/Get Video-Product Association Statistics

     # [中文]
    ### 用途:
    - 获取指定 TikTok 视频与指定商品关联的推广详细统计数据。
    - 支持分析视频为商品带来的商品浏览量、点击量、销售量、订单量、商品收入、直接收入等多维度指标。
    - 返回数据按时间段（日/周/月）分段统计，便于观察趋势变化。

    ### 备注:
    - 必须同时提供 item_id（视频 ID）和 product_id（商品 ID）。
    - 时间范围基于 start_date 所在自然月。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
    - item_id: 视频 ID，例如 \"7496499484705246507\"
    - product_id: 商品 ID，例如 \"1731050202505515549\"
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回内容说明:
    - `segments`（数据分段列表）:
      - `time_selector`: 时间筛选参数（period, granularity, start_timestamp, end_timestamp）
      - `filter`: 查询条件（creator_id, item_id, product_id）
      - `timed_stats`: 按时间段分段的统计数据
        - `start_timestamp`: 时间段开始时间戳
        - `end_timestamp`: 时间段结束时间戳
        - `stats`:
          - `item_id`: 视频 ID
          - `product_id`: 商品 ID
          - `product_revenue.amount_formatted`: 商品产生的总收入（格式化字符串，如 \"$100.00\"）
          - `product_revenue.amount`: 商品产生的总收入（数值）
          - `direct_revenue.amount_formatted`: 直接成交产生的收入（格式化字符串）
          - `product_sales_cnt`: 商品销售数量
          - `product_view_cnt`: 商品浏览量
          - `product_click_cnt`: 商品点击量
          - `order_cnt`: 生成订单数量

    ### 示例请求体:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\",
      \"product_id\": \"1731050202505515549\"
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve detailed promotional statistics between a specific TikTok video and a specific product.
    - Supports analyzing metrics such as product views, clicks, sales, order counts, product revenue,
    and direct revenue.
    - The data is segmented by time intervals (daily/weekly/monthly) to observe trends over time.

    ### Notes:
    - Requires both item_id (video ID) and product_id (product ID).
    - The time range is based on the calendar month of the specified start_date.

    ### Return Description:
    - `segments`:
      - `time_selector`: Time filtering parameters (period, granularity, start_timestamp, end_timestamp)
      - `filter`: Query conditions (creator_id, item_id, product_id)
      - `timed_stats`: Segmented statistics list
        - `start_timestamp`: Start timestamp
        - `end_timestamp`: End timestamp
        - `stats`:
          - `item_id`: Video ID
          - `product_id`: Product ID
          - `product_revenue.amount_formatted`: Total product revenue (formatted string, e.g.,
    \"$100.00\")
          - `product_revenue.amount`: Total product revenue (numeric)
          - `direct_revenue.amount_formatted`: Direct sales revenue (formatted string)
          - `product_sales_cnt`: Number of products sold
          - `product_view_cnt`: Number of product views
          - `product_click_cnt`: Number of product clicks
          - `order_cnt`: Number of orders created

    ### Example Request Body:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\",
      \"product_id\": \"1731050202505515549\"
    }
    ```

    Args:
        body (GetVideoToProductStatsRequest):

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
