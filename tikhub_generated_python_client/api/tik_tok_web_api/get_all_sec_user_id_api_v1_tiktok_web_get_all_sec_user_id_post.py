from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: list[str],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tiktok/web/get_all_sec_user_id",
    }

    _kwargs["json"] = body

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
    body: list[str],
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""提取列表用户sec_user_id/Extract list user sec_user_id

     # [中文]
    ### 用途:
    - 提取列表用户id
    ### 参数:
    - url: 用户主页链接（最多支持10个链接）、
    ### 返回:
    - 如果链接成功获取到sec_user_id，则返回sec_user_id，否则返回原始的输入链接，后续可以手动校验链接无法获取sec_user_id的原因。

    # [English]
    ### Purpose:
    - Extract list user id
    ### Parameters:
    - url: User homepage link (Support up to 10 links)
    ### Return:
    - If the sec_user_id is successfully obtained, the sec_user_id is returned, otherwise the original
    input link is returned, and the reason why the sec_user_id cannot be obtained can be manually
    verified later.

    # [示例/Example]
    url = [\"https://www.tiktok.com/@tiktok\"]

    Args:
        body (list[str]): 用户主页链接/User homepage link

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
    body: list[str],
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""提取列表用户sec_user_id/Extract list user sec_user_id

     # [中文]
    ### 用途:
    - 提取列表用户id
    ### 参数:
    - url: 用户主页链接（最多支持10个链接）、
    ### 返回:
    - 如果链接成功获取到sec_user_id，则返回sec_user_id，否则返回原始的输入链接，后续可以手动校验链接无法获取sec_user_id的原因。

    # [English]
    ### Purpose:
    - Extract list user id
    ### Parameters:
    - url: User homepage link (Support up to 10 links)
    ### Return:
    - If the sec_user_id is successfully obtained, the sec_user_id is returned, otherwise the original
    input link is returned, and the reason why the sec_user_id cannot be obtained can be manually
    verified later.

    # [示例/Example]
    url = [\"https://www.tiktok.com/@tiktok\"]

    Args:
        body (list[str]): 用户主页链接/User homepage link

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
    body: list[str],
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""提取列表用户sec_user_id/Extract list user sec_user_id

     # [中文]
    ### 用途:
    - 提取列表用户id
    ### 参数:
    - url: 用户主页链接（最多支持10个链接）、
    ### 返回:
    - 如果链接成功获取到sec_user_id，则返回sec_user_id，否则返回原始的输入链接，后续可以手动校验链接无法获取sec_user_id的原因。

    # [English]
    ### Purpose:
    - Extract list user id
    ### Parameters:
    - url: User homepage link (Support up to 10 links)
    ### Return:
    - If the sec_user_id is successfully obtained, the sec_user_id is returned, otherwise the original
    input link is returned, and the reason why the sec_user_id cannot be obtained can be manually
    verified later.

    # [示例/Example]
    url = [\"https://www.tiktok.com/@tiktok\"]

    Args:
        body (list[str]): 用户主页链接/User homepage link

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
    body: list[str],
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""提取列表用户sec_user_id/Extract list user sec_user_id

     # [中文]
    ### 用途:
    - 提取列表用户id
    ### 参数:
    - url: 用户主页链接（最多支持10个链接）、
    ### 返回:
    - 如果链接成功获取到sec_user_id，则返回sec_user_id，否则返回原始的输入链接，后续可以手动校验链接无法获取sec_user_id的原因。

    # [English]
    ### Purpose:
    - Extract list user id
    ### Parameters:
    - url: User homepage link (Support up to 10 links)
    ### Return:
    - If the sec_user_id is successfully obtained, the sec_user_id is returned, otherwise the original
    input link is returned, and the reason why the sec_user_id cannot be obtained can be manually
    verified later.

    # [示例/Example]
    url = [\"https://www.tiktok.com/@tiktok\"]

    Args:
        body (list[str]): 用户主页链接/User homepage link

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
