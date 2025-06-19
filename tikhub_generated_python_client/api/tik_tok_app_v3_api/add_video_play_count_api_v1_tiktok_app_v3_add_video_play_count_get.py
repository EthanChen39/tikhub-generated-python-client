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
    aweme_type: int,
    item_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["aweme_type"] = aweme_type

    params["item_id"] = item_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/app/v3/add_video_play_count",
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
    aweme_type: int,
    item_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID

     # [中文]
    ### 用途:
    - 根据视频ID来增加作品的播放数
    ### 参数:
    - aweme_type: 作品类型，0:视频 1:图文，可以从单一作品数据接口中获取。
    - item_id: 作品id，别名为aweme_id
    - invite_code: 邀请码，此接口需要邀请码才能使用。
    ### 返回:
    - 当前时间戳和状态码，状态码为200时表示成功，否则为失败，可以尝试更换一个作品id再次调用，或者等待一段时间后再次调用。

    # [English]
    ### Purpose:
    - Increase the number of plays of the work according to the video ID
    ### Parameters:
    - aweme_type: Video type, 0: Video 1: Graphic and text, can be obtained from the single work data
    interface.
    - item_id: Video id, alias aweme_id
    - invite_code: Invite code, this interface requires an invite code to use.
    ### Return:
    - The current timestamp and status code. When the status code is 200, it means success, otherwise it
    is a failure. You can try to change another work id and call it again, or wait for a period of time
    and call it again.

    # [示例/Example]
    aweme_type = 0
    item_id = \"7419966340443819295\"
    cookie = None

    Args:
        aweme_type (int): 作品类型/Video type
        item_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        aweme_type=aweme_type,
        item_id=item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    aweme_type: int,
    item_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID

     # [中文]
    ### 用途:
    - 根据视频ID来增加作品的播放数
    ### 参数:
    - aweme_type: 作品类型，0:视频 1:图文，可以从单一作品数据接口中获取。
    - item_id: 作品id，别名为aweme_id
    - invite_code: 邀请码，此接口需要邀请码才能使用。
    ### 返回:
    - 当前时间戳和状态码，状态码为200时表示成功，否则为失败，可以尝试更换一个作品id再次调用，或者等待一段时间后再次调用。

    # [English]
    ### Purpose:
    - Increase the number of plays of the work according to the video ID
    ### Parameters:
    - aweme_type: Video type, 0: Video 1: Graphic and text, can be obtained from the single work data
    interface.
    - item_id: Video id, alias aweme_id
    - invite_code: Invite code, this interface requires an invite code to use.
    ### Return:
    - The current timestamp and status code. When the status code is 200, it means success, otherwise it
    is a failure. You can try to change another work id and call it again, or wait for a period of time
    and call it again.

    # [示例/Example]
    aweme_type = 0
    item_id = \"7419966340443819295\"
    cookie = None

    Args:
        aweme_type (int): 作品类型/Video type
        item_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        aweme_type=aweme_type,
        item_id=item_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    aweme_type: int,
    item_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID

     # [中文]
    ### 用途:
    - 根据视频ID来增加作品的播放数
    ### 参数:
    - aweme_type: 作品类型，0:视频 1:图文，可以从单一作品数据接口中获取。
    - item_id: 作品id，别名为aweme_id
    - invite_code: 邀请码，此接口需要邀请码才能使用。
    ### 返回:
    - 当前时间戳和状态码，状态码为200时表示成功，否则为失败，可以尝试更换一个作品id再次调用，或者等待一段时间后再次调用。

    # [English]
    ### Purpose:
    - Increase the number of plays of the work according to the video ID
    ### Parameters:
    - aweme_type: Video type, 0: Video 1: Graphic and text, can be obtained from the single work data
    interface.
    - item_id: Video id, alias aweme_id
    - invite_code: Invite code, this interface requires an invite code to use.
    ### Return:
    - The current timestamp and status code. When the status code is 200, it means success, otherwise it
    is a failure. You can try to change another work id and call it again, or wait for a period of time
    and call it again.

    # [示例/Example]
    aweme_type = 0
    item_id = \"7419966340443819295\"
    cookie = None

    Args:
        aweme_type (int): 作品类型/Video type
        item_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        aweme_type=aweme_type,
        item_id=item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    aweme_type: int,
    item_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID

     # [中文]
    ### 用途:
    - 根据视频ID来增加作品的播放数
    ### 参数:
    - aweme_type: 作品类型，0:视频 1:图文，可以从单一作品数据接口中获取。
    - item_id: 作品id，别名为aweme_id
    - invite_code: 邀请码，此接口需要邀请码才能使用。
    ### 返回:
    - 当前时间戳和状态码，状态码为200时表示成功，否则为失败，可以尝试更换一个作品id再次调用，或者等待一段时间后再次调用。

    # [English]
    ### Purpose:
    - Increase the number of plays of the work according to the video ID
    ### Parameters:
    - aweme_type: Video type, 0: Video 1: Graphic and text, can be obtained from the single work data
    interface.
    - item_id: Video id, alias aweme_id
    - invite_code: Invite code, this interface requires an invite code to use.
    ### Return:
    - The current timestamp and status code. When the status code is 200, it means success, otherwise it
    is a failure. You can try to change another work id and call it again, or wait for a period of time
    and call it again.

    # [示例/Example]
    aweme_type = 0
    item_id = \"7419966340443819295\"
    cookie = None

    Args:
        aweme_type (int): 作品类型/Video type
        item_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            aweme_type=aweme_type,
            item_id=item_id,
        )
    ).parsed
