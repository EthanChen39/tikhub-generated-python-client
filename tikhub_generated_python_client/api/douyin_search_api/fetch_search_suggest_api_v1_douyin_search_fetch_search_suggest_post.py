from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...models.search_suggest_request import SearchSuggestRequest
from ...types import Response


def _get_kwargs(
    *,
    body: SearchSuggestRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/search/fetch_search_suggest",
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
    body: SearchSuggestRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取搜索关键词推荐/Fetch search keyword suggestions

     # [中文]
    ### 用途:
    - 获取抖音 App 中搜索关键词的联想推荐结果。
    - 根据用户输入的关键词，返回相关搜索词建议，用于提升搜索体验。

    ### 备注:
    - 通常用于实现搜索框实时推荐（如输入时下拉补全）。
    - 返回的推荐词经过抖音推荐系统内部打分排序。

    ### 参数:
    - keyword: 输入的关键词，如 \"人工智能\"

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"人工智能\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `status_code`: 状态码（0 表示成功）
    - `status_msg`: 返回信息（一般为空）
    - `rid`: 请求ID
    - `sug_list[]`: 搜索建议列表
      - `content`: 推荐的搜索关键词（如 \"人工智能ai软件免费版下载\"）
      - `sug_type`: 建议类型（一般为空，预留字段）
      - `pos[]`: 匹配位置（标记关键词在原搜索词中的起止位置）
        - `begin`: 开始字符位置
        - `end`: 结束字符位置
      - `word_record`:
        - `group_id`: 推荐词组ID
        - `words_position`: 在本次推荐列表中的位置
        - `words_content`: 词内容（同 `content`）
        - `words_source`: 词来源（通常为 \"sug\"）
      - `extra_info`:
        - `client_server_extra`: 附加配置信息（JSON字符串）
        - `poi_id`: 关联POI ID（通常为空）
        - `search_params`: 搜索参数（带内部推荐得分）
    - `words_query_record`:
      - `info`: 附加信息（通常为空）
      - `words_source`: 推荐来源
      - `query_id`: 推荐查询ID
    - `extra`:
      - `now`: 当前服务器时间戳（毫秒）
      - `logid`: 日志ID
      - `fatal_item_ids`: 错误项列表（通常为空）
      - `search_request_id`: 搜索请求ID（通常为空）
    - `log_pb`:
      - `impr_id`: 曝光日志ID
    - `time_cost`:
      - `stream_inner`: 内部处理耗时（毫秒）
      - `server_engine_cost`: 搜索引擎处理耗时（毫秒）
    - `cache_conf`:
      - `enable`: 是否命中缓存（布尔值）

    # [English]
    ### Purpose:
    - Fetch keyword suggestion results from Douyin App.
    - Based on the user's input, returns a list of recommended search keywords to improve search
    experience.

    ### Notes:
    - Typically used for real-time keyword suggestions in the search box.
    - The returned suggestions are scored and sorted internally by Douyin's recommendation system.

    ### Parameters:
    - keyword: Input keyword, e.g., \"Artificial Intelligence\"

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"Artificial Intelligence\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `status_code`: Status code (0 means success)
    - `status_msg`: Response message (usually empty)
    - `rid`: Request ID
    - `sug_list[]`: List of suggested search keywords
      - `content`: Suggested keyword (e.g., \"AI software free download\")
      - `sug_type`: Suggestion type (usually empty, reserved field)
      - `pos[]`: Position marking
        - `begin`: Begin character position
        - `end`: End character position
      - `word_record`:
        - `group_id`: Suggestion group ID
        - `words_position`: Position in the current suggestion list
        - `words_content`: The word content (same as `content`)
        - `words_source`: Word source (typically \"sug\")
      - `extra_info`:
        - `client_server_extra`: Extra client-server config (JSON string)
        - `poi_id`: Related POI ID (usually empty)
        - `search_params`: Search parameters (with recommendation scores)
    - `words_query_record`:
      - `info`: Additional info (usually empty)
      - `words_source`: Source of suggestions
      - `query_id`: Suggestion query ID
    - `extra`:
      - `now`: Current server timestamp (milliseconds)
      - `logid`: Log ID
      - `fatal_item_ids`: List of fatal error items (usually empty)
      - `search_request_id`: Search request ID (usually empty)
    - `log_pb`:
      - `impr_id`: Impression log ID
    - `time_cost`:
      - `stream_inner`: Internal stream processing time (milliseconds)
      - `server_engine_cost`: Server search engine processing time (milliseconds)
    - `cache_conf`:
      - `enable`: Whether cache was hit (boolean)

    Args:
        body (SearchSuggestRequest):

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
    body: SearchSuggestRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取搜索关键词推荐/Fetch search keyword suggestions

     # [中文]
    ### 用途:
    - 获取抖音 App 中搜索关键词的联想推荐结果。
    - 根据用户输入的关键词，返回相关搜索词建议，用于提升搜索体验。

    ### 备注:
    - 通常用于实现搜索框实时推荐（如输入时下拉补全）。
    - 返回的推荐词经过抖音推荐系统内部打分排序。

    ### 参数:
    - keyword: 输入的关键词，如 \"人工智能\"

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"人工智能\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `status_code`: 状态码（0 表示成功）
    - `status_msg`: 返回信息（一般为空）
    - `rid`: 请求ID
    - `sug_list[]`: 搜索建议列表
      - `content`: 推荐的搜索关键词（如 \"人工智能ai软件免费版下载\"）
      - `sug_type`: 建议类型（一般为空，预留字段）
      - `pos[]`: 匹配位置（标记关键词在原搜索词中的起止位置）
        - `begin`: 开始字符位置
        - `end`: 结束字符位置
      - `word_record`:
        - `group_id`: 推荐词组ID
        - `words_position`: 在本次推荐列表中的位置
        - `words_content`: 词内容（同 `content`）
        - `words_source`: 词来源（通常为 \"sug\"）
      - `extra_info`:
        - `client_server_extra`: 附加配置信息（JSON字符串）
        - `poi_id`: 关联POI ID（通常为空）
        - `search_params`: 搜索参数（带内部推荐得分）
    - `words_query_record`:
      - `info`: 附加信息（通常为空）
      - `words_source`: 推荐来源
      - `query_id`: 推荐查询ID
    - `extra`:
      - `now`: 当前服务器时间戳（毫秒）
      - `logid`: 日志ID
      - `fatal_item_ids`: 错误项列表（通常为空）
      - `search_request_id`: 搜索请求ID（通常为空）
    - `log_pb`:
      - `impr_id`: 曝光日志ID
    - `time_cost`:
      - `stream_inner`: 内部处理耗时（毫秒）
      - `server_engine_cost`: 搜索引擎处理耗时（毫秒）
    - `cache_conf`:
      - `enable`: 是否命中缓存（布尔值）

    # [English]
    ### Purpose:
    - Fetch keyword suggestion results from Douyin App.
    - Based on the user's input, returns a list of recommended search keywords to improve search
    experience.

    ### Notes:
    - Typically used for real-time keyword suggestions in the search box.
    - The returned suggestions are scored and sorted internally by Douyin's recommendation system.

    ### Parameters:
    - keyword: Input keyword, e.g., \"Artificial Intelligence\"

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"Artificial Intelligence\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `status_code`: Status code (0 means success)
    - `status_msg`: Response message (usually empty)
    - `rid`: Request ID
    - `sug_list[]`: List of suggested search keywords
      - `content`: Suggested keyword (e.g., \"AI software free download\")
      - `sug_type`: Suggestion type (usually empty, reserved field)
      - `pos[]`: Position marking
        - `begin`: Begin character position
        - `end`: End character position
      - `word_record`:
        - `group_id`: Suggestion group ID
        - `words_position`: Position in the current suggestion list
        - `words_content`: The word content (same as `content`)
        - `words_source`: Word source (typically \"sug\")
      - `extra_info`:
        - `client_server_extra`: Extra client-server config (JSON string)
        - `poi_id`: Related POI ID (usually empty)
        - `search_params`: Search parameters (with recommendation scores)
    - `words_query_record`:
      - `info`: Additional info (usually empty)
      - `words_source`: Source of suggestions
      - `query_id`: Suggestion query ID
    - `extra`:
      - `now`: Current server timestamp (milliseconds)
      - `logid`: Log ID
      - `fatal_item_ids`: List of fatal error items (usually empty)
      - `search_request_id`: Search request ID (usually empty)
    - `log_pb`:
      - `impr_id`: Impression log ID
    - `time_cost`:
      - `stream_inner`: Internal stream processing time (milliseconds)
      - `server_engine_cost`: Server search engine processing time (milliseconds)
    - `cache_conf`:
      - `enable`: Whether cache was hit (boolean)

    Args:
        body (SearchSuggestRequest):

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
    body: SearchSuggestRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取搜索关键词推荐/Fetch search keyword suggestions

     # [中文]
    ### 用途:
    - 获取抖音 App 中搜索关键词的联想推荐结果。
    - 根据用户输入的关键词，返回相关搜索词建议，用于提升搜索体验。

    ### 备注:
    - 通常用于实现搜索框实时推荐（如输入时下拉补全）。
    - 返回的推荐词经过抖音推荐系统内部打分排序。

    ### 参数:
    - keyword: 输入的关键词，如 \"人工智能\"

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"人工智能\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `status_code`: 状态码（0 表示成功）
    - `status_msg`: 返回信息（一般为空）
    - `rid`: 请求ID
    - `sug_list[]`: 搜索建议列表
      - `content`: 推荐的搜索关键词（如 \"人工智能ai软件免费版下载\"）
      - `sug_type`: 建议类型（一般为空，预留字段）
      - `pos[]`: 匹配位置（标记关键词在原搜索词中的起止位置）
        - `begin`: 开始字符位置
        - `end`: 结束字符位置
      - `word_record`:
        - `group_id`: 推荐词组ID
        - `words_position`: 在本次推荐列表中的位置
        - `words_content`: 词内容（同 `content`）
        - `words_source`: 词来源（通常为 \"sug\"）
      - `extra_info`:
        - `client_server_extra`: 附加配置信息（JSON字符串）
        - `poi_id`: 关联POI ID（通常为空）
        - `search_params`: 搜索参数（带内部推荐得分）
    - `words_query_record`:
      - `info`: 附加信息（通常为空）
      - `words_source`: 推荐来源
      - `query_id`: 推荐查询ID
    - `extra`:
      - `now`: 当前服务器时间戳（毫秒）
      - `logid`: 日志ID
      - `fatal_item_ids`: 错误项列表（通常为空）
      - `search_request_id`: 搜索请求ID（通常为空）
    - `log_pb`:
      - `impr_id`: 曝光日志ID
    - `time_cost`:
      - `stream_inner`: 内部处理耗时（毫秒）
      - `server_engine_cost`: 搜索引擎处理耗时（毫秒）
    - `cache_conf`:
      - `enable`: 是否命中缓存（布尔值）

    # [English]
    ### Purpose:
    - Fetch keyword suggestion results from Douyin App.
    - Based on the user's input, returns a list of recommended search keywords to improve search
    experience.

    ### Notes:
    - Typically used for real-time keyword suggestions in the search box.
    - The returned suggestions are scored and sorted internally by Douyin's recommendation system.

    ### Parameters:
    - keyword: Input keyword, e.g., \"Artificial Intelligence\"

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"Artificial Intelligence\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `status_code`: Status code (0 means success)
    - `status_msg`: Response message (usually empty)
    - `rid`: Request ID
    - `sug_list[]`: List of suggested search keywords
      - `content`: Suggested keyword (e.g., \"AI software free download\")
      - `sug_type`: Suggestion type (usually empty, reserved field)
      - `pos[]`: Position marking
        - `begin`: Begin character position
        - `end`: End character position
      - `word_record`:
        - `group_id`: Suggestion group ID
        - `words_position`: Position in the current suggestion list
        - `words_content`: The word content (same as `content`)
        - `words_source`: Word source (typically \"sug\")
      - `extra_info`:
        - `client_server_extra`: Extra client-server config (JSON string)
        - `poi_id`: Related POI ID (usually empty)
        - `search_params`: Search parameters (with recommendation scores)
    - `words_query_record`:
      - `info`: Additional info (usually empty)
      - `words_source`: Source of suggestions
      - `query_id`: Suggestion query ID
    - `extra`:
      - `now`: Current server timestamp (milliseconds)
      - `logid`: Log ID
      - `fatal_item_ids`: List of fatal error items (usually empty)
      - `search_request_id`: Search request ID (usually empty)
    - `log_pb`:
      - `impr_id`: Impression log ID
    - `time_cost`:
      - `stream_inner`: Internal stream processing time (milliseconds)
      - `server_engine_cost`: Server search engine processing time (milliseconds)
    - `cache_conf`:
      - `enable`: Whether cache was hit (boolean)

    Args:
        body (SearchSuggestRequest):

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
    body: SearchSuggestRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取搜索关键词推荐/Fetch search keyword suggestions

     # [中文]
    ### 用途:
    - 获取抖音 App 中搜索关键词的联想推荐结果。
    - 根据用户输入的关键词，返回相关搜索词建议，用于提升搜索体验。

    ### 备注:
    - 通常用于实现搜索框实时推荐（如输入时下拉补全）。
    - 返回的推荐词经过抖音推荐系统内部打分排序。

    ### 参数:
    - keyword: 输入的关键词，如 \"人工智能\"

    ### 请求体示例：
    ```json
    payload = {
        \"keyword\": \"人工智能\"
    }
    ```

    ### 返回（部分常用字段，实际返回字段更多，一切以实际响应为准）:
    - `status_code`: 状态码（0 表示成功）
    - `status_msg`: 返回信息（一般为空）
    - `rid`: 请求ID
    - `sug_list[]`: 搜索建议列表
      - `content`: 推荐的搜索关键词（如 \"人工智能ai软件免费版下载\"）
      - `sug_type`: 建议类型（一般为空，预留字段）
      - `pos[]`: 匹配位置（标记关键词在原搜索词中的起止位置）
        - `begin`: 开始字符位置
        - `end`: 结束字符位置
      - `word_record`:
        - `group_id`: 推荐词组ID
        - `words_position`: 在本次推荐列表中的位置
        - `words_content`: 词内容（同 `content`）
        - `words_source`: 词来源（通常为 \"sug\"）
      - `extra_info`:
        - `client_server_extra`: 附加配置信息（JSON字符串）
        - `poi_id`: 关联POI ID（通常为空）
        - `search_params`: 搜索参数（带内部推荐得分）
    - `words_query_record`:
      - `info`: 附加信息（通常为空）
      - `words_source`: 推荐来源
      - `query_id`: 推荐查询ID
    - `extra`:
      - `now`: 当前服务器时间戳（毫秒）
      - `logid`: 日志ID
      - `fatal_item_ids`: 错误项列表（通常为空）
      - `search_request_id`: 搜索请求ID（通常为空）
    - `log_pb`:
      - `impr_id`: 曝光日志ID
    - `time_cost`:
      - `stream_inner`: 内部处理耗时（毫秒）
      - `server_engine_cost`: 搜索引擎处理耗时（毫秒）
    - `cache_conf`:
      - `enable`: 是否命中缓存（布尔值）

    # [English]
    ### Purpose:
    - Fetch keyword suggestion results from Douyin App.
    - Based on the user's input, returns a list of recommended search keywords to improve search
    experience.

    ### Notes:
    - Typically used for real-time keyword suggestions in the search box.
    - The returned suggestions are scored and sorted internally by Douyin's recommendation system.

    ### Parameters:
    - keyword: Input keyword, e.g., \"Artificial Intelligence\"

    ### Request Body Example:
    ```json
    payload = {
        \"keyword\": \"Artificial Intelligence\"
    }
    ```

    ### Response (common fields, actual response may contain more fields):
    - `status_code`: Status code (0 means success)
    - `status_msg`: Response message (usually empty)
    - `rid`: Request ID
    - `sug_list[]`: List of suggested search keywords
      - `content`: Suggested keyword (e.g., \"AI software free download\")
      - `sug_type`: Suggestion type (usually empty, reserved field)
      - `pos[]`: Position marking
        - `begin`: Begin character position
        - `end`: End character position
      - `word_record`:
        - `group_id`: Suggestion group ID
        - `words_position`: Position in the current suggestion list
        - `words_content`: The word content (same as `content`)
        - `words_source`: Word source (typically \"sug\")
      - `extra_info`:
        - `client_server_extra`: Extra client-server config (JSON string)
        - `poi_id`: Related POI ID (usually empty)
        - `search_params`: Search parameters (with recommendation scores)
    - `words_query_record`:
      - `info`: Additional info (usually empty)
      - `words_source`: Source of suggestions
      - `query_id`: Suggestion query ID
    - `extra`:
      - `now`: Current server timestamp (milliseconds)
      - `logid`: Log ID
      - `fatal_item_ids`: List of fatal error items (usually empty)
      - `search_request_id`: Search request ID (usually empty)
    - `log_pb`:
      - `impr_id`: Impression log ID
    - `time_cost`:
      - `stream_inner`: Internal stream processing time (milliseconds)
      - `server_engine_cost`: Server search engine processing time (milliseconds)
    - `cache_conf`:
      - `enable`: Whether cache was hit (boolean)

    Args:
        body (SearchSuggestRequest):

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
