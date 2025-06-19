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
    room_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["room_id"] = room_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/web/fetch_user_live_videos_by_room_id_v2",
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
    room_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""通过room_id获取指定用户的直播流数据 V2/Gets the live stream data of the specified user by room_id V2

     # [中文]
    ### 用途:
    - 获取指定用户的直播流数据V2
    ### 参数:
    - room_id: 直播间room_id
    ### 返回:
    - 直播流数据

    # [English]
    ### Purpose:
    - Gets the live stream data of the specified user V2
    ### Parameters:
    - room_id: Room room_id
    ### Return:
    - Live stream data

    # [示例/Example]
    room_id = \"7462723839303093032\"

    Args:
        room_id (str): 直播间room_id/Room room_id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    room_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""通过room_id获取指定用户的直播流数据 V2/Gets the live stream data of the specified user by room_id V2

     # [中文]
    ### 用途:
    - 获取指定用户的直播流数据V2
    ### 参数:
    - room_id: 直播间room_id
    ### 返回:
    - 直播流数据

    # [English]
    ### Purpose:
    - Gets the live stream data of the specified user V2
    ### Parameters:
    - room_id: Room room_id
    ### Return:
    - Live stream data

    # [示例/Example]
    room_id = \"7462723839303093032\"

    Args:
        room_id (str): 直播间room_id/Room room_id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        room_id=room_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    room_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""通过room_id获取指定用户的直播流数据 V2/Gets the live stream data of the specified user by room_id V2

     # [中文]
    ### 用途:
    - 获取指定用户的直播流数据V2
    ### 参数:
    - room_id: 直播间room_id
    ### 返回:
    - 直播流数据

    # [English]
    ### Purpose:
    - Gets the live stream data of the specified user V2
    ### Parameters:
    - room_id: Room room_id
    ### Return:
    - Live stream data

    # [示例/Example]
    room_id = \"7462723839303093032\"

    Args:
        room_id (str): 直播间room_id/Room room_id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    room_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""通过room_id获取指定用户的直播流数据 V2/Gets the live stream data of the specified user by room_id V2

     # [中文]
    ### 用途:
    - 获取指定用户的直播流数据V2
    ### 参数:
    - room_id: 直播间room_id
    ### 返回:
    - 直播流数据

    # [English]
    ### Purpose:
    - Gets the live stream data of the specified user V2
    ### Parameters:
    - room_id: Room room_id
    ### Return:
    - Live stream data

    # [示例/Example]
    room_id = \"7462723839303093032\"

    Args:
        room_id (str): 直播间room_id/Room room_id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            room_id=room_id,
        )
    ).parsed
