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
    keyword: str,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, str] = "general",
    note_type: Union[Unset, str] = "_0",
    note_time: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["page"] = page

    params["sort"] = sort

    params["noteType"] = note_type

    params["noteTime"] = note_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/xiaohongshu/web/search_notes",
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
    keyword: str,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, str] = "general",
    note_type: Union[Unset, str] = "_0",
    note_time: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索笔记/Search notes

     # [中文]
    ### 用途:
    - 搜索笔记
    ### 参数:
    - keyword: 搜索关键词
    - page: 页码，默认为1
    - sort: 排序方式
        - 综合排序（默认参数）: general
        - 最热排序: popularity_descending
        - 最新排序: time_descending
        - 最多评论: comment_descending
        - 最多收藏: collect_descending
    - noteType: 笔记类型
        - 综合笔记（默认参数）: _0
        - 视频笔记: _1
        - 图文笔记: _2
        - 直播: _3
    - noteTime: 发布时间
        - 不限: \"\"
        - 一天内 :一天内
        - 一周内 :一周内
        - 半年内 :半年内
    ### 返回:
    - 笔记列表

    # [English]
    ### Purpose:
    - Search notes
    ### Parameters:
    - keyword: Keyword
    - page: Page, default is 1
    - sort: Sort
        - General sort (default): general
        - Popularity sort: popularity_descending
        - Latest sort: time_descending
        - Most comments: comment_descending
        - Most favorites: collect_descending
    - noteType: Note type
        - General note (default): _0
        - Video note: _1
        - Image note: _2
        - Live: _3
    - noteTime: Release time
        - No limit: \"\"
        - Within one day: 一天内
        - Within one week: 一周内
        - Within half a year: 半年内
    ### Return:
    - Note list

    # [示例/Example]
    keyword=\"美食\"
    page=1
    sort=\"general\"
    noteType=\"_0\"

    Args:
        keyword (str): 搜索关键词/Keyword
        page (Union[Unset, int]): 页码/Page Default: 1.
        sort (Union[Unset, str]): 排序方式/Sort Default: 'general'.
        note_type (Union[Unset, str]): 笔记类型/Note type Default: '_0'.
        note_time (Union[Unset, str]): 发布时间/Release time Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        page=page,
        sort=sort,
        note_type=note_type,
        note_time=note_time,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    keyword: str,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, str] = "general",
    note_type: Union[Unset, str] = "_0",
    note_time: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索笔记/Search notes

     # [中文]
    ### 用途:
    - 搜索笔记
    ### 参数:
    - keyword: 搜索关键词
    - page: 页码，默认为1
    - sort: 排序方式
        - 综合排序（默认参数）: general
        - 最热排序: popularity_descending
        - 最新排序: time_descending
        - 最多评论: comment_descending
        - 最多收藏: collect_descending
    - noteType: 笔记类型
        - 综合笔记（默认参数）: _0
        - 视频笔记: _1
        - 图文笔记: _2
        - 直播: _3
    - noteTime: 发布时间
        - 不限: \"\"
        - 一天内 :一天内
        - 一周内 :一周内
        - 半年内 :半年内
    ### 返回:
    - 笔记列表

    # [English]
    ### Purpose:
    - Search notes
    ### Parameters:
    - keyword: Keyword
    - page: Page, default is 1
    - sort: Sort
        - General sort (default): general
        - Popularity sort: popularity_descending
        - Latest sort: time_descending
        - Most comments: comment_descending
        - Most favorites: collect_descending
    - noteType: Note type
        - General note (default): _0
        - Video note: _1
        - Image note: _2
        - Live: _3
    - noteTime: Release time
        - No limit: \"\"
        - Within one day: 一天内
        - Within one week: 一周内
        - Within half a year: 半年内
    ### Return:
    - Note list

    # [示例/Example]
    keyword=\"美食\"
    page=1
    sort=\"general\"
    noteType=\"_0\"

    Args:
        keyword (str): 搜索关键词/Keyword
        page (Union[Unset, int]): 页码/Page Default: 1.
        sort (Union[Unset, str]): 排序方式/Sort Default: 'general'.
        note_type (Union[Unset, str]): 笔记类型/Note type Default: '_0'.
        note_time (Union[Unset, str]): 发布时间/Release time Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        keyword=keyword,
        page=page,
        sort=sort,
        note_type=note_type,
        note_time=note_time,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, str] = "general",
    note_type: Union[Unset, str] = "_0",
    note_time: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索笔记/Search notes

     # [中文]
    ### 用途:
    - 搜索笔记
    ### 参数:
    - keyword: 搜索关键词
    - page: 页码，默认为1
    - sort: 排序方式
        - 综合排序（默认参数）: general
        - 最热排序: popularity_descending
        - 最新排序: time_descending
        - 最多评论: comment_descending
        - 最多收藏: collect_descending
    - noteType: 笔记类型
        - 综合笔记（默认参数）: _0
        - 视频笔记: _1
        - 图文笔记: _2
        - 直播: _3
    - noteTime: 发布时间
        - 不限: \"\"
        - 一天内 :一天内
        - 一周内 :一周内
        - 半年内 :半年内
    ### 返回:
    - 笔记列表

    # [English]
    ### Purpose:
    - Search notes
    ### Parameters:
    - keyword: Keyword
    - page: Page, default is 1
    - sort: Sort
        - General sort (default): general
        - Popularity sort: popularity_descending
        - Latest sort: time_descending
        - Most comments: comment_descending
        - Most favorites: collect_descending
    - noteType: Note type
        - General note (default): _0
        - Video note: _1
        - Image note: _2
        - Live: _3
    - noteTime: Release time
        - No limit: \"\"
        - Within one day: 一天内
        - Within one week: 一周内
        - Within half a year: 半年内
    ### Return:
    - Note list

    # [示例/Example]
    keyword=\"美食\"
    page=1
    sort=\"general\"
    noteType=\"_0\"

    Args:
        keyword (str): 搜索关键词/Keyword
        page (Union[Unset, int]): 页码/Page Default: 1.
        sort (Union[Unset, str]): 排序方式/Sort Default: 'general'.
        note_type (Union[Unset, str]): 笔记类型/Note type Default: '_0'.
        note_time (Union[Unset, str]): 发布时间/Release time Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        page=page,
        sort=sort,
        note_type=note_type,
        note_time=note_time,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
    page: Union[Unset, int] = 1,
    sort: Union[Unset, str] = "general",
    note_type: Union[Unset, str] = "_0",
    note_time: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索笔记/Search notes

     # [中文]
    ### 用途:
    - 搜索笔记
    ### 参数:
    - keyword: 搜索关键词
    - page: 页码，默认为1
    - sort: 排序方式
        - 综合排序（默认参数）: general
        - 最热排序: popularity_descending
        - 最新排序: time_descending
        - 最多评论: comment_descending
        - 最多收藏: collect_descending
    - noteType: 笔记类型
        - 综合笔记（默认参数）: _0
        - 视频笔记: _1
        - 图文笔记: _2
        - 直播: _3
    - noteTime: 发布时间
        - 不限: \"\"
        - 一天内 :一天内
        - 一周内 :一周内
        - 半年内 :半年内
    ### 返回:
    - 笔记列表

    # [English]
    ### Purpose:
    - Search notes
    ### Parameters:
    - keyword: Keyword
    - page: Page, default is 1
    - sort: Sort
        - General sort (default): general
        - Popularity sort: popularity_descending
        - Latest sort: time_descending
        - Most comments: comment_descending
        - Most favorites: collect_descending
    - noteType: Note type
        - General note (default): _0
        - Video note: _1
        - Image note: _2
        - Live: _3
    - noteTime: Release time
        - No limit: \"\"
        - Within one day: 一天内
        - Within one week: 一周内
        - Within half a year: 半年内
    ### Return:
    - Note list

    # [示例/Example]
    keyword=\"美食\"
    page=1
    sort=\"general\"
    noteType=\"_0\"

    Args:
        keyword (str): 搜索关键词/Keyword
        page (Union[Unset, int]): 页码/Page Default: 1.
        sort (Union[Unset, str]): 排序方式/Sort Default: 'general'.
        note_type (Union[Unset, str]): 笔记类型/Note type Default: '_0'.
        note_time (Union[Unset, str]): 发布时间/Release time Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            keyword=keyword,
            page=page,
            sort=sort,
            note_type=note_type,
            note_time=note_time,
        )
    ).parsed
