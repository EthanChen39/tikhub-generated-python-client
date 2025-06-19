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
    query: str,
    max_cursor: Union[Unset, str] = "",
    filter_type: Union[Unset, str] = "",
    order_by: Union[Unset, str] = "",
    search_tab: Union[Unset, str] = "main",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["query"] = query

    params["max_cursor"] = max_cursor

    params["filter_type"] = filter_type

    params["order_by"] = order_by

    params["search_tab"] = search_tab

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/lemon8/app/fetch_search",
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
    query: str,
    max_cursor: Union[Unset, str] = "",
    filter_type: Union[Unset, str] = "",
    order_by: Union[Unset, str] = "",
    search_tab: Union[Unset, str] = "main",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索接口/Search API

     # [中文]
    ### 用途:
    - 搜索接口
    ### 参数:
    - query: 搜索关键词
    - max_cursor:
    翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的`max_cursor`进行翻页，可以通过返回结果的`has_more`字段判断是否还有更多数据。
    - filter_type: 搜索过滤类型，默认为空字符串，可选值如下：
        - 空字符串：All（全部，默认使用此参数搜索）
        - video：只搜索视频作品
        - posts：只搜索文章作品
    - order_by: 搜索排序方式，默认为空字符串，可选值如下：
        - 空字符串：Relevance（相关度，默认使用此参数排序）
        - popular：流行度排序
        - recent：从新到旧排序
    - search_tab: 搜索类型，默认为`main`，可选值如下：
        - main：APP中显示为 `Top`（综合搜索，默认使用此参数搜索）
        - user：APP中显示为 `Accounts` （搜索用户账号）
        - hashtag：APP中显示为 `Hashtags`（搜索话题）
        - article：APP中显示为 `Posts`（搜索文章）
    ### 返回:
    - 搜索结果

    # [English]
    ### Purpose:
    - Search API
    ### Parameters:
    - query: Search keyword
    - max_cursor: Pagination parameter, can be obtained from the return result of the last request. It
    is empty for the first request, and the `max_cursor` returned by the last request is used for
    subsequent requests. You can judge whether there is more data by the `has_more` field in the return
    result.
    - filter_type: Search filter type, default is an empty string, optional values are as follows:
        - Empty string: All (default using this parameter to search)
        - video: Search only video
        - posts: Search only posts
    - order_by: Search sort type, default is an empty string, optional values are as follows:
        - Empty string: Relevance (default using this parameter to sort)
        - popular: Sort by popularity
        - recent: Sort from new to old
    - search_tab: Search type, default is `main`, optional values are as follows:
        - main: Display as `Top` in the APP (comprehensive search, default using this parameter to
    search)
        - user: Display as `Accounts` in the APP (search user accounts)
        - hashtag: Display as `Hashtags` in the APP (search hashtags)
        - article: Display as `Posts` in the APP (search articles)
    ### Return:
    - Search results

    # [示例/Example]
    query = \"lemon8\"
    max_cursor = \"\"
    filter_type = \"\"
    order_by = \"\"
    search_tab = \"main\"

    Args:
        query (str): 搜索关键词/Search keyword
        max_cursor (Union[Unset, str]): 翻页参数/Pagination parameter Default: ''.
        filter_type (Union[Unset, str]): 搜索过滤类型/Search filter type Default: ''.
        order_by (Union[Unset, str]): 搜索排序方式/Search sort type Default: ''.
        search_tab (Union[Unset, str]): 搜索类型/Search type Default: 'main'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        query=query,
        max_cursor=max_cursor,
        filter_type=filter_type,
        order_by=order_by,
        search_tab=search_tab,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    query: str,
    max_cursor: Union[Unset, str] = "",
    filter_type: Union[Unset, str] = "",
    order_by: Union[Unset, str] = "",
    search_tab: Union[Unset, str] = "main",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索接口/Search API

     # [中文]
    ### 用途:
    - 搜索接口
    ### 参数:
    - query: 搜索关键词
    - max_cursor:
    翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的`max_cursor`进行翻页，可以通过返回结果的`has_more`字段判断是否还有更多数据。
    - filter_type: 搜索过滤类型，默认为空字符串，可选值如下：
        - 空字符串：All（全部，默认使用此参数搜索）
        - video：只搜索视频作品
        - posts：只搜索文章作品
    - order_by: 搜索排序方式，默认为空字符串，可选值如下：
        - 空字符串：Relevance（相关度，默认使用此参数排序）
        - popular：流行度排序
        - recent：从新到旧排序
    - search_tab: 搜索类型，默认为`main`，可选值如下：
        - main：APP中显示为 `Top`（综合搜索，默认使用此参数搜索）
        - user：APP中显示为 `Accounts` （搜索用户账号）
        - hashtag：APP中显示为 `Hashtags`（搜索话题）
        - article：APP中显示为 `Posts`（搜索文章）
    ### 返回:
    - 搜索结果

    # [English]
    ### Purpose:
    - Search API
    ### Parameters:
    - query: Search keyword
    - max_cursor: Pagination parameter, can be obtained from the return result of the last request. It
    is empty for the first request, and the `max_cursor` returned by the last request is used for
    subsequent requests. You can judge whether there is more data by the `has_more` field in the return
    result.
    - filter_type: Search filter type, default is an empty string, optional values are as follows:
        - Empty string: All (default using this parameter to search)
        - video: Search only video
        - posts: Search only posts
    - order_by: Search sort type, default is an empty string, optional values are as follows:
        - Empty string: Relevance (default using this parameter to sort)
        - popular: Sort by popularity
        - recent: Sort from new to old
    - search_tab: Search type, default is `main`, optional values are as follows:
        - main: Display as `Top` in the APP (comprehensive search, default using this parameter to
    search)
        - user: Display as `Accounts` in the APP (search user accounts)
        - hashtag: Display as `Hashtags` in the APP (search hashtags)
        - article: Display as `Posts` in the APP (search articles)
    ### Return:
    - Search results

    # [示例/Example]
    query = \"lemon8\"
    max_cursor = \"\"
    filter_type = \"\"
    order_by = \"\"
    search_tab = \"main\"

    Args:
        query (str): 搜索关键词/Search keyword
        max_cursor (Union[Unset, str]): 翻页参数/Pagination parameter Default: ''.
        filter_type (Union[Unset, str]): 搜索过滤类型/Search filter type Default: ''.
        order_by (Union[Unset, str]): 搜索排序方式/Search sort type Default: ''.
        search_tab (Union[Unset, str]): 搜索类型/Search type Default: 'main'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        query=query,
        max_cursor=max_cursor,
        filter_type=filter_type,
        order_by=order_by,
        search_tab=search_tab,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    query: str,
    max_cursor: Union[Unset, str] = "",
    filter_type: Union[Unset, str] = "",
    order_by: Union[Unset, str] = "",
    search_tab: Union[Unset, str] = "main",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索接口/Search API

     # [中文]
    ### 用途:
    - 搜索接口
    ### 参数:
    - query: 搜索关键词
    - max_cursor:
    翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的`max_cursor`进行翻页，可以通过返回结果的`has_more`字段判断是否还有更多数据。
    - filter_type: 搜索过滤类型，默认为空字符串，可选值如下：
        - 空字符串：All（全部，默认使用此参数搜索）
        - video：只搜索视频作品
        - posts：只搜索文章作品
    - order_by: 搜索排序方式，默认为空字符串，可选值如下：
        - 空字符串：Relevance（相关度，默认使用此参数排序）
        - popular：流行度排序
        - recent：从新到旧排序
    - search_tab: 搜索类型，默认为`main`，可选值如下：
        - main：APP中显示为 `Top`（综合搜索，默认使用此参数搜索）
        - user：APP中显示为 `Accounts` （搜索用户账号）
        - hashtag：APP中显示为 `Hashtags`（搜索话题）
        - article：APP中显示为 `Posts`（搜索文章）
    ### 返回:
    - 搜索结果

    # [English]
    ### Purpose:
    - Search API
    ### Parameters:
    - query: Search keyword
    - max_cursor: Pagination parameter, can be obtained from the return result of the last request. It
    is empty for the first request, and the `max_cursor` returned by the last request is used for
    subsequent requests. You can judge whether there is more data by the `has_more` field in the return
    result.
    - filter_type: Search filter type, default is an empty string, optional values are as follows:
        - Empty string: All (default using this parameter to search)
        - video: Search only video
        - posts: Search only posts
    - order_by: Search sort type, default is an empty string, optional values are as follows:
        - Empty string: Relevance (default using this parameter to sort)
        - popular: Sort by popularity
        - recent: Sort from new to old
    - search_tab: Search type, default is `main`, optional values are as follows:
        - main: Display as `Top` in the APP (comprehensive search, default using this parameter to
    search)
        - user: Display as `Accounts` in the APP (search user accounts)
        - hashtag: Display as `Hashtags` in the APP (search hashtags)
        - article: Display as `Posts` in the APP (search articles)
    ### Return:
    - Search results

    # [示例/Example]
    query = \"lemon8\"
    max_cursor = \"\"
    filter_type = \"\"
    order_by = \"\"
    search_tab = \"main\"

    Args:
        query (str): 搜索关键词/Search keyword
        max_cursor (Union[Unset, str]): 翻页参数/Pagination parameter Default: ''.
        filter_type (Union[Unset, str]): 搜索过滤类型/Search filter type Default: ''.
        order_by (Union[Unset, str]): 搜索排序方式/Search sort type Default: ''.
        search_tab (Union[Unset, str]): 搜索类型/Search type Default: 'main'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        query=query,
        max_cursor=max_cursor,
        filter_type=filter_type,
        order_by=order_by,
        search_tab=search_tab,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    query: str,
    max_cursor: Union[Unset, str] = "",
    filter_type: Union[Unset, str] = "",
    order_by: Union[Unset, str] = "",
    search_tab: Union[Unset, str] = "main",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索接口/Search API

     # [中文]
    ### 用途:
    - 搜索接口
    ### 参数:
    - query: 搜索关键词
    - max_cursor:
    翻页参数，可以从上一次请求的返回结果中获取，第一次请求为空，后续请求使用上一次请求返回的`max_cursor`进行翻页，可以通过返回结果的`has_more`字段判断是否还有更多数据。
    - filter_type: 搜索过滤类型，默认为空字符串，可选值如下：
        - 空字符串：All（全部，默认使用此参数搜索）
        - video：只搜索视频作品
        - posts：只搜索文章作品
    - order_by: 搜索排序方式，默认为空字符串，可选值如下：
        - 空字符串：Relevance（相关度，默认使用此参数排序）
        - popular：流行度排序
        - recent：从新到旧排序
    - search_tab: 搜索类型，默认为`main`，可选值如下：
        - main：APP中显示为 `Top`（综合搜索，默认使用此参数搜索）
        - user：APP中显示为 `Accounts` （搜索用户账号）
        - hashtag：APP中显示为 `Hashtags`（搜索话题）
        - article：APP中显示为 `Posts`（搜索文章）
    ### 返回:
    - 搜索结果

    # [English]
    ### Purpose:
    - Search API
    ### Parameters:
    - query: Search keyword
    - max_cursor: Pagination parameter, can be obtained from the return result of the last request. It
    is empty for the first request, and the `max_cursor` returned by the last request is used for
    subsequent requests. You can judge whether there is more data by the `has_more` field in the return
    result.
    - filter_type: Search filter type, default is an empty string, optional values are as follows:
        - Empty string: All (default using this parameter to search)
        - video: Search only video
        - posts: Search only posts
    - order_by: Search sort type, default is an empty string, optional values are as follows:
        - Empty string: Relevance (default using this parameter to sort)
        - popular: Sort by popularity
        - recent: Sort from new to old
    - search_tab: Search type, default is `main`, optional values are as follows:
        - main: Display as `Top` in the APP (comprehensive search, default using this parameter to
    search)
        - user: Display as `Accounts` in the APP (search user accounts)
        - hashtag: Display as `Hashtags` in the APP (search hashtags)
        - article: Display as `Posts` in the APP (search articles)
    ### Return:
    - Search results

    # [示例/Example]
    query = \"lemon8\"
    max_cursor = \"\"
    filter_type = \"\"
    order_by = \"\"
    search_tab = \"main\"

    Args:
        query (str): 搜索关键词/Search keyword
        max_cursor (Union[Unset, str]): 翻页参数/Pagination parameter Default: ''.
        filter_type (Union[Unset, str]): 搜索过滤类型/Search filter type Default: ''.
        order_by (Union[Unset, str]): 搜索排序方式/Search sort type Default: ''.
        search_tab (Union[Unset, str]): 搜索类型/Search type Default: 'main'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            max_cursor=max_cursor,
            filter_type=filter_type,
            order_by=order_by,
            search_tab=search_tab,
        )
    ).parsed
