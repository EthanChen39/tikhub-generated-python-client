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
    device_id: str,
    region: str,
    proxy: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["device_id"] = device_id

    params["region"] = region

    params["proxy"] = proxy

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/web/fetch_sso_login_qrcode",
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
    device_id: str,
    region: str,
    proxy: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取SSO登录二维码/Get SSO login QR code

     # [中文]
    ### 用途:
    - 获取SSO登录二维码
    ### 参数:
    - device_id: 设备ID
    - region: 地区
    - proxy: 代理
    ### 返回:
    - SSO登录二维码
    ### 说明:
    - 该接口返回的二维码需要使用手机扫描登录，登录成功后会返回登录信息。
    - 不传入设备ID将由后端自动生成设备ID。
    - 如果需要使用代理，请传入代理地址，否则传入None。
    - 单次二维码有效期为一分钟。

    # [English]
    ### Purpose:
    - Get SSO login QR code
    ### Parameters:
    - device_id: Device ID
    - region: Region
    - proxy: Proxy
    ### Return:
    - SSO login QR code
    ### Description:
    - The QR code returned by this interface needs to be scanned by the mobile phone for login, and the
    login information will be returned after successful login.
    - If the device ID is not passed in, the device ID will be automatically generated by the backend.
    - If you need to use a proxy, please pass in the proxy address, otherwise pass in None
    - The validity period of a single QR code is one minute.

    # [示例/Example]
    device_id = \"7481276116461831688\"
    region = \"US\"
    proxy = \"None\"

    Args:
        device_id (str): 设备ID/Device ID
        region (str): 地区/Region
        proxy (str): 代理/Proxy

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        device_id=device_id,
        region=region,
        proxy=proxy,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    device_id: str,
    region: str,
    proxy: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取SSO登录二维码/Get SSO login QR code

     # [中文]
    ### 用途:
    - 获取SSO登录二维码
    ### 参数:
    - device_id: 设备ID
    - region: 地区
    - proxy: 代理
    ### 返回:
    - SSO登录二维码
    ### 说明:
    - 该接口返回的二维码需要使用手机扫描登录，登录成功后会返回登录信息。
    - 不传入设备ID将由后端自动生成设备ID。
    - 如果需要使用代理，请传入代理地址，否则传入None。
    - 单次二维码有效期为一分钟。

    # [English]
    ### Purpose:
    - Get SSO login QR code
    ### Parameters:
    - device_id: Device ID
    - region: Region
    - proxy: Proxy
    ### Return:
    - SSO login QR code
    ### Description:
    - The QR code returned by this interface needs to be scanned by the mobile phone for login, and the
    login information will be returned after successful login.
    - If the device ID is not passed in, the device ID will be automatically generated by the backend.
    - If you need to use a proxy, please pass in the proxy address, otherwise pass in None
    - The validity period of a single QR code is one minute.

    # [示例/Example]
    device_id = \"7481276116461831688\"
    region = \"US\"
    proxy = \"None\"

    Args:
        device_id (str): 设备ID/Device ID
        region (str): 地区/Region
        proxy (str): 代理/Proxy

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        device_id=device_id,
        region=region,
        proxy=proxy,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    device_id: str,
    region: str,
    proxy: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取SSO登录二维码/Get SSO login QR code

     # [中文]
    ### 用途:
    - 获取SSO登录二维码
    ### 参数:
    - device_id: 设备ID
    - region: 地区
    - proxy: 代理
    ### 返回:
    - SSO登录二维码
    ### 说明:
    - 该接口返回的二维码需要使用手机扫描登录，登录成功后会返回登录信息。
    - 不传入设备ID将由后端自动生成设备ID。
    - 如果需要使用代理，请传入代理地址，否则传入None。
    - 单次二维码有效期为一分钟。

    # [English]
    ### Purpose:
    - Get SSO login QR code
    ### Parameters:
    - device_id: Device ID
    - region: Region
    - proxy: Proxy
    ### Return:
    - SSO login QR code
    ### Description:
    - The QR code returned by this interface needs to be scanned by the mobile phone for login, and the
    login information will be returned after successful login.
    - If the device ID is not passed in, the device ID will be automatically generated by the backend.
    - If you need to use a proxy, please pass in the proxy address, otherwise pass in None
    - The validity period of a single QR code is one minute.

    # [示例/Example]
    device_id = \"7481276116461831688\"
    region = \"US\"
    proxy = \"None\"

    Args:
        device_id (str): 设备ID/Device ID
        region (str): 地区/Region
        proxy (str): 代理/Proxy

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        device_id=device_id,
        region=region,
        proxy=proxy,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    device_id: str,
    region: str,
    proxy: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取SSO登录二维码/Get SSO login QR code

     # [中文]
    ### 用途:
    - 获取SSO登录二维码
    ### 参数:
    - device_id: 设备ID
    - region: 地区
    - proxy: 代理
    ### 返回:
    - SSO登录二维码
    ### 说明:
    - 该接口返回的二维码需要使用手机扫描登录，登录成功后会返回登录信息。
    - 不传入设备ID将由后端自动生成设备ID。
    - 如果需要使用代理，请传入代理地址，否则传入None。
    - 单次二维码有效期为一分钟。

    # [English]
    ### Purpose:
    - Get SSO login QR code
    ### Parameters:
    - device_id: Device ID
    - region: Region
    - proxy: Proxy
    ### Return:
    - SSO login QR code
    ### Description:
    - The QR code returned by this interface needs to be scanned by the mobile phone for login, and the
    login information will be returned after successful login.
    - If the device ID is not passed in, the device ID will be automatically generated by the backend.
    - If you need to use a proxy, please pass in the proxy address, otherwise pass in None
    - The validity period of a single QR code is one minute.

    # [示例/Example]
    device_id = \"7481276116461831688\"
    region = \"US\"
    proxy = \"None\"

    Args:
        device_id (str): 设备ID/Device ID
        region (str): 地区/Region
        proxy (str): 代理/Proxy

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            device_id=device_id,
            region=region,
            proxy=proxy,
        )
    ).parsed
