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
        "url": "/api/v1/tiktok/ads/get_hashtag_filters",
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
    r"""获取标签筛选器/Get hashtag filters

     # [中文]
    ### 用途:
    - 获取热门标签功能的可用筛选选项
    - 了解支持的国家/地区、行业等筛选维度
    - 为标签分析提供筛选参数参考

    ### 返回内容说明:
    - `country`: 支持的国家/地区列表
      - `id`: 国家代码
      - `value`: 国家名称
    - `industry`: 支持的行业列表
      - `id`: 行业ID
      - `value`: 行业名称

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_hashtag_filters\",
      \"params\": {},
      \"data\": {
        \"country\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"},
          {\"id\": \"JP\", \"value\": \"Japan\"}
        ],
        \"industry\": [
          {\"id\": \"27000000000\", \"value\": \"Games\"},
          {\"id\": \"19000000000\", \"value\": \"E-commerce\"},
          {\"id\": \"10000000000\", \"value\": \"Education\"}
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get available filter options for popular hashtag functionality
    - Understand supported countries/regions, industries and other filter dimensions
    - Provide filter parameter reference for hashtag analysis

    ### Return Description:
    - `country`: List of supported countries/regions
      - `id`: Country code
      - `value`: Country name
    - `industry`: List of supported industries
      - `id`: Industry ID
      - `value`: Industry name

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_hashtag_filters\",
      \"params\": {},
      \"data\": {
        \"country\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"},
          {\"id\": \"JP\", \"value\": \"Japan\"}
        ],
        \"industry\": [
          {\"id\": \"27000000000\", \"value\": \"Games\"},
          {\"id\": \"19000000000\", \"value\": \"E-commerce\"},
          {\"id\": \"10000000000\", \"value\": \"Education\"}
        ]
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
    r"""获取标签筛选器/Get hashtag filters

     # [中文]
    ### 用途:
    - 获取热门标签功能的可用筛选选项
    - 了解支持的国家/地区、行业等筛选维度
    - 为标签分析提供筛选参数参考

    ### 返回内容说明:
    - `country`: 支持的国家/地区列表
      - `id`: 国家代码
      - `value`: 国家名称
    - `industry`: 支持的行业列表
      - `id`: 行业ID
      - `value`: 行业名称

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_hashtag_filters\",
      \"params\": {},
      \"data\": {
        \"country\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"},
          {\"id\": \"JP\", \"value\": \"Japan\"}
        ],
        \"industry\": [
          {\"id\": \"27000000000\", \"value\": \"Games\"},
          {\"id\": \"19000000000\", \"value\": \"E-commerce\"},
          {\"id\": \"10000000000\", \"value\": \"Education\"}
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get available filter options for popular hashtag functionality
    - Understand supported countries/regions, industries and other filter dimensions
    - Provide filter parameter reference for hashtag analysis

    ### Return Description:
    - `country`: List of supported countries/regions
      - `id`: Country code
      - `value`: Country name
    - `industry`: List of supported industries
      - `id`: Industry ID
      - `value`: Industry name

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_hashtag_filters\",
      \"params\": {},
      \"data\": {
        \"country\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"},
          {\"id\": \"JP\", \"value\": \"Japan\"}
        ],
        \"industry\": [
          {\"id\": \"27000000000\", \"value\": \"Games\"},
          {\"id\": \"19000000000\", \"value\": \"E-commerce\"},
          {\"id\": \"10000000000\", \"value\": \"Education\"}
        ]
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
    r"""获取标签筛选器/Get hashtag filters

     # [中文]
    ### 用途:
    - 获取热门标签功能的可用筛选选项
    - 了解支持的国家/地区、行业等筛选维度
    - 为标签分析提供筛选参数参考

    ### 返回内容说明:
    - `country`: 支持的国家/地区列表
      - `id`: 国家代码
      - `value`: 国家名称
    - `industry`: 支持的行业列表
      - `id`: 行业ID
      - `value`: 行业名称

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_hashtag_filters\",
      \"params\": {},
      \"data\": {
        \"country\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"},
          {\"id\": \"JP\", \"value\": \"Japan\"}
        ],
        \"industry\": [
          {\"id\": \"27000000000\", \"value\": \"Games\"},
          {\"id\": \"19000000000\", \"value\": \"E-commerce\"},
          {\"id\": \"10000000000\", \"value\": \"Education\"}
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get available filter options for popular hashtag functionality
    - Understand supported countries/regions, industries and other filter dimensions
    - Provide filter parameter reference for hashtag analysis

    ### Return Description:
    - `country`: List of supported countries/regions
      - `id`: Country code
      - `value`: Country name
    - `industry`: List of supported industries
      - `id`: Industry ID
      - `value`: Industry name

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_hashtag_filters\",
      \"params\": {},
      \"data\": {
        \"country\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"},
          {\"id\": \"JP\", \"value\": \"Japan\"}
        ],
        \"industry\": [
          {\"id\": \"27000000000\", \"value\": \"Games\"},
          {\"id\": \"19000000000\", \"value\": \"E-commerce\"},
          {\"id\": \"10000000000\", \"value\": \"Education\"}
        ]
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
    r"""获取标签筛选器/Get hashtag filters

     # [中文]
    ### 用途:
    - 获取热门标签功能的可用筛选选项
    - 了解支持的国家/地区、行业等筛选维度
    - 为标签分析提供筛选参数参考

    ### 返回内容说明:
    - `country`: 支持的国家/地区列表
      - `id`: 国家代码
      - `value`: 国家名称
    - `industry`: 支持的行业列表
      - `id`: 行业ID
      - `value`: 行业名称

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_hashtag_filters\",
      \"params\": {},
      \"data\": {
        \"country\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"},
          {\"id\": \"JP\", \"value\": \"Japan\"}
        ],
        \"industry\": [
          {\"id\": \"27000000000\", \"value\": \"Games\"},
          {\"id\": \"19000000000\", \"value\": \"E-commerce\"},
          {\"id\": \"10000000000\", \"value\": \"Education\"}
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get available filter options for popular hashtag functionality
    - Understand supported countries/regions, industries and other filter dimensions
    - Provide filter parameter reference for hashtag analysis

    ### Return Description:
    - `country`: List of supported countries/regions
      - `id`: Country code
      - `value`: Country name
    - `industry`: List of supported industries
      - `id`: Industry ID
      - `value`: Industry name

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_hashtag_filters\",
      \"params\": {},
      \"data\": {
        \"country\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"},
          {\"id\": \"JP\", \"value\": \"Japan\"}
        ],
        \"industry\": [
          {\"id\": \"27000000000\", \"value\": \"Games\"},
          {\"id\": \"19000000000\", \"value\": \"E-commerce\"},
          {\"id\": \"10000000000\", \"value\": \"Education\"}
        ]
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
