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
    keyword: Union[Unset, str] = "cat toy",
    period: Union[Unset, int] = 120,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 6,
    country_code: Union[Unset, str] = "US",
    industry: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["period"] = period

    params["page"] = page

    params["limit"] = limit

    params["country_code"] = country_code

    params["industry"] = industry

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/get_keyword_list",
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
    keyword: Union[Unset, str] = "cat toy",
    period: Union[Unset, int] = 120,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 6,
    country_code: Union[Unset, str] = "US",
    industry: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取关键词列表/Get keyword list

     # [中文]
    ### 用途:
    - 获取特定关键词的广告投放数据，了解关键词在TikTok广告中的使用情况
    - 分析关键词的发布量趋势、相关视频等信息
    - 帮助广告主发现有效的广告关键词

    ### 参数:
    - keyword: 搜索关键词，必填参数
    - period: 时间范围（天），如7、30、120天
    - page: 页码，默认1
    - limit: 每页数量，默认6
    - country_code: 国家代码，如US、UK、JP等
    - industry: 行业ID列表，多个ID用逗号分隔

    ### 返回内容说明:
    - `keyword_info_list`: 关键词信息列表
      - `keyword`: 关键词文本
      - `post`: 使用该关键词的广告发布数量
      - `video_list`: 使用该关键词的示例视频ID列表
    - `pagination`: 分页信息

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_keyword_list\",
      \"params\": {
        \"keyword\": \"cat toy\",
        \"period\": 120,
        \"page\": 1,
        \"limit\": 6
      },
      \"data\": {
        \"keyword_info_list\": [
          {
            \"keyword\": \"cat toy\",
            \"post\": 12345,
            \"video_list\": [\"7213258221116751874\", \"7213258221116751875\"]
          }
        ],
        \"pagination\": {
          \"page\": 1,
          \"limit\": 6,
          \"total\": 50,
          \"has_more\": true
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get ad placement data for specific keywords to understand keyword usage in TikTok ads
    - Analyze keyword post trends, related videos, and other information
    - Help advertisers discover effective ad keywords

    ### Parameters:
    - keyword: Search keyword, required parameter
    - period: Time period in days, e.g., 7, 30, 120 days
    - page: Page number, default 1
    - limit: Items per page, default 6
    - country_code: Country code, e.g., US, UK, JP
    - industry: Industry ID list, multiple IDs separated by commas

    ### Return Description:
    - `keyword_info_list`: Keyword information list
      - `keyword`: Keyword text
      - `post`: Number of ads using this keyword
      - `video_list`: List of example video IDs using this keyword
    - `pagination`: Pagination info

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_keyword_list\",
      \"params\": {
        \"keyword\": \"cat toy\",
        \"period\": 120,
        \"page\": 1,
        \"limit\": 6
      },
      \"data\": {
        \"keyword_info_list\": [
          {
            \"keyword\": \"cat toy\",
            \"post\": 12345,
            \"video_list\": [\"7213258221116751874\", \"7213258221116751875\"]
          }
        ],
        \"pagination\": {
          \"page\": 1,
          \"limit\": 6,
          \"total\": 50,
          \"has_more\": true
        }
      }
    }
    ```

    Args:
        keyword (Union[Unset, str]): 关键词/Keyword Default: 'cat toy'.
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 120.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 6.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.
        industry (Union[Unset, str]): 行业ID列表，逗号分隔/Industry IDs, comma separated Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        period=period,
        page=page,
        limit=limit,
        country_code=country_code,
        industry=industry,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    keyword: Union[Unset, str] = "cat toy",
    period: Union[Unset, int] = 120,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 6,
    country_code: Union[Unset, str] = "US",
    industry: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取关键词列表/Get keyword list

     # [中文]
    ### 用途:
    - 获取特定关键词的广告投放数据，了解关键词在TikTok广告中的使用情况
    - 分析关键词的发布量趋势、相关视频等信息
    - 帮助广告主发现有效的广告关键词

    ### 参数:
    - keyword: 搜索关键词，必填参数
    - period: 时间范围（天），如7、30、120天
    - page: 页码，默认1
    - limit: 每页数量，默认6
    - country_code: 国家代码，如US、UK、JP等
    - industry: 行业ID列表，多个ID用逗号分隔

    ### 返回内容说明:
    - `keyword_info_list`: 关键词信息列表
      - `keyword`: 关键词文本
      - `post`: 使用该关键词的广告发布数量
      - `video_list`: 使用该关键词的示例视频ID列表
    - `pagination`: 分页信息

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_keyword_list\",
      \"params\": {
        \"keyword\": \"cat toy\",
        \"period\": 120,
        \"page\": 1,
        \"limit\": 6
      },
      \"data\": {
        \"keyword_info_list\": [
          {
            \"keyword\": \"cat toy\",
            \"post\": 12345,
            \"video_list\": [\"7213258221116751874\", \"7213258221116751875\"]
          }
        ],
        \"pagination\": {
          \"page\": 1,
          \"limit\": 6,
          \"total\": 50,
          \"has_more\": true
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get ad placement data for specific keywords to understand keyword usage in TikTok ads
    - Analyze keyword post trends, related videos, and other information
    - Help advertisers discover effective ad keywords

    ### Parameters:
    - keyword: Search keyword, required parameter
    - period: Time period in days, e.g., 7, 30, 120 days
    - page: Page number, default 1
    - limit: Items per page, default 6
    - country_code: Country code, e.g., US, UK, JP
    - industry: Industry ID list, multiple IDs separated by commas

    ### Return Description:
    - `keyword_info_list`: Keyword information list
      - `keyword`: Keyword text
      - `post`: Number of ads using this keyword
      - `video_list`: List of example video IDs using this keyword
    - `pagination`: Pagination info

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_keyword_list\",
      \"params\": {
        \"keyword\": \"cat toy\",
        \"period\": 120,
        \"page\": 1,
        \"limit\": 6
      },
      \"data\": {
        \"keyword_info_list\": [
          {
            \"keyword\": \"cat toy\",
            \"post\": 12345,
            \"video_list\": [\"7213258221116751874\", \"7213258221116751875\"]
          }
        ],
        \"pagination\": {
          \"page\": 1,
          \"limit\": 6,
          \"total\": 50,
          \"has_more\": true
        }
      }
    }
    ```

    Args:
        keyword (Union[Unset, str]): 关键词/Keyword Default: 'cat toy'.
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 120.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 6.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.
        industry (Union[Unset, str]): 行业ID列表，逗号分隔/Industry IDs, comma separated Default: ''.

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
        page=page,
        limit=limit,
        country_code=country_code,
        industry=industry,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: Union[Unset, str] = "cat toy",
    period: Union[Unset, int] = 120,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 6,
    country_code: Union[Unset, str] = "US",
    industry: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取关键词列表/Get keyword list

     # [中文]
    ### 用途:
    - 获取特定关键词的广告投放数据，了解关键词在TikTok广告中的使用情况
    - 分析关键词的发布量趋势、相关视频等信息
    - 帮助广告主发现有效的广告关键词

    ### 参数:
    - keyword: 搜索关键词，必填参数
    - period: 时间范围（天），如7、30、120天
    - page: 页码，默认1
    - limit: 每页数量，默认6
    - country_code: 国家代码，如US、UK、JP等
    - industry: 行业ID列表，多个ID用逗号分隔

    ### 返回内容说明:
    - `keyword_info_list`: 关键词信息列表
      - `keyword`: 关键词文本
      - `post`: 使用该关键词的广告发布数量
      - `video_list`: 使用该关键词的示例视频ID列表
    - `pagination`: 分页信息

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_keyword_list\",
      \"params\": {
        \"keyword\": \"cat toy\",
        \"period\": 120,
        \"page\": 1,
        \"limit\": 6
      },
      \"data\": {
        \"keyword_info_list\": [
          {
            \"keyword\": \"cat toy\",
            \"post\": 12345,
            \"video_list\": [\"7213258221116751874\", \"7213258221116751875\"]
          }
        ],
        \"pagination\": {
          \"page\": 1,
          \"limit\": 6,
          \"total\": 50,
          \"has_more\": true
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get ad placement data for specific keywords to understand keyword usage in TikTok ads
    - Analyze keyword post trends, related videos, and other information
    - Help advertisers discover effective ad keywords

    ### Parameters:
    - keyword: Search keyword, required parameter
    - period: Time period in days, e.g., 7, 30, 120 days
    - page: Page number, default 1
    - limit: Items per page, default 6
    - country_code: Country code, e.g., US, UK, JP
    - industry: Industry ID list, multiple IDs separated by commas

    ### Return Description:
    - `keyword_info_list`: Keyword information list
      - `keyword`: Keyword text
      - `post`: Number of ads using this keyword
      - `video_list`: List of example video IDs using this keyword
    - `pagination`: Pagination info

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_keyword_list\",
      \"params\": {
        \"keyword\": \"cat toy\",
        \"period\": 120,
        \"page\": 1,
        \"limit\": 6
      },
      \"data\": {
        \"keyword_info_list\": [
          {
            \"keyword\": \"cat toy\",
            \"post\": 12345,
            \"video_list\": [\"7213258221116751874\", \"7213258221116751875\"]
          }
        ],
        \"pagination\": {
          \"page\": 1,
          \"limit\": 6,
          \"total\": 50,
          \"has_more\": true
        }
      }
    }
    ```

    Args:
        keyword (Union[Unset, str]): 关键词/Keyword Default: 'cat toy'.
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 120.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 6.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.
        industry (Union[Unset, str]): 行业ID列表，逗号分隔/Industry IDs, comma separated Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        period=period,
        page=page,
        limit=limit,
        country_code=country_code,
        industry=industry,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: Union[Unset, str] = "cat toy",
    period: Union[Unset, int] = 120,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 6,
    country_code: Union[Unset, str] = "US",
    industry: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取关键词列表/Get keyword list

     # [中文]
    ### 用途:
    - 获取特定关键词的广告投放数据，了解关键词在TikTok广告中的使用情况
    - 分析关键词的发布量趋势、相关视频等信息
    - 帮助广告主发现有效的广告关键词

    ### 参数:
    - keyword: 搜索关键词，必填参数
    - period: 时间范围（天），如7、30、120天
    - page: 页码，默认1
    - limit: 每页数量，默认6
    - country_code: 国家代码，如US、UK、JP等
    - industry: 行业ID列表，多个ID用逗号分隔

    ### 返回内容说明:
    - `keyword_info_list`: 关键词信息列表
      - `keyword`: 关键词文本
      - `post`: 使用该关键词的广告发布数量
      - `video_list`: 使用该关键词的示例视频ID列表
    - `pagination`: 分页信息

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_keyword_list\",
      \"params\": {
        \"keyword\": \"cat toy\",
        \"period\": 120,
        \"page\": 1,
        \"limit\": 6
      },
      \"data\": {
        \"keyword_info_list\": [
          {
            \"keyword\": \"cat toy\",
            \"post\": 12345,
            \"video_list\": [\"7213258221116751874\", \"7213258221116751875\"]
          }
        ],
        \"pagination\": {
          \"page\": 1,
          \"limit\": 6,
          \"total\": 50,
          \"has_more\": true
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get ad placement data for specific keywords to understand keyword usage in TikTok ads
    - Analyze keyword post trends, related videos, and other information
    - Help advertisers discover effective ad keywords

    ### Parameters:
    - keyword: Search keyword, required parameter
    - period: Time period in days, e.g., 7, 30, 120 days
    - page: Page number, default 1
    - limit: Items per page, default 6
    - country_code: Country code, e.g., US, UK, JP
    - industry: Industry ID list, multiple IDs separated by commas

    ### Return Description:
    - `keyword_info_list`: Keyword information list
      - `keyword`: Keyword text
      - `post`: Number of ads using this keyword
      - `video_list`: List of example video IDs using this keyword
    - `pagination`: Pagination info

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_keyword_list\",
      \"params\": {
        \"keyword\": \"cat toy\",
        \"period\": 120,
        \"page\": 1,
        \"limit\": 6
      },
      \"data\": {
        \"keyword_info_list\": [
          {
            \"keyword\": \"cat toy\",
            \"post\": 12345,
            \"video_list\": [\"7213258221116751874\", \"7213258221116751875\"]
          }
        ],
        \"pagination\": {
          \"page\": 1,
          \"limit\": 6,
          \"total\": 50,
          \"has_more\": true
        }
      }
    }
    ```

    Args:
        keyword (Union[Unset, str]): 关键词/Keyword Default: 'cat toy'.
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 120.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 6.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.
        industry (Union[Unset, str]): 行业ID列表，逗号分隔/Industry IDs, comma separated Default: ''.

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
            page=page,
            limit=limit,
            country_code=country_code,
            industry=industry,
        )
    ).parsed
