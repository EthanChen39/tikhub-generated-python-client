from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import UNSET, Response


def _get_kwargs(
    *,
    token: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["token"] = token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/temp_mail/v1/get_emails_inbox",
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
    token: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """Get Emails

     # [中文]
    ### 用途:
    - 获取邮件列表
    ### 参数:
    - token: 邮箱Bearer Token
    ### 返回:
    - emails: 邮件列表

    # [English]
    ### Purpose:
    - Get a list of emails
    ### Parameters:
    - token: Email Bearer Token
    ### Returns:
    - emails: List of emails

    Args:
        token (str): Bearer Token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        token=token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    token: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """Get Emails

     # [中文]
    ### 用途:
    - 获取邮件列表
    ### 参数:
    - token: 邮箱Bearer Token
    ### 返回:
    - emails: 邮件列表

    # [English]
    ### Purpose:
    - Get a list of emails
    ### Parameters:
    - token: Email Bearer Token
    ### Returns:
    - emails: List of emails

    Args:
        token (str): Bearer Token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        token=token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """Get Emails

     # [中文]
    ### 用途:
    - 获取邮件列表
    ### 参数:
    - token: 邮箱Bearer Token
    ### 返回:
    - emails: 邮件列表

    # [English]
    ### Purpose:
    - Get a list of emails
    ### Parameters:
    - token: Email Bearer Token
    ### Returns:
    - emails: List of emails

    Args:
        token (str): Bearer Token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        token=token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """Get Emails

     # [中文]
    ### 用途:
    - 获取邮件列表
    ### 参数:
    - token: 邮箱Bearer Token
    ### 返回:
    - emails: 邮件列表

    # [English]
    ### Purpose:
    - Get a list of emails
    ### Parameters:
    - token: Email Bearer Token
    ### Returns:
    - emails: List of emails

    Args:
        token (str): Bearer Token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            token=token,
        )
    ).parsed
