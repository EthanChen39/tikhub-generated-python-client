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
        "url": "/api/v1/tiktok/ads/get_product_filters",
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
    r"""获取产品筛选器/Get product filters

     # [中文]
    ### 用途:
    - 获取产品分析功能的可用筛选选项
    - 了解支持的电商类目、时间类型等筛选维度
    - 为产品数据分析提供筛选参数参考

    ### 返回内容说明:
    - `country`: 国家列表
      - `id`: 国家ID
      - `value`: 国家名称
      - `label`: 国家标签
    - `ecom_category`: 电商类目列表
      - `id`: 类目ID
      - `value`: 类目名称
      - `label`: 类目标签
    - `latest_month`: 最新月份
    - `latest_week`: 最新周

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_product_filters\",
      \"params\": {},
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"country\": [
            {
              \"id\": \"AR\",
              \"value\": \"Argentina\",
              \"label\": \"AR\"
            },
            {
              \"id\": \"AU\",
              \"value\": \"Australia\",
              \"label\": \"AU\"
            }
          ],
          \"ecom_category\": [
            {
              \"id\": 605196,
              \"value\": \"Automotive & Motorbike\",
              \"label\": \"category_605196\"
            },
            {
              \"id\": 602284,
              \"value\": \"Baby & Maternity\",
              \"label\": \"category_602284\"
            }
          ],
          \"latest_month\": \"2025-05\",
          \"latest_week\": \"2025-06-07\"
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get available filter options for product analysis functionality
    - Understand supported e-commerce categories, time types and other filter dimensions
    - Provide filter parameter reference for product data analysis

    ### Return Description:
    - `country`: Country list
      - `id`: Country ID
      - `value`: Country name
      - `label`: Country label
    - `ecom_category`: E-commerce category list
      - `id`: Category ID
      - `value`: Category name
      - `label`: Category label
    - `latest_month`: Latest month
    - `latest_week`: Latest week

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_product_filters\",
      \"params\": {},
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"country\": [
            {
              \"id\": \"AR\",
              \"value\": \"Argentina\",
              \"label\": \"AR\"
            },
            {
              \"id\": \"AU\",
              \"value\": \"Australia\",
              \"label\": \"AU\"
            }
          ],
          \"ecom_category\": [
            {
              \"id\": 605196,
              \"value\": \"Automotive & Motorbike\",
              \"label\": \"category_605196\"
            },
            {
              \"id\": 602284,
              \"value\": \"Baby & Maternity\",
              \"label\": \"category_602284\"
            }
          ],
          \"latest_month\": \"2025-05\",
          \"latest_week\": \"2025-06-07\"
        }
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
    r"""获取产品筛选器/Get product filters

     # [中文]
    ### 用途:
    - 获取产品分析功能的可用筛选选项
    - 了解支持的电商类目、时间类型等筛选维度
    - 为产品数据分析提供筛选参数参考

    ### 返回内容说明:
    - `country`: 国家列表
      - `id`: 国家ID
      - `value`: 国家名称
      - `label`: 国家标签
    - `ecom_category`: 电商类目列表
      - `id`: 类目ID
      - `value`: 类目名称
      - `label`: 类目标签
    - `latest_month`: 最新月份
    - `latest_week`: 最新周

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_product_filters\",
      \"params\": {},
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"country\": [
            {
              \"id\": \"AR\",
              \"value\": \"Argentina\",
              \"label\": \"AR\"
            },
            {
              \"id\": \"AU\",
              \"value\": \"Australia\",
              \"label\": \"AU\"
            }
          ],
          \"ecom_category\": [
            {
              \"id\": 605196,
              \"value\": \"Automotive & Motorbike\",
              \"label\": \"category_605196\"
            },
            {
              \"id\": 602284,
              \"value\": \"Baby & Maternity\",
              \"label\": \"category_602284\"
            }
          ],
          \"latest_month\": \"2025-05\",
          \"latest_week\": \"2025-06-07\"
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get available filter options for product analysis functionality
    - Understand supported e-commerce categories, time types and other filter dimensions
    - Provide filter parameter reference for product data analysis

    ### Return Description:
    - `country`: Country list
      - `id`: Country ID
      - `value`: Country name
      - `label`: Country label
    - `ecom_category`: E-commerce category list
      - `id`: Category ID
      - `value`: Category name
      - `label`: Category label
    - `latest_month`: Latest month
    - `latest_week`: Latest week

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_product_filters\",
      \"params\": {},
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"country\": [
            {
              \"id\": \"AR\",
              \"value\": \"Argentina\",
              \"label\": \"AR\"
            },
            {
              \"id\": \"AU\",
              \"value\": \"Australia\",
              \"label\": \"AU\"
            }
          ],
          \"ecom_category\": [
            {
              \"id\": 605196,
              \"value\": \"Automotive & Motorbike\",
              \"label\": \"category_605196\"
            },
            {
              \"id\": 602284,
              \"value\": \"Baby & Maternity\",
              \"label\": \"category_602284\"
            }
          ],
          \"latest_month\": \"2025-05\",
          \"latest_week\": \"2025-06-07\"
        }
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
    r"""获取产品筛选器/Get product filters

     # [中文]
    ### 用途:
    - 获取产品分析功能的可用筛选选项
    - 了解支持的电商类目、时间类型等筛选维度
    - 为产品数据分析提供筛选参数参考

    ### 返回内容说明:
    - `country`: 国家列表
      - `id`: 国家ID
      - `value`: 国家名称
      - `label`: 国家标签
    - `ecom_category`: 电商类目列表
      - `id`: 类目ID
      - `value`: 类目名称
      - `label`: 类目标签
    - `latest_month`: 最新月份
    - `latest_week`: 最新周

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_product_filters\",
      \"params\": {},
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"country\": [
            {
              \"id\": \"AR\",
              \"value\": \"Argentina\",
              \"label\": \"AR\"
            },
            {
              \"id\": \"AU\",
              \"value\": \"Australia\",
              \"label\": \"AU\"
            }
          ],
          \"ecom_category\": [
            {
              \"id\": 605196,
              \"value\": \"Automotive & Motorbike\",
              \"label\": \"category_605196\"
            },
            {
              \"id\": 602284,
              \"value\": \"Baby & Maternity\",
              \"label\": \"category_602284\"
            }
          ],
          \"latest_month\": \"2025-05\",
          \"latest_week\": \"2025-06-07\"
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get available filter options for product analysis functionality
    - Understand supported e-commerce categories, time types and other filter dimensions
    - Provide filter parameter reference for product data analysis

    ### Return Description:
    - `country`: Country list
      - `id`: Country ID
      - `value`: Country name
      - `label`: Country label
    - `ecom_category`: E-commerce category list
      - `id`: Category ID
      - `value`: Category name
      - `label`: Category label
    - `latest_month`: Latest month
    - `latest_week`: Latest week

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_product_filters\",
      \"params\": {},
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"country\": [
            {
              \"id\": \"AR\",
              \"value\": \"Argentina\",
              \"label\": \"AR\"
            },
            {
              \"id\": \"AU\",
              \"value\": \"Australia\",
              \"label\": \"AU\"
            }
          ],
          \"ecom_category\": [
            {
              \"id\": 605196,
              \"value\": \"Automotive & Motorbike\",
              \"label\": \"category_605196\"
            },
            {
              \"id\": 602284,
              \"value\": \"Baby & Maternity\",
              \"label\": \"category_602284\"
            }
          ],
          \"latest_month\": \"2025-05\",
          \"latest_week\": \"2025-06-07\"
        }
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
    r"""获取产品筛选器/Get product filters

     # [中文]
    ### 用途:
    - 获取产品分析功能的可用筛选选项
    - 了解支持的电商类目、时间类型等筛选维度
    - 为产品数据分析提供筛选参数参考

    ### 返回内容说明:
    - `country`: 国家列表
      - `id`: 国家ID
      - `value`: 国家名称
      - `label`: 国家标签
    - `ecom_category`: 电商类目列表
      - `id`: 类目ID
      - `value`: 类目名称
      - `label`: 类目标签
    - `latest_month`: 最新月份
    - `latest_week`: 最新周

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_product_filters\",
      \"params\": {},
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"country\": [
            {
              \"id\": \"AR\",
              \"value\": \"Argentina\",
              \"label\": \"AR\"
            },
            {
              \"id\": \"AU\",
              \"value\": \"Australia\",
              \"label\": \"AU\"
            }
          ],
          \"ecom_category\": [
            {
              \"id\": 605196,
              \"value\": \"Automotive & Motorbike\",
              \"label\": \"category_605196\"
            },
            {
              \"id\": 602284,
              \"value\": \"Baby & Maternity\",
              \"label\": \"category_602284\"
            }
          ],
          \"latest_month\": \"2025-05\",
          \"latest_week\": \"2025-06-07\"
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get available filter options for product analysis functionality
    - Understand supported e-commerce categories, time types and other filter dimensions
    - Provide filter parameter reference for product data analysis

    ### Return Description:
    - `country`: Country list
      - `id`: Country ID
      - `value`: Country name
      - `label`: Country label
    - `ecom_category`: E-commerce category list
      - `id`: Category ID
      - `value`: Category name
      - `label`: Category label
    - `latest_month`: Latest month
    - `latest_week`: Latest week

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_product_filters\",
      \"params\": {},
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"country\": [
            {
              \"id\": \"AR\",
              \"value\": \"Argentina\",
              \"label\": \"AR\"
            },
            {
              \"id\": \"AU\",
              \"value\": \"Australia\",
              \"label\": \"AU\"
            }
          ],
          \"ecom_category\": [
            {
              \"id\": 605196,
              \"value\": \"Automotive & Motorbike\",
              \"label\": \"category_605196\"
            },
            {
              \"id\": 602284,
              \"value\": \"Baby & Maternity\",
              \"label\": \"category_602284\"
            }
          ],
          \"latest_month\": \"2025-05\",
          \"latest_week\": \"2025-06-07\"
        }
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
