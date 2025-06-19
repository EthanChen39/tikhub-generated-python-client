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
    uid: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["uid"] = uid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/web/encrypt_uid_to_sec_user_id",
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
    uid: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""加密用户uid到sec_user_id/Encrypt user uid to sec_user_id

     # [中文]
    ### 用途:
    - 加密用户uid到sec_user_id
    ### 参数:
    - uid: 用户uid，也就是抖音号的short_id
    ### 返回:
    - 用户信息

    # [English]
    ### Purpose:
    - Encrypt user uid to sec_user_id
    ### Parameters:
    - uid: User uid, which is the short_id of the Douyin number
    ### Return:
    - User information

    # [示例/Example]
    uid = \"1673937488185292\"

    Args:
        uid (str): 用户uid(short_id)/User uid(short_id)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        uid=uid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    uid: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""加密用户uid到sec_user_id/Encrypt user uid to sec_user_id

     # [中文]
    ### 用途:
    - 加密用户uid到sec_user_id
    ### 参数:
    - uid: 用户uid，也就是抖音号的short_id
    ### 返回:
    - 用户信息

    # [English]
    ### Purpose:
    - Encrypt user uid to sec_user_id
    ### Parameters:
    - uid: User uid, which is the short_id of the Douyin number
    ### Return:
    - User information

    # [示例/Example]
    uid = \"1673937488185292\"

    Args:
        uid (str): 用户uid(short_id)/User uid(short_id)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        uid=uid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    uid: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""加密用户uid到sec_user_id/Encrypt user uid to sec_user_id

     # [中文]
    ### 用途:
    - 加密用户uid到sec_user_id
    ### 参数:
    - uid: 用户uid，也就是抖音号的short_id
    ### 返回:
    - 用户信息

    # [English]
    ### Purpose:
    - Encrypt user uid to sec_user_id
    ### Parameters:
    - uid: User uid, which is the short_id of the Douyin number
    ### Return:
    - User information

    # [示例/Example]
    uid = \"1673937488185292\"

    Args:
        uid (str): 用户uid(short_id)/User uid(short_id)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        uid=uid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    uid: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""加密用户uid到sec_user_id/Encrypt user uid to sec_user_id

     # [中文]
    ### 用途:
    - 加密用户uid到sec_user_id
    ### 参数:
    - uid: 用户uid，也就是抖音号的short_id
    ### 返回:
    - 用户信息

    # [English]
    ### Purpose:
    - Encrypt user uid to sec_user_id
    ### Parameters:
    - uid: User uid, which is the short_id of the Douyin number
    ### Return:
    - User information

    # [示例/Example]
    uid = \"1673937488185292\"

    Args:
        uid (str): 用户uid(short_id)/User uid(short_id)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            uid=uid,
        )
    ).parsed
