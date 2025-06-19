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
        "url": "/api/v1/douyin/app/v3/register_device",
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
    r"""抖音APP注册设备/Douyin APP register device

     # [中文]
    ### 用途:
    - 抖音APP注册设备，获取设备信息以及设备的Cookie信息。

    ### 参数:
    - proxy: 代理，要带http://或https://，仅支持http代理。
      - 格式: username:password@ip:port

    ### 返回:
    - 设备信息以及设备的Cookie信息。

    # [English]
    ### Purpose:
    - Register device in Douyin APP, retrieve device information and device cookies.

    ### Parameters:
    - proxy: Proxy, with http:// or https://, only supports http proxies.
      - Format: username:password@ip:port

    ### Return:
    - Device information and device cookies.

    # [示例/Example]
    proxy = \"http://username:password@ip:port\"

    # [响应/Response]
    ```json
    {
        \"code\": 200,
        \"router\": \"/api/v1/douyin/app/v3/register_device\",
        \"params\": {
            \"proxy\": \"username:password@ip:port\"
        },
        \"data\": {
            \"iid\": \"3631064037200330\",
            \"device_id\": \"3631064037196234\",
            \"mssdk_token\": \"\",
            \"device_platform\": \"android\",
            \"channel\": \"xiaomi_64_1775\",
            \"version_code\": 240900,
            \"version_name\": \"24.9.0\",
            \"manifest_version_code\": 240901,
            \"update_version_code\": 24909900,
            \"device_type\": \"V1963A\",
            \"device_brand\": \"vivo\",
            \"device_model\": \"V1963A\",
            \"openudid\": \"5d736335afc17aab\",
            \"os_api\": 29,
            \"os_version\": \"10\",
            \"resolution\": \"2400x1080\",
            \"dpi\": 480,
            \"host_abi\": \"arm64-v8a\",
            \"ua\": \"com.ss.android.ugc.aweme/240901 (Linux; U; Android 10; zh_CN; V1963A;
    Build/compiler10301842;tt-ok/3.12.13.4-tiktok)\",
            \"cookies\": {
                \"install_id\": \"3631064037200330\",
                \"odin_tt\": \"5ef413aaa319b3a4077814a1da3d3e1bcec3e8640ddc3ad30945a8518f59d1563d24c3b7a
    3c59d97fbd5344f13208a25cf143312acf4462b028e56cd0b611cc3fc2a64318f7375470d6db86440f92841\",
                \"d_ticket\": \"42186c5b0c54ea1a2a9e02d4e62bf6ab\",
                \"store-region\": \"cn-js\",
                \"store-region-src\": \"did\",
                \"multi_sids\": \"462868309327184:38167255076198698951907954929873\",
                \"passport_csrf_token\": \"6f75287240634ad1f51f3b3bdcdb5424\",
                \"passport_csrf_token_default\": \"6f75287240634ad1f51f3b3bdcdb5424\",
                \"ttreq\": \"1$7f616210b41fc044b1f164542ac4e064288b5163\"
            },
            \"lanusk\": \"\",
            \"device_manufacturer\": \"vivo\",
            \"uuid\": \"357125675341697\",
            \"cdid\": \"f64372bf-4d1d-4883-bc8a-d3d6fa87a9e3\",
            \"first_launch_timestamp\": 1726970498636,
            \"x_tt_dt\": \"AAA2FGV24A2GAOHJJ3D3XCJ32IZDZ26XXKMQAOTDNUDWTB644ISU5YA3GBYVX2Y3XVOQ3ISDH3UA4
    JXGGNFXBLJ6AAZU7QTIBKHFYJLDJMDG5K36LVPBRCKLHW2XM\",
            \"BootTime\": 1726980411,
            \"MbTime\": 1726780411,
            \"server_time\": 1726980500,
            \"mc\": \"2A:66:7A:2D:8B:29\",
            \"rom\": \"compiler10301842\",
            \"rom_version\": \"PD1963-user 10 QP1A.190711.020 compiler10301842 release-keys\"
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
    r"""抖音APP注册设备/Douyin APP register device

     # [中文]
    ### 用途:
    - 抖音APP注册设备，获取设备信息以及设备的Cookie信息。

    ### 参数:
    - proxy: 代理，要带http://或https://，仅支持http代理。
      - 格式: username:password@ip:port

    ### 返回:
    - 设备信息以及设备的Cookie信息。

    # [English]
    ### Purpose:
    - Register device in Douyin APP, retrieve device information and device cookies.

    ### Parameters:
    - proxy: Proxy, with http:// or https://, only supports http proxies.
      - Format: username:password@ip:port

    ### Return:
    - Device information and device cookies.

    # [示例/Example]
    proxy = \"http://username:password@ip:port\"

    # [响应/Response]
    ```json
    {
        \"code\": 200,
        \"router\": \"/api/v1/douyin/app/v3/register_device\",
        \"params\": {
            \"proxy\": \"username:password@ip:port\"
        },
        \"data\": {
            \"iid\": \"3631064037200330\",
            \"device_id\": \"3631064037196234\",
            \"mssdk_token\": \"\",
            \"device_platform\": \"android\",
            \"channel\": \"xiaomi_64_1775\",
            \"version_code\": 240900,
            \"version_name\": \"24.9.0\",
            \"manifest_version_code\": 240901,
            \"update_version_code\": 24909900,
            \"device_type\": \"V1963A\",
            \"device_brand\": \"vivo\",
            \"device_model\": \"V1963A\",
            \"openudid\": \"5d736335afc17aab\",
            \"os_api\": 29,
            \"os_version\": \"10\",
            \"resolution\": \"2400x1080\",
            \"dpi\": 480,
            \"host_abi\": \"arm64-v8a\",
            \"ua\": \"com.ss.android.ugc.aweme/240901 (Linux; U; Android 10; zh_CN; V1963A;
    Build/compiler10301842;tt-ok/3.12.13.4-tiktok)\",
            \"cookies\": {
                \"install_id\": \"3631064037200330\",
                \"odin_tt\": \"5ef413aaa319b3a4077814a1da3d3e1bcec3e8640ddc3ad30945a8518f59d1563d24c3b7a
    3c59d97fbd5344f13208a25cf143312acf4462b028e56cd0b611cc3fc2a64318f7375470d6db86440f92841\",
                \"d_ticket\": \"42186c5b0c54ea1a2a9e02d4e62bf6ab\",
                \"store-region\": \"cn-js\",
                \"store-region-src\": \"did\",
                \"multi_sids\": \"462868309327184:38167255076198698951907954929873\",
                \"passport_csrf_token\": \"6f75287240634ad1f51f3b3bdcdb5424\",
                \"passport_csrf_token_default\": \"6f75287240634ad1f51f3b3bdcdb5424\",
                \"ttreq\": \"1$7f616210b41fc044b1f164542ac4e064288b5163\"
            },
            \"lanusk\": \"\",
            \"device_manufacturer\": \"vivo\",
            \"uuid\": \"357125675341697\",
            \"cdid\": \"f64372bf-4d1d-4883-bc8a-d3d6fa87a9e3\",
            \"first_launch_timestamp\": 1726970498636,
            \"x_tt_dt\": \"AAA2FGV24A2GAOHJJ3D3XCJ32IZDZ26XXKMQAOTDNUDWTB644ISU5YA3GBYVX2Y3XVOQ3ISDH3UA4
    JXGGNFXBLJ6AAZU7QTIBKHFYJLDJMDG5K36LVPBRCKLHW2XM\",
            \"BootTime\": 1726980411,
            \"MbTime\": 1726780411,
            \"server_time\": 1726980500,
            \"mc\": \"2A:66:7A:2D:8B:29\",
            \"rom\": \"compiler10301842\",
            \"rom_version\": \"PD1963-user 10 QP1A.190711.020 compiler10301842 release-keys\"
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
    r"""抖音APP注册设备/Douyin APP register device

     # [中文]
    ### 用途:
    - 抖音APP注册设备，获取设备信息以及设备的Cookie信息。

    ### 参数:
    - proxy: 代理，要带http://或https://，仅支持http代理。
      - 格式: username:password@ip:port

    ### 返回:
    - 设备信息以及设备的Cookie信息。

    # [English]
    ### Purpose:
    - Register device in Douyin APP, retrieve device information and device cookies.

    ### Parameters:
    - proxy: Proxy, with http:// or https://, only supports http proxies.
      - Format: username:password@ip:port

    ### Return:
    - Device information and device cookies.

    # [示例/Example]
    proxy = \"http://username:password@ip:port\"

    # [响应/Response]
    ```json
    {
        \"code\": 200,
        \"router\": \"/api/v1/douyin/app/v3/register_device\",
        \"params\": {
            \"proxy\": \"username:password@ip:port\"
        },
        \"data\": {
            \"iid\": \"3631064037200330\",
            \"device_id\": \"3631064037196234\",
            \"mssdk_token\": \"\",
            \"device_platform\": \"android\",
            \"channel\": \"xiaomi_64_1775\",
            \"version_code\": 240900,
            \"version_name\": \"24.9.0\",
            \"manifest_version_code\": 240901,
            \"update_version_code\": 24909900,
            \"device_type\": \"V1963A\",
            \"device_brand\": \"vivo\",
            \"device_model\": \"V1963A\",
            \"openudid\": \"5d736335afc17aab\",
            \"os_api\": 29,
            \"os_version\": \"10\",
            \"resolution\": \"2400x1080\",
            \"dpi\": 480,
            \"host_abi\": \"arm64-v8a\",
            \"ua\": \"com.ss.android.ugc.aweme/240901 (Linux; U; Android 10; zh_CN; V1963A;
    Build/compiler10301842;tt-ok/3.12.13.4-tiktok)\",
            \"cookies\": {
                \"install_id\": \"3631064037200330\",
                \"odin_tt\": \"5ef413aaa319b3a4077814a1da3d3e1bcec3e8640ddc3ad30945a8518f59d1563d24c3b7a
    3c59d97fbd5344f13208a25cf143312acf4462b028e56cd0b611cc3fc2a64318f7375470d6db86440f92841\",
                \"d_ticket\": \"42186c5b0c54ea1a2a9e02d4e62bf6ab\",
                \"store-region\": \"cn-js\",
                \"store-region-src\": \"did\",
                \"multi_sids\": \"462868309327184:38167255076198698951907954929873\",
                \"passport_csrf_token\": \"6f75287240634ad1f51f3b3bdcdb5424\",
                \"passport_csrf_token_default\": \"6f75287240634ad1f51f3b3bdcdb5424\",
                \"ttreq\": \"1$7f616210b41fc044b1f164542ac4e064288b5163\"
            },
            \"lanusk\": \"\",
            \"device_manufacturer\": \"vivo\",
            \"uuid\": \"357125675341697\",
            \"cdid\": \"f64372bf-4d1d-4883-bc8a-d3d6fa87a9e3\",
            \"first_launch_timestamp\": 1726970498636,
            \"x_tt_dt\": \"AAA2FGV24A2GAOHJJ3D3XCJ32IZDZ26XXKMQAOTDNUDWTB644ISU5YA3GBYVX2Y3XVOQ3ISDH3UA4
    JXGGNFXBLJ6AAZU7QTIBKHFYJLDJMDG5K36LVPBRCKLHW2XM\",
            \"BootTime\": 1726980411,
            \"MbTime\": 1726780411,
            \"server_time\": 1726980500,
            \"mc\": \"2A:66:7A:2D:8B:29\",
            \"rom\": \"compiler10301842\",
            \"rom_version\": \"PD1963-user 10 QP1A.190711.020 compiler10301842 release-keys\"
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
    r"""抖音APP注册设备/Douyin APP register device

     # [中文]
    ### 用途:
    - 抖音APP注册设备，获取设备信息以及设备的Cookie信息。

    ### 参数:
    - proxy: 代理，要带http://或https://，仅支持http代理。
      - 格式: username:password@ip:port

    ### 返回:
    - 设备信息以及设备的Cookie信息。

    # [English]
    ### Purpose:
    - Register device in Douyin APP, retrieve device information and device cookies.

    ### Parameters:
    - proxy: Proxy, with http:// or https://, only supports http proxies.
      - Format: username:password@ip:port

    ### Return:
    - Device information and device cookies.

    # [示例/Example]
    proxy = \"http://username:password@ip:port\"

    # [响应/Response]
    ```json
    {
        \"code\": 200,
        \"router\": \"/api/v1/douyin/app/v3/register_device\",
        \"params\": {
            \"proxy\": \"username:password@ip:port\"
        },
        \"data\": {
            \"iid\": \"3631064037200330\",
            \"device_id\": \"3631064037196234\",
            \"mssdk_token\": \"\",
            \"device_platform\": \"android\",
            \"channel\": \"xiaomi_64_1775\",
            \"version_code\": 240900,
            \"version_name\": \"24.9.0\",
            \"manifest_version_code\": 240901,
            \"update_version_code\": 24909900,
            \"device_type\": \"V1963A\",
            \"device_brand\": \"vivo\",
            \"device_model\": \"V1963A\",
            \"openudid\": \"5d736335afc17aab\",
            \"os_api\": 29,
            \"os_version\": \"10\",
            \"resolution\": \"2400x1080\",
            \"dpi\": 480,
            \"host_abi\": \"arm64-v8a\",
            \"ua\": \"com.ss.android.ugc.aweme/240901 (Linux; U; Android 10; zh_CN; V1963A;
    Build/compiler10301842;tt-ok/3.12.13.4-tiktok)\",
            \"cookies\": {
                \"install_id\": \"3631064037200330\",
                \"odin_tt\": \"5ef413aaa319b3a4077814a1da3d3e1bcec3e8640ddc3ad30945a8518f59d1563d24c3b7a
    3c59d97fbd5344f13208a25cf143312acf4462b028e56cd0b611cc3fc2a64318f7375470d6db86440f92841\",
                \"d_ticket\": \"42186c5b0c54ea1a2a9e02d4e62bf6ab\",
                \"store-region\": \"cn-js\",
                \"store-region-src\": \"did\",
                \"multi_sids\": \"462868309327184:38167255076198698951907954929873\",
                \"passport_csrf_token\": \"6f75287240634ad1f51f3b3bdcdb5424\",
                \"passport_csrf_token_default\": \"6f75287240634ad1f51f3b3bdcdb5424\",
                \"ttreq\": \"1$7f616210b41fc044b1f164542ac4e064288b5163\"
            },
            \"lanusk\": \"\",
            \"device_manufacturer\": \"vivo\",
            \"uuid\": \"357125675341697\",
            \"cdid\": \"f64372bf-4d1d-4883-bc8a-d3d6fa87a9e3\",
            \"first_launch_timestamp\": 1726970498636,
            \"x_tt_dt\": \"AAA2FGV24A2GAOHJJ3D3XCJ32IZDZ26XXKMQAOTDNUDWTB644ISU5YA3GBYVX2Y3XVOQ3ISDH3UA4
    JXGGNFXBLJ6AAZU7QTIBKHFYJLDJMDG5K36LVPBRCKLHW2XM\",
            \"BootTime\": 1726980411,
            \"MbTime\": 1726780411,
            \"server_time\": 1726980500,
            \"mc\": \"2A:66:7A:2D:8B:29\",
            \"rom\": \"compiler10301842\",
            \"rom_version\": \"PD1963-user 10 QP1A.190711.020 compiler10301842 release-keys\"
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
