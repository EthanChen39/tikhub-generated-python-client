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
    period: Union[Unset, int] = 120,
    country_code: Union[Unset, str] = "US",
    sort_by: Union[Unset, str] = "popular",
    industry_id: Union[Unset, str] = "",
    filter_by: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params["period"] = period

    params["country_code"] = country_code

    params["sort_by"] = sort_by

    params["industry_id"] = industry_id

    params["filter_by"] = filter_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/get_hashtag_list",
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
    period: Union[Unset, int] = 120,
    country_code: Union[Unset, str] = "US",
    sort_by: Union[Unset, str] = "popular",
    industry_id: Union[Unset, str] = "",
    filter_by: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取热门标签列表/Get popular hashtags list

     # [中文]
    ### 用途:
    - 获取TikTok广告中的热门标签排行榜，了解当前流行的话题标签
    - 分析标签的使用量、观看量等数据，发现潜力标签
    - 帮助广告主选择合适的标签，提升广告曝光和互动率

    ### 参数:
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - period: 时间范围（天），如7、30、120天
    - country_code: 国家代码，如US、UK、JP等
    - sort_by: 排序方式，\"popular\"=热门，\"new\"=最新
    - industry_id: 行业ID，留空返回所有行业
    - filter_by: 筛选条件，\"new_on_board\"=新上榜标签

    ### 返回内容说明:
    - `list`: 标签列表
      - `hashtag_id`: 标签ID
      - `hashtag_name`: 标签名称
      - `country_info`: 国家信息
        - `id`: 国家ID
        - `value`: 国家名称
        - `label`: 国家标签
      - `industry_info`: 行业信息
        - `id`: 行业ID
        - `value`: 行业名称
        - `label`: 行业标签
      - `is_promoted`: 是否推广
      - `trend`: 趋势数据列表
        - `time`: 时间戳
        - `value`: 该时间点的值
      - `creators`: 创作者列表
        - `nick_name`: 昵称
        - `avatar_url`: 头像URL
      - `publish_cnt`: 发布数量
      - `video_views`: 视频观看量
      - `rank`: 排名
      - `rank_diff`: 排名变化
      - `rank_diff_type`: 排名变化类型
    - `pagination`: 分页信息
      - `page`: 当前页
      - `size`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_hashtag_list\",
      \"params\": {
        \"page\": \"1\",
        \"limit\": \"20\",
        \"period\": \"120\",
        \"country_code\": \"US\",
        \"sort_by\": \"popular\",
        \"industry_id\": \"\",
        \"filter_by\": \"\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"list\": [
            {
              \"hashtag_id\": \"4100\",
              \"hashtag_name\": \"summer\",
              \"country_info\": {
                \"id\": \"US\",
                \"value\": \"United States\",
                \"label\": \"US\"
              },
              \"industry_info\": {
                \"id\": 28000000000,
                \"value\": \"Sports & Outdoor\",
                \"label\": \"label_28000000000\"
              },
              \"is_promoted\": false,
              \"trend\": [
                {
                  \"time\": 1740787200,
                  \"value\": 0.38
                },
                {
                  \"time\": 1741392000,
                  \"value\": 0.37
                },
                {
                  \"time\": 1741996800,
                  \"value\": 0.43
                },
                {
                  \"time\": 1749254400,
                  \"value\": 1
                }
              ],
              \"creators\": [
                {
                  \"nick_name\": \"Mark Broze\",
                  \"avatar_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-
    avt-0068/28bb3ad309c2165f9579a67515d17ca9~tplv-tiktokx-cropcenter:100:100.png\"
                },
                {
                  \"nick_name\": \"Liam 🤠\",
                  \"avatar_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-
    avt-0068/a27b40671c78f8af17cdd2618ad8ba20~tplv-tiktokx-cropcenter:100:100.png\"
                }
              ],
              \"publish_cnt\": 2886791,
              \"video_views\": 19583705445,
              \"rank\": 1,
              \"rank_diff\": 1,
              \"rank_diff_type\": 1
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 100,
            \"has_more\": true
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get popular hashtag rankings in TikTok ads to understand current trending topics
    - Analyze usage and view data for hashtags to discover potential tags
    - Help advertisers choose appropriate hashtags to increase ad exposure and engagement

    ### Parameters:
    - page: Page number, default 1
    - limit: Items per page, default 20
    - period: Time period in days, e.g., 7, 30, 120 days
    - country_code: Country code, e.g., US, UK, JP
    - sort_by: Sort method, \"popular\"=Popular, \"new\"=Latest
    - industry_id: Industry ID, empty returns all industries
    - filter_by: Filter condition, \"new_on_board\"=Newly trending hashtags

    ### Return Description:
    - `list`: Hashtag list
      - `hashtag_id`: Hashtag ID
      - `hashtag_name`: Hashtag name
      - `country_info`: Country information
        - `id`: Country ID
        - `value`: Country name
        - `label`: Country label
      - `industry_info`: Industry information
        - `id`: Industry ID
        - `value`: Industry name
        - `label`: Industry label
      - `is_promoted`: Whether promoted
      - `trend`: Trend data list
        - `time`: Timestamp
        - `value`: Value at that time point
      - `creators`: Creator list
        - `nick_name`: Nickname
        - `avatar_url`: Avatar URL
      - `publish_cnt`: Publish count
      - `video_views`: Video views
      - `rank`: Ranking
      - `rank_diff`: Rank difference
      - `rank_diff_type`: Rank difference type
    - `pagination`: Pagination info
      - `page`: Current page
      - `size`: Items per page
      - `total`: Total count
      - `has_more`: Whether there are more items

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_hashtag_list\",
      \"params\": {
        \"page\": \"1\",
        \"limit\": \"20\",
        \"period\": \"120\",
        \"country_code\": \"US\",
        \"sort_by\": \"popular\",
        \"industry_id\": \"\",
        \"filter_by\": \"\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"list\": [
            {
              \"hashtag_id\": \"4100\",
              \"hashtag_name\": \"summer\",
              \"country_info\": {
                \"id\": \"US\",
                \"value\": \"United States\",
                \"label\": \"US\"
              },
              \"industry_info\": {
                \"id\": 28000000000,
                \"value\": \"Sports & Outdoor\",
                \"label\": \"label_28000000000\"
              },
              \"is_promoted\": false,
              \"trend\": [
                {
                  \"time\": 1740787200,
                  \"value\": 0.38
                },
                {
                  \"time\": 1741392000,
                  \"value\": 0.37
                }
              ],
              \"creators\": [
                {
                  \"nick_name\": \"creator1\",
                  \"avatar_url\": \"https://example.com/avatar1.jpg\"
                }
              ],
              \"publish_cnt\": 45678,
              \"video_views\": 123456789,
              \"rank\": 1,
              \"rank_diff\": 2,
              \"rank_diff_type\": 1
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 500,
            \"has_more\": true
          }
        }
      }
    }
    ```

    Args:
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 120.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.
        sort_by (Union[Unset, str]): 排序方式/Sort by (popular, new) Default: 'popular'.
        industry_id (Union[Unset, str]): 行业ID/Industry ID Default: ''.
        filter_by (Union[Unset, str]): 筛选条件/Filter (new_on_board) Default: ''.

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
        sort_by=sort_by,
        industry_id=industry_id,
        filter_by=filter_by,
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
    period: Union[Unset, int] = 120,
    country_code: Union[Unset, str] = "US",
    sort_by: Union[Unset, str] = "popular",
    industry_id: Union[Unset, str] = "",
    filter_by: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取热门标签列表/Get popular hashtags list

     # [中文]
    ### 用途:
    - 获取TikTok广告中的热门标签排行榜，了解当前流行的话题标签
    - 分析标签的使用量、观看量等数据，发现潜力标签
    - 帮助广告主选择合适的标签，提升广告曝光和互动率

    ### 参数:
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - period: 时间范围（天），如7、30、120天
    - country_code: 国家代码，如US、UK、JP等
    - sort_by: 排序方式，\"popular\"=热门，\"new\"=最新
    - industry_id: 行业ID，留空返回所有行业
    - filter_by: 筛选条件，\"new_on_board\"=新上榜标签

    ### 返回内容说明:
    - `list`: 标签列表
      - `hashtag_id`: 标签ID
      - `hashtag_name`: 标签名称
      - `country_info`: 国家信息
        - `id`: 国家ID
        - `value`: 国家名称
        - `label`: 国家标签
      - `industry_info`: 行业信息
        - `id`: 行业ID
        - `value`: 行业名称
        - `label`: 行业标签
      - `is_promoted`: 是否推广
      - `trend`: 趋势数据列表
        - `time`: 时间戳
        - `value`: 该时间点的值
      - `creators`: 创作者列表
        - `nick_name`: 昵称
        - `avatar_url`: 头像URL
      - `publish_cnt`: 发布数量
      - `video_views`: 视频观看量
      - `rank`: 排名
      - `rank_diff`: 排名变化
      - `rank_diff_type`: 排名变化类型
    - `pagination`: 分页信息
      - `page`: 当前页
      - `size`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_hashtag_list\",
      \"params\": {
        \"page\": \"1\",
        \"limit\": \"20\",
        \"period\": \"120\",
        \"country_code\": \"US\",
        \"sort_by\": \"popular\",
        \"industry_id\": \"\",
        \"filter_by\": \"\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"list\": [
            {
              \"hashtag_id\": \"4100\",
              \"hashtag_name\": \"summer\",
              \"country_info\": {
                \"id\": \"US\",
                \"value\": \"United States\",
                \"label\": \"US\"
              },
              \"industry_info\": {
                \"id\": 28000000000,
                \"value\": \"Sports & Outdoor\",
                \"label\": \"label_28000000000\"
              },
              \"is_promoted\": false,
              \"trend\": [
                {
                  \"time\": 1740787200,
                  \"value\": 0.38
                },
                {
                  \"time\": 1741392000,
                  \"value\": 0.37
                },
                {
                  \"time\": 1741996800,
                  \"value\": 0.43
                },
                {
                  \"time\": 1749254400,
                  \"value\": 1
                }
              ],
              \"creators\": [
                {
                  \"nick_name\": \"Mark Broze\",
                  \"avatar_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-
    avt-0068/28bb3ad309c2165f9579a67515d17ca9~tplv-tiktokx-cropcenter:100:100.png\"
                },
                {
                  \"nick_name\": \"Liam 🤠\",
                  \"avatar_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-
    avt-0068/a27b40671c78f8af17cdd2618ad8ba20~tplv-tiktokx-cropcenter:100:100.png\"
                }
              ],
              \"publish_cnt\": 2886791,
              \"video_views\": 19583705445,
              \"rank\": 1,
              \"rank_diff\": 1,
              \"rank_diff_type\": 1
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 100,
            \"has_more\": true
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get popular hashtag rankings in TikTok ads to understand current trending topics
    - Analyze usage and view data for hashtags to discover potential tags
    - Help advertisers choose appropriate hashtags to increase ad exposure and engagement

    ### Parameters:
    - page: Page number, default 1
    - limit: Items per page, default 20
    - period: Time period in days, e.g., 7, 30, 120 days
    - country_code: Country code, e.g., US, UK, JP
    - sort_by: Sort method, \"popular\"=Popular, \"new\"=Latest
    - industry_id: Industry ID, empty returns all industries
    - filter_by: Filter condition, \"new_on_board\"=Newly trending hashtags

    ### Return Description:
    - `list`: Hashtag list
      - `hashtag_id`: Hashtag ID
      - `hashtag_name`: Hashtag name
      - `country_info`: Country information
        - `id`: Country ID
        - `value`: Country name
        - `label`: Country label
      - `industry_info`: Industry information
        - `id`: Industry ID
        - `value`: Industry name
        - `label`: Industry label
      - `is_promoted`: Whether promoted
      - `trend`: Trend data list
        - `time`: Timestamp
        - `value`: Value at that time point
      - `creators`: Creator list
        - `nick_name`: Nickname
        - `avatar_url`: Avatar URL
      - `publish_cnt`: Publish count
      - `video_views`: Video views
      - `rank`: Ranking
      - `rank_diff`: Rank difference
      - `rank_diff_type`: Rank difference type
    - `pagination`: Pagination info
      - `page`: Current page
      - `size`: Items per page
      - `total`: Total count
      - `has_more`: Whether there are more items

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_hashtag_list\",
      \"params\": {
        \"page\": \"1\",
        \"limit\": \"20\",
        \"period\": \"120\",
        \"country_code\": \"US\",
        \"sort_by\": \"popular\",
        \"industry_id\": \"\",
        \"filter_by\": \"\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"list\": [
            {
              \"hashtag_id\": \"4100\",
              \"hashtag_name\": \"summer\",
              \"country_info\": {
                \"id\": \"US\",
                \"value\": \"United States\",
                \"label\": \"US\"
              },
              \"industry_info\": {
                \"id\": 28000000000,
                \"value\": \"Sports & Outdoor\",
                \"label\": \"label_28000000000\"
              },
              \"is_promoted\": false,
              \"trend\": [
                {
                  \"time\": 1740787200,
                  \"value\": 0.38
                },
                {
                  \"time\": 1741392000,
                  \"value\": 0.37
                }
              ],
              \"creators\": [
                {
                  \"nick_name\": \"creator1\",
                  \"avatar_url\": \"https://example.com/avatar1.jpg\"
                }
              ],
              \"publish_cnt\": 45678,
              \"video_views\": 123456789,
              \"rank\": 1,
              \"rank_diff\": 2,
              \"rank_diff_type\": 1
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 500,
            \"has_more\": true
          }
        }
      }
    }
    ```

    Args:
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 120.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.
        sort_by (Union[Unset, str]): 排序方式/Sort by (popular, new) Default: 'popular'.
        industry_id (Union[Unset, str]): 行业ID/Industry ID Default: ''.
        filter_by (Union[Unset, str]): 筛选条件/Filter (new_on_board) Default: ''.

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
        sort_by=sort_by,
        industry_id=industry_id,
        filter_by=filter_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    period: Union[Unset, int] = 120,
    country_code: Union[Unset, str] = "US",
    sort_by: Union[Unset, str] = "popular",
    industry_id: Union[Unset, str] = "",
    filter_by: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取热门标签列表/Get popular hashtags list

     # [中文]
    ### 用途:
    - 获取TikTok广告中的热门标签排行榜，了解当前流行的话题标签
    - 分析标签的使用量、观看量等数据，发现潜力标签
    - 帮助广告主选择合适的标签，提升广告曝光和互动率

    ### 参数:
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - period: 时间范围（天），如7、30、120天
    - country_code: 国家代码，如US、UK、JP等
    - sort_by: 排序方式，\"popular\"=热门，\"new\"=最新
    - industry_id: 行业ID，留空返回所有行业
    - filter_by: 筛选条件，\"new_on_board\"=新上榜标签

    ### 返回内容说明:
    - `list`: 标签列表
      - `hashtag_id`: 标签ID
      - `hashtag_name`: 标签名称
      - `country_info`: 国家信息
        - `id`: 国家ID
        - `value`: 国家名称
        - `label`: 国家标签
      - `industry_info`: 行业信息
        - `id`: 行业ID
        - `value`: 行业名称
        - `label`: 行业标签
      - `is_promoted`: 是否推广
      - `trend`: 趋势数据列表
        - `time`: 时间戳
        - `value`: 该时间点的值
      - `creators`: 创作者列表
        - `nick_name`: 昵称
        - `avatar_url`: 头像URL
      - `publish_cnt`: 发布数量
      - `video_views`: 视频观看量
      - `rank`: 排名
      - `rank_diff`: 排名变化
      - `rank_diff_type`: 排名变化类型
    - `pagination`: 分页信息
      - `page`: 当前页
      - `size`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_hashtag_list\",
      \"params\": {
        \"page\": \"1\",
        \"limit\": \"20\",
        \"period\": \"120\",
        \"country_code\": \"US\",
        \"sort_by\": \"popular\",
        \"industry_id\": \"\",
        \"filter_by\": \"\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"list\": [
            {
              \"hashtag_id\": \"4100\",
              \"hashtag_name\": \"summer\",
              \"country_info\": {
                \"id\": \"US\",
                \"value\": \"United States\",
                \"label\": \"US\"
              },
              \"industry_info\": {
                \"id\": 28000000000,
                \"value\": \"Sports & Outdoor\",
                \"label\": \"label_28000000000\"
              },
              \"is_promoted\": false,
              \"trend\": [
                {
                  \"time\": 1740787200,
                  \"value\": 0.38
                },
                {
                  \"time\": 1741392000,
                  \"value\": 0.37
                },
                {
                  \"time\": 1741996800,
                  \"value\": 0.43
                },
                {
                  \"time\": 1749254400,
                  \"value\": 1
                }
              ],
              \"creators\": [
                {
                  \"nick_name\": \"Mark Broze\",
                  \"avatar_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-
    avt-0068/28bb3ad309c2165f9579a67515d17ca9~tplv-tiktokx-cropcenter:100:100.png\"
                },
                {
                  \"nick_name\": \"Liam 🤠\",
                  \"avatar_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-
    avt-0068/a27b40671c78f8af17cdd2618ad8ba20~tplv-tiktokx-cropcenter:100:100.png\"
                }
              ],
              \"publish_cnt\": 2886791,
              \"video_views\": 19583705445,
              \"rank\": 1,
              \"rank_diff\": 1,
              \"rank_diff_type\": 1
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 100,
            \"has_more\": true
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get popular hashtag rankings in TikTok ads to understand current trending topics
    - Analyze usage and view data for hashtags to discover potential tags
    - Help advertisers choose appropriate hashtags to increase ad exposure and engagement

    ### Parameters:
    - page: Page number, default 1
    - limit: Items per page, default 20
    - period: Time period in days, e.g., 7, 30, 120 days
    - country_code: Country code, e.g., US, UK, JP
    - sort_by: Sort method, \"popular\"=Popular, \"new\"=Latest
    - industry_id: Industry ID, empty returns all industries
    - filter_by: Filter condition, \"new_on_board\"=Newly trending hashtags

    ### Return Description:
    - `list`: Hashtag list
      - `hashtag_id`: Hashtag ID
      - `hashtag_name`: Hashtag name
      - `country_info`: Country information
        - `id`: Country ID
        - `value`: Country name
        - `label`: Country label
      - `industry_info`: Industry information
        - `id`: Industry ID
        - `value`: Industry name
        - `label`: Industry label
      - `is_promoted`: Whether promoted
      - `trend`: Trend data list
        - `time`: Timestamp
        - `value`: Value at that time point
      - `creators`: Creator list
        - `nick_name`: Nickname
        - `avatar_url`: Avatar URL
      - `publish_cnt`: Publish count
      - `video_views`: Video views
      - `rank`: Ranking
      - `rank_diff`: Rank difference
      - `rank_diff_type`: Rank difference type
    - `pagination`: Pagination info
      - `page`: Current page
      - `size`: Items per page
      - `total`: Total count
      - `has_more`: Whether there are more items

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_hashtag_list\",
      \"params\": {
        \"page\": \"1\",
        \"limit\": \"20\",
        \"period\": \"120\",
        \"country_code\": \"US\",
        \"sort_by\": \"popular\",
        \"industry_id\": \"\",
        \"filter_by\": \"\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"list\": [
            {
              \"hashtag_id\": \"4100\",
              \"hashtag_name\": \"summer\",
              \"country_info\": {
                \"id\": \"US\",
                \"value\": \"United States\",
                \"label\": \"US\"
              },
              \"industry_info\": {
                \"id\": 28000000000,
                \"value\": \"Sports & Outdoor\",
                \"label\": \"label_28000000000\"
              },
              \"is_promoted\": false,
              \"trend\": [
                {
                  \"time\": 1740787200,
                  \"value\": 0.38
                },
                {
                  \"time\": 1741392000,
                  \"value\": 0.37
                }
              ],
              \"creators\": [
                {
                  \"nick_name\": \"creator1\",
                  \"avatar_url\": \"https://example.com/avatar1.jpg\"
                }
              ],
              \"publish_cnt\": 45678,
              \"video_views\": 123456789,
              \"rank\": 1,
              \"rank_diff\": 2,
              \"rank_diff_type\": 1
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 500,
            \"has_more\": true
          }
        }
      }
    }
    ```

    Args:
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 120.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.
        sort_by (Union[Unset, str]): 排序方式/Sort by (popular, new) Default: 'popular'.
        industry_id (Union[Unset, str]): 行业ID/Industry ID Default: ''.
        filter_by (Union[Unset, str]): 筛选条件/Filter (new_on_board) Default: ''.

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
        sort_by=sort_by,
        industry_id=industry_id,
        filter_by=filter_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    period: Union[Unset, int] = 120,
    country_code: Union[Unset, str] = "US",
    sort_by: Union[Unset, str] = "popular",
    industry_id: Union[Unset, str] = "",
    filter_by: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取热门标签列表/Get popular hashtags list

     # [中文]
    ### 用途:
    - 获取TikTok广告中的热门标签排行榜，了解当前流行的话题标签
    - 分析标签的使用量、观看量等数据，发现潜力标签
    - 帮助广告主选择合适的标签，提升广告曝光和互动率

    ### 参数:
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - period: 时间范围（天），如7、30、120天
    - country_code: 国家代码，如US、UK、JP等
    - sort_by: 排序方式，\"popular\"=热门，\"new\"=最新
    - industry_id: 行业ID，留空返回所有行业
    - filter_by: 筛选条件，\"new_on_board\"=新上榜标签

    ### 返回内容说明:
    - `list`: 标签列表
      - `hashtag_id`: 标签ID
      - `hashtag_name`: 标签名称
      - `country_info`: 国家信息
        - `id`: 国家ID
        - `value`: 国家名称
        - `label`: 国家标签
      - `industry_info`: 行业信息
        - `id`: 行业ID
        - `value`: 行业名称
        - `label`: 行业标签
      - `is_promoted`: 是否推广
      - `trend`: 趋势数据列表
        - `time`: 时间戳
        - `value`: 该时间点的值
      - `creators`: 创作者列表
        - `nick_name`: 昵称
        - `avatar_url`: 头像URL
      - `publish_cnt`: 发布数量
      - `video_views`: 视频观看量
      - `rank`: 排名
      - `rank_diff`: 排名变化
      - `rank_diff_type`: 排名变化类型
    - `pagination`: 分页信息
      - `page`: 当前页
      - `size`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_hashtag_list\",
      \"params\": {
        \"page\": \"1\",
        \"limit\": \"20\",
        \"period\": \"120\",
        \"country_code\": \"US\",
        \"sort_by\": \"popular\",
        \"industry_id\": \"\",
        \"filter_by\": \"\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"list\": [
            {
              \"hashtag_id\": \"4100\",
              \"hashtag_name\": \"summer\",
              \"country_info\": {
                \"id\": \"US\",
                \"value\": \"United States\",
                \"label\": \"US\"
              },
              \"industry_info\": {
                \"id\": 28000000000,
                \"value\": \"Sports & Outdoor\",
                \"label\": \"label_28000000000\"
              },
              \"is_promoted\": false,
              \"trend\": [
                {
                  \"time\": 1740787200,
                  \"value\": 0.38
                },
                {
                  \"time\": 1741392000,
                  \"value\": 0.37
                },
                {
                  \"time\": 1741996800,
                  \"value\": 0.43
                },
                {
                  \"time\": 1749254400,
                  \"value\": 1
                }
              ],
              \"creators\": [
                {
                  \"nick_name\": \"Mark Broze\",
                  \"avatar_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-
    avt-0068/28bb3ad309c2165f9579a67515d17ca9~tplv-tiktokx-cropcenter:100:100.png\"
                },
                {
                  \"nick_name\": \"Liam 🤠\",
                  \"avatar_url\": \"https://p16-sign-sg.tiktokcdn.com/tos-alisg-
    avt-0068/a27b40671c78f8af17cdd2618ad8ba20~tplv-tiktokx-cropcenter:100:100.png\"
                }
              ],
              \"publish_cnt\": 2886791,
              \"video_views\": 19583705445,
              \"rank\": 1,
              \"rank_diff\": 1,
              \"rank_diff_type\": 1
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 100,
            \"has_more\": true
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get popular hashtag rankings in TikTok ads to understand current trending topics
    - Analyze usage and view data for hashtags to discover potential tags
    - Help advertisers choose appropriate hashtags to increase ad exposure and engagement

    ### Parameters:
    - page: Page number, default 1
    - limit: Items per page, default 20
    - period: Time period in days, e.g., 7, 30, 120 days
    - country_code: Country code, e.g., US, UK, JP
    - sort_by: Sort method, \"popular\"=Popular, \"new\"=Latest
    - industry_id: Industry ID, empty returns all industries
    - filter_by: Filter condition, \"new_on_board\"=Newly trending hashtags

    ### Return Description:
    - `list`: Hashtag list
      - `hashtag_id`: Hashtag ID
      - `hashtag_name`: Hashtag name
      - `country_info`: Country information
        - `id`: Country ID
        - `value`: Country name
        - `label`: Country label
      - `industry_info`: Industry information
        - `id`: Industry ID
        - `value`: Industry name
        - `label`: Industry label
      - `is_promoted`: Whether promoted
      - `trend`: Trend data list
        - `time`: Timestamp
        - `value`: Value at that time point
      - `creators`: Creator list
        - `nick_name`: Nickname
        - `avatar_url`: Avatar URL
      - `publish_cnt`: Publish count
      - `video_views`: Video views
      - `rank`: Ranking
      - `rank_diff`: Rank difference
      - `rank_diff_type`: Rank difference type
    - `pagination`: Pagination info
      - `page`: Current page
      - `size`: Items per page
      - `total`: Total count
      - `has_more`: Whether there are more items

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_hashtag_list\",
      \"params\": {
        \"page\": \"1\",
        \"limit\": \"20\",
        \"period\": \"120\",
        \"country_code\": \"US\",
        \"sort_by\": \"popular\",
        \"industry_id\": \"\",
        \"filter_by\": \"\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"list\": [
            {
              \"hashtag_id\": \"4100\",
              \"hashtag_name\": \"summer\",
              \"country_info\": {
                \"id\": \"US\",
                \"value\": \"United States\",
                \"label\": \"US\"
              },
              \"industry_info\": {
                \"id\": 28000000000,
                \"value\": \"Sports & Outdoor\",
                \"label\": \"label_28000000000\"
              },
              \"is_promoted\": false,
              \"trend\": [
                {
                  \"time\": 1740787200,
                  \"value\": 0.38
                },
                {
                  \"time\": 1741392000,
                  \"value\": 0.37
                }
              ],
              \"creators\": [
                {
                  \"nick_name\": \"creator1\",
                  \"avatar_url\": \"https://example.com/avatar1.jpg\"
                }
              ],
              \"publish_cnt\": 45678,
              \"video_views\": 123456789,
              \"rank\": 1,
              \"rank_diff\": 2,
              \"rank_diff_type\": 1
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 500,
            \"has_more\": true
          }
        }
      }
    }
    ```

    Args:
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 120.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.
        sort_by (Union[Unset, str]): 排序方式/Sort by (popular, new) Default: 'popular'.
        industry_id (Union[Unset, str]): 行业ID/Industry ID Default: ''.
        filter_by (Union[Unset, str]): 筛选条件/Filter (new_on_board) Default: ''.

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
            sort_by=sort_by,
            industry_id=industry_id,
            filter_by=filter_by,
        )
    ).parsed
