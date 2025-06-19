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
    id: str,
    last: Union[Unset, int] = 30,
    ecom_type: Union[Unset, str] = "l3",
    period_type: Union[Unset, str] = "last",
    country_code: Union[Unset, str] = "US",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["id"] = id

    params["last"] = last

    params["ecom_type"] = ecom_type

    params["period_type"] = period_type

    params["country_code"] = country_code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/get_product_detail",
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
    id: str,
    last: Union[Unset, int] = 30,
    ecom_type: Union[Unset, str] = "l3",
    period_type: Union[Unset, str] = "last",
    country_code: Union[Unset, str] = "US",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取产品详细信息/Get product detail

     # [中文]
    ### 用途:
    - 获取特定产品类目的完整详细信息
    - 包括受众分析、热门标签、相关帖子等多维度数据
    - 为产品营销策略提供全面的数据支持

    ### 参数:
    - id: 产品类目ID，如香水：601583
    - last: 最近天数，如7、30天
    - ecom_type: 电商类型，默认\"l3\"
    - period_type: 时间类型，默认\"last\"

    ### 返回内容说明:
    - `info`: 产品详细信息
      - `audience_ages`: 受众年龄分布
        - `age_level`: 年龄数值
        - `score`: 占比分数
      - `audience_interests`: 受众兴趣分布
        - `interest_info`: 兴趣信息
          - `id`: 兴趣ID
          - `label`: 兴趣标签
          - `value`: 兴趣名称
        - `score`: 占比分数
      - `cover_url`: 封面图URL（可能为null）
      - `ecom_type`: 电商类型
      - `first_ecom_category`: 一级电商类目
        - `id`: 类目ID
        - `label`: 类目标签
        - `value`: 类目名称
      - `hashtags`: 热门标签列表
      - `posts`: 相关帖子列表
      - `second_ecom_category`: 二级电商类目
      - `third_ecom_category`: 三级电商类目
      - `url_title`: URL标题

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_product_detail\",
      \"params\": {
        \"id\": \"601583\",
        \"last\": \"30\",
        \"ecom_type\": \"l3\",
        \"period_type\": \"last\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"info\": {
            \"audience_ages\": [
              {
                \"age_level\": 35,
                \"score\": 27
              },
              {
                \"age_level\": 25,
                \"score\": 22
              },
              {
                \"age_level\": 18,
                \"score\": 22
              },
              {
                \"age_level\": 45,
                \"score\": 18
              },
              {
                \"age_level\": 55,
                \"score\": 11
              }
            ],
            \"audience_interests\": [
              {
                \"interest_info\": {
                  \"id\": \"13105000000\",
                  \"label\": \"label_13105000000\",
                  \"value\": \"Pawn Shops\"
                },
                \"score\": 135
              },
              {
                \"interest_info\": {
                  \"id\": \"24104000000\",
                  \"label\": \"label_24104000000\",
                  \"value\": \"Electronics & Electrical\"
                },
                \"score\": 127
              }
            ],
            \"cover_url\": null,
            \"ecom_type\": \"l3\",
            \"first_ecom_category\": {
              \"id\": \"601450\",
              \"label\": \"category_601450\",
              \"value\": \"Beauty & Personal Care\"
            },
            \"hashtags\": [
              \"vlog\",
              \"perfumetiktok\",
              \"perfume\",
              \"fragrance\",
              \"fragrancetiktok\"
            ],
            \"posts\": [
              \"7436474042036522248\",
              \"7486253493716536584\",
              \"7503974461725740295\"
            ],
            \"url_title\": \"Perfume\"
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get complete detailed information for specific product categories
    - Includes multi-dimensional data like audience analysis, popular hashtags, related posts
    - Provide comprehensive data support for product marketing strategies

    ### Parameters:
    - id: Product category ID, e.g., Perfume: 601583
    - last: Number of recent days, e.g., 7, 30 days
    - ecom_type: E-commerce type, default \"l3\"
    - period_type: Period type, default \"last\"

    ### Return Description:
    - `info`: Product detailed information
      - `audience_ages`: Audience age distribution
        - `age_level`: Age value
        - `score`: Score value
      - `audience_interests`: Audience interest distribution
        - `interest_info`: Interest information
          - `id`: Interest ID
          - `label`: Interest label
          - `value`: Interest name
        - `score`: Score value
      - `cover_url`: Cover image URL (may be null)
      - `ecom_type`: E-commerce type
      - `first_ecom_category`: First-level e-commerce category
        - `id`: Category ID
        - `label`: Category label
        - `value`: Category name
      - `hashtags`: Popular hashtags list
      - `posts`: Related posts list
      - `second_ecom_category`: Second-level e-commerce category
      - `third_ecom_category`: Third-level e-commerce category
      - `url_title`: URL title

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_product_detail\",
      \"params\": {
        \"id\": \"601583\",
        \"last\": \"30\",
        \"ecom_type\": \"l3\",
        \"period_type\": \"last\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"info\": {
            \"audience_ages\": [
              {
                \"age_level\": 35,
                \"score\": 27
              },
              {
                \"age_level\": 25,
                \"score\": 22
              },
              {
                \"age_level\": 18,
                \"score\": 22
              },
              {
                \"age_level\": 45,
                \"score\": 18
              },
              {
                \"age_level\": 55,
                \"score\": 11
              }
            ],
            \"audience_interests\": [
              {
                \"interest_info\": {
                  \"id\": \"13105000000\",
                  \"label\": \"label_13105000000\",
                  \"value\": \"Pawn Shops\"
                },
                \"score\": 135
              },
              {
                \"interest_info\": {
                  \"id\": \"24104000000\",
                  \"label\": \"label_24104000000\",
                  \"value\": \"Electronics & Electrical\"
                },
                \"score\": 127
              }
            ],
            \"cover_url\": null,
            \"ecom_type\": \"l3\",
            \"first_ecom_category\": {
              \"id\": \"601450\",
              \"label\": \"category_601450\",
              \"value\": \"Beauty & Personal Care\"
            },
            \"hashtags\": [
              \"vlog\",
              \"perfumetiktok\",
              \"perfume\",
              \"fragrance\",
              \"fragrancetiktok\"
            ],
            \"posts\": [
              \"7436474042036522248\",
              \"7486253493716536584\",
              \"7503974461725740295\"
            ],
            \"url_title\": \"Perfume\"
          }
        }
      }
    }
    ```

    Args:
        id (str): 产品类目ID/Product category ID
        last (Union[Unset, int]): 最近天数/Last days Default: 30.
        ecom_type (Union[Unset, str]): 电商类型/E-commerce type Default: 'l3'.
        period_type (Union[Unset, str]): 时间类型/Period type Default: 'last'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        id=id,
        last=last,
        ecom_type=ecom_type,
        period_type=period_type,
        country_code=country_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: str,
    last: Union[Unset, int] = 30,
    ecom_type: Union[Unset, str] = "l3",
    period_type: Union[Unset, str] = "last",
    country_code: Union[Unset, str] = "US",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取产品详细信息/Get product detail

     # [中文]
    ### 用途:
    - 获取特定产品类目的完整详细信息
    - 包括受众分析、热门标签、相关帖子等多维度数据
    - 为产品营销策略提供全面的数据支持

    ### 参数:
    - id: 产品类目ID，如香水：601583
    - last: 最近天数，如7、30天
    - ecom_type: 电商类型，默认\"l3\"
    - period_type: 时间类型，默认\"last\"

    ### 返回内容说明:
    - `info`: 产品详细信息
      - `audience_ages`: 受众年龄分布
        - `age_level`: 年龄数值
        - `score`: 占比分数
      - `audience_interests`: 受众兴趣分布
        - `interest_info`: 兴趣信息
          - `id`: 兴趣ID
          - `label`: 兴趣标签
          - `value`: 兴趣名称
        - `score`: 占比分数
      - `cover_url`: 封面图URL（可能为null）
      - `ecom_type`: 电商类型
      - `first_ecom_category`: 一级电商类目
        - `id`: 类目ID
        - `label`: 类目标签
        - `value`: 类目名称
      - `hashtags`: 热门标签列表
      - `posts`: 相关帖子列表
      - `second_ecom_category`: 二级电商类目
      - `third_ecom_category`: 三级电商类目
      - `url_title`: URL标题

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_product_detail\",
      \"params\": {
        \"id\": \"601583\",
        \"last\": \"30\",
        \"ecom_type\": \"l3\",
        \"period_type\": \"last\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"info\": {
            \"audience_ages\": [
              {
                \"age_level\": 35,
                \"score\": 27
              },
              {
                \"age_level\": 25,
                \"score\": 22
              },
              {
                \"age_level\": 18,
                \"score\": 22
              },
              {
                \"age_level\": 45,
                \"score\": 18
              },
              {
                \"age_level\": 55,
                \"score\": 11
              }
            ],
            \"audience_interests\": [
              {
                \"interest_info\": {
                  \"id\": \"13105000000\",
                  \"label\": \"label_13105000000\",
                  \"value\": \"Pawn Shops\"
                },
                \"score\": 135
              },
              {
                \"interest_info\": {
                  \"id\": \"24104000000\",
                  \"label\": \"label_24104000000\",
                  \"value\": \"Electronics & Electrical\"
                },
                \"score\": 127
              }
            ],
            \"cover_url\": null,
            \"ecom_type\": \"l3\",
            \"first_ecom_category\": {
              \"id\": \"601450\",
              \"label\": \"category_601450\",
              \"value\": \"Beauty & Personal Care\"
            },
            \"hashtags\": [
              \"vlog\",
              \"perfumetiktok\",
              \"perfume\",
              \"fragrance\",
              \"fragrancetiktok\"
            ],
            \"posts\": [
              \"7436474042036522248\",
              \"7486253493716536584\",
              \"7503974461725740295\"
            ],
            \"url_title\": \"Perfume\"
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get complete detailed information for specific product categories
    - Includes multi-dimensional data like audience analysis, popular hashtags, related posts
    - Provide comprehensive data support for product marketing strategies

    ### Parameters:
    - id: Product category ID, e.g., Perfume: 601583
    - last: Number of recent days, e.g., 7, 30 days
    - ecom_type: E-commerce type, default \"l3\"
    - period_type: Period type, default \"last\"

    ### Return Description:
    - `info`: Product detailed information
      - `audience_ages`: Audience age distribution
        - `age_level`: Age value
        - `score`: Score value
      - `audience_interests`: Audience interest distribution
        - `interest_info`: Interest information
          - `id`: Interest ID
          - `label`: Interest label
          - `value`: Interest name
        - `score`: Score value
      - `cover_url`: Cover image URL (may be null)
      - `ecom_type`: E-commerce type
      - `first_ecom_category`: First-level e-commerce category
        - `id`: Category ID
        - `label`: Category label
        - `value`: Category name
      - `hashtags`: Popular hashtags list
      - `posts`: Related posts list
      - `second_ecom_category`: Second-level e-commerce category
      - `third_ecom_category`: Third-level e-commerce category
      - `url_title`: URL title

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_product_detail\",
      \"params\": {
        \"id\": \"601583\",
        \"last\": \"30\",
        \"ecom_type\": \"l3\",
        \"period_type\": \"last\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"info\": {
            \"audience_ages\": [
              {
                \"age_level\": 35,
                \"score\": 27
              },
              {
                \"age_level\": 25,
                \"score\": 22
              },
              {
                \"age_level\": 18,
                \"score\": 22
              },
              {
                \"age_level\": 45,
                \"score\": 18
              },
              {
                \"age_level\": 55,
                \"score\": 11
              }
            ],
            \"audience_interests\": [
              {
                \"interest_info\": {
                  \"id\": \"13105000000\",
                  \"label\": \"label_13105000000\",
                  \"value\": \"Pawn Shops\"
                },
                \"score\": 135
              },
              {
                \"interest_info\": {
                  \"id\": \"24104000000\",
                  \"label\": \"label_24104000000\",
                  \"value\": \"Electronics & Electrical\"
                },
                \"score\": 127
              }
            ],
            \"cover_url\": null,
            \"ecom_type\": \"l3\",
            \"first_ecom_category\": {
              \"id\": \"601450\",
              \"label\": \"category_601450\",
              \"value\": \"Beauty & Personal Care\"
            },
            \"hashtags\": [
              \"vlog\",
              \"perfumetiktok\",
              \"perfume\",
              \"fragrance\",
              \"fragrancetiktok\"
            ],
            \"posts\": [
              \"7436474042036522248\",
              \"7486253493716536584\",
              \"7503974461725740295\"
            ],
            \"url_title\": \"Perfume\"
          }
        }
      }
    }
    ```

    Args:
        id (str): 产品类目ID/Product category ID
        last (Union[Unset, int]): 最近天数/Last days Default: 30.
        ecom_type (Union[Unset, str]): 电商类型/E-commerce type Default: 'l3'.
        period_type (Union[Unset, str]): 时间类型/Period type Default: 'last'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        id=id,
        last=last,
        ecom_type=ecom_type,
        period_type=period_type,
        country_code=country_code,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: str,
    last: Union[Unset, int] = 30,
    ecom_type: Union[Unset, str] = "l3",
    period_type: Union[Unset, str] = "last",
    country_code: Union[Unset, str] = "US",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取产品详细信息/Get product detail

     # [中文]
    ### 用途:
    - 获取特定产品类目的完整详细信息
    - 包括受众分析、热门标签、相关帖子等多维度数据
    - 为产品营销策略提供全面的数据支持

    ### 参数:
    - id: 产品类目ID，如香水：601583
    - last: 最近天数，如7、30天
    - ecom_type: 电商类型，默认\"l3\"
    - period_type: 时间类型，默认\"last\"

    ### 返回内容说明:
    - `info`: 产品详细信息
      - `audience_ages`: 受众年龄分布
        - `age_level`: 年龄数值
        - `score`: 占比分数
      - `audience_interests`: 受众兴趣分布
        - `interest_info`: 兴趣信息
          - `id`: 兴趣ID
          - `label`: 兴趣标签
          - `value`: 兴趣名称
        - `score`: 占比分数
      - `cover_url`: 封面图URL（可能为null）
      - `ecom_type`: 电商类型
      - `first_ecom_category`: 一级电商类目
        - `id`: 类目ID
        - `label`: 类目标签
        - `value`: 类目名称
      - `hashtags`: 热门标签列表
      - `posts`: 相关帖子列表
      - `second_ecom_category`: 二级电商类目
      - `third_ecom_category`: 三级电商类目
      - `url_title`: URL标题

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_product_detail\",
      \"params\": {
        \"id\": \"601583\",
        \"last\": \"30\",
        \"ecom_type\": \"l3\",
        \"period_type\": \"last\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"info\": {
            \"audience_ages\": [
              {
                \"age_level\": 35,
                \"score\": 27
              },
              {
                \"age_level\": 25,
                \"score\": 22
              },
              {
                \"age_level\": 18,
                \"score\": 22
              },
              {
                \"age_level\": 45,
                \"score\": 18
              },
              {
                \"age_level\": 55,
                \"score\": 11
              }
            ],
            \"audience_interests\": [
              {
                \"interest_info\": {
                  \"id\": \"13105000000\",
                  \"label\": \"label_13105000000\",
                  \"value\": \"Pawn Shops\"
                },
                \"score\": 135
              },
              {
                \"interest_info\": {
                  \"id\": \"24104000000\",
                  \"label\": \"label_24104000000\",
                  \"value\": \"Electronics & Electrical\"
                },
                \"score\": 127
              }
            ],
            \"cover_url\": null,
            \"ecom_type\": \"l3\",
            \"first_ecom_category\": {
              \"id\": \"601450\",
              \"label\": \"category_601450\",
              \"value\": \"Beauty & Personal Care\"
            },
            \"hashtags\": [
              \"vlog\",
              \"perfumetiktok\",
              \"perfume\",
              \"fragrance\",
              \"fragrancetiktok\"
            ],
            \"posts\": [
              \"7436474042036522248\",
              \"7486253493716536584\",
              \"7503974461725740295\"
            ],
            \"url_title\": \"Perfume\"
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get complete detailed information for specific product categories
    - Includes multi-dimensional data like audience analysis, popular hashtags, related posts
    - Provide comprehensive data support for product marketing strategies

    ### Parameters:
    - id: Product category ID, e.g., Perfume: 601583
    - last: Number of recent days, e.g., 7, 30 days
    - ecom_type: E-commerce type, default \"l3\"
    - period_type: Period type, default \"last\"

    ### Return Description:
    - `info`: Product detailed information
      - `audience_ages`: Audience age distribution
        - `age_level`: Age value
        - `score`: Score value
      - `audience_interests`: Audience interest distribution
        - `interest_info`: Interest information
          - `id`: Interest ID
          - `label`: Interest label
          - `value`: Interest name
        - `score`: Score value
      - `cover_url`: Cover image URL (may be null)
      - `ecom_type`: E-commerce type
      - `first_ecom_category`: First-level e-commerce category
        - `id`: Category ID
        - `label`: Category label
        - `value`: Category name
      - `hashtags`: Popular hashtags list
      - `posts`: Related posts list
      - `second_ecom_category`: Second-level e-commerce category
      - `third_ecom_category`: Third-level e-commerce category
      - `url_title`: URL title

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_product_detail\",
      \"params\": {
        \"id\": \"601583\",
        \"last\": \"30\",
        \"ecom_type\": \"l3\",
        \"period_type\": \"last\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"info\": {
            \"audience_ages\": [
              {
                \"age_level\": 35,
                \"score\": 27
              },
              {
                \"age_level\": 25,
                \"score\": 22
              },
              {
                \"age_level\": 18,
                \"score\": 22
              },
              {
                \"age_level\": 45,
                \"score\": 18
              },
              {
                \"age_level\": 55,
                \"score\": 11
              }
            ],
            \"audience_interests\": [
              {
                \"interest_info\": {
                  \"id\": \"13105000000\",
                  \"label\": \"label_13105000000\",
                  \"value\": \"Pawn Shops\"
                },
                \"score\": 135
              },
              {
                \"interest_info\": {
                  \"id\": \"24104000000\",
                  \"label\": \"label_24104000000\",
                  \"value\": \"Electronics & Electrical\"
                },
                \"score\": 127
              }
            ],
            \"cover_url\": null,
            \"ecom_type\": \"l3\",
            \"first_ecom_category\": {
              \"id\": \"601450\",
              \"label\": \"category_601450\",
              \"value\": \"Beauty & Personal Care\"
            },
            \"hashtags\": [
              \"vlog\",
              \"perfumetiktok\",
              \"perfume\",
              \"fragrance\",
              \"fragrancetiktok\"
            ],
            \"posts\": [
              \"7436474042036522248\",
              \"7486253493716536584\",
              \"7503974461725740295\"
            ],
            \"url_title\": \"Perfume\"
          }
        }
      }
    }
    ```

    Args:
        id (str): 产品类目ID/Product category ID
        last (Union[Unset, int]): 最近天数/Last days Default: 30.
        ecom_type (Union[Unset, str]): 电商类型/E-commerce type Default: 'l3'.
        period_type (Union[Unset, str]): 时间类型/Period type Default: 'last'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        id=id,
        last=last,
        ecom_type=ecom_type,
        period_type=period_type,
        country_code=country_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: str,
    last: Union[Unset, int] = 30,
    ecom_type: Union[Unset, str] = "l3",
    period_type: Union[Unset, str] = "last",
    country_code: Union[Unset, str] = "US",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取产品详细信息/Get product detail

     # [中文]
    ### 用途:
    - 获取特定产品类目的完整详细信息
    - 包括受众分析、热门标签、相关帖子等多维度数据
    - 为产品营销策略提供全面的数据支持

    ### 参数:
    - id: 产品类目ID，如香水：601583
    - last: 最近天数，如7、30天
    - ecom_type: 电商类型，默认\"l3\"
    - period_type: 时间类型，默认\"last\"

    ### 返回内容说明:
    - `info`: 产品详细信息
      - `audience_ages`: 受众年龄分布
        - `age_level`: 年龄数值
        - `score`: 占比分数
      - `audience_interests`: 受众兴趣分布
        - `interest_info`: 兴趣信息
          - `id`: 兴趣ID
          - `label`: 兴趣标签
          - `value`: 兴趣名称
        - `score`: 占比分数
      - `cover_url`: 封面图URL（可能为null）
      - `ecom_type`: 电商类型
      - `first_ecom_category`: 一级电商类目
        - `id`: 类目ID
        - `label`: 类目标签
        - `value`: 类目名称
      - `hashtags`: 热门标签列表
      - `posts`: 相关帖子列表
      - `second_ecom_category`: 二级电商类目
      - `third_ecom_category`: 三级电商类目
      - `url_title`: URL标题

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_product_detail\",
      \"params\": {
        \"id\": \"601583\",
        \"last\": \"30\",
        \"ecom_type\": \"l3\",
        \"period_type\": \"last\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"info\": {
            \"audience_ages\": [
              {
                \"age_level\": 35,
                \"score\": 27
              },
              {
                \"age_level\": 25,
                \"score\": 22
              },
              {
                \"age_level\": 18,
                \"score\": 22
              },
              {
                \"age_level\": 45,
                \"score\": 18
              },
              {
                \"age_level\": 55,
                \"score\": 11
              }
            ],
            \"audience_interests\": [
              {
                \"interest_info\": {
                  \"id\": \"13105000000\",
                  \"label\": \"label_13105000000\",
                  \"value\": \"Pawn Shops\"
                },
                \"score\": 135
              },
              {
                \"interest_info\": {
                  \"id\": \"24104000000\",
                  \"label\": \"label_24104000000\",
                  \"value\": \"Electronics & Electrical\"
                },
                \"score\": 127
              }
            ],
            \"cover_url\": null,
            \"ecom_type\": \"l3\",
            \"first_ecom_category\": {
              \"id\": \"601450\",
              \"label\": \"category_601450\",
              \"value\": \"Beauty & Personal Care\"
            },
            \"hashtags\": [
              \"vlog\",
              \"perfumetiktok\",
              \"perfume\",
              \"fragrance\",
              \"fragrancetiktok\"
            ],
            \"posts\": [
              \"7436474042036522248\",
              \"7486253493716536584\",
              \"7503974461725740295\"
            ],
            \"url_title\": \"Perfume\"
          }
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get complete detailed information for specific product categories
    - Includes multi-dimensional data like audience analysis, popular hashtags, related posts
    - Provide comprehensive data support for product marketing strategies

    ### Parameters:
    - id: Product category ID, e.g., Perfume: 601583
    - last: Number of recent days, e.g., 7, 30 days
    - ecom_type: E-commerce type, default \"l3\"
    - period_type: Period type, default \"last\"

    ### Return Description:
    - `info`: Product detailed information
      - `audience_ages`: Audience age distribution
        - `age_level`: Age value
        - `score`: Score value
      - `audience_interests`: Audience interest distribution
        - `interest_info`: Interest information
          - `id`: Interest ID
          - `label`: Interest label
          - `value`: Interest name
        - `score`: Score value
      - `cover_url`: Cover image URL (may be null)
      - `ecom_type`: E-commerce type
      - `first_ecom_category`: First-level e-commerce category
        - `id`: Category ID
        - `label`: Category label
        - `value`: Category name
      - `hashtags`: Popular hashtags list
      - `posts`: Related posts list
      - `second_ecom_category`: Second-level e-commerce category
      - `third_ecom_category`: Third-level e-commerce category
      - `url_title`: URL title

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_product_detail\",
      \"params\": {
        \"id\": \"601583\",
        \"last\": \"30\",
        \"ecom_type\": \"l3\",
        \"period_type\": \"last\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"info\": {
            \"audience_ages\": [
              {
                \"age_level\": 35,
                \"score\": 27
              },
              {
                \"age_level\": 25,
                \"score\": 22
              },
              {
                \"age_level\": 18,
                \"score\": 22
              },
              {
                \"age_level\": 45,
                \"score\": 18
              },
              {
                \"age_level\": 55,
                \"score\": 11
              }
            ],
            \"audience_interests\": [
              {
                \"interest_info\": {
                  \"id\": \"13105000000\",
                  \"label\": \"label_13105000000\",
                  \"value\": \"Pawn Shops\"
                },
                \"score\": 135
              },
              {
                \"interest_info\": {
                  \"id\": \"24104000000\",
                  \"label\": \"label_24104000000\",
                  \"value\": \"Electronics & Electrical\"
                },
                \"score\": 127
              }
            ],
            \"cover_url\": null,
            \"ecom_type\": \"l3\",
            \"first_ecom_category\": {
              \"id\": \"601450\",
              \"label\": \"category_601450\",
              \"value\": \"Beauty & Personal Care\"
            },
            \"hashtags\": [
              \"vlog\",
              \"perfumetiktok\",
              \"perfume\",
              \"fragrance\",
              \"fragrancetiktok\"
            ],
            \"posts\": [
              \"7436474042036522248\",
              \"7486253493716536584\",
              \"7503974461725740295\"
            ],
            \"url_title\": \"Perfume\"
          }
        }
      }
    }
    ```

    Args:
        id (str): 产品类目ID/Product category ID
        last (Union[Unset, int]): 最近天数/Last days Default: 30.
        ecom_type (Union[Unset, str]): 电商类型/E-commerce type Default: 'l3'.
        period_type (Union[Unset, str]): 时间类型/Period type Default: 'last'.
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
            id=id,
            last=last,
            ecom_type=ecom_type,
            period_type=period_type,
            country_code=country_code,
        )
    ).parsed
