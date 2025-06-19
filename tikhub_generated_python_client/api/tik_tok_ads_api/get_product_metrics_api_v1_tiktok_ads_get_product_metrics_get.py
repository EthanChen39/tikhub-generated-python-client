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
    id: str,
    last: Union[Unset, int] = 30,
    metrics: Union[Unset, str] = "post,ctr",
    ecom_type: Union[Unset, str] = "l3",
    period_type: Union[Unset, str] = "last",
    country_code: Union[Unset, str] = "US",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["id"] = id

    params["last"] = last

    params["metrics"] = metrics

    params["ecom_type"] = ecom_type

    params["period_type"] = period_type

    params["country_code"] = country_code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/get_product_metrics",
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
    id: str,
    last: Union[Unset, int] = 30,
    metrics: Union[Unset, str] = "post,ctr",
    ecom_type: Union[Unset, str] = "l3",
    period_type: Union[Unset, str] = "last",
    country_code: Union[Unset, str] = "US",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取产品指标数据/Get product metrics

     # [中文]
    ### 用途:
    - 获取特定产品类目的详细指标数据和时间趋势
    - 分析产品的发布量、点击率、转化率等核心指标变化
    - 帮助了解产品类目的市场表现和发展趋势

    ### 参数:
    - id: 产品类目ID，如香水：601583
    - last: 最近天数，如7、30天
    - metrics: 指标类型，多个用逗号分隔，如\"post,ctr,cvr\"
    - ecom_type: 电商类型，默认\"l3\"
    - period_type: 时间类型，默认\"last\"

    ### 返回内容说明:
    - `info`: 产品指标信息
      - `comment`: 评论数
      - `cost`: 花费金额
      - `cover_url`: 封面图URL（可能为null）
      - `cpa`: 每次转化成本
      - `ctr`: 点击率
      - `ctr_metrics`: 点击率时间序列数据
        - `time`: 时间戳
        - `value`: 对应时间的点击率
      - `cvr`: 转化率
      - `ecom_type`: 电商类型
      - `first_ecom_category`: 一级电商类目
      - `impression`: 展示量
      - `like`: 点赞数
      - `play_six_rate`: 6秒播放率
      - `post`: 发布量
      - `post_change`: 发布量变化率
      - `post_metrics`: 发布量时间序列数据
        - `time`: 时间戳
        - `value`: 对应时间的发布量
      - `second_ecom_category`: 二级电商类目
      - `share`: 分享数
      - `third_ecom_category`: 三级电商类目
      - `url_title`: URL标题

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_product_metrics\",
      \"params\": {
        \"id\": \"601583\",
        \"last\": \"30\",
        \"metrics\": \"post,ctr\",
        \"ecom_type\": \"l3\",
        \"period_type\": \"last\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"info\": {
            \"comment\": 13559,
            \"cost\": 2330000,
            \"cover_url\": null,
            \"cpa\": 12.4,
            \"ctr\": 1.04,
            \"ctr_metrics\": [
              {
                \"time\": 1747267200,
                \"value\": 0.88
              },
              {
                \"time\": 1747353600,
                \"value\": 0.99
              }
            ],
            \"cvr\": 15.2,
            \"ecom_type\": \"l3\",
            \"post\": 52300,
            \"post_change\": -8.12,
            \"post_metrics\": [
              {
                \"time\": 1747267200,
                \"value\": 1800
              }
            ]
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get detailed metric data and time trends for specific product categories
    - Analyze changes in core metrics like post volume, CTR, CVR for products
    - Help understand market performance and development trends of product categories

    ### Parameters:
    - id: Product category ID, e.g., Perfume: 601583
    - last: Number of recent days, e.g., 7, 30 days
    - metrics: Metric types, multiple separated by commas, e.g., \"post,ctr,cvr\"
    - ecom_type: E-commerce type, default \"l3\"
    - period_type: Period type, default \"last\"

    ### Return Description:
    - `info`: Product metric information
      - `comment`: Comment count
      - `cost`: Cost amount
      - `cover_url`: Cover image URL (may be null)
      - `cpa`: Cost per acquisition
      - `ctr`: Click-through rate
      - `ctr_metrics`: CTR time series data
        - `time`: Timestamp
        - `value`: CTR at that time
      - `cvr`: Conversion rate
      - `ecom_type`: E-commerce type
      - `first_ecom_category`: First-level e-commerce category
      - `impression`: Impression count
      - `like`: Like count
      - `play_six_rate`: 6-second play rate
      - `post`: Post volume
      - `post_change`: Post volume change rate
      - `post_metrics`: Post volume time series data
        - `time`: Timestamp
        - `value`: Post volume at that time
      - `second_ecom_category`: Second-level e-commerce category
      - `share`: Share count
      - `third_ecom_category`: Third-level e-commerce category
      - `url_title`: URL title

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_product_metrics\",
      \"params\": {
        \"id\": \"601583\",
        \"last\": \"30\",
        \"metrics\": \"post,ctr\",
        \"ecom_type\": \"l3\",
        \"period_type\": \"last\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"info\": {
            \"comment\": 13559,
            \"cost\": 2330000,
            \"cover_url\": null,
            \"cpa\": 12.4,
            \"ctr\": 1.04,
            \"ctr_metrics\": [
              {
                \"time\": 1747267200,
                \"value\": 0.88
              },
              {
                \"time\": 1747353600,
                \"value\": 0.99
              }
            ],
            \"cvr\": 15.2,
            \"ecom_type\": \"l3\",
            \"post\": 52300,
            \"post_change\": -8.12,
            \"post_metrics\": [
              {
                \"time\": 1747267200,
                \"value\": 1800
              }
            ]
          }
        }
      }
    }
    ```

    Args:
        id (str): 产品类目ID/Product category ID
        last (Union[Unset, int]): 最近天数/Last days Default: 30.
        metrics (Union[Unset, str]): 指标类型，逗号分隔/Metrics types, comma separated Default: 'post,ctr'.
        ecom_type (Union[Unset, str]): 电商类型/E-commerce type Default: 'l3'.
        period_type (Union[Unset, str]): 时间类型/Period type Default: 'last'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        id=id,
        last=last,
        metrics=metrics,
        ecom_type=ecom_type,
        period_type=period_type,
        country_code=country_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: str,
    last: Union[Unset, int] = 30,
    metrics: Union[Unset, str] = "post,ctr",
    ecom_type: Union[Unset, str] = "l3",
    period_type: Union[Unset, str] = "last",
    country_code: Union[Unset, str] = "US",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取产品指标数据/Get product metrics

     # [中文]
    ### 用途:
    - 获取特定产品类目的详细指标数据和时间趋势
    - 分析产品的发布量、点击率、转化率等核心指标变化
    - 帮助了解产品类目的市场表现和发展趋势

    ### 参数:
    - id: 产品类目ID，如香水：601583
    - last: 最近天数，如7、30天
    - metrics: 指标类型，多个用逗号分隔，如\"post,ctr,cvr\"
    - ecom_type: 电商类型，默认\"l3\"
    - period_type: 时间类型，默认\"last\"

    ### 返回内容说明:
    - `info`: 产品指标信息
      - `comment`: 评论数
      - `cost`: 花费金额
      - `cover_url`: 封面图URL（可能为null）
      - `cpa`: 每次转化成本
      - `ctr`: 点击率
      - `ctr_metrics`: 点击率时间序列数据
        - `time`: 时间戳
        - `value`: 对应时间的点击率
      - `cvr`: 转化率
      - `ecom_type`: 电商类型
      - `first_ecom_category`: 一级电商类目
      - `impression`: 展示量
      - `like`: 点赞数
      - `play_six_rate`: 6秒播放率
      - `post`: 发布量
      - `post_change`: 发布量变化率
      - `post_metrics`: 发布量时间序列数据
        - `time`: 时间戳
        - `value`: 对应时间的发布量
      - `second_ecom_category`: 二级电商类目
      - `share`: 分享数
      - `third_ecom_category`: 三级电商类目
      - `url_title`: URL标题

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_product_metrics\",
      \"params\": {
        \"id\": \"601583\",
        \"last\": \"30\",
        \"metrics\": \"post,ctr\",
        \"ecom_type\": \"l3\",
        \"period_type\": \"last\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"info\": {
            \"comment\": 13559,
            \"cost\": 2330000,
            \"cover_url\": null,
            \"cpa\": 12.4,
            \"ctr\": 1.04,
            \"ctr_metrics\": [
              {
                \"time\": 1747267200,
                \"value\": 0.88
              },
              {
                \"time\": 1747353600,
                \"value\": 0.99
              }
            ],
            \"cvr\": 15.2,
            \"ecom_type\": \"l3\",
            \"post\": 52300,
            \"post_change\": -8.12,
            \"post_metrics\": [
              {
                \"time\": 1747267200,
                \"value\": 1800
              }
            ]
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get detailed metric data and time trends for specific product categories
    - Analyze changes in core metrics like post volume, CTR, CVR for products
    - Help understand market performance and development trends of product categories

    ### Parameters:
    - id: Product category ID, e.g., Perfume: 601583
    - last: Number of recent days, e.g., 7, 30 days
    - metrics: Metric types, multiple separated by commas, e.g., \"post,ctr,cvr\"
    - ecom_type: E-commerce type, default \"l3\"
    - period_type: Period type, default \"last\"

    ### Return Description:
    - `info`: Product metric information
      - `comment`: Comment count
      - `cost`: Cost amount
      - `cover_url`: Cover image URL (may be null)
      - `cpa`: Cost per acquisition
      - `ctr`: Click-through rate
      - `ctr_metrics`: CTR time series data
        - `time`: Timestamp
        - `value`: CTR at that time
      - `cvr`: Conversion rate
      - `ecom_type`: E-commerce type
      - `first_ecom_category`: First-level e-commerce category
      - `impression`: Impression count
      - `like`: Like count
      - `play_six_rate`: 6-second play rate
      - `post`: Post volume
      - `post_change`: Post volume change rate
      - `post_metrics`: Post volume time series data
        - `time`: Timestamp
        - `value`: Post volume at that time
      - `second_ecom_category`: Second-level e-commerce category
      - `share`: Share count
      - `third_ecom_category`: Third-level e-commerce category
      - `url_title`: URL title

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_product_metrics\",
      \"params\": {
        \"id\": \"601583\",
        \"last\": \"30\",
        \"metrics\": \"post,ctr\",
        \"ecom_type\": \"l3\",
        \"period_type\": \"last\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"info\": {
            \"comment\": 13559,
            \"cost\": 2330000,
            \"cover_url\": null,
            \"cpa\": 12.4,
            \"ctr\": 1.04,
            \"ctr_metrics\": [
              {
                \"time\": 1747267200,
                \"value\": 0.88
              },
              {
                \"time\": 1747353600,
                \"value\": 0.99
              }
            ],
            \"cvr\": 15.2,
            \"ecom_type\": \"l3\",
            \"post\": 52300,
            \"post_change\": -8.12,
            \"post_metrics\": [
              {
                \"time\": 1747267200,
                \"value\": 1800
              }
            ]
          }
        }
      }
    }
    ```

    Args:
        id (str): 产品类目ID/Product category ID
        last (Union[Unset, int]): 最近天数/Last days Default: 30.
        metrics (Union[Unset, str]): 指标类型，逗号分隔/Metrics types, comma separated Default: 'post,ctr'.
        ecom_type (Union[Unset, str]): 电商类型/E-commerce type Default: 'l3'.
        period_type (Union[Unset, str]): 时间类型/Period type Default: 'last'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        id=id,
        last=last,
        metrics=metrics,
        ecom_type=ecom_type,
        period_type=period_type,
        country_code=country_code,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: str,
    last: Union[Unset, int] = 30,
    metrics: Union[Unset, str] = "post,ctr",
    ecom_type: Union[Unset, str] = "l3",
    period_type: Union[Unset, str] = "last",
    country_code: Union[Unset, str] = "US",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取产品指标数据/Get product metrics

     # [中文]
    ### 用途:
    - 获取特定产品类目的详细指标数据和时间趋势
    - 分析产品的发布量、点击率、转化率等核心指标变化
    - 帮助了解产品类目的市场表现和发展趋势

    ### 参数:
    - id: 产品类目ID，如香水：601583
    - last: 最近天数，如7、30天
    - metrics: 指标类型，多个用逗号分隔，如\"post,ctr,cvr\"
    - ecom_type: 电商类型，默认\"l3\"
    - period_type: 时间类型，默认\"last\"

    ### 返回内容说明:
    - `info`: 产品指标信息
      - `comment`: 评论数
      - `cost`: 花费金额
      - `cover_url`: 封面图URL（可能为null）
      - `cpa`: 每次转化成本
      - `ctr`: 点击率
      - `ctr_metrics`: 点击率时间序列数据
        - `time`: 时间戳
        - `value`: 对应时间的点击率
      - `cvr`: 转化率
      - `ecom_type`: 电商类型
      - `first_ecom_category`: 一级电商类目
      - `impression`: 展示量
      - `like`: 点赞数
      - `play_six_rate`: 6秒播放率
      - `post`: 发布量
      - `post_change`: 发布量变化率
      - `post_metrics`: 发布量时间序列数据
        - `time`: 时间戳
        - `value`: 对应时间的发布量
      - `second_ecom_category`: 二级电商类目
      - `share`: 分享数
      - `third_ecom_category`: 三级电商类目
      - `url_title`: URL标题

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_product_metrics\",
      \"params\": {
        \"id\": \"601583\",
        \"last\": \"30\",
        \"metrics\": \"post,ctr\",
        \"ecom_type\": \"l3\",
        \"period_type\": \"last\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"info\": {
            \"comment\": 13559,
            \"cost\": 2330000,
            \"cover_url\": null,
            \"cpa\": 12.4,
            \"ctr\": 1.04,
            \"ctr_metrics\": [
              {
                \"time\": 1747267200,
                \"value\": 0.88
              },
              {
                \"time\": 1747353600,
                \"value\": 0.99
              }
            ],
            \"cvr\": 15.2,
            \"ecom_type\": \"l3\",
            \"post\": 52300,
            \"post_change\": -8.12,
            \"post_metrics\": [
              {
                \"time\": 1747267200,
                \"value\": 1800
              }
            ]
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get detailed metric data and time trends for specific product categories
    - Analyze changes in core metrics like post volume, CTR, CVR for products
    - Help understand market performance and development trends of product categories

    ### Parameters:
    - id: Product category ID, e.g., Perfume: 601583
    - last: Number of recent days, e.g., 7, 30 days
    - metrics: Metric types, multiple separated by commas, e.g., \"post,ctr,cvr\"
    - ecom_type: E-commerce type, default \"l3\"
    - period_type: Period type, default \"last\"

    ### Return Description:
    - `info`: Product metric information
      - `comment`: Comment count
      - `cost`: Cost amount
      - `cover_url`: Cover image URL (may be null)
      - `cpa`: Cost per acquisition
      - `ctr`: Click-through rate
      - `ctr_metrics`: CTR time series data
        - `time`: Timestamp
        - `value`: CTR at that time
      - `cvr`: Conversion rate
      - `ecom_type`: E-commerce type
      - `first_ecom_category`: First-level e-commerce category
      - `impression`: Impression count
      - `like`: Like count
      - `play_six_rate`: 6-second play rate
      - `post`: Post volume
      - `post_change`: Post volume change rate
      - `post_metrics`: Post volume time series data
        - `time`: Timestamp
        - `value`: Post volume at that time
      - `second_ecom_category`: Second-level e-commerce category
      - `share`: Share count
      - `third_ecom_category`: Third-level e-commerce category
      - `url_title`: URL title

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_product_metrics\",
      \"params\": {
        \"id\": \"601583\",
        \"last\": \"30\",
        \"metrics\": \"post,ctr\",
        \"ecom_type\": \"l3\",
        \"period_type\": \"last\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"info\": {
            \"comment\": 13559,
            \"cost\": 2330000,
            \"cover_url\": null,
            \"cpa\": 12.4,
            \"ctr\": 1.04,
            \"ctr_metrics\": [
              {
                \"time\": 1747267200,
                \"value\": 0.88
              },
              {
                \"time\": 1747353600,
                \"value\": 0.99
              }
            ],
            \"cvr\": 15.2,
            \"ecom_type\": \"l3\",
            \"post\": 52300,
            \"post_change\": -8.12,
            \"post_metrics\": [
              {
                \"time\": 1747267200,
                \"value\": 1800
              }
            ]
          }
        }
      }
    }
    ```

    Args:
        id (str): 产品类目ID/Product category ID
        last (Union[Unset, int]): 最近天数/Last days Default: 30.
        metrics (Union[Unset, str]): 指标类型，逗号分隔/Metrics types, comma separated Default: 'post,ctr'.
        ecom_type (Union[Unset, str]): 电商类型/E-commerce type Default: 'l3'.
        period_type (Union[Unset, str]): 时间类型/Period type Default: 'last'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        id=id,
        last=last,
        metrics=metrics,
        ecom_type=ecom_type,
        period_type=period_type,
        country_code=country_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: str,
    last: Union[Unset, int] = 30,
    metrics: Union[Unset, str] = "post,ctr",
    ecom_type: Union[Unset, str] = "l3",
    period_type: Union[Unset, str] = "last",
    country_code: Union[Unset, str] = "US",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取产品指标数据/Get product metrics

     # [中文]
    ### 用途:
    - 获取特定产品类目的详细指标数据和时间趋势
    - 分析产品的发布量、点击率、转化率等核心指标变化
    - 帮助了解产品类目的市场表现和发展趋势

    ### 参数:
    - id: 产品类目ID，如香水：601583
    - last: 最近天数，如7、30天
    - metrics: 指标类型，多个用逗号分隔，如\"post,ctr,cvr\"
    - ecom_type: 电商类型，默认\"l3\"
    - period_type: 时间类型，默认\"last\"

    ### 返回内容说明:
    - `info`: 产品指标信息
      - `comment`: 评论数
      - `cost`: 花费金额
      - `cover_url`: 封面图URL（可能为null）
      - `cpa`: 每次转化成本
      - `ctr`: 点击率
      - `ctr_metrics`: 点击率时间序列数据
        - `time`: 时间戳
        - `value`: 对应时间的点击率
      - `cvr`: 转化率
      - `ecom_type`: 电商类型
      - `first_ecom_category`: 一级电商类目
      - `impression`: 展示量
      - `like`: 点赞数
      - `play_six_rate`: 6秒播放率
      - `post`: 发布量
      - `post_change`: 发布量变化率
      - `post_metrics`: 发布量时间序列数据
        - `time`: 时间戳
        - `value`: 对应时间的发布量
      - `second_ecom_category`: 二级电商类目
      - `share`: 分享数
      - `third_ecom_category`: 三级电商类目
      - `url_title`: URL标题

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_product_metrics\",
      \"params\": {
        \"id\": \"601583\",
        \"last\": \"30\",
        \"metrics\": \"post,ctr\",
        \"ecom_type\": \"l3\",
        \"period_type\": \"last\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"info\": {
            \"comment\": 13559,
            \"cost\": 2330000,
            \"cover_url\": null,
            \"cpa\": 12.4,
            \"ctr\": 1.04,
            \"ctr_metrics\": [
              {
                \"time\": 1747267200,
                \"value\": 0.88
              },
              {
                \"time\": 1747353600,
                \"value\": 0.99
              }
            ],
            \"cvr\": 15.2,
            \"ecom_type\": \"l3\",
            \"post\": 52300,
            \"post_change\": -8.12,
            \"post_metrics\": [
              {
                \"time\": 1747267200,
                \"value\": 1800
              }
            ]
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get detailed metric data and time trends for specific product categories
    - Analyze changes in core metrics like post volume, CTR, CVR for products
    - Help understand market performance and development trends of product categories

    ### Parameters:
    - id: Product category ID, e.g., Perfume: 601583
    - last: Number of recent days, e.g., 7, 30 days
    - metrics: Metric types, multiple separated by commas, e.g., \"post,ctr,cvr\"
    - ecom_type: E-commerce type, default \"l3\"
    - period_type: Period type, default \"last\"

    ### Return Description:
    - `info`: Product metric information
      - `comment`: Comment count
      - `cost`: Cost amount
      - `cover_url`: Cover image URL (may be null)
      - `cpa`: Cost per acquisition
      - `ctr`: Click-through rate
      - `ctr_metrics`: CTR time series data
        - `time`: Timestamp
        - `value`: CTR at that time
      - `cvr`: Conversion rate
      - `ecom_type`: E-commerce type
      - `first_ecom_category`: First-level e-commerce category
      - `impression`: Impression count
      - `like`: Like count
      - `play_six_rate`: 6-second play rate
      - `post`: Post volume
      - `post_change`: Post volume change rate
      - `post_metrics`: Post volume time series data
        - `time`: Timestamp
        - `value`: Post volume at that time
      - `second_ecom_category`: Second-level e-commerce category
      - `share`: Share count
      - `third_ecom_category`: Third-level e-commerce category
      - `url_title`: URL title

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_product_metrics\",
      \"params\": {
        \"id\": \"601583\",
        \"last\": \"30\",
        \"metrics\": \"post,ctr\",
        \"ecom_type\": \"l3\",
        \"period_type\": \"last\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"info\": {
            \"comment\": 13559,
            \"cost\": 2330000,
            \"cover_url\": null,
            \"cpa\": 12.4,
            \"ctr\": 1.04,
            \"ctr_metrics\": [
              {
                \"time\": 1747267200,
                \"value\": 0.88
              },
              {
                \"time\": 1747353600,
                \"value\": 0.99
              }
            ],
            \"cvr\": 15.2,
            \"ecom_type\": \"l3\",
            \"post\": 52300,
            \"post_change\": -8.12,
            \"post_metrics\": [
              {
                \"time\": 1747267200,
                \"value\": 1800
              }
            ]
          }
        }
      }
    }
    ```

    Args:
        id (str): 产品类目ID/Product category ID
        last (Union[Unset, int]): 最近天数/Last days Default: 30.
        metrics (Union[Unset, str]): 指标类型，逗号分隔/Metrics types, comma separated Default: 'post,ctr'.
        ecom_type (Union[Unset, str]): 电商类型/E-commerce type Default: 'l3'.
        period_type (Union[Unset, str]): 时间类型/Period type Default: 'last'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            last=last,
            metrics=metrics,
            ecom_type=ecom_type,
            period_type=period_type,
            country_code=country_code,
        )
    ).parsed
