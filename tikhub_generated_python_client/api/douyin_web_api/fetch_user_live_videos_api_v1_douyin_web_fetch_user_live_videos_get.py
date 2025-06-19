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
    webcast_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["webcast_id"] = webcast_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/web/fetch_user_live_videos",
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
    webcast_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户直播流数据/Get user live video data

     # [中文]
    ### 用途:
    - 获取用户直播流数据
    ### 参数:
    - webcast_id: 直播间 webcast_id
    - 获取方法：
        - 假设你的直播间链接为：https://www.douyin.com/root/live/376034101029
        - 那么直播间webcast_id为：376034101029
        - webcast_id为直播间链接的最后一段数字，与room_id不同。
    ### 返回:
    - 直播流数据

    # [English]
    ### Purpose:
    - Get user live video data
    ### Parameters:
    - webcast_id: Room webcast_id
    - Acquisition method:
        - Assuming your live room link is: https://www.douyin.com/root/live/376034101029
        - Then the live room webcast_id is: 376034101029
        - The webcast_id is the last number of the live room link, which is different from the room_id.
    ### Return:
    - Live stream data

    # [示例/Example]
    webcast_id = \"376034101029\"

    Args:
        webcast_id (str): 直播间webcast_id/Room webcast_id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        webcast_id=webcast_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    webcast_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户直播流数据/Get user live video data

     # [中文]
    ### 用途:
    - 获取用户直播流数据
    ### 参数:
    - webcast_id: 直播间 webcast_id
    - 获取方法：
        - 假设你的直播间链接为：https://www.douyin.com/root/live/376034101029
        - 那么直播间webcast_id为：376034101029
        - webcast_id为直播间链接的最后一段数字，与room_id不同。
    ### 返回:
    - 直播流数据

    # [English]
    ### Purpose:
    - Get user live video data
    ### Parameters:
    - webcast_id: Room webcast_id
    - Acquisition method:
        - Assuming your live room link is: https://www.douyin.com/root/live/376034101029
        - Then the live room webcast_id is: 376034101029
        - The webcast_id is the last number of the live room link, which is different from the room_id.
    ### Return:
    - Live stream data

    # [示例/Example]
    webcast_id = \"376034101029\"

    Args:
        webcast_id (str): 直播间webcast_id/Room webcast_id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        webcast_id=webcast_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    webcast_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户直播流数据/Get user live video data

     # [中文]
    ### 用途:
    - 获取用户直播流数据
    ### 参数:
    - webcast_id: 直播间 webcast_id
    - 获取方法：
        - 假设你的直播间链接为：https://www.douyin.com/root/live/376034101029
        - 那么直播间webcast_id为：376034101029
        - webcast_id为直播间链接的最后一段数字，与room_id不同。
    ### 返回:
    - 直播流数据

    # [English]
    ### Purpose:
    - Get user live video data
    ### Parameters:
    - webcast_id: Room webcast_id
    - Acquisition method:
        - Assuming your live room link is: https://www.douyin.com/root/live/376034101029
        - Then the live room webcast_id is: 376034101029
        - The webcast_id is the last number of the live room link, which is different from the room_id.
    ### Return:
    - Live stream data

    # [示例/Example]
    webcast_id = \"376034101029\"

    Args:
        webcast_id (str): 直播间webcast_id/Room webcast_id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        webcast_id=webcast_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    webcast_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户直播流数据/Get user live video data

     # [中文]
    ### 用途:
    - 获取用户直播流数据
    ### 参数:
    - webcast_id: 直播间 webcast_id
    - 获取方法：
        - 假设你的直播间链接为：https://www.douyin.com/root/live/376034101029
        - 那么直播间webcast_id为：376034101029
        - webcast_id为直播间链接的最后一段数字，与room_id不同。
    ### 返回:
    - 直播流数据

    # [English]
    ### Purpose:
    - Get user live video data
    ### Parameters:
    - webcast_id: Room webcast_id
    - Acquisition method:
        - Assuming your live room link is: https://www.douyin.com/root/live/376034101029
        - Then the live room webcast_id is: 376034101029
        - The webcast_id is the last number of the live room link, which is different from the room_id.
    ### Return:
    - Live stream data

    # [示例/Example]
    webcast_id = \"376034101029\"

    Args:
        webcast_id (str): 直播间webcast_id/Room webcast_id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            webcast_id=webcast_id,
        )
    ).parsed
