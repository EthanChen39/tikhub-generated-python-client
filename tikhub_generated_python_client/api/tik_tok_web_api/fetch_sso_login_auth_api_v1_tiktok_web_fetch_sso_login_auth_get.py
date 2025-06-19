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
    verify_fp: str,
    region: str,
    proxy: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["device_id"] = device_id

    params["verifyFp"] = verify_fp

    params["region"] = region

    params["proxy"] = proxy

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/web/fetch_sso_login_auth",
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
    verify_fp: str,
    region: str,
    proxy: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""认证SSO登录/Authenticate SSO login

     # [中文]
    ### 用途:
    - 认证SSO登录
    ### 参数:
    - device_id: 设备ID
    - verifyFp: verifyFp
    - region: 地区
    - proxy: 代理
    ### 返回:
    - SSO登录认证信息
    ### 说明:
    - 认证需要保持参数一致，否则会认证失败。

    # [English]
    ### Purpose:
    - Authenticate SSO login
    ### Parameters:
    - token: Login token
    - device_id: Device ID
    - verifyFp: verifyFp
    - region: Region
    - proxy: Proxy
    ### Return:
    - SSO login authentication information
    ### Description:
    - Please use the value obtained by the /fetch_sso_login_status interface for input.
    - If you need to use a proxy, please pass in the proxy address, otherwise pass in None.

    # [示例/Example]
    device_id = \"7481276116461831688\"
    verifyFp = \"verify_m8909xlr_d7UEdRqf_mA73_4So4_B0RT_L1gFyzsKr7IL\"
    region = \"US\"
    proxy = \"None\"

    Args:
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
    device_id: str,
    verify_fp: str,
    region: str,
    proxy: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""认证SSO登录/Authenticate SSO login

     # [中文]
    ### 用途:
    - 认证SSO登录
    ### 参数:
    - device_id: 设备ID
    - verifyFp: verifyFp
    - region: 地区
    - proxy: 代理
    ### 返回:
    - SSO登录认证信息
    ### 说明:
    - 认证需要保持参数一致，否则会认证失败。

    # [English]
    ### Purpose:
    - Authenticate SSO login
    ### Parameters:
    - token: Login token
    - device_id: Device ID
    - verifyFp: verifyFp
    - region: Region
    - proxy: Proxy
    ### Return:
    - SSO login authentication information
    ### Description:
    - Please use the value obtained by the /fetch_sso_login_status interface for input.
    - If you need to use a proxy, please pass in the proxy address, otherwise pass in None.

    # [示例/Example]
    device_id = \"7481276116461831688\"
    verifyFp = \"verify_m8909xlr_d7UEdRqf_mA73_4So4_B0RT_L1gFyzsKr7IL\"
    region = \"US\"
    proxy = \"None\"

    Args:
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
        device_id=device_id,
        verify_fp=verify_fp,
        region=region,
        proxy=proxy,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    device_id: str,
    verify_fp: str,
    region: str,
    proxy: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""认证SSO登录/Authenticate SSO login

     # [中文]
    ### 用途:
    - 认证SSO登录
    ### 参数:
    - device_id: 设备ID
    - verifyFp: verifyFp
    - region: 地区
    - proxy: 代理
    ### 返回:
    - SSO登录认证信息
    ### 说明:
    - 认证需要保持参数一致，否则会认证失败。

    # [English]
    ### Purpose:
    - Authenticate SSO login
    ### Parameters:
    - token: Login token
    - device_id: Device ID
    - verifyFp: verifyFp
    - region: Region
    - proxy: Proxy
    ### Return:
    - SSO login authentication information
    ### Description:
    - Please use the value obtained by the /fetch_sso_login_status interface for input.
    - If you need to use a proxy, please pass in the proxy address, otherwise pass in None.

    # [示例/Example]
    device_id = \"7481276116461831688\"
    verifyFp = \"verify_m8909xlr_d7UEdRqf_mA73_4So4_B0RT_L1gFyzsKr7IL\"
    region = \"US\"
    proxy = \"None\"

    Args:
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
    device_id: str,
    verify_fp: str,
    region: str,
    proxy: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""认证SSO登录/Authenticate SSO login

     # [中文]
    ### 用途:
    - 认证SSO登录
    ### 参数:
    - device_id: 设备ID
    - verifyFp: verifyFp
    - region: 地区
    - proxy: 代理
    ### 返回:
    - SSO登录认证信息
    ### 说明:
    - 认证需要保持参数一致，否则会认证失败。

    # [English]
    ### Purpose:
    - Authenticate SSO login
    ### Parameters:
    - token: Login token
    - device_id: Device ID
    - verifyFp: verifyFp
    - region: Region
    - proxy: Proxy
    ### Return:
    - SSO login authentication information
    ### Description:
    - Please use the value obtained by the /fetch_sso_login_status interface for input.
    - If you need to use a proxy, please pass in the proxy address, otherwise pass in None.

    # [示例/Example]
    device_id = \"7481276116461831688\"
    verifyFp = \"verify_m8909xlr_d7UEdRqf_mA73_4So4_B0RT_L1gFyzsKr7IL\"
    region = \"US\"
    proxy = \"None\"

    Args:
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
            device_id=device_id,
            verify_fp=verify_fp,
            region=region,
            proxy=proxy,
        )
    ).parsed
