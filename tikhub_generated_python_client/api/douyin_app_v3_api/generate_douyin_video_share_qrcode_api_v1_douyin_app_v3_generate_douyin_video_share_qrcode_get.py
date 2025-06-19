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
    object_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["object_id"] = object_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/app/v3/generate_douyin_video_share_qrcode",
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
    object_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""生成抖音视频分享二维码/Generate Douyin video share QR code

     # [中文]
    ### 用途:
    - 生成抖音视频分享二维码
    ### 参数:
    - object_id: 作品id或作者uid
    ### 返回:
    - 二维码数据

    # [English]
    ### Purpose:
    - Generate Douyin video share QR code
    ### Parameters:
    - object_id: Video id or author uid
    ### Return:
    - QR code data

    # [示例/Example]
    object_id = \"7348044435755846962\"

    Args:
        object_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    object_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""生成抖音视频分享二维码/Generate Douyin video share QR code

     # [中文]
    ### 用途:
    - 生成抖音视频分享二维码
    ### 参数:
    - object_id: 作品id或作者uid
    ### 返回:
    - 二维码数据

    # [English]
    ### Purpose:
    - Generate Douyin video share QR code
    ### Parameters:
    - object_id: Video id or author uid
    ### Return:
    - QR code data

    # [示例/Example]
    object_id = \"7348044435755846962\"

    Args:
        object_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        object_id=object_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    object_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""生成抖音视频分享二维码/Generate Douyin video share QR code

     # [中文]
    ### 用途:
    - 生成抖音视频分享二维码
    ### 参数:
    - object_id: 作品id或作者uid
    ### 返回:
    - 二维码数据

    # [English]
    ### Purpose:
    - Generate Douyin video share QR code
    ### Parameters:
    - object_id: Video id or author uid
    ### Return:
    - QR code data

    # [示例/Example]
    object_id = \"7348044435755846962\"

    Args:
        object_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    object_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""生成抖音视频分享二维码/Generate Douyin video share QR code

     # [中文]
    ### 用途:
    - 生成抖音视频分享二维码
    ### 参数:
    - object_id: 作品id或作者uid
    ### 返回:
    - 二维码数据

    # [English]
    ### Purpose:
    - Generate Douyin video share QR code
    ### Parameters:
    - object_id: Video id or author uid
    ### Return:
    - QR code data

    # [示例/Example]
    object_id = \"7348044435755846962\"

    Args:
        object_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            object_id=object_id,
        )
    ).parsed
