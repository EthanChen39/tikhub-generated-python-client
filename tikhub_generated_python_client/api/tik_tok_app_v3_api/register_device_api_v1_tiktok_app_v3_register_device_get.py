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
    proxy: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["proxy"] = proxy

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/app/v3/register_device",
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
    proxy: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""注册设备信息/Register device information

     # [中文]
    ### 用途:
    - TikTok APP注册设备，获取设备信息以及设备的Cookie信息。

    ### 参数:
    - proxy: 代理，不要带http://或https://，仅支持http代理。
      - 格式: username:password@ip:port

    ### 返回:
    - 设备信息以及设备的Cookie信息。

    # [English]
    ### Purpose:
    - Register device for TikTok APP, retrieve device information and device cookies.

    ### Parameters:
    - proxy: Proxy, without http:// or https://, only supports http proxies.
      - Format: username:password@ip:port

    ### Return:
    - Device information and device cookies.

    # [示例/Example]
    proxy = \"username:password@ip:port\"

    # [响应/Response]
    ```json
    {
       \"code\":200,
       \"router\":\"/api/v1/tiktok/app/v3/register_device\",
       \"params\":{
          \"proxy\":\"username:password@ip:port\"
       },
       \"data\":{
          \"cookie\":\"install_id=7417331203928426283; store-country-code=us; store-country-code-
    src=did; store-idc=useast5; ttreq=1$85b1f5b0b40aeb0ff76598a6a94fcb0704b10d74\",
          \"id\":\"eyJhYyI6ICJ3aWZpIiwgImNoYW5uZWwiOiAiZ29vZ2xlcGxheSIsICJhaWQiOiAiMTIzMyIsICJhcHBfbmFtZ
    SI6ICJtdXNpY2FsX2x5IiwgInZlcnNpb25fY29kZSI6ICIyNjA2MDIiLCAidmVyc2lvbl9uYW1lIjogIjI2LjYuMiIsICJkZXZpY
    2VfcGxhdGZvcm0iOiAiYW5kcm9pZCIsICJhYl92ZXJzaW9uIjogIjI2LjYuMiIsICJzc21peCI6ICJhIiwgImRldmljZV90eXBlI
    jogIlBPVC1MWDQ2IiwgImRldmljZV9icmFuZCI6ICJIVUFXRUkiLCAiZGV2aWNlX21vZGVsIjogIlBPVC1MWDQ2IiwgImxhbmd1Y
    WdlIjogImVuIiwgIm9zX2FwaSI6ICIyOSIsICJvc192ZXJzaW9uIjogIjEwIiwgIm1hbmlmZXN0X3ZlcnNpb25fY29kZSI6ICIyM
    DIyNjA2MDIwIiwgInJlc29sdXRpb24iOiAiMTA4MCoyMzQwIiwgImRwaSI6ICI0ODAiLCAidXBkYXRlX3ZlcnNpb25fY29kZSI6I
    CIyMDIyNjA2MDIwIiwgImFwcF9za2luIjogIndoaXRlIiwgImFwcF90eXBlIjogIm5vcm1hbCIsICJyZXNpZGVuY2UiOiAiVVMiL
    CAic3lzX3JlZ2lvbiI6ICJVUyIsICJwYXNzLXJvdXRlIjogIjEiLCAibWNjX21uYyI6ICIzMTAyNjAiLCAicGFzcy1yZWdpb24iO
    iAiMSIsICJ0aW1lem9uZV9uYW1lIjogIkFtZXJpY2ElMkZOZXdfWW9yayIsICJjYXJyaWVyX3JlZ2lvbl92MiI6ICIzMTAiLCAiY
    3B1X3N1cHBvcnQ2NCI6ICJ0cnVlIiwgImhvc3RfYWJpIjogImFybTY0LXY4YSIsICJhcHBfbGFuZ3VhZ2UiOiAiZW4iLCAiY2Fyc
    mllcl9yZWdpb24iOiAiVVMiLCAiYWMyIjogIndpZmkiLCAidW9vIjogIjEiLCAib3BfcmVnaW9uIjogIlVTIiwgInRpbWV6b25lX
    29mZnNldCI6IC0xNDQwMCwgImJ1aWxkX251bWJlciI6ICIyNi42LjIiLCAibG9jYWxlIjogImVuIiwgInJlZ2lvbiI6ICJVUyIsI
    CJvcGVudWRpZCI6ICI0ZTM5NzdlNmJhNWNhZDc0IiwgImNkaWQiOiAiYjFkOTA2YzMtOTYxMy00MWM1LTk4ZjgtZDZhYWJjOTdiM
    TExIiwgImRldmljZV9pZCI6ICI3NDE3MzMwOTk5MDIzNTAyODkwIiwgImlpZCI6ICI3NDE3MzMxMjAzOTI4NDI2MjgzIiwgInVzZ
    XJfYWdlbnQiOiAiY29tLnpoaWxpYW9hcHAubXVzaWNhbGx5LzIwMjI2MDYwMjAgKExpbnV4OyBVOyBBbmRyb2lkIDEwLjAuMDsgZ
    W47IEhVQVdFSSBQT1QtTFg0NjsgQnVpbGQvT1BSNi4xNzA2MjMuMDE3O3R0LW9rLzMuMTIuMTMuMSkiLCAiY29va2llIjogImluc
    3RhbGxfaWQ9NzQxNzMzMTIwMzkyODQyNjI4Mzsgc3RvcmUtY291bnRyeS1jb2RlPXVzOyBzdG9yZS1jb3VudHJ5LWNvZGUtc3JjP
    WRpZDsgc3RvcmUtaWRjPXVzZWFzdDU7IHR0cmVxPTEkODViMWY1YjBiNDBhZWIwZmY3NjU5OGE2YTk0ZmNiMDcwNGIxMGQ3NCIsI
    CJwcm94eSI6ICJodHRwOi8vMTU0LjIwMi4xMDcuMjAyOjMxMjgifQ==\",
          \"tiktok_info\":{
             \"cdid\":\"b1d906c3-9613-41c5-98f8-d6aabc97b111\",
             \"cookie\":\"install_id=7417331203928426283; store-country-code=us; store-country-code-
    src=did; store-idc=useast5; ttreq=1$85b1f5b0b40aeb0ff76598a6a94fcb0704b10d74\",
             \"device_brand\":\"HUAWEI\",
             \"device_type\":\"POT-LX46\",
             \"did\":\"7417330999023502890\",
             \"iid\":\"7417331203928426283\",
             \"mcc_mnc\":\"310260\",
             \"openudid\":\"4e3977e6ba5cad74\",
             \"os_api\":\"29\",
             \"os_version\":\"10\",
             \"user_agent\":\"okhttp/3.10.0.1\",
             \"version_code\":\"260602\",
             \"version_name\":\"26.6.2\"
          }
       }
    }
    ```

    Args:
        proxy (Union[Unset, str]): 代理/Proxy

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        proxy=proxy,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    proxy: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""注册设备信息/Register device information

     # [中文]
    ### 用途:
    - TikTok APP注册设备，获取设备信息以及设备的Cookie信息。

    ### 参数:
    - proxy: 代理，不要带http://或https://，仅支持http代理。
      - 格式: username:password@ip:port

    ### 返回:
    - 设备信息以及设备的Cookie信息。

    # [English]
    ### Purpose:
    - Register device for TikTok APP, retrieve device information and device cookies.

    ### Parameters:
    - proxy: Proxy, without http:// or https://, only supports http proxies.
      - Format: username:password@ip:port

    ### Return:
    - Device information and device cookies.

    # [示例/Example]
    proxy = \"username:password@ip:port\"

    # [响应/Response]
    ```json
    {
       \"code\":200,
       \"router\":\"/api/v1/tiktok/app/v3/register_device\",
       \"params\":{
          \"proxy\":\"username:password@ip:port\"
       },
       \"data\":{
          \"cookie\":\"install_id=7417331203928426283; store-country-code=us; store-country-code-
    src=did; store-idc=useast5; ttreq=1$85b1f5b0b40aeb0ff76598a6a94fcb0704b10d74\",
          \"id\":\"eyJhYyI6ICJ3aWZpIiwgImNoYW5uZWwiOiAiZ29vZ2xlcGxheSIsICJhaWQiOiAiMTIzMyIsICJhcHBfbmFtZ
    SI6ICJtdXNpY2FsX2x5IiwgInZlcnNpb25fY29kZSI6ICIyNjA2MDIiLCAidmVyc2lvbl9uYW1lIjogIjI2LjYuMiIsICJkZXZpY
    2VfcGxhdGZvcm0iOiAiYW5kcm9pZCIsICJhYl92ZXJzaW9uIjogIjI2LjYuMiIsICJzc21peCI6ICJhIiwgImRldmljZV90eXBlI
    jogIlBPVC1MWDQ2IiwgImRldmljZV9icmFuZCI6ICJIVUFXRUkiLCAiZGV2aWNlX21vZGVsIjogIlBPVC1MWDQ2IiwgImxhbmd1Y
    WdlIjogImVuIiwgIm9zX2FwaSI6ICIyOSIsICJvc192ZXJzaW9uIjogIjEwIiwgIm1hbmlmZXN0X3ZlcnNpb25fY29kZSI6ICIyM
    DIyNjA2MDIwIiwgInJlc29sdXRpb24iOiAiMTA4MCoyMzQwIiwgImRwaSI6ICI0ODAiLCAidXBkYXRlX3ZlcnNpb25fY29kZSI6I
    CIyMDIyNjA2MDIwIiwgImFwcF9za2luIjogIndoaXRlIiwgImFwcF90eXBlIjogIm5vcm1hbCIsICJyZXNpZGVuY2UiOiAiVVMiL
    CAic3lzX3JlZ2lvbiI6ICJVUyIsICJwYXNzLXJvdXRlIjogIjEiLCAibWNjX21uYyI6ICIzMTAyNjAiLCAicGFzcy1yZWdpb24iO
    iAiMSIsICJ0aW1lem9uZV9uYW1lIjogIkFtZXJpY2ElMkZOZXdfWW9yayIsICJjYXJyaWVyX3JlZ2lvbl92MiI6ICIzMTAiLCAiY
    3B1X3N1cHBvcnQ2NCI6ICJ0cnVlIiwgImhvc3RfYWJpIjogImFybTY0LXY4YSIsICJhcHBfbGFuZ3VhZ2UiOiAiZW4iLCAiY2Fyc
    mllcl9yZWdpb24iOiAiVVMiLCAiYWMyIjogIndpZmkiLCAidW9vIjogIjEiLCAib3BfcmVnaW9uIjogIlVTIiwgInRpbWV6b25lX
    29mZnNldCI6IC0xNDQwMCwgImJ1aWxkX251bWJlciI6ICIyNi42LjIiLCAibG9jYWxlIjogImVuIiwgInJlZ2lvbiI6ICJVUyIsI
    CJvcGVudWRpZCI6ICI0ZTM5NzdlNmJhNWNhZDc0IiwgImNkaWQiOiAiYjFkOTA2YzMtOTYxMy00MWM1LTk4ZjgtZDZhYWJjOTdiM
    TExIiwgImRldmljZV9pZCI6ICI3NDE3MzMwOTk5MDIzNTAyODkwIiwgImlpZCI6ICI3NDE3MzMxMjAzOTI4NDI2MjgzIiwgInVzZ
    XJfYWdlbnQiOiAiY29tLnpoaWxpYW9hcHAubXVzaWNhbGx5LzIwMjI2MDYwMjAgKExpbnV4OyBVOyBBbmRyb2lkIDEwLjAuMDsgZ
    W47IEhVQVdFSSBQT1QtTFg0NjsgQnVpbGQvT1BSNi4xNzA2MjMuMDE3O3R0LW9rLzMuMTIuMTMuMSkiLCAiY29va2llIjogImluc
    3RhbGxfaWQ9NzQxNzMzMTIwMzkyODQyNjI4Mzsgc3RvcmUtY291bnRyeS1jb2RlPXVzOyBzdG9yZS1jb3VudHJ5LWNvZGUtc3JjP
    WRpZDsgc3RvcmUtaWRjPXVzZWFzdDU7IHR0cmVxPTEkODViMWY1YjBiNDBhZWIwZmY3NjU5OGE2YTk0ZmNiMDcwNGIxMGQ3NCIsI
    CJwcm94eSI6ICJodHRwOi8vMTU0LjIwMi4xMDcuMjAyOjMxMjgifQ==\",
          \"tiktok_info\":{
             \"cdid\":\"b1d906c3-9613-41c5-98f8-d6aabc97b111\",
             \"cookie\":\"install_id=7417331203928426283; store-country-code=us; store-country-code-
    src=did; store-idc=useast5; ttreq=1$85b1f5b0b40aeb0ff76598a6a94fcb0704b10d74\",
             \"device_brand\":\"HUAWEI\",
             \"device_type\":\"POT-LX46\",
             \"did\":\"7417330999023502890\",
             \"iid\":\"7417331203928426283\",
             \"mcc_mnc\":\"310260\",
             \"openudid\":\"4e3977e6ba5cad74\",
             \"os_api\":\"29\",
             \"os_version\":\"10\",
             \"user_agent\":\"okhttp/3.10.0.1\",
             \"version_code\":\"260602\",
             \"version_name\":\"26.6.2\"
          }
       }
    }
    ```

    Args:
        proxy (Union[Unset, str]): 代理/Proxy

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        proxy=proxy,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    proxy: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""注册设备信息/Register device information

     # [中文]
    ### 用途:
    - TikTok APP注册设备，获取设备信息以及设备的Cookie信息。

    ### 参数:
    - proxy: 代理，不要带http://或https://，仅支持http代理。
      - 格式: username:password@ip:port

    ### 返回:
    - 设备信息以及设备的Cookie信息。

    # [English]
    ### Purpose:
    - Register device for TikTok APP, retrieve device information and device cookies.

    ### Parameters:
    - proxy: Proxy, without http:// or https://, only supports http proxies.
      - Format: username:password@ip:port

    ### Return:
    - Device information and device cookies.

    # [示例/Example]
    proxy = \"username:password@ip:port\"

    # [响应/Response]
    ```json
    {
       \"code\":200,
       \"router\":\"/api/v1/tiktok/app/v3/register_device\",
       \"params\":{
          \"proxy\":\"username:password@ip:port\"
       },
       \"data\":{
          \"cookie\":\"install_id=7417331203928426283; store-country-code=us; store-country-code-
    src=did; store-idc=useast5; ttreq=1$85b1f5b0b40aeb0ff76598a6a94fcb0704b10d74\",
          \"id\":\"eyJhYyI6ICJ3aWZpIiwgImNoYW5uZWwiOiAiZ29vZ2xlcGxheSIsICJhaWQiOiAiMTIzMyIsICJhcHBfbmFtZ
    SI6ICJtdXNpY2FsX2x5IiwgInZlcnNpb25fY29kZSI6ICIyNjA2MDIiLCAidmVyc2lvbl9uYW1lIjogIjI2LjYuMiIsICJkZXZpY
    2VfcGxhdGZvcm0iOiAiYW5kcm9pZCIsICJhYl92ZXJzaW9uIjogIjI2LjYuMiIsICJzc21peCI6ICJhIiwgImRldmljZV90eXBlI
    jogIlBPVC1MWDQ2IiwgImRldmljZV9icmFuZCI6ICJIVUFXRUkiLCAiZGV2aWNlX21vZGVsIjogIlBPVC1MWDQ2IiwgImxhbmd1Y
    WdlIjogImVuIiwgIm9zX2FwaSI6ICIyOSIsICJvc192ZXJzaW9uIjogIjEwIiwgIm1hbmlmZXN0X3ZlcnNpb25fY29kZSI6ICIyM
    DIyNjA2MDIwIiwgInJlc29sdXRpb24iOiAiMTA4MCoyMzQwIiwgImRwaSI6ICI0ODAiLCAidXBkYXRlX3ZlcnNpb25fY29kZSI6I
    CIyMDIyNjA2MDIwIiwgImFwcF9za2luIjogIndoaXRlIiwgImFwcF90eXBlIjogIm5vcm1hbCIsICJyZXNpZGVuY2UiOiAiVVMiL
    CAic3lzX3JlZ2lvbiI6ICJVUyIsICJwYXNzLXJvdXRlIjogIjEiLCAibWNjX21uYyI6ICIzMTAyNjAiLCAicGFzcy1yZWdpb24iO
    iAiMSIsICJ0aW1lem9uZV9uYW1lIjogIkFtZXJpY2ElMkZOZXdfWW9yayIsICJjYXJyaWVyX3JlZ2lvbl92MiI6ICIzMTAiLCAiY
    3B1X3N1cHBvcnQ2NCI6ICJ0cnVlIiwgImhvc3RfYWJpIjogImFybTY0LXY4YSIsICJhcHBfbGFuZ3VhZ2UiOiAiZW4iLCAiY2Fyc
    mllcl9yZWdpb24iOiAiVVMiLCAiYWMyIjogIndpZmkiLCAidW9vIjogIjEiLCAib3BfcmVnaW9uIjogIlVTIiwgInRpbWV6b25lX
    29mZnNldCI6IC0xNDQwMCwgImJ1aWxkX251bWJlciI6ICIyNi42LjIiLCAibG9jYWxlIjogImVuIiwgInJlZ2lvbiI6ICJVUyIsI
    CJvcGVudWRpZCI6ICI0ZTM5NzdlNmJhNWNhZDc0IiwgImNkaWQiOiAiYjFkOTA2YzMtOTYxMy00MWM1LTk4ZjgtZDZhYWJjOTdiM
    TExIiwgImRldmljZV9pZCI6ICI3NDE3MzMwOTk5MDIzNTAyODkwIiwgImlpZCI6ICI3NDE3MzMxMjAzOTI4NDI2MjgzIiwgInVzZ
    XJfYWdlbnQiOiAiY29tLnpoaWxpYW9hcHAubXVzaWNhbGx5LzIwMjI2MDYwMjAgKExpbnV4OyBVOyBBbmRyb2lkIDEwLjAuMDsgZ
    W47IEhVQVdFSSBQT1QtTFg0NjsgQnVpbGQvT1BSNi4xNzA2MjMuMDE3O3R0LW9rLzMuMTIuMTMuMSkiLCAiY29va2llIjogImluc
    3RhbGxfaWQ9NzQxNzMzMTIwMzkyODQyNjI4Mzsgc3RvcmUtY291bnRyeS1jb2RlPXVzOyBzdG9yZS1jb3VudHJ5LWNvZGUtc3JjP
    WRpZDsgc3RvcmUtaWRjPXVzZWFzdDU7IHR0cmVxPTEkODViMWY1YjBiNDBhZWIwZmY3NjU5OGE2YTk0ZmNiMDcwNGIxMGQ3NCIsI
    CJwcm94eSI6ICJodHRwOi8vMTU0LjIwMi4xMDcuMjAyOjMxMjgifQ==\",
          \"tiktok_info\":{
             \"cdid\":\"b1d906c3-9613-41c5-98f8-d6aabc97b111\",
             \"cookie\":\"install_id=7417331203928426283; store-country-code=us; store-country-code-
    src=did; store-idc=useast5; ttreq=1$85b1f5b0b40aeb0ff76598a6a94fcb0704b10d74\",
             \"device_brand\":\"HUAWEI\",
             \"device_type\":\"POT-LX46\",
             \"did\":\"7417330999023502890\",
             \"iid\":\"7417331203928426283\",
             \"mcc_mnc\":\"310260\",
             \"openudid\":\"4e3977e6ba5cad74\",
             \"os_api\":\"29\",
             \"os_version\":\"10\",
             \"user_agent\":\"okhttp/3.10.0.1\",
             \"version_code\":\"260602\",
             \"version_name\":\"26.6.2\"
          }
       }
    }
    ```

    Args:
        proxy (Union[Unset, str]): 代理/Proxy

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        proxy=proxy,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    proxy: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""注册设备信息/Register device information

     # [中文]
    ### 用途:
    - TikTok APP注册设备，获取设备信息以及设备的Cookie信息。

    ### 参数:
    - proxy: 代理，不要带http://或https://，仅支持http代理。
      - 格式: username:password@ip:port

    ### 返回:
    - 设备信息以及设备的Cookie信息。

    # [English]
    ### Purpose:
    - Register device for TikTok APP, retrieve device information and device cookies.

    ### Parameters:
    - proxy: Proxy, without http:// or https://, only supports http proxies.
      - Format: username:password@ip:port

    ### Return:
    - Device information and device cookies.

    # [示例/Example]
    proxy = \"username:password@ip:port\"

    # [响应/Response]
    ```json
    {
       \"code\":200,
       \"router\":\"/api/v1/tiktok/app/v3/register_device\",
       \"params\":{
          \"proxy\":\"username:password@ip:port\"
       },
       \"data\":{
          \"cookie\":\"install_id=7417331203928426283; store-country-code=us; store-country-code-
    src=did; store-idc=useast5; ttreq=1$85b1f5b0b40aeb0ff76598a6a94fcb0704b10d74\",
          \"id\":\"eyJhYyI6ICJ3aWZpIiwgImNoYW5uZWwiOiAiZ29vZ2xlcGxheSIsICJhaWQiOiAiMTIzMyIsICJhcHBfbmFtZ
    SI6ICJtdXNpY2FsX2x5IiwgInZlcnNpb25fY29kZSI6ICIyNjA2MDIiLCAidmVyc2lvbl9uYW1lIjogIjI2LjYuMiIsICJkZXZpY
    2VfcGxhdGZvcm0iOiAiYW5kcm9pZCIsICJhYl92ZXJzaW9uIjogIjI2LjYuMiIsICJzc21peCI6ICJhIiwgImRldmljZV90eXBlI
    jogIlBPVC1MWDQ2IiwgImRldmljZV9icmFuZCI6ICJIVUFXRUkiLCAiZGV2aWNlX21vZGVsIjogIlBPVC1MWDQ2IiwgImxhbmd1Y
    WdlIjogImVuIiwgIm9zX2FwaSI6ICIyOSIsICJvc192ZXJzaW9uIjogIjEwIiwgIm1hbmlmZXN0X3ZlcnNpb25fY29kZSI6ICIyM
    DIyNjA2MDIwIiwgInJlc29sdXRpb24iOiAiMTA4MCoyMzQwIiwgImRwaSI6ICI0ODAiLCAidXBkYXRlX3ZlcnNpb25fY29kZSI6I
    CIyMDIyNjA2MDIwIiwgImFwcF9za2luIjogIndoaXRlIiwgImFwcF90eXBlIjogIm5vcm1hbCIsICJyZXNpZGVuY2UiOiAiVVMiL
    CAic3lzX3JlZ2lvbiI6ICJVUyIsICJwYXNzLXJvdXRlIjogIjEiLCAibWNjX21uYyI6ICIzMTAyNjAiLCAicGFzcy1yZWdpb24iO
    iAiMSIsICJ0aW1lem9uZV9uYW1lIjogIkFtZXJpY2ElMkZOZXdfWW9yayIsICJjYXJyaWVyX3JlZ2lvbl92MiI6ICIzMTAiLCAiY
    3B1X3N1cHBvcnQ2NCI6ICJ0cnVlIiwgImhvc3RfYWJpIjogImFybTY0LXY4YSIsICJhcHBfbGFuZ3VhZ2UiOiAiZW4iLCAiY2Fyc
    mllcl9yZWdpb24iOiAiVVMiLCAiYWMyIjogIndpZmkiLCAidW9vIjogIjEiLCAib3BfcmVnaW9uIjogIlVTIiwgInRpbWV6b25lX
    29mZnNldCI6IC0xNDQwMCwgImJ1aWxkX251bWJlciI6ICIyNi42LjIiLCAibG9jYWxlIjogImVuIiwgInJlZ2lvbiI6ICJVUyIsI
    CJvcGVudWRpZCI6ICI0ZTM5NzdlNmJhNWNhZDc0IiwgImNkaWQiOiAiYjFkOTA2YzMtOTYxMy00MWM1LTk4ZjgtZDZhYWJjOTdiM
    TExIiwgImRldmljZV9pZCI6ICI3NDE3MzMwOTk5MDIzNTAyODkwIiwgImlpZCI6ICI3NDE3MzMxMjAzOTI4NDI2MjgzIiwgInVzZ
    XJfYWdlbnQiOiAiY29tLnpoaWxpYW9hcHAubXVzaWNhbGx5LzIwMjI2MDYwMjAgKExpbnV4OyBVOyBBbmRyb2lkIDEwLjAuMDsgZ
    W47IEhVQVdFSSBQT1QtTFg0NjsgQnVpbGQvT1BSNi4xNzA2MjMuMDE3O3R0LW9rLzMuMTIuMTMuMSkiLCAiY29va2llIjogImluc
    3RhbGxfaWQ9NzQxNzMzMTIwMzkyODQyNjI4Mzsgc3RvcmUtY291bnRyeS1jb2RlPXVzOyBzdG9yZS1jb3VudHJ5LWNvZGUtc3JjP
    WRpZDsgc3RvcmUtaWRjPXVzZWFzdDU7IHR0cmVxPTEkODViMWY1YjBiNDBhZWIwZmY3NjU5OGE2YTk0ZmNiMDcwNGIxMGQ3NCIsI
    CJwcm94eSI6ICJodHRwOi8vMTU0LjIwMi4xMDcuMjAyOjMxMjgifQ==\",
          \"tiktok_info\":{
             \"cdid\":\"b1d906c3-9613-41c5-98f8-d6aabc97b111\",
             \"cookie\":\"install_id=7417331203928426283; store-country-code=us; store-country-code-
    src=did; store-idc=useast5; ttreq=1$85b1f5b0b40aeb0ff76598a6a94fcb0704b10d74\",
             \"device_brand\":\"HUAWEI\",
             \"device_type\":\"POT-LX46\",
             \"did\":\"7417330999023502890\",
             \"iid\":\"7417331203928426283\",
             \"mcc_mnc\":\"310260\",
             \"openudid\":\"4e3977e6ba5cad74\",
             \"os_api\":\"29\",
             \"os_version\":\"10\",
             \"user_agent\":\"okhttp/3.10.0.1\",
             \"version_code\":\"260602\",
             \"version_name\":\"26.6.2\"
          }
       }
    }
    ```

    Args:
        proxy (Union[Unset, str]): 代理/Proxy

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            proxy=proxy,
        )
    ).parsed
