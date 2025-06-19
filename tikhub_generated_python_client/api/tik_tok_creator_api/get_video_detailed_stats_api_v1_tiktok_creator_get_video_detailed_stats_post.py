from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_video_detailed_stats_request import GetVideoDetailedStatsRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: GetVideoDetailedStatsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tiktok/creator/get_video_detailed_stats",
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
    body: GetVideoDetailedStatsRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频详细分段统计数据/Get Video Detailed Statistics

     # [中文]
    ### 用途:
    - 获取指定 TikTok 视频在指定自然月内的详细分段统计数据。
    - 支持按时间段（日/周/月）统计新粉丝、点赞、评论、分享、商品浏览、完播率等多维指标。
    - 可用于深入分析单个视频在不同时间段的表现变化，优化内容策略和推广效果。

    ### 备注:
    - 必须提供 item_id（视频 ID）。
    - 时间范围基于 start_date 所在自然月。
    - 若数据量大，返回的数据将按不同时间粒度分段统计（granularity=日/周/月）。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
    - item_id: 视频 ID，例如 \"7496499484705246507\"
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回内容说明:
    - `segments`（数据分段列表）:
      - `time_selector`: 时间筛选条件（period, granularity, start_timestamp, end_timestamp）
      - `filter`: 查询条件（creator_id, item_id）
      - `timed_stats`: 按时间段返回的统计数据列表
        - `start_timestamp`: 开始时间戳
        - `end_timestamp`: 结束时间戳
        - `stats`:
          - `creator_id`: 创作者账号 ID
          - `item_id`: 视频 ID
          - `new_follower_cnt`: 新增粉丝数量
          - `share_cnt`: 分享次数
          - `comment_cnt`: 评论次数
          - `like_cnt`: 点赞次数
          - `product_view_cnt`: 商品浏览量
          - `video_completion_rate`: 视频完播率（字符串，0-1）

    ### 示例请求体:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\"
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve detailed segmented statistics for a specified TikTok video within a given calendar month.
    - Supports analyzing new followers, likes, comments, shares, product views, and video completion
    rates across different time segments (daily/weekly/monthly).
    - Useful for deeply analyzing the performance changes of a single video over time, optimizing
    content strategies and promotional outcomes.

    ### Notes:
    - Requires item_id (video ID).
    - Time range is based on the calendar month of start_date.
    - Large datasets will be automatically segmented based on granularity (daily/weekly/monthly).

    ### Return Description:
    - `segments`:
      - `time_selector`: Time filtering parameters (period, granularity, start_timestamp, end_timestamp)
      - `filter`: Query conditions (creator_id, item_id)
      - `timed_stats`: Segmented statistics list
        - `start_timestamp`: Start timestamp
        - `end_timestamp`: End timestamp
        - `stats`:
          - `creator_id`: Creator ID
          - `item_id`: Video ID
          - `new_follower_cnt`: Number of new followers
          - `share_cnt`: Number of shares
          - `comment_cnt`: Number of comments
          - `like_cnt`: Number of likes
          - `product_view_cnt`: Number of product views
          - `video_completion_rate`: Video completion rate (string, range 0-1)

    ### Example Request Body:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\"
    }
    ```

    Args:
        body (GetVideoDetailedStatsRequest):

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
    body: GetVideoDetailedStatsRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频详细分段统计数据/Get Video Detailed Statistics

     # [中文]
    ### 用途:
    - 获取指定 TikTok 视频在指定自然月内的详细分段统计数据。
    - 支持按时间段（日/周/月）统计新粉丝、点赞、评论、分享、商品浏览、完播率等多维指标。
    - 可用于深入分析单个视频在不同时间段的表现变化，优化内容策略和推广效果。

    ### 备注:
    - 必须提供 item_id（视频 ID）。
    - 时间范围基于 start_date 所在自然月。
    - 若数据量大，返回的数据将按不同时间粒度分段统计（granularity=日/周/月）。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
    - item_id: 视频 ID，例如 \"7496499484705246507\"
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回内容说明:
    - `segments`（数据分段列表）:
      - `time_selector`: 时间筛选条件（period, granularity, start_timestamp, end_timestamp）
      - `filter`: 查询条件（creator_id, item_id）
      - `timed_stats`: 按时间段返回的统计数据列表
        - `start_timestamp`: 开始时间戳
        - `end_timestamp`: 结束时间戳
        - `stats`:
          - `creator_id`: 创作者账号 ID
          - `item_id`: 视频 ID
          - `new_follower_cnt`: 新增粉丝数量
          - `share_cnt`: 分享次数
          - `comment_cnt`: 评论次数
          - `like_cnt`: 点赞次数
          - `product_view_cnt`: 商品浏览量
          - `video_completion_rate`: 视频完播率（字符串，0-1）

    ### 示例请求体:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\"
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve detailed segmented statistics for a specified TikTok video within a given calendar month.
    - Supports analyzing new followers, likes, comments, shares, product views, and video completion
    rates across different time segments (daily/weekly/monthly).
    - Useful for deeply analyzing the performance changes of a single video over time, optimizing
    content strategies and promotional outcomes.

    ### Notes:
    - Requires item_id (video ID).
    - Time range is based on the calendar month of start_date.
    - Large datasets will be automatically segmented based on granularity (daily/weekly/monthly).

    ### Return Description:
    - `segments`:
      - `time_selector`: Time filtering parameters (period, granularity, start_timestamp, end_timestamp)
      - `filter`: Query conditions (creator_id, item_id)
      - `timed_stats`: Segmented statistics list
        - `start_timestamp`: Start timestamp
        - `end_timestamp`: End timestamp
        - `stats`:
          - `creator_id`: Creator ID
          - `item_id`: Video ID
          - `new_follower_cnt`: Number of new followers
          - `share_cnt`: Number of shares
          - `comment_cnt`: Number of comments
          - `like_cnt`: Number of likes
          - `product_view_cnt`: Number of product views
          - `video_completion_rate`: Video completion rate (string, range 0-1)

    ### Example Request Body:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\"
    }
    ```

    Args:
        body (GetVideoDetailedStatsRequest):

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
    body: GetVideoDetailedStatsRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频详细分段统计数据/Get Video Detailed Statistics

     # [中文]
    ### 用途:
    - 获取指定 TikTok 视频在指定自然月内的详细分段统计数据。
    - 支持按时间段（日/周/月）统计新粉丝、点赞、评论、分享、商品浏览、完播率等多维指标。
    - 可用于深入分析单个视频在不同时间段的表现变化，优化内容策略和推广效果。

    ### 备注:
    - 必须提供 item_id（视频 ID）。
    - 时间范围基于 start_date 所在自然月。
    - 若数据量大，返回的数据将按不同时间粒度分段统计（granularity=日/周/月）。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
    - item_id: 视频 ID，例如 \"7496499484705246507\"
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回内容说明:
    - `segments`（数据分段列表）:
      - `time_selector`: 时间筛选条件（period, granularity, start_timestamp, end_timestamp）
      - `filter`: 查询条件（creator_id, item_id）
      - `timed_stats`: 按时间段返回的统计数据列表
        - `start_timestamp`: 开始时间戳
        - `end_timestamp`: 结束时间戳
        - `stats`:
          - `creator_id`: 创作者账号 ID
          - `item_id`: 视频 ID
          - `new_follower_cnt`: 新增粉丝数量
          - `share_cnt`: 分享次数
          - `comment_cnt`: 评论次数
          - `like_cnt`: 点赞次数
          - `product_view_cnt`: 商品浏览量
          - `video_completion_rate`: 视频完播率（字符串，0-1）

    ### 示例请求体:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\"
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve detailed segmented statistics for a specified TikTok video within a given calendar month.
    - Supports analyzing new followers, likes, comments, shares, product views, and video completion
    rates across different time segments (daily/weekly/monthly).
    - Useful for deeply analyzing the performance changes of a single video over time, optimizing
    content strategies and promotional outcomes.

    ### Notes:
    - Requires item_id (video ID).
    - Time range is based on the calendar month of start_date.
    - Large datasets will be automatically segmented based on granularity (daily/weekly/monthly).

    ### Return Description:
    - `segments`:
      - `time_selector`: Time filtering parameters (period, granularity, start_timestamp, end_timestamp)
      - `filter`: Query conditions (creator_id, item_id)
      - `timed_stats`: Segmented statistics list
        - `start_timestamp`: Start timestamp
        - `end_timestamp`: End timestamp
        - `stats`:
          - `creator_id`: Creator ID
          - `item_id`: Video ID
          - `new_follower_cnt`: Number of new followers
          - `share_cnt`: Number of shares
          - `comment_cnt`: Number of comments
          - `like_cnt`: Number of likes
          - `product_view_cnt`: Number of product views
          - `video_completion_rate`: Video completion rate (string, range 0-1)

    ### Example Request Body:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\"
    }
    ```

    Args:
        body (GetVideoDetailedStatsRequest):

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
    body: GetVideoDetailedStatsRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频详细分段统计数据/Get Video Detailed Statistics

     # [中文]
    ### 用途:
    - 获取指定 TikTok 视频在指定自然月内的详细分段统计数据。
    - 支持按时间段（日/周/月）统计新粉丝、点赞、评论、分享、商品浏览、完播率等多维指标。
    - 可用于深入分析单个视频在不同时间段的表现变化，优化内容策略和推广效果。

    ### 备注:
    - 必须提供 item_id（视频 ID）。
    - 时间范围基于 start_date 所在自然月。
    - 若数据量大，返回的数据将按不同时间粒度分段统计（granularity=日/周/月）。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
    - item_id: 视频 ID，例如 \"7496499484705246507\"
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回内容说明:
    - `segments`（数据分段列表）:
      - `time_selector`: 时间筛选条件（period, granularity, start_timestamp, end_timestamp）
      - `filter`: 查询条件（creator_id, item_id）
      - `timed_stats`: 按时间段返回的统计数据列表
        - `start_timestamp`: 开始时间戳
        - `end_timestamp`: 结束时间戳
        - `stats`:
          - `creator_id`: 创作者账号 ID
          - `item_id`: 视频 ID
          - `new_follower_cnt`: 新增粉丝数量
          - `share_cnt`: 分享次数
          - `comment_cnt`: 评论次数
          - `like_cnt`: 点赞次数
          - `product_view_cnt`: 商品浏览量
          - `video_completion_rate`: 视频完播率（字符串，0-1）

    ### 示例请求体:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\"
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve detailed segmented statistics for a specified TikTok video within a given calendar month.
    - Supports analyzing new followers, likes, comments, shares, product views, and video completion
    rates across different time segments (daily/weekly/monthly).
    - Useful for deeply analyzing the performance changes of a single video over time, optimizing
    content strategies and promotional outcomes.

    ### Notes:
    - Requires item_id (video ID).
    - Time range is based on the calendar month of start_date.
    - Large datasets will be automatically segmented based on granularity (daily/weekly/monthly).

    ### Return Description:
    - `segments`:
      - `time_selector`: Time filtering parameters (period, granularity, start_timestamp, end_timestamp)
      - `filter`: Query conditions (creator_id, item_id)
      - `timed_stats`: Segmented statistics list
        - `start_timestamp`: Start timestamp
        - `end_timestamp`: End timestamp
        - `stats`:
          - `creator_id`: Creator ID
          - `item_id`: Video ID
          - `new_follower_cnt`: Number of new followers
          - `share_cnt`: Number of shares
          - `comment_cnt`: Number of comments
          - `like_cnt`: Number of likes
          - `product_view_cnt`: Number of product views
          - `video_completion_rate`: Video completion rate (string, range 0-1)

    ### Example Request Body:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\"
    }
    ```

    Args:
        body (GetVideoDetailedStatsRequest):

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
