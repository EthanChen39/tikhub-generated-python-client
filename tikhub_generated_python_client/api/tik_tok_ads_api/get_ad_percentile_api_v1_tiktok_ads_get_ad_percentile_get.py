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
    metric: Union[Unset, str] = "ctr_percentile",
    period_type: Union[Unset, int] = 180,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["material_id"] = material_id

    params["metric"] = metric

    params["period_type"] = period_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/get_ad_percentile",
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
    metric: Union[Unset, str] = "ctr_percentile",
    period_type: Union[Unset, int] = 180,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取广告百分位数据/Get ad percentile data

     # [中文]
    ### 用途:
    - 获取广告在同行业中的百分位排名数据
    - 了解广告在各项指标上相对于同行的表现水平
    - 帮助评估广告效果并制定优化策略

    ### 参数:
    - material_id: 广告素材ID，必填参数
    - metric: 分析指标，可选值：
      - ctr_percentile: 点击率百分位（默认）
      - time_attr_conversion_rate_percentile: 时间归因转化率百分位
      - click_cnt_percentile: 点击次数百分位
      - time_attr_convert_cnt_percentile: 时间归因转化次数百分位
      - show_cnt_percentile: 展示次数百分位
    - period_type: 时间范围(天)，默认180天

    ### 返回内容说明:
    - `percentile_data`: 百分位数据
      - `ctr_percentile`: 点击率百分位（0-100）
      - `cvr_percentile`: 转化率百分位
      - `engagement_percentile`: 互动率百分位
      - `view_percentile`: 观看量百分位
      - `industry_average`: 行业平均值对比

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ad_percentile\",
      \"params\": {
        \"material_id\": \"7213258221116751874\"
      },
      \"data\": {
        \"percentile_data\": {
          \"ctr_percentile\": 85,
          \"cvr_percentile\": 72,
          \"engagement_percentile\": 90,
          \"view_percentile\": 88,
          \"industry_average\": {
            \"ctr\": 2.5,
            \"cvr\": 1.2,
            \"engagement\": 5.8
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get ad percentile ranking data within the industry
    - Understand ad performance levels relative to peers across various metrics
    - Help evaluate ad effectiveness and develop optimization strategies

    ### Parameters:
    - material_id: Ad material ID, required parameter
    - metric: Analysis metric, options:
      - ctr_percentile: CTR percentile (default)
      - time_attr_conversion_rate_percentile: Time-attributed conversion rate percentile
      - click_cnt_percentile: Click count percentile
      - time_attr_convert_cnt_percentile: Time-attributed conversion count percentile
      - show_cnt_percentile: Impression count percentile
    - period_type: Time period in days, default 180

    ### Return Description:
    - `percentile_data`: Percentile data
      - `ctr_percentile`: Click-through rate percentile (0-100)
      - `cvr_percentile`: Conversion rate percentile
      - `engagement_percentile`: Engagement rate percentile
      - `view_percentile`: View count percentile
      - `industry_average`: Industry average comparison

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ad_percentile\",
      \"params\": {
        \"material_id\": \"7213258221116751874\"
      },
      \"data\": {
        \"percentile_data\": {
          \"ctr_percentile\": 85,
          \"cvr_percentile\": 72,
          \"engagement_percentile\": 90,
          \"view_percentile\": 88,
          \"industry_average\": {
            \"ctr\": 2.5,
            \"cvr\": 1.2,
            \"engagement\": 5.8
          }
        }
      }
    }
    ```

    Args:
        material_id (str): 广告素材ID/Ad material ID
        metric (Union[Unset, str]): 分析指标/Analysis metric (ctr_percentile,
            time_attr_conversion_rate_percentile, click_cnt_percentile,
            time_attr_convert_cnt_percentile, show_cnt_percentile) Default: 'ctr_percentile'.
        period_type (Union[Unset, int]): 时间范围(天)/Time period (days) Default: 180.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        material_id=material_id,
        metric=metric,
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
    metric: Union[Unset, str] = "ctr_percentile",
    period_type: Union[Unset, int] = 180,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取广告百分位数据/Get ad percentile data

     # [中文]
    ### 用途:
    - 获取广告在同行业中的百分位排名数据
    - 了解广告在各项指标上相对于同行的表现水平
    - 帮助评估广告效果并制定优化策略

    ### 参数:
    - material_id: 广告素材ID，必填参数
    - metric: 分析指标，可选值：
      - ctr_percentile: 点击率百分位（默认）
      - time_attr_conversion_rate_percentile: 时间归因转化率百分位
      - click_cnt_percentile: 点击次数百分位
      - time_attr_convert_cnt_percentile: 时间归因转化次数百分位
      - show_cnt_percentile: 展示次数百分位
    - period_type: 时间范围(天)，默认180天

    ### 返回内容说明:
    - `percentile_data`: 百分位数据
      - `ctr_percentile`: 点击率百分位（0-100）
      - `cvr_percentile`: 转化率百分位
      - `engagement_percentile`: 互动率百分位
      - `view_percentile`: 观看量百分位
      - `industry_average`: 行业平均值对比

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ad_percentile\",
      \"params\": {
        \"material_id\": \"7213258221116751874\"
      },
      \"data\": {
        \"percentile_data\": {
          \"ctr_percentile\": 85,
          \"cvr_percentile\": 72,
          \"engagement_percentile\": 90,
          \"view_percentile\": 88,
          \"industry_average\": {
            \"ctr\": 2.5,
            \"cvr\": 1.2,
            \"engagement\": 5.8
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get ad percentile ranking data within the industry
    - Understand ad performance levels relative to peers across various metrics
    - Help evaluate ad effectiveness and develop optimization strategies

    ### Parameters:
    - material_id: Ad material ID, required parameter
    - metric: Analysis metric, options:
      - ctr_percentile: CTR percentile (default)
      - time_attr_conversion_rate_percentile: Time-attributed conversion rate percentile
      - click_cnt_percentile: Click count percentile
      - time_attr_convert_cnt_percentile: Time-attributed conversion count percentile
      - show_cnt_percentile: Impression count percentile
    - period_type: Time period in days, default 180

    ### Return Description:
    - `percentile_data`: Percentile data
      - `ctr_percentile`: Click-through rate percentile (0-100)
      - `cvr_percentile`: Conversion rate percentile
      - `engagement_percentile`: Engagement rate percentile
      - `view_percentile`: View count percentile
      - `industry_average`: Industry average comparison

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ad_percentile\",
      \"params\": {
        \"material_id\": \"7213258221116751874\"
      },
      \"data\": {
        \"percentile_data\": {
          \"ctr_percentile\": 85,
          \"cvr_percentile\": 72,
          \"engagement_percentile\": 90,
          \"view_percentile\": 88,
          \"industry_average\": {
            \"ctr\": 2.5,
            \"cvr\": 1.2,
            \"engagement\": 5.8
          }
        }
      }
    }
    ```

    Args:
        material_id (str): 广告素材ID/Ad material ID
        metric (Union[Unset, str]): 分析指标/Analysis metric (ctr_percentile,
            time_attr_conversion_rate_percentile, click_cnt_percentile,
            time_attr_convert_cnt_percentile, show_cnt_percentile) Default: 'ctr_percentile'.
        period_type (Union[Unset, int]): 时间范围(天)/Time period (days) Default: 180.

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
        period_type=period_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    material_id: str,
    metric: Union[Unset, str] = "ctr_percentile",
    period_type: Union[Unset, int] = 180,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取广告百分位数据/Get ad percentile data

     # [中文]
    ### 用途:
    - 获取广告在同行业中的百分位排名数据
    - 了解广告在各项指标上相对于同行的表现水平
    - 帮助评估广告效果并制定优化策略

    ### 参数:
    - material_id: 广告素材ID，必填参数
    - metric: 分析指标，可选值：
      - ctr_percentile: 点击率百分位（默认）
      - time_attr_conversion_rate_percentile: 时间归因转化率百分位
      - click_cnt_percentile: 点击次数百分位
      - time_attr_convert_cnt_percentile: 时间归因转化次数百分位
      - show_cnt_percentile: 展示次数百分位
    - period_type: 时间范围(天)，默认180天

    ### 返回内容说明:
    - `percentile_data`: 百分位数据
      - `ctr_percentile`: 点击率百分位（0-100）
      - `cvr_percentile`: 转化率百分位
      - `engagement_percentile`: 互动率百分位
      - `view_percentile`: 观看量百分位
      - `industry_average`: 行业平均值对比

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ad_percentile\",
      \"params\": {
        \"material_id\": \"7213258221116751874\"
      },
      \"data\": {
        \"percentile_data\": {
          \"ctr_percentile\": 85,
          \"cvr_percentile\": 72,
          \"engagement_percentile\": 90,
          \"view_percentile\": 88,
          \"industry_average\": {
            \"ctr\": 2.5,
            \"cvr\": 1.2,
            \"engagement\": 5.8
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get ad percentile ranking data within the industry
    - Understand ad performance levels relative to peers across various metrics
    - Help evaluate ad effectiveness and develop optimization strategies

    ### Parameters:
    - material_id: Ad material ID, required parameter
    - metric: Analysis metric, options:
      - ctr_percentile: CTR percentile (default)
      - time_attr_conversion_rate_percentile: Time-attributed conversion rate percentile
      - click_cnt_percentile: Click count percentile
      - time_attr_convert_cnt_percentile: Time-attributed conversion count percentile
      - show_cnt_percentile: Impression count percentile
    - period_type: Time period in days, default 180

    ### Return Description:
    - `percentile_data`: Percentile data
      - `ctr_percentile`: Click-through rate percentile (0-100)
      - `cvr_percentile`: Conversion rate percentile
      - `engagement_percentile`: Engagement rate percentile
      - `view_percentile`: View count percentile
      - `industry_average`: Industry average comparison

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ad_percentile\",
      \"params\": {
        \"material_id\": \"7213258221116751874\"
      },
      \"data\": {
        \"percentile_data\": {
          \"ctr_percentile\": 85,
          \"cvr_percentile\": 72,
          \"engagement_percentile\": 90,
          \"view_percentile\": 88,
          \"industry_average\": {
            \"ctr\": 2.5,
            \"cvr\": 1.2,
            \"engagement\": 5.8
          }
        }
      }
    }
    ```

    Args:
        material_id (str): 广告素材ID/Ad material ID
        metric (Union[Unset, str]): 分析指标/Analysis metric (ctr_percentile,
            time_attr_conversion_rate_percentile, click_cnt_percentile,
            time_attr_convert_cnt_percentile, show_cnt_percentile) Default: 'ctr_percentile'.
        period_type (Union[Unset, int]): 时间范围(天)/Time period (days) Default: 180.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        material_id=material_id,
        metric=metric,
        period_type=period_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    material_id: str,
    metric: Union[Unset, str] = "ctr_percentile",
    period_type: Union[Unset, int] = 180,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取广告百分位数据/Get ad percentile data

     # [中文]
    ### 用途:
    - 获取广告在同行业中的百分位排名数据
    - 了解广告在各项指标上相对于同行的表现水平
    - 帮助评估广告效果并制定优化策略

    ### 参数:
    - material_id: 广告素材ID，必填参数
    - metric: 分析指标，可选值：
      - ctr_percentile: 点击率百分位（默认）
      - time_attr_conversion_rate_percentile: 时间归因转化率百分位
      - click_cnt_percentile: 点击次数百分位
      - time_attr_convert_cnt_percentile: 时间归因转化次数百分位
      - show_cnt_percentile: 展示次数百分位
    - period_type: 时间范围(天)，默认180天

    ### 返回内容说明:
    - `percentile_data`: 百分位数据
      - `ctr_percentile`: 点击率百分位（0-100）
      - `cvr_percentile`: 转化率百分位
      - `engagement_percentile`: 互动率百分位
      - `view_percentile`: 观看量百分位
      - `industry_average`: 行业平均值对比

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ad_percentile\",
      \"params\": {
        \"material_id\": \"7213258221116751874\"
      },
      \"data\": {
        \"percentile_data\": {
          \"ctr_percentile\": 85,
          \"cvr_percentile\": 72,
          \"engagement_percentile\": 90,
          \"view_percentile\": 88,
          \"industry_average\": {
            \"ctr\": 2.5,
            \"cvr\": 1.2,
            \"engagement\": 5.8
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get ad percentile ranking data within the industry
    - Understand ad performance levels relative to peers across various metrics
    - Help evaluate ad effectiveness and develop optimization strategies

    ### Parameters:
    - material_id: Ad material ID, required parameter
    - metric: Analysis metric, options:
      - ctr_percentile: CTR percentile (default)
      - time_attr_conversion_rate_percentile: Time-attributed conversion rate percentile
      - click_cnt_percentile: Click count percentile
      - time_attr_convert_cnt_percentile: Time-attributed conversion count percentile
      - show_cnt_percentile: Impression count percentile
    - period_type: Time period in days, default 180

    ### Return Description:
    - `percentile_data`: Percentile data
      - `ctr_percentile`: Click-through rate percentile (0-100)
      - `cvr_percentile`: Conversion rate percentile
      - `engagement_percentile`: Engagement rate percentile
      - `view_percentile`: View count percentile
      - `industry_average`: Industry average comparison

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_ad_percentile\",
      \"params\": {
        \"material_id\": \"7213258221116751874\"
      },
      \"data\": {
        \"percentile_data\": {
          \"ctr_percentile\": 85,
          \"cvr_percentile\": 72,
          \"engagement_percentile\": 90,
          \"view_percentile\": 88,
          \"industry_average\": {
            \"ctr\": 2.5,
            \"cvr\": 1.2,
            \"engagement\": 5.8
          }
        }
      }
    }
    ```

    Args:
        material_id (str): 广告素材ID/Ad material ID
        metric (Union[Unset, str]): 分析指标/Analysis metric (ctr_percentile,
            time_attr_conversion_rate_percentile, click_cnt_percentile,
            time_attr_convert_cnt_percentile, show_cnt_percentile) Default: 'ctr_percentile'.
        period_type (Union[Unset, int]): 时间范围(天)/Time period (days) Default: 180.

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
            period_type=period_type,
        )
    ).parsed
