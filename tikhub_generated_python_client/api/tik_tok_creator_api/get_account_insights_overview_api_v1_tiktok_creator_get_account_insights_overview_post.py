from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_account_overview_request import GetAccountOverviewRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: GetAccountOverviewRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tiktok/creator/get_account_insights_overview",
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
    body: GetAccountOverviewRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取创作者账号概览/Get Creator Account Overview

     # [中文]
    ### 用途:
    - 获取 TikTok Shop 创作者账号在指定时间范围内的表现概览，包括收益、曝光、点击、成交等多维度数据。
    - 默认统计从 `start_date` 当月起 1 个自然月（如传入 2025-04-01，则统计整个 4 月的数据）。

    ### 备注:
    - 此接口仅适用于已开通 TikTok Shop 功能的创作者账号。
    - 数据按照时间粒度进行分段统计，可用于数据分析和趋势观察。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询开始时间，格式为 'MM-DD-YYYY'，如 '04-01-2025'
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回:
    - `segments`（分段数据列表）:
      - `time_selector`: 当前统计段的时间设置，包括周期、起止时间戳、时区、语言等
      - `timed_stats`: 每天/每段的详细数据，包含以下字段：
        - `live_revenue.amount`: 直播带货收益
        - `video_revenue.amount`: 视频带货收益
        - `revenue.amount`: 总收益（直播 + 视频）
        - `base_revenue.amount`: 基础收益
        - `commission_estimated.amount`: 预估佣金
        - `alc_base_revenue.amount`: ALC 模式下基础收益
        - `overall_item_sold_cnt`: 商品成交数
        - `product_show_cnt`: 商品展示次数
        - `product_click_cnt`: 商品点击次数
        - `alc_pay_sku_order_cnt`: ALC 成交订单数
    - `meta.is_bound_shop`: 是否绑定 TikTok 店铺

    # [English]
    ### Purpose:
    - Retrieve performance overview of a TikTok Shop creator account within a specified date range,
    including metrics like revenue, exposure, clicks, and orders.
    - By default, it aggregates data from the month of `start_date` (e.g., if `start_date` is
    2025-04-01, it retrieves data for the entire month of April).

    ### Notes:
    - This API is only applicable to TikTok accounts that have TikTok Shop enabled.
    - Data is segmented by time granularity (daily/monthly), and can be used for performance analysis or
    trend monitoring.

    ### Parameters:
    - cookie: User cookie string for authentication
    - start_date: Query start date in 'MM-DD-YYYY' format, e.g. '04-01-2025'
    - proxy: Optional HTTP proxy address. Leave empty if not needed.
        - Example format: `http://username:password@host:port`

    ### Response:
    - `segments`: List of data segments, each containing:
      - `time_selector`: Time settings for the segment, including period, timestamp range, timezone, and
    locale
      - `timed_stats`: Daily or interval-based statistics, including:
        - `live_revenue.amount`: Revenue from livestream sales
        - `video_revenue.amount`: Revenue from video sales
        - `revenue.amount`: Total revenue (live + video)
        - `base_revenue.amount`: Base revenue
        - `commission_estimated.amount`: Estimated commission
        - `alc_base_revenue.amount`: Base revenue under ALC model
        - `overall_item_sold_cnt`: Total items sold
        - `product_show_cnt`: Product exposure count
        - `product_click_cnt`: Product click count
        - `alc_pay_sku_order_cnt`: Orders under ALC model
    - `meta.is_bound_shop`: Whether the TikTok account is bound to a shop

    Args:
        body (GetAccountOverviewRequest):

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
    body: GetAccountOverviewRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取创作者账号概览/Get Creator Account Overview

     # [中文]
    ### 用途:
    - 获取 TikTok Shop 创作者账号在指定时间范围内的表现概览，包括收益、曝光、点击、成交等多维度数据。
    - 默认统计从 `start_date` 当月起 1 个自然月（如传入 2025-04-01，则统计整个 4 月的数据）。

    ### 备注:
    - 此接口仅适用于已开通 TikTok Shop 功能的创作者账号。
    - 数据按照时间粒度进行分段统计，可用于数据分析和趋势观察。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询开始时间，格式为 'MM-DD-YYYY'，如 '04-01-2025'
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回:
    - `segments`（分段数据列表）:
      - `time_selector`: 当前统计段的时间设置，包括周期、起止时间戳、时区、语言等
      - `timed_stats`: 每天/每段的详细数据，包含以下字段：
        - `live_revenue.amount`: 直播带货收益
        - `video_revenue.amount`: 视频带货收益
        - `revenue.amount`: 总收益（直播 + 视频）
        - `base_revenue.amount`: 基础收益
        - `commission_estimated.amount`: 预估佣金
        - `alc_base_revenue.amount`: ALC 模式下基础收益
        - `overall_item_sold_cnt`: 商品成交数
        - `product_show_cnt`: 商品展示次数
        - `product_click_cnt`: 商品点击次数
        - `alc_pay_sku_order_cnt`: ALC 成交订单数
    - `meta.is_bound_shop`: 是否绑定 TikTok 店铺

    # [English]
    ### Purpose:
    - Retrieve performance overview of a TikTok Shop creator account within a specified date range,
    including metrics like revenue, exposure, clicks, and orders.
    - By default, it aggregates data from the month of `start_date` (e.g., if `start_date` is
    2025-04-01, it retrieves data for the entire month of April).

    ### Notes:
    - This API is only applicable to TikTok accounts that have TikTok Shop enabled.
    - Data is segmented by time granularity (daily/monthly), and can be used for performance analysis or
    trend monitoring.

    ### Parameters:
    - cookie: User cookie string for authentication
    - start_date: Query start date in 'MM-DD-YYYY' format, e.g. '04-01-2025'
    - proxy: Optional HTTP proxy address. Leave empty if not needed.
        - Example format: `http://username:password@host:port`

    ### Response:
    - `segments`: List of data segments, each containing:
      - `time_selector`: Time settings for the segment, including period, timestamp range, timezone, and
    locale
      - `timed_stats`: Daily or interval-based statistics, including:
        - `live_revenue.amount`: Revenue from livestream sales
        - `video_revenue.amount`: Revenue from video sales
        - `revenue.amount`: Total revenue (live + video)
        - `base_revenue.amount`: Base revenue
        - `commission_estimated.amount`: Estimated commission
        - `alc_base_revenue.amount`: Base revenue under ALC model
        - `overall_item_sold_cnt`: Total items sold
        - `product_show_cnt`: Product exposure count
        - `product_click_cnt`: Product click count
        - `alc_pay_sku_order_cnt`: Orders under ALC model
    - `meta.is_bound_shop`: Whether the TikTok account is bound to a shop

    Args:
        body (GetAccountOverviewRequest):

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
    body: GetAccountOverviewRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """获取创作者账号概览/Get Creator Account Overview

     # [中文]
    ### 用途:
    - 获取 TikTok Shop 创作者账号在指定时间范围内的表现概览，包括收益、曝光、点击、成交等多维度数据。
    - 默认统计从 `start_date` 当月起 1 个自然月（如传入 2025-04-01，则统计整个 4 月的数据）。

    ### 备注:
    - 此接口仅适用于已开通 TikTok Shop 功能的创作者账号。
    - 数据按照时间粒度进行分段统计，可用于数据分析和趋势观察。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询开始时间，格式为 'MM-DD-YYYY'，如 '04-01-2025'
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回:
    - `segments`（分段数据列表）:
      - `time_selector`: 当前统计段的时间设置，包括周期、起止时间戳、时区、语言等
      - `timed_stats`: 每天/每段的详细数据，包含以下字段：
        - `live_revenue.amount`: 直播带货收益
        - `video_revenue.amount`: 视频带货收益
        - `revenue.amount`: 总收益（直播 + 视频）
        - `base_revenue.amount`: 基础收益
        - `commission_estimated.amount`: 预估佣金
        - `alc_base_revenue.amount`: ALC 模式下基础收益
        - `overall_item_sold_cnt`: 商品成交数
        - `product_show_cnt`: 商品展示次数
        - `product_click_cnt`: 商品点击次数
        - `alc_pay_sku_order_cnt`: ALC 成交订单数
    - `meta.is_bound_shop`: 是否绑定 TikTok 店铺

    # [English]
    ### Purpose:
    - Retrieve performance overview of a TikTok Shop creator account within a specified date range,
    including metrics like revenue, exposure, clicks, and orders.
    - By default, it aggregates data from the month of `start_date` (e.g., if `start_date` is
    2025-04-01, it retrieves data for the entire month of April).

    ### Notes:
    - This API is only applicable to TikTok accounts that have TikTok Shop enabled.
    - Data is segmented by time granularity (daily/monthly), and can be used for performance analysis or
    trend monitoring.

    ### Parameters:
    - cookie: User cookie string for authentication
    - start_date: Query start date in 'MM-DD-YYYY' format, e.g. '04-01-2025'
    - proxy: Optional HTTP proxy address. Leave empty if not needed.
        - Example format: `http://username:password@host:port`

    ### Response:
    - `segments`: List of data segments, each containing:
      - `time_selector`: Time settings for the segment, including period, timestamp range, timezone, and
    locale
      - `timed_stats`: Daily or interval-based statistics, including:
        - `live_revenue.amount`: Revenue from livestream sales
        - `video_revenue.amount`: Revenue from video sales
        - `revenue.amount`: Total revenue (live + video)
        - `base_revenue.amount`: Base revenue
        - `commission_estimated.amount`: Estimated commission
        - `alc_base_revenue.amount`: Base revenue under ALC model
        - `overall_item_sold_cnt`: Total items sold
        - `product_show_cnt`: Product exposure count
        - `product_click_cnt`: Product click count
        - `alc_pay_sku_order_cnt`: Orders under ALC model
    - `meta.is_bound_shop`: Whether the TikTok account is bound to a shop

    Args:
        body (GetAccountOverviewRequest):

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
    body: GetAccountOverviewRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """获取创作者账号概览/Get Creator Account Overview

     # [中文]
    ### 用途:
    - 获取 TikTok Shop 创作者账号在指定时间范围内的表现概览，包括收益、曝光、点击、成交等多维度数据。
    - 默认统计从 `start_date` 当月起 1 个自然月（如传入 2025-04-01，则统计整个 4 月的数据）。

    ### 备注:
    - 此接口仅适用于已开通 TikTok Shop 功能的创作者账号。
    - 数据按照时间粒度进行分段统计，可用于数据分析和趋势观察。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询开始时间，格式为 'MM-DD-YYYY'，如 '04-01-2025'
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回:
    - `segments`（分段数据列表）:
      - `time_selector`: 当前统计段的时间设置，包括周期、起止时间戳、时区、语言等
      - `timed_stats`: 每天/每段的详细数据，包含以下字段：
        - `live_revenue.amount`: 直播带货收益
        - `video_revenue.amount`: 视频带货收益
        - `revenue.amount`: 总收益（直播 + 视频）
        - `base_revenue.amount`: 基础收益
        - `commission_estimated.amount`: 预估佣金
        - `alc_base_revenue.amount`: ALC 模式下基础收益
        - `overall_item_sold_cnt`: 商品成交数
        - `product_show_cnt`: 商品展示次数
        - `product_click_cnt`: 商品点击次数
        - `alc_pay_sku_order_cnt`: ALC 成交订单数
    - `meta.is_bound_shop`: 是否绑定 TikTok 店铺

    # [English]
    ### Purpose:
    - Retrieve performance overview of a TikTok Shop creator account within a specified date range,
    including metrics like revenue, exposure, clicks, and orders.
    - By default, it aggregates data from the month of `start_date` (e.g., if `start_date` is
    2025-04-01, it retrieves data for the entire month of April).

    ### Notes:
    - This API is only applicable to TikTok accounts that have TikTok Shop enabled.
    - Data is segmented by time granularity (daily/monthly), and can be used for performance analysis or
    trend monitoring.

    ### Parameters:
    - cookie: User cookie string for authentication
    - start_date: Query start date in 'MM-DD-YYYY' format, e.g. '04-01-2025'
    - proxy: Optional HTTP proxy address. Leave empty if not needed.
        - Example format: `http://username:password@host:port`

    ### Response:
    - `segments`: List of data segments, each containing:
      - `time_selector`: Time settings for the segment, including period, timestamp range, timezone, and
    locale
      - `timed_stats`: Daily or interval-based statistics, including:
        - `live_revenue.amount`: Revenue from livestream sales
        - `video_revenue.amount`: Revenue from video sales
        - `revenue.amount`: Total revenue (live + video)
        - `base_revenue.amount`: Base revenue
        - `commission_estimated.amount`: Estimated commission
        - `alc_base_revenue.amount`: Base revenue under ALC model
        - `overall_item_sold_cnt`: Total items sold
        - `product_show_cnt`: Product exposure count
        - `product_click_cnt`: Product click count
        - `alc_pay_sku_order_cnt`: Orders under ALC model
    - `meta.is_bound_shop`: Whether the TikTok account is bound to a shop

    Args:
        body (GetAccountOverviewRequest):

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
