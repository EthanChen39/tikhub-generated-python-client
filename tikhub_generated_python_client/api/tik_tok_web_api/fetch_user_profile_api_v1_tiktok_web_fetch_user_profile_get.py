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
    unique_id: Union[Unset, str] = "",
    sec_uid: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["uniqueId"] = unique_id

    params["secUid"] = sec_uid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/web/fetch_user_profile",
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
    unique_id: Union[Unset, str] = "",
    sec_uid: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户的个人信息/Get user profile

     # [中文]
    ### 用途:
    - 获取用户的个人信息
    ### 参数:
    - secUid: 用户secUid
    - uniqueId: 用户uniqueId
    - secUid和uniqueId至少提供一个, 优先使用uniqueId, 也就是用户主页的链接中的用户名。
    ### 返回:
    - 用户的个人信息

    # [English]
    ### Purpose:
    - Get user profile
    ### Parameters:
    - secUid: User secUid
    - uniqueId: User uniqueId
    - At least one of secUid and uniqueId is provided, and uniqueId is preferred, that is, the username
    in the user's homepage link.
    ### Return:
    - User profile

    # [示例/Example]
    secUid = \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\"
    uniqueId = \"tiktok\"

    Args:
        unique_id (Union[Unset, str]): 用户uniqueId/User uniqueId Default: ''.
        sec_uid (Union[Unset, str]): 用户secUid/User secUid Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        unique_id=unique_id,
        sec_uid=sec_uid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    unique_id: Union[Unset, str] = "",
    sec_uid: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户的个人信息/Get user profile

     # [中文]
    ### 用途:
    - 获取用户的个人信息
    ### 参数:
    - secUid: 用户secUid
    - uniqueId: 用户uniqueId
    - secUid和uniqueId至少提供一个, 优先使用uniqueId, 也就是用户主页的链接中的用户名。
    ### 返回:
    - 用户的个人信息

    # [English]
    ### Purpose:
    - Get user profile
    ### Parameters:
    - secUid: User secUid
    - uniqueId: User uniqueId
    - At least one of secUid and uniqueId is provided, and uniqueId is preferred, that is, the username
    in the user's homepage link.
    ### Return:
    - User profile

    # [示例/Example]
    secUid = \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\"
    uniqueId = \"tiktok\"

    Args:
        unique_id (Union[Unset, str]): 用户uniqueId/User uniqueId Default: ''.
        sec_uid (Union[Unset, str]): 用户secUid/User secUid Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        unique_id=unique_id,
        sec_uid=sec_uid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    unique_id: Union[Unset, str] = "",
    sec_uid: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户的个人信息/Get user profile

     # [中文]
    ### 用途:
    - 获取用户的个人信息
    ### 参数:
    - secUid: 用户secUid
    - uniqueId: 用户uniqueId
    - secUid和uniqueId至少提供一个, 优先使用uniqueId, 也就是用户主页的链接中的用户名。
    ### 返回:
    - 用户的个人信息

    # [English]
    ### Purpose:
    - Get user profile
    ### Parameters:
    - secUid: User secUid
    - uniqueId: User uniqueId
    - At least one of secUid and uniqueId is provided, and uniqueId is preferred, that is, the username
    in the user's homepage link.
    ### Return:
    - User profile

    # [示例/Example]
    secUid = \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\"
    uniqueId = \"tiktok\"

    Args:
        unique_id (Union[Unset, str]): 用户uniqueId/User uniqueId Default: ''.
        sec_uid (Union[Unset, str]): 用户secUid/User secUid Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        unique_id=unique_id,
        sec_uid=sec_uid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    unique_id: Union[Unset, str] = "",
    sec_uid: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户的个人信息/Get user profile

     # [中文]
    ### 用途:
    - 获取用户的个人信息
    ### 参数:
    - secUid: 用户secUid
    - uniqueId: 用户uniqueId
    - secUid和uniqueId至少提供一个, 优先使用uniqueId, 也就是用户主页的链接中的用户名。
    ### 返回:
    - 用户的个人信息

    # [English]
    ### Purpose:
    - Get user profile
    ### Parameters:
    - secUid: User secUid
    - uniqueId: User uniqueId
    - At least one of secUid and uniqueId is provided, and uniqueId is preferred, that is, the username
    in the user's homepage link.
    ### Return:
    - User profile

    # [示例/Example]
    secUid = \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\"
    uniqueId = \"tiktok\"

    Args:
        unique_id (Union[Unset, str]): 用户uniqueId/User uniqueId Default: ''.
        sec_uid (Union[Unset, str]): 用户secUid/User secUid Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            unique_id=unique_id,
            sec_uid=sec_uid,
        )
    ).parsed
