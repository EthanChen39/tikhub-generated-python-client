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
    metric: Union[Unset, str] = "retain_ctr",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["material_id"] = material_id

    params["metric"] = metric

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/get_ad_keyframe_analysis",
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
    metric: Union[Unset, str] = "retain_ctr",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取广告关键帧分析/Get ad keyframe analysis

     # [中文]
    ### 用途:
    - 获取广告视频的关键帧分析，了解视频在不同时间点的观众留存情况
    - 分析哪些时间点最吸引观众，哪些时间点观众流失最多
    - 帮助优化广告视频结构，提高观看完成率

    ### 参数:
    - material_id: 广告素材ID，必填参数
    - metric: 分析指标，可选值：
      - retain_ctr: 留存点击率（默认）
      - retain_cvr: 留存转化率
      - click_cnt: 点击次数
      - convert_cnt: 转化次数
      - play_retain_cnt: 播放留存量

    ### 返回内容说明:
    - `keyframe_data`: 关键帧数据
      - `time_points`: 时间点列表（秒）
      - `retention_rates`: 对应时间点的留存率（百分比）
      - `drop_points`: 流失率较高的时间点
      - `highlight_points`: 观众兴趣较高的时间点

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ad_keyframe_analysis\",
      \"params\": {
        \"material_id\": \"7213258221116751874\"
      },
      \"data\": {
        \"keyframe_data\": {
          \"time_points\": [0, 1, 2, 3, 4, 5],
          \"retention_rates\": [100, 95, 88, 82, 78, 75],
          \"drop_points\": [2, 4],
          \"highlight_points\": [1, 5]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get keyframe analysis of ad videos to understand audience retention at different time points
    - Analyze which time points attract viewers most and where viewers drop off
    - Help optimize ad video structure to improve completion rates

    ### Parameters:
    - material_id: Ad material ID, required parameter
    - metric: Analysis metric, options:
      - retain_ctr: Retention CTR (default)
      - retain_cvr: Retention CVR
      - click_cnt: Click count
      - convert_cnt: Conversion count
      - play_retain_cnt: Play retention count

    ### Return Description:
    - `keyframe_data`: Keyframe data
      - `time_points`: List of time points (seconds)
      - `retention_rates`: Retention rates at corresponding time points (percentage)
      - `drop_points`: Time points with high drop-off rates
      - `highlight_points`: Time points with high viewer interest

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ad_keyframe_analysis\",
      \"params\": {
        \"material_id\": \"7213258221116751874\"
      },
      \"data\": {
        \"keyframe_data\": {
          \"time_points\": [0, 1, 2, 3, 4, 5],
          \"retention_rates\": [100, 95, 88, 82, 78, 75],
          \"drop_points\": [2, 4],
          \"highlight_points\": [1, 5]
        }
      }
    }
    ```

    Args:
        material_id (str): 广告素材ID/Ad material ID
        metric (Union[Unset, str]): 分析指标/Analysis metric (retain_ctr, retain_cvr, click_cnt,
            convert_cnt, play_retain_cnt) Default: 'retain_ctr'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        material_id=material_id,
        metric=metric,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    material_id: str,
    metric: Union[Unset, str] = "retain_ctr",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取广告关键帧分析/Get ad keyframe analysis

     # [中文]
    ### 用途:
    - 获取广告视频的关键帧分析，了解视频在不同时间点的观众留存情况
    - 分析哪些时间点最吸引观众，哪些时间点观众流失最多
    - 帮助优化广告视频结构，提高观看完成率

    ### 参数:
    - material_id: 广告素材ID，必填参数
    - metric: 分析指标，可选值：
      - retain_ctr: 留存点击率（默认）
      - retain_cvr: 留存转化率
      - click_cnt: 点击次数
      - convert_cnt: 转化次数
      - play_retain_cnt: 播放留存量

    ### 返回内容说明:
    - `keyframe_data`: 关键帧数据
      - `time_points`: 时间点列表（秒）
      - `retention_rates`: 对应时间点的留存率（百分比）
      - `drop_points`: 流失率较高的时间点
      - `highlight_points`: 观众兴趣较高的时间点

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ad_keyframe_analysis\",
      \"params\": {
        \"material_id\": \"7213258221116751874\"
      },
      \"data\": {
        \"keyframe_data\": {
          \"time_points\": [0, 1, 2, 3, 4, 5],
          \"retention_rates\": [100, 95, 88, 82, 78, 75],
          \"drop_points\": [2, 4],
          \"highlight_points\": [1, 5]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get keyframe analysis of ad videos to understand audience retention at different time points
    - Analyze which time points attract viewers most and where viewers drop off
    - Help optimize ad video structure to improve completion rates

    ### Parameters:
    - material_id: Ad material ID, required parameter
    - metric: Analysis metric, options:
      - retain_ctr: Retention CTR (default)
      - retain_cvr: Retention CVR
      - click_cnt: Click count
      - convert_cnt: Conversion count
      - play_retain_cnt: Play retention count

    ### Return Description:
    - `keyframe_data`: Keyframe data
      - `time_points`: List of time points (seconds)
      - `retention_rates`: Retention rates at corresponding time points (percentage)
      - `drop_points`: Time points with high drop-off rates
      - `highlight_points`: Time points with high viewer interest

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ad_keyframe_analysis\",
      \"params\": {
        \"material_id\": \"7213258221116751874\"
      },
      \"data\": {
        \"keyframe_data\": {
          \"time_points\": [0, 1, 2, 3, 4, 5],
          \"retention_rates\": [100, 95, 88, 82, 78, 75],
          \"drop_points\": [2, 4],
          \"highlight_points\": [1, 5]
        }
      }
    }
    ```

    Args:
        material_id (str): 广告素材ID/Ad material ID
        metric (Union[Unset, str]): 分析指标/Analysis metric (retain_ctr, retain_cvr, click_cnt,
            convert_cnt, play_retain_cnt) Default: 'retain_ctr'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        material_id=material_id,
        metric=metric,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    material_id: str,
    metric: Union[Unset, str] = "retain_ctr",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取广告关键帧分析/Get ad keyframe analysis

     # [中文]
    ### 用途:
    - 获取广告视频的关键帧分析，了解视频在不同时间点的观众留存情况
    - 分析哪些时间点最吸引观众，哪些时间点观众流失最多
    - 帮助优化广告视频结构，提高观看完成率

    ### 参数:
    - material_id: 广告素材ID，必填参数
    - metric: 分析指标，可选值：
      - retain_ctr: 留存点击率（默认）
      - retain_cvr: 留存转化率
      - click_cnt: 点击次数
      - convert_cnt: 转化次数
      - play_retain_cnt: 播放留存量

    ### 返回内容说明:
    - `keyframe_data`: 关键帧数据
      - `time_points`: 时间点列表（秒）
      - `retention_rates`: 对应时间点的留存率（百分比）
      - `drop_points`: 流失率较高的时间点
      - `highlight_points`: 观众兴趣较高的时间点

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ad_keyframe_analysis\",
      \"params\": {
        \"material_id\": \"7213258221116751874\"
      },
      \"data\": {
        \"keyframe_data\": {
          \"time_points\": [0, 1, 2, 3, 4, 5],
          \"retention_rates\": [100, 95, 88, 82, 78, 75],
          \"drop_points\": [2, 4],
          \"highlight_points\": [1, 5]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get keyframe analysis of ad videos to understand audience retention at different time points
    - Analyze which time points attract viewers most and where viewers drop off
    - Help optimize ad video structure to improve completion rates

    ### Parameters:
    - material_id: Ad material ID, required parameter
    - metric: Analysis metric, options:
      - retain_ctr: Retention CTR (default)
      - retain_cvr: Retention CVR
      - click_cnt: Click count
      - convert_cnt: Conversion count
      - play_retain_cnt: Play retention count

    ### Return Description:
    - `keyframe_data`: Keyframe data
      - `time_points`: List of time points (seconds)
      - `retention_rates`: Retention rates at corresponding time points (percentage)
      - `drop_points`: Time points with high drop-off rates
      - `highlight_points`: Time points with high viewer interest

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ad_keyframe_analysis\",
      \"params\": {
        \"material_id\": \"7213258221116751874\"
      },
      \"data\": {
        \"keyframe_data\": {
          \"time_points\": [0, 1, 2, 3, 4, 5],
          \"retention_rates\": [100, 95, 88, 82, 78, 75],
          \"drop_points\": [2, 4],
          \"highlight_points\": [1, 5]
        }
      }
    }
    ```

    Args:
        material_id (str): 广告素材ID/Ad material ID
        metric (Union[Unset, str]): 分析指标/Analysis metric (retain_ctr, retain_cvr, click_cnt,
            convert_cnt, play_retain_cnt) Default: 'retain_ctr'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        material_id=material_id,
        metric=metric,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    material_id: str,
    metric: Union[Unset, str] = "retain_ctr",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取广告关键帧分析/Get ad keyframe analysis

     # [中文]
    ### 用途:
    - 获取广告视频的关键帧分析，了解视频在不同时间点的观众留存情况
    - 分析哪些时间点最吸引观众，哪些时间点观众流失最多
    - 帮助优化广告视频结构，提高观看完成率

    ### 参数:
    - material_id: 广告素材ID，必填参数
    - metric: 分析指标，可选值：
      - retain_ctr: 留存点击率（默认）
      - retain_cvr: 留存转化率
      - click_cnt: 点击次数
      - convert_cnt: 转化次数
      - play_retain_cnt: 播放留存量

    ### 返回内容说明:
    - `keyframe_data`: 关键帧数据
      - `time_points`: 时间点列表（秒）
      - `retention_rates`: 对应时间点的留存率（百分比）
      - `drop_points`: 流失率较高的时间点
      - `highlight_points`: 观众兴趣较高的时间点

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ad_keyframe_analysis\",
      \"params\": {
        \"material_id\": \"7213258221116751874\"
      },
      \"data\": {
        \"keyframe_data\": {
          \"time_points\": [0, 1, 2, 3, 4, 5],
          \"retention_rates\": [100, 95, 88, 82, 78, 75],
          \"drop_points\": [2, 4],
          \"highlight_points\": [1, 5]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get keyframe analysis of ad videos to understand audience retention at different time points
    - Analyze which time points attract viewers most and where viewers drop off
    - Help optimize ad video structure to improve completion rates

    ### Parameters:
    - material_id: Ad material ID, required parameter
    - metric: Analysis metric, options:
      - retain_ctr: Retention CTR (default)
      - retain_cvr: Retention CVR
      - click_cnt: Click count
      - convert_cnt: Conversion count
      - play_retain_cnt: Play retention count

    ### Return Description:
    - `keyframe_data`: Keyframe data
      - `time_points`: List of time points (seconds)
      - `retention_rates`: Retention rates at corresponding time points (percentage)
      - `drop_points`: Time points with high drop-off rates
      - `highlight_points`: Time points with high viewer interest

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ad_keyframe_analysis\",
      \"params\": {
        \"material_id\": \"7213258221116751874\"
      },
      \"data\": {
        \"keyframe_data\": {
          \"time_points\": [0, 1, 2, 3, 4, 5],
          \"retention_rates\": [100, 95, 88, 82, 78, 75],
          \"drop_points\": [2, 4],
          \"highlight_points\": [1, 5]
        }
      }
    }
    ```

    Args:
        material_id (str): 广告素材ID/Ad material ID
        metric (Union[Unset, str]): 分析指标/Analysis metric (retain_ctr, retain_cvr, click_cnt,
            convert_cnt, play_retain_cnt) Default: 'retain_ctr'.

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
            metric=metric,
        )
    ).parsed
