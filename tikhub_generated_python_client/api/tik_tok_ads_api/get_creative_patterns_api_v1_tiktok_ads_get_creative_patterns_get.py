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
    first_industry_id: Union[Unset, str] = "25000000000",
    period_type: Union[Unset, str] = "week",
    order_field: Union[Unset, str] = "ctr",
    order_type: Union[Unset, str] = "desc",
    week: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["first_industry_id"] = first_industry_id

    params["period_type"] = period_type

    params["order_field"] = order_field

    params["order_type"] = order_type

    params["week"] = week

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/get_creative_patterns",
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
    first_industry_id: Union[Unset, str] = "25000000000",
    period_type: Union[Unset, str] = "week",
    order_field: Union[Unset, str] = "ctr",
    order_type: Union[Unset, str] = "desc",
    week: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创意模式排行榜/Get creative pattern rankings

     # [中文]
    ### 用途:
    - 获取特定行业的创意模式排行榜，了解哪些创意模式效果最好
    - 分析不同创意模式的点击率、完播率等关键指标
    - 为广告创意制作提供数据支持的最佳实践

    ### 参数:
    - first_industry_id: 行业ID，如游戏行业：25000000000
    - period_type: 时间类型，\"week\"=周数据，\"month\"=月数据
    - order_field: 排序字段，\"ctr\"=点击率，\"play_over_rate\"=播放完成率
    - order_type: 排序方式，desc（降序）或asc（升序）
    - week: 查看特定周的数据，格式：YYYY-MM-DD（可选）

    ### 返回内容说明:
    - `list`: 创意模式列表
      - `label_info`: 模式标签信息
        - `value`: 模式名称
        - `description`: 模式描述
      - `ctr`: 点击率（百分比）
      - `play_over_rate`: 播放完成率（百分比）
      - `avg_watch_time`: 平均观看时长
      - `example_count`: 示例数量

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_creative_patterns\",
      \"params\": {
        \"first_industry_id\": \"25000000000\",
        \"period_type\": \"week\",
        \"order_field\": \"ctr\"
      },
      \"data\": {
        \"list\": [
          {
            \"label_info\": {
              \"value\": \"Problem-Solution\",
              \"description\": \"Present a problem and show the solution\"
            },
            \"ctr\": 4.5,
            \"play_over_rate\": 68.2,
            \"avg_watch_time\": 12.3,
            \"example_count\": 234
          }
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get creative pattern rankings for specific industries to understand which patterns perform best
    - Analyze key metrics like CTR and completion rate for different creative patterns
    - Provide data-driven best practices for ad creative production

    ### Parameters:
    - first_industry_id: Industry ID, e.g., Games: 25000000000
    - period_type: Period type, \"week\"=Weekly data, \"month\"=Monthly data
    - order_field: Sort field, \"ctr\"=Click-through rate, \"play_over_rate\"=Completion rate
    - order_type: Sort order, desc (descending) or asc (ascending)
    - week: View data for specific week, format: YYYY-MM-DD (optional)

    ### Return Description:
    - `list`: Creative pattern list
      - `label_info`: Pattern label information
        - `value`: Pattern name
        - `description`: Pattern description
      - `ctr`: Click-through rate (percentage)
      - `play_over_rate`: Play completion rate (percentage)
      - `avg_watch_time`: Average watch time
      - `example_count`: Number of examples

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_creative_patterns\",
      \"params\": {
        \"first_industry_id\": \"25000000000\",
        \"period_type\": \"week\",
        \"order_field\": \"ctr\"
      },
      \"data\": {
        \"list\": [
          {
            \"label_info\": {
              \"value\": \"Problem-Solution\",
              \"description\": \"Present a problem and show the solution\"
            },
            \"ctr\": 4.5,
            \"play_over_rate\": 68.2,
            \"avg_watch_time\": 12.3,
            \"example_count\": 234
          }
        ]
      }
    }
    ```

    Args:
        first_industry_id (Union[Unset, str]): 一级行业ID/First industry ID Default: '25000000000'.
        period_type (Union[Unset, str]): 时间周期类型/Period type (week, month) Default: 'week'.
        order_field (Union[Unset, str]): 排序字段/Order field (ctr, play_over_rate) Default: 'ctr'.
        order_type (Union[Unset, str]): 排序方式/Sort order (desc, asc) Default: 'desc'.
        week (Union[Unset, str]): 特定周（可选）/Specific week (optional)
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        first_industry_id=first_industry_id,
        period_type=period_type,
        order_field=order_field,
        order_type=order_type,
        week=week,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    first_industry_id: Union[Unset, str] = "25000000000",
    period_type: Union[Unset, str] = "week",
    order_field: Union[Unset, str] = "ctr",
    order_type: Union[Unset, str] = "desc",
    week: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创意模式排行榜/Get creative pattern rankings

     # [中文]
    ### 用途:
    - 获取特定行业的创意模式排行榜，了解哪些创意模式效果最好
    - 分析不同创意模式的点击率、完播率等关键指标
    - 为广告创意制作提供数据支持的最佳实践

    ### 参数:
    - first_industry_id: 行业ID，如游戏行业：25000000000
    - period_type: 时间类型，\"week\"=周数据，\"month\"=月数据
    - order_field: 排序字段，\"ctr\"=点击率，\"play_over_rate\"=播放完成率
    - order_type: 排序方式，desc（降序）或asc（升序）
    - week: 查看特定周的数据，格式：YYYY-MM-DD（可选）

    ### 返回内容说明:
    - `list`: 创意模式列表
      - `label_info`: 模式标签信息
        - `value`: 模式名称
        - `description`: 模式描述
      - `ctr`: 点击率（百分比）
      - `play_over_rate`: 播放完成率（百分比）
      - `avg_watch_time`: 平均观看时长
      - `example_count`: 示例数量

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_creative_patterns\",
      \"params\": {
        \"first_industry_id\": \"25000000000\",
        \"period_type\": \"week\",
        \"order_field\": \"ctr\"
      },
      \"data\": {
        \"list\": [
          {
            \"label_info\": {
              \"value\": \"Problem-Solution\",
              \"description\": \"Present a problem and show the solution\"
            },
            \"ctr\": 4.5,
            \"play_over_rate\": 68.2,
            \"avg_watch_time\": 12.3,
            \"example_count\": 234
          }
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get creative pattern rankings for specific industries to understand which patterns perform best
    - Analyze key metrics like CTR and completion rate for different creative patterns
    - Provide data-driven best practices for ad creative production

    ### Parameters:
    - first_industry_id: Industry ID, e.g., Games: 25000000000
    - period_type: Period type, \"week\"=Weekly data, \"month\"=Monthly data
    - order_field: Sort field, \"ctr\"=Click-through rate, \"play_over_rate\"=Completion rate
    - order_type: Sort order, desc (descending) or asc (ascending)
    - week: View data for specific week, format: YYYY-MM-DD (optional)

    ### Return Description:
    - `list`: Creative pattern list
      - `label_info`: Pattern label information
        - `value`: Pattern name
        - `description`: Pattern description
      - `ctr`: Click-through rate (percentage)
      - `play_over_rate`: Play completion rate (percentage)
      - `avg_watch_time`: Average watch time
      - `example_count`: Number of examples

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_creative_patterns\",
      \"params\": {
        \"first_industry_id\": \"25000000000\",
        \"period_type\": \"week\",
        \"order_field\": \"ctr\"
      },
      \"data\": {
        \"list\": [
          {
            \"label_info\": {
              \"value\": \"Problem-Solution\",
              \"description\": \"Present a problem and show the solution\"
            },
            \"ctr\": 4.5,
            \"play_over_rate\": 68.2,
            \"avg_watch_time\": 12.3,
            \"example_count\": 234
          }
        ]
      }
    }
    ```

    Args:
        first_industry_id (Union[Unset, str]): 一级行业ID/First industry ID Default: '25000000000'.
        period_type (Union[Unset, str]): 时间周期类型/Period type (week, month) Default: 'week'.
        order_field (Union[Unset, str]): 排序字段/Order field (ctr, play_over_rate) Default: 'ctr'.
        order_type (Union[Unset, str]): 排序方式/Sort order (desc, asc) Default: 'desc'.
        week (Union[Unset, str]): 特定周（可选）/Specific week (optional)
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        first_industry_id=first_industry_id,
        period_type=period_type,
        order_field=order_field,
        order_type=order_type,
        week=week,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    first_industry_id: Union[Unset, str] = "25000000000",
    period_type: Union[Unset, str] = "week",
    order_field: Union[Unset, str] = "ctr",
    order_type: Union[Unset, str] = "desc",
    week: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创意模式排行榜/Get creative pattern rankings

     # [中文]
    ### 用途:
    - 获取特定行业的创意模式排行榜，了解哪些创意模式效果最好
    - 分析不同创意模式的点击率、完播率等关键指标
    - 为广告创意制作提供数据支持的最佳实践

    ### 参数:
    - first_industry_id: 行业ID，如游戏行业：25000000000
    - period_type: 时间类型，\"week\"=周数据，\"month\"=月数据
    - order_field: 排序字段，\"ctr\"=点击率，\"play_over_rate\"=播放完成率
    - order_type: 排序方式，desc（降序）或asc（升序）
    - week: 查看特定周的数据，格式：YYYY-MM-DD（可选）

    ### 返回内容说明:
    - `list`: 创意模式列表
      - `label_info`: 模式标签信息
        - `value`: 模式名称
        - `description`: 模式描述
      - `ctr`: 点击率（百分比）
      - `play_over_rate`: 播放完成率（百分比）
      - `avg_watch_time`: 平均观看时长
      - `example_count`: 示例数量

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_creative_patterns\",
      \"params\": {
        \"first_industry_id\": \"25000000000\",
        \"period_type\": \"week\",
        \"order_field\": \"ctr\"
      },
      \"data\": {
        \"list\": [
          {
            \"label_info\": {
              \"value\": \"Problem-Solution\",
              \"description\": \"Present a problem and show the solution\"
            },
            \"ctr\": 4.5,
            \"play_over_rate\": 68.2,
            \"avg_watch_time\": 12.3,
            \"example_count\": 234
          }
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get creative pattern rankings for specific industries to understand which patterns perform best
    - Analyze key metrics like CTR and completion rate for different creative patterns
    - Provide data-driven best practices for ad creative production

    ### Parameters:
    - first_industry_id: Industry ID, e.g., Games: 25000000000
    - period_type: Period type, \"week\"=Weekly data, \"month\"=Monthly data
    - order_field: Sort field, \"ctr\"=Click-through rate, \"play_over_rate\"=Completion rate
    - order_type: Sort order, desc (descending) or asc (ascending)
    - week: View data for specific week, format: YYYY-MM-DD (optional)

    ### Return Description:
    - `list`: Creative pattern list
      - `label_info`: Pattern label information
        - `value`: Pattern name
        - `description`: Pattern description
      - `ctr`: Click-through rate (percentage)
      - `play_over_rate`: Play completion rate (percentage)
      - `avg_watch_time`: Average watch time
      - `example_count`: Number of examples

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_creative_patterns\",
      \"params\": {
        \"first_industry_id\": \"25000000000\",
        \"period_type\": \"week\",
        \"order_field\": \"ctr\"
      },
      \"data\": {
        \"list\": [
          {
            \"label_info\": {
              \"value\": \"Problem-Solution\",
              \"description\": \"Present a problem and show the solution\"
            },
            \"ctr\": 4.5,
            \"play_over_rate\": 68.2,
            \"avg_watch_time\": 12.3,
            \"example_count\": 234
          }
        ]
      }
    }
    ```

    Args:
        first_industry_id (Union[Unset, str]): 一级行业ID/First industry ID Default: '25000000000'.
        period_type (Union[Unset, str]): 时间周期类型/Period type (week, month) Default: 'week'.
        order_field (Union[Unset, str]): 排序字段/Order field (ctr, play_over_rate) Default: 'ctr'.
        order_type (Union[Unset, str]): 排序方式/Sort order (desc, asc) Default: 'desc'.
        week (Union[Unset, str]): 特定周（可选）/Specific week (optional)
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        first_industry_id=first_industry_id,
        period_type=period_type,
        order_field=order_field,
        order_type=order_type,
        week=week,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    first_industry_id: Union[Unset, str] = "25000000000",
    period_type: Union[Unset, str] = "week",
    order_field: Union[Unset, str] = "ctr",
    order_type: Union[Unset, str] = "desc",
    week: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创意模式排行榜/Get creative pattern rankings

     # [中文]
    ### 用途:
    - 获取特定行业的创意模式排行榜，了解哪些创意模式效果最好
    - 分析不同创意模式的点击率、完播率等关键指标
    - 为广告创意制作提供数据支持的最佳实践

    ### 参数:
    - first_industry_id: 行业ID，如游戏行业：25000000000
    - period_type: 时间类型，\"week\"=周数据，\"month\"=月数据
    - order_field: 排序字段，\"ctr\"=点击率，\"play_over_rate\"=播放完成率
    - order_type: 排序方式，desc（降序）或asc（升序）
    - week: 查看特定周的数据，格式：YYYY-MM-DD（可选）

    ### 返回内容说明:
    - `list`: 创意模式列表
      - `label_info`: 模式标签信息
        - `value`: 模式名称
        - `description`: 模式描述
      - `ctr`: 点击率（百分比）
      - `play_over_rate`: 播放完成率（百分比）
      - `avg_watch_time`: 平均观看时长
      - `example_count`: 示例数量

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_creative_patterns\",
      \"params\": {
        \"first_industry_id\": \"25000000000\",
        \"period_type\": \"week\",
        \"order_field\": \"ctr\"
      },
      \"data\": {
        \"list\": [
          {
            \"label_info\": {
              \"value\": \"Problem-Solution\",
              \"description\": \"Present a problem and show the solution\"
            },
            \"ctr\": 4.5,
            \"play_over_rate\": 68.2,
            \"avg_watch_time\": 12.3,
            \"example_count\": 234
          }
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get creative pattern rankings for specific industries to understand which patterns perform best
    - Analyze key metrics like CTR and completion rate for different creative patterns
    - Provide data-driven best practices for ad creative production

    ### Parameters:
    - first_industry_id: Industry ID, e.g., Games: 25000000000
    - period_type: Period type, \"week\"=Weekly data, \"month\"=Monthly data
    - order_field: Sort field, \"ctr\"=Click-through rate, \"play_over_rate\"=Completion rate
    - order_type: Sort order, desc (descending) or asc (ascending)
    - week: View data for specific week, format: YYYY-MM-DD (optional)

    ### Return Description:
    - `list`: Creative pattern list
      - `label_info`: Pattern label information
        - `value`: Pattern name
        - `description`: Pattern description
      - `ctr`: Click-through rate (percentage)
      - `play_over_rate`: Play completion rate (percentage)
      - `avg_watch_time`: Average watch time
      - `example_count`: Number of examples

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_creative_patterns\",
      \"params\": {
        \"first_industry_id\": \"25000000000\",
        \"period_type\": \"week\",
        \"order_field\": \"ctr\"
      },
      \"data\": {
        \"list\": [
          {
            \"label_info\": {
              \"value\": \"Problem-Solution\",
              \"description\": \"Present a problem and show the solution\"
            },
            \"ctr\": 4.5,
            \"play_over_rate\": 68.2,
            \"avg_watch_time\": 12.3,
            \"example_count\": 234
          }
        ]
      }
    }
    ```

    Args:
        first_industry_id (Union[Unset, str]): 一级行业ID/First industry ID Default: '25000000000'.
        period_type (Union[Unset, str]): 时间周期类型/Period type (week, month) Default: 'week'.
        order_field (Union[Unset, str]): 排序字段/Order field (ctr, play_over_rate) Default: 'ctr'.
        order_type (Union[Unset, str]): 排序方式/Sort order (desc, asc) Default: 'desc'.
        week (Union[Unset, str]): 特定周（可选）/Specific week (optional)
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            first_industry_id=first_industry_id,
            period_type=period_type,
            order_field=order_field,
            order_type=order_type,
            week=week,
            page=page,
            limit=limit,
        )
    ).parsed
