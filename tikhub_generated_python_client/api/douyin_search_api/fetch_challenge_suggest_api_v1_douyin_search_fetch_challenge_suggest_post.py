from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.challenge_suggest_request import ChallengeSuggestRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: ChallengeSuggestRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/search/fetch_challenge_suggest",
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
    body: ChallengeSuggestRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取话题推荐搜索/Fetch hashtag suggestions

     # [中文]
    ### 用途:
    - 获取抖音 App 中话题(挑战/标签)的推荐搜索结果。
    - 根据输入的关键词，返回相关的话题建议列表，包含话题名称、浏览量等信息。

    ### 备注:
    - 本接口可用于话题联想推荐场景，如输入关键词实时展示相关热门话题。
    - 初次请求时 `cursor` 传入 0，`search_id` 传空字符串。

    ### 参数:
    - keyword: 搜索关键词，如 \"游戏\"

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"游戏\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `sug_list[]`: 推荐话题列表
      - `cha_name`: 话题名称（如 \"#游戏\"）
      - `view_count`: 话题总浏览量
      - `cid`: 话题ID
      - `group_id`: 话题关联的群组ID（可以用于跳转）
      - `tag`: 话题标签分类（0=普通话题，1=流量风向标）
    - `status_code`: 状态码（0=成功）
    - `status_msg`: 状态信息（通常为空）
    - `rid`: 请求ID
    - `words_query_record`:
      - `info`: 额外信息（目前为空）
      - `words_source`: 关键词来源（固定\"sug\"）
      - `query_id`: 查询ID（通常为空）
    - `extra`:
      - `now`: 当前服务器时间戳
      - `logid`: 日志ID
      - `fatal_item_ids`: 错误项目ID列表（通常为空）
      - `search_request_id`: 搜索请求ID（通常为空）
    - `log_pb`:
      - `impr_id`: 曝光ID（日志追踪用）

    # [English]
    ### Purpose:
    - Fetch hashtag/challenge suggestions from Douyin App based on the input keyword.
    - Returns a list of related hashtags including name and view count.

    ### Notes:
    - Suitable for implementing keyword suggestion features in search bars.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.

    ### Parameters:
    - keyword: Search keyword, e.g., \"game\"

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"game\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `sug_list[]`: List of suggested hashtags
      - `cha_name`: Hashtag name (e.g., \"#game\")
      - `view_count`: Total view count
      - `cid`: Challenge ID
      - `group_id`: Associated group ID
      - `tag`: Tag category (0=normal, 1=hot trend)
    - `status_code`: Status code (0=success)
    - `status_msg`: Status message (usually empty)
    - `rid`: Request ID
    - `words_query_record`:
      - `info`: Additional info (currently empty)
      - `words_source`: Words source (\"sug\")
      - `query_id`: Query ID (usually empty)
    - `extra`:
      - `now`: Server timestamp
      - `logid`: Log ID
      - `fatal_item_ids`: List of fatal item IDs (usually empty)
      - `search_request_id`: Search request ID (usually empty)
    - `log_pb`:
      - `impr_id`: Impression ID (for logging)

    Args:
        body (ChallengeSuggestRequest):

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
    body: ChallengeSuggestRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取话题推荐搜索/Fetch hashtag suggestions

     # [中文]
    ### 用途:
    - 获取抖音 App 中话题(挑战/标签)的推荐搜索结果。
    - 根据输入的关键词，返回相关的话题建议列表，包含话题名称、浏览量等信息。

    ### 备注:
    - 本接口可用于话题联想推荐场景，如输入关键词实时展示相关热门话题。
    - 初次请求时 `cursor` 传入 0，`search_id` 传空字符串。

    ### 参数:
    - keyword: 搜索关键词，如 \"游戏\"

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"游戏\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `sug_list[]`: 推荐话题列表
      - `cha_name`: 话题名称（如 \"#游戏\"）
      - `view_count`: 话题总浏览量
      - `cid`: 话题ID
      - `group_id`: 话题关联的群组ID（可以用于跳转）
      - `tag`: 话题标签分类（0=普通话题，1=流量风向标）
    - `status_code`: 状态码（0=成功）
    - `status_msg`: 状态信息（通常为空）
    - `rid`: 请求ID
    - `words_query_record`:
      - `info`: 额外信息（目前为空）
      - `words_source`: 关键词来源（固定\"sug\"）
      - `query_id`: 查询ID（通常为空）
    - `extra`:
      - `now`: 当前服务器时间戳
      - `logid`: 日志ID
      - `fatal_item_ids`: 错误项目ID列表（通常为空）
      - `search_request_id`: 搜索请求ID（通常为空）
    - `log_pb`:
      - `impr_id`: 曝光ID（日志追踪用）

    # [English]
    ### Purpose:
    - Fetch hashtag/challenge suggestions from Douyin App based on the input keyword.
    - Returns a list of related hashtags including name and view count.

    ### Notes:
    - Suitable for implementing keyword suggestion features in search bars.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.

    ### Parameters:
    - keyword: Search keyword, e.g., \"game\"

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"game\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `sug_list[]`: List of suggested hashtags
      - `cha_name`: Hashtag name (e.g., \"#game\")
      - `view_count`: Total view count
      - `cid`: Challenge ID
      - `group_id`: Associated group ID
      - `tag`: Tag category (0=normal, 1=hot trend)
    - `status_code`: Status code (0=success)
    - `status_msg`: Status message (usually empty)
    - `rid`: Request ID
    - `words_query_record`:
      - `info`: Additional info (currently empty)
      - `words_source`: Words source (\"sug\")
      - `query_id`: Query ID (usually empty)
    - `extra`:
      - `now`: Server timestamp
      - `logid`: Log ID
      - `fatal_item_ids`: List of fatal item IDs (usually empty)
      - `search_request_id`: Search request ID (usually empty)
    - `log_pb`:
      - `impr_id`: Impression ID (for logging)

    Args:
        body (ChallengeSuggestRequest):

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
    body: ChallengeSuggestRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取话题推荐搜索/Fetch hashtag suggestions

     # [中文]
    ### 用途:
    - 获取抖音 App 中话题(挑战/标签)的推荐搜索结果。
    - 根据输入的关键词，返回相关的话题建议列表，包含话题名称、浏览量等信息。

    ### 备注:
    - 本接口可用于话题联想推荐场景，如输入关键词实时展示相关热门话题。
    - 初次请求时 `cursor` 传入 0，`search_id` 传空字符串。

    ### 参数:
    - keyword: 搜索关键词，如 \"游戏\"

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"游戏\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `sug_list[]`: 推荐话题列表
      - `cha_name`: 话题名称（如 \"#游戏\"）
      - `view_count`: 话题总浏览量
      - `cid`: 话题ID
      - `group_id`: 话题关联的群组ID（可以用于跳转）
      - `tag`: 话题标签分类（0=普通话题，1=流量风向标）
    - `status_code`: 状态码（0=成功）
    - `status_msg`: 状态信息（通常为空）
    - `rid`: 请求ID
    - `words_query_record`:
      - `info`: 额外信息（目前为空）
      - `words_source`: 关键词来源（固定\"sug\"）
      - `query_id`: 查询ID（通常为空）
    - `extra`:
      - `now`: 当前服务器时间戳
      - `logid`: 日志ID
      - `fatal_item_ids`: 错误项目ID列表（通常为空）
      - `search_request_id`: 搜索请求ID（通常为空）
    - `log_pb`:
      - `impr_id`: 曝光ID（日志追踪用）

    # [English]
    ### Purpose:
    - Fetch hashtag/challenge suggestions from Douyin App based on the input keyword.
    - Returns a list of related hashtags including name and view count.

    ### Notes:
    - Suitable for implementing keyword suggestion features in search bars.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.

    ### Parameters:
    - keyword: Search keyword, e.g., \"game\"

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"game\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `sug_list[]`: List of suggested hashtags
      - `cha_name`: Hashtag name (e.g., \"#game\")
      - `view_count`: Total view count
      - `cid`: Challenge ID
      - `group_id`: Associated group ID
      - `tag`: Tag category (0=normal, 1=hot trend)
    - `status_code`: Status code (0=success)
    - `status_msg`: Status message (usually empty)
    - `rid`: Request ID
    - `words_query_record`:
      - `info`: Additional info (currently empty)
      - `words_source`: Words source (\"sug\")
      - `query_id`: Query ID (usually empty)
    - `extra`:
      - `now`: Server timestamp
      - `logid`: Log ID
      - `fatal_item_ids`: List of fatal item IDs (usually empty)
      - `search_request_id`: Search request ID (usually empty)
    - `log_pb`:
      - `impr_id`: Impression ID (for logging)

    Args:
        body (ChallengeSuggestRequest):

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
    body: ChallengeSuggestRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取话题推荐搜索/Fetch hashtag suggestions

     # [中文]
    ### 用途:
    - 获取抖音 App 中话题(挑战/标签)的推荐搜索结果。
    - 根据输入的关键词，返回相关的话题建议列表，包含话题名称、浏览量等信息。

    ### 备注:
    - 本接口可用于话题联想推荐场景，如输入关键词实时展示相关热门话题。
    - 初次请求时 `cursor` 传入 0，`search_id` 传空字符串。

    ### 参数:
    - keyword: 搜索关键词，如 \"游戏\"

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"游戏\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `sug_list[]`: 推荐话题列表
      - `cha_name`: 话题名称（如 \"#游戏\"）
      - `view_count`: 话题总浏览量
      - `cid`: 话题ID
      - `group_id`: 话题关联的群组ID（可以用于跳转）
      - `tag`: 话题标签分类（0=普通话题，1=流量风向标）
    - `status_code`: 状态码（0=成功）
    - `status_msg`: 状态信息（通常为空）
    - `rid`: 请求ID
    - `words_query_record`:
      - `info`: 额外信息（目前为空）
      - `words_source`: 关键词来源（固定\"sug\"）
      - `query_id`: 查询ID（通常为空）
    - `extra`:
      - `now`: 当前服务器时间戳
      - `logid`: 日志ID
      - `fatal_item_ids`: 错误项目ID列表（通常为空）
      - `search_request_id`: 搜索请求ID（通常为空）
    - `log_pb`:
      - `impr_id`: 曝光ID（日志追踪用）

    # [English]
    ### Purpose:
    - Fetch hashtag/challenge suggestions from Douyin App based on the input keyword.
    - Returns a list of related hashtags including name and view count.

    ### Notes:
    - Suitable for implementing keyword suggestion features in search bars.
    - Set `cursor` to 0 and `search_id` to an empty string for the first request.

    ### Parameters:
    - keyword: Search keyword, e.g., \"game\"

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"game\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `sug_list[]`: List of suggested hashtags
      - `cha_name`: Hashtag name (e.g., \"#game\")
      - `view_count`: Total view count
      - `cid`: Challenge ID
      - `group_id`: Associated group ID
      - `tag`: Tag category (0=normal, 1=hot trend)
    - `status_code`: Status code (0=success)
    - `status_msg`: Status message (usually empty)
    - `rid`: Request ID
    - `words_query_record`:
      - `info`: Additional info (currently empty)
      - `words_source`: Words source (\"sug\")
      - `query_id`: Query ID (usually empty)
    - `extra`:
      - `now`: Server timestamp
      - `logid`: Log ID
      - `fatal_item_ids`: List of fatal item IDs (usually empty)
      - `search_request_id`: Search request ID (usually empty)
    - `log_pb`:
      - `impr_id`: Impression ID (for logging)

    Args:
        body (ChallengeSuggestRequest):

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
