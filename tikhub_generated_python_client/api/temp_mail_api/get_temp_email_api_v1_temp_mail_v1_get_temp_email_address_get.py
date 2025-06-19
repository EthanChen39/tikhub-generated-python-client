from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/temp_mail/v1/get_temp_email_address",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ResponseModel]:
    if response.status_code == 200:
        response_200 = ResponseModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ResponseModel]:
    """Get Temp Email

     # [中文]
    ### 用途:
    - 获取一个临时邮箱地址
    - 用于注册或者接收邮件，该邮箱地址不会被删除，也不会被其他人使用。
    - 该邮箱无法发送邮件，只能接收邮件。
    - 请自行保存邮箱地址、用户名、密码、Bearer Token，我们无法帮助您找回这些关键信息。
    ### 参数:
    - 无
    ### 返回:
    - domain: 邮箱域名
    - name: 邮箱用户名
    - password: 邮箱密码
    - email_address: 邮箱地址
    - token: 邮箱Bearer Token

    # [English]
    ### Purpose:
    - Get a temporary email address
    - Used for registration or receiving emails, this email address will not be deleted or used by
    others.
    - This email cannot send emails, only receive emails.
    - Please save the email address, username, password, and Bearer Token yourself, we cannot help you
    retrieve this critical information.
    ### Parameters:
    - None
    ### Returns:
    - domain: Email domain
    - name: Email username
    - password: Email password
    - email_address: Email address
    - token: Email Bearer Token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseModel]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[ResponseModel]:
    """Get Temp Email

     # [中文]
    ### 用途:
    - 获取一个临时邮箱地址
    - 用于注册或者接收邮件，该邮箱地址不会被删除，也不会被其他人使用。
    - 该邮箱无法发送邮件，只能接收邮件。
    - 请自行保存邮箱地址、用户名、密码、Bearer Token，我们无法帮助您找回这些关键信息。
    ### 参数:
    - 无
    ### 返回:
    - domain: 邮箱域名
    - name: 邮箱用户名
    - password: 邮箱密码
    - email_address: 邮箱地址
    - token: 邮箱Bearer Token

    # [English]
    ### Purpose:
    - Get a temporary email address
    - Used for registration or receiving emails, this email address will not be deleted or used by
    others.
    - This email cannot send emails, only receive emails.
    - Please save the email address, username, password, and Bearer Token yourself, we cannot help you
    retrieve this critical information.
    ### Parameters:
    - None
    ### Returns:
    - domain: Email domain
    - name: Email username
    - password: Email password
    - email_address: Email address
    - token: Email Bearer Token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseModel
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ResponseModel]:
    """Get Temp Email

     # [中文]
    ### 用途:
    - 获取一个临时邮箱地址
    - 用于注册或者接收邮件，该邮箱地址不会被删除，也不会被其他人使用。
    - 该邮箱无法发送邮件，只能接收邮件。
    - 请自行保存邮箱地址、用户名、密码、Bearer Token，我们无法帮助您找回这些关键信息。
    ### 参数:
    - 无
    ### 返回:
    - domain: 邮箱域名
    - name: 邮箱用户名
    - password: 邮箱密码
    - email_address: 邮箱地址
    - token: 邮箱Bearer Token

    # [English]
    ### Purpose:
    - Get a temporary email address
    - Used for registration or receiving emails, this email address will not be deleted or used by
    others.
    - This email cannot send emails, only receive emails.
    - Please save the email address, username, password, and Bearer Token yourself, we cannot help you
    retrieve this critical information.
    ### Parameters:
    - None
    ### Returns:
    - domain: Email domain
    - name: Email username
    - password: Email password
    - email_address: Email address
    - token: Email Bearer Token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseModel]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[ResponseModel]:
    """Get Temp Email

     # [中文]
    ### 用途:
    - 获取一个临时邮箱地址
    - 用于注册或者接收邮件，该邮箱地址不会被删除，也不会被其他人使用。
    - 该邮箱无法发送邮件，只能接收邮件。
    - 请自行保存邮箱地址、用户名、密码、Bearer Token，我们无法帮助您找回这些关键信息。
    ### 参数:
    - 无
    ### 返回:
    - domain: 邮箱域名
    - name: 邮箱用户名
    - password: 邮箱密码
    - email_address: 邮箱地址
    - token: 邮箱Bearer Token

    # [English]
    ### Purpose:
    - Get a temporary email address
    - Used for registration or receiving emails, this email address will not be deleted or used by
    others.
    - This email cannot send emails, only receive emails.
    - Please save the email address, username, password, and Bearer Token yourself, we cannot help you
    retrieve this critical information.
    ### Parameters:
    - None
    ### Returns:
    - domain: Email domain
    - name: Email username
    - password: Email password
    - email_address: Email address
    - token: Email Bearer Token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
