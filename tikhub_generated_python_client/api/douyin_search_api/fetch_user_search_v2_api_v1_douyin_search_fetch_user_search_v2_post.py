from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...models.user_search_request_v2 import UserSearchRequestV2
from ...types import Response


def _get_kwargs(
    *,
    body: UserSearchRequestV2,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/search/fetch_user_search_v2",
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
    body: UserSearchRequestV2,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户搜索 V2/Fetch user search V2

     # [中文]
    ### 用途:
    - 获取抖音 App 中根据关键词搜索到的用户列表。
    - 不支持粉丝数量、用户类型筛选查询。

    ### 备注:
    - 初次请求 `cursor` 传 0。
    - 返回的数据仅包含「用户信息」，不包括视频、话题、音乐等内容。

    ### 参数:
    - keyword: 搜索关键词，如 \"人工智能\"
    - cursor: 翻页游标（首次请求传0）

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"人工智能\",
        \"cursor\": 0
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `cursor`: 下一页游标
    - `has_more`: 是否还有更多数据（1=有，0=无）
    - `user_list[]`: 用户列表
      - `user_info`:
        - `uid`: 用户ID
        - `nickname`: 用户昵称
        - `gender`: 性别（0=未知，1=男，2=女）
        - `unique_id`: 抖音号
        - `sec_uid`: 安全UID
        - `signature`: 个性签名
        - `follower_count`: 粉丝数量
        - `avatar_thumb.url_list`: 小头像地址
        - `avatar_medium.url_list`: 中头像地址
        - `avatar_larger.url_list`: 大头像地址
        - `follow_status`: 是否已关注
        - `live_status`: 是否正在直播（0=否，1=是）
        - `enterprise_verify_reason`: 企业认证信息（若有）
        - `versatile_display`: 抖音号展示文案（例如\"抖音号：xxx\"）
    - `extra`:
      - `now`: 当前服务器时间戳
      - `logid`: 请求日志ID
      - `search_request_id`: 搜索请求ID

    # [English]
    ### Purpose:
    - Fetch a list of users from Douyin App based on search keywords.
    - Supports filtering by fan count and user type.

    ### Notes:
    - Set `cursor` to 0.
    - Only user information is returned. No videos, music, or hashtags.

    ### Parameters:
    - keyword: Search keyword, e.g., \"AI\"
    - cursor: Pagination cursor (0 for first page)

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"AI\",
        \"cursor\": 0
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `cursor`: Cursor for next page
    - `has_more`: Whether more data is available (1=Yes, 0=No)
    - `user_list[]`: List of users
      - `user_info`:
        - `uid`: User ID
        - `nickname`: Nickname
        - `gender`: Gender (0=Unknown, 1=Male, 2=Female)
        - `unique_id`: Douyin ID
        - `sec_uid`: Secured UID
        - `signature`: Personal bio
        - `follower_count`: Number of followers
        - `avatar_thumb.url_list`: List of thumbnail avatar URLs
        - `avatar_medium.url_list`: List of medium avatar URLs
        - `avatar_larger.url_list`: List of large avatar URLs
        - `follow_status`: Whether followed
        - `live_status`: Whether live
        - `enterprise_verify_reason`: Enterprise verification info (if any)
        - `versatile_display`: Display text (e.g., \"Douyin ID: xxx\")
    - `extra`:
      - `now`: Current server timestamp
      - `logid`: Request log ID
      - `search_request_id`: Search request ID

    Args:
        body (UserSearchRequestV2):

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
    body: UserSearchRequestV2,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户搜索 V2/Fetch user search V2

     # [中文]
    ### 用途:
    - 获取抖音 App 中根据关键词搜索到的用户列表。
    - 不支持粉丝数量、用户类型筛选查询。

    ### 备注:
    - 初次请求 `cursor` 传 0。
    - 返回的数据仅包含「用户信息」，不包括视频、话题、音乐等内容。

    ### 参数:
    - keyword: 搜索关键词，如 \"人工智能\"
    - cursor: 翻页游标（首次请求传0）

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"人工智能\",
        \"cursor\": 0
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `cursor`: 下一页游标
    - `has_more`: 是否还有更多数据（1=有，0=无）
    - `user_list[]`: 用户列表
      - `user_info`:
        - `uid`: 用户ID
        - `nickname`: 用户昵称
        - `gender`: 性别（0=未知，1=男，2=女）
        - `unique_id`: 抖音号
        - `sec_uid`: 安全UID
        - `signature`: 个性签名
        - `follower_count`: 粉丝数量
        - `avatar_thumb.url_list`: 小头像地址
        - `avatar_medium.url_list`: 中头像地址
        - `avatar_larger.url_list`: 大头像地址
        - `follow_status`: 是否已关注
        - `live_status`: 是否正在直播（0=否，1=是）
        - `enterprise_verify_reason`: 企业认证信息（若有）
        - `versatile_display`: 抖音号展示文案（例如\"抖音号：xxx\"）
    - `extra`:
      - `now`: 当前服务器时间戳
      - `logid`: 请求日志ID
      - `search_request_id`: 搜索请求ID

    # [English]
    ### Purpose:
    - Fetch a list of users from Douyin App based on search keywords.
    - Supports filtering by fan count and user type.

    ### Notes:
    - Set `cursor` to 0.
    - Only user information is returned. No videos, music, or hashtags.

    ### Parameters:
    - keyword: Search keyword, e.g., \"AI\"
    - cursor: Pagination cursor (0 for first page)

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"AI\",
        \"cursor\": 0
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `cursor`: Cursor for next page
    - `has_more`: Whether more data is available (1=Yes, 0=No)
    - `user_list[]`: List of users
      - `user_info`:
        - `uid`: User ID
        - `nickname`: Nickname
        - `gender`: Gender (0=Unknown, 1=Male, 2=Female)
        - `unique_id`: Douyin ID
        - `sec_uid`: Secured UID
        - `signature`: Personal bio
        - `follower_count`: Number of followers
        - `avatar_thumb.url_list`: List of thumbnail avatar URLs
        - `avatar_medium.url_list`: List of medium avatar URLs
        - `avatar_larger.url_list`: List of large avatar URLs
        - `follow_status`: Whether followed
        - `live_status`: Whether live
        - `enterprise_verify_reason`: Enterprise verification info (if any)
        - `versatile_display`: Display text (e.g., \"Douyin ID: xxx\")
    - `extra`:
      - `now`: Current server timestamp
      - `logid`: Request log ID
      - `search_request_id`: Search request ID

    Args:
        body (UserSearchRequestV2):

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
    body: UserSearchRequestV2,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户搜索 V2/Fetch user search V2

     # [中文]
    ### 用途:
    - 获取抖音 App 中根据关键词搜索到的用户列表。
    - 不支持粉丝数量、用户类型筛选查询。

    ### 备注:
    - 初次请求 `cursor` 传 0。
    - 返回的数据仅包含「用户信息」，不包括视频、话题、音乐等内容。

    ### 参数:
    - keyword: 搜索关键词，如 \"人工智能\"
    - cursor: 翻页游标（首次请求传0）

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"人工智能\",
        \"cursor\": 0
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `cursor`: 下一页游标
    - `has_more`: 是否还有更多数据（1=有，0=无）
    - `user_list[]`: 用户列表
      - `user_info`:
        - `uid`: 用户ID
        - `nickname`: 用户昵称
        - `gender`: 性别（0=未知，1=男，2=女）
        - `unique_id`: 抖音号
        - `sec_uid`: 安全UID
        - `signature`: 个性签名
        - `follower_count`: 粉丝数量
        - `avatar_thumb.url_list`: 小头像地址
        - `avatar_medium.url_list`: 中头像地址
        - `avatar_larger.url_list`: 大头像地址
        - `follow_status`: 是否已关注
        - `live_status`: 是否正在直播（0=否，1=是）
        - `enterprise_verify_reason`: 企业认证信息（若有）
        - `versatile_display`: 抖音号展示文案（例如\"抖音号：xxx\"）
    - `extra`:
      - `now`: 当前服务器时间戳
      - `logid`: 请求日志ID
      - `search_request_id`: 搜索请求ID

    # [English]
    ### Purpose:
    - Fetch a list of users from Douyin App based on search keywords.
    - Supports filtering by fan count and user type.

    ### Notes:
    - Set `cursor` to 0.
    - Only user information is returned. No videos, music, or hashtags.

    ### Parameters:
    - keyword: Search keyword, e.g., \"AI\"
    - cursor: Pagination cursor (0 for first page)

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"AI\",
        \"cursor\": 0
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `cursor`: Cursor for next page
    - `has_more`: Whether more data is available (1=Yes, 0=No)
    - `user_list[]`: List of users
      - `user_info`:
        - `uid`: User ID
        - `nickname`: Nickname
        - `gender`: Gender (0=Unknown, 1=Male, 2=Female)
        - `unique_id`: Douyin ID
        - `sec_uid`: Secured UID
        - `signature`: Personal bio
        - `follower_count`: Number of followers
        - `avatar_thumb.url_list`: List of thumbnail avatar URLs
        - `avatar_medium.url_list`: List of medium avatar URLs
        - `avatar_larger.url_list`: List of large avatar URLs
        - `follow_status`: Whether followed
        - `live_status`: Whether live
        - `enterprise_verify_reason`: Enterprise verification info (if any)
        - `versatile_display`: Display text (e.g., \"Douyin ID: xxx\")
    - `extra`:
      - `now`: Current server timestamp
      - `logid`: Request log ID
      - `search_request_id`: Search request ID

    Args:
        body (UserSearchRequestV2):

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
    body: UserSearchRequestV2,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户搜索 V2/Fetch user search V2

     # [中文]
    ### 用途:
    - 获取抖音 App 中根据关键词搜索到的用户列表。
    - 不支持粉丝数量、用户类型筛选查询。

    ### 备注:
    - 初次请求 `cursor` 传 0。
    - 返回的数据仅包含「用户信息」，不包括视频、话题、音乐等内容。

    ### 参数:
    - keyword: 搜索关键词，如 \"人工智能\"
    - cursor: 翻页游标（首次请求传0）

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"人工智能\",
        \"cursor\": 0
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `cursor`: 下一页游标
    - `has_more`: 是否还有更多数据（1=有，0=无）
    - `user_list[]`: 用户列表
      - `user_info`:
        - `uid`: 用户ID
        - `nickname`: 用户昵称
        - `gender`: 性别（0=未知，1=男，2=女）
        - `unique_id`: 抖音号
        - `sec_uid`: 安全UID
        - `signature`: 个性签名
        - `follower_count`: 粉丝数量
        - `avatar_thumb.url_list`: 小头像地址
        - `avatar_medium.url_list`: 中头像地址
        - `avatar_larger.url_list`: 大头像地址
        - `follow_status`: 是否已关注
        - `live_status`: 是否正在直播（0=否，1=是）
        - `enterprise_verify_reason`: 企业认证信息（若有）
        - `versatile_display`: 抖音号展示文案（例如\"抖音号：xxx\"）
    - `extra`:
      - `now`: 当前服务器时间戳
      - `logid`: 请求日志ID
      - `search_request_id`: 搜索请求ID

    # [English]
    ### Purpose:
    - Fetch a list of users from Douyin App based on search keywords.
    - Supports filtering by fan count and user type.

    ### Notes:
    - Set `cursor` to 0.
    - Only user information is returned. No videos, music, or hashtags.

    ### Parameters:
    - keyword: Search keyword, e.g., \"AI\"
    - cursor: Pagination cursor (0 for first page)

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"AI\",
        \"cursor\": 0
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `cursor`: Cursor for next page
    - `has_more`: Whether more data is available (1=Yes, 0=No)
    - `user_list[]`: List of users
      - `user_info`:
        - `uid`: User ID
        - `nickname`: Nickname
        - `gender`: Gender (0=Unknown, 1=Male, 2=Female)
        - `unique_id`: Douyin ID
        - `sec_uid`: Secured UID
        - `signature`: Personal bio
        - `follower_count`: Number of followers
        - `avatar_thumb.url_list`: List of thumbnail avatar URLs
        - `avatar_medium.url_list`: List of medium avatar URLs
        - `avatar_larger.url_list`: List of large avatar URLs
        - `follow_status`: Whether followed
        - `live_status`: Whether live
        - `enterprise_verify_reason`: Enterprise verification info (if any)
        - `versatile_display`: Display text (e.g., \"Douyin ID: xxx\")
    - `extra`:
      - `now`: Current server timestamp
      - `logid`: Request log ID
      - `search_request_id`: Search request ID

    Args:
        body (UserSearchRequestV2):

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
