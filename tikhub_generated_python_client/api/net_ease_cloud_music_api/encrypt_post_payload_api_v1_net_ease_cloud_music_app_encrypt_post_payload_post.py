from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.encrypt_post_payload_api_v1_net_ease_cloud_music_app_encrypt_post_payload_post_payload import (
    EncryptPostPayloadApiV1NetEaseCloudMusicAppEncryptPostPayloadPostPayload,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: EncryptPostPayloadApiV1NetEaseCloudMusicAppEncryptPostPayloadPostPayload,
    uri: str,
    add_variable: Union[Unset, bool] = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["uri"] = uri

    params["add_variable"] = add_variable

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/net_ease_cloud_music/app/encrypt_post_payload",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: EncryptPostPayloadApiV1NetEaseCloudMusicAppEncryptPostPayloadPostPayload,
    uri: str,
    add_variable: Union[Unset, bool] = False,
) -> Response[Union[Any, HTTPValidationError]]:
    r"""加密POST请求中的payload并且返回16进制/Encrypt the payload in the POST request and return 16 hexadecimal

     # [中文]
    ### 用途:
    - 加密POST请求中的payload并且返回16进制。
    ### 参数:
    - payload: 需要加密的payload。
    ### 返回:
    - 加密后的16进制payload

    # [English]
    ### Purpose:
    - Encrypt the payload in the POST request and return 16 hexadecimal.
    ### Parameters:
    - payload: Payload to be encrypted.
    ### Returns:
    - Encrypted 16 hexadecimal payload

    # [示例/Example]
    payload = {\"id\": 2135155051, \"br\": 192000}

    Args:
        uri (str): 请求URI/Request URI
        add_variable (Union[Unset, bool]): 是否添加变量/Whether to add variables Default: False.
        body (EncryptPostPayloadApiV1NetEaseCloudMusicAppEncryptPostPayloadPostPayload):
            需要加密的payload/Need to be encrypted payload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
        uri=uri,
        add_variable=add_variable,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: EncryptPostPayloadApiV1NetEaseCloudMusicAppEncryptPostPayloadPostPayload,
    uri: str,
    add_variable: Union[Unset, bool] = False,
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""加密POST请求中的payload并且返回16进制/Encrypt the payload in the POST request and return 16 hexadecimal

     # [中文]
    ### 用途:
    - 加密POST请求中的payload并且返回16进制。
    ### 参数:
    - payload: 需要加密的payload。
    ### 返回:
    - 加密后的16进制payload

    # [English]
    ### Purpose:
    - Encrypt the payload in the POST request and return 16 hexadecimal.
    ### Parameters:
    - payload: Payload to be encrypted.
    ### Returns:
    - Encrypted 16 hexadecimal payload

    # [示例/Example]
    payload = {\"id\": 2135155051, \"br\": 192000}

    Args:
        uri (str): 请求URI/Request URI
        add_variable (Union[Unset, bool]): 是否添加变量/Whether to add variables Default: False.
        body (EncryptPostPayloadApiV1NetEaseCloudMusicAppEncryptPostPayloadPostPayload):
            需要加密的payload/Need to be encrypted payload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        body=body,
        uri=uri,
        add_variable=add_variable,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: EncryptPostPayloadApiV1NetEaseCloudMusicAppEncryptPostPayloadPostPayload,
    uri: str,
    add_variable: Union[Unset, bool] = False,
) -> Response[Union[Any, HTTPValidationError]]:
    r"""加密POST请求中的payload并且返回16进制/Encrypt the payload in the POST request and return 16 hexadecimal

     # [中文]
    ### 用途:
    - 加密POST请求中的payload并且返回16进制。
    ### 参数:
    - payload: 需要加密的payload。
    ### 返回:
    - 加密后的16进制payload

    # [English]
    ### Purpose:
    - Encrypt the payload in the POST request and return 16 hexadecimal.
    ### Parameters:
    - payload: Payload to be encrypted.
    ### Returns:
    - Encrypted 16 hexadecimal payload

    # [示例/Example]
    payload = {\"id\": 2135155051, \"br\": 192000}

    Args:
        uri (str): 请求URI/Request URI
        add_variable (Union[Unset, bool]): 是否添加变量/Whether to add variables Default: False.
        body (EncryptPostPayloadApiV1NetEaseCloudMusicAppEncryptPostPayloadPostPayload):
            需要加密的payload/Need to be encrypted payload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
        uri=uri,
        add_variable=add_variable,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: EncryptPostPayloadApiV1NetEaseCloudMusicAppEncryptPostPayloadPostPayload,
    uri: str,
    add_variable: Union[Unset, bool] = False,
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""加密POST请求中的payload并且返回16进制/Encrypt the payload in the POST request and return 16 hexadecimal

     # [中文]
    ### 用途:
    - 加密POST请求中的payload并且返回16进制。
    ### 参数:
    - payload: 需要加密的payload。
    ### 返回:
    - 加密后的16进制payload

    # [English]
    ### Purpose:
    - Encrypt the payload in the POST request and return 16 hexadecimal.
    ### Parameters:
    - payload: Payload to be encrypted.
    ### Returns:
    - Encrypted 16 hexadecimal payload

    # [示例/Example]
    payload = {\"id\": 2135155051, \"br\": 192000}

    Args:
        uri (str): 请求URI/Request URI
        add_variable (Union[Unset, bool]): 是否添加变量/Whether to add variables Default: False.
        body (EncryptPostPayloadApiV1NetEaseCloudMusicAppEncryptPostPayloadPostPayload):
            需要加密的payload/Need to be encrypted payload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            uri=uri,
            add_variable=add_variable,
        )
    ).parsed
