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
    note_id: Union[Unset, str] = "",
    share_text: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["note_id"] = note_id

    params["share_text"] = share_text

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/xiaohongshu/web/get_note_info_v2",
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
    note_id: Union[Unset, str] = "",
    share_text: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取笔记信息 V2/Get note info V2

     # [中文]
    ### 用途:
    - 获取笔记信息 V2
    ### 参数:
    - note_id: 笔记ID，可以从小红书的分享链接中获取
    - share_text: 小红书分享链接（支持APP和Web端分享链接）
    - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。
    ### 返回:
    - 笔记信息

    # [English]
    ### Purpose:
    - Get note info V2
    ### Parameters:
    - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
    - share_text: Xiaohongshu sharing link (support APP and Web sharing link)
    - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both
    are carried, `note_id` shall prevail.
    ### Return:
    - Note info

    # [示例/Example]
    note_id=\"665f95200000000006005624\"

    Args:
        note_id (Union[Unset, str]): 笔记ID/Note ID Default: ''.
        share_text (Union[Unset, str]): 分享链接/Share link Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        note_id=note_id,
        share_text=share_text,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    note_id: Union[Unset, str] = "",
    share_text: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取笔记信息 V2/Get note info V2

     # [中文]
    ### 用途:
    - 获取笔记信息 V2
    ### 参数:
    - note_id: 笔记ID，可以从小红书的分享链接中获取
    - share_text: 小红书分享链接（支持APP和Web端分享链接）
    - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。
    ### 返回:
    - 笔记信息

    # [English]
    ### Purpose:
    - Get note info V2
    ### Parameters:
    - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
    - share_text: Xiaohongshu sharing link (support APP and Web sharing link)
    - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both
    are carried, `note_id` shall prevail.
    ### Return:
    - Note info

    # [示例/Example]
    note_id=\"665f95200000000006005624\"

    Args:
        note_id (Union[Unset, str]): 笔记ID/Note ID Default: ''.
        share_text (Union[Unset, str]): 分享链接/Share link Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        note_id=note_id,
        share_text=share_text,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    note_id: Union[Unset, str] = "",
    share_text: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取笔记信息 V2/Get note info V2

     # [中文]
    ### 用途:
    - 获取笔记信息 V2
    ### 参数:
    - note_id: 笔记ID，可以从小红书的分享链接中获取
    - share_text: 小红书分享链接（支持APP和Web端分享链接）
    - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。
    ### 返回:
    - 笔记信息

    # [English]
    ### Purpose:
    - Get note info V2
    ### Parameters:
    - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
    - share_text: Xiaohongshu sharing link (support APP and Web sharing link)
    - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both
    are carried, `note_id` shall prevail.
    ### Return:
    - Note info

    # [示例/Example]
    note_id=\"665f95200000000006005624\"

    Args:
        note_id (Union[Unset, str]): 笔记ID/Note ID Default: ''.
        share_text (Union[Unset, str]): 分享链接/Share link Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        note_id=note_id,
        share_text=share_text,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    note_id: Union[Unset, str] = "",
    share_text: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取笔记信息 V2/Get note info V2

     # [中文]
    ### 用途:
    - 获取笔记信息 V2
    ### 参数:
    - note_id: 笔记ID，可以从小红书的分享链接中获取
    - share_text: 小红书分享链接（支持APP和Web端分享链接）
    - 优先使用`note_id`，如果没有则使用`share_text`，两个参数二选一，如都携带则以`note_id`为准。
    ### 返回:
    - 笔记信息

    # [English]
    ### Purpose:
    - Get note info V2
    ### Parameters:
    - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
    - share_text: Xiaohongshu sharing link (support APP and Web sharing link)
    - Prefer to use `note_id`, if not, use `share_text`, one of the two parameters is required, if both
    are carried, `note_id` shall prevail.
    ### Return:
    - Note info

    # [示例/Example]
    note_id=\"665f95200000000006005624\"

    Args:
        note_id (Union[Unset, str]): 笔记ID/Note ID Default: ''.
        share_text (Union[Unset, str]): 分享链接/Share link Default: ''.

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
            share_text=share_text,
        )
    ).parsed
