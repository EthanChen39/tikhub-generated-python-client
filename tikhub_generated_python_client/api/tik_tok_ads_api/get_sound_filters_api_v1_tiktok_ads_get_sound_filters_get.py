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
    rank_type: Union[Unset, str] = "popular",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["rank_type"] = rank_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/get_sound_filters",
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
    rank_type: Union[Unset, str] = "popular",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取音乐筛选器/Get sound filters

     # [中文]
    ### 用途:
    - 获取热门音乐功能的可用筛选选项
    - 了解不同排行类型下的筛选维度
    - 为音乐选择提供参数参考

    ### 参数:
    - rank_type: 排行类型，\"popular\"=热门，\"surging\"=上升最快

    ### 返回内容说明:
    - `country`: 国家列表
      - `id`: 国家ID
      - `value`: 国家名称
      - `label`: 国家标签

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_filters\",
      \"params\": {
        \"rank_type\": \"popular\"
      },
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
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get available filter options for popular music functionality
    - Understand filter dimensions for different ranking types
    - Provide parameter reference for music selection

    ### Parameters:
    - rank_type: Ranking type, \"popular\"=Popular, \"surging\"=Fastest rising

    ### Return Description:
    - `country`: Country list
      - `id`: Country ID
      - `value`: Country name
      - `label`: Country label

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_filters\",
      \"params\": {
        \"rank_type\": \"popular\"
      },
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
          ]
        }
      }
    }
    ```

    Args:
        rank_type (Union[Unset, str]): 排行类型/Rank type (popular, surging) Default: 'popular'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        rank_type=rank_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    rank_type: Union[Unset, str] = "popular",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取音乐筛选器/Get sound filters

     # [中文]
    ### 用途:
    - 获取热门音乐功能的可用筛选选项
    - 了解不同排行类型下的筛选维度
    - 为音乐选择提供参数参考

    ### 参数:
    - rank_type: 排行类型，\"popular\"=热门，\"surging\"=上升最快

    ### 返回内容说明:
    - `country`: 国家列表
      - `id`: 国家ID
      - `value`: 国家名称
      - `label`: 国家标签

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_filters\",
      \"params\": {
        \"rank_type\": \"popular\"
      },
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
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get available filter options for popular music functionality
    - Understand filter dimensions for different ranking types
    - Provide parameter reference for music selection

    ### Parameters:
    - rank_type: Ranking type, \"popular\"=Popular, \"surging\"=Fastest rising

    ### Return Description:
    - `country`: Country list
      - `id`: Country ID
      - `value`: Country name
      - `label`: Country label

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_filters\",
      \"params\": {
        \"rank_type\": \"popular\"
      },
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
          ]
        }
      }
    }
    ```

    Args:
        rank_type (Union[Unset, str]): 排行类型/Rank type (popular, surging) Default: 'popular'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        rank_type=rank_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    rank_type: Union[Unset, str] = "popular",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取音乐筛选器/Get sound filters

     # [中文]
    ### 用途:
    - 获取热门音乐功能的可用筛选选项
    - 了解不同排行类型下的筛选维度
    - 为音乐选择提供参数参考

    ### 参数:
    - rank_type: 排行类型，\"popular\"=热门，\"surging\"=上升最快

    ### 返回内容说明:
    - `country`: 国家列表
      - `id`: 国家ID
      - `value`: 国家名称
      - `label`: 国家标签

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_filters\",
      \"params\": {
        \"rank_type\": \"popular\"
      },
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
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get available filter options for popular music functionality
    - Understand filter dimensions for different ranking types
    - Provide parameter reference for music selection

    ### Parameters:
    - rank_type: Ranking type, \"popular\"=Popular, \"surging\"=Fastest rising

    ### Return Description:
    - `country`: Country list
      - `id`: Country ID
      - `value`: Country name
      - `label`: Country label

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_filters\",
      \"params\": {
        \"rank_type\": \"popular\"
      },
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
          ]
        }
      }
    }
    ```

    Args:
        rank_type (Union[Unset, str]): 排行类型/Rank type (popular, surging) Default: 'popular'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        rank_type=rank_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    rank_type: Union[Unset, str] = "popular",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取音乐筛选器/Get sound filters

     # [中文]
    ### 用途:
    - 获取热门音乐功能的可用筛选选项
    - 了解不同排行类型下的筛选维度
    - 为音乐选择提供参数参考

    ### 参数:
    - rank_type: 排行类型，\"popular\"=热门，\"surging\"=上升最快

    ### 返回内容说明:
    - `country`: 国家列表
      - `id`: 国家ID
      - `value`: 国家名称
      - `label`: 国家标签

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_filters\",
      \"params\": {
        \"rank_type\": \"popular\"
      },
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
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get available filter options for popular music functionality
    - Understand filter dimensions for different ranking types
    - Provide parameter reference for music selection

    ### Parameters:
    - rank_type: Ranking type, \"popular\"=Popular, \"surging\"=Fastest rising

    ### Return Description:
    - `country`: Country list
      - `id`: Country ID
      - `value`: Country name
      - `label`: Country label

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_sound_filters\",
      \"params\": {
        \"rank_type\": \"popular\"
      },
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
          ]
        }
      }
    }
    ```

    Args:
        rank_type (Union[Unset, str]): 排行类型/Rank type (popular, surging) Default: 'popular'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            rank_type=rank_type,
        )
    ).parsed
