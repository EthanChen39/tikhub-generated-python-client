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
    last: Union[Unset, int] = 7,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    country_code: Union[Unset, str] = "US",
    first_ecom_category_id: Union[Unset, str] = "",
    ecom_type: Union[Unset, str] = "l3",
    period_type: Union[Unset, str] = "last",
    order_by: Union[Unset, str] = "post",
    order_type: Union[Unset, str] = "desc",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["last"] = last

    params["page"] = page

    params["limit"] = limit

    params["country_code"] = country_code

    params["first_ecom_category_id"] = first_ecom_category_id

    params["ecom_type"] = ecom_type

    params["period_type"] = period_type

    params["order_by"] = order_by

    params["order_type"] = order_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/get_top_products",
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
    last: Union[Unset, int] = 7,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    country_code: Union[Unset, str] = "US",
    first_ecom_category_id: Union[Unset, str] = "",
    ecom_type: Union[Unset, str] = "l3",
    period_type: Union[Unset, str] = "last",
    order_by: Union[Unset, str] = "post",
    order_type: Union[Unset, str] = "desc",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取热门产品列表/Get top products list

     # [中文]
    ### 用途:
    - 获取TikTok广告中的热门产品排行榜，了解各类目下的爆款产品
    - 分析产品的广告投放量、点击率、转化率等核心指标
    - 帮助电商卖家发现潜力产品，优化选品和营销策略

    ### 参数:
    - last: 最近天数，如7、30天
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - country_code: 国家代码，如US、UK、JP等
    - first_ecom_category_id: 电商类目ID，多个用逗号分隔
    - ecom_type: 电商类型，默认\"l3\"
    - period_type: 时间类型，默认\"last\"
    - order_by: 排序字段，可选：post（发布量）、ctr（点击率）、cvr（转化率）
    - order_type: 排序方式，desc（降序）或asc（升序）

    ### 常用电商类目ID:
    - 美妆个护: 605196
    - 女装女内衣: 602284
    - 时尚配饰: 601450
    - 手机电子: 801928
    - 健康产品: 951432
    - 家居用品: 601755
    - 男装男内衣: 605248
    - 香水: 601583

    ### 返回内容说明:
    - `list`: 产品列表
      - `comment`: 评论数
      - `cost`: 花费金额
      - `cover_url`: 封面图URL（可能为null）
      - `cpa`: 每次转化成本
      - `ctr`: 点击率（百分比）
      - `cvr`: 转化率（百分比）
      - `ecom_type`: 电商类型
      - `first_ecom_category`: 一级电商类目
        - `id`: 类目ID
        - `label`: 类目标签
        - `value`: 类目名称
      - `impression`: 展示量
      - `like`: 点赞数
      - `play_six_rate`: 6秒播放率（百分比）
      - `post`: 发布量
      - `post_change`: 发布量变化率（百分比）
      - `second_ecom_category`: 二级电商类目
        - `id`: 类目ID
        - `label`: 类目标签
        - `parent_id`: 父类目ID
        - `value`: 类目名称
      - `share`: 分享数
      - `third_ecom_category`: 三级电商类目
        - `id`: 类目ID
        - `label`: 类目标签
        - `parent_id`: 父类目ID
        - `value`: 类目名称
      - `url_title`: URL标题
    - `pagination`: 分页信息
      - `page`: 当前页
      - `size`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_top_products\",
      \"params\": {
        \"last\": \"7\",
        \"page\": \"1\",
        \"limit\": \"20\",
        \"country_code\": \"US\",
        \"first_ecom_category_id\": \"\",
        \"ecom_type\": \"l3\",
        \"period_type\": \"last\",
        \"order_by\": \"post\",
        \"order_type\": \"desc\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"list\": [
            {
              \"comment\": 3449,
              \"cost\": 477000,
              \"cover_url\": null,
              \"cpa\": 9.21,
              \"ctr\": 1.29,
              \"cvr\": 12.94,
              \"ecom_type\": \"l3\",
              \"first_ecom_category\": {
                \"id\": \"601450\",
                \"label\": \"category_601450\",
                \"value\": \"Beauty & Personal Care\"
              },
              \"impression\": 65000000,
              \"like\": 166618,
              \"play_six_rate\": 7.62,
              \"post\": 10600,
              \"post_change\": -10.16,
              \"second_ecom_category\": {
                \"id\": \"848648\",
                \"label\": \"category_848648\",
                \"parent_id\": \"601450\",
                \"value\": \"Makeup & Perfume\"
              },
              \"share\": 2359,
              \"third_ecom_category\": {
                \"id\": \"601583\",
                \"label\": \"category_601583\",
                \"parent_id\": \"848648\",
                \"value\": \"Perfume\"
              },
              \"url_title\": \"Perfume\"
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 156,
            \"has_more\": true
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get top product rankings in TikTok ads to understand popular products in various categories
    - Analyze core metrics like ad post volume, CTR, and conversion rate for products
    - Help e-commerce sellers discover potential products and optimize product selection and marketing
    strategies

    ### Parameters:
    - last: Number of recent days, e.g., 7, 30 days
    - page: Page number, default 1
    - limit: Items per page, default 20
    - country_code: Country code, e.g., US, UK, JP
    - first_ecom_category_id: E-commerce category IDs, multiple separated by commas
    - ecom_type: E-commerce type, default \"l3\"
    - period_type: Period type, default \"last\"
    - order_by: Sort field, options: post (post volume), ctr (click-through rate), cvr (conversion rate)
    - order_type: Sort order, desc (descending) or asc (ascending)

    ### Common E-commerce Category IDs:
    - Beauty & Personal Care: 605196
    - Women's Clothing & Underwear: 602284
    - Fashion Accessories: 601450
    - Mobile & Electronics: 801928
    - Health Products: 951432
    - Home & Living: 601755
    - Men's Clothing & Underwear: 605248
    - Perfume: 601583

    ### Return Description:
    - `list`: Product list
      - `comment`: Comment count
      - `cost`: Cost amount
      - `cover_url`: Cover image URL (may be null)
      - `cpa`: Cost per acquisition
      - `ctr`: Click-through rate (percentage)
      - `cvr`: Conversion rate (percentage)
      - `ecom_type`: E-commerce type
      - `first_ecom_category`: First-level e-commerce category
        - `id`: Category ID
        - `label`: Category label
        - `value`: Category name
      - `impression`: Impression count
      - `like`: Like count
      - `play_six_rate`: 6-second play rate (percentage)
      - `post`: Post volume
      - `post_change`: Post volume change rate (percentage)
      - `second_ecom_category`: Second-level e-commerce category
        - `id`: Category ID
        - `label`: Category label
        - `parent_id`: Parent category ID
        - `value`: Category name
      - `share`: Share count
      - `third_ecom_category`: Third-level e-commerce category
        - `id`: Category ID
        - `label`: Category label
        - `parent_id`: Parent category ID
        - `value`: Category name
      - `url_title`: URL title
    - `pagination`: Pagination info
      - `page`: Current page
      - `size`: Items per page
      - `total`: Total count
      - `has_more`: Whether there are more items

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_top_products\",
      \"params\": {
        \"last\": \"7\",
        \"page\": \"1\",
        \"limit\": \"20\",
        \"country_code\": \"US\",
        \"first_ecom_category_id\": \"\",
        \"ecom_type\": \"l3\",
        \"period_type\": \"last\",
        \"order_by\": \"post\",
        \"order_type\": \"desc\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"list\": [
            {
              \"comment\": 3449,
              \"cost\": 477000,
              \"cover_url\": null,
              \"cpa\": 9.21,
              \"ctr\": 1.29,
              \"cvr\": 12.94,
              \"ecom_type\": \"l3\",
              \"first_ecom_category\": {
                \"id\": \"601450\",
                \"label\": \"category_601450\",
                \"value\": \"Beauty & Personal Care\"
              },
              \"impression\": 65000000,
              \"like\": 166618,
              \"play_six_rate\": 7.62,
              \"post\": 10600,
              \"post_change\": -10.16,
              \"second_ecom_category\": {
                \"id\": \"848648\",
                \"label\": \"category_848648\",
                \"parent_id\": \"601450\",
                \"value\": \"Makeup & Perfume\"
              },
              \"share\": 2359,
              \"third_ecom_category\": {
                \"id\": \"601583\",
                \"label\": \"category_601583\",
                \"parent_id\": \"848648\",
                \"value\": \"Perfume\"
              },
              \"url_title\": \"Perfume\"
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 156,
            \"has_more\": true
          }
        }
      }
    }
    ```

    Args:
        last (Union[Unset, int]): 最近天数/Last days Default: 7.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.
        first_ecom_category_id (Union[Unset, str]): 电商类目ID，多个用逗号分隔/E-commerce category IDs, comma
            separated Default: ''.
        ecom_type (Union[Unset, str]): 电商类型/E-commerce type (l3) Default: 'l3'.
        period_type (Union[Unset, str]): 时间类型/Period type (last) Default: 'last'.
        order_by (Union[Unset, str]): 排序字段/Sort field (post, ctr, cvr) Default: 'post'.
        order_type (Union[Unset, str]): 排序方式/Sort order (desc, asc) Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        last=last,
        page=page,
        limit=limit,
        country_code=country_code,
        first_ecom_category_id=first_ecom_category_id,
        ecom_type=ecom_type,
        period_type=period_type,
        order_by=order_by,
        order_type=order_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    last: Union[Unset, int] = 7,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    country_code: Union[Unset, str] = "US",
    first_ecom_category_id: Union[Unset, str] = "",
    ecom_type: Union[Unset, str] = "l3",
    period_type: Union[Unset, str] = "last",
    order_by: Union[Unset, str] = "post",
    order_type: Union[Unset, str] = "desc",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取热门产品列表/Get top products list

     # [中文]
    ### 用途:
    - 获取TikTok广告中的热门产品排行榜，了解各类目下的爆款产品
    - 分析产品的广告投放量、点击率、转化率等核心指标
    - 帮助电商卖家发现潜力产品，优化选品和营销策略

    ### 参数:
    - last: 最近天数，如7、30天
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - country_code: 国家代码，如US、UK、JP等
    - first_ecom_category_id: 电商类目ID，多个用逗号分隔
    - ecom_type: 电商类型，默认\"l3\"
    - period_type: 时间类型，默认\"last\"
    - order_by: 排序字段，可选：post（发布量）、ctr（点击率）、cvr（转化率）
    - order_type: 排序方式，desc（降序）或asc（升序）

    ### 常用电商类目ID:
    - 美妆个护: 605196
    - 女装女内衣: 602284
    - 时尚配饰: 601450
    - 手机电子: 801928
    - 健康产品: 951432
    - 家居用品: 601755
    - 男装男内衣: 605248
    - 香水: 601583

    ### 返回内容说明:
    - `list`: 产品列表
      - `comment`: 评论数
      - `cost`: 花费金额
      - `cover_url`: 封面图URL（可能为null）
      - `cpa`: 每次转化成本
      - `ctr`: 点击率（百分比）
      - `cvr`: 转化率（百分比）
      - `ecom_type`: 电商类型
      - `first_ecom_category`: 一级电商类目
        - `id`: 类目ID
        - `label`: 类目标签
        - `value`: 类目名称
      - `impression`: 展示量
      - `like`: 点赞数
      - `play_six_rate`: 6秒播放率（百分比）
      - `post`: 发布量
      - `post_change`: 发布量变化率（百分比）
      - `second_ecom_category`: 二级电商类目
        - `id`: 类目ID
        - `label`: 类目标签
        - `parent_id`: 父类目ID
        - `value`: 类目名称
      - `share`: 分享数
      - `third_ecom_category`: 三级电商类目
        - `id`: 类目ID
        - `label`: 类目标签
        - `parent_id`: 父类目ID
        - `value`: 类目名称
      - `url_title`: URL标题
    - `pagination`: 分页信息
      - `page`: 当前页
      - `size`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_top_products\",
      \"params\": {
        \"last\": \"7\",
        \"page\": \"1\",
        \"limit\": \"20\",
        \"country_code\": \"US\",
        \"first_ecom_category_id\": \"\",
        \"ecom_type\": \"l3\",
        \"period_type\": \"last\",
        \"order_by\": \"post\",
        \"order_type\": \"desc\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"list\": [
            {
              \"comment\": 3449,
              \"cost\": 477000,
              \"cover_url\": null,
              \"cpa\": 9.21,
              \"ctr\": 1.29,
              \"cvr\": 12.94,
              \"ecom_type\": \"l3\",
              \"first_ecom_category\": {
                \"id\": \"601450\",
                \"label\": \"category_601450\",
                \"value\": \"Beauty & Personal Care\"
              },
              \"impression\": 65000000,
              \"like\": 166618,
              \"play_six_rate\": 7.62,
              \"post\": 10600,
              \"post_change\": -10.16,
              \"second_ecom_category\": {
                \"id\": \"848648\",
                \"label\": \"category_848648\",
                \"parent_id\": \"601450\",
                \"value\": \"Makeup & Perfume\"
              },
              \"share\": 2359,
              \"third_ecom_category\": {
                \"id\": \"601583\",
                \"label\": \"category_601583\",
                \"parent_id\": \"848648\",
                \"value\": \"Perfume\"
              },
              \"url_title\": \"Perfume\"
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 156,
            \"has_more\": true
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get top product rankings in TikTok ads to understand popular products in various categories
    - Analyze core metrics like ad post volume, CTR, and conversion rate for products
    - Help e-commerce sellers discover potential products and optimize product selection and marketing
    strategies

    ### Parameters:
    - last: Number of recent days, e.g., 7, 30 days
    - page: Page number, default 1
    - limit: Items per page, default 20
    - country_code: Country code, e.g., US, UK, JP
    - first_ecom_category_id: E-commerce category IDs, multiple separated by commas
    - ecom_type: E-commerce type, default \"l3\"
    - period_type: Period type, default \"last\"
    - order_by: Sort field, options: post (post volume), ctr (click-through rate), cvr (conversion rate)
    - order_type: Sort order, desc (descending) or asc (ascending)

    ### Common E-commerce Category IDs:
    - Beauty & Personal Care: 605196
    - Women's Clothing & Underwear: 602284
    - Fashion Accessories: 601450
    - Mobile & Electronics: 801928
    - Health Products: 951432
    - Home & Living: 601755
    - Men's Clothing & Underwear: 605248
    - Perfume: 601583

    ### Return Description:
    - `list`: Product list
      - `comment`: Comment count
      - `cost`: Cost amount
      - `cover_url`: Cover image URL (may be null)
      - `cpa`: Cost per acquisition
      - `ctr`: Click-through rate (percentage)
      - `cvr`: Conversion rate (percentage)
      - `ecom_type`: E-commerce type
      - `first_ecom_category`: First-level e-commerce category
        - `id`: Category ID
        - `label`: Category label
        - `value`: Category name
      - `impression`: Impression count
      - `like`: Like count
      - `play_six_rate`: 6-second play rate (percentage)
      - `post`: Post volume
      - `post_change`: Post volume change rate (percentage)
      - `second_ecom_category`: Second-level e-commerce category
        - `id`: Category ID
        - `label`: Category label
        - `parent_id`: Parent category ID
        - `value`: Category name
      - `share`: Share count
      - `third_ecom_category`: Third-level e-commerce category
        - `id`: Category ID
        - `label`: Category label
        - `parent_id`: Parent category ID
        - `value`: Category name
      - `url_title`: URL title
    - `pagination`: Pagination info
      - `page`: Current page
      - `size`: Items per page
      - `total`: Total count
      - `has_more`: Whether there are more items

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_top_products\",
      \"params\": {
        \"last\": \"7\",
        \"page\": \"1\",
        \"limit\": \"20\",
        \"country_code\": \"US\",
        \"first_ecom_category_id\": \"\",
        \"ecom_type\": \"l3\",
        \"period_type\": \"last\",
        \"order_by\": \"post\",
        \"order_type\": \"desc\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"list\": [
            {
              \"comment\": 3449,
              \"cost\": 477000,
              \"cover_url\": null,
              \"cpa\": 9.21,
              \"ctr\": 1.29,
              \"cvr\": 12.94,
              \"ecom_type\": \"l3\",
              \"first_ecom_category\": {
                \"id\": \"601450\",
                \"label\": \"category_601450\",
                \"value\": \"Beauty & Personal Care\"
              },
              \"impression\": 65000000,
              \"like\": 166618,
              \"play_six_rate\": 7.62,
              \"post\": 10600,
              \"post_change\": -10.16,
              \"second_ecom_category\": {
                \"id\": \"848648\",
                \"label\": \"category_848648\",
                \"parent_id\": \"601450\",
                \"value\": \"Makeup & Perfume\"
              },
              \"share\": 2359,
              \"third_ecom_category\": {
                \"id\": \"601583\",
                \"label\": \"category_601583\",
                \"parent_id\": \"848648\",
                \"value\": \"Perfume\"
              },
              \"url_title\": \"Perfume\"
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 156,
            \"has_more\": true
          }
        }
      }
    }
    ```

    Args:
        last (Union[Unset, int]): 最近天数/Last days Default: 7.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.
        first_ecom_category_id (Union[Unset, str]): 电商类目ID，多个用逗号分隔/E-commerce category IDs, comma
            separated Default: ''.
        ecom_type (Union[Unset, str]): 电商类型/E-commerce type (l3) Default: 'l3'.
        period_type (Union[Unset, str]): 时间类型/Period type (last) Default: 'last'.
        order_by (Union[Unset, str]): 排序字段/Sort field (post, ctr, cvr) Default: 'post'.
        order_type (Union[Unset, str]): 排序方式/Sort order (desc, asc) Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        last=last,
        page=page,
        limit=limit,
        country_code=country_code,
        first_ecom_category_id=first_ecom_category_id,
        ecom_type=ecom_type,
        period_type=period_type,
        order_by=order_by,
        order_type=order_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    last: Union[Unset, int] = 7,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    country_code: Union[Unset, str] = "US",
    first_ecom_category_id: Union[Unset, str] = "",
    ecom_type: Union[Unset, str] = "l3",
    period_type: Union[Unset, str] = "last",
    order_by: Union[Unset, str] = "post",
    order_type: Union[Unset, str] = "desc",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取热门产品列表/Get top products list

     # [中文]
    ### 用途:
    - 获取TikTok广告中的热门产品排行榜，了解各类目下的爆款产品
    - 分析产品的广告投放量、点击率、转化率等核心指标
    - 帮助电商卖家发现潜力产品，优化选品和营销策略

    ### 参数:
    - last: 最近天数，如7、30天
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - country_code: 国家代码，如US、UK、JP等
    - first_ecom_category_id: 电商类目ID，多个用逗号分隔
    - ecom_type: 电商类型，默认\"l3\"
    - period_type: 时间类型，默认\"last\"
    - order_by: 排序字段，可选：post（发布量）、ctr（点击率）、cvr（转化率）
    - order_type: 排序方式，desc（降序）或asc（升序）

    ### 常用电商类目ID:
    - 美妆个护: 605196
    - 女装女内衣: 602284
    - 时尚配饰: 601450
    - 手机电子: 801928
    - 健康产品: 951432
    - 家居用品: 601755
    - 男装男内衣: 605248
    - 香水: 601583

    ### 返回内容说明:
    - `list`: 产品列表
      - `comment`: 评论数
      - `cost`: 花费金额
      - `cover_url`: 封面图URL（可能为null）
      - `cpa`: 每次转化成本
      - `ctr`: 点击率（百分比）
      - `cvr`: 转化率（百分比）
      - `ecom_type`: 电商类型
      - `first_ecom_category`: 一级电商类目
        - `id`: 类目ID
        - `label`: 类目标签
        - `value`: 类目名称
      - `impression`: 展示量
      - `like`: 点赞数
      - `play_six_rate`: 6秒播放率（百分比）
      - `post`: 发布量
      - `post_change`: 发布量变化率（百分比）
      - `second_ecom_category`: 二级电商类目
        - `id`: 类目ID
        - `label`: 类目标签
        - `parent_id`: 父类目ID
        - `value`: 类目名称
      - `share`: 分享数
      - `third_ecom_category`: 三级电商类目
        - `id`: 类目ID
        - `label`: 类目标签
        - `parent_id`: 父类目ID
        - `value`: 类目名称
      - `url_title`: URL标题
    - `pagination`: 分页信息
      - `page`: 当前页
      - `size`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_top_products\",
      \"params\": {
        \"last\": \"7\",
        \"page\": \"1\",
        \"limit\": \"20\",
        \"country_code\": \"US\",
        \"first_ecom_category_id\": \"\",
        \"ecom_type\": \"l3\",
        \"period_type\": \"last\",
        \"order_by\": \"post\",
        \"order_type\": \"desc\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"list\": [
            {
              \"comment\": 3449,
              \"cost\": 477000,
              \"cover_url\": null,
              \"cpa\": 9.21,
              \"ctr\": 1.29,
              \"cvr\": 12.94,
              \"ecom_type\": \"l3\",
              \"first_ecom_category\": {
                \"id\": \"601450\",
                \"label\": \"category_601450\",
                \"value\": \"Beauty & Personal Care\"
              },
              \"impression\": 65000000,
              \"like\": 166618,
              \"play_six_rate\": 7.62,
              \"post\": 10600,
              \"post_change\": -10.16,
              \"second_ecom_category\": {
                \"id\": \"848648\",
                \"label\": \"category_848648\",
                \"parent_id\": \"601450\",
                \"value\": \"Makeup & Perfume\"
              },
              \"share\": 2359,
              \"third_ecom_category\": {
                \"id\": \"601583\",
                \"label\": \"category_601583\",
                \"parent_id\": \"848648\",
                \"value\": \"Perfume\"
              },
              \"url_title\": \"Perfume\"
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 156,
            \"has_more\": true
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get top product rankings in TikTok ads to understand popular products in various categories
    - Analyze core metrics like ad post volume, CTR, and conversion rate for products
    - Help e-commerce sellers discover potential products and optimize product selection and marketing
    strategies

    ### Parameters:
    - last: Number of recent days, e.g., 7, 30 days
    - page: Page number, default 1
    - limit: Items per page, default 20
    - country_code: Country code, e.g., US, UK, JP
    - first_ecom_category_id: E-commerce category IDs, multiple separated by commas
    - ecom_type: E-commerce type, default \"l3\"
    - period_type: Period type, default \"last\"
    - order_by: Sort field, options: post (post volume), ctr (click-through rate), cvr (conversion rate)
    - order_type: Sort order, desc (descending) or asc (ascending)

    ### Common E-commerce Category IDs:
    - Beauty & Personal Care: 605196
    - Women's Clothing & Underwear: 602284
    - Fashion Accessories: 601450
    - Mobile & Electronics: 801928
    - Health Products: 951432
    - Home & Living: 601755
    - Men's Clothing & Underwear: 605248
    - Perfume: 601583

    ### Return Description:
    - `list`: Product list
      - `comment`: Comment count
      - `cost`: Cost amount
      - `cover_url`: Cover image URL (may be null)
      - `cpa`: Cost per acquisition
      - `ctr`: Click-through rate (percentage)
      - `cvr`: Conversion rate (percentage)
      - `ecom_type`: E-commerce type
      - `first_ecom_category`: First-level e-commerce category
        - `id`: Category ID
        - `label`: Category label
        - `value`: Category name
      - `impression`: Impression count
      - `like`: Like count
      - `play_six_rate`: 6-second play rate (percentage)
      - `post`: Post volume
      - `post_change`: Post volume change rate (percentage)
      - `second_ecom_category`: Second-level e-commerce category
        - `id`: Category ID
        - `label`: Category label
        - `parent_id`: Parent category ID
        - `value`: Category name
      - `share`: Share count
      - `third_ecom_category`: Third-level e-commerce category
        - `id`: Category ID
        - `label`: Category label
        - `parent_id`: Parent category ID
        - `value`: Category name
      - `url_title`: URL title
    - `pagination`: Pagination info
      - `page`: Current page
      - `size`: Items per page
      - `total`: Total count
      - `has_more`: Whether there are more items

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_top_products\",
      \"params\": {
        \"last\": \"7\",
        \"page\": \"1\",
        \"limit\": \"20\",
        \"country_code\": \"US\",
        \"first_ecom_category_id\": \"\",
        \"ecom_type\": \"l3\",
        \"period_type\": \"last\",
        \"order_by\": \"post\",
        \"order_type\": \"desc\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"list\": [
            {
              \"comment\": 3449,
              \"cost\": 477000,
              \"cover_url\": null,
              \"cpa\": 9.21,
              \"ctr\": 1.29,
              \"cvr\": 12.94,
              \"ecom_type\": \"l3\",
              \"first_ecom_category\": {
                \"id\": \"601450\",
                \"label\": \"category_601450\",
                \"value\": \"Beauty & Personal Care\"
              },
              \"impression\": 65000000,
              \"like\": 166618,
              \"play_six_rate\": 7.62,
              \"post\": 10600,
              \"post_change\": -10.16,
              \"second_ecom_category\": {
                \"id\": \"848648\",
                \"label\": \"category_848648\",
                \"parent_id\": \"601450\",
                \"value\": \"Makeup & Perfume\"
              },
              \"share\": 2359,
              \"third_ecom_category\": {
                \"id\": \"601583\",
                \"label\": \"category_601583\",
                \"parent_id\": \"848648\",
                \"value\": \"Perfume\"
              },
              \"url_title\": \"Perfume\"
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 156,
            \"has_more\": true
          }
        }
      }
    }
    ```

    Args:
        last (Union[Unset, int]): 最近天数/Last days Default: 7.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.
        first_ecom_category_id (Union[Unset, str]): 电商类目ID，多个用逗号分隔/E-commerce category IDs, comma
            separated Default: ''.
        ecom_type (Union[Unset, str]): 电商类型/E-commerce type (l3) Default: 'l3'.
        period_type (Union[Unset, str]): 时间类型/Period type (last) Default: 'last'.
        order_by (Union[Unset, str]): 排序字段/Sort field (post, ctr, cvr) Default: 'post'.
        order_type (Union[Unset, str]): 排序方式/Sort order (desc, asc) Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        last=last,
        page=page,
        limit=limit,
        country_code=country_code,
        first_ecom_category_id=first_ecom_category_id,
        ecom_type=ecom_type,
        period_type=period_type,
        order_by=order_by,
        order_type=order_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    last: Union[Unset, int] = 7,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    country_code: Union[Unset, str] = "US",
    first_ecom_category_id: Union[Unset, str] = "",
    ecom_type: Union[Unset, str] = "l3",
    period_type: Union[Unset, str] = "last",
    order_by: Union[Unset, str] = "post",
    order_type: Union[Unset, str] = "desc",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取热门产品列表/Get top products list

     # [中文]
    ### 用途:
    - 获取TikTok广告中的热门产品排行榜，了解各类目下的爆款产品
    - 分析产品的广告投放量、点击率、转化率等核心指标
    - 帮助电商卖家发现潜力产品，优化选品和营销策略

    ### 参数:
    - last: 最近天数，如7、30天
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - country_code: 国家代码，如US、UK、JP等
    - first_ecom_category_id: 电商类目ID，多个用逗号分隔
    - ecom_type: 电商类型，默认\"l3\"
    - period_type: 时间类型，默认\"last\"
    - order_by: 排序字段，可选：post（发布量）、ctr（点击率）、cvr（转化率）
    - order_type: 排序方式，desc（降序）或asc（升序）

    ### 常用电商类目ID:
    - 美妆个护: 605196
    - 女装女内衣: 602284
    - 时尚配饰: 601450
    - 手机电子: 801928
    - 健康产品: 951432
    - 家居用品: 601755
    - 男装男内衣: 605248
    - 香水: 601583

    ### 返回内容说明:
    - `list`: 产品列表
      - `comment`: 评论数
      - `cost`: 花费金额
      - `cover_url`: 封面图URL（可能为null）
      - `cpa`: 每次转化成本
      - `ctr`: 点击率（百分比）
      - `cvr`: 转化率（百分比）
      - `ecom_type`: 电商类型
      - `first_ecom_category`: 一级电商类目
        - `id`: 类目ID
        - `label`: 类目标签
        - `value`: 类目名称
      - `impression`: 展示量
      - `like`: 点赞数
      - `play_six_rate`: 6秒播放率（百分比）
      - `post`: 发布量
      - `post_change`: 发布量变化率（百分比）
      - `second_ecom_category`: 二级电商类目
        - `id`: 类目ID
        - `label`: 类目标签
        - `parent_id`: 父类目ID
        - `value`: 类目名称
      - `share`: 分享数
      - `third_ecom_category`: 三级电商类目
        - `id`: 类目ID
        - `label`: 类目标签
        - `parent_id`: 父类目ID
        - `value`: 类目名称
      - `url_title`: URL标题
    - `pagination`: 分页信息
      - `page`: 当前页
      - `size`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_top_products\",
      \"params\": {
        \"last\": \"7\",
        \"page\": \"1\",
        \"limit\": \"20\",
        \"country_code\": \"US\",
        \"first_ecom_category_id\": \"\",
        \"ecom_type\": \"l3\",
        \"period_type\": \"last\",
        \"order_by\": \"post\",
        \"order_type\": \"desc\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"list\": [
            {
              \"comment\": 3449,
              \"cost\": 477000,
              \"cover_url\": null,
              \"cpa\": 9.21,
              \"ctr\": 1.29,
              \"cvr\": 12.94,
              \"ecom_type\": \"l3\",
              \"first_ecom_category\": {
                \"id\": \"601450\",
                \"label\": \"category_601450\",
                \"value\": \"Beauty & Personal Care\"
              },
              \"impression\": 65000000,
              \"like\": 166618,
              \"play_six_rate\": 7.62,
              \"post\": 10600,
              \"post_change\": -10.16,
              \"second_ecom_category\": {
                \"id\": \"848648\",
                \"label\": \"category_848648\",
                \"parent_id\": \"601450\",
                \"value\": \"Makeup & Perfume\"
              },
              \"share\": 2359,
              \"third_ecom_category\": {
                \"id\": \"601583\",
                \"label\": \"category_601583\",
                \"parent_id\": \"848648\",
                \"value\": \"Perfume\"
              },
              \"url_title\": \"Perfume\"
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 156,
            \"has_more\": true
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get top product rankings in TikTok ads to understand popular products in various categories
    - Analyze core metrics like ad post volume, CTR, and conversion rate for products
    - Help e-commerce sellers discover potential products and optimize product selection and marketing
    strategies

    ### Parameters:
    - last: Number of recent days, e.g., 7, 30 days
    - page: Page number, default 1
    - limit: Items per page, default 20
    - country_code: Country code, e.g., US, UK, JP
    - first_ecom_category_id: E-commerce category IDs, multiple separated by commas
    - ecom_type: E-commerce type, default \"l3\"
    - period_type: Period type, default \"last\"
    - order_by: Sort field, options: post (post volume), ctr (click-through rate), cvr (conversion rate)
    - order_type: Sort order, desc (descending) or asc (ascending)

    ### Common E-commerce Category IDs:
    - Beauty & Personal Care: 605196
    - Women's Clothing & Underwear: 602284
    - Fashion Accessories: 601450
    - Mobile & Electronics: 801928
    - Health Products: 951432
    - Home & Living: 601755
    - Men's Clothing & Underwear: 605248
    - Perfume: 601583

    ### Return Description:
    - `list`: Product list
      - `comment`: Comment count
      - `cost`: Cost amount
      - `cover_url`: Cover image URL (may be null)
      - `cpa`: Cost per acquisition
      - `ctr`: Click-through rate (percentage)
      - `cvr`: Conversion rate (percentage)
      - `ecom_type`: E-commerce type
      - `first_ecom_category`: First-level e-commerce category
        - `id`: Category ID
        - `label`: Category label
        - `value`: Category name
      - `impression`: Impression count
      - `like`: Like count
      - `play_six_rate`: 6-second play rate (percentage)
      - `post`: Post volume
      - `post_change`: Post volume change rate (percentage)
      - `second_ecom_category`: Second-level e-commerce category
        - `id`: Category ID
        - `label`: Category label
        - `parent_id`: Parent category ID
        - `value`: Category name
      - `share`: Share count
      - `third_ecom_category`: Third-level e-commerce category
        - `id`: Category ID
        - `label`: Category label
        - `parent_id`: Parent category ID
        - `value`: Category name
      - `url_title`: URL title
    - `pagination`: Pagination info
      - `page`: Current page
      - `size`: Items per page
      - `total`: Total count
      - `has_more`: Whether there are more items

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_top_products\",
      \"params\": {
        \"last\": \"7\",
        \"page\": \"1\",
        \"limit\": \"20\",
        \"country_code\": \"US\",
        \"first_ecom_category_id\": \"\",
        \"ecom_type\": \"l3\",
        \"period_type\": \"last\",
        \"order_by\": \"post\",
        \"order_type\": \"desc\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"list\": [
            {
              \"comment\": 3449,
              \"cost\": 477000,
              \"cover_url\": null,
              \"cpa\": 9.21,
              \"ctr\": 1.29,
              \"cvr\": 12.94,
              \"ecom_type\": \"l3\",
              \"first_ecom_category\": {
                \"id\": \"601450\",
                \"label\": \"category_601450\",
                \"value\": \"Beauty & Personal Care\"
              },
              \"impression\": 65000000,
              \"like\": 166618,
              \"play_six_rate\": 7.62,
              \"post\": 10600,
              \"post_change\": -10.16,
              \"second_ecom_category\": {
                \"id\": \"848648\",
                \"label\": \"category_848648\",
                \"parent_id\": \"601450\",
                \"value\": \"Makeup & Perfume\"
              },
              \"share\": 2359,
              \"third_ecom_category\": {
                \"id\": \"601583\",
                \"label\": \"category_601583\",
                \"parent_id\": \"848648\",
                \"value\": \"Perfume\"
              },
              \"url_title\": \"Perfume\"
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 156,
            \"has_more\": true
          }
        }
      }
    }
    ```

    Args:
        last (Union[Unset, int]): 最近天数/Last days Default: 7.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.
        first_ecom_category_id (Union[Unset, str]): 电商类目ID，多个用逗号分隔/E-commerce category IDs, comma
            separated Default: ''.
        ecom_type (Union[Unset, str]): 电商类型/E-commerce type (l3) Default: 'l3'.
        period_type (Union[Unset, str]): 时间类型/Period type (last) Default: 'last'.
        order_by (Union[Unset, str]): 排序字段/Sort field (post, ctr, cvr) Default: 'post'.
        order_type (Union[Unset, str]): 排序方式/Sort order (desc, asc) Default: 'desc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            last=last,
            page=page,
            limit=limit,
            country_code=country_code,
            first_ecom_category_id=first_ecom_category_id,
            ecom_type=ecom_type,
            period_type=period_type,
            order_by=order_by,
            order_type=order_type,
        )
    ).parsed
