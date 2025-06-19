from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_note_info_v5_request import GetNoteInfoV5Request
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: GetNoteInfoV5Request,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/xiaohongshu/web/get_note_info_v5",
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
    body: GetNoteInfoV5Request,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取笔记信息 V5 (自带Cookie)/Get note info V5 (Self-provided Cookie)

     # [中文]
    ### 用途:
    - 获取笔记信息V5，用户自行提供Cookie来获取笔记信息
    - 此接口收费0.001$
    ### 参数:
    - note_id: 笔记ID，可以从小红书的分享链接中获取
    - xsec_token: X-Sec-Token，可以从搜索接口中获取，分享链接中也有/X-Sec-Token, can be obtained from the search interface,
    also in the sharing link
    - cookie: 用户自行提供的已登录的网页Cookie
    - proxy: 代理，格式：http://用户名:密码@IP:端口/Proxy, format: http://username:password@IP:port
    - 最好使用代理，避免被封号或其他未知问题。

    ### 返回:
    - 笔记信息

    # [English]
    ### Purpose:
    - Get note info V5, user provides Cookie to get note info
    - This interface charges 0.001$
    ### Parameters:
    - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
    - xsec_token: X-Sec-Token, can be obtained from the search interface, also in the sharing link
    - cookie: User provided logged-in web Cookie
    - proxy: Proxy, format: http://username:password@IP:port
    - It is recommended to use a proxy to avoid being banned or other unknown issues.
    ### Return:
    - Note info

    # [示例/Example]
    note_id = \"67855d09000000001703d449\"
    xsec_token = \"ABfpRSESmZDRbX-EX7lzEztktMngxPVC9kU-dgQmuQoNo=\"
    cookie = \"Your Cookie\"
    proxy = \"http://username:password@IP:port\"

    Args:
        body (GetNoteInfoV5Request):

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
    body: GetNoteInfoV5Request,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取笔记信息 V5 (自带Cookie)/Get note info V5 (Self-provided Cookie)

     # [中文]
    ### 用途:
    - 获取笔记信息V5，用户自行提供Cookie来获取笔记信息
    - 此接口收费0.001$
    ### 参数:
    - note_id: 笔记ID，可以从小红书的分享链接中获取
    - xsec_token: X-Sec-Token，可以从搜索接口中获取，分享链接中也有/X-Sec-Token, can be obtained from the search interface,
    also in the sharing link
    - cookie: 用户自行提供的已登录的网页Cookie
    - proxy: 代理，格式：http://用户名:密码@IP:端口/Proxy, format: http://username:password@IP:port
    - 最好使用代理，避免被封号或其他未知问题。

    ### 返回:
    - 笔记信息

    # [English]
    ### Purpose:
    - Get note info V5, user provides Cookie to get note info
    - This interface charges 0.001$
    ### Parameters:
    - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
    - xsec_token: X-Sec-Token, can be obtained from the search interface, also in the sharing link
    - cookie: User provided logged-in web Cookie
    - proxy: Proxy, format: http://username:password@IP:port
    - It is recommended to use a proxy to avoid being banned or other unknown issues.
    ### Return:
    - Note info

    # [示例/Example]
    note_id = \"67855d09000000001703d449\"
    xsec_token = \"ABfpRSESmZDRbX-EX7lzEztktMngxPVC9kU-dgQmuQoNo=\"
    cookie = \"Your Cookie\"
    proxy = \"http://username:password@IP:port\"

    Args:
        body (GetNoteInfoV5Request):

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
    body: GetNoteInfoV5Request,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取笔记信息 V5 (自带Cookie)/Get note info V5 (Self-provided Cookie)

     # [中文]
    ### 用途:
    - 获取笔记信息V5，用户自行提供Cookie来获取笔记信息
    - 此接口收费0.001$
    ### 参数:
    - note_id: 笔记ID，可以从小红书的分享链接中获取
    - xsec_token: X-Sec-Token，可以从搜索接口中获取，分享链接中也有/X-Sec-Token, can be obtained from the search interface,
    also in the sharing link
    - cookie: 用户自行提供的已登录的网页Cookie
    - proxy: 代理，格式：http://用户名:密码@IP:端口/Proxy, format: http://username:password@IP:port
    - 最好使用代理，避免被封号或其他未知问题。

    ### 返回:
    - 笔记信息

    # [English]
    ### Purpose:
    - Get note info V5, user provides Cookie to get note info
    - This interface charges 0.001$
    ### Parameters:
    - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
    - xsec_token: X-Sec-Token, can be obtained from the search interface, also in the sharing link
    - cookie: User provided logged-in web Cookie
    - proxy: Proxy, format: http://username:password@IP:port
    - It is recommended to use a proxy to avoid being banned or other unknown issues.
    ### Return:
    - Note info

    # [示例/Example]
    note_id = \"67855d09000000001703d449\"
    xsec_token = \"ABfpRSESmZDRbX-EX7lzEztktMngxPVC9kU-dgQmuQoNo=\"
    cookie = \"Your Cookie\"
    proxy = \"http://username:password@IP:port\"

    Args:
        body (GetNoteInfoV5Request):

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
    body: GetNoteInfoV5Request,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取笔记信息 V5 (自带Cookie)/Get note info V5 (Self-provided Cookie)

     # [中文]
    ### 用途:
    - 获取笔记信息V5，用户自行提供Cookie来获取笔记信息
    - 此接口收费0.001$
    ### 参数:
    - note_id: 笔记ID，可以从小红书的分享链接中获取
    - xsec_token: X-Sec-Token，可以从搜索接口中获取，分享链接中也有/X-Sec-Token, can be obtained from the search interface,
    also in the sharing link
    - cookie: 用户自行提供的已登录的网页Cookie
    - proxy: 代理，格式：http://用户名:密码@IP:端口/Proxy, format: http://username:password@IP:port
    - 最好使用代理，避免被封号或其他未知问题。

    ### 返回:
    - 笔记信息

    # [English]
    ### Purpose:
    - Get note info V5, user provides Cookie to get note info
    - This interface charges 0.001$
    ### Parameters:
    - note_id: Note ID, can be obtained from the sharing link of Xiaohongshu website.
    - xsec_token: X-Sec-Token, can be obtained from the search interface, also in the sharing link
    - cookie: User provided logged-in web Cookie
    - proxy: Proxy, format: http://username:password@IP:port
    - It is recommended to use a proxy to avoid being banned or other unknown issues.
    ### Return:
    - Note info

    # [示例/Example]
    note_id = \"67855d09000000001703d449\"
    xsec_token = \"ABfpRSESmZDRbX-EX7lzEztktMngxPVC9kU-dgQmuQoNo=\"
    cookie = \"Your Cookie\"
    proxy = \"http://username:password@IP:port\"

    Args:
        body (GetNoteInfoV5Request):

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
