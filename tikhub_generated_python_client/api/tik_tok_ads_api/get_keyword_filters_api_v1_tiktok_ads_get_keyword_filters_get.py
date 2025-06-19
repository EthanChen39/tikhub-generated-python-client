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
        "url": "/api/v1/tiktok/ads/get_keyword_filters",
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
    r"""获取关键词筛选器/Get keyword filters

     # [中文]
    ### 用途:
    - 获取关键词洞察功能的可用筛选选项
    - 了解支持的国家/地区、行业、关键词类型等筛选维度
    - 为关键词分析提供筛选参数参考

    ### 返回内容说明:
    - `country_list`: 支持的国家/地区列表
      - `id`: 国家代码
      - `value`: 国家名称
    - `industry_list`: 支持的行业列表
      - `id`: 行业ID
      - `value`: 行业名称
    - `keyword_type`: 支持的关键词类型
    - `objective_list`: 支持的广告目标列表

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_keyword_filters\",
      \"params\": {},
      \"data\": {
        \"country_list\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"}
        ],
        \"industry_list\": [
          {\"id\": \"27000000000\", \"value\": \"Games\"},
          {\"id\": \"19000000000\", \"value\": \"E-commerce\"}
        ],
        \"keyword_type\": [\"general\", \"brand\", \"product\"],
        \"objective_list\": [
          {\"id\": \"1\", \"value\": \"Traffic\"},
          {\"id\": \"2\", \"value\": \"Conversions\"}
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get available filter options for keyword insights functionality
    - Understand supported countries/regions, industries, keyword types and other filter dimensions
    - Provide filter parameter reference for keyword analysis

    ### Return Description:
    - `country_list`: List of supported countries/regions
      - `id`: Country code
      - `value`: Country name
    - `industry_list`: List of supported industries
      - `id`: Industry ID
      - `value`: Industry name
    - `keyword_type`: Supported keyword types
    - `objective_list`: List of supported ad objectives

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_keyword_filters\",
      \"params\": {},
      \"data\": {
        \"country_list\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"}
        ],
        \"industry_list\": [
          {\"id\": \"27000000000\", \"value\": \"Games\"},
          {\"id\": \"19000000000\", \"value\": \"E-commerce\"}
        ],
        \"keyword_type\": [\"general\", \"brand\", \"product\"],
        \"objective_list\": [
          {\"id\": \"1\", \"value\": \"Traffic\"},
          {\"id\": \"2\", \"value\": \"Conversions\"}
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
    r"""获取关键词筛选器/Get keyword filters

     # [中文]
    ### 用途:
    - 获取关键词洞察功能的可用筛选选项
    - 了解支持的国家/地区、行业、关键词类型等筛选维度
    - 为关键词分析提供筛选参数参考

    ### 返回内容说明:
    - `country_list`: 支持的国家/地区列表
      - `id`: 国家代码
      - `value`: 国家名称
    - `industry_list`: 支持的行业列表
      - `id`: 行业ID
      - `value`: 行业名称
    - `keyword_type`: 支持的关键词类型
    - `objective_list`: 支持的广告目标列表

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_keyword_filters\",
      \"params\": {},
      \"data\": {
        \"country_list\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"}
        ],
        \"industry_list\": [
          {\"id\": \"27000000000\", \"value\": \"Games\"},
          {\"id\": \"19000000000\", \"value\": \"E-commerce\"}
        ],
        \"keyword_type\": [\"general\", \"brand\", \"product\"],
        \"objective_list\": [
          {\"id\": \"1\", \"value\": \"Traffic\"},
          {\"id\": \"2\", \"value\": \"Conversions\"}
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get available filter options for keyword insights functionality
    - Understand supported countries/regions, industries, keyword types and other filter dimensions
    - Provide filter parameter reference for keyword analysis

    ### Return Description:
    - `country_list`: List of supported countries/regions
      - `id`: Country code
      - `value`: Country name
    - `industry_list`: List of supported industries
      - `id`: Industry ID
      - `value`: Industry name
    - `keyword_type`: Supported keyword types
    - `objective_list`: List of supported ad objectives

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_keyword_filters\",
      \"params\": {},
      \"data\": {
        \"country_list\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"}
        ],
        \"industry_list\": [
          {\"id\": \"27000000000\", \"value\": \"Games\"},
          {\"id\": \"19000000000\", \"value\": \"E-commerce\"}
        ],
        \"keyword_type\": [\"general\", \"brand\", \"product\"],
        \"objective_list\": [
          {\"id\": \"1\", \"value\": \"Traffic\"},
          {\"id\": \"2\", \"value\": \"Conversions\"}
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
    r"""获取关键词筛选器/Get keyword filters

     # [中文]
    ### 用途:
    - 获取关键词洞察功能的可用筛选选项
    - 了解支持的国家/地区、行业、关键词类型等筛选维度
    - 为关键词分析提供筛选参数参考

    ### 返回内容说明:
    - `country_list`: 支持的国家/地区列表
      - `id`: 国家代码
      - `value`: 国家名称
    - `industry_list`: 支持的行业列表
      - `id`: 行业ID
      - `value`: 行业名称
    - `keyword_type`: 支持的关键词类型
    - `objective_list`: 支持的广告目标列表

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_keyword_filters\",
      \"params\": {},
      \"data\": {
        \"country_list\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"}
        ],
        \"industry_list\": [
          {\"id\": \"27000000000\", \"value\": \"Games\"},
          {\"id\": \"19000000000\", \"value\": \"E-commerce\"}
        ],
        \"keyword_type\": [\"general\", \"brand\", \"product\"],
        \"objective_list\": [
          {\"id\": \"1\", \"value\": \"Traffic\"},
          {\"id\": \"2\", \"value\": \"Conversions\"}
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get available filter options for keyword insights functionality
    - Understand supported countries/regions, industries, keyword types and other filter dimensions
    - Provide filter parameter reference for keyword analysis

    ### Return Description:
    - `country_list`: List of supported countries/regions
      - `id`: Country code
      - `value`: Country name
    - `industry_list`: List of supported industries
      - `id`: Industry ID
      - `value`: Industry name
    - `keyword_type`: Supported keyword types
    - `objective_list`: List of supported ad objectives

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_keyword_filters\",
      \"params\": {},
      \"data\": {
        \"country_list\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"}
        ],
        \"industry_list\": [
          {\"id\": \"27000000000\", \"value\": \"Games\"},
          {\"id\": \"19000000000\", \"value\": \"E-commerce\"}
        ],
        \"keyword_type\": [\"general\", \"brand\", \"product\"],
        \"objective_list\": [
          {\"id\": \"1\", \"value\": \"Traffic\"},
          {\"id\": \"2\", \"value\": \"Conversions\"}
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
    r"""获取关键词筛选器/Get keyword filters

     # [中文]
    ### 用途:
    - 获取关键词洞察功能的可用筛选选项
    - 了解支持的国家/地区、行业、关键词类型等筛选维度
    - 为关键词分析提供筛选参数参考

    ### 返回内容说明:
    - `country_list`: 支持的国家/地区列表
      - `id`: 国家代码
      - `value`: 国家名称
    - `industry_list`: 支持的行业列表
      - `id`: 行业ID
      - `value`: 行业名称
    - `keyword_type`: 支持的关键词类型
    - `objective_list`: 支持的广告目标列表

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_keyword_filters\",
      \"params\": {},
      \"data\": {
        \"country_list\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"}
        ],
        \"industry_list\": [
          {\"id\": \"27000000000\", \"value\": \"Games\"},
          {\"id\": \"19000000000\", \"value\": \"E-commerce\"}
        ],
        \"keyword_type\": [\"general\", \"brand\", \"product\"],
        \"objective_list\": [
          {\"id\": \"1\", \"value\": \"Traffic\"},
          {\"id\": \"2\", \"value\": \"Conversions\"}
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get available filter options for keyword insights functionality
    - Understand supported countries/regions, industries, keyword types and other filter dimensions
    - Provide filter parameter reference for keyword analysis

    ### Return Description:
    - `country_list`: List of supported countries/regions
      - `id`: Country code
      - `value`: Country name
    - `industry_list`: List of supported industries
      - `id`: Industry ID
      - `value`: Industry name
    - `keyword_type`: Supported keyword types
    - `objective_list`: List of supported ad objectives

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_keyword_filters\",
      \"params\": {},
      \"data\": {
        \"country_list\": [
          {\"id\": \"US\", \"value\": \"United States\"},
          {\"id\": \"UK\", \"value\": \"United Kingdom\"}
        ],
        \"industry_list\": [
          {\"id\": \"27000000000\", \"value\": \"Games\"},
          {\"id\": \"19000000000\", \"value\": \"E-commerce\"}
        ],
        \"keyword_type\": [\"general\", \"brand\", \"product\"],
        \"objective_list\": [
          {\"id\": \"1\", \"value\": \"Traffic\"},
          {\"id\": \"2\", \"value\": \"Conversions\"}
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
