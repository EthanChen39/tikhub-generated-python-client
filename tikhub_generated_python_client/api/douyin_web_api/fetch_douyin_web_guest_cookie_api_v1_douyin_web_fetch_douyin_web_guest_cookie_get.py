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
    user_agent: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["user_agent"] = user_agent

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/web/fetch_douyin_web_guest_cookie",
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
    user_agent: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取抖音Web的游客Cookie/Get the guest Cookie of Douyin Web

     # [中文]
    ### 用途:
    - 获取抖音Web的游客Cookie
    - 可以用于爬取抖音Web的数据，如用户作品、合辑作品等。
    - 可以固定身份避免部分接口重复数据。
    - 请注意：游客Cookie无法爬取所有数据，有一定的限制。
    - 可以配合开源项目使用此接口实现抖音Web的数据爬取。
    ### 参数:
    - user_agent: 用户浏览器代理
    ### 返回:
    - 游客Cookie

    # [English]
    ### Purpose:
    - Get the guest Cookie of Douyin Web
    - Can be used to crawl data of Douyin Web, such as user videos, mix videos, etc.
    - Can fix identity to avoid duplicate data for some interfaces.
    - Please note: Guest Cookie cannot crawl all data, there are certain restrictions.
    - Can be used with open source projects to implement data crawling of Douyin Web using this
    interface.
    ### Parameters:
    - user_agent: User browser agent
    ### Return:
    - Guest Cookie

    # [示例/Example]
    user_agent = \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
    Chrome/90.0.4430.212 Safari/537.36\"

    Args:
        user_agent (str): 用户浏览器代理/User browser agent

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        user_agent=user_agent,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_agent: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取抖音Web的游客Cookie/Get the guest Cookie of Douyin Web

     # [中文]
    ### 用途:
    - 获取抖音Web的游客Cookie
    - 可以用于爬取抖音Web的数据，如用户作品、合辑作品等。
    - 可以固定身份避免部分接口重复数据。
    - 请注意：游客Cookie无法爬取所有数据，有一定的限制。
    - 可以配合开源项目使用此接口实现抖音Web的数据爬取。
    ### 参数:
    - user_agent: 用户浏览器代理
    ### 返回:
    - 游客Cookie

    # [English]
    ### Purpose:
    - Get the guest Cookie of Douyin Web
    - Can be used to crawl data of Douyin Web, such as user videos, mix videos, etc.
    - Can fix identity to avoid duplicate data for some interfaces.
    - Please note: Guest Cookie cannot crawl all data, there are certain restrictions.
    - Can be used with open source projects to implement data crawling of Douyin Web using this
    interface.
    ### Parameters:
    - user_agent: User browser agent
    ### Return:
    - Guest Cookie

    # [示例/Example]
    user_agent = \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
    Chrome/90.0.4430.212 Safari/537.36\"

    Args:
        user_agent (str): 用户浏览器代理/User browser agent

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        user_agent=user_agent,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_agent: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取抖音Web的游客Cookie/Get the guest Cookie of Douyin Web

     # [中文]
    ### 用途:
    - 获取抖音Web的游客Cookie
    - 可以用于爬取抖音Web的数据，如用户作品、合辑作品等。
    - 可以固定身份避免部分接口重复数据。
    - 请注意：游客Cookie无法爬取所有数据，有一定的限制。
    - 可以配合开源项目使用此接口实现抖音Web的数据爬取。
    ### 参数:
    - user_agent: 用户浏览器代理
    ### 返回:
    - 游客Cookie

    # [English]
    ### Purpose:
    - Get the guest Cookie of Douyin Web
    - Can be used to crawl data of Douyin Web, such as user videos, mix videos, etc.
    - Can fix identity to avoid duplicate data for some interfaces.
    - Please note: Guest Cookie cannot crawl all data, there are certain restrictions.
    - Can be used with open source projects to implement data crawling of Douyin Web using this
    interface.
    ### Parameters:
    - user_agent: User browser agent
    ### Return:
    - Guest Cookie

    # [示例/Example]
    user_agent = \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
    Chrome/90.0.4430.212 Safari/537.36\"

    Args:
        user_agent (str): 用户浏览器代理/User browser agent

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        user_agent=user_agent,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_agent: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取抖音Web的游客Cookie/Get the guest Cookie of Douyin Web

     # [中文]
    ### 用途:
    - 获取抖音Web的游客Cookie
    - 可以用于爬取抖音Web的数据，如用户作品、合辑作品等。
    - 可以固定身份避免部分接口重复数据。
    - 请注意：游客Cookie无法爬取所有数据，有一定的限制。
    - 可以配合开源项目使用此接口实现抖音Web的数据爬取。
    ### 参数:
    - user_agent: 用户浏览器代理
    ### 返回:
    - 游客Cookie

    # [English]
    ### Purpose:
    - Get the guest Cookie of Douyin Web
    - Can be used to crawl data of Douyin Web, such as user videos, mix videos, etc.
    - Can fix identity to avoid duplicate data for some interfaces.
    - Please note: Guest Cookie cannot crawl all data, there are certain restrictions.
    - Can be used with open source projects to implement data crawling of Douyin Web using this
    interface.
    ### Parameters:
    - user_agent: User browser agent
    ### Return:
    - Guest Cookie

    # [示例/Example]
    user_agent = \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
    Chrome/90.0.4430.212 Safari/537.36\"

    Args:
        user_agent (str): 用户浏览器代理/User browser agent

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_agent=user_agent,
        )
    ).parsed
