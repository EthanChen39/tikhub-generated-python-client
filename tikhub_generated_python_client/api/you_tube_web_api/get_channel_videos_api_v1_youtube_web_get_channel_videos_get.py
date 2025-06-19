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
    channel_id: str,
    continuation_token: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["channel_id"] = channel_id

    params["continuation_token"] = continuation_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/youtube/web/get_channel_videos",
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
    channel_id: str,
    continuation_token: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取频道视频 V1（即将过时，优先使用 V2）/Get channel videos V1 (deprecated soon, use V2 first)

     # [中文]
    ### 用途:
    - 获取频道视频。
    ### 参数:
    - channel_id: 频道ID。
    - continuation_token: 用于继续获取频道视频的令牌。默认为None。
    ### 返回:
    - 频道视频。

    # [English]
    ### Purpose:
    - Get channel videos.
    ### Parameters:
    - channel_id: Channel ID.
    - continuation_token: Token to continue fetching channel videos. Default is None.
    ### Returns:
    - Channel videos.

    # [示例/Example]
    channel_id = \"UCXuqSBlHAE6Xw-yeJA0Tunw\"

    Args:
        channel_id (str): 频道ID/Channel ID
        continuation_token (Union[Unset, str]): 翻页令牌/Pagination token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        continuation_token=continuation_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    channel_id: str,
    continuation_token: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取频道视频 V1（即将过时，优先使用 V2）/Get channel videos V1 (deprecated soon, use V2 first)

     # [中文]
    ### 用途:
    - 获取频道视频。
    ### 参数:
    - channel_id: 频道ID。
    - continuation_token: 用于继续获取频道视频的令牌。默认为None。
    ### 返回:
    - 频道视频。

    # [English]
    ### Purpose:
    - Get channel videos.
    ### Parameters:
    - channel_id: Channel ID.
    - continuation_token: Token to continue fetching channel videos. Default is None.
    ### Returns:
    - Channel videos.

    # [示例/Example]
    channel_id = \"UCXuqSBlHAE6Xw-yeJA0Tunw\"

    Args:
        channel_id (str): 频道ID/Channel ID
        continuation_token (Union[Unset, str]): 翻页令牌/Pagination token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        channel_id=channel_id,
        continuation_token=continuation_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    channel_id: str,
    continuation_token: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取频道视频 V1（即将过时，优先使用 V2）/Get channel videos V1 (deprecated soon, use V2 first)

     # [中文]
    ### 用途:
    - 获取频道视频。
    ### 参数:
    - channel_id: 频道ID。
    - continuation_token: 用于继续获取频道视频的令牌。默认为None。
    ### 返回:
    - 频道视频。

    # [English]
    ### Purpose:
    - Get channel videos.
    ### Parameters:
    - channel_id: Channel ID.
    - continuation_token: Token to continue fetching channel videos. Default is None.
    ### Returns:
    - Channel videos.

    # [示例/Example]
    channel_id = \"UCXuqSBlHAE6Xw-yeJA0Tunw\"

    Args:
        channel_id (str): 频道ID/Channel ID
        continuation_token (Union[Unset, str]): 翻页令牌/Pagination token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        continuation_token=continuation_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    channel_id: str,
    continuation_token: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取频道视频 V1（即将过时，优先使用 V2）/Get channel videos V1 (deprecated soon, use V2 first)

     # [中文]
    ### 用途:
    - 获取频道视频。
    ### 参数:
    - channel_id: 频道ID。
    - continuation_token: 用于继续获取频道视频的令牌。默认为None。
    ### 返回:
    - 频道视频。

    # [English]
    ### Purpose:
    - Get channel videos.
    ### Parameters:
    - channel_id: Channel ID.
    - continuation_token: Token to continue fetching channel videos. Default is None.
    ### Returns:
    - Channel videos.

    # [示例/Example]
    channel_id = \"UCXuqSBlHAE6Xw-yeJA0Tunw\"

    Args:
        channel_id (str): 频道ID/Channel ID
        continuation_token (Union[Unset, str]): 翻页令牌/Pagination token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            channel_id=channel_id,
            continuation_token=continuation_token,
        )
    ).parsed
