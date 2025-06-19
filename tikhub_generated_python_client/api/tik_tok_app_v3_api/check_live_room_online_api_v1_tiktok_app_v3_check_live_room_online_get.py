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
        "url": "/api/v1/tiktok/app/v3/check_live_room_online",
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
    r"""检测直播间是否在线/Check if live room is online

     # [中文]
    ### 用途:
    - 检测直播间是否在线
    - 直播间的Room ID可以通过直播间链接从`/api/v1/tiktok/web/get_live_room_id`接口获取
    ### 参数:
    - room_id: 直播间id
    ### 返回:
    - 是否在线

    # [English]
    ### Purpose:
    - Check if live room is online
    - The Room ID of the live room can be obtained from the `/api/v1/tiktok/web/get_live_room_id`
    interface through the live room link
    ### Parameters:
    - room_id: Live room id
    ### Return:
    - Whether online

    # [示例/Example]
    room_id = \"7358603858249009962\"

    Args:
        room_id (str): 直播间id/Live room id

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
    r"""检测直播间是否在线/Check if live room is online

     # [中文]
    ### 用途:
    - 检测直播间是否在线
    - 直播间的Room ID可以通过直播间链接从`/api/v1/tiktok/web/get_live_room_id`接口获取
    ### 参数:
    - room_id: 直播间id
    ### 返回:
    - 是否在线

    # [English]
    ### Purpose:
    - Check if live room is online
    - The Room ID of the live room can be obtained from the `/api/v1/tiktok/web/get_live_room_id`
    interface through the live room link
    ### Parameters:
    - room_id: Live room id
    ### Return:
    - Whether online

    # [示例/Example]
    room_id = \"7358603858249009962\"

    Args:
        room_id (str): 直播间id/Live room id

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
    r"""检测直播间是否在线/Check if live room is online

     # [中文]
    ### 用途:
    - 检测直播间是否在线
    - 直播间的Room ID可以通过直播间链接从`/api/v1/tiktok/web/get_live_room_id`接口获取
    ### 参数:
    - room_id: 直播间id
    ### 返回:
    - 是否在线

    # [English]
    ### Purpose:
    - Check if live room is online
    - The Room ID of the live room can be obtained from the `/api/v1/tiktok/web/get_live_room_id`
    interface through the live room link
    ### Parameters:
    - room_id: Live room id
    ### Return:
    - Whether online

    # [示例/Example]
    room_id = \"7358603858249009962\"

    Args:
        room_id (str): 直播间id/Live room id

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
    r"""检测直播间是否在线/Check if live room is online

     # [中文]
    ### 用途:
    - 检测直播间是否在线
    - 直播间的Room ID可以通过直播间链接从`/api/v1/tiktok/web/get_live_room_id`接口获取
    ### 参数:
    - room_id: 直播间id
    ### 返回:
    - 是否在线

    # [English]
    ### Purpose:
    - Check if live room is online
    - The Room ID of the live room can be obtained from the `/api/v1/tiktok/web/get_live_room_id`
    interface through the live room link
    ### Parameters:
    - room_id: Live room id
    ### Return:
    - Whether online

    # [示例/Example]
    room_id = \"7358603858249009962\"

    Args:
        room_id (str): 直播间id/Live room id

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
