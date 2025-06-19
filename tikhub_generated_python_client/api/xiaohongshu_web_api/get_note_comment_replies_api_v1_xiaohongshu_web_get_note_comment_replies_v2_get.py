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
    note_id: str,
    comment_id: str,
    last_cursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["note_id"] = note_id

    params["comment_id"] = comment_id

    params["lastCursor"] = last_cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/xiaohongshu/web/get_note_comment_replies_v2",
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
    note_id: str,
    comment_id: str,
    last_cursor: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取笔记评论回复 V2/Get note comment replies V2

     # [中文]
    ### 用途:
    - 获取笔记评论回复 V2
    ### 参数:
    - note_id: 笔记ID，可以从小红书的分享链接中获取
    - comment_id: 评论ID
    - lastCursor: 第一次请求时为空，之后请求时使用上一次请求响应中返回的游标
    ### 返回:
    - 笔记评论回复列表

    # [English]
    ### Purpose:
    - Get note comment replies V2
    ### Parameters:
    - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
    - comment_id: Comment ID
    - lastCursor: Last cursor, empty for the first request, use the cursor returned in the last response
    for subsequent requests
    ### Return:
    - Note comment replies list

    # [示例/Example]
    note_id=\"6683b283000000001f0052bf\"
    comment_id=\"6683ec5b000000000303b91a\"
    lastCursor=None

    Args:
        note_id (str): 笔记ID/Note ID
        comment_id (str): 评论ID/Comment ID
        last_cursor (Union[Unset, str]): 上一页的游标/Last cursor

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        note_id=note_id,
        comment_id=comment_id,
        last_cursor=last_cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    note_id: str,
    comment_id: str,
    last_cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取笔记评论回复 V2/Get note comment replies V2

     # [中文]
    ### 用途:
    - 获取笔记评论回复 V2
    ### 参数:
    - note_id: 笔记ID，可以从小红书的分享链接中获取
    - comment_id: 评论ID
    - lastCursor: 第一次请求时为空，之后请求时使用上一次请求响应中返回的游标
    ### 返回:
    - 笔记评论回复列表

    # [English]
    ### Purpose:
    - Get note comment replies V2
    ### Parameters:
    - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
    - comment_id: Comment ID
    - lastCursor: Last cursor, empty for the first request, use the cursor returned in the last response
    for subsequent requests
    ### Return:
    - Note comment replies list

    # [示例/Example]
    note_id=\"6683b283000000001f0052bf\"
    comment_id=\"6683ec5b000000000303b91a\"
    lastCursor=None

    Args:
        note_id (str): 笔记ID/Note ID
        comment_id (str): 评论ID/Comment ID
        last_cursor (Union[Unset, str]): 上一页的游标/Last cursor

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        note_id=note_id,
        comment_id=comment_id,
        last_cursor=last_cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    note_id: str,
    comment_id: str,
    last_cursor: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取笔记评论回复 V2/Get note comment replies V2

     # [中文]
    ### 用途:
    - 获取笔记评论回复 V2
    ### 参数:
    - note_id: 笔记ID，可以从小红书的分享链接中获取
    - comment_id: 评论ID
    - lastCursor: 第一次请求时为空，之后请求时使用上一次请求响应中返回的游标
    ### 返回:
    - 笔记评论回复列表

    # [English]
    ### Purpose:
    - Get note comment replies V2
    ### Parameters:
    - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
    - comment_id: Comment ID
    - lastCursor: Last cursor, empty for the first request, use the cursor returned in the last response
    for subsequent requests
    ### Return:
    - Note comment replies list

    # [示例/Example]
    note_id=\"6683b283000000001f0052bf\"
    comment_id=\"6683ec5b000000000303b91a\"
    lastCursor=None

    Args:
        note_id (str): 笔记ID/Note ID
        comment_id (str): 评论ID/Comment ID
        last_cursor (Union[Unset, str]): 上一页的游标/Last cursor

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        note_id=note_id,
        comment_id=comment_id,
        last_cursor=last_cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    note_id: str,
    comment_id: str,
    last_cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取笔记评论回复 V2/Get note comment replies V2

     # [中文]
    ### 用途:
    - 获取笔记评论回复 V2
    ### 参数:
    - note_id: 笔记ID，可以从小红书的分享链接中获取
    - comment_id: 评论ID
    - lastCursor: 第一次请求时为空，之后请求时使用上一次请求响应中返回的游标
    ### 返回:
    - 笔记评论回复列表

    # [English]
    ### Purpose:
    - Get note comment replies V2
    ### Parameters:
    - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
    - comment_id: Comment ID
    - lastCursor: Last cursor, empty for the first request, use the cursor returned in the last response
    for subsequent requests
    ### Return:
    - Note comment replies list

    # [示例/Example]
    note_id=\"6683b283000000001f0052bf\"
    comment_id=\"6683ec5b000000000303b91a\"
    lastCursor=None

    Args:
        note_id (str): 笔记ID/Note ID
        comment_id (str): 评论ID/Comment ID
        last_cursor (Union[Unset, str]): 上一页的游标/Last cursor

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            note_id=note_id,
            comment_id=comment_id,
            last_cursor=last_cursor,
        )
    ).parsed
