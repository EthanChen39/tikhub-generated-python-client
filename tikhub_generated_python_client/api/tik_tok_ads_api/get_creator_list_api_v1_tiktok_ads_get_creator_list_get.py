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
    sort_by: Union[Unset, str] = "follower",
    creator_country: Union[Unset, str] = "US",
    audience_country: Union[Unset, str] = "",
    audience_count: Union[Unset, int] = 0,
    keyword: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params["sort_by"] = sort_by

    params["creator_country"] = creator_country

    params["audience_country"] = audience_country

    params["audience_count"] = audience_count

    params["keyword"] = keyword

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/get_creator_list",
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
    sort_by: Union[Unset, str] = "follower",
    creator_country: Union[Unset, str] = "US",
    audience_country: Union[Unset, str] = "",
    audience_count: Union[Unset, int] = 0,
    keyword: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者列表/Get creator list

     # [中文]
    ### 用途:
    - 获取符合条件的创作者列表，包括粉丝数、互动率等数据
    - 发现高质量的广告合作创作者
    - 分析不同类型创作者的表现和特点

    ### 参数:
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - sort_by: 排序方式
      - follower: 按粉丝数排序
      - engagement: 按互动率排序
      - avg_views: 按平均观看量排序
    - creator_country: 创作者所在国家
    - audience_country: 受众所在国家（可选）
    - audience_count: 受众数量筛选（可选）

    ### 返回内容说明:
    - `creators`: 创作者列表
      - `tcm_id`: TCM ID
      - `user_id`: 用户ID
      - `nick_name`: 昵称
      - `avatar_url`: 头像URL
      - `country_code`: 国家代码
      - `follower_cnt`: 粉丝数
      - `liked_cnt`: 获赞总数
      - `tt_link`: TikTok链接
      - `tcm_link`: TCM链接
      - `items`: 作品列表
        - `item_id`: 作品ID
        - `cover_url`: 封面URL
        - `tt_link`: TikTok链接
        - `vv`: 观看量
        - `liked_cnt`: 点赞数
        - `create_time`: 创建时间
    - `pagination`: 分页信息
      - `page`: 当前页
      - `size`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_creator_list\",
      \"params\": {
        \"page\": \"1\",
        \"limit\": \"20\",
        \"sort_by\": \"follower\",
        \"creator_country\": \"US\",
        \"audience_country\": \"\",
        \"audience_count\": \"0\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"creators\": [
            {
              \"tcm_id\": \"7414477993612935173\",
              \"user_id\": \"62133858422239232\",
              \"nick_name\": \"Fernanda\",
              \"avatar_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-
    avt-0068/200b649d30f76f1238d771f4aff51ee1~tplv-tiktokx-cropcenter:100:100.png\",
              \"country_code\": \"US\",
              \"follower_cnt\": 9135515,
              \"liked_cnt\": 668294555,
              \"tt_link\": \"https://www.tiktok.com/@ferchugimenez\",
              \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/7414477993612935173\",
              \"items\": [
                {
                  \"item_id\": \"7444674312784645432\",
                  \"cover_url\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068/oQIBhn2EeBMUWQR5wVQACFEBtlDxgUDdAfoB8J~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7444674312784645432\",
                  \"vv\": 13733332,
                  \"liked_cnt\": 516217,
                  \"create_time\": 1733348322
                }
              ]
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 459,
            \"has_more\": true
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get a list of creators matching criteria, including follower count, engagement rate, etc.
    - Discover high-quality creators for ad collaboration
    - Analyze performance and characteristics of different creator types

    ### Parameters:
    - page: Page number, default 1
    - limit: Items per page, default 20
    - sort_by: Sorting method
      - follower: Sort by follower count
      - engagement: Sort by engagement rate
      - avg_views: Sort by average views
    - creator_country: Creator's country
    - audience_country: Audience country (optional)
    - audience_count: Audience count filter (optional)

    ### Return Description:
    - `creators`: Creator list
      - `tcm_id`: TikTok Creator Marketplace ID
      - `user_id`: User ID
      - `nick_name`: Nickname
      - `avatar_url`: Avatar URL
      - `country_code`: Country code
      - `follower_cnt`: Follower count
      - `liked_cnt`: Total likes count
      - `tt_link`: TikTok profile link
      - `tcm_link`: Creator marketplace link
      - `items`: Video list
        - `item_id`: Video ID
        - `cover_url`: Cover image URL
        - `tt_link`: Video link
        - `vv`: View count
        - `liked_cnt`: Like count
        - `create_time`: Creation timestamp
    - `pagination`: Pagination info
      - `page`: Current page
      - `size`: Items per page
      - `total`: Total count
      - `has_more`: Has more pages

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_creator_list\",
      \"params\": {
        \"page\": \"1\",
        \"limit\": \"20\",
        \"sort_by\": \"follower\",
        \"creator_country\": \"US\",
        \"audience_country\": \"\",
        \"audience_count\": \"0\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"creators\": [
            {
              \"tcm_id\": \"7414477993612935173\",
              \"user_id\": \"62133858422239232\",
              \"nick_name\": \"Fernanda\",
              \"avatar_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-
    avt-0068/200b649d30f76f1238d771f4aff51ee1~tplv-tiktokx-cropcenter:100:100.png\",
              \"country_code\": \"US\",
              \"follower_cnt\": 9135515,
              \"liked_cnt\": 668294555,
              \"tt_link\": \"https://www.tiktok.com/@ferchugimenez\",
              \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/7414477993612935173\",
              \"items\": [
                {
                  \"item_id\": \"7444674312784645432\",
                  \"cover_url\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068/oQIBhn2EeBMUWQR5wVQACFEBtlDxgUDdAfoB8J~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7444674312784645432\",
                  \"vv\": 13733332,
                  \"liked_cnt\": 516217,
                  \"create_time\": 1733348322
                }
              ]
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 459,
            \"has_more\": true
          }
        }
      }
    }
    ```

    Args:
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        sort_by (Union[Unset, str]): 排序方式/Sort by (follower, engagement, avg_views) Default:
            'follower'.
        creator_country (Union[Unset, str]): 创作者国家/Creator country Default: 'US'.
        audience_country (Union[Unset, str]): 受众国家/Audience country Default: ''.
        audience_count (Union[Unset, int]): 受众数量筛选/Audience count filter Default: 0.
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
        sort_by=sort_by,
        creator_country=creator_country,
        audience_country=audience_country,
        audience_count=audience_count,
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
    sort_by: Union[Unset, str] = "follower",
    creator_country: Union[Unset, str] = "US",
    audience_country: Union[Unset, str] = "",
    audience_count: Union[Unset, int] = 0,
    keyword: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者列表/Get creator list

     # [中文]
    ### 用途:
    - 获取符合条件的创作者列表，包括粉丝数、互动率等数据
    - 发现高质量的广告合作创作者
    - 分析不同类型创作者的表现和特点

    ### 参数:
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - sort_by: 排序方式
      - follower: 按粉丝数排序
      - engagement: 按互动率排序
      - avg_views: 按平均观看量排序
    - creator_country: 创作者所在国家
    - audience_country: 受众所在国家（可选）
    - audience_count: 受众数量筛选（可选）

    ### 返回内容说明:
    - `creators`: 创作者列表
      - `tcm_id`: TCM ID
      - `user_id`: 用户ID
      - `nick_name`: 昵称
      - `avatar_url`: 头像URL
      - `country_code`: 国家代码
      - `follower_cnt`: 粉丝数
      - `liked_cnt`: 获赞总数
      - `tt_link`: TikTok链接
      - `tcm_link`: TCM链接
      - `items`: 作品列表
        - `item_id`: 作品ID
        - `cover_url`: 封面URL
        - `tt_link`: TikTok链接
        - `vv`: 观看量
        - `liked_cnt`: 点赞数
        - `create_time`: 创建时间
    - `pagination`: 分页信息
      - `page`: 当前页
      - `size`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_creator_list\",
      \"params\": {
        \"page\": \"1\",
        \"limit\": \"20\",
        \"sort_by\": \"follower\",
        \"creator_country\": \"US\",
        \"audience_country\": \"\",
        \"audience_count\": \"0\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"creators\": [
            {
              \"tcm_id\": \"7414477993612935173\",
              \"user_id\": \"62133858422239232\",
              \"nick_name\": \"Fernanda\",
              \"avatar_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-
    avt-0068/200b649d30f76f1238d771f4aff51ee1~tplv-tiktokx-cropcenter:100:100.png\",
              \"country_code\": \"US\",
              \"follower_cnt\": 9135515,
              \"liked_cnt\": 668294555,
              \"tt_link\": \"https://www.tiktok.com/@ferchugimenez\",
              \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/7414477993612935173\",
              \"items\": [
                {
                  \"item_id\": \"7444674312784645432\",
                  \"cover_url\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068/oQIBhn2EeBMUWQR5wVQACFEBtlDxgUDdAfoB8J~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7444674312784645432\",
                  \"vv\": 13733332,
                  \"liked_cnt\": 516217,
                  \"create_time\": 1733348322
                }
              ]
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 459,
            \"has_more\": true
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get a list of creators matching criteria, including follower count, engagement rate, etc.
    - Discover high-quality creators for ad collaboration
    - Analyze performance and characteristics of different creator types

    ### Parameters:
    - page: Page number, default 1
    - limit: Items per page, default 20
    - sort_by: Sorting method
      - follower: Sort by follower count
      - engagement: Sort by engagement rate
      - avg_views: Sort by average views
    - creator_country: Creator's country
    - audience_country: Audience country (optional)
    - audience_count: Audience count filter (optional)

    ### Return Description:
    - `creators`: Creator list
      - `tcm_id`: TikTok Creator Marketplace ID
      - `user_id`: User ID
      - `nick_name`: Nickname
      - `avatar_url`: Avatar URL
      - `country_code`: Country code
      - `follower_cnt`: Follower count
      - `liked_cnt`: Total likes count
      - `tt_link`: TikTok profile link
      - `tcm_link`: Creator marketplace link
      - `items`: Video list
        - `item_id`: Video ID
        - `cover_url`: Cover image URL
        - `tt_link`: Video link
        - `vv`: View count
        - `liked_cnt`: Like count
        - `create_time`: Creation timestamp
    - `pagination`: Pagination info
      - `page`: Current page
      - `size`: Items per page
      - `total`: Total count
      - `has_more`: Has more pages

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_creator_list\",
      \"params\": {
        \"page\": \"1\",
        \"limit\": \"20\",
        \"sort_by\": \"follower\",
        \"creator_country\": \"US\",
        \"audience_country\": \"\",
        \"audience_count\": \"0\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"creators\": [
            {
              \"tcm_id\": \"7414477993612935173\",
              \"user_id\": \"62133858422239232\",
              \"nick_name\": \"Fernanda\",
              \"avatar_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-
    avt-0068/200b649d30f76f1238d771f4aff51ee1~tplv-tiktokx-cropcenter:100:100.png\",
              \"country_code\": \"US\",
              \"follower_cnt\": 9135515,
              \"liked_cnt\": 668294555,
              \"tt_link\": \"https://www.tiktok.com/@ferchugimenez\",
              \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/7414477993612935173\",
              \"items\": [
                {
                  \"item_id\": \"7444674312784645432\",
                  \"cover_url\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068/oQIBhn2EeBMUWQR5wVQACFEBtlDxgUDdAfoB8J~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7444674312784645432\",
                  \"vv\": 13733332,
                  \"liked_cnt\": 516217,
                  \"create_time\": 1733348322
                }
              ]
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 459,
            \"has_more\": true
          }
        }
      }
    }
    ```

    Args:
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        sort_by (Union[Unset, str]): 排序方式/Sort by (follower, engagement, avg_views) Default:
            'follower'.
        creator_country (Union[Unset, str]): 创作者国家/Creator country Default: 'US'.
        audience_country (Union[Unset, str]): 受众国家/Audience country Default: ''.
        audience_count (Union[Unset, int]): 受众数量筛选/Audience count filter Default: 0.
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
        sort_by=sort_by,
        creator_country=creator_country,
        audience_country=audience_country,
        audience_count=audience_count,
        keyword=keyword,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    sort_by: Union[Unset, str] = "follower",
    creator_country: Union[Unset, str] = "US",
    audience_country: Union[Unset, str] = "",
    audience_count: Union[Unset, int] = 0,
    keyword: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者列表/Get creator list

     # [中文]
    ### 用途:
    - 获取符合条件的创作者列表，包括粉丝数、互动率等数据
    - 发现高质量的广告合作创作者
    - 分析不同类型创作者的表现和特点

    ### 参数:
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - sort_by: 排序方式
      - follower: 按粉丝数排序
      - engagement: 按互动率排序
      - avg_views: 按平均观看量排序
    - creator_country: 创作者所在国家
    - audience_country: 受众所在国家（可选）
    - audience_count: 受众数量筛选（可选）

    ### 返回内容说明:
    - `creators`: 创作者列表
      - `tcm_id`: TCM ID
      - `user_id`: 用户ID
      - `nick_name`: 昵称
      - `avatar_url`: 头像URL
      - `country_code`: 国家代码
      - `follower_cnt`: 粉丝数
      - `liked_cnt`: 获赞总数
      - `tt_link`: TikTok链接
      - `tcm_link`: TCM链接
      - `items`: 作品列表
        - `item_id`: 作品ID
        - `cover_url`: 封面URL
        - `tt_link`: TikTok链接
        - `vv`: 观看量
        - `liked_cnt`: 点赞数
        - `create_time`: 创建时间
    - `pagination`: 分页信息
      - `page`: 当前页
      - `size`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_creator_list\",
      \"params\": {
        \"page\": \"1\",
        \"limit\": \"20\",
        \"sort_by\": \"follower\",
        \"creator_country\": \"US\",
        \"audience_country\": \"\",
        \"audience_count\": \"0\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"creators\": [
            {
              \"tcm_id\": \"7414477993612935173\",
              \"user_id\": \"62133858422239232\",
              \"nick_name\": \"Fernanda\",
              \"avatar_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-
    avt-0068/200b649d30f76f1238d771f4aff51ee1~tplv-tiktokx-cropcenter:100:100.png\",
              \"country_code\": \"US\",
              \"follower_cnt\": 9135515,
              \"liked_cnt\": 668294555,
              \"tt_link\": \"https://www.tiktok.com/@ferchugimenez\",
              \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/7414477993612935173\",
              \"items\": [
                {
                  \"item_id\": \"7444674312784645432\",
                  \"cover_url\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068/oQIBhn2EeBMUWQR5wVQACFEBtlDxgUDdAfoB8J~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7444674312784645432\",
                  \"vv\": 13733332,
                  \"liked_cnt\": 516217,
                  \"create_time\": 1733348322
                }
              ]
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 459,
            \"has_more\": true
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get a list of creators matching criteria, including follower count, engagement rate, etc.
    - Discover high-quality creators for ad collaboration
    - Analyze performance and characteristics of different creator types

    ### Parameters:
    - page: Page number, default 1
    - limit: Items per page, default 20
    - sort_by: Sorting method
      - follower: Sort by follower count
      - engagement: Sort by engagement rate
      - avg_views: Sort by average views
    - creator_country: Creator's country
    - audience_country: Audience country (optional)
    - audience_count: Audience count filter (optional)

    ### Return Description:
    - `creators`: Creator list
      - `tcm_id`: TikTok Creator Marketplace ID
      - `user_id`: User ID
      - `nick_name`: Nickname
      - `avatar_url`: Avatar URL
      - `country_code`: Country code
      - `follower_cnt`: Follower count
      - `liked_cnt`: Total likes count
      - `tt_link`: TikTok profile link
      - `tcm_link`: Creator marketplace link
      - `items`: Video list
        - `item_id`: Video ID
        - `cover_url`: Cover image URL
        - `tt_link`: Video link
        - `vv`: View count
        - `liked_cnt`: Like count
        - `create_time`: Creation timestamp
    - `pagination`: Pagination info
      - `page`: Current page
      - `size`: Items per page
      - `total`: Total count
      - `has_more`: Has more pages

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_creator_list\",
      \"params\": {
        \"page\": \"1\",
        \"limit\": \"20\",
        \"sort_by\": \"follower\",
        \"creator_country\": \"US\",
        \"audience_country\": \"\",
        \"audience_count\": \"0\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"creators\": [
            {
              \"tcm_id\": \"7414477993612935173\",
              \"user_id\": \"62133858422239232\",
              \"nick_name\": \"Fernanda\",
              \"avatar_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-
    avt-0068/200b649d30f76f1238d771f4aff51ee1~tplv-tiktokx-cropcenter:100:100.png\",
              \"country_code\": \"US\",
              \"follower_cnt\": 9135515,
              \"liked_cnt\": 668294555,
              \"tt_link\": \"https://www.tiktok.com/@ferchugimenez\",
              \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/7414477993612935173\",
              \"items\": [
                {
                  \"item_id\": \"7444674312784645432\",
                  \"cover_url\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068/oQIBhn2EeBMUWQR5wVQACFEBtlDxgUDdAfoB8J~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7444674312784645432\",
                  \"vv\": 13733332,
                  \"liked_cnt\": 516217,
                  \"create_time\": 1733348322
                }
              ]
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 459,
            \"has_more\": true
          }
        }
      }
    }
    ```

    Args:
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        sort_by (Union[Unset, str]): 排序方式/Sort by (follower, engagement, avg_views) Default:
            'follower'.
        creator_country (Union[Unset, str]): 创作者国家/Creator country Default: 'US'.
        audience_country (Union[Unset, str]): 受众国家/Audience country Default: ''.
        audience_count (Union[Unset, int]): 受众数量筛选/Audience count filter Default: 0.
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
        sort_by=sort_by,
        creator_country=creator_country,
        audience_country=audience_country,
        audience_count=audience_count,
        keyword=keyword,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    sort_by: Union[Unset, str] = "follower",
    creator_country: Union[Unset, str] = "US",
    audience_country: Union[Unset, str] = "",
    audience_count: Union[Unset, int] = 0,
    keyword: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者列表/Get creator list

     # [中文]
    ### 用途:
    - 获取符合条件的创作者列表，包括粉丝数、互动率等数据
    - 发现高质量的广告合作创作者
    - 分析不同类型创作者的表现和特点

    ### 参数:
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - sort_by: 排序方式
      - follower: 按粉丝数排序
      - engagement: 按互动率排序
      - avg_views: 按平均观看量排序
    - creator_country: 创作者所在国家
    - audience_country: 受众所在国家（可选）
    - audience_count: 受众数量筛选（可选）

    ### 返回内容说明:
    - `creators`: 创作者列表
      - `tcm_id`: TCM ID
      - `user_id`: 用户ID
      - `nick_name`: 昵称
      - `avatar_url`: 头像URL
      - `country_code`: 国家代码
      - `follower_cnt`: 粉丝数
      - `liked_cnt`: 获赞总数
      - `tt_link`: TikTok链接
      - `tcm_link`: TCM链接
      - `items`: 作品列表
        - `item_id`: 作品ID
        - `cover_url`: 封面URL
        - `tt_link`: TikTok链接
        - `vv`: 观看量
        - `liked_cnt`: 点赞数
        - `create_time`: 创建时间
    - `pagination`: 分页信息
      - `page`: 当前页
      - `size`: 每页数量
      - `total`: 总数量
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_creator_list\",
      \"params\": {
        \"page\": \"1\",
        \"limit\": \"20\",
        \"sort_by\": \"follower\",
        \"creator_country\": \"US\",
        \"audience_country\": \"\",
        \"audience_count\": \"0\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"creators\": [
            {
              \"tcm_id\": \"7414477993612935173\",
              \"user_id\": \"62133858422239232\",
              \"nick_name\": \"Fernanda\",
              \"avatar_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-
    avt-0068/200b649d30f76f1238d771f4aff51ee1~tplv-tiktokx-cropcenter:100:100.png\",
              \"country_code\": \"US\",
              \"follower_cnt\": 9135515,
              \"liked_cnt\": 668294555,
              \"tt_link\": \"https://www.tiktok.com/@ferchugimenez\",
              \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/7414477993612935173\",
              \"items\": [
                {
                  \"item_id\": \"7444674312784645432\",
                  \"cover_url\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068/oQIBhn2EeBMUWQR5wVQACFEBtlDxgUDdAfoB8J~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7444674312784645432\",
                  \"vv\": 13733332,
                  \"liked_cnt\": 516217,
                  \"create_time\": 1733348322
                }
              ]
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 459,
            \"has_more\": true
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get a list of creators matching criteria, including follower count, engagement rate, etc.
    - Discover high-quality creators for ad collaboration
    - Analyze performance and characteristics of different creator types

    ### Parameters:
    - page: Page number, default 1
    - limit: Items per page, default 20
    - sort_by: Sorting method
      - follower: Sort by follower count
      - engagement: Sort by engagement rate
      - avg_views: Sort by average views
    - creator_country: Creator's country
    - audience_country: Audience country (optional)
    - audience_count: Audience count filter (optional)

    ### Return Description:
    - `creators`: Creator list
      - `tcm_id`: TikTok Creator Marketplace ID
      - `user_id`: User ID
      - `nick_name`: Nickname
      - `avatar_url`: Avatar URL
      - `country_code`: Country code
      - `follower_cnt`: Follower count
      - `liked_cnt`: Total likes count
      - `tt_link`: TikTok profile link
      - `tcm_link`: Creator marketplace link
      - `items`: Video list
        - `item_id`: Video ID
        - `cover_url`: Cover image URL
        - `tt_link`: Video link
        - `vv`: View count
        - `liked_cnt`: Like count
        - `create_time`: Creation timestamp
    - `pagination`: Pagination info
      - `page`: Current page
      - `size`: Items per page
      - `total`: Total count
      - `has_more`: Has more pages

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_creator_list\",
      \"params\": {
        \"page\": \"1\",
        \"limit\": \"20\",
        \"sort_by\": \"follower\",
        \"creator_country\": \"US\",
        \"audience_country\": \"\",
        \"audience_count\": \"0\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"creators\": [
            {
              \"tcm_id\": \"7414477993612935173\",
              \"user_id\": \"62133858422239232\",
              \"nick_name\": \"Fernanda\",
              \"avatar_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-
    avt-0068/200b649d30f76f1238d771f4aff51ee1~tplv-tiktokx-cropcenter:100:100.png\",
              \"country_code\": \"US\",
              \"follower_cnt\": 9135515,
              \"liked_cnt\": 668294555,
              \"tt_link\": \"https://www.tiktok.com/@ferchugimenez\",
              \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/7414477993612935173\",
              \"items\": [
                {
                  \"item_id\": \"7444674312784645432\",
                  \"cover_url\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068/oQIBhn2EeBMUWQR5wVQACFEBtlDxgUDdAfoB8J~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7444674312784645432\",
                  \"vv\": 13733332,
                  \"liked_cnt\": 516217,
                  \"create_time\": 1733348322
                }
              ]
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 459,
            \"has_more\": true
          }
        }
      }
    }
    ```

    Args:
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        sort_by (Union[Unset, str]): 排序方式/Sort by (follower, engagement, avg_views) Default:
            'follower'.
        creator_country (Union[Unset, str]): 创作者国家/Creator country Default: 'US'.
        audience_country (Union[Unset, str]): 受众国家/Audience country Default: ''.
        audience_count (Union[Unset, int]): 受众数量筛选/Audience count filter Default: 0.
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
            sort_by=sort_by,
            creator_country=creator_country,
            audience_country=audience_country,
            audience_count=audience_count,
            keyword=keyword,
        )
    ).parsed
