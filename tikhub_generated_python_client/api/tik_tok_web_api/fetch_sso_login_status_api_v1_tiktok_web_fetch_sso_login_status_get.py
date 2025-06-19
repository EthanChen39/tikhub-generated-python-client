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
    token: str,
    device_id: str,
    verify_fp: str,
    region: str,
    proxy: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["token"] = token

    params["device_id"] = device_id

    params["verifyFp"] = verify_fp

    params["region"] = region

    params["proxy"] = proxy

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/web/fetch_sso_login_status",
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
    token: str,
    device_id: str,
    verify_fp: str,
    region: str,
    proxy: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取SSO登录状态/Get SSO login status

     # [中文]
    ### 用途:
    - 获取SSO登录状态
    ### 参数:
    - token: 登录令牌
    - device_id: 设备ID
    - verifyFp: verifyFp
    - region: 地区
    - proxy: 代理
    ### 返回:
    - SSO登录状态
    ### 说明:
    - 该接口返回的登录状态需要轮询，建议2秒轮询一次。
    - 请使用/fetch_sso_login_qrcode接口获取的值进行传入。
    - 如果需要使用代理，请传入代理地址，否则传入None。
    - 扫码状态：
        - new: 未扫码
        - expired: 二维码过期（需要重新请求/fetch_sso_login_qrcode）
        - scanned: 已扫码
        - confirmed: 已确认登录（需要请求/fetch_sso_login_auth认证）

    # [English]
    ### Purpose:
    - Get SSO login status
    ### Parameters:
    - token: Login token
    - device_id: Device ID
    - verifyFp: verifyFp
    - region: Region
    - proxy: Proxy
    ### Return:
    - SSO login status
    ### Description:
    - The login status returned by this interface needs to be polled, and it is recommended to poll once
    every 2 seconds.
    - Please use the value obtained by the /fetch_sso_login_qrcode interface for input.
    - If you need to use a proxy, please pass in the proxy address, otherwise pass in None.
    - Scan status:
        - new: Not scanned
        - expired: QR code expired (need to request /fetch_sso_login_qrcode again)
        - scanned: Scanned
        - confirmed: Confirmed login (need to request /fetch_sso_login_auth for authentication

    # [示例/Example]
    token = \"jiHRabSoJdwNrsvJvlRKj4hecTstR2xsn2NmtmKMN8o=_useast5\"
    device_id = \"7481276116461831688\"
    verifyFp = \"verify_m8909xlr_d7UEdRqf_mA73_4So4_B0RT_L1gFyzsKr7IL\"
    region = \"US\"
    proxy = \"None\"

    Args:
        token (str): 登录令牌/Login token
        device_id (str): 设备ID/Device ID
        verify_fp (str): verifyFp
        region (str): 地区/Region
        proxy (str): 代理/Proxy

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        token=token,
        device_id=device_id,
        verify_fp=verify_fp,
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
    token: str,
    device_id: str,
    verify_fp: str,
    region: str,
    proxy: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取SSO登录状态/Get SSO login status

     # [中文]
    ### 用途:
    - 获取SSO登录状态
    ### 参数:
    - token: 登录令牌
    - device_id: 设备ID
    - verifyFp: verifyFp
    - region: 地区
    - proxy: 代理
    ### 返回:
    - SSO登录状态
    ### 说明:
    - 该接口返回的登录状态需要轮询，建议2秒轮询一次。
    - 请使用/fetch_sso_login_qrcode接口获取的值进行传入。
    - 如果需要使用代理，请传入代理地址，否则传入None。
    - 扫码状态：
        - new: 未扫码
        - expired: 二维码过期（需要重新请求/fetch_sso_login_qrcode）
        - scanned: 已扫码
        - confirmed: 已确认登录（需要请求/fetch_sso_login_auth认证）

    # [English]
    ### Purpose:
    - Get SSO login status
    ### Parameters:
    - token: Login token
    - device_id: Device ID
    - verifyFp: verifyFp
    - region: Region
    - proxy: Proxy
    ### Return:
    - SSO login status
    ### Description:
    - The login status returned by this interface needs to be polled, and it is recommended to poll once
    every 2 seconds.
    - Please use the value obtained by the /fetch_sso_login_qrcode interface for input.
    - If you need to use a proxy, please pass in the proxy address, otherwise pass in None.
    - Scan status:
        - new: Not scanned
        - expired: QR code expired (need to request /fetch_sso_login_qrcode again)
        - scanned: Scanned
        - confirmed: Confirmed login (need to request /fetch_sso_login_auth for authentication

    # [示例/Example]
    token = \"jiHRabSoJdwNrsvJvlRKj4hecTstR2xsn2NmtmKMN8o=_useast5\"
    device_id = \"7481276116461831688\"
    verifyFp = \"verify_m8909xlr_d7UEdRqf_mA73_4So4_B0RT_L1gFyzsKr7IL\"
    region = \"US\"
    proxy = \"None\"

    Args:
        token (str): 登录令牌/Login token
        device_id (str): 设备ID/Device ID
        verify_fp (str): verifyFp
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
        token=token,
        device_id=device_id,
        verify_fp=verify_fp,
        region=region,
        proxy=proxy,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    token: str,
    device_id: str,
    verify_fp: str,
    region: str,
    proxy: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取SSO登录状态/Get SSO login status

     # [中文]
    ### 用途:
    - 获取SSO登录状态
    ### 参数:
    - token: 登录令牌
    - device_id: 设备ID
    - verifyFp: verifyFp
    - region: 地区
    - proxy: 代理
    ### 返回:
    - SSO登录状态
    ### 说明:
    - 该接口返回的登录状态需要轮询，建议2秒轮询一次。
    - 请使用/fetch_sso_login_qrcode接口获取的值进行传入。
    - 如果需要使用代理，请传入代理地址，否则传入None。
    - 扫码状态：
        - new: 未扫码
        - expired: 二维码过期（需要重新请求/fetch_sso_login_qrcode）
        - scanned: 已扫码
        - confirmed: 已确认登录（需要请求/fetch_sso_login_auth认证）

    # [English]
    ### Purpose:
    - Get SSO login status
    ### Parameters:
    - token: Login token
    - device_id: Device ID
    - verifyFp: verifyFp
    - region: Region
    - proxy: Proxy
    ### Return:
    - SSO login status
    ### Description:
    - The login status returned by this interface needs to be polled, and it is recommended to poll once
    every 2 seconds.
    - Please use the value obtained by the /fetch_sso_login_qrcode interface for input.
    - If you need to use a proxy, please pass in the proxy address, otherwise pass in None.
    - Scan status:
        - new: Not scanned
        - expired: QR code expired (need to request /fetch_sso_login_qrcode again)
        - scanned: Scanned
        - confirmed: Confirmed login (need to request /fetch_sso_login_auth for authentication

    # [示例/Example]
    token = \"jiHRabSoJdwNrsvJvlRKj4hecTstR2xsn2NmtmKMN8o=_useast5\"
    device_id = \"7481276116461831688\"
    verifyFp = \"verify_m8909xlr_d7UEdRqf_mA73_4So4_B0RT_L1gFyzsKr7IL\"
    region = \"US\"
    proxy = \"None\"

    Args:
        token (str): 登录令牌/Login token
        device_id (str): 设备ID/Device ID
        verify_fp (str): verifyFp
        region (str): 地区/Region
        proxy (str): 代理/Proxy

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        token=token,
        device_id=device_id,
        verify_fp=verify_fp,
        region=region,
        proxy=proxy,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    token: str,
    device_id: str,
    verify_fp: str,
    region: str,
    proxy: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取SSO登录状态/Get SSO login status

     # [中文]
    ### 用途:
    - 获取SSO登录状态
    ### 参数:
    - token: 登录令牌
    - device_id: 设备ID
    - verifyFp: verifyFp
    - region: 地区
    - proxy: 代理
    ### 返回:
    - SSO登录状态
    ### 说明:
    - 该接口返回的登录状态需要轮询，建议2秒轮询一次。
    - 请使用/fetch_sso_login_qrcode接口获取的值进行传入。
    - 如果需要使用代理，请传入代理地址，否则传入None。
    - 扫码状态：
        - new: 未扫码
        - expired: 二维码过期（需要重新请求/fetch_sso_login_qrcode）
        - scanned: 已扫码
        - confirmed: 已确认登录（需要请求/fetch_sso_login_auth认证）

    # [English]
    ### Purpose:
    - Get SSO login status
    ### Parameters:
    - token: Login token
    - device_id: Device ID
    - verifyFp: verifyFp
    - region: Region
    - proxy: Proxy
    ### Return:
    - SSO login status
    ### Description:
    - The login status returned by this interface needs to be polled, and it is recommended to poll once
    every 2 seconds.
    - Please use the value obtained by the /fetch_sso_login_qrcode interface for input.
    - If you need to use a proxy, please pass in the proxy address, otherwise pass in None.
    - Scan status:
        - new: Not scanned
        - expired: QR code expired (need to request /fetch_sso_login_qrcode again)
        - scanned: Scanned
        - confirmed: Confirmed login (need to request /fetch_sso_login_auth for authentication

    # [示例/Example]
    token = \"jiHRabSoJdwNrsvJvlRKj4hecTstR2xsn2NmtmKMN8o=_useast5\"
    device_id = \"7481276116461831688\"
    verifyFp = \"verify_m8909xlr_d7UEdRqf_mA73_4So4_B0RT_L1gFyzsKr7IL\"
    region = \"US\"
    proxy = \"None\"

    Args:
        token (str): 登录令牌/Login token
        device_id (str): 设备ID/Device ID
        verify_fp (str): verifyFp
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
            token=token,
            device_id=device_id,
            verify_fp=verify_fp,
            region=region,
            proxy=proxy,
        )
    ).parsed
