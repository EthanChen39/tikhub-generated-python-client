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
    material_id: str,
    metric_type: Union[Unset, str] = "remain",
    period_type: Union[Unset, int] = 180,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["material_id"] = material_id

    params["metric_type"] = metric_type

    params["period_type"] = period_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/get_ad_interactive_analysis",
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
    material_id: str,
    metric_type: Union[Unset, str] = "remain",
    period_type: Union[Unset, int] = 180,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取广告互动分析/Get ad interactive analysis

     # [中文]
    ### 用途:
    - 获取广告的互动时间分析，了解观众在视频不同时间点的留存和互动情况
    - 分析广告视频的吸引力曲线，找出最佳时长和关键互动点
    - 优化广告内容结构，提高整体效果

    ### 参数:
    - material_id: 广告素材ID，必填参数
    - metric_type: 指标类型，默认\"remain\"（留存率）
    - period_type: 时间范围，默认180天

    ### 返回内容说明:
    - `interactive_data`: 互动分析数据
      - `time_series`: 时间序列数据
        - `time`: 视频播放时间点（秒）
        - `value`: 对应的指标值（如留存率）
      - `average_watch_time`: 平均观看时长
      - `completion_rate`: 完播率
      - `peak_interaction_time`: 互动高峰时间点

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ad_interactive_analysis\",
      \"params\": {
        \"material_id\": \"7213258221116751874\",
        \"metric_type\": \"remain\",
        \"period_type\": 180
      },
      \"data\": {
        \"interactive_data\": {
          \"time_series\": [
            {\"time\": 0, \"value\": 100},
            {\"time\": 1, \"value\": 95},
            {\"time\": 2, \"value\": 88}
          ],
          \"average_watch_time\": 8.5,
          \"completion_rate\": 65.2,
          \"peak_interaction_time\": 3
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get ad interactive time analysis to understand audience retention and engagement at different
    video time points
    - Analyze ad video attractiveness curve to find optimal duration and key interaction points
    - Optimize ad content structure to improve overall effectiveness

    ### Parameters:
    - material_id: Ad material ID, required parameter
    - metric_type: Metric type, default \"remain\" (retention rate)
    - period_type: Time range, default 180 days

    ### Return Description:
    - `interactive_data`: Interactive analysis data
      - `time_series`: Time series data
        - `time`: Video playback time point (seconds)
        - `value`: Corresponding metric value (e.g., retention rate)
      - `average_watch_time`: Average watch time
      - `completion_rate`: Completion rate
      - `peak_interaction_time`: Peak interaction time point

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ad_interactive_analysis\",
      \"params\": {
        \"material_id\": \"7213258221116751874\",
        \"metric_type\": \"remain\",
        \"period_type\": 180
      },
      \"data\": {
        \"interactive_data\": {
          \"time_series\": [
            {\"time\": 0, \"value\": 100},
            {\"time\": 1, \"value\": 95},
            {\"time\": 2, \"value\": 88}
          ],
          \"average_watch_time\": 8.5,
          \"completion_rate\": 65.2,
          \"peak_interaction_time\": 3
        }
      }
    }
    ```

    Args:
        material_id (str): 广告素材ID/Ad material ID
        metric_type (Union[Unset, str]): 分析类型/Analysis type (ctr, cvr, clicks, conversion, remain)
            Default: 'remain'.
        period_type (Union[Unset, int]): 时间范围(天)/Period type (days) Default: 180.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        material_id=material_id,
        metric_type=metric_type,
        period_type=period_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    material_id: str,
    metric_type: Union[Unset, str] = "remain",
    period_type: Union[Unset, int] = 180,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取广告互动分析/Get ad interactive analysis

     # [中文]
    ### 用途:
    - 获取广告的互动时间分析，了解观众在视频不同时间点的留存和互动情况
    - 分析广告视频的吸引力曲线，找出最佳时长和关键互动点
    - 优化广告内容结构，提高整体效果

    ### 参数:
    - material_id: 广告素材ID，必填参数
    - metric_type: 指标类型，默认\"remain\"（留存率）
    - period_type: 时间范围，默认180天

    ### 返回内容说明:
    - `interactive_data`: 互动分析数据
      - `time_series`: 时间序列数据
        - `time`: 视频播放时间点（秒）
        - `value`: 对应的指标值（如留存率）
      - `average_watch_time`: 平均观看时长
      - `completion_rate`: 完播率
      - `peak_interaction_time`: 互动高峰时间点

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ad_interactive_analysis\",
      \"params\": {
        \"material_id\": \"7213258221116751874\",
        \"metric_type\": \"remain\",
        \"period_type\": 180
      },
      \"data\": {
        \"interactive_data\": {
          \"time_series\": [
            {\"time\": 0, \"value\": 100},
            {\"time\": 1, \"value\": 95},
            {\"time\": 2, \"value\": 88}
          ],
          \"average_watch_time\": 8.5,
          \"completion_rate\": 65.2,
          \"peak_interaction_time\": 3
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get ad interactive time analysis to understand audience retention and engagement at different
    video time points
    - Analyze ad video attractiveness curve to find optimal duration and key interaction points
    - Optimize ad content structure to improve overall effectiveness

    ### Parameters:
    - material_id: Ad material ID, required parameter
    - metric_type: Metric type, default \"remain\" (retention rate)
    - period_type: Time range, default 180 days

    ### Return Description:
    - `interactive_data`: Interactive analysis data
      - `time_series`: Time series data
        - `time`: Video playback time point (seconds)
        - `value`: Corresponding metric value (e.g., retention rate)
      - `average_watch_time`: Average watch time
      - `completion_rate`: Completion rate
      - `peak_interaction_time`: Peak interaction time point

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ad_interactive_analysis\",
      \"params\": {
        \"material_id\": \"7213258221116751874\",
        \"metric_type\": \"remain\",
        \"period_type\": 180
      },
      \"data\": {
        \"interactive_data\": {
          \"time_series\": [
            {\"time\": 0, \"value\": 100},
            {\"time\": 1, \"value\": 95},
            {\"time\": 2, \"value\": 88}
          ],
          \"average_watch_time\": 8.5,
          \"completion_rate\": 65.2,
          \"peak_interaction_time\": 3
        }
      }
    }
    ```

    Args:
        material_id (str): 广告素材ID/Ad material ID
        metric_type (Union[Unset, str]): 分析类型/Analysis type (ctr, cvr, clicks, conversion, remain)
            Default: 'remain'.
        period_type (Union[Unset, int]): 时间范围(天)/Period type (days) Default: 180.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        material_id=material_id,
        metric_type=metric_type,
        period_type=period_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    material_id: str,
    metric_type: Union[Unset, str] = "remain",
    period_type: Union[Unset, int] = 180,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取广告互动分析/Get ad interactive analysis

     # [中文]
    ### 用途:
    - 获取广告的互动时间分析，了解观众在视频不同时间点的留存和互动情况
    - 分析广告视频的吸引力曲线，找出最佳时长和关键互动点
    - 优化广告内容结构，提高整体效果

    ### 参数:
    - material_id: 广告素材ID，必填参数
    - metric_type: 指标类型，默认\"remain\"（留存率）
    - period_type: 时间范围，默认180天

    ### 返回内容说明:
    - `interactive_data`: 互动分析数据
      - `time_series`: 时间序列数据
        - `time`: 视频播放时间点（秒）
        - `value`: 对应的指标值（如留存率）
      - `average_watch_time`: 平均观看时长
      - `completion_rate`: 完播率
      - `peak_interaction_time`: 互动高峰时间点

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ad_interactive_analysis\",
      \"params\": {
        \"material_id\": \"7213258221116751874\",
        \"metric_type\": \"remain\",
        \"period_type\": 180
      },
      \"data\": {
        \"interactive_data\": {
          \"time_series\": [
            {\"time\": 0, \"value\": 100},
            {\"time\": 1, \"value\": 95},
            {\"time\": 2, \"value\": 88}
          ],
          \"average_watch_time\": 8.5,
          \"completion_rate\": 65.2,
          \"peak_interaction_time\": 3
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get ad interactive time analysis to understand audience retention and engagement at different
    video time points
    - Analyze ad video attractiveness curve to find optimal duration and key interaction points
    - Optimize ad content structure to improve overall effectiveness

    ### Parameters:
    - material_id: Ad material ID, required parameter
    - metric_type: Metric type, default \"remain\" (retention rate)
    - period_type: Time range, default 180 days

    ### Return Description:
    - `interactive_data`: Interactive analysis data
      - `time_series`: Time series data
        - `time`: Video playback time point (seconds)
        - `value`: Corresponding metric value (e.g., retention rate)
      - `average_watch_time`: Average watch time
      - `completion_rate`: Completion rate
      - `peak_interaction_time`: Peak interaction time point

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ad_interactive_analysis\",
      \"params\": {
        \"material_id\": \"7213258221116751874\",
        \"metric_type\": \"remain\",
        \"period_type\": 180
      },
      \"data\": {
        \"interactive_data\": {
          \"time_series\": [
            {\"time\": 0, \"value\": 100},
            {\"time\": 1, \"value\": 95},
            {\"time\": 2, \"value\": 88}
          ],
          \"average_watch_time\": 8.5,
          \"completion_rate\": 65.2,
          \"peak_interaction_time\": 3
        }
      }
    }
    ```

    Args:
        material_id (str): 广告素材ID/Ad material ID
        metric_type (Union[Unset, str]): 分析类型/Analysis type (ctr, cvr, clicks, conversion, remain)
            Default: 'remain'.
        period_type (Union[Unset, int]): 时间范围(天)/Period type (days) Default: 180.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        material_id=material_id,
        metric_type=metric_type,
        period_type=period_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    material_id: str,
    metric_type: Union[Unset, str] = "remain",
    period_type: Union[Unset, int] = 180,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取广告互动分析/Get ad interactive analysis

     # [中文]
    ### 用途:
    - 获取广告的互动时间分析，了解观众在视频不同时间点的留存和互动情况
    - 分析广告视频的吸引力曲线，找出最佳时长和关键互动点
    - 优化广告内容结构，提高整体效果

    ### 参数:
    - material_id: 广告素材ID，必填参数
    - metric_type: 指标类型，默认\"remain\"（留存率）
    - period_type: 时间范围，默认180天

    ### 返回内容说明:
    - `interactive_data`: 互动分析数据
      - `time_series`: 时间序列数据
        - `time`: 视频播放时间点（秒）
        - `value`: 对应的指标值（如留存率）
      - `average_watch_time`: 平均观看时长
      - `completion_rate`: 完播率
      - `peak_interaction_time`: 互动高峰时间点

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ad_interactive_analysis\",
      \"params\": {
        \"material_id\": \"7213258221116751874\",
        \"metric_type\": \"remain\",
        \"period_type\": 180
      },
      \"data\": {
        \"interactive_data\": {
          \"time_series\": [
            {\"time\": 0, \"value\": 100},
            {\"time\": 1, \"value\": 95},
            {\"time\": 2, \"value\": 88}
          ],
          \"average_watch_time\": 8.5,
          \"completion_rate\": 65.2,
          \"peak_interaction_time\": 3
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get ad interactive time analysis to understand audience retention and engagement at different
    video time points
    - Analyze ad video attractiveness curve to find optimal duration and key interaction points
    - Optimize ad content structure to improve overall effectiveness

    ### Parameters:
    - material_id: Ad material ID, required parameter
    - metric_type: Metric type, default \"remain\" (retention rate)
    - period_type: Time range, default 180 days

    ### Return Description:
    - `interactive_data`: Interactive analysis data
      - `time_series`: Time series data
        - `time`: Video playback time point (seconds)
        - `value`: Corresponding metric value (e.g., retention rate)
      - `average_watch_time`: Average watch time
      - `completion_rate`: Completion rate
      - `peak_interaction_time`: Peak interaction time point

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ad_interactive_analysis\",
      \"params\": {
        \"material_id\": \"7213258221116751874\",
        \"metric_type\": \"remain\",
        \"period_type\": 180
      },
      \"data\": {
        \"interactive_data\": {
          \"time_series\": [
            {\"time\": 0, \"value\": 100},
            {\"time\": 1, \"value\": 95},
            {\"time\": 2, \"value\": 88}
          ],
          \"average_watch_time\": 8.5,
          \"completion_rate\": 65.2,
          \"peak_interaction_time\": 3
        }
      }
    }
    ```

    Args:
        material_id (str): 广告素材ID/Ad material ID
        metric_type (Union[Unset, str]): 分析类型/Analysis type (ctr, cvr, clicks, conversion, remain)
            Default: 'remain'.
        period_type (Union[Unset, int]): 时间范围(天)/Period type (days) Default: 180.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            material_id=material_id,
            metric_type=metric_type,
            period_type=period_type,
        )
    ).parsed
