from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...models.tik_tok_app_encrypt_request import TikTokAPPEncryptRequest
from ...types import Response


def _get_kwargs(
    *,
    body: TikTokAPPEncryptRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tiktok/app/v3/TTencrypt_algorithm",
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
    body: TikTokAPPEncryptRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """TikTok APP加密算法/TikTok APP encryption algorithm

     # [中文]
    ### 用途:
    - TikTok APP加密算法，用于生成请求头中的加密参数。
    - 生成的加密参数列表：
        - `x-ladon`
        - `x-khronos`
        - `x-argus`
        - `x-gorgon` （8404）

    ### 参数:
    - url: 需要加密的完整URL
    - data: 如果接口是POST请求，请填写POST请求的数据参与加密计算，GET请求时传入空字符串即可。
    - device_info: 设备信息，可选参数，如果不填写则使用默认设备信息，设备信息会修改传入的URL中的参数。

    ### 返回:
    - 加密参数列表

    # [English]
    ### Purpose:
    - TikTok APP encryption algorithm, used to generate encrypted parameters in the request header.
    - The generated encrypted parameter list:
        - `x-ladon`
        - `x-khronos`
        - `x-argus`
        - `x-gorgon` (8404)

    ### Parameters:
    - url: Full URL to be encrypted
    - data: If the interface is a POST request, please fill in the data of the POST request to
    participate in the encryption calculation. For GET requests, pass an empty string.
    - device_info: Device information, optional parameter, if not filled in, the default device
    information will be used, and the device information will modify the parameters in the URL passed
    in.

    ### Return:
    - Encrypted parameter list

    Args:
        body (TikTokAPPEncryptRequest):

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
    body: TikTokAPPEncryptRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """TikTok APP加密算法/TikTok APP encryption algorithm

     # [中文]
    ### 用途:
    - TikTok APP加密算法，用于生成请求头中的加密参数。
    - 生成的加密参数列表：
        - `x-ladon`
        - `x-khronos`
        - `x-argus`
        - `x-gorgon` （8404）

    ### 参数:
    - url: 需要加密的完整URL
    - data: 如果接口是POST请求，请填写POST请求的数据参与加密计算，GET请求时传入空字符串即可。
    - device_info: 设备信息，可选参数，如果不填写则使用默认设备信息，设备信息会修改传入的URL中的参数。

    ### 返回:
    - 加密参数列表

    # [English]
    ### Purpose:
    - TikTok APP encryption algorithm, used to generate encrypted parameters in the request header.
    - The generated encrypted parameter list:
        - `x-ladon`
        - `x-khronos`
        - `x-argus`
        - `x-gorgon` (8404)

    ### Parameters:
    - url: Full URL to be encrypted
    - data: If the interface is a POST request, please fill in the data of the POST request to
    participate in the encryption calculation. For GET requests, pass an empty string.
    - device_info: Device information, optional parameter, if not filled in, the default device
    information will be used, and the device information will modify the parameters in the URL passed
    in.

    ### Return:
    - Encrypted parameter list

    Args:
        body (TikTokAPPEncryptRequest):

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
    body: TikTokAPPEncryptRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """TikTok APP加密算法/TikTok APP encryption algorithm

     # [中文]
    ### 用途:
    - TikTok APP加密算法，用于生成请求头中的加密参数。
    - 生成的加密参数列表：
        - `x-ladon`
        - `x-khronos`
        - `x-argus`
        - `x-gorgon` （8404）

    ### 参数:
    - url: 需要加密的完整URL
    - data: 如果接口是POST请求，请填写POST请求的数据参与加密计算，GET请求时传入空字符串即可。
    - device_info: 设备信息，可选参数，如果不填写则使用默认设备信息，设备信息会修改传入的URL中的参数。

    ### 返回:
    - 加密参数列表

    # [English]
    ### Purpose:
    - TikTok APP encryption algorithm, used to generate encrypted parameters in the request header.
    - The generated encrypted parameter list:
        - `x-ladon`
        - `x-khronos`
        - `x-argus`
        - `x-gorgon` (8404)

    ### Parameters:
    - url: Full URL to be encrypted
    - data: If the interface is a POST request, please fill in the data of the POST request to
    participate in the encryption calculation. For GET requests, pass an empty string.
    - device_info: Device information, optional parameter, if not filled in, the default device
    information will be used, and the device information will modify the parameters in the URL passed
    in.

    ### Return:
    - Encrypted parameter list

    Args:
        body (TikTokAPPEncryptRequest):

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
    body: TikTokAPPEncryptRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """TikTok APP加密算法/TikTok APP encryption algorithm

     # [中文]
    ### 用途:
    - TikTok APP加密算法，用于生成请求头中的加密参数。
    - 生成的加密参数列表：
        - `x-ladon`
        - `x-khronos`
        - `x-argus`
        - `x-gorgon` （8404）

    ### 参数:
    - url: 需要加密的完整URL
    - data: 如果接口是POST请求，请填写POST请求的数据参与加密计算，GET请求时传入空字符串即可。
    - device_info: 设备信息，可选参数，如果不填写则使用默认设备信息，设备信息会修改传入的URL中的参数。

    ### 返回:
    - 加密参数列表

    # [English]
    ### Purpose:
    - TikTok APP encryption algorithm, used to generate encrypted parameters in the request header.
    - The generated encrypted parameter list:
        - `x-ladon`
        - `x-khronos`
        - `x-argus`
        - `x-gorgon` (8404)

    ### Parameters:
    - url: Full URL to be encrypted
    - data: If the interface is a POST request, please fill in the data of the POST request to
    participate in the encryption calculation. For GET requests, pass an empty string.
    - device_info: Device information, optional parameter, if not filled in, the default device
    information will be used, and the device information will modify the parameters in the URL passed
    in.

    ### Return:
    - Encrypted parameter list

    Args:
        body (TikTokAPPEncryptRequest):

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
