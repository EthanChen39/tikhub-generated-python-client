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
    sec_uid: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["sec_uid"] = sec_uid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/web/fetch_user_live_videos_by_sec_uid",
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
    sec_uid: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""通过sec_uid获取指定用户的直播流数据/Get live video data of specified user by sec_uid

     # [中文]
    ### 用途:
    - 通过sec_uid获取指定用户的直播流数据
    ### 参数:
    - sec_uid: 用户sec_uid，也叫 sec_user_id，可以在用户主页链接中找到。
    ### 返回:
    - 直播流数据

    # [English]
    ### Purpose
    - Get live video data of specified user by sec_uid
    ### Parameters
    - sec_uid: User sec_uid, also called sec_user_id, can be found in the user's homepage link.
    ### Return
    - Live stream data

    # [示例/Example]
    sec_uid = \"MS4wLjABAAAAAIKOBr_x6p2fPVKOAhqG8LrC1lwwdWChifKEsl-TXFS-kGSGqpMBRexJdzoAfvUF\"

    Args:
        sec_uid (str): 用户sec_uid/User sec_uid

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        sec_uid=sec_uid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    sec_uid: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""通过sec_uid获取指定用户的直播流数据/Get live video data of specified user by sec_uid

     # [中文]
    ### 用途:
    - 通过sec_uid获取指定用户的直播流数据
    ### 参数:
    - sec_uid: 用户sec_uid，也叫 sec_user_id，可以在用户主页链接中找到。
    ### 返回:
    - 直播流数据

    # [English]
    ### Purpose
    - Get live video data of specified user by sec_uid
    ### Parameters
    - sec_uid: User sec_uid, also called sec_user_id, can be found in the user's homepage link.
    ### Return
    - Live stream data

    # [示例/Example]
    sec_uid = \"MS4wLjABAAAAAIKOBr_x6p2fPVKOAhqG8LrC1lwwdWChifKEsl-TXFS-kGSGqpMBRexJdzoAfvUF\"

    Args:
        sec_uid (str): 用户sec_uid/User sec_uid

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        sec_uid=sec_uid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    sec_uid: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""通过sec_uid获取指定用户的直播流数据/Get live video data of specified user by sec_uid

     # [中文]
    ### 用途:
    - 通过sec_uid获取指定用户的直播流数据
    ### 参数:
    - sec_uid: 用户sec_uid，也叫 sec_user_id，可以在用户主页链接中找到。
    ### 返回:
    - 直播流数据

    # [English]
    ### Purpose
    - Get live video data of specified user by sec_uid
    ### Parameters
    - sec_uid: User sec_uid, also called sec_user_id, can be found in the user's homepage link.
    ### Return
    - Live stream data

    # [示例/Example]
    sec_uid = \"MS4wLjABAAAAAIKOBr_x6p2fPVKOAhqG8LrC1lwwdWChifKEsl-TXFS-kGSGqpMBRexJdzoAfvUF\"

    Args:
        sec_uid (str): 用户sec_uid/User sec_uid

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        sec_uid=sec_uid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    sec_uid: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""通过sec_uid获取指定用户的直播流数据/Get live video data of specified user by sec_uid

     # [中文]
    ### 用途:
    - 通过sec_uid获取指定用户的直播流数据
    ### 参数:
    - sec_uid: 用户sec_uid，也叫 sec_user_id，可以在用户主页链接中找到。
    ### 返回:
    - 直播流数据

    # [English]
    ### Purpose
    - Get live video data of specified user by sec_uid
    ### Parameters
    - sec_uid: User sec_uid, also called sec_user_id, can be found in the user's homepage link.
    ### Return
    - Live stream data

    # [示例/Example]
    sec_uid = \"MS4wLjABAAAAAIKOBr_x6p2fPVKOAhqG8LrC1lwwdWChifKEsl-TXFS-kGSGqpMBRexJdzoAfvUF\"

    Args:
        sec_uid (str): 用户sec_uid/User sec_uid

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            sec_uid=sec_uid,
        )
    ).parsed
