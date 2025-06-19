from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...models.x_bogus_model import XBogusModel
from ...types import Response


def _get_kwargs(
    *,
    body: XBogusModel,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tiktok/web/generate_xbogus",
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
    body: XBogusModel,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""生成xbogus/Generate xbogus

     # [中文]
    ### 用途:
    - 生成xbogus
    ### 参数:
    - url: 未签名的API URL
    - user_agent: 用户浏览器User-Agent
    ### 返回:
    - xbogus

    # [English]
    ### Purpose:
    - Generate xbogus
    ### Parameters:
    - url: Unsigned API URL
    - user_agent: User browser User-Agent
    ### Return:
    - xbogus

    # [示例/Example]

    ```json
    {
        \"url\": \"https://www.douyin.com/aweme/v1/web/aweme/detail/?aweme_id=7148736076176215311&device
    _platform=webapp&aid=6383&channel=channel_pc_web&pc_client_type=1&version_code=170400&version_name=1
    7.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platfo
    rm=Win32&browser_name=Edge&browser_version=117.0.2045.47&browser_online=true&engine_name=Blink&engin
    e_version=117.0.0.0&os_name=Windows&os_version=10&cpu_core_num=128&device_memory=10240&platform=PC&d
    ownlink=10&effective_type=4g&round_trip_time=100\",
        \"user_agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like
    Gecko) Chrome/90.0.4430.212 Safari/537.36\"
    }

    Args:
        body (XBogusModel):

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
    body: XBogusModel,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""生成xbogus/Generate xbogus

     # [中文]
    ### 用途:
    - 生成xbogus
    ### 参数:
    - url: 未签名的API URL
    - user_agent: 用户浏览器User-Agent
    ### 返回:
    - xbogus

    # [English]
    ### Purpose:
    - Generate xbogus
    ### Parameters:
    - url: Unsigned API URL
    - user_agent: User browser User-Agent
    ### Return:
    - xbogus

    # [示例/Example]

    ```json
    {
        \"url\": \"https://www.douyin.com/aweme/v1/web/aweme/detail/?aweme_id=7148736076176215311&device
    _platform=webapp&aid=6383&channel=channel_pc_web&pc_client_type=1&version_code=170400&version_name=1
    7.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platfo
    rm=Win32&browser_name=Edge&browser_version=117.0.2045.47&browser_online=true&engine_name=Blink&engin
    e_version=117.0.0.0&os_name=Windows&os_version=10&cpu_core_num=128&device_memory=10240&platform=PC&d
    ownlink=10&effective_type=4g&round_trip_time=100\",
        \"user_agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like
    Gecko) Chrome/90.0.4430.212 Safari/537.36\"
    }

    Args:
        body (XBogusModel):

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
    body: XBogusModel,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""生成xbogus/Generate xbogus

     # [中文]
    ### 用途:
    - 生成xbogus
    ### 参数:
    - url: 未签名的API URL
    - user_agent: 用户浏览器User-Agent
    ### 返回:
    - xbogus

    # [English]
    ### Purpose:
    - Generate xbogus
    ### Parameters:
    - url: Unsigned API URL
    - user_agent: User browser User-Agent
    ### Return:
    - xbogus

    # [示例/Example]

    ```json
    {
        \"url\": \"https://www.douyin.com/aweme/v1/web/aweme/detail/?aweme_id=7148736076176215311&device
    _platform=webapp&aid=6383&channel=channel_pc_web&pc_client_type=1&version_code=170400&version_name=1
    7.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platfo
    rm=Win32&browser_name=Edge&browser_version=117.0.2045.47&browser_online=true&engine_name=Blink&engin
    e_version=117.0.0.0&os_name=Windows&os_version=10&cpu_core_num=128&device_memory=10240&platform=PC&d
    ownlink=10&effective_type=4g&round_trip_time=100\",
        \"user_agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like
    Gecko) Chrome/90.0.4430.212 Safari/537.36\"
    }

    Args:
        body (XBogusModel):

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
    body: XBogusModel,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""生成xbogus/Generate xbogus

     # [中文]
    ### 用途:
    - 生成xbogus
    ### 参数:
    - url: 未签名的API URL
    - user_agent: 用户浏览器User-Agent
    ### 返回:
    - xbogus

    # [English]
    ### Purpose:
    - Generate xbogus
    ### Parameters:
    - url: Unsigned API URL
    - user_agent: User browser User-Agent
    ### Return:
    - xbogus

    # [示例/Example]

    ```json
    {
        \"url\": \"https://www.douyin.com/aweme/v1/web/aweme/detail/?aweme_id=7148736076176215311&device
    _platform=webapp&aid=6383&channel=channel_pc_web&pc_client_type=1&version_code=170400&version_name=1
    7.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platfo
    rm=Win32&browser_name=Edge&browser_version=117.0.2045.47&browser_online=true&engine_name=Blink&engin
    e_version=117.0.0.0&os_name=Windows&os_version=10&cpu_core_num=128&device_memory=10240&platform=PC&d
    ownlink=10&effective_type=4g&round_trip_time=100\",
        \"user_agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like
    Gecko) Chrome/90.0.4430.212 Safari/537.36\"
    }

    Args:
        body (XBogusModel):

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
