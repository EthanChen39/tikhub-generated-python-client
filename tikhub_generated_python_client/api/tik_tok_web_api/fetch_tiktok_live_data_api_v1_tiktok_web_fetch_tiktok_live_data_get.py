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
    live_room_url: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["live_room_url"] = live_room_url

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/web/fetch_tiktok_live_data",
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
    live_room_url: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""通过直播链接获取直播间信息/Get live room information via live link

     # [中文]
    ### 用途:
    - 通过直播链接获取直播间信息
    - 此接口可获取离线直播间信息
    ### 参数:
    - live_room_url: 直播间链接
    ### 返回:
    - 直播间信息

    # [English]
    ### Purpose:
    - Get live room information via live link
    - This interface can get offline live room information
    ### Parameters:
    - live_room_url: Live room link
    ### Return:
    - Live room information

    # [示例/Example]
    live_room_url = \"https://www.tiktok.com/@.caseoh_daily/live\"

    Args:
        live_room_url (str): 直播间链接/Live room link

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        live_room_url=live_room_url,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    live_room_url: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""通过直播链接获取直播间信息/Get live room information via live link

     # [中文]
    ### 用途:
    - 通过直播链接获取直播间信息
    - 此接口可获取离线直播间信息
    ### 参数:
    - live_room_url: 直播间链接
    ### 返回:
    - 直播间信息

    # [English]
    ### Purpose:
    - Get live room information via live link
    - This interface can get offline live room information
    ### Parameters:
    - live_room_url: Live room link
    ### Return:
    - Live room information

    # [示例/Example]
    live_room_url = \"https://www.tiktok.com/@.caseoh_daily/live\"

    Args:
        live_room_url (str): 直播间链接/Live room link

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        live_room_url=live_room_url,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    live_room_url: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""通过直播链接获取直播间信息/Get live room information via live link

     # [中文]
    ### 用途:
    - 通过直播链接获取直播间信息
    - 此接口可获取离线直播间信息
    ### 参数:
    - live_room_url: 直播间链接
    ### 返回:
    - 直播间信息

    # [English]
    ### Purpose:
    - Get live room information via live link
    - This interface can get offline live room information
    ### Parameters:
    - live_room_url: Live room link
    ### Return:
    - Live room information

    # [示例/Example]
    live_room_url = \"https://www.tiktok.com/@.caseoh_daily/live\"

    Args:
        live_room_url (str): 直播间链接/Live room link

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        live_room_url=live_room_url,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    live_room_url: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""通过直播链接获取直播间信息/Get live room information via live link

     # [中文]
    ### 用途:
    - 通过直播链接获取直播间信息
    - 此接口可获取离线直播间信息
    ### 参数:
    - live_room_url: 直播间链接
    ### 返回:
    - 直播间信息

    # [English]
    ### Purpose:
    - Get live room information via live link
    - This interface can get offline live room information
    ### Parameters:
    - live_room_url: Live room link
    ### Return:
    - Live room information

    # [示例/Example]
    live_room_url = \"https://www.tiktok.com/@.caseoh_daily/live\"

    Args:
        live_room_url (str): 直播间链接/Live room link

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            live_room_url=live_room_url,
        )
    ).parsed
