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
    period: Union[Unset, int] = 7,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    order_by: Union[Unset, str] = "vv",
    country_code: Union[Unset, str] = "US",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["period"] = period

    params["page"] = page

    params["limit"] = limit

    params["order_by"] = order_by

    params["country_code"] = country_code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/get_popular_trends",
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
    period: Union[Unset, int] = 7,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    order_by: Union[Unset, str] = "vv",
    country_code: Union[Unset, str] = "US",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取流行趋势视频/Get popular trend videos

     # [中文]
    ### 用途:
    - 获取指定时间段内的流行趋势视频
    - 了解当前热门内容的特点和趋势
    - 为广告创意提供灵感和参考

    ### 参数:
    - period: 时间范围（天），如7、30天
    - page: 页码，默认1
    - limit: 每页数量，默认10
    - order_by: 排序字段
      - vv: 按观看量排序
      - like: 按点赞数排序
      - comment: 按评论数排序
      - repost: 按转发数排序
    - country_code: 国家代码

    ### 返回内容说明:
    - `pagination`: 分页信息
      - `has_more`: 是否有更多
      - `limit`: 每页数量
      - `page`: 当前页
      - `total_count`: 总数量
    - `videos`: 趋势视频列表
      - `country_code`: 国家代码
      - `cover`: 封面图URL
      - `duration`: 时长（秒）
      - `id`: 视频ID
      - `item_id`: 视频项目ID
      - `item_url`: 视频链接
      - `region`: 地区
      - `title`: 视频标题

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_popular_trends\",
      \"params\": {
        \"period\": \"7\",
        \"page\": \"1\",
        \"limit\": \"10\",
        \"order_by\": \"vv\",
        \"country_code\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"pagination\": {
            \"has_more\": true,
            \"limit\": 10,
            \"page\": 1,
            \"total_count\": 500
          },
          \"videos\": [
            {
              \"country_code\": \"US\",
              \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068c799-us/osAmHI2QkEfCyjJI57DfCFPhVDQJqnImEusfHA~tplv-noop.image\",
              \"duration\": 15,
              \"id\": \"7512918118663081262\",
              \"item_id\": \"7512918118663081262\",
              \"item_url\": \"https://www.tiktok.com/@mnm_pipi/video/7512918118663081262\",
              \"region\": \"United States\",
              \"title\": \"We've lowered MSRP on Rogue and Pathfinder, because Nissan is here for you.\"
            },
            {
              \"country_code\": \"US\",
              \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068c799-us/ocQjW3QOfqt0seM0CA8gWfAqC5I2BO1LIkjQUI~tplv-noop.image\",
              \"duration\": 15,
              \"id\": \"7514018454932835615\",
              \"item_id\": \"7514018454932835615\",
              \"item_url\": \"https://www.tiktok.com/@mnm_pipi/video/7514018454932835615\",
              \"region\": \"United States\",
              \"title\": \"Wanna see something gorgeous? Apple's new look is coming soon. Learn more at
    www.apple.com/os/. #LiquidGlass #WWDC25 #Apple #iOS26 #macOS26\"
            }
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get popular trend videos for specified time period
    - Understand characteristics and trends of current hot content
    - Provide inspiration and reference for ad creativity

    ### Parameters:
    - period: Time period in days, e.g., 7, 30 days
    - page: Page number, default 1
    - limit: Items per page, default 10
    - order_by: Sort field
      - vv: Sort by view count
      - like: Sort by like count
      - comment: Sort by comment count
      - repost: Sort by repost count
    - country_code: Country code

    ### Return Description:
    - `pagination`: Pagination info
      - `has_more`: Has more pages
      - `limit`: Items per page
      - `page`: Current page
      - `total_count`: Total count
    - `videos`: Trend video list
      - `country_code`: Country code
      - `cover`: Cover image URL
      - `duration`: Duration in seconds
      - `id`: Video ID
      - `item_id`: Video item ID
      - `item_url`: Video link
      - `region`: Region name
      - `title`: Video title

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_popular_trends\",
      \"params\": {
        \"period\": \"7\",
        \"page\": \"1\",
        \"limit\": \"10\",
        \"order_by\": \"vv\",
        \"country_code\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"pagination\": {
            \"has_more\": true,
            \"limit\": 10,
            \"page\": 1,
            \"total_count\": 500
          },
          \"videos\": [
            {
              \"country_code\": \"US\",
              \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068c799-us/osAmHI2QkEfCyjJI57DfCFPhVDQJqnImEusfHA~tplv-noop.image\",
              \"duration\": 15,
              \"id\": \"7512918118663081262\",
              \"item_id\": \"7512918118663081262\",
              \"item_url\": \"https://www.tiktok.com/@mnm_pipi/video/7512918118663081262\",
              \"region\": \"United States\",
              \"title\": \"We've lowered MSRP on Rogue and Pathfinder, because Nissan is here for you.\"
            },
            {
              \"country_code\": \"US\",
              \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068c799-us/ocQjW3QOfqt0seM0CA8gWfAqC5I2BO1LIkjQUI~tplv-noop.image\",
              \"duration\": 15,
              \"id\": \"7514018454932835615\",
              \"item_id\": \"7514018454932835615\",
              \"item_url\": \"https://www.tiktok.com/@mnm_pipi/video/7514018454932835615\",
              \"region\": \"United States\",
              \"title\": \"Wanna see something gorgeous? Apple's new look is coming soon. Learn more at
    www.apple.com/os/. #LiquidGlass #WWDC25 #Apple #iOS26 #macOS26\"
            }
          ]
        }
      }
    }
    ```

    Args:
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 7.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 10.
        order_by (Union[Unset, str]): 排序字段/Order by (vv, like, comment, repost) Default: 'vv'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        period=period,
        page=page,
        limit=limit,
        order_by=order_by,
        country_code=country_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    period: Union[Unset, int] = 7,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    order_by: Union[Unset, str] = "vv",
    country_code: Union[Unset, str] = "US",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取流行趋势视频/Get popular trend videos

     # [中文]
    ### 用途:
    - 获取指定时间段内的流行趋势视频
    - 了解当前热门内容的特点和趋势
    - 为广告创意提供灵感和参考

    ### 参数:
    - period: 时间范围（天），如7、30天
    - page: 页码，默认1
    - limit: 每页数量，默认10
    - order_by: 排序字段
      - vv: 按观看量排序
      - like: 按点赞数排序
      - comment: 按评论数排序
      - repost: 按转发数排序
    - country_code: 国家代码

    ### 返回内容说明:
    - `pagination`: 分页信息
      - `has_more`: 是否有更多
      - `limit`: 每页数量
      - `page`: 当前页
      - `total_count`: 总数量
    - `videos`: 趋势视频列表
      - `country_code`: 国家代码
      - `cover`: 封面图URL
      - `duration`: 时长（秒）
      - `id`: 视频ID
      - `item_id`: 视频项目ID
      - `item_url`: 视频链接
      - `region`: 地区
      - `title`: 视频标题

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_popular_trends\",
      \"params\": {
        \"period\": \"7\",
        \"page\": \"1\",
        \"limit\": \"10\",
        \"order_by\": \"vv\",
        \"country_code\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"pagination\": {
            \"has_more\": true,
            \"limit\": 10,
            \"page\": 1,
            \"total_count\": 500
          },
          \"videos\": [
            {
              \"country_code\": \"US\",
              \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068c799-us/osAmHI2QkEfCyjJI57DfCFPhVDQJqnImEusfHA~tplv-noop.image\",
              \"duration\": 15,
              \"id\": \"7512918118663081262\",
              \"item_id\": \"7512918118663081262\",
              \"item_url\": \"https://www.tiktok.com/@mnm_pipi/video/7512918118663081262\",
              \"region\": \"United States\",
              \"title\": \"We've lowered MSRP on Rogue and Pathfinder, because Nissan is here for you.\"
            },
            {
              \"country_code\": \"US\",
              \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068c799-us/ocQjW3QOfqt0seM0CA8gWfAqC5I2BO1LIkjQUI~tplv-noop.image\",
              \"duration\": 15,
              \"id\": \"7514018454932835615\",
              \"item_id\": \"7514018454932835615\",
              \"item_url\": \"https://www.tiktok.com/@mnm_pipi/video/7514018454932835615\",
              \"region\": \"United States\",
              \"title\": \"Wanna see something gorgeous? Apple's new look is coming soon. Learn more at
    www.apple.com/os/. #LiquidGlass #WWDC25 #Apple #iOS26 #macOS26\"
            }
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get popular trend videos for specified time period
    - Understand characteristics and trends of current hot content
    - Provide inspiration and reference for ad creativity

    ### Parameters:
    - period: Time period in days, e.g., 7, 30 days
    - page: Page number, default 1
    - limit: Items per page, default 10
    - order_by: Sort field
      - vv: Sort by view count
      - like: Sort by like count
      - comment: Sort by comment count
      - repost: Sort by repost count
    - country_code: Country code

    ### Return Description:
    - `pagination`: Pagination info
      - `has_more`: Has more pages
      - `limit`: Items per page
      - `page`: Current page
      - `total_count`: Total count
    - `videos`: Trend video list
      - `country_code`: Country code
      - `cover`: Cover image URL
      - `duration`: Duration in seconds
      - `id`: Video ID
      - `item_id`: Video item ID
      - `item_url`: Video link
      - `region`: Region name
      - `title`: Video title

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_popular_trends\",
      \"params\": {
        \"period\": \"7\",
        \"page\": \"1\",
        \"limit\": \"10\",
        \"order_by\": \"vv\",
        \"country_code\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"pagination\": {
            \"has_more\": true,
            \"limit\": 10,
            \"page\": 1,
            \"total_count\": 500
          },
          \"videos\": [
            {
              \"country_code\": \"US\",
              \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068c799-us/osAmHI2QkEfCyjJI57DfCFPhVDQJqnImEusfHA~tplv-noop.image\",
              \"duration\": 15,
              \"id\": \"7512918118663081262\",
              \"item_id\": \"7512918118663081262\",
              \"item_url\": \"https://www.tiktok.com/@mnm_pipi/video/7512918118663081262\",
              \"region\": \"United States\",
              \"title\": \"We've lowered MSRP on Rogue and Pathfinder, because Nissan is here for you.\"
            },
            {
              \"country_code\": \"US\",
              \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068c799-us/ocQjW3QOfqt0seM0CA8gWfAqC5I2BO1LIkjQUI~tplv-noop.image\",
              \"duration\": 15,
              \"id\": \"7514018454932835615\",
              \"item_id\": \"7514018454932835615\",
              \"item_url\": \"https://www.tiktok.com/@mnm_pipi/video/7514018454932835615\",
              \"region\": \"United States\",
              \"title\": \"Wanna see something gorgeous? Apple's new look is coming soon. Learn more at
    www.apple.com/os/. #LiquidGlass #WWDC25 #Apple #iOS26 #macOS26\"
            }
          ]
        }
      }
    }
    ```

    Args:
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 7.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 10.
        order_by (Union[Unset, str]): 排序字段/Order by (vv, like, comment, repost) Default: 'vv'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        period=period,
        page=page,
        limit=limit,
        order_by=order_by,
        country_code=country_code,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    period: Union[Unset, int] = 7,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    order_by: Union[Unset, str] = "vv",
    country_code: Union[Unset, str] = "US",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取流行趋势视频/Get popular trend videos

     # [中文]
    ### 用途:
    - 获取指定时间段内的流行趋势视频
    - 了解当前热门内容的特点和趋势
    - 为广告创意提供灵感和参考

    ### 参数:
    - period: 时间范围（天），如7、30天
    - page: 页码，默认1
    - limit: 每页数量，默认10
    - order_by: 排序字段
      - vv: 按观看量排序
      - like: 按点赞数排序
      - comment: 按评论数排序
      - repost: 按转发数排序
    - country_code: 国家代码

    ### 返回内容说明:
    - `pagination`: 分页信息
      - `has_more`: 是否有更多
      - `limit`: 每页数量
      - `page`: 当前页
      - `total_count`: 总数量
    - `videos`: 趋势视频列表
      - `country_code`: 国家代码
      - `cover`: 封面图URL
      - `duration`: 时长（秒）
      - `id`: 视频ID
      - `item_id`: 视频项目ID
      - `item_url`: 视频链接
      - `region`: 地区
      - `title`: 视频标题

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_popular_trends\",
      \"params\": {
        \"period\": \"7\",
        \"page\": \"1\",
        \"limit\": \"10\",
        \"order_by\": \"vv\",
        \"country_code\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"pagination\": {
            \"has_more\": true,
            \"limit\": 10,
            \"page\": 1,
            \"total_count\": 500
          },
          \"videos\": [
            {
              \"country_code\": \"US\",
              \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068c799-us/osAmHI2QkEfCyjJI57DfCFPhVDQJqnImEusfHA~tplv-noop.image\",
              \"duration\": 15,
              \"id\": \"7512918118663081262\",
              \"item_id\": \"7512918118663081262\",
              \"item_url\": \"https://www.tiktok.com/@mnm_pipi/video/7512918118663081262\",
              \"region\": \"United States\",
              \"title\": \"We've lowered MSRP on Rogue and Pathfinder, because Nissan is here for you.\"
            },
            {
              \"country_code\": \"US\",
              \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068c799-us/ocQjW3QOfqt0seM0CA8gWfAqC5I2BO1LIkjQUI~tplv-noop.image\",
              \"duration\": 15,
              \"id\": \"7514018454932835615\",
              \"item_id\": \"7514018454932835615\",
              \"item_url\": \"https://www.tiktok.com/@mnm_pipi/video/7514018454932835615\",
              \"region\": \"United States\",
              \"title\": \"Wanna see something gorgeous? Apple's new look is coming soon. Learn more at
    www.apple.com/os/. #LiquidGlass #WWDC25 #Apple #iOS26 #macOS26\"
            }
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get popular trend videos for specified time period
    - Understand characteristics and trends of current hot content
    - Provide inspiration and reference for ad creativity

    ### Parameters:
    - period: Time period in days, e.g., 7, 30 days
    - page: Page number, default 1
    - limit: Items per page, default 10
    - order_by: Sort field
      - vv: Sort by view count
      - like: Sort by like count
      - comment: Sort by comment count
      - repost: Sort by repost count
    - country_code: Country code

    ### Return Description:
    - `pagination`: Pagination info
      - `has_more`: Has more pages
      - `limit`: Items per page
      - `page`: Current page
      - `total_count`: Total count
    - `videos`: Trend video list
      - `country_code`: Country code
      - `cover`: Cover image URL
      - `duration`: Duration in seconds
      - `id`: Video ID
      - `item_id`: Video item ID
      - `item_url`: Video link
      - `region`: Region name
      - `title`: Video title

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_popular_trends\",
      \"params\": {
        \"period\": \"7\",
        \"page\": \"1\",
        \"limit\": \"10\",
        \"order_by\": \"vv\",
        \"country_code\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"pagination\": {
            \"has_more\": true,
            \"limit\": 10,
            \"page\": 1,
            \"total_count\": 500
          },
          \"videos\": [
            {
              \"country_code\": \"US\",
              \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068c799-us/osAmHI2QkEfCyjJI57DfCFPhVDQJqnImEusfHA~tplv-noop.image\",
              \"duration\": 15,
              \"id\": \"7512918118663081262\",
              \"item_id\": \"7512918118663081262\",
              \"item_url\": \"https://www.tiktok.com/@mnm_pipi/video/7512918118663081262\",
              \"region\": \"United States\",
              \"title\": \"We've lowered MSRP on Rogue and Pathfinder, because Nissan is here for you.\"
            },
            {
              \"country_code\": \"US\",
              \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068c799-us/ocQjW3QOfqt0seM0CA8gWfAqC5I2BO1LIkjQUI~tplv-noop.image\",
              \"duration\": 15,
              \"id\": \"7514018454932835615\",
              \"item_id\": \"7514018454932835615\",
              \"item_url\": \"https://www.tiktok.com/@mnm_pipi/video/7514018454932835615\",
              \"region\": \"United States\",
              \"title\": \"Wanna see something gorgeous? Apple's new look is coming soon. Learn more at
    www.apple.com/os/. #LiquidGlass #WWDC25 #Apple #iOS26 #macOS26\"
            }
          ]
        }
      }
    }
    ```

    Args:
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 7.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 10.
        order_by (Union[Unset, str]): 排序字段/Order by (vv, like, comment, repost) Default: 'vv'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        period=period,
        page=page,
        limit=limit,
        order_by=order_by,
        country_code=country_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    period: Union[Unset, int] = 7,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    order_by: Union[Unset, str] = "vv",
    country_code: Union[Unset, str] = "US",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取流行趋势视频/Get popular trend videos

     # [中文]
    ### 用途:
    - 获取指定时间段内的流行趋势视频
    - 了解当前热门内容的特点和趋势
    - 为广告创意提供灵感和参考

    ### 参数:
    - period: 时间范围（天），如7、30天
    - page: 页码，默认1
    - limit: 每页数量，默认10
    - order_by: 排序字段
      - vv: 按观看量排序
      - like: 按点赞数排序
      - comment: 按评论数排序
      - repost: 按转发数排序
    - country_code: 国家代码

    ### 返回内容说明:
    - `pagination`: 分页信息
      - `has_more`: 是否有更多
      - `limit`: 每页数量
      - `page`: 当前页
      - `total_count`: 总数量
    - `videos`: 趋势视频列表
      - `country_code`: 国家代码
      - `cover`: 封面图URL
      - `duration`: 时长（秒）
      - `id`: 视频ID
      - `item_id`: 视频项目ID
      - `item_url`: 视频链接
      - `region`: 地区
      - `title`: 视频标题

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_popular_trends\",
      \"params\": {
        \"period\": \"7\",
        \"page\": \"1\",
        \"limit\": \"10\",
        \"order_by\": \"vv\",
        \"country_code\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"pagination\": {
            \"has_more\": true,
            \"limit\": 10,
            \"page\": 1,
            \"total_count\": 500
          },
          \"videos\": [
            {
              \"country_code\": \"US\",
              \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068c799-us/osAmHI2QkEfCyjJI57DfCFPhVDQJqnImEusfHA~tplv-noop.image\",
              \"duration\": 15,
              \"id\": \"7512918118663081262\",
              \"item_id\": \"7512918118663081262\",
              \"item_url\": \"https://www.tiktok.com/@mnm_pipi/video/7512918118663081262\",
              \"region\": \"United States\",
              \"title\": \"We've lowered MSRP on Rogue and Pathfinder, because Nissan is here for you.\"
            },
            {
              \"country_code\": \"US\",
              \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068c799-us/ocQjW3QOfqt0seM0CA8gWfAqC5I2BO1LIkjQUI~tplv-noop.image\",
              \"duration\": 15,
              \"id\": \"7514018454932835615\",
              \"item_id\": \"7514018454932835615\",
              \"item_url\": \"https://www.tiktok.com/@mnm_pipi/video/7514018454932835615\",
              \"region\": \"United States\",
              \"title\": \"Wanna see something gorgeous? Apple's new look is coming soon. Learn more at
    www.apple.com/os/. #LiquidGlass #WWDC25 #Apple #iOS26 #macOS26\"
            }
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get popular trend videos for specified time period
    - Understand characteristics and trends of current hot content
    - Provide inspiration and reference for ad creativity

    ### Parameters:
    - period: Time period in days, e.g., 7, 30 days
    - page: Page number, default 1
    - limit: Items per page, default 10
    - order_by: Sort field
      - vv: Sort by view count
      - like: Sort by like count
      - comment: Sort by comment count
      - repost: Sort by repost count
    - country_code: Country code

    ### Return Description:
    - `pagination`: Pagination info
      - `has_more`: Has more pages
      - `limit`: Items per page
      - `page`: Current page
      - `total_count`: Total count
    - `videos`: Trend video list
      - `country_code`: Country code
      - `cover`: Cover image URL
      - `duration`: Duration in seconds
      - `id`: Video ID
      - `item_id`: Video item ID
      - `item_url`: Video link
      - `region`: Region name
      - `title`: Video title

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_popular_trends\",
      \"params\": {
        \"period\": \"7\",
        \"page\": \"1\",
        \"limit\": \"10\",
        \"order_by\": \"vv\",
        \"country_code\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"pagination\": {
            \"has_more\": true,
            \"limit\": 10,
            \"page\": 1,
            \"total_count\": 500
          },
          \"videos\": [
            {
              \"country_code\": \"US\",
              \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068c799-us/osAmHI2QkEfCyjJI57DfCFPhVDQJqnImEusfHA~tplv-noop.image\",
              \"duration\": 15,
              \"id\": \"7512918118663081262\",
              \"item_id\": \"7512918118663081262\",
              \"item_url\": \"https://www.tiktok.com/@mnm_pipi/video/7512918118663081262\",
              \"region\": \"United States\",
              \"title\": \"We've lowered MSRP on Rogue and Pathfinder, because Nissan is here for you.\"
            },
            {
              \"country_code\": \"US\",
              \"cover\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068c799-us/ocQjW3QOfqt0seM0CA8gWfAqC5I2BO1LIkjQUI~tplv-noop.image\",
              \"duration\": 15,
              \"id\": \"7514018454932835615\",
              \"item_id\": \"7514018454932835615\",
              \"item_url\": \"https://www.tiktok.com/@mnm_pipi/video/7514018454932835615\",
              \"region\": \"United States\",
              \"title\": \"Wanna see something gorgeous? Apple's new look is coming soon. Learn more at
    www.apple.com/os/. #LiquidGlass #WWDC25 #Apple #iOS26 #macOS26\"
            }
          ]
        }
      }
    }
    ```

    Args:
        period (Union[Unset, int]): 时间范围（天）/Time period (days) Default: 7.
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 10.
        order_by (Union[Unset, str]): 排序字段/Order by (vv, like, comment, repost) Default: 'vv'.
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
            period=period,
            page=page,
            limit=limit,
            order_by=order_by,
            country_code=country_code,
        )
    ).parsed
