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
    keywords: str,
    page: Union[Unset, int] = 1,
    sort_type: Union[Unset, str] = "general",
    note_type: Union[Unset, str] = "0",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keywords"] = keywords

    params["page"] = page

    params["sort_type"] = sort_type

    params["note_type"] = note_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/xiaohongshu/web_v2/fetch_search_notes",
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
    keywords: str,
    page: Union[Unset, int] = 1,
    sort_type: Union[Unset, str] = "general",
    note_type: Union[Unset, str] = "0",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取搜索笔记/Fetch search notes

     # [中文]
    ### 用途:
    - 获取搜索笔记
    ### 参数:
    - keywords：搜索关键词
    - sort_type：排序方式
        - general：综合
        - time_descending：最新
        - popularity_descending：最热
    - note_type: 笔记类型
        - 0：全部
        - 1：视频
        - 2：图文
    ### 返回:
    - 搜索笔记

    # [English]
    ### Purpose:
    - Get search notes
    ### Parameters:
    - keywords: Search keywords
    - sort_type: Sort type
        - general: General
        - time_descending: Latest
        - popularity_descending: Popular
    - note_type: Note type
        - 0: All
        - 1: Video
        - 2: Note
    ### Return:
    - Search notes

    # [示例/Example]
    keywords = \"口红\"
    page = 1
    sort_type = \"general\"
    note_type = \"1\"

    Args:
        keywords (str): 搜索关键词/Search keywords
        page (Union[Unset, int]): 页码/Page number Default: 1.
        sort_type (Union[Unset, str]): 排序方式/Sort type Default: 'general'.
        note_type (Union[Unset, str]): 笔记类型/Note type Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keywords=keywords,
        page=page,
        sort_type=sort_type,
        note_type=note_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    keywords: str,
    page: Union[Unset, int] = 1,
    sort_type: Union[Unset, str] = "general",
    note_type: Union[Unset, str] = "0",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取搜索笔记/Fetch search notes

     # [中文]
    ### 用途:
    - 获取搜索笔记
    ### 参数:
    - keywords：搜索关键词
    - sort_type：排序方式
        - general：综合
        - time_descending：最新
        - popularity_descending：最热
    - note_type: 笔记类型
        - 0：全部
        - 1：视频
        - 2：图文
    ### 返回:
    - 搜索笔记

    # [English]
    ### Purpose:
    - Get search notes
    ### Parameters:
    - keywords: Search keywords
    - sort_type: Sort type
        - general: General
        - time_descending: Latest
        - popularity_descending: Popular
    - note_type: Note type
        - 0: All
        - 1: Video
        - 2: Note
    ### Return:
    - Search notes

    # [示例/Example]
    keywords = \"口红\"
    page = 1
    sort_type = \"general\"
    note_type = \"1\"

    Args:
        keywords (str): 搜索关键词/Search keywords
        page (Union[Unset, int]): 页码/Page number Default: 1.
        sort_type (Union[Unset, str]): 排序方式/Sort type Default: 'general'.
        note_type (Union[Unset, str]): 笔记类型/Note type Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        keywords=keywords,
        page=page,
        sort_type=sort_type,
        note_type=note_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keywords: str,
    page: Union[Unset, int] = 1,
    sort_type: Union[Unset, str] = "general",
    note_type: Union[Unset, str] = "0",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取搜索笔记/Fetch search notes

     # [中文]
    ### 用途:
    - 获取搜索笔记
    ### 参数:
    - keywords：搜索关键词
    - sort_type：排序方式
        - general：综合
        - time_descending：最新
        - popularity_descending：最热
    - note_type: 笔记类型
        - 0：全部
        - 1：视频
        - 2：图文
    ### 返回:
    - 搜索笔记

    # [English]
    ### Purpose:
    - Get search notes
    ### Parameters:
    - keywords: Search keywords
    - sort_type: Sort type
        - general: General
        - time_descending: Latest
        - popularity_descending: Popular
    - note_type: Note type
        - 0: All
        - 1: Video
        - 2: Note
    ### Return:
    - Search notes

    # [示例/Example]
    keywords = \"口红\"
    page = 1
    sort_type = \"general\"
    note_type = \"1\"

    Args:
        keywords (str): 搜索关键词/Search keywords
        page (Union[Unset, int]): 页码/Page number Default: 1.
        sort_type (Union[Unset, str]): 排序方式/Sort type Default: 'general'.
        note_type (Union[Unset, str]): 笔记类型/Note type Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keywords=keywords,
        page=page,
        sort_type=sort_type,
        note_type=note_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keywords: str,
    page: Union[Unset, int] = 1,
    sort_type: Union[Unset, str] = "general",
    note_type: Union[Unset, str] = "0",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取搜索笔记/Fetch search notes

     # [中文]
    ### 用途:
    - 获取搜索笔记
    ### 参数:
    - keywords：搜索关键词
    - sort_type：排序方式
        - general：综合
        - time_descending：最新
        - popularity_descending：最热
    - note_type: 笔记类型
        - 0：全部
        - 1：视频
        - 2：图文
    ### 返回:
    - 搜索笔记

    # [English]
    ### Purpose:
    - Get search notes
    ### Parameters:
    - keywords: Search keywords
    - sort_type: Sort type
        - general: General
        - time_descending: Latest
        - popularity_descending: Popular
    - note_type: Note type
        - 0: All
        - 1: Video
        - 2: Note
    ### Return:
    - Search notes

    # [示例/Example]
    keywords = \"口红\"
    page = 1
    sort_type = \"general\"
    note_type = \"1\"

    Args:
        keywords (str): 搜索关键词/Search keywords
        page (Union[Unset, int]): 页码/Page number Default: 1.
        sort_type (Union[Unset, str]): 排序方式/Sort type Default: 'general'.
        note_type (Union[Unset, str]): 笔记类型/Note type Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            keywords=keywords,
            page=page,
            sort_type=sort_type,
            note_type=note_type,
        )
    ).parsed
