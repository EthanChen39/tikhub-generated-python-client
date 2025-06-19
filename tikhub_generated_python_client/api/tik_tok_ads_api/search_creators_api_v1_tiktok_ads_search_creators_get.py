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
    keyword: str,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    sort_by: Union[Unset, str] = "follower",
    creator_country: Union[Unset, str] = "US",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["page"] = page

    params["limit"] = limit

    params["sort_by"] = sort_by

    params["creator_country"] = creator_country

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/search_creators",
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
    keyword: str,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    sort_by: Union[Unset, str] = "follower",
    creator_country: Union[Unset, str] = "US",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索创作者/Search creators

     # [中文]
    ### 用途:
    - 通过关键词搜索创作者
    - 快速找到特定领域或名称的创作者
    - 支持按粉丝数或平均观看量排序

    ### 参数:
    - keyword: 搜索关键词，可以是用户名、昵称的一部分
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - sort_by: 排序方式
      - follower: 按粉丝数排序
      - avg_views: 按平均观看量排序
    - creator_country: 创作者所在国家

    ### 返回内容说明:
    - `creators`: 创作者列表
      - `tcm_id`: 创作者市场ID
      - `user_id`: 用户ID
      - `nick_name`: 昵称
      - `avatar_url`: 头像URL
      - `country_code`: 国家代码
      - `follower_cnt`: 粉丝数
      - `liked_cnt`: 总点赞数
      - `tt_link`: TikTok个人主页链接
      - `tcm_link`: 创作者市场链接
      - `items`: 作品列表
        - `item_id`: 作品ID
        - `cover_url`: 封面URL
        - `tt_link`: 作品链接
        - `vv`: 观看量
        - `liked_cnt`: 点赞数
        - `create_time`: 创建时间戳
    - `pagination`: 分页信息
      - `page`: 当前页码
      - `size`: 每页数量
      - `total`: 总数
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_creators\",
      \"params\": {
        \"keyword\": \"jo\",
        \"page\": \"1\",
        \"limit\": \"20\",
        \"sort_by\": \"follower\",
        \"creator_country\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"creators\": [
            {
              \"tcm_id\": \"6894787532572065797\",
              \"user_id\": \"6684747467718820870\",
              \"nick_name\": \"Josh Zilberberg\",
              \"avatar_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-
    avt-0068/f11c960c637601225c29d6e7849069eb~tplv-tiktokx-cropcenter:100:100.png\",
              \"country_code\": \"US\",
              \"follower_cnt\": 3048368,
              \"liked_cnt\": 130131619,
              \"tt_link\": \"https://www.tiktok.com/@josh.zilberberg\",
              \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/6894787532572065797\",
              \"items\": [
                {
                  \"item_id\": \"7406005139112283397\",
                  \"cover_url\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068/6e0c79311c2b49758674ae64721c495b_1724344961~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7406005139112283397\",
                  \"vv\": 3266905,
                  \"liked_cnt\": 4057,
                  \"create_time\": 1724344950
                }
              ]
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 6,
            \"has_more\": false
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Search creators by keyword
    - Quickly find creators in specific fields or with specific names
    - Support sorting by follower count or average views

    ### Parameters:
    - keyword: Search keyword, can be part of username or nickname
    - page: Page number, default 1
    - limit: Items per page, default 20
    - sort_by: Sorting method
      - follower: Sort by follower count
      - avg_views: Sort by average views
    - creator_country: Creator's country

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
      \"router\": \"/api/v1/tiktok/ads/search_creators\",
      \"params\": {
        \"keyword\": \"jo\",
        \"page\": \"1\",
        \"limit\": \"20\",
        \"sort_by\": \"follower\",
        \"creator_country\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"creators\": [
            {
              \"tcm_id\": \"6894787532572065797\",
              \"user_id\": \"6684747467718820870\",
              \"nick_name\": \"Josh Zilberberg\",
              \"avatar_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-
    avt-0068/f11c960c637601225c29d6e7849069eb~tplv-tiktokx-cropcenter:100:100.png\",
              \"country_code\": \"US\",
              \"follower_cnt\": 3048368,
              \"liked_cnt\": 130131619,
              \"tt_link\": \"https://www.tiktok.com/@josh.zilberberg\",
              \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/6894787532572065797\",
              \"items\": [
                {
                  \"item_id\": \"7406005139112283397\",
                  \"cover_url\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068/6e0c79311c2b49758674ae64721c495b_1724344961~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7406005139112283397\",
                  \"vv\": 3266905,
                  \"liked_cnt\": 4057,
                  \"create_time\": 1724344950
                }
              ]
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 6,
            \"has_more\": false
          }
        }
      }
    }
    ```

    Args:
        keyword (str): 搜索关键词/Search keyword
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        sort_by (Union[Unset, str]): 排序方式/Sort by (follower, avg_views) Default: 'follower'.
        creator_country (Union[Unset, str]): 创作者国家/Creator country Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        page=page,
        limit=limit,
        sort_by=sort_by,
        creator_country=creator_country,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    keyword: str,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    sort_by: Union[Unset, str] = "follower",
    creator_country: Union[Unset, str] = "US",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索创作者/Search creators

     # [中文]
    ### 用途:
    - 通过关键词搜索创作者
    - 快速找到特定领域或名称的创作者
    - 支持按粉丝数或平均观看量排序

    ### 参数:
    - keyword: 搜索关键词，可以是用户名、昵称的一部分
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - sort_by: 排序方式
      - follower: 按粉丝数排序
      - avg_views: 按平均观看量排序
    - creator_country: 创作者所在国家

    ### 返回内容说明:
    - `creators`: 创作者列表
      - `tcm_id`: 创作者市场ID
      - `user_id`: 用户ID
      - `nick_name`: 昵称
      - `avatar_url`: 头像URL
      - `country_code`: 国家代码
      - `follower_cnt`: 粉丝数
      - `liked_cnt`: 总点赞数
      - `tt_link`: TikTok个人主页链接
      - `tcm_link`: 创作者市场链接
      - `items`: 作品列表
        - `item_id`: 作品ID
        - `cover_url`: 封面URL
        - `tt_link`: 作品链接
        - `vv`: 观看量
        - `liked_cnt`: 点赞数
        - `create_time`: 创建时间戳
    - `pagination`: 分页信息
      - `page`: 当前页码
      - `size`: 每页数量
      - `total`: 总数
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_creators\",
      \"params\": {
        \"keyword\": \"jo\",
        \"page\": \"1\",
        \"limit\": \"20\",
        \"sort_by\": \"follower\",
        \"creator_country\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"creators\": [
            {
              \"tcm_id\": \"6894787532572065797\",
              \"user_id\": \"6684747467718820870\",
              \"nick_name\": \"Josh Zilberberg\",
              \"avatar_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-
    avt-0068/f11c960c637601225c29d6e7849069eb~tplv-tiktokx-cropcenter:100:100.png\",
              \"country_code\": \"US\",
              \"follower_cnt\": 3048368,
              \"liked_cnt\": 130131619,
              \"tt_link\": \"https://www.tiktok.com/@josh.zilberberg\",
              \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/6894787532572065797\",
              \"items\": [
                {
                  \"item_id\": \"7406005139112283397\",
                  \"cover_url\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068/6e0c79311c2b49758674ae64721c495b_1724344961~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7406005139112283397\",
                  \"vv\": 3266905,
                  \"liked_cnt\": 4057,
                  \"create_time\": 1724344950
                }
              ]
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 6,
            \"has_more\": false
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Search creators by keyword
    - Quickly find creators in specific fields or with specific names
    - Support sorting by follower count or average views

    ### Parameters:
    - keyword: Search keyword, can be part of username or nickname
    - page: Page number, default 1
    - limit: Items per page, default 20
    - sort_by: Sorting method
      - follower: Sort by follower count
      - avg_views: Sort by average views
    - creator_country: Creator's country

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
      \"router\": \"/api/v1/tiktok/ads/search_creators\",
      \"params\": {
        \"keyword\": \"jo\",
        \"page\": \"1\",
        \"limit\": \"20\",
        \"sort_by\": \"follower\",
        \"creator_country\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"creators\": [
            {
              \"tcm_id\": \"6894787532572065797\",
              \"user_id\": \"6684747467718820870\",
              \"nick_name\": \"Josh Zilberberg\",
              \"avatar_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-
    avt-0068/f11c960c637601225c29d6e7849069eb~tplv-tiktokx-cropcenter:100:100.png\",
              \"country_code\": \"US\",
              \"follower_cnt\": 3048368,
              \"liked_cnt\": 130131619,
              \"tt_link\": \"https://www.tiktok.com/@josh.zilberberg\",
              \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/6894787532572065797\",
              \"items\": [
                {
                  \"item_id\": \"7406005139112283397\",
                  \"cover_url\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068/6e0c79311c2b49758674ae64721c495b_1724344961~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7406005139112283397\",
                  \"vv\": 3266905,
                  \"liked_cnt\": 4057,
                  \"create_time\": 1724344950
                }
              ]
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 6,
            \"has_more\": false
          }
        }
      }
    }
    ```

    Args:
        keyword (str): 搜索关键词/Search keyword
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        sort_by (Union[Unset, str]): 排序方式/Sort by (follower, avg_views) Default: 'follower'.
        creator_country (Union[Unset, str]): 创作者国家/Creator country Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        keyword=keyword,
        page=page,
        limit=limit,
        sort_by=sort_by,
        creator_country=creator_country,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    sort_by: Union[Unset, str] = "follower",
    creator_country: Union[Unset, str] = "US",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索创作者/Search creators

     # [中文]
    ### 用途:
    - 通过关键词搜索创作者
    - 快速找到特定领域或名称的创作者
    - 支持按粉丝数或平均观看量排序

    ### 参数:
    - keyword: 搜索关键词，可以是用户名、昵称的一部分
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - sort_by: 排序方式
      - follower: 按粉丝数排序
      - avg_views: 按平均观看量排序
    - creator_country: 创作者所在国家

    ### 返回内容说明:
    - `creators`: 创作者列表
      - `tcm_id`: 创作者市场ID
      - `user_id`: 用户ID
      - `nick_name`: 昵称
      - `avatar_url`: 头像URL
      - `country_code`: 国家代码
      - `follower_cnt`: 粉丝数
      - `liked_cnt`: 总点赞数
      - `tt_link`: TikTok个人主页链接
      - `tcm_link`: 创作者市场链接
      - `items`: 作品列表
        - `item_id`: 作品ID
        - `cover_url`: 封面URL
        - `tt_link`: 作品链接
        - `vv`: 观看量
        - `liked_cnt`: 点赞数
        - `create_time`: 创建时间戳
    - `pagination`: 分页信息
      - `page`: 当前页码
      - `size`: 每页数量
      - `total`: 总数
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_creators\",
      \"params\": {
        \"keyword\": \"jo\",
        \"page\": \"1\",
        \"limit\": \"20\",
        \"sort_by\": \"follower\",
        \"creator_country\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"creators\": [
            {
              \"tcm_id\": \"6894787532572065797\",
              \"user_id\": \"6684747467718820870\",
              \"nick_name\": \"Josh Zilberberg\",
              \"avatar_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-
    avt-0068/f11c960c637601225c29d6e7849069eb~tplv-tiktokx-cropcenter:100:100.png\",
              \"country_code\": \"US\",
              \"follower_cnt\": 3048368,
              \"liked_cnt\": 130131619,
              \"tt_link\": \"https://www.tiktok.com/@josh.zilberberg\",
              \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/6894787532572065797\",
              \"items\": [
                {
                  \"item_id\": \"7406005139112283397\",
                  \"cover_url\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068/6e0c79311c2b49758674ae64721c495b_1724344961~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7406005139112283397\",
                  \"vv\": 3266905,
                  \"liked_cnt\": 4057,
                  \"create_time\": 1724344950
                }
              ]
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 6,
            \"has_more\": false
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Search creators by keyword
    - Quickly find creators in specific fields or with specific names
    - Support sorting by follower count or average views

    ### Parameters:
    - keyword: Search keyword, can be part of username or nickname
    - page: Page number, default 1
    - limit: Items per page, default 20
    - sort_by: Sorting method
      - follower: Sort by follower count
      - avg_views: Sort by average views
    - creator_country: Creator's country

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
      \"router\": \"/api/v1/tiktok/ads/search_creators\",
      \"params\": {
        \"keyword\": \"jo\",
        \"page\": \"1\",
        \"limit\": \"20\",
        \"sort_by\": \"follower\",
        \"creator_country\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"creators\": [
            {
              \"tcm_id\": \"6894787532572065797\",
              \"user_id\": \"6684747467718820870\",
              \"nick_name\": \"Josh Zilberberg\",
              \"avatar_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-
    avt-0068/f11c960c637601225c29d6e7849069eb~tplv-tiktokx-cropcenter:100:100.png\",
              \"country_code\": \"US\",
              \"follower_cnt\": 3048368,
              \"liked_cnt\": 130131619,
              \"tt_link\": \"https://www.tiktok.com/@josh.zilberberg\",
              \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/6894787532572065797\",
              \"items\": [
                {
                  \"item_id\": \"7406005139112283397\",
                  \"cover_url\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068/6e0c79311c2b49758674ae64721c495b_1724344961~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7406005139112283397\",
                  \"vv\": 3266905,
                  \"liked_cnt\": 4057,
                  \"create_time\": 1724344950
                }
              ]
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 6,
            \"has_more\": false
          }
        }
      }
    }
    ```

    Args:
        keyword (str): 搜索关键词/Search keyword
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        sort_by (Union[Unset, str]): 排序方式/Sort by (follower, avg_views) Default: 'follower'.
        creator_country (Union[Unset, str]): 创作者国家/Creator country Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        page=page,
        limit=limit,
        sort_by=sort_by,
        creator_country=creator_country,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
    sort_by: Union[Unset, str] = "follower",
    creator_country: Union[Unset, str] = "US",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索创作者/Search creators

     # [中文]
    ### 用途:
    - 通过关键词搜索创作者
    - 快速找到特定领域或名称的创作者
    - 支持按粉丝数或平均观看量排序

    ### 参数:
    - keyword: 搜索关键词，可以是用户名、昵称的一部分
    - page: 页码，默认1
    - limit: 每页数量，默认20
    - sort_by: 排序方式
      - follower: 按粉丝数排序
      - avg_views: 按平均观看量排序
    - creator_country: 创作者所在国家

    ### 返回内容说明:
    - `creators`: 创作者列表
      - `tcm_id`: 创作者市场ID
      - `user_id`: 用户ID
      - `nick_name`: 昵称
      - `avatar_url`: 头像URL
      - `country_code`: 国家代码
      - `follower_cnt`: 粉丝数
      - `liked_cnt`: 总点赞数
      - `tt_link`: TikTok个人主页链接
      - `tcm_link`: 创作者市场链接
      - `items`: 作品列表
        - `item_id`: 作品ID
        - `cover_url`: 封面URL
        - `tt_link`: 作品链接
        - `vv`: 观看量
        - `liked_cnt`: 点赞数
        - `create_time`: 创建时间戳
    - `pagination`: 分页信息
      - `page`: 当前页码
      - `size`: 每页数量
      - `total`: 总数
      - `has_more`: 是否有更多

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/search_creators\",
      \"params\": {
        \"keyword\": \"jo\",
        \"page\": \"1\",
        \"limit\": \"20\",
        \"sort_by\": \"follower\",
        \"creator_country\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"creators\": [
            {
              \"tcm_id\": \"6894787532572065797\",
              \"user_id\": \"6684747467718820870\",
              \"nick_name\": \"Josh Zilberberg\",
              \"avatar_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-
    avt-0068/f11c960c637601225c29d6e7849069eb~tplv-tiktokx-cropcenter:100:100.png\",
              \"country_code\": \"US\",
              \"follower_cnt\": 3048368,
              \"liked_cnt\": 130131619,
              \"tt_link\": \"https://www.tiktok.com/@josh.zilberberg\",
              \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/6894787532572065797\",
              \"items\": [
                {
                  \"item_id\": \"7406005139112283397\",
                  \"cover_url\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068/6e0c79311c2b49758674ae64721c495b_1724344961~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7406005139112283397\",
                  \"vv\": 3266905,
                  \"liked_cnt\": 4057,
                  \"create_time\": 1724344950
                }
              ]
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 6,
            \"has_more\": false
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Search creators by keyword
    - Quickly find creators in specific fields or with specific names
    - Support sorting by follower count or average views

    ### Parameters:
    - keyword: Search keyword, can be part of username or nickname
    - page: Page number, default 1
    - limit: Items per page, default 20
    - sort_by: Sorting method
      - follower: Sort by follower count
      - avg_views: Sort by average views
    - creator_country: Creator's country

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
      \"router\": \"/api/v1/tiktok/ads/search_creators\",
      \"params\": {
        \"keyword\": \"jo\",
        \"page\": \"1\",
        \"limit\": \"20\",
        \"sort_by\": \"follower\",
        \"creator_country\": \"US\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"creators\": [
            {
              \"tcm_id\": \"6894787532572065797\",
              \"user_id\": \"6684747467718820870\",
              \"nick_name\": \"Josh Zilberberg\",
              \"avatar_url\": \"https://p16-sign-va.tiktokcdn.com/tos-maliva-
    avt-0068/f11c960c637601225c29d6e7849069eb~tplv-tiktokx-cropcenter:100:100.png\",
              \"country_code\": \"US\",
              \"follower_cnt\": 3048368,
              \"liked_cnt\": 130131619,
              \"tt_link\": \"https://www.tiktok.com/@josh.zilberberg\",
              \"tcm_link\": \"https://creatormarketplace.tiktok.com/ad#/author/6894787532572065797\",
              \"items\": [
                {
                  \"item_id\": \"7406005139112283397\",
                  \"cover_url\": \"https://p16-sign-va.tiktokcdn.com/tos-
    maliva-p-0068/6e0c79311c2b49758674ae64721c495b_1724344961~tplv-noop.image\",
                  \"tt_link\": \"https://www.tiktok.com/@author/video/7406005139112283397\",
                  \"vv\": 3266905,
                  \"liked_cnt\": 4057,
                  \"create_time\": 1724344950
                }
              ]
            }
          ],
          \"pagination\": {
            \"page\": 1,
            \"size\": 20,
            \"total\": 6,
            \"has_more\": false
          }
        }
      }
    }
    ```

    Args:
        keyword (str): 搜索关键词/Search keyword
        page (Union[Unset, int]): 页码/Page number Default: 1.
        limit (Union[Unset, int]): 每页数量/Items per page Default: 20.
        sort_by (Union[Unset, str]): 排序方式/Sort by (follower, avg_views) Default: 'follower'.
        creator_country (Union[Unset, str]): 创作者国家/Creator country Default: 'US'.

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
            page=page,
            limit=limit,
            sort_by=sort_by,
            creator_country=creator_country,
        )
    ).parsed
