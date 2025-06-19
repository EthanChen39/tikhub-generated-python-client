from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/xiaohongshu/web/get_visitor_cookie",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ResponseModel]:
    if response.status_code == 200:
        response_200 = ResponseModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ResponseModel]:
    """获取游客Cookie/Get visitor cookie

     # [中文]
    ### 用途:
    - 获取小红书网页版的游客Cookie，可以用于爬取小红书的一些数据。
    ### 返回:
    - 游客Cookie

    # [English]
    ### Purpose:
    - Get Xiaohongshu web visitor cookie, which can be used to crawl some data of Xiaohongshu.
    ### Return:
    - Visitor cookie

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseModel]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[ResponseModel]:
    """获取游客Cookie/Get visitor cookie

     # [中文]
    ### 用途:
    - 获取小红书网页版的游客Cookie，可以用于爬取小红书的一些数据。
    ### 返回:
    - 游客Cookie

    # [English]
    ### Purpose:
    - Get Xiaohongshu web visitor cookie, which can be used to crawl some data of Xiaohongshu.
    ### Return:
    - Visitor cookie

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseModel
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ResponseModel]:
    """获取游客Cookie/Get visitor cookie

     # [中文]
    ### 用途:
    - 获取小红书网页版的游客Cookie，可以用于爬取小红书的一些数据。
    ### 返回:
    - 游客Cookie

    # [English]
    ### Purpose:
    - Get Xiaohongshu web visitor cookie, which can be used to crawl some data of Xiaohongshu.
    ### Return:
    - Visitor cookie

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponseModel]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[ResponseModel]:
    """获取游客Cookie/Get visitor cookie

     # [中文]
    ### 用途:
    - 获取小红书网页版的游客Cookie，可以用于爬取小红书的一些数据。
    ### 返回:
    - 游客Cookie

    # [English]
    ### Purpose:
    - Get Xiaohongshu web visitor cookie, which can be used to crawl some data of Xiaohongshu.
    ### Return:
    - Visitor cookie

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
