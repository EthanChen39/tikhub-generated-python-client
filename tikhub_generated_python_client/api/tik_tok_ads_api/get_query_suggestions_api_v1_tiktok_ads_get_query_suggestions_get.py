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
    count: Union[Unset, int] = 50,
    scenario: Union[Unset, int] = 1,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["count"] = count

    params["scenario"] = scenario

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/ads/get_query_suggestions",
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
    count: Union[Unset, int] = 50,
    scenario: Union[Unset, int] = 1,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取查询建议/Get query suggestions

     # [中文]
    ### 用途:
    - 获取广告搜索的热门查询建议
    - 了解当前流行的广告搜索关键词和趋势
    - 帮助发现新的广告创意方向和热点话题

    ### 参数:
    - count: 返回的建议数量，默认50
    - scenario: 场景类型，默认1

    ### 返回内容说明:
    - `query`: 查询建议列表（字符串数组）

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_query_suggestions\",
      \"params\": {
        \"count\": \"50\",
        \"scenario\": \"1\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"query\": [
            \"shop now\",
            \"50% off\"
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get popular query suggestions for ad search
    - Understand current popular ad search keywords and trends
    - Help discover new creative directions and hot topics

    ### Parameters:
    - count: Number of suggestions to return, default 50
    - scenario: Scenario type, default 1

    ### Return Description:
    - `query`: Query suggestions list (string array)

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_query_suggestions\",
      \"params\": {
        \"count\": \"50\",
        \"scenario\": \"1\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"query\": [
            \"shop now\",
            \"50% off\"
          ]
        }
      }
    }
    ```

    Args:
        count (Union[Unset, int]): 建议数量/Suggestion count Default: 50.
        scenario (Union[Unset, int]): 场景类型/Scenario type Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        count=count,
        scenario=scenario,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    count: Union[Unset, int] = 50,
    scenario: Union[Unset, int] = 1,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取查询建议/Get query suggestions

     # [中文]
    ### 用途:
    - 获取广告搜索的热门查询建议
    - 了解当前流行的广告搜索关键词和趋势
    - 帮助发现新的广告创意方向和热点话题

    ### 参数:
    - count: 返回的建议数量，默认50
    - scenario: 场景类型，默认1

    ### 返回内容说明:
    - `query`: 查询建议列表（字符串数组）

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_query_suggestions\",
      \"params\": {
        \"count\": \"50\",
        \"scenario\": \"1\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"query\": [
            \"shop now\",
            \"50% off\"
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get popular query suggestions for ad search
    - Understand current popular ad search keywords and trends
    - Help discover new creative directions and hot topics

    ### Parameters:
    - count: Number of suggestions to return, default 50
    - scenario: Scenario type, default 1

    ### Return Description:
    - `query`: Query suggestions list (string array)

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_query_suggestions\",
      \"params\": {
        \"count\": \"50\",
        \"scenario\": \"1\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"query\": [
            \"shop now\",
            \"50% off\"
          ]
        }
      }
    }
    ```

    Args:
        count (Union[Unset, int]): 建议数量/Suggestion count Default: 50.
        scenario (Union[Unset, int]): 场景类型/Scenario type Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        count=count,
        scenario=scenario,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    count: Union[Unset, int] = 50,
    scenario: Union[Unset, int] = 1,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取查询建议/Get query suggestions

     # [中文]
    ### 用途:
    - 获取广告搜索的热门查询建议
    - 了解当前流行的广告搜索关键词和趋势
    - 帮助发现新的广告创意方向和热点话题

    ### 参数:
    - count: 返回的建议数量，默认50
    - scenario: 场景类型，默认1

    ### 返回内容说明:
    - `query`: 查询建议列表（字符串数组）

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_query_suggestions\",
      \"params\": {
        \"count\": \"50\",
        \"scenario\": \"1\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"query\": [
            \"shop now\",
            \"50% off\"
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get popular query suggestions for ad search
    - Understand current popular ad search keywords and trends
    - Help discover new creative directions and hot topics

    ### Parameters:
    - count: Number of suggestions to return, default 50
    - scenario: Scenario type, default 1

    ### Return Description:
    - `query`: Query suggestions list (string array)

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_query_suggestions\",
      \"params\": {
        \"count\": \"50\",
        \"scenario\": \"1\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"query\": [
            \"shop now\",
            \"50% off\"
          ]
        }
      }
    }
    ```

    Args:
        count (Union[Unset, int]): 建议数量/Suggestion count Default: 50.
        scenario (Union[Unset, int]): 场景类型/Scenario type Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        count=count,
        scenario=scenario,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    count: Union[Unset, int] = 50,
    scenario: Union[Unset, int] = 1,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取查询建议/Get query suggestions

     # [中文]
    ### 用途:
    - 获取广告搜索的热门查询建议
    - 了解当前流行的广告搜索关键词和趋势
    - 帮助发现新的广告创意方向和热点话题

    ### 参数:
    - count: 返回的建议数量，默认50
    - scenario: 场景类型，默认1

    ### 返回内容说明:
    - `query`: 查询建议列表（字符串数组）

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_query_suggestions\",
      \"params\": {
        \"count\": \"50\",
        \"scenario\": \"1\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"query\": [
            \"shop now\",
            \"50% off\"
          ]
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Get popular query suggestions for ad search
    - Understand current popular ad search keywords and trends
    - Help discover new creative directions and hot topics

    ### Parameters:
    - count: Number of suggestions to return, default 50
    - scenario: Scenario type, default 1

    ### Return Description:
    - `query`: Query suggestions list (string array)

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/ads/get_query_suggestions\",
      \"params\": {
        \"count\": \"50\",
        \"scenario\": \"1\"
      },
      \"data\": {
        \"code\": 0,
        \"msg\": \"OK\",
        \"data\": {
          \"query\": [
            \"shop now\",
            \"50% off\"
          ]
        }
      }
    }
    ```

    Args:
        count (Union[Unset, int]): 建议数量/Suggestion count Default: 50.
        scenario (Union[Unset, int]): 场景类型/Scenario type Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            count=count,
            scenario=scenario,
        )
    ).parsed
