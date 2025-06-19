from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_live_overview_request import GetLiveOverviewRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: GetLiveOverviewRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tiktok/creator/get_live_analytics_summary",
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
    body: GetLiveOverviewRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者直播概览/Get Creator Live Overview

     # [中文]
    ### 用途:
    - 获取 TikTok Shop 创作者账号在指定时间范围内的直播表现数据概览。
    - 默认统计从 `start_date` 当月起 1 个自然月（如传入 2025-04-01，则统计整个 4 月的数据）。

    ### 返回内容说明:
    - `segments`（分段数据列表）:
      - `time_selector`: 时间范围设置（周期、起止时间戳、时区、语言）
      - `filter.creator_id`: 创作者 ID
      - `timed_stats`: 每个时间段（通常按日或月分段）的直播表现数据，包含：
        - `live_revenue.amount`: 直播带货收入
        - `live_show_gpm.amount`: 直播场均带货收入
        - `new_follower_cnt`: 新增粉丝数量
        - `sku_order_paid_cnt`: 已付款 SKU 数量
        - `item_sold_cnt`: 成交商品件数
        - `product_view`: 商品曝光次数（浏览量）
        - `product_click`: 商品点击次数
        - `live_pay_order_ucnt`: 直播支付订单人数
        - `live_ctr`: 直播点击率（Click-Through Rate）
        - `live_co`: 直播转化率（Conversion Rate）
        - `live_like_cnt`: 直播点赞次数
        - `live_comment_cnt`: 直播评论次数
        - `live_show_cnt`: 直播场次
        - `live_watch_cnt`: 直播观看人数

    ### 备注:
    - 此接口仅适用于 TikTok Shop 创作者账号。
    - 直播期间数据按自然日拆分。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询开始时间（格式 `MM-DD-YYYY`），如 `04-01-2025`
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回:
    - 创作者账号直播数据概览

    # [English]
    ### Purpose:
    - Retrieve a summary of live streaming performance for a TikTok Shop creator account within a
    specified time range.
    - By default, it covers one full calendar month starting from the provided `start_date` (e.g., input
    `04-01-2025` will fetch data for the entire April 2025).

    ### Response Fields:
    - `segments` (List of segmented data):
      - `time_selector`: Time period settings (period, start/end timestamps, timezone, locale)
      - `filter.creator_id`: Creator ID
      - `timed_stats`: Live performance statistics per time segment, including:
        - `live_revenue.amount`: Live streaming revenue
        - `live_show_gpm.amount`: Average revenue per live show
        - `new_follower_cnt`: Number of new followers
        - `sku_order_paid_cnt`: Number of SKUs paid
        - `item_sold_cnt`: Number of items sold
        - `product_view`: Number of product views
        - `product_click`: Number of product clicks
        - `live_pay_order_ucnt`: Number of unique users who placed live orders
        - `live_ctr`: Live Click-Through Rate (CTR)
        - `live_co`: Live Conversion Rate (CO)
        - `live_like_cnt`: Number of live likes
        - `live_comment_cnt`: Number of live comments
        - `live_show_cnt`: Number of live sessions
        - `live_watch_cnt`: Number of live viewers

    ### Notes:
    - This API is only applicable to TikTok Shop creator accounts.
    - Data is split by natural days during the live sessions.

    ### Parameters:
    - cookie: User Cookie string for authentication
    - start_date: Query start date in the format `MM-DD-YYYY`, e.g., `04-01-2025`
    - proxy: Optional HTTP proxy address, can be omitted if not used
        - Example format: `http://username:password@host:port`

    ### Return:
    - Creator live streaming performance overview

    # [示例/Example]
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\"
    }
    ```

    Args:
        body (GetLiveOverviewRequest):

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
    body: GetLiveOverviewRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者直播概览/Get Creator Live Overview

     # [中文]
    ### 用途:
    - 获取 TikTok Shop 创作者账号在指定时间范围内的直播表现数据概览。
    - 默认统计从 `start_date` 当月起 1 个自然月（如传入 2025-04-01，则统计整个 4 月的数据）。

    ### 返回内容说明:
    - `segments`（分段数据列表）:
      - `time_selector`: 时间范围设置（周期、起止时间戳、时区、语言）
      - `filter.creator_id`: 创作者 ID
      - `timed_stats`: 每个时间段（通常按日或月分段）的直播表现数据，包含：
        - `live_revenue.amount`: 直播带货收入
        - `live_show_gpm.amount`: 直播场均带货收入
        - `new_follower_cnt`: 新增粉丝数量
        - `sku_order_paid_cnt`: 已付款 SKU 数量
        - `item_sold_cnt`: 成交商品件数
        - `product_view`: 商品曝光次数（浏览量）
        - `product_click`: 商品点击次数
        - `live_pay_order_ucnt`: 直播支付订单人数
        - `live_ctr`: 直播点击率（Click-Through Rate）
        - `live_co`: 直播转化率（Conversion Rate）
        - `live_like_cnt`: 直播点赞次数
        - `live_comment_cnt`: 直播评论次数
        - `live_show_cnt`: 直播场次
        - `live_watch_cnt`: 直播观看人数

    ### 备注:
    - 此接口仅适用于 TikTok Shop 创作者账号。
    - 直播期间数据按自然日拆分。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询开始时间（格式 `MM-DD-YYYY`），如 `04-01-2025`
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回:
    - 创作者账号直播数据概览

    # [English]
    ### Purpose:
    - Retrieve a summary of live streaming performance for a TikTok Shop creator account within a
    specified time range.
    - By default, it covers one full calendar month starting from the provided `start_date` (e.g., input
    `04-01-2025` will fetch data for the entire April 2025).

    ### Response Fields:
    - `segments` (List of segmented data):
      - `time_selector`: Time period settings (period, start/end timestamps, timezone, locale)
      - `filter.creator_id`: Creator ID
      - `timed_stats`: Live performance statistics per time segment, including:
        - `live_revenue.amount`: Live streaming revenue
        - `live_show_gpm.amount`: Average revenue per live show
        - `new_follower_cnt`: Number of new followers
        - `sku_order_paid_cnt`: Number of SKUs paid
        - `item_sold_cnt`: Number of items sold
        - `product_view`: Number of product views
        - `product_click`: Number of product clicks
        - `live_pay_order_ucnt`: Number of unique users who placed live orders
        - `live_ctr`: Live Click-Through Rate (CTR)
        - `live_co`: Live Conversion Rate (CO)
        - `live_like_cnt`: Number of live likes
        - `live_comment_cnt`: Number of live comments
        - `live_show_cnt`: Number of live sessions
        - `live_watch_cnt`: Number of live viewers

    ### Notes:
    - This API is only applicable to TikTok Shop creator accounts.
    - Data is split by natural days during the live sessions.

    ### Parameters:
    - cookie: User Cookie string for authentication
    - start_date: Query start date in the format `MM-DD-YYYY`, e.g., `04-01-2025`
    - proxy: Optional HTTP proxy address, can be omitted if not used
        - Example format: `http://username:password@host:port`

    ### Return:
    - Creator live streaming performance overview

    # [示例/Example]
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\"
    }
    ```

    Args:
        body (GetLiveOverviewRequest):

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
    body: GetLiveOverviewRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者直播概览/Get Creator Live Overview

     # [中文]
    ### 用途:
    - 获取 TikTok Shop 创作者账号在指定时间范围内的直播表现数据概览。
    - 默认统计从 `start_date` 当月起 1 个自然月（如传入 2025-04-01，则统计整个 4 月的数据）。

    ### 返回内容说明:
    - `segments`（分段数据列表）:
      - `time_selector`: 时间范围设置（周期、起止时间戳、时区、语言）
      - `filter.creator_id`: 创作者 ID
      - `timed_stats`: 每个时间段（通常按日或月分段）的直播表现数据，包含：
        - `live_revenue.amount`: 直播带货收入
        - `live_show_gpm.amount`: 直播场均带货收入
        - `new_follower_cnt`: 新增粉丝数量
        - `sku_order_paid_cnt`: 已付款 SKU 数量
        - `item_sold_cnt`: 成交商品件数
        - `product_view`: 商品曝光次数（浏览量）
        - `product_click`: 商品点击次数
        - `live_pay_order_ucnt`: 直播支付订单人数
        - `live_ctr`: 直播点击率（Click-Through Rate）
        - `live_co`: 直播转化率（Conversion Rate）
        - `live_like_cnt`: 直播点赞次数
        - `live_comment_cnt`: 直播评论次数
        - `live_show_cnt`: 直播场次
        - `live_watch_cnt`: 直播观看人数

    ### 备注:
    - 此接口仅适用于 TikTok Shop 创作者账号。
    - 直播期间数据按自然日拆分。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询开始时间（格式 `MM-DD-YYYY`），如 `04-01-2025`
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回:
    - 创作者账号直播数据概览

    # [English]
    ### Purpose:
    - Retrieve a summary of live streaming performance for a TikTok Shop creator account within a
    specified time range.
    - By default, it covers one full calendar month starting from the provided `start_date` (e.g., input
    `04-01-2025` will fetch data for the entire April 2025).

    ### Response Fields:
    - `segments` (List of segmented data):
      - `time_selector`: Time period settings (period, start/end timestamps, timezone, locale)
      - `filter.creator_id`: Creator ID
      - `timed_stats`: Live performance statistics per time segment, including:
        - `live_revenue.amount`: Live streaming revenue
        - `live_show_gpm.amount`: Average revenue per live show
        - `new_follower_cnt`: Number of new followers
        - `sku_order_paid_cnt`: Number of SKUs paid
        - `item_sold_cnt`: Number of items sold
        - `product_view`: Number of product views
        - `product_click`: Number of product clicks
        - `live_pay_order_ucnt`: Number of unique users who placed live orders
        - `live_ctr`: Live Click-Through Rate (CTR)
        - `live_co`: Live Conversion Rate (CO)
        - `live_like_cnt`: Number of live likes
        - `live_comment_cnt`: Number of live comments
        - `live_show_cnt`: Number of live sessions
        - `live_watch_cnt`: Number of live viewers

    ### Notes:
    - This API is only applicable to TikTok Shop creator accounts.
    - Data is split by natural days during the live sessions.

    ### Parameters:
    - cookie: User Cookie string for authentication
    - start_date: Query start date in the format `MM-DD-YYYY`, e.g., `04-01-2025`
    - proxy: Optional HTTP proxy address, can be omitted if not used
        - Example format: `http://username:password@host:port`

    ### Return:
    - Creator live streaming performance overview

    # [示例/Example]
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\"
    }
    ```

    Args:
        body (GetLiveOverviewRequest):

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
    body: GetLiveOverviewRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者直播概览/Get Creator Live Overview

     # [中文]
    ### 用途:
    - 获取 TikTok Shop 创作者账号在指定时间范围内的直播表现数据概览。
    - 默认统计从 `start_date` 当月起 1 个自然月（如传入 2025-04-01，则统计整个 4 月的数据）。

    ### 返回内容说明:
    - `segments`（分段数据列表）:
      - `time_selector`: 时间范围设置（周期、起止时间戳、时区、语言）
      - `filter.creator_id`: 创作者 ID
      - `timed_stats`: 每个时间段（通常按日或月分段）的直播表现数据，包含：
        - `live_revenue.amount`: 直播带货收入
        - `live_show_gpm.amount`: 直播场均带货收入
        - `new_follower_cnt`: 新增粉丝数量
        - `sku_order_paid_cnt`: 已付款 SKU 数量
        - `item_sold_cnt`: 成交商品件数
        - `product_view`: 商品曝光次数（浏览量）
        - `product_click`: 商品点击次数
        - `live_pay_order_ucnt`: 直播支付订单人数
        - `live_ctr`: 直播点击率（Click-Through Rate）
        - `live_co`: 直播转化率（Conversion Rate）
        - `live_like_cnt`: 直播点赞次数
        - `live_comment_cnt`: 直播评论次数
        - `live_show_cnt`: 直播场次
        - `live_watch_cnt`: 直播观看人数

    ### 备注:
    - 此接口仅适用于 TikTok Shop 创作者账号。
    - 直播期间数据按自然日拆分。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询开始时间（格式 `MM-DD-YYYY`），如 `04-01-2025`
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回:
    - 创作者账号直播数据概览

    # [English]
    ### Purpose:
    - Retrieve a summary of live streaming performance for a TikTok Shop creator account within a
    specified time range.
    - By default, it covers one full calendar month starting from the provided `start_date` (e.g., input
    `04-01-2025` will fetch data for the entire April 2025).

    ### Response Fields:
    - `segments` (List of segmented data):
      - `time_selector`: Time period settings (period, start/end timestamps, timezone, locale)
      - `filter.creator_id`: Creator ID
      - `timed_stats`: Live performance statistics per time segment, including:
        - `live_revenue.amount`: Live streaming revenue
        - `live_show_gpm.amount`: Average revenue per live show
        - `new_follower_cnt`: Number of new followers
        - `sku_order_paid_cnt`: Number of SKUs paid
        - `item_sold_cnt`: Number of items sold
        - `product_view`: Number of product views
        - `product_click`: Number of product clicks
        - `live_pay_order_ucnt`: Number of unique users who placed live orders
        - `live_ctr`: Live Click-Through Rate (CTR)
        - `live_co`: Live Conversion Rate (CO)
        - `live_like_cnt`: Number of live likes
        - `live_comment_cnt`: Number of live comments
        - `live_show_cnt`: Number of live sessions
        - `live_watch_cnt`: Number of live viewers

    ### Notes:
    - This API is only applicable to TikTok Shop creator accounts.
    - Data is split by natural days during the live sessions.

    ### Parameters:
    - cookie: User Cookie string for authentication
    - start_date: Query start date in the format `MM-DD-YYYY`, e.g., `04-01-2025`
    - proxy: Optional HTTP proxy address, can be omitted if not used
        - Example format: `http://username:password@host:port`

    ### Return:
    - Creator live streaming performance overview

    # [示例/Example]
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\"
    }
    ```

    Args:
        body (GetLiveOverviewRequest):

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
