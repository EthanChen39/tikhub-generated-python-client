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
    objective: Union[Unset, int] = 1,
    like: Union[Unset, int] = 1,
    period: Union[Unset, int] = 180,
    industry: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    order_by: Union[Unset, str] = "for_you",
    country_code: Union[Unset, str] = "US",
    ad_format: Union[Unset, int] = 1,
    ad_language: Union[Unset, str] = "en",
    search_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["objective"] = objective

    params["like"] = like

    params["period"] = period

    params["industry"] = industry

    params["keyword"] = keyword

    params["page"] = page

    params["limit"] = limit

    params["order_by"] = order_by

    params["country_code"] = country_code

    params["ad_format"] = ad_format

    params["ad_language"] = ad_language

    params["search_id"] = search_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/search_ads",
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
    objective: Union[Unset, int] = 1,
    like: Union[Unset, int] = 1,
    period: Union[Unset, int] = 180,
    industry: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    order_by: Union[Unset, str] = "for_you",
    country_code: Union[Unset, str] = "US",
    ad_format: Union[Unset, int] = 1,
    ad_language: Union[Unset, str] = "en",
    search_id: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索广告/Search ads

     # [中文]
    ### 用途:
    - 搜索TikTok广告创意库中的广告，支持多维度筛选和排序
    - 发现特定行业、关键词或目标相关的高效广告案例
    - 为广告策划和创意制作提供参考和灵感

    ### 参数:
    - keyword: 搜索关键词，可选参数，留空返回所有广告
    - objective: 广告目标，1=全部
    - like: 点赞数筛选，1=全部
    - period: 时间范围（天），如7、30、120、180天
    - industry: 行业ID列表，多个ID用逗号分隔。完整行业ID列表见: https://github.com/TikHub/TikTok-Ads-Industry-Code
    - page: 页码，默认1
    - limit: 每页数量，默认20，最大50
    - order_by: 排序方式，\"for_you\"=为你推荐，\"likes\"=按点赞数排序
    - country_code: 国家代码，如US、UK、JP等
    - ad_format: 广告格式，1=视频广告
    - ad_language: 广告语言代码，如en、zh等

    ### 常用行业ID示例:
    - 游戏: 27000000000
    - 电子商务: 19000000000
    - 金融服务: 30000000000
    - 教育: 10000000000
    - 美妆个护: 22000000000
    - 食品饮料: 16000000000

    ### 返回内容说明:
    - `materials`: 广告素材列表
      - `id`: 广告素材ID
      - `aweme_id`: 广告视频ID
      - `desc`: 广告描述
      - `create_time`: 创建时间
      - `video_info`: 视频信息
        - `cover`: 封面图URL
        - `duration`: 时长（秒）
      - `statistics`: 统计数据
        - `digg_count`: 点赞数
        - `comment_count`: 评论数
        - `share_count`: 分享数
      - `ads_info`: 广告信息
        - `advertiser_name`: 广告主名称
        - `landing_page`: 落地页URL
    - `pagination`: 分页信息
      - `page`: 当前页
      - `limit`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_ads\",
      \"params\": {
        \"keyword\": \"cat toy\",
        \"period\": 180,
        \"industry\": \"27000000000\",
        \"page\": 1,
        \"limit\": 20
      },
      \"data\": {
        \"materials\": [
          {
            \"id\": \"7213258221116751874\",
            \"aweme_id\": \"7213258221116751874\",
            \"desc\": \"Best interactive cat toys! Keep your cats entertained 🐱\",
            \"create_time\": 1680234567,
            \"video_info\": {
              \"cover\": \"https://p16-ad-sg.tiktokcdn.com/img/xxx.jpeg\",
              \"duration\": 15
            },
            \"statistics\": {
              \"digg_count\": 128456,
              \"comment_count\": 3421,
              \"share_count\": 892
            },
            \"ads_info\": {
              \"advertiser_name\": \"PetToys Inc.\",
              \"landing_page\": \"https://example.com/cat-toys\"
            }
          }
        ],
        \"pagination\": {
          \"page\": 1,
          \"limit\": 20,
          \"total\": 1523,
          \"has_more\": true
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Search ads in TikTok's Creative Center with multi-dimensional filtering and sorting
    - Discover effective ad cases related to specific industries, keywords, or objectives
    - Provide reference and inspiration for ad planning and creative production

    ### Parameters:
    - keyword: Search keyword, optional, returns all ads if empty
    - objective: Ad objective, 1=All
    - like: Like count filter, 1=All
    - period: Time period in days, e.g., 7, 30, 120, 180 days
    - industry: Industry ID list, multiple IDs separated by commas. Full industry ID list:
    https://github.com/TikHub/TikTok-Ads-Industry-Code
    - page: Page number, default 1
    - limit: Items per page, default 20, max 50
    - order_by: Sort method, \"for_you\"=Recommended, \"likes\"=Sort by likes
    - country_code: Country code, e.g., US, UK, JP
    - ad_format: Ad format, 1=Video ads
    - ad_language: Ad language code, e.g., en, zh

    ### Common Industry ID Examples:
    - Games: 27000000000
    - E-commerce: 19000000000
    - Financial Services: 30000000000
    - Education: 10000000000
    - Beauty & Personal Care: 22000000000
    - Food & Beverage: 16000000000

    ### Return Description:
    - `materials`: List of ad materials
      - `id`: Ad material ID
      - `aweme_id`: Ad video ID
      - `desc`: Ad description
      - `create_time`: Creation time
      - `video_info`: Video information
        - `cover`: Cover image URL
        - `duration`: Duration in seconds
      - `statistics`: Statistics
        - `digg_count`: Number of likes
        - `comment_count`: Number of comments
        - `share_count`: Number of shares
      - `ads_info`: Ad information
        - `advertiser_name`: Advertiser name
        - `landing_page`: Landing page URL
    - `pagination`: Pagination info
      - `page`: Current page
      - `limit`: Items per page
      - `total`: Total count
      - `has_more`: Whether there are more items

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_ads\",
      \"params\": {
        \"keyword\": \"cat toy\",
        \"period\": 180,
        \"industry\": \"27000000000\",
        \"page\": 1,
        \"limit\": 20
      },
      \"data\": {
        \"materials\": [
          {
            \"id\": \"7213258221116751874\",
            \"aweme_id\": \"7213258221116751874\",
            \"desc\": \"Best interactive cat toys! Keep your cats entertained 🐱\",
            \"create_time\": 1680234567,
            \"video_info\": {
              \"cover\": \"https://p16-ad-sg.tiktokcdn.com/img/xxx.jpeg\",
              \"duration\": 15
            },
            \"statistics\": {
              \"digg_count\": 128456,
              \"comment_count\": 3421,
              \"share_count\": 892
            },
            \"ads_info\": {
              \"advertiser_name\": \"PetToys Inc.\",
              \"landing_page\": \"https://example.com/cat-toys\"
            }
          }
        ],
        \"pagination\": {
          \"page\": 1,
          \"limit\": 20,
          \"total\": 1523,
          \"has_more\": true
        }
      }
    }
    ```

    Args:
        objective (Union[Unset, int]): 广告目标类型/Ad objective (1:流量 2:应用安装 3:转化 4:视频浏览 5:触达 6:潜在客户
            7:产品销售) Default: 1.
        like (Union[Unset, int]): 表现排名/Performance rank (1:前1-20% 2:前21-40% 3:前41-60% 4:前61-80%)
            Default: 1.
        period (Union[Unset, int]): 时间段/Time period (days) Default: 180.
        industry (Union[Unset, str]): 行业ID/Industry ID
        keyword (Union[Unset, str]): 搜索关键词/Search keyword
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        order_by (Union[Unset, str]): 排序方式/Sort by (for_you, likes) Default: 'for_you'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.
        ad_format (Union[Unset, int]): 广告格式/Ad format (1:视频) Default: 1.
        ad_language (Union[Unset, str]): 广告语言/Ad language Default: 'en'.
        search_id (Union[Unset, str]): 搜索ID（可选）/Search ID (optional)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        objective=objective,
        like=like,
        period=period,
        industry=industry,
        keyword=keyword,
        page=page,
        limit=limit,
        order_by=order_by,
        country_code=country_code,
        ad_format=ad_format,
        ad_language=ad_language,
        search_id=search_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    objective: Union[Unset, int] = 1,
    like: Union[Unset, int] = 1,
    period: Union[Unset, int] = 180,
    industry: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    order_by: Union[Unset, str] = "for_you",
    country_code: Union[Unset, str] = "US",
    ad_format: Union[Unset, int] = 1,
    ad_language: Union[Unset, str] = "en",
    search_id: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索广告/Search ads

     # [中文]
    ### 用途:
    - 搜索TikTok广告创意库中的广告，支持多维度筛选和排序
    - 发现特定行业、关键词或目标相关的高效广告案例
    - 为广告策划和创意制作提供参考和灵感

    ### 参数:
    - keyword: 搜索关键词，可选参数，留空返回所有广告
    - objective: 广告目标，1=全部
    - like: 点赞数筛选，1=全部
    - period: 时间范围（天），如7、30、120、180天
    - industry: 行业ID列表，多个ID用逗号分隔。完整行业ID列表见: https://github.com/TikHub/TikTok-Ads-Industry-Code
    - page: 页码，默认1
    - limit: 每页数量，默认20，最大50
    - order_by: 排序方式，\"for_you\"=为你推荐，\"likes\"=按点赞数排序
    - country_code: 国家代码，如US、UK、JP等
    - ad_format: 广告格式，1=视频广告
    - ad_language: 广告语言代码，如en、zh等

    ### 常用行业ID示例:
    - 游戏: 27000000000
    - 电子商务: 19000000000
    - 金融服务: 30000000000
    - 教育: 10000000000
    - 美妆个护: 22000000000
    - 食品饮料: 16000000000

    ### 返回内容说明:
    - `materials`: 广告素材列表
      - `id`: 广告素材ID
      - `aweme_id`: 广告视频ID
      - `desc`: 广告描述
      - `create_time`: 创建时间
      - `video_info`: 视频信息
        - `cover`: 封面图URL
        - `duration`: 时长（秒）
      - `statistics`: 统计数据
        - `digg_count`: 点赞数
        - `comment_count`: 评论数
        - `share_count`: 分享数
      - `ads_info`: 广告信息
        - `advertiser_name`: 广告主名称
        - `landing_page`: 落地页URL
    - `pagination`: 分页信息
      - `page`: 当前页
      - `limit`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_ads\",
      \"params\": {
        \"keyword\": \"cat toy\",
        \"period\": 180,
        \"industry\": \"27000000000\",
        \"page\": 1,
        \"limit\": 20
      },
      \"data\": {
        \"materials\": [
          {
            \"id\": \"7213258221116751874\",
            \"aweme_id\": \"7213258221116751874\",
            \"desc\": \"Best interactive cat toys! Keep your cats entertained 🐱\",
            \"create_time\": 1680234567,
            \"video_info\": {
              \"cover\": \"https://p16-ad-sg.tiktokcdn.com/img/xxx.jpeg\",
              \"duration\": 15
            },
            \"statistics\": {
              \"digg_count\": 128456,
              \"comment_count\": 3421,
              \"share_count\": 892
            },
            \"ads_info\": {
              \"advertiser_name\": \"PetToys Inc.\",
              \"landing_page\": \"https://example.com/cat-toys\"
            }
          }
        ],
        \"pagination\": {
          \"page\": 1,
          \"limit\": 20,
          \"total\": 1523,
          \"has_more\": true
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Search ads in TikTok's Creative Center with multi-dimensional filtering and sorting
    - Discover effective ad cases related to specific industries, keywords, or objectives
    - Provide reference and inspiration for ad planning and creative production

    ### Parameters:
    - keyword: Search keyword, optional, returns all ads if empty
    - objective: Ad objective, 1=All
    - like: Like count filter, 1=All
    - period: Time period in days, e.g., 7, 30, 120, 180 days
    - industry: Industry ID list, multiple IDs separated by commas. Full industry ID list:
    https://github.com/TikHub/TikTok-Ads-Industry-Code
    - page: Page number, default 1
    - limit: Items per page, default 20, max 50
    - order_by: Sort method, \"for_you\"=Recommended, \"likes\"=Sort by likes
    - country_code: Country code, e.g., US, UK, JP
    - ad_format: Ad format, 1=Video ads
    - ad_language: Ad language code, e.g., en, zh

    ### Common Industry ID Examples:
    - Games: 27000000000
    - E-commerce: 19000000000
    - Financial Services: 30000000000
    - Education: 10000000000
    - Beauty & Personal Care: 22000000000
    - Food & Beverage: 16000000000

    ### Return Description:
    - `materials`: List of ad materials
      - `id`: Ad material ID
      - `aweme_id`: Ad video ID
      - `desc`: Ad description
      - `create_time`: Creation time
      - `video_info`: Video information
        - `cover`: Cover image URL
        - `duration`: Duration in seconds
      - `statistics`: Statistics
        - `digg_count`: Number of likes
        - `comment_count`: Number of comments
        - `share_count`: Number of shares
      - `ads_info`: Ad information
        - `advertiser_name`: Advertiser name
        - `landing_page`: Landing page URL
    - `pagination`: Pagination info
      - `page`: Current page
      - `limit`: Items per page
      - `total`: Total count
      - `has_more`: Whether there are more items

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_ads\",
      \"params\": {
        \"keyword\": \"cat toy\",
        \"period\": 180,
        \"industry\": \"27000000000\",
        \"page\": 1,
        \"limit\": 20
      },
      \"data\": {
        \"materials\": [
          {
            \"id\": \"7213258221116751874\",
            \"aweme_id\": \"7213258221116751874\",
            \"desc\": \"Best interactive cat toys! Keep your cats entertained 🐱\",
            \"create_time\": 1680234567,
            \"video_info\": {
              \"cover\": \"https://p16-ad-sg.tiktokcdn.com/img/xxx.jpeg\",
              \"duration\": 15
            },
            \"statistics\": {
              \"digg_count\": 128456,
              \"comment_count\": 3421,
              \"share_count\": 892
            },
            \"ads_info\": {
              \"advertiser_name\": \"PetToys Inc.\",
              \"landing_page\": \"https://example.com/cat-toys\"
            }
          }
        ],
        \"pagination\": {
          \"page\": 1,
          \"limit\": 20,
          \"total\": 1523,
          \"has_more\": true
        }
      }
    }
    ```

    Args:
        objective (Union[Unset, int]): 广告目标类型/Ad objective (1:流量 2:应用安装 3:转化 4:视频浏览 5:触达 6:潜在客户
            7:产品销售) Default: 1.
        like (Union[Unset, int]): 表现排名/Performance rank (1:前1-20% 2:前21-40% 3:前41-60% 4:前61-80%)
            Default: 1.
        period (Union[Unset, int]): 时间段/Time period (days) Default: 180.
        industry (Union[Unset, str]): 行业ID/Industry ID
        keyword (Union[Unset, str]): 搜索关键词/Search keyword
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        order_by (Union[Unset, str]): 排序方式/Sort by (for_you, likes) Default: 'for_you'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.
        ad_format (Union[Unset, int]): 广告格式/Ad format (1:视频) Default: 1.
        ad_language (Union[Unset, str]): 广告语言/Ad language Default: 'en'.
        search_id (Union[Unset, str]): 搜索ID（可选）/Search ID (optional)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        objective=objective,
        like=like,
        period=period,
        industry=industry,
        keyword=keyword,
        page=page,
        limit=limit,
        order_by=order_by,
        country_code=country_code,
        ad_format=ad_format,
        ad_language=ad_language,
        search_id=search_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    objective: Union[Unset, int] = 1,
    like: Union[Unset, int] = 1,
    period: Union[Unset, int] = 180,
    industry: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    order_by: Union[Unset, str] = "for_you",
    country_code: Union[Unset, str] = "US",
    ad_format: Union[Unset, int] = 1,
    ad_language: Union[Unset, str] = "en",
    search_id: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索广告/Search ads

     # [中文]
    ### 用途:
    - 搜索TikTok广告创意库中的广告，支持多维度筛选和排序
    - 发现特定行业、关键词或目标相关的高效广告案例
    - 为广告策划和创意制作提供参考和灵感

    ### 参数:
    - keyword: 搜索关键词，可选参数，留空返回所有广告
    - objective: 广告目标，1=全部
    - like: 点赞数筛选，1=全部
    - period: 时间范围（天），如7、30、120、180天
    - industry: 行业ID列表，多个ID用逗号分隔。完整行业ID列表见: https://github.com/TikHub/TikTok-Ads-Industry-Code
    - page: 页码，默认1
    - limit: 每页数量，默认20，最大50
    - order_by: 排序方式，\"for_you\"=为你推荐，\"likes\"=按点赞数排序
    - country_code: 国家代码，如US、UK、JP等
    - ad_format: 广告格式，1=视频广告
    - ad_language: 广告语言代码，如en、zh等

    ### 常用行业ID示例:
    - 游戏: 27000000000
    - 电子商务: 19000000000
    - 金融服务: 30000000000
    - 教育: 10000000000
    - 美妆个护: 22000000000
    - 食品饮料: 16000000000

    ### 返回内容说明:
    - `materials`: 广告素材列表
      - `id`: 广告素材ID
      - `aweme_id`: 广告视频ID
      - `desc`: 广告描述
      - `create_time`: 创建时间
      - `video_info`: 视频信息
        - `cover`: 封面图URL
        - `duration`: 时长（秒）
      - `statistics`: 统计数据
        - `digg_count`: 点赞数
        - `comment_count`: 评论数
        - `share_count`: 分享数
      - `ads_info`: 广告信息
        - `advertiser_name`: 广告主名称
        - `landing_page`: 落地页URL
    - `pagination`: 分页信息
      - `page`: 当前页
      - `limit`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_ads\",
      \"params\": {
        \"keyword\": \"cat toy\",
        \"period\": 180,
        \"industry\": \"27000000000\",
        \"page\": 1,
        \"limit\": 20
      },
      \"data\": {
        \"materials\": [
          {
            \"id\": \"7213258221116751874\",
            \"aweme_id\": \"7213258221116751874\",
            \"desc\": \"Best interactive cat toys! Keep your cats entertained 🐱\",
            \"create_time\": 1680234567,
            \"video_info\": {
              \"cover\": \"https://p16-ad-sg.tiktokcdn.com/img/xxx.jpeg\",
              \"duration\": 15
            },
            \"statistics\": {
              \"digg_count\": 128456,
              \"comment_count\": 3421,
              \"share_count\": 892
            },
            \"ads_info\": {
              \"advertiser_name\": \"PetToys Inc.\",
              \"landing_page\": \"https://example.com/cat-toys\"
            }
          }
        ],
        \"pagination\": {
          \"page\": 1,
          \"limit\": 20,
          \"total\": 1523,
          \"has_more\": true
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Search ads in TikTok's Creative Center with multi-dimensional filtering and sorting
    - Discover effective ad cases related to specific industries, keywords, or objectives
    - Provide reference and inspiration for ad planning and creative production

    ### Parameters:
    - keyword: Search keyword, optional, returns all ads if empty
    - objective: Ad objective, 1=All
    - like: Like count filter, 1=All
    - period: Time period in days, e.g., 7, 30, 120, 180 days
    - industry: Industry ID list, multiple IDs separated by commas. Full industry ID list:
    https://github.com/TikHub/TikTok-Ads-Industry-Code
    - page: Page number, default 1
    - limit: Items per page, default 20, max 50
    - order_by: Sort method, \"for_you\"=Recommended, \"likes\"=Sort by likes
    - country_code: Country code, e.g., US, UK, JP
    - ad_format: Ad format, 1=Video ads
    - ad_language: Ad language code, e.g., en, zh

    ### Common Industry ID Examples:
    - Games: 27000000000
    - E-commerce: 19000000000
    - Financial Services: 30000000000
    - Education: 10000000000
    - Beauty & Personal Care: 22000000000
    - Food & Beverage: 16000000000

    ### Return Description:
    - `materials`: List of ad materials
      - `id`: Ad material ID
      - `aweme_id`: Ad video ID
      - `desc`: Ad description
      - `create_time`: Creation time
      - `video_info`: Video information
        - `cover`: Cover image URL
        - `duration`: Duration in seconds
      - `statistics`: Statistics
        - `digg_count`: Number of likes
        - `comment_count`: Number of comments
        - `share_count`: Number of shares
      - `ads_info`: Ad information
        - `advertiser_name`: Advertiser name
        - `landing_page`: Landing page URL
    - `pagination`: Pagination info
      - `page`: Current page
      - `limit`: Items per page
      - `total`: Total count
      - `has_more`: Whether there are more items

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_ads\",
      \"params\": {
        \"keyword\": \"cat toy\",
        \"period\": 180,
        \"industry\": \"27000000000\",
        \"page\": 1,
        \"limit\": 20
      },
      \"data\": {
        \"materials\": [
          {
            \"id\": \"7213258221116751874\",
            \"aweme_id\": \"7213258221116751874\",
            \"desc\": \"Best interactive cat toys! Keep your cats entertained 🐱\",
            \"create_time\": 1680234567,
            \"video_info\": {
              \"cover\": \"https://p16-ad-sg.tiktokcdn.com/img/xxx.jpeg\",
              \"duration\": 15
            },
            \"statistics\": {
              \"digg_count\": 128456,
              \"comment_count\": 3421,
              \"share_count\": 892
            },
            \"ads_info\": {
              \"advertiser_name\": \"PetToys Inc.\",
              \"landing_page\": \"https://example.com/cat-toys\"
            }
          }
        ],
        \"pagination\": {
          \"page\": 1,
          \"limit\": 20,
          \"total\": 1523,
          \"has_more\": true
        }
      }
    }
    ```

    Args:
        objective (Union[Unset, int]): 广告目标类型/Ad objective (1:流量 2:应用安装 3:转化 4:视频浏览 5:触达 6:潜在客户
            7:产品销售) Default: 1.
        like (Union[Unset, int]): 表现排名/Performance rank (1:前1-20% 2:前21-40% 3:前41-60% 4:前61-80%)
            Default: 1.
        period (Union[Unset, int]): 时间段/Time period (days) Default: 180.
        industry (Union[Unset, str]): 行业ID/Industry ID
        keyword (Union[Unset, str]): 搜索关键词/Search keyword
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        order_by (Union[Unset, str]): 排序方式/Sort by (for_you, likes) Default: 'for_you'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.
        ad_format (Union[Unset, int]): 广告格式/Ad format (1:视频) Default: 1.
        ad_language (Union[Unset, str]): 广告语言/Ad language Default: 'en'.
        search_id (Union[Unset, str]): 搜索ID（可选）/Search ID (optional)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        objective=objective,
        like=like,
        period=period,
        industry=industry,
        keyword=keyword,
        page=page,
        limit=limit,
        order_by=order_by,
        country_code=country_code,
        ad_format=ad_format,
        ad_language=ad_language,
        search_id=search_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    objective: Union[Unset, int] = 1,
    like: Union[Unset, int] = 1,
    period: Union[Unset, int] = 180,
    industry: Union[Unset, str] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    order_by: Union[Unset, str] = "for_you",
    country_code: Union[Unset, str] = "US",
    ad_format: Union[Unset, int] = 1,
    ad_language: Union[Unset, str] = "en",
    search_id: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索广告/Search ads

     # [中文]
    ### 用途:
    - 搜索TikTok广告创意库中的广告，支持多维度筛选和排序
    - 发现特定行业、关键词或目标相关的高效广告案例
    - 为广告策划和创意制作提供参考和灵感

    ### 参数:
    - keyword: 搜索关键词，可选参数，留空返回所有广告
    - objective: 广告目标，1=全部
    - like: 点赞数筛选，1=全部
    - period: 时间范围（天），如7、30、120、180天
    - industry: 行业ID列表，多个ID用逗号分隔。完整行业ID列表见: https://github.com/TikHub/TikTok-Ads-Industry-Code
    - page: 页码，默认1
    - limit: 每页数量，默认20，最大50
    - order_by: 排序方式，\"for_you\"=为你推荐，\"likes\"=按点赞数排序
    - country_code: 国家代码，如US、UK、JP等
    - ad_format: 广告格式，1=视频广告
    - ad_language: 广告语言代码，如en、zh等

    ### 常用行业ID示例:
    - 游戏: 27000000000
    - 电子商务: 19000000000
    - 金融服务: 30000000000
    - 教育: 10000000000
    - 美妆个护: 22000000000
    - 食品饮料: 16000000000

    ### 返回内容说明:
    - `materials`: 广告素材列表
      - `id`: 广告素材ID
      - `aweme_id`: 广告视频ID
      - `desc`: 广告描述
      - `create_time`: 创建时间
      - `video_info`: 视频信息
        - `cover`: 封面图URL
        - `duration`: 时长（秒）
      - `statistics`: 统计数据
        - `digg_count`: 点赞数
        - `comment_count`: 评论数
        - `share_count`: 分享数
      - `ads_info`: 广告信息
        - `advertiser_name`: 广告主名称
        - `landing_page`: 落地页URL
    - `pagination`: 分页信息
      - `page`: 当前页
      - `limit`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_ads\",
      \"params\": {
        \"keyword\": \"cat toy\",
        \"period\": 180,
        \"industry\": \"27000000000\",
        \"page\": 1,
        \"limit\": 20
      },
      \"data\": {
        \"materials\": [
          {
            \"id\": \"7213258221116751874\",
            \"aweme_id\": \"7213258221116751874\",
            \"desc\": \"Best interactive cat toys! Keep your cats entertained 🐱\",
            \"create_time\": 1680234567,
            \"video_info\": {
              \"cover\": \"https://p16-ad-sg.tiktokcdn.com/img/xxx.jpeg\",
              \"duration\": 15
            },
            \"statistics\": {
              \"digg_count\": 128456,
              \"comment_count\": 3421,
              \"share_count\": 892
            },
            \"ads_info\": {
              \"advertiser_name\": \"PetToys Inc.\",
              \"landing_page\": \"https://example.com/cat-toys\"
            }
          }
        ],
        \"pagination\": {
          \"page\": 1,
          \"limit\": 20,
          \"total\": 1523,
          \"has_more\": true
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Search ads in TikTok's Creative Center with multi-dimensional filtering and sorting
    - Discover effective ad cases related to specific industries, keywords, or objectives
    - Provide reference and inspiration for ad planning and creative production

    ### Parameters:
    - keyword: Search keyword, optional, returns all ads if empty
    - objective: Ad objective, 1=All
    - like: Like count filter, 1=All
    - period: Time period in days, e.g., 7, 30, 120, 180 days
    - industry: Industry ID list, multiple IDs separated by commas. Full industry ID list:
    https://github.com/TikHub/TikTok-Ads-Industry-Code
    - page: Page number, default 1
    - limit: Items per page, default 20, max 50
    - order_by: Sort method, \"for_you\"=Recommended, \"likes\"=Sort by likes
    - country_code: Country code, e.g., US, UK, JP
    - ad_format: Ad format, 1=Video ads
    - ad_language: Ad language code, e.g., en, zh

    ### Common Industry ID Examples:
    - Games: 27000000000
    - E-commerce: 19000000000
    - Financial Services: 30000000000
    - Education: 10000000000
    - Beauty & Personal Care: 22000000000
    - Food & Beverage: 16000000000

    ### Return Description:
    - `materials`: List of ad materials
      - `id`: Ad material ID
      - `aweme_id`: Ad video ID
      - `desc`: Ad description
      - `create_time`: Creation time
      - `video_info`: Video information
        - `cover`: Cover image URL
        - `duration`: Duration in seconds
      - `statistics`: Statistics
        - `digg_count`: Number of likes
        - `comment_count`: Number of comments
        - `share_count`: Number of shares
      - `ads_info`: Ad information
        - `advertiser_name`: Advertiser name
        - `landing_page`: Landing page URL
    - `pagination`: Pagination info
      - `page`: Current page
      - `limit`: Items per page
      - `total`: Total count
      - `has_more`: Whether there are more items

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_ads\",
      \"params\": {
        \"keyword\": \"cat toy\",
        \"period\": 180,
        \"industry\": \"27000000000\",
        \"page\": 1,
        \"limit\": 20
      },
      \"data\": {
        \"materials\": [
          {
            \"id\": \"7213258221116751874\",
            \"aweme_id\": \"7213258221116751874\",
            \"desc\": \"Best interactive cat toys! Keep your cats entertained 🐱\",
            \"create_time\": 1680234567,
            \"video_info\": {
              \"cover\": \"https://p16-ad-sg.tiktokcdn.com/img/xxx.jpeg\",
              \"duration\": 15
            },
            \"statistics\": {
              \"digg_count\": 128456,
              \"comment_count\": 3421,
              \"share_count\": 892
            },
            \"ads_info\": {
              \"advertiser_name\": \"PetToys Inc.\",
              \"landing_page\": \"https://example.com/cat-toys\"
            }
          }
        ],
        \"pagination\": {
          \"page\": 1,
          \"limit\": 20,
          \"total\": 1523,
          \"has_more\": true
        }
      }
    }
    ```

    Args:
        objective (Union[Unset, int]): 广告目标类型/Ad objective (1:流量 2:应用安装 3:转化 4:视频浏览 5:触达 6:潜在客户
            7:产品销售) Default: 1.
        like (Union[Unset, int]): 表现排名/Performance rank (1:前1-20% 2:前21-40% 3:前41-60% 4:前61-80%)
            Default: 1.
        period (Union[Unset, int]): 时间段/Time period (days) Default: 180.
        industry (Union[Unset, str]): 行业ID/Industry ID
        keyword (Union[Unset, str]): 搜索关键词/Search keyword
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        order_by (Union[Unset, str]): 排序方式/Sort by (for_you, likes) Default: 'for_you'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.
        ad_format (Union[Unset, int]): 广告格式/Ad format (1:视频) Default: 1.
        ad_language (Union[Unset, str]): 广告语言/Ad language Default: 'en'.
        search_id (Union[Unset, str]): 搜索ID（可选）/Search ID (optional)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            objective=objective,
            like=like,
            period=period,
            industry=industry,
            keyword=keyword,
            page=page,
            limit=limit,
            order_by=order_by,
            country_code=country_code,
            ad_format=ad_format,
            ad_language=ad_language,
            search_id=search_id,
        )
    ).parsed
