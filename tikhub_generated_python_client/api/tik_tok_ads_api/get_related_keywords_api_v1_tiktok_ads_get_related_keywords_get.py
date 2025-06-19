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
    keyword: Union[Unset, str] = "free shipping",
    period: Union[Unset, int] = 7,
    country_code: Union[Unset, str] = "US",
    rank_type: Union[Unset, str] = "popular",
    content_type: Union[Unset, str] = "keyword",
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 50,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["period"] = period

    params["country_code"] = country_code

    params["rank_type"] = rank_type

    params["content_type"] = content_type

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/get_related_keywords",
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
    keyword: Union[Unset, str] = "free shipping",
    period: Union[Unset, int] = 7,
    country_code: Union[Unset, str] = "US",
    rank_type: Union[Unset, str] = "popular",
    content_type: Union[Unset, str] = "keyword",
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 50,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取相关关键词/Get related keywords

     # [中文]
    ### 用途:
    - 获取与指定关键词相关的其他关键词或标签
    - 发现关键词的相关搜索词，扩展广告投放词库
    - 分析突破性关键词，抓住新兴趋势

    ### 参数:
    - keyword: 主关键词，必填参数
    - period: 时间范围（天），如7、30天
    - country_code: 国家代码，如US、UK、JP等
    - rank_type: 排序类型，\"popular\"=热门，\"breakout\"=突破性
    - content_type: 内容类型，\"keyword\"=关键词，\"hashtag\"=标签

    ### 返回内容说明:
    - `list`: 相关关键词列表
      - `keyword`: 相关关键词文本
      - `relevance_score`: 相关性评分
      - `search_volume`: 搜索量级别
      - `growth_rate`: 增长率（突破性关键词）
      - `post_count`: 使用该词的广告数量

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_related_keywords\",
      \"params\": {
        \"keyword\": \"free shipping\",
        \"period\": 7,
        \"rank_type\": \"popular\"
      },
      \"data\": {
        \"list\": [
          {
            \"keyword\": \"fast delivery\",
            \"relevance_score\": 95,
            \"search_volume\": \"high\",
            \"post_count\": 8934
          },
          {
            \"keyword\": \"discount code\",
            \"relevance_score\": 88,
            \"search_volume\": \"medium\",
            \"post_count\": 5621
          }
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get other keywords or hashtags related to a specified keyword
    - Discover related search terms to expand ad keyword library
    - Analyze breakout keywords to capture emerging trends

    ### Parameters:
    - keyword: Main keyword, required parameter
    - period: Time period in days, e.g., 7, 30 days
    - country_code: Country code, e.g., US, UK, JP
    - rank_type: Ranking type, \"popular\"=Popular, \"breakout\"=Breakout
    - content_type: Content type, \"keyword\"=Keywords, \"hashtag\"=Hashtags

    ### Return Description:
    - `list`: Related keywords list
      - `keyword`: Related keyword text
      - `relevance_score`: Relevance score
      - `search_volume`: Search volume level
      - `growth_rate`: Growth rate (for breakout keywords)
      - `post_count`: Number of ads using this term

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_related_keywords\",
      \"params\": {
        \"keyword\": \"free shipping\",
        \"period\": 7,
        \"rank_type\": \"popular\"
      },
      \"data\": {
        \"list\": [
          {
            \"keyword\": \"fast delivery\",
            \"relevance_score\": 95,
            \"search_volume\": \"high\",
            \"post_count\": 8934
          },
          {
            \"keyword\": \"discount code\",
            \"relevance_score\": 88,
            \"search_volume\": \"medium\",
            \"post_count\": 5621
          }
        ]
      }
    }
    ```

    Args:
        keyword (Union[Unset, str]): 目标关键词/Target keyword Default: 'free shipping'.
        period (Union[Unset, int]): 时间段（天）/Time period (days, 7/30/120) Default: 7.
        country_code (Union[Unset, str]): 国家/地区代码/Country code Default: 'US'.
        rank_type (Union[Unset, str]): 排名类型/Rank type (popular: 热门, breakout: 突破性) Default:
            'popular'.
        content_type (Union[Unset, str]): 内容类型/Content type (keyword, hashtag) Default: 'keyword'.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        period=period,
        country_code=country_code,
        rank_type=rank_type,
        content_type=content_type,
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
    keyword: Union[Unset, str] = "free shipping",
    period: Union[Unset, int] = 7,
    country_code: Union[Unset, str] = "US",
    rank_type: Union[Unset, str] = "popular",
    content_type: Union[Unset, str] = "keyword",
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 50,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取相关关键词/Get related keywords

     # [中文]
    ### 用途:
    - 获取与指定关键词相关的其他关键词或标签
    - 发现关键词的相关搜索词，扩展广告投放词库
    - 分析突破性关键词，抓住新兴趋势

    ### 参数:
    - keyword: 主关键词，必填参数
    - period: 时间范围（天），如7、30天
    - country_code: 国家代码，如US、UK、JP等
    - rank_type: 排序类型，\"popular\"=热门，\"breakout\"=突破性
    - content_type: 内容类型，\"keyword\"=关键词，\"hashtag\"=标签

    ### 返回内容说明:
    - `list`: 相关关键词列表
      - `keyword`: 相关关键词文本
      - `relevance_score`: 相关性评分
      - `search_volume`: 搜索量级别
      - `growth_rate`: 增长率（突破性关键词）
      - `post_count`: 使用该词的广告数量

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_related_keywords\",
      \"params\": {
        \"keyword\": \"free shipping\",
        \"period\": 7,
        \"rank_type\": \"popular\"
      },
      \"data\": {
        \"list\": [
          {
            \"keyword\": \"fast delivery\",
            \"relevance_score\": 95,
            \"search_volume\": \"high\",
            \"post_count\": 8934
          },
          {
            \"keyword\": \"discount code\",
            \"relevance_score\": 88,
            \"search_volume\": \"medium\",
            \"post_count\": 5621
          }
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get other keywords or hashtags related to a specified keyword
    - Discover related search terms to expand ad keyword library
    - Analyze breakout keywords to capture emerging trends

    ### Parameters:
    - keyword: Main keyword, required parameter
    - period: Time period in days, e.g., 7, 30 days
    - country_code: Country code, e.g., US, UK, JP
    - rank_type: Ranking type, \"popular\"=Popular, \"breakout\"=Breakout
    - content_type: Content type, \"keyword\"=Keywords, \"hashtag\"=Hashtags

    ### Return Description:
    - `list`: Related keywords list
      - `keyword`: Related keyword text
      - `relevance_score`: Relevance score
      - `search_volume`: Search volume level
      - `growth_rate`: Growth rate (for breakout keywords)
      - `post_count`: Number of ads using this term

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_related_keywords\",
      \"params\": {
        \"keyword\": \"free shipping\",
        \"period\": 7,
        \"rank_type\": \"popular\"
      },
      \"data\": {
        \"list\": [
          {
            \"keyword\": \"fast delivery\",
            \"relevance_score\": 95,
            \"search_volume\": \"high\",
            \"post_count\": 8934
          },
          {
            \"keyword\": \"discount code\",
            \"relevance_score\": 88,
            \"search_volume\": \"medium\",
            \"post_count\": 5621
          }
        ]
      }
    }
    ```

    Args:
        keyword (Union[Unset, str]): 目标关键词/Target keyword Default: 'free shipping'.
        period (Union[Unset, int]): 时间段（天）/Time period (days, 7/30/120) Default: 7.
        country_code (Union[Unset, str]): 国家/地区代码/Country code Default: 'US'.
        rank_type (Union[Unset, str]): 排名类型/Rank type (popular: 热门, breakout: 突破性) Default:
            'popular'.
        content_type (Union[Unset, str]): 内容类型/Content type (keyword, hashtag) Default: 'keyword'.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        keyword=keyword,
        period=period,
        country_code=country_code,
        rank_type=rank_type,
        content_type=content_type,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: Union[Unset, str] = "free shipping",
    period: Union[Unset, int] = 7,
    country_code: Union[Unset, str] = "US",
    rank_type: Union[Unset, str] = "popular",
    content_type: Union[Unset, str] = "keyword",
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 50,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取相关关键词/Get related keywords

     # [中文]
    ### 用途:
    - 获取与指定关键词相关的其他关键词或标签
    - 发现关键词的相关搜索词，扩展广告投放词库
    - 分析突破性关键词，抓住新兴趋势

    ### 参数:
    - keyword: 主关键词，必填参数
    - period: 时间范围（天），如7、30天
    - country_code: 国家代码，如US、UK、JP等
    - rank_type: 排序类型，\"popular\"=热门，\"breakout\"=突破性
    - content_type: 内容类型，\"keyword\"=关键词，\"hashtag\"=标签

    ### 返回内容说明:
    - `list`: 相关关键词列表
      - `keyword`: 相关关键词文本
      - `relevance_score`: 相关性评分
      - `search_volume`: 搜索量级别
      - `growth_rate`: 增长率（突破性关键词）
      - `post_count`: 使用该词的广告数量

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_related_keywords\",
      \"params\": {
        \"keyword\": \"free shipping\",
        \"period\": 7,
        \"rank_type\": \"popular\"
      },
      \"data\": {
        \"list\": [
          {
            \"keyword\": \"fast delivery\",
            \"relevance_score\": 95,
            \"search_volume\": \"high\",
            \"post_count\": 8934
          },
          {
            \"keyword\": \"discount code\",
            \"relevance_score\": 88,
            \"search_volume\": \"medium\",
            \"post_count\": 5621
          }
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get other keywords or hashtags related to a specified keyword
    - Discover related search terms to expand ad keyword library
    - Analyze breakout keywords to capture emerging trends

    ### Parameters:
    - keyword: Main keyword, required parameter
    - period: Time period in days, e.g., 7, 30 days
    - country_code: Country code, e.g., US, UK, JP
    - rank_type: Ranking type, \"popular\"=Popular, \"breakout\"=Breakout
    - content_type: Content type, \"keyword\"=Keywords, \"hashtag\"=Hashtags

    ### Return Description:
    - `list`: Related keywords list
      - `keyword`: Related keyword text
      - `relevance_score`: Relevance score
      - `search_volume`: Search volume level
      - `growth_rate`: Growth rate (for breakout keywords)
      - `post_count`: Number of ads using this term

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_related_keywords\",
      \"params\": {
        \"keyword\": \"free shipping\",
        \"period\": 7,
        \"rank_type\": \"popular\"
      },
      \"data\": {
        \"list\": [
          {
            \"keyword\": \"fast delivery\",
            \"relevance_score\": 95,
            \"search_volume\": \"high\",
            \"post_count\": 8934
          },
          {
            \"keyword\": \"discount code\",
            \"relevance_score\": 88,
            \"search_volume\": \"medium\",
            \"post_count\": 5621
          }
        ]
      }
    }
    ```

    Args:
        keyword (Union[Unset, str]): 目标关键词/Target keyword Default: 'free shipping'.
        period (Union[Unset, int]): 时间段（天）/Time period (days, 7/30/120) Default: 7.
        country_code (Union[Unset, str]): 国家/地区代码/Country code Default: 'US'.
        rank_type (Union[Unset, str]): 排名类型/Rank type (popular: 热门, breakout: 突破性) Default:
            'popular'.
        content_type (Union[Unset, str]): 内容类型/Content type (keyword, hashtag) Default: 'keyword'.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        period=period,
        country_code=country_code,
        rank_type=rank_type,
        content_type=content_type,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: Union[Unset, str] = "free shipping",
    period: Union[Unset, int] = 7,
    country_code: Union[Unset, str] = "US",
    rank_type: Union[Unset, str] = "popular",
    content_type: Union[Unset, str] = "keyword",
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 50,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取相关关键词/Get related keywords

     # [中文]
    ### 用途:
    - 获取与指定关键词相关的其他关键词或标签
    - 发现关键词的相关搜索词，扩展广告投放词库
    - 分析突破性关键词，抓住新兴趋势

    ### 参数:
    - keyword: 主关键词，必填参数
    - period: 时间范围（天），如7、30天
    - country_code: 国家代码，如US、UK、JP等
    - rank_type: 排序类型，\"popular\"=热门，\"breakout\"=突破性
    - content_type: 内容类型，\"keyword\"=关键词，\"hashtag\"=标签

    ### 返回内容说明:
    - `list`: 相关关键词列表
      - `keyword`: 相关关键词文本
      - `relevance_score`: 相关性评分
      - `search_volume`: 搜索量级别
      - `growth_rate`: 增长率（突破性关键词）
      - `post_count`: 使用该词的广告数量

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_related_keywords\",
      \"params\": {
        \"keyword\": \"free shipping\",
        \"period\": 7,
        \"rank_type\": \"popular\"
      },
      \"data\": {
        \"list\": [
          {
            \"keyword\": \"fast delivery\",
            \"relevance_score\": 95,
            \"search_volume\": \"high\",
            \"post_count\": 8934
          },
          {
            \"keyword\": \"discount code\",
            \"relevance_score\": 88,
            \"search_volume\": \"medium\",
            \"post_count\": 5621
          }
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get other keywords or hashtags related to a specified keyword
    - Discover related search terms to expand ad keyword library
    - Analyze breakout keywords to capture emerging trends

    ### Parameters:
    - keyword: Main keyword, required parameter
    - period: Time period in days, e.g., 7, 30 days
    - country_code: Country code, e.g., US, UK, JP
    - rank_type: Ranking type, \"popular\"=Popular, \"breakout\"=Breakout
    - content_type: Content type, \"keyword\"=Keywords, \"hashtag\"=Hashtags

    ### Return Description:
    - `list`: Related keywords list
      - `keyword`: Related keyword text
      - `relevance_score`: Relevance score
      - `search_volume`: Search volume level
      - `growth_rate`: Growth rate (for breakout keywords)
      - `post_count`: Number of ads using this term

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_related_keywords\",
      \"params\": {
        \"keyword\": \"free shipping\",
        \"period\": 7,
        \"rank_type\": \"popular\"
      },
      \"data\": {
        \"list\": [
          {
            \"keyword\": \"fast delivery\",
            \"relevance_score\": 95,
            \"search_volume\": \"high\",
            \"post_count\": 8934
          },
          {
            \"keyword\": \"discount code\",
            \"relevance_score\": 88,
            \"search_volume\": \"medium\",
            \"post_count\": 5621
          }
        ]
      }
    }
    ```

    Args:
        keyword (Union[Unset, str]): 目标关键词/Target keyword Default: 'free shipping'.
        period (Union[Unset, int]): 时间段（天）/Time period (days, 7/30/120) Default: 7.
        country_code (Union[Unset, str]): 国家/地区代码/Country code Default: 'US'.
        rank_type (Union[Unset, str]): 排名类型/Rank type (popular: 热门, breakout: 突破性) Default:
            'popular'.
        content_type (Union[Unset, str]): 内容类型/Content type (keyword, hashtag) Default: 'keyword'.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            keyword=keyword,
            period=period,
            country_code=country_code,
            rank_type=rank_type,
            content_type=content_type,
            page=page,
            limit=limit,
        )
    ).parsed
