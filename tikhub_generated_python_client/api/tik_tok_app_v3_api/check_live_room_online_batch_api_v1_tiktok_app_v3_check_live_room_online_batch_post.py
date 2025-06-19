from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.live_room_batch_check_request import LiveRoomBatchCheckRequest
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: LiveRoomBatchCheckRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tiktok/app/v3/check_live_room_online_batch",
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
    body: LiveRoomBatchCheckRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""批量检测直播间是否在线/Batch check if live rooms are online

     # [中文]
    ### 用途:
    - 批量检测多个 TikTok 直播间是否在线，最大支持50个直播间ID
    - Room ID 可以通过 `/api/v1/tiktok/web/get_live_room_id` 获取
    ### 参数:
    - room_ids: 多个直播间 ID 的数组
    ### 返回:
    - 每个直播间的在线状态

    # [English]
    ### Purpose:
    - Batch check TikTok live rooms' online status, supports up to 50 room IDs
    - Room IDs can be retrieved from `/api/v1/tiktok/web/get_live_room_id`
    ### Parameters:
    - room_ids: List of TikTok live room IDs
    ### Return:
    - Online status per room

    # [示例/Example]
    ```
    payload = {
        \"room_ids\": [
            \"7494491933781003054\",
            \"7494514925034113835\"
        ]
    }
    ```

    Args:
        body (LiveRoomBatchCheckRequest):

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
    body: LiveRoomBatchCheckRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""批量检测直播间是否在线/Batch check if live rooms are online

     # [中文]
    ### 用途:
    - 批量检测多个 TikTok 直播间是否在线，最大支持50个直播间ID
    - Room ID 可以通过 `/api/v1/tiktok/web/get_live_room_id` 获取
    ### 参数:
    - room_ids: 多个直播间 ID 的数组
    ### 返回:
    - 每个直播间的在线状态

    # [English]
    ### Purpose:
    - Batch check TikTok live rooms' online status, supports up to 50 room IDs
    - Room IDs can be retrieved from `/api/v1/tiktok/web/get_live_room_id`
    ### Parameters:
    - room_ids: List of TikTok live room IDs
    ### Return:
    - Online status per room

    # [示例/Example]
    ```
    payload = {
        \"room_ids\": [
            \"7494491933781003054\",
            \"7494514925034113835\"
        ]
    }
    ```

    Args:
        body (LiveRoomBatchCheckRequest):

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
    body: LiveRoomBatchCheckRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""批量检测直播间是否在线/Batch check if live rooms are online

     # [中文]
    ### 用途:
    - 批量检测多个 TikTok 直播间是否在线，最大支持50个直播间ID
    - Room ID 可以通过 `/api/v1/tiktok/web/get_live_room_id` 获取
    ### 参数:
    - room_ids: 多个直播间 ID 的数组
    ### 返回:
    - 每个直播间的在线状态

    # [English]
    ### Purpose:
    - Batch check TikTok live rooms' online status, supports up to 50 room IDs
    - Room IDs can be retrieved from `/api/v1/tiktok/web/get_live_room_id`
    ### Parameters:
    - room_ids: List of TikTok live room IDs
    ### Return:
    - Online status per room

    # [示例/Example]
    ```
    payload = {
        \"room_ids\": [
            \"7494491933781003054\",
            \"7494514925034113835\"
        ]
    }
    ```

    Args:
        body (LiveRoomBatchCheckRequest):

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
    body: LiveRoomBatchCheckRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""批量检测直播间是否在线/Batch check if live rooms are online

     # [中文]
    ### 用途:
    - 批量检测多个 TikTok 直播间是否在线，最大支持50个直播间ID
    - Room ID 可以通过 `/api/v1/tiktok/web/get_live_room_id` 获取
    ### 参数:
    - room_ids: 多个直播间 ID 的数组
    ### 返回:
    - 每个直播间的在线状态

    # [English]
    ### Purpose:
    - Batch check TikTok live rooms' online status, supports up to 50 room IDs
    - Room IDs can be retrieved from `/api/v1/tiktok/web/get_live_room_id`
    ### Parameters:
    - room_ids: List of TikTok live room IDs
    ### Return:
    - Online status per room

    # [示例/Example]
    ```
    payload = {
        \"room_ids\": [
            \"7494491933781003054\",
            \"7494514925034113835\"
        ]
    }
    ```

    Args:
        body (LiveRoomBatchCheckRequest):

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
