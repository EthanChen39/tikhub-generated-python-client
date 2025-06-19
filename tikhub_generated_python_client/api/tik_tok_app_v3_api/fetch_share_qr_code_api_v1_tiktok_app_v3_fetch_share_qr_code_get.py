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
    object_id: str,
    schema_type: Union[Unset, int] = 4,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["object_id"] = object_id

    params["schema_type"] = schema_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/app/v3/fetch_share_qr_code",
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
    schema_type: Union[Unset, int] = 4,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取分享二维码/Get share QR code

     # [中文]
    ### 用途:
    - 获取分享二维码
    ### 参数:
    - object_id: 对象id，当前支持个人主页接口响应中的uid作为参数。
    ### 返回:
    - 二维码图片

    # [English]
    ### Purpose:
    - Get share QR code
    ### Parameters:
    - object_id: Object id, currently supports the uid in the response of the personal homepage
    interface as a parameter.
    ### Return:
    - QR code image

    # [示例/Example]
    url = \"6762244951259661318\"

    Args:
        object_id (str): 对象id/Object id
        schema_type (Union[Unset, int]): 模式类型/Schema type Default: 4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
        schema_type=schema_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    object_id: str,
    schema_type: Union[Unset, int] = 4,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取分享二维码/Get share QR code

     # [中文]
    ### 用途:
    - 获取分享二维码
    ### 参数:
    - object_id: 对象id，当前支持个人主页接口响应中的uid作为参数。
    ### 返回:
    - 二维码图片

    # [English]
    ### Purpose:
    - Get share QR code
    ### Parameters:
    - object_id: Object id, currently supports the uid in the response of the personal homepage
    interface as a parameter.
    ### Return:
    - QR code image

    # [示例/Example]
    url = \"6762244951259661318\"

    Args:
        object_id (str): 对象id/Object id
        schema_type (Union[Unset, int]): 模式类型/Schema type Default: 4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        object_id=object_id,
        schema_type=schema_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    object_id: str,
    schema_type: Union[Unset, int] = 4,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取分享二维码/Get share QR code

     # [中文]
    ### 用途:
    - 获取分享二维码
    ### 参数:
    - object_id: 对象id，当前支持个人主页接口响应中的uid作为参数。
    ### 返回:
    - 二维码图片

    # [English]
    ### Purpose:
    - Get share QR code
    ### Parameters:
    - object_id: Object id, currently supports the uid in the response of the personal homepage
    interface as a parameter.
    ### Return:
    - QR code image

    # [示例/Example]
    url = \"6762244951259661318\"

    Args:
        object_id (str): 对象id/Object id
        schema_type (Union[Unset, int]): 模式类型/Schema type Default: 4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
        schema_type=schema_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    object_id: str,
    schema_type: Union[Unset, int] = 4,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取分享二维码/Get share QR code

     # [中文]
    ### 用途:
    - 获取分享二维码
    ### 参数:
    - object_id: 对象id，当前支持个人主页接口响应中的uid作为参数。
    ### 返回:
    - 二维码图片

    # [English]
    ### Purpose:
    - Get share QR code
    ### Parameters:
    - object_id: Object id, currently supports the uid in the response of the personal homepage
    interface as a parameter.
    ### Return:
    - QR code image

    # [示例/Example]
    url = \"6762244951259661318\"

    Args:
        object_id (str): 对象id/Object id
        schema_type (Union[Unset, int]): 模式类型/Schema type Default: 4.

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
            schema_type=schema_type,
        )
    ).parsed
