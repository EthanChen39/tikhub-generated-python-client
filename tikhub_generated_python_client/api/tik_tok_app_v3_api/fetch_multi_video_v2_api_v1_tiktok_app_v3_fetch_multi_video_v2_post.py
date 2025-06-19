from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: list[str],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tiktok/app/v3/fetch_multi_video_v2",
    }

    _kwargs["json"] = body

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
    body: list[str],
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""批量获取视频信息 V2/Batch Get Video Information V2

     # [中文]
    ### 用途:
    - 批量获取视频信息，支持图文、视频等，一次性最多支持10个视频，此接口收费固定价格为0.001$ * 10 = 0.01$一次。
    ### 参数:
    - aweme_ids: 作品id列表，最多支持10个作品id。
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Batch Get Video Information, support photo, video, etc., up to 10 videos at a time, this interface
    charges a fixed price of 0.001$ * 10 = 0.01$ each time.
    ### Parameters:
    - aweme_ids: List of video ids, up to 10 video ids are supported.
    ### Return:
    - Video data

    # [示例/Example]
    aweme_ids = [
            \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\",
    \"7339393672959757570\", \"7339393672959757570\",
            \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\",
    \"7339393672959757570\", \"7339393672959757570\",
        ]

    Args:
        body (list[str]): 作品id列表/Video id list

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
    body: list[str],
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""批量获取视频信息 V2/Batch Get Video Information V2

     # [中文]
    ### 用途:
    - 批量获取视频信息，支持图文、视频等，一次性最多支持10个视频，此接口收费固定价格为0.001$ * 10 = 0.01$一次。
    ### 参数:
    - aweme_ids: 作品id列表，最多支持10个作品id。
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Batch Get Video Information, support photo, video, etc., up to 10 videos at a time, this interface
    charges a fixed price of 0.001$ * 10 = 0.01$ each time.
    ### Parameters:
    - aweme_ids: List of video ids, up to 10 video ids are supported.
    ### Return:
    - Video data

    # [示例/Example]
    aweme_ids = [
            \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\",
    \"7339393672959757570\", \"7339393672959757570\",
            \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\",
    \"7339393672959757570\", \"7339393672959757570\",
        ]

    Args:
        body (list[str]): 作品id列表/Video id list

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
    body: list[str],
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""批量获取视频信息 V2/Batch Get Video Information V2

     # [中文]
    ### 用途:
    - 批量获取视频信息，支持图文、视频等，一次性最多支持10个视频，此接口收费固定价格为0.001$ * 10 = 0.01$一次。
    ### 参数:
    - aweme_ids: 作品id列表，最多支持10个作品id。
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Batch Get Video Information, support photo, video, etc., up to 10 videos at a time, this interface
    charges a fixed price of 0.001$ * 10 = 0.01$ each time.
    ### Parameters:
    - aweme_ids: List of video ids, up to 10 video ids are supported.
    ### Return:
    - Video data

    # [示例/Example]
    aweme_ids = [
            \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\",
    \"7339393672959757570\", \"7339393672959757570\",
            \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\",
    \"7339393672959757570\", \"7339393672959757570\",
        ]

    Args:
        body (list[str]): 作品id列表/Video id list

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
    body: list[str],
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""批量获取视频信息 V2/Batch Get Video Information V2

     # [中文]
    ### 用途:
    - 批量获取视频信息，支持图文、视频等，一次性最多支持10个视频，此接口收费固定价格为0.001$ * 10 = 0.01$一次。
    ### 参数:
    - aweme_ids: 作品id列表，最多支持10个作品id。
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Batch Get Video Information, support photo, video, etc., up to 10 videos at a time, this interface
    charges a fixed price of 0.001$ * 10 = 0.01$ each time.
    ### Parameters:
    - aweme_ids: List of video ids, up to 10 video ids are supported.
    ### Return:
    - Video data

    # [示例/Example]
    aweme_ids = [
            \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\",
    \"7339393672959757570\", \"7339393672959757570\",
            \"7339393672959757570\", \"7339393672959757570\", \"7339393672959757570\",
    \"7339393672959757570\", \"7339393672959757570\",
        ]

    Args:
        body (list[str]): 作品id列表/Video id list

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
