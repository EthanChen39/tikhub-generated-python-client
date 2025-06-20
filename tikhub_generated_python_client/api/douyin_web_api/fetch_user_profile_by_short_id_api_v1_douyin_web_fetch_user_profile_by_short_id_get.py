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
    short_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["short_id"] = short_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/web/fetch_user_profile_by_short_id",
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
    short_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""使用Short ID获取用户信息/Get user information by Short ID

     # [中文]
    ### 用途:
    - 使用Short ID获取用户信息
    ### 参数:
    - short_id: 用户Short ID
    ### 返回:
    - 用户信息

    # [English]
    ### Purpose:
    - Get user information by Short ID
    ### Parameters:
    - short_id: User Short ID
    ### Return:
    - User information

    # [示例/Example]
    short_id = \"114131058\"

    Args:
        short_id (str): 用户Short ID/User Short ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        short_id=short_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    short_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""使用Short ID获取用户信息/Get user information by Short ID

     # [中文]
    ### 用途:
    - 使用Short ID获取用户信息
    ### 参数:
    - short_id: 用户Short ID
    ### 返回:
    - 用户信息

    # [English]
    ### Purpose:
    - Get user information by Short ID
    ### Parameters:
    - short_id: User Short ID
    ### Return:
    - User information

    # [示例/Example]
    short_id = \"114131058\"

    Args:
        short_id (str): 用户Short ID/User Short ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        short_id=short_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    short_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""使用Short ID获取用户信息/Get user information by Short ID

     # [中文]
    ### 用途:
    - 使用Short ID获取用户信息
    ### 参数:
    - short_id: 用户Short ID
    ### 返回:
    - 用户信息

    # [English]
    ### Purpose:
    - Get user information by Short ID
    ### Parameters:
    - short_id: User Short ID
    ### Return:
    - User information

    # [示例/Example]
    short_id = \"114131058\"

    Args:
        short_id (str): 用户Short ID/User Short ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        short_id=short_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    short_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""使用Short ID获取用户信息/Get user information by Short ID

     # [中文]
    ### 用途:
    - 使用Short ID获取用户信息
    ### 参数:
    - short_id: 用户Short ID
    ### 返回:
    - 用户信息

    # [English]
    ### Purpose:
    - Get user information by Short ID
    ### Parameters:
    - short_id: User Short ID
    ### Return:
    - User information

    # [示例/Example]
    short_id = \"114131058\"

    Args:
        short_id (str): 用户Short ID/User Short ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            short_id=short_id,
        )
    ).parsed
