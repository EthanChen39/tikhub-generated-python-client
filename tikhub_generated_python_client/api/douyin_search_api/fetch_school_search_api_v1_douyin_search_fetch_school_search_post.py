from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...models.school_search_request import SchoolSearchRequest
from ...types import Response


def _get_kwargs(
    *,
    body: SchoolSearchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/search/fetch_school_search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: SchoolSearchRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取学校搜索/Fetch school search

     # [中文]
    ### 用途:
    - 获取抖音 App 中学校信息的搜索结果。
    - 根据关键词返回学校名称列表，常用于用户设置学校资料、兴趣推荐等场景。

    ### 备注:
    - 本接口专注于学校信息搜索，仅返回学校的名称字段。
    - 初次请求时 `cursor` 应传 0，分页时使用上一次返回的 `cursor`。
    - 本接口响应体较简单，适合快速检索学校数据。

    ### 参数:
    - keyword: 搜索关键词，如学校名称 \"北京大学\"、地区名 \"北京\"

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"北京大学\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `schools[]`: 学校列表
      - `name`: 学校名称（如 \"北京大学\"、\"北京四中\"）
    - `extra`:
      - `now`: 当前服务器时间戳（毫秒）
      - `logid`: 请求日志ID
      - `fatal_item_ids`: 错误项目ID列表（通常为空）
    - `log_pb`:
      - `impr_id`: 曝光追踪ID（用于链路追踪）
    - `status_code`: 状态码（0=成功）
    - `status_msg`: 状态信息（通常为空）

    # [English]
    ### Purpose:
    - Fetch school information search results from Douyin App.
    - Returns a list of school names based on the input keyword, useful for user profile settings,
    school recommendations, etc.

    ### Notes:
    - This API focuses on school information search, and only returns school names.
    - Set `cursor` to 0 for the first request; for pagination, use the cursor from the last response.
    - The response structure is simple and lightweight for fast lookup.

    ### Parameters:
    - keyword: Search keyword, e.g., school name \"Peking University\" or city \"Beijing\"

    ### Example Request Body:
    ```json
    payload = {
        \"keyword\": \"Peking University\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `schools[]`: List of schools
      - `name`: School name (e.g., \"Peking University\", \"Beijing No.4 High School\")
    - `extra`:
      - `now`: Server timestamp in milliseconds
      - `logid`: Log ID for request tracing
      - `fatal_item_ids`: List of fatal item IDs (usually empty)
    - `log_pb`:
      - `impr_id`: Impression ID for tracking
    - `status_code`: Status code (0=success)
    - `status_msg`: Status message (usually empty)

    Args:
        body (SchoolSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: SchoolSearchRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取学校搜索/Fetch school search

     # [中文]
    ### 用途:
    - 获取抖音 App 中学校信息的搜索结果。
    - 根据关键词返回学校名称列表，常用于用户设置学校资料、兴趣推荐等场景。

    ### 备注:
    - 本接口专注于学校信息搜索，仅返回学校的名称字段。
    - 初次请求时 `cursor` 应传 0，分页时使用上一次返回的 `cursor`。
    - 本接口响应体较简单，适合快速检索学校数据。

    ### 参数:
    - keyword: 搜索关键词，如学校名称 \"北京大学\"、地区名 \"北京\"

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"北京大学\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `schools[]`: 学校列表
      - `name`: 学校名称（如 \"北京大学\"、\"北京四中\"）
    - `extra`:
      - `now`: 当前服务器时间戳（毫秒）
      - `logid`: 请求日志ID
      - `fatal_item_ids`: 错误项目ID列表（通常为空）
    - `log_pb`:
      - `impr_id`: 曝光追踪ID（用于链路追踪）
    - `status_code`: 状态码（0=成功）
    - `status_msg`: 状态信息（通常为空）

    # [English]
    ### Purpose:
    - Fetch school information search results from Douyin App.
    - Returns a list of school names based on the input keyword, useful for user profile settings,
    school recommendations, etc.

    ### Notes:
    - This API focuses on school information search, and only returns school names.
    - Set `cursor` to 0 for the first request; for pagination, use the cursor from the last response.
    - The response structure is simple and lightweight for fast lookup.

    ### Parameters:
    - keyword: Search keyword, e.g., school name \"Peking University\" or city \"Beijing\"

    ### Example Request Body:
    ```json
    payload = {
        \"keyword\": \"Peking University\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `schools[]`: List of schools
      - `name`: School name (e.g., \"Peking University\", \"Beijing No.4 High School\")
    - `extra`:
      - `now`: Server timestamp in milliseconds
      - `logid`: Log ID for request tracing
      - `fatal_item_ids`: List of fatal item IDs (usually empty)
    - `log_pb`:
      - `impr_id`: Impression ID for tracking
    - `status_code`: Status code (0=success)
    - `status_msg`: Status message (usually empty)

    Args:
        body (SchoolSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SchoolSearchRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取学校搜索/Fetch school search

     # [中文]
    ### 用途:
    - 获取抖音 App 中学校信息的搜索结果。
    - 根据关键词返回学校名称列表，常用于用户设置学校资料、兴趣推荐等场景。

    ### 备注:
    - 本接口专注于学校信息搜索，仅返回学校的名称字段。
    - 初次请求时 `cursor` 应传 0，分页时使用上一次返回的 `cursor`。
    - 本接口响应体较简单，适合快速检索学校数据。

    ### 参数:
    - keyword: 搜索关键词，如学校名称 \"北京大学\"、地区名 \"北京\"

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"北京大学\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `schools[]`: 学校列表
      - `name`: 学校名称（如 \"北京大学\"、\"北京四中\"）
    - `extra`:
      - `now`: 当前服务器时间戳（毫秒）
      - `logid`: 请求日志ID
      - `fatal_item_ids`: 错误项目ID列表（通常为空）
    - `log_pb`:
      - `impr_id`: 曝光追踪ID（用于链路追踪）
    - `status_code`: 状态码（0=成功）
    - `status_msg`: 状态信息（通常为空）

    # [English]
    ### Purpose:
    - Fetch school information search results from Douyin App.
    - Returns a list of school names based on the input keyword, useful for user profile settings,
    school recommendations, etc.

    ### Notes:
    - This API focuses on school information search, and only returns school names.
    - Set `cursor` to 0 for the first request; for pagination, use the cursor from the last response.
    - The response structure is simple and lightweight for fast lookup.

    ### Parameters:
    - keyword: Search keyword, e.g., school name \"Peking University\" or city \"Beijing\"

    ### Example Request Body:
    ```json
    payload = {
        \"keyword\": \"Peking University\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `schools[]`: List of schools
      - `name`: School name (e.g., \"Peking University\", \"Beijing No.4 High School\")
    - `extra`:
      - `now`: Server timestamp in milliseconds
      - `logid`: Log ID for request tracing
      - `fatal_item_ids`: List of fatal item IDs (usually empty)
    - `log_pb`:
      - `impr_id`: Impression ID for tracking
    - `status_code`: Status code (0=success)
    - `status_msg`: Status message (usually empty)

    Args:
        body (SchoolSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SchoolSearchRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取学校搜索/Fetch school search

     # [中文]
    ### 用途:
    - 获取抖音 App 中学校信息的搜索结果。
    - 根据关键词返回学校名称列表，常用于用户设置学校资料、兴趣推荐等场景。

    ### 备注:
    - 本接口专注于学校信息搜索，仅返回学校的名称字段。
    - 初次请求时 `cursor` 应传 0，分页时使用上一次返回的 `cursor`。
    - 本接口响应体较简单，适合快速检索学校数据。

    ### 参数:
    - keyword: 搜索关键词，如学校名称 \"北京大学\"、地区名 \"北京\"

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"北京大学\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `schools[]`: 学校列表
      - `name`: 学校名称（如 \"北京大学\"、\"北京四中\"）
    - `extra`:
      - `now`: 当前服务器时间戳（毫秒）
      - `logid`: 请求日志ID
      - `fatal_item_ids`: 错误项目ID列表（通常为空）
    - `log_pb`:
      - `impr_id`: 曝光追踪ID（用于链路追踪）
    - `status_code`: 状态码（0=成功）
    - `status_msg`: 状态信息（通常为空）

    # [English]
    ### Purpose:
    - Fetch school information search results from Douyin App.
    - Returns a list of school names based on the input keyword, useful for user profile settings,
    school recommendations, etc.

    ### Notes:
    - This API focuses on school information search, and only returns school names.
    - Set `cursor` to 0 for the first request; for pagination, use the cursor from the last response.
    - The response structure is simple and lightweight for fast lookup.

    ### Parameters:
    - keyword: Search keyword, e.g., school name \"Peking University\" or city \"Beijing\"

    ### Example Request Body:
    ```json
    payload = {
        \"keyword\": \"Peking University\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `schools[]`: List of schools
      - `name`: School name (e.g., \"Peking University\", \"Beijing No.4 High School\")
    - `extra`:
      - `now`: Server timestamp in milliseconds
      - `logid`: Log ID for request tracing
      - `fatal_item_ids`: List of fatal item IDs (usually empty)
    - `log_pb`:
      - `impr_id`: Impression ID for tracking
    - `status_code`: Status code (0=success)
    - `status_msg`: Status message (usually empty)

    Args:
        body (SchoolSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
