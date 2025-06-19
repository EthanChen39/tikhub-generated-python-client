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
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    period: Union[Unset, int] = 7,
    country_code: Union[Unset, str] = "US",
    order_by: Union[Unset, str] = "post",
    order_type: Union[Unset, str] = "desc",
    industry: Union[Unset, str] = UNSET,
    objective: Union[Unset, str] = UNSET,
    keyword_type: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params["period"] = period

    params["country_code"] = country_code

    params["order_by"] = order_by

    params["order_type"] = order_type

    params["industry"] = industry

    params["objective"] = objective

    params["keyword_type"] = keyword_type

    params["keyword"] = keyword

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/get_keyword_insights",
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
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    period: Union[Unset, int] = 7,
    country_code: Union[Unset, str] = "US",
    order_by: Union[Unset, str] = "post",
    order_type: Union[Unset, str] = "desc",
    industry: Union[Unset, str] = UNSET,
    objective: Union[Unset, str] = UNSET,
    keyword_type: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取关键词洞察数据/Get keyword insights data

     # [中文]
    ### 用途:
    - 获取TikTok广告关键词洞察数据，了解热门关键词的表现指标
    - 分析不同关键词的点击率、发布量、增长趋势等核心数据
    - 帮助广告主优化关键词策略，提升广告投放效果

    ### 参数:
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - period: 时间范围（天），如7、30、120天
    - country_code: 国家代码，如US、UK、JP等
    - order_by: 排序字段，可选：post（发布量）、ctr（点击率）、click_rate（点击率）、trend（趋势）
    - order_type: 排序方式，desc（降序）或asc（升序）
    - industry: 行业ID，多个用逗号分隔
    - objective: 广告目标
    - keyword_type: 关键词类型

    ### 返回内容说明:
    - `keyword_list`: 关键词列表
      - `comment`: 评论数
      - `cost`: 花费金额
      - `cpa`: 每次转化成本
      - `ctr`: 点击率（百分比）
      - `cvr`: 转化率（百分比）
      - `impression`: 展示量
      - `keyword`: 关键词文本
      - `like`: 点赞数
      - `play_six_rate`: 6秒播放率（百分比）
      - `post`: 发布量
      - `post_change`: 发布量变化率（百分比）
      - `share`: 分享数
      - `video_list`: 视频ID列表
    - `pagination`: 分页信息
      - `page`: 当前页
      - `size`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_keyword_insights\",
      \"params\": {
        \"page\": \"1\",
        \"limit\": \"20\",
        \"period\": \"7\",
        \"country_code\": \"US\",
        \"order_by\": \"post\",
        \"order_type\": \"desc\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"keyword_list\": [
            {
              \"comment\": 4785,
              \"cost\": 756000,
              \"cpa\": 20.2,
              \"ctr\": 0.53,
              \"cvr\": 9.75,
              \"impression\": 164000000,
              \"keyword\": \"summer\",
              \"like\": 475734,
              \"play_six_rate\": 6.43,
              \"post\": 14200,
              \"post_change\": 111.21,
              \"share\": 5754,
              \"video_list\": [
                \"7504060523021896977\",
                \"7512164952346529031\",
                \"7511370341621435679\",
                \"7511483560939785514\",
                \"7506971390613015854\"
              ]
            },
            {
              \"comment\": 2151,
              \"cost\": 264000,
              \"cpa\": 17.8,
              \"ctr\": 1.38,
              \"cvr\": 6.15,
              \"impression\": 38100000,
              \"keyword\": \"free shipping\",
              \"like\": 84131,
              \"play_six_rate\": 8.64,
              \"post\": 7810,
              \"post_change\": 91.91,
              \"share\": 3707,
              \"video_list\": [
                \"7471433861654727943\",
                \"7515178617568070930\",
                \"7502578466194312456\",
                \"7513186274711244054\",
                \"7514776490123201810\"
              ]
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 484,
            \"has_more\": true
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get TikTok ad keyword insights data to understand performance metrics of popular keywords
    - Analyze CTR, post volume, growth trends and other core data for different keywords
    - Help advertisers optimize keyword strategies and improve ad delivery effectiveness

    ### Parameters:
    - page: Page number, default 1
    - limit: Items per page, default 20
    - period: Time period in days, e.g., 7, 30, 120 days
    - country_code: Country code, e.g., US, UK, JP
    - order_by: Sort field, options: post (post volume), ctr (click-through rate), click_rate, trend
    - order_type: Sort order, desc (descending) or asc (ascending)
    - industry: Industry IDs, multiple separated by commas
    - objective: Ad objectives
    - keyword_type: Keyword type

    ### Return Description:
    - `keyword_list`: List of keywords
      - `comment`: Comment count
      - `cost`: Cost amount
      - `cpa`: Cost per acquisition
      - `ctr`: Click-through rate (percentage)
      - `cvr`: Conversion rate (percentage)
      - `impression`: Impression count
      - `keyword`: Keyword text
      - `like`: Like count
      - `play_six_rate`: 6-second play rate (percentage)
      - `post`: Post volume
      - `post_change`: Post volume change rate (percentage)
      - `share`: Share count
      - `video_list`: List of video IDs
    - `pagination`: Pagination info
      - `page`: Current page
      - `size`: Items per page
      - `total`: Total count
      - `has_more`: Whether there are more items

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_keyword_insights\",
      \"params\": {
        \"page\": \"1\",
        \"limit\": \"20\",
        \"period\": \"7\",
        \"country_code\": \"US\",
        \"order_by\": \"post\",
        \"order_type\": \"desc\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"keyword_list\": [
            {
              \"comment\": 4785,
              \"cost\": 756000,
              \"cpa\": 20.2,
              \"ctr\": 0.53,
              \"cvr\": 9.75,
              \"impression\": 164000000,
              \"keyword\": \"summer\",
              \"like\": 475734,
              \"play_six_rate\": 6.43,
              \"post\": 14200,
              \"post_change\": 111.21,
              \"share\": 5754,
              \"video_list\": [
                \"7504060523021896977\",
                \"7512164952346529031\",
                \"7511370341621435679\",
                \"7511483560939785514\",
                \"7506971390613015854\"
              ]
            },
            {
              \"comment\": 2151,
              \"cost\": 264000,
              \"cpa\": 17.8,
              \"ctr\": 1.38,
              \"cvr\": 6.15,
              \"impression\": 38100000,
              \"keyword\": \"free shipping\",
              \"like\": 84131,
              \"play_six_rate\": 8.64,
              \"post\": 7810,
              \"post_change\": 91.91,
              \"share\": 3707,
              \"video_list\": [
                \"7471433861654727943\",
                \"7515178617568070930\",
                \"7502578466194312456\",
                \"7513186274711244054\",
                \"7514776490123201810\"
              ]
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 484,
            \"has_more\": true
          }
        }
      }
    }
    ```

    Args:
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        period (Union[Unset, int]): 时间段（天）/Time period (days, 7/30/120/180) Default: 7.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.
        order_by (Union[Unset, str]): 排序字段/Sort field (post, ctr, click_rate, etc.) Default:
            'post'.
        order_type (Union[Unset, str]): 排序方式/Sort order (desc, asc) Default: 'desc'.
        industry (Union[Unset, str]): 行业ID/Industry ID
        objective (Union[Unset, str]): 广告目标/Ad objective
        keyword_type (Union[Unset, str]): 关键词类型/Keyword type
        keyword (Union[Unset, str]): 关键词/Keyword

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        period=period,
        country_code=country_code,
        order_by=order_by,
        order_type=order_type,
        industry=industry,
        objective=objective,
        keyword_type=keyword_type,
        keyword=keyword,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    period: Union[Unset, int] = 7,
    country_code: Union[Unset, str] = "US",
    order_by: Union[Unset, str] = "post",
    order_type: Union[Unset, str] = "desc",
    industry: Union[Unset, str] = UNSET,
    objective: Union[Unset, str] = UNSET,
    keyword_type: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取关键词洞察数据/Get keyword insights data

     # [中文]
    ### 用途:
    - 获取TikTok广告关键词洞察数据，了解热门关键词的表现指标
    - 分析不同关键词的点击率、发布量、增长趋势等核心数据
    - 帮助广告主优化关键词策略，提升广告投放效果

    ### 参数:
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - period: 时间范围（天），如7、30、120天
    - country_code: 国家代码，如US、UK、JP等
    - order_by: 排序字段，可选：post（发布量）、ctr（点击率）、click_rate（点击率）、trend（趋势）
    - order_type: 排序方式，desc（降序）或asc（升序）
    - industry: 行业ID，多个用逗号分隔
    - objective: 广告目标
    - keyword_type: 关键词类型

    ### 返回内容说明:
    - `keyword_list`: 关键词列表
      - `comment`: 评论数
      - `cost`: 花费金额
      - `cpa`: 每次转化成本
      - `ctr`: 点击率（百分比）
      - `cvr`: 转化率（百分比）
      - `impression`: 展示量
      - `keyword`: 关键词文本
      - `like`: 点赞数
      - `play_six_rate`: 6秒播放率（百分比）
      - `post`: 发布量
      - `post_change`: 发布量变化率（百分比）
      - `share`: 分享数
      - `video_list`: 视频ID列表
    - `pagination`: 分页信息
      - `page`: 当前页
      - `size`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_keyword_insights\",
      \"params\": {
        \"page\": \"1\",
        \"limit\": \"20\",
        \"period\": \"7\",
        \"country_code\": \"US\",
        \"order_by\": \"post\",
        \"order_type\": \"desc\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"keyword_list\": [
            {
              \"comment\": 4785,
              \"cost\": 756000,
              \"cpa\": 20.2,
              \"ctr\": 0.53,
              \"cvr\": 9.75,
              \"impression\": 164000000,
              \"keyword\": \"summer\",
              \"like\": 475734,
              \"play_six_rate\": 6.43,
              \"post\": 14200,
              \"post_change\": 111.21,
              \"share\": 5754,
              \"video_list\": [
                \"7504060523021896977\",
                \"7512164952346529031\",
                \"7511370341621435679\",
                \"7511483560939785514\",
                \"7506971390613015854\"
              ]
            },
            {
              \"comment\": 2151,
              \"cost\": 264000,
              \"cpa\": 17.8,
              \"ctr\": 1.38,
              \"cvr\": 6.15,
              \"impression\": 38100000,
              \"keyword\": \"free shipping\",
              \"like\": 84131,
              \"play_six_rate\": 8.64,
              \"post\": 7810,
              \"post_change\": 91.91,
              \"share\": 3707,
              \"video_list\": [
                \"7471433861654727943\",
                \"7515178617568070930\",
                \"7502578466194312456\",
                \"7513186274711244054\",
                \"7514776490123201810\"
              ]
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 484,
            \"has_more\": true
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get TikTok ad keyword insights data to understand performance metrics of popular keywords
    - Analyze CTR, post volume, growth trends and other core data for different keywords
    - Help advertisers optimize keyword strategies and improve ad delivery effectiveness

    ### Parameters:
    - page: Page number, default 1
    - limit: Items per page, default 20
    - period: Time period in days, e.g., 7, 30, 120 days
    - country_code: Country code, e.g., US, UK, JP
    - order_by: Sort field, options: post (post volume), ctr (click-through rate), click_rate, trend
    - order_type: Sort order, desc (descending) or asc (ascending)
    - industry: Industry IDs, multiple separated by commas
    - objective: Ad objectives
    - keyword_type: Keyword type

    ### Return Description:
    - `keyword_list`: List of keywords
      - `comment`: Comment count
      - `cost`: Cost amount
      - `cpa`: Cost per acquisition
      - `ctr`: Click-through rate (percentage)
      - `cvr`: Conversion rate (percentage)
      - `impression`: Impression count
      - `keyword`: Keyword text
      - `like`: Like count
      - `play_six_rate`: 6-second play rate (percentage)
      - `post`: Post volume
      - `post_change`: Post volume change rate (percentage)
      - `share`: Share count
      - `video_list`: List of video IDs
    - `pagination`: Pagination info
      - `page`: Current page
      - `size`: Items per page
      - `total`: Total count
      - `has_more`: Whether there are more items

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_keyword_insights\",
      \"params\": {
        \"page\": \"1\",
        \"limit\": \"20\",
        \"period\": \"7\",
        \"country_code\": \"US\",
        \"order_by\": \"post\",
        \"order_type\": \"desc\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"keyword_list\": [
            {
              \"comment\": 4785,
              \"cost\": 756000,
              \"cpa\": 20.2,
              \"ctr\": 0.53,
              \"cvr\": 9.75,
              \"impression\": 164000000,
              \"keyword\": \"summer\",
              \"like\": 475734,
              \"play_six_rate\": 6.43,
              \"post\": 14200,
              \"post_change\": 111.21,
              \"share\": 5754,
              \"video_list\": [
                \"7504060523021896977\",
                \"7512164952346529031\",
                \"7511370341621435679\",
                \"7511483560939785514\",
                \"7506971390613015854\"
              ]
            },
            {
              \"comment\": 2151,
              \"cost\": 264000,
              \"cpa\": 17.8,
              \"ctr\": 1.38,
              \"cvr\": 6.15,
              \"impression\": 38100000,
              \"keyword\": \"free shipping\",
              \"like\": 84131,
              \"play_six_rate\": 8.64,
              \"post\": 7810,
              \"post_change\": 91.91,
              \"share\": 3707,
              \"video_list\": [
                \"7471433861654727943\",
                \"7515178617568070930\",
                \"7502578466194312456\",
                \"7513186274711244054\",
                \"7514776490123201810\"
              ]
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 484,
            \"has_more\": true
          }
        }
      }
    }
    ```

    Args:
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        period (Union[Unset, int]): 时间段（天）/Time period (days, 7/30/120/180) Default: 7.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.
        order_by (Union[Unset, str]): 排序字段/Sort field (post, ctr, click_rate, etc.) Default:
            'post'.
        order_type (Union[Unset, str]): 排序方式/Sort order (desc, asc) Default: 'desc'.
        industry (Union[Unset, str]): 行业ID/Industry ID
        objective (Union[Unset, str]): 广告目标/Ad objective
        keyword_type (Union[Unset, str]): 关键词类型/Keyword type
        keyword (Union[Unset, str]): 关键词/Keyword

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        page=page,
        limit=limit,
        period=period,
        country_code=country_code,
        order_by=order_by,
        order_type=order_type,
        industry=industry,
        objective=objective,
        keyword_type=keyword_type,
        keyword=keyword,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    period: Union[Unset, int] = 7,
    country_code: Union[Unset, str] = "US",
    order_by: Union[Unset, str] = "post",
    order_type: Union[Unset, str] = "desc",
    industry: Union[Unset, str] = UNSET,
    objective: Union[Unset, str] = UNSET,
    keyword_type: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取关键词洞察数据/Get keyword insights data

     # [中文]
    ### 用途:
    - 获取TikTok广告关键词洞察数据，了解热门关键词的表现指标
    - 分析不同关键词的点击率、发布量、增长趋势等核心数据
    - 帮助广告主优化关键词策略，提升广告投放效果

    ### 参数:
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - period: 时间范围（天），如7、30、120天
    - country_code: 国家代码，如US、UK、JP等
    - order_by: 排序字段，可选：post（发布量）、ctr（点击率）、click_rate（点击率）、trend（趋势）
    - order_type: 排序方式，desc（降序）或asc（升序）
    - industry: 行业ID，多个用逗号分隔
    - objective: 广告目标
    - keyword_type: 关键词类型

    ### 返回内容说明:
    - `keyword_list`: 关键词列表
      - `comment`: 评论数
      - `cost`: 花费金额
      - `cpa`: 每次转化成本
      - `ctr`: 点击率（百分比）
      - `cvr`: 转化率（百分比）
      - `impression`: 展示量
      - `keyword`: 关键词文本
      - `like`: 点赞数
      - `play_six_rate`: 6秒播放率（百分比）
      - `post`: 发布量
      - `post_change`: 发布量变化率（百分比）
      - `share`: 分享数
      - `video_list`: 视频ID列表
    - `pagination`: 分页信息
      - `page`: 当前页
      - `size`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_keyword_insights\",
      \"params\": {
        \"page\": \"1\",
        \"limit\": \"20\",
        \"period\": \"7\",
        \"country_code\": \"US\",
        \"order_by\": \"post\",
        \"order_type\": \"desc\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"keyword_list\": [
            {
              \"comment\": 4785,
              \"cost\": 756000,
              \"cpa\": 20.2,
              \"ctr\": 0.53,
              \"cvr\": 9.75,
              \"impression\": 164000000,
              \"keyword\": \"summer\",
              \"like\": 475734,
              \"play_six_rate\": 6.43,
              \"post\": 14200,
              \"post_change\": 111.21,
              \"share\": 5754,
              \"video_list\": [
                \"7504060523021896977\",
                \"7512164952346529031\",
                \"7511370341621435679\",
                \"7511483560939785514\",
                \"7506971390613015854\"
              ]
            },
            {
              \"comment\": 2151,
              \"cost\": 264000,
              \"cpa\": 17.8,
              \"ctr\": 1.38,
              \"cvr\": 6.15,
              \"impression\": 38100000,
              \"keyword\": \"free shipping\",
              \"like\": 84131,
              \"play_six_rate\": 8.64,
              \"post\": 7810,
              \"post_change\": 91.91,
              \"share\": 3707,
              \"video_list\": [
                \"7471433861654727943\",
                \"7515178617568070930\",
                \"7502578466194312456\",
                \"7513186274711244054\",
                \"7514776490123201810\"
              ]
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 484,
            \"has_more\": true
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get TikTok ad keyword insights data to understand performance metrics of popular keywords
    - Analyze CTR, post volume, growth trends and other core data for different keywords
    - Help advertisers optimize keyword strategies and improve ad delivery effectiveness

    ### Parameters:
    - page: Page number, default 1
    - limit: Items per page, default 20
    - period: Time period in days, e.g., 7, 30, 120 days
    - country_code: Country code, e.g., US, UK, JP
    - order_by: Sort field, options: post (post volume), ctr (click-through rate), click_rate, trend
    - order_type: Sort order, desc (descending) or asc (ascending)
    - industry: Industry IDs, multiple separated by commas
    - objective: Ad objectives
    - keyword_type: Keyword type

    ### Return Description:
    - `keyword_list`: List of keywords
      - `comment`: Comment count
      - `cost`: Cost amount
      - `cpa`: Cost per acquisition
      - `ctr`: Click-through rate (percentage)
      - `cvr`: Conversion rate (percentage)
      - `impression`: Impression count
      - `keyword`: Keyword text
      - `like`: Like count
      - `play_six_rate`: 6-second play rate (percentage)
      - `post`: Post volume
      - `post_change`: Post volume change rate (percentage)
      - `share`: Share count
      - `video_list`: List of video IDs
    - `pagination`: Pagination info
      - `page`: Current page
      - `size`: Items per page
      - `total`: Total count
      - `has_more`: Whether there are more items

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_keyword_insights\",
      \"params\": {
        \"page\": \"1\",
        \"limit\": \"20\",
        \"period\": \"7\",
        \"country_code\": \"US\",
        \"order_by\": \"post\",
        \"order_type\": \"desc\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"keyword_list\": [
            {
              \"comment\": 4785,
              \"cost\": 756000,
              \"cpa\": 20.2,
              \"ctr\": 0.53,
              \"cvr\": 9.75,
              \"impression\": 164000000,
              \"keyword\": \"summer\",
              \"like\": 475734,
              \"play_six_rate\": 6.43,
              \"post\": 14200,
              \"post_change\": 111.21,
              \"share\": 5754,
              \"video_list\": [
                \"7504060523021896977\",
                \"7512164952346529031\",
                \"7511370341621435679\",
                \"7511483560939785514\",
                \"7506971390613015854\"
              ]
            },
            {
              \"comment\": 2151,
              \"cost\": 264000,
              \"cpa\": 17.8,
              \"ctr\": 1.38,
              \"cvr\": 6.15,
              \"impression\": 38100000,
              \"keyword\": \"free shipping\",
              \"like\": 84131,
              \"play_six_rate\": 8.64,
              \"post\": 7810,
              \"post_change\": 91.91,
              \"share\": 3707,
              \"video_list\": [
                \"7471433861654727943\",
                \"7515178617568070930\",
                \"7502578466194312456\",
                \"7513186274711244054\",
                \"7514776490123201810\"
              ]
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 484,
            \"has_more\": true
          }
        }
      }
    }
    ```

    Args:
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        period (Union[Unset, int]): 时间段（天）/Time period (days, 7/30/120/180) Default: 7.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.
        order_by (Union[Unset, str]): 排序字段/Sort field (post, ctr, click_rate, etc.) Default:
            'post'.
        order_type (Union[Unset, str]): 排序方式/Sort order (desc, asc) Default: 'desc'.
        industry (Union[Unset, str]): 行业ID/Industry ID
        objective (Union[Unset, str]): 广告目标/Ad objective
        keyword_type (Union[Unset, str]): 关键词类型/Keyword type
        keyword (Union[Unset, str]): 关键词/Keyword

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        period=period,
        country_code=country_code,
        order_by=order_by,
        order_type=order_type,
        industry=industry,
        objective=objective,
        keyword_type=keyword_type,
        keyword=keyword,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    period: Union[Unset, int] = 7,
    country_code: Union[Unset, str] = "US",
    order_by: Union[Unset, str] = "post",
    order_type: Union[Unset, str] = "desc",
    industry: Union[Unset, str] = UNSET,
    objective: Union[Unset, str] = UNSET,
    keyword_type: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取关键词洞察数据/Get keyword insights data

     # [中文]
    ### 用途:
    - 获取TikTok广告关键词洞察数据，了解热门关键词的表现指标
    - 分析不同关键词的点击率、发布量、增长趋势等核心数据
    - 帮助广告主优化关键词策略，提升广告投放效果

    ### 参数:
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - period: 时间范围（天），如7、30、120天
    - country_code: 国家代码，如US、UK、JP等
    - order_by: 排序字段，可选：post（发布量）、ctr（点击率）、click_rate（点击率）、trend（趋势）
    - order_type: 排序方式，desc（降序）或asc（升序）
    - industry: 行业ID，多个用逗号分隔
    - objective: 广告目标
    - keyword_type: 关键词类型

    ### 返回内容说明:
    - `keyword_list`: 关键词列表
      - `comment`: 评论数
      - `cost`: 花费金额
      - `cpa`: 每次转化成本
      - `ctr`: 点击率（百分比）
      - `cvr`: 转化率（百分比）
      - `impression`: 展示量
      - `keyword`: 关键词文本
      - `like`: 点赞数
      - `play_six_rate`: 6秒播放率（百分比）
      - `post`: 发布量
      - `post_change`: 发布量变化率（百分比）
      - `share`: 分享数
      - `video_list`: 视频ID列表
    - `pagination`: 分页信息
      - `page`: 当前页
      - `size`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_keyword_insights\",
      \"params\": {
        \"page\": \"1\",
        \"limit\": \"20\",
        \"period\": \"7\",
        \"country_code\": \"US\",
        \"order_by\": \"post\",
        \"order_type\": \"desc\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"keyword_list\": [
            {
              \"comment\": 4785,
              \"cost\": 756000,
              \"cpa\": 20.2,
              \"ctr\": 0.53,
              \"cvr\": 9.75,
              \"impression\": 164000000,
              \"keyword\": \"summer\",
              \"like\": 475734,
              \"play_six_rate\": 6.43,
              \"post\": 14200,
              \"post_change\": 111.21,
              \"share\": 5754,
              \"video_list\": [
                \"7504060523021896977\",
                \"7512164952346529031\",
                \"7511370341621435679\",
                \"7511483560939785514\",
                \"7506971390613015854\"
              ]
            },
            {
              \"comment\": 2151,
              \"cost\": 264000,
              \"cpa\": 17.8,
              \"ctr\": 1.38,
              \"cvr\": 6.15,
              \"impression\": 38100000,
              \"keyword\": \"free shipping\",
              \"like\": 84131,
              \"play_six_rate\": 8.64,
              \"post\": 7810,
              \"post_change\": 91.91,
              \"share\": 3707,
              \"video_list\": [
                \"7471433861654727943\",
                \"7515178617568070930\",
                \"7502578466194312456\",
                \"7513186274711244054\",
                \"7514776490123201810\"
              ]
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 484,
            \"has_more\": true
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get TikTok ad keyword insights data to understand performance metrics of popular keywords
    - Analyze CTR, post volume, growth trends and other core data for different keywords
    - Help advertisers optimize keyword strategies and improve ad delivery effectiveness

    ### Parameters:
    - page: Page number, default 1
    - limit: Items per page, default 20
    - period: Time period in days, e.g., 7, 30, 120 days
    - country_code: Country code, e.g., US, UK, JP
    - order_by: Sort field, options: post (post volume), ctr (click-through rate), click_rate, trend
    - order_type: Sort order, desc (descending) or asc (ascending)
    - industry: Industry IDs, multiple separated by commas
    - objective: Ad objectives
    - keyword_type: Keyword type

    ### Return Description:
    - `keyword_list`: List of keywords
      - `comment`: Comment count
      - `cost`: Cost amount
      - `cpa`: Cost per acquisition
      - `ctr`: Click-through rate (percentage)
      - `cvr`: Conversion rate (percentage)
      - `impression`: Impression count
      - `keyword`: Keyword text
      - `like`: Like count
      - `play_six_rate`: 6-second play rate (percentage)
      - `post`: Post volume
      - `post_change`: Post volume change rate (percentage)
      - `share`: Share count
      - `video_list`: List of video IDs
    - `pagination`: Pagination info
      - `page`: Current page
      - `size`: Items per page
      - `total`: Total count
      - `has_more`: Whether there are more items

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_keyword_insights\",
      \"params\": {
        \"page\": \"1\",
        \"limit\": \"20\",
        \"period\": \"7\",
        \"country_code\": \"US\",
        \"order_by\": \"post\",
        \"order_type\": \"desc\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"keyword_list\": [
            {
              \"comment\": 4785,
              \"cost\": 756000,
              \"cpa\": 20.2,
              \"ctr\": 0.53,
              \"cvr\": 9.75,
              \"impression\": 164000000,
              \"keyword\": \"summer\",
              \"like\": 475734,
              \"play_six_rate\": 6.43,
              \"post\": 14200,
              \"post_change\": 111.21,
              \"share\": 5754,
              \"video_list\": [
                \"7504060523021896977\",
                \"7512164952346529031\",
                \"7511370341621435679\",
                \"7511483560939785514\",
                \"7506971390613015854\"
              ]
            },
            {
              \"comment\": 2151,
              \"cost\": 264000,
              \"cpa\": 17.8,
              \"ctr\": 1.38,
              \"cvr\": 6.15,
              \"impression\": 38100000,
              \"keyword\": \"free shipping\",
              \"like\": 84131,
              \"play_six_rate\": 8.64,
              \"post\": 7810,
              \"post_change\": 91.91,
              \"share\": 3707,
              \"video_list\": [
                \"7471433861654727943\",
                \"7515178617568070930\",
                \"7502578466194312456\",
                \"7513186274711244054\",
                \"7514776490123201810\"
              ]
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 484,
            \"has_more\": true
          }
        }
      }
    }
    ```

    Args:
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        period (Union[Unset, int]): 时间段（天）/Time period (days, 7/30/120/180) Default: 7.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.
        order_by (Union[Unset, str]): 排序字段/Sort field (post, ctr, click_rate, etc.) Default:
            'post'.
        order_type (Union[Unset, str]): 排序方式/Sort order (desc, asc) Default: 'desc'.
        industry (Union[Unset, str]): 行业ID/Industry ID
        objective (Union[Unset, str]): 广告目标/Ad objective
        keyword_type (Union[Unset, str]): 关键词类型/Keyword type
        keyword (Union[Unset, str]): 关键词/Keyword

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            limit=limit,
            period=period,
            country_code=country_code,
            order_by=order_by,
            order_type=order_type,
            industry=industry,
            objective=objective,
            keyword_type=keyword_type,
            keyword=keyword,
        )
    ).parsed
