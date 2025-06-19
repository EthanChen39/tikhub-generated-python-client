from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/get_creator_filters",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ResponseModel]:
    if response.status_code == 200:
        response_200 = ResponseModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ResponseModel]:
    r"""获取创作者筛选器/Get creator filters

     # [中文]
    ### 用途:
    - 获取创作者搜索和筛选的可用选项
    - 了解支持的国家、排序方式等筛选维度
    - 为创作者分析提供参数参考

    ### 返回内容说明:
    - `audience_country`: 受众国家列表
      - `id`: 国家代码
      - `value`: 国家名称
    - `creator_country`: 创作者所在国家列表
    - `sort_by`: 支持的排序方式
      - follower: 按粉丝数排序
      - engagement: 按互动率排序
      - avg_views: 按平均观看量排序

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_creator_filters\",
      \"params\": {},
      \"data\": {
        \"audience_country\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"}
        ],
        \"creator_country\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"}
        ],
        \"sort_by\": [\"follower\", \"engagement\", \"avg_views\"]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get available options for creator search and filtering
    - Understand supported countries, sorting methods and other filter dimensions
    - Provide parameter reference for creator analysis

    ### Return Description:
    - `audience_country`: Audience country list
      - `id`: Country code
      - `value`: Country name
    - `creator_country`: Creator country list
    - `sort_by`: Supported sorting methods
      - follower: Sort by follower count
      - engagement: Sort by engagement rate
      - avg_views: Sort by average views

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_creator_filters\",
      \"params\": {},
      \"data\": {
        \"audience_country\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"}
        ],
        \"creator_country\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"}
        ],
        \"sort_by\": [\"follower\", \"engagement\", \"avg_views\"]
      }
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseModel]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[ResponseModel]:
    r"""获取创作者筛选器/Get creator filters

     # [中文]
    ### 用途:
    - 获取创作者搜索和筛选的可用选项
    - 了解支持的国家、排序方式等筛选维度
    - 为创作者分析提供参数参考

    ### 返回内容说明:
    - `audience_country`: 受众国家列表
      - `id`: 国家代码
      - `value`: 国家名称
    - `creator_country`: 创作者所在国家列表
    - `sort_by`: 支持的排序方式
      - follower: 按粉丝数排序
      - engagement: 按互动率排序
      - avg_views: 按平均观看量排序

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_creator_filters\",
      \"params\": {},
      \"data\": {
        \"audience_country\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"}
        ],
        \"creator_country\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"}
        ],
        \"sort_by\": [\"follower\", \"engagement\", \"avg_views\"]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get available options for creator search and filtering
    - Understand supported countries, sorting methods and other filter dimensions
    - Provide parameter reference for creator analysis

    ### Return Description:
    - `audience_country`: Audience country list
      - `id`: Country code
      - `value`: Country name
    - `creator_country`: Creator country list
    - `sort_by`: Supported sorting methods
      - follower: Sort by follower count
      - engagement: Sort by engagement rate
      - avg_views: Sort by average views

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_creator_filters\",
      \"params\": {},
      \"data\": {
        \"audience_country\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"}
        ],
        \"creator_country\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"}
        ],
        \"sort_by\": [\"follower\", \"engagement\", \"avg_views\"]
      }
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseModel
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ResponseModel]:
    r"""获取创作者筛选器/Get creator filters

     # [中文]
    ### 用途:
    - 获取创作者搜索和筛选的可用选项
    - 了解支持的国家、排序方式等筛选维度
    - 为创作者分析提供参数参考

    ### 返回内容说明:
    - `audience_country`: 受众国家列表
      - `id`: 国家代码
      - `value`: 国家名称
    - `creator_country`: 创作者所在国家列表
    - `sort_by`: 支持的排序方式
      - follower: 按粉丝数排序
      - engagement: 按互动率排序
      - avg_views: 按平均观看量排序

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_creator_filters\",
      \"params\": {},
      \"data\": {
        \"audience_country\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"}
        ],
        \"creator_country\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"}
        ],
        \"sort_by\": [\"follower\", \"engagement\", \"avg_views\"]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get available options for creator search and filtering
    - Understand supported countries, sorting methods and other filter dimensions
    - Provide parameter reference for creator analysis

    ### Return Description:
    - `audience_country`: Audience country list
      - `id`: Country code
      - `value`: Country name
    - `creator_country`: Creator country list
    - `sort_by`: Supported sorting methods
      - follower: Sort by follower count
      - engagement: Sort by engagement rate
      - avg_views: Sort by average views

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_creator_filters\",
      \"params\": {},
      \"data\": {
        \"audience_country\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"}
        ],
        \"creator_country\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"}
        ],
        \"sort_by\": [\"follower\", \"engagement\", \"avg_views\"]
      }
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseModel]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[ResponseModel]:
    r"""获取创作者筛选器/Get creator filters

     # [中文]
    ### 用途:
    - 获取创作者搜索和筛选的可用选项
    - 了解支持的国家、排序方式等筛选维度
    - 为创作者分析提供参数参考

    ### 返回内容说明:
    - `audience_country`: 受众国家列表
      - `id`: 国家代码
      - `value`: 国家名称
    - `creator_country`: 创作者所在国家列表
    - `sort_by`: 支持的排序方式
      - follower: 按粉丝数排序
      - engagement: 按互动率排序
      - avg_views: 按平均观看量排序

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_creator_filters\",
      \"params\": {},
      \"data\": {
        \"audience_country\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"}
        ],
        \"creator_country\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"}
        ],
        \"sort_by\": [\"follower\", \"engagement\", \"avg_views\"]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get available options for creator search and filtering
    - Understand supported countries, sorting methods and other filter dimensions
    - Provide parameter reference for creator analysis

    ### Return Description:
    - `audience_country`: Audience country list
      - `id`: Country code
      - `value`: Country name
    - `creator_country`: Creator country list
    - `sort_by`: Supported sorting methods
      - follower: Sort by follower count
      - engagement: Sort by engagement rate
      - avg_views: Sort by average views

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_creator_filters\",
      \"params\": {},
      \"data\": {
        \"audience_country\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"}
        ],
        \"creator_country\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"}
        ],
        \"sort_by\": [\"follower\", \"engagement\", \"avg_views\"]
      }
    }
    ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
