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
    url_query: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["url"] = url_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/wechat_mp/web/fetch_mp_article_ad",
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
    url_query: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取微信公众号广告/Get Wechat MP Article Ad

     # [中文]
    ### 用途:
    - 获取微信公众号广告
    ### 参数:
    - url: 文章链接
    ### 返回:
    - 广告

    # [English]
    ### Purpose:
    - Get Wechat MP Article Ad
    ### Parameters:
    - url: Article URL
    ### Returns:
    - Ad

    # [示例/Example]
    url = \"https://mp.weixin.qq.com/s/hrTDuwh0pWyJFYC93kKCrg\"

    Args:
        url_query (str): 文章链接/Article URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        url_query=url_query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    url_query: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取微信公众号广告/Get Wechat MP Article Ad

     # [中文]
    ### 用途:
    - 获取微信公众号广告
    ### 参数:
    - url: 文章链接
    ### 返回:
    - 广告

    # [English]
    ### Purpose:
    - Get Wechat MP Article Ad
    ### Parameters:
    - url: Article URL
    ### Returns:
    - Ad

    # [示例/Example]
    url = \"https://mp.weixin.qq.com/s/hrTDuwh0pWyJFYC93kKCrg\"

    Args:
        url_query (str): 文章链接/Article URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        url_query=url_query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    url_query: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取微信公众号广告/Get Wechat MP Article Ad

     # [中文]
    ### 用途:
    - 获取微信公众号广告
    ### 参数:
    - url: 文章链接
    ### 返回:
    - 广告

    # [English]
    ### Purpose:
    - Get Wechat MP Article Ad
    ### Parameters:
    - url: Article URL
    ### Returns:
    - Ad

    # [示例/Example]
    url = \"https://mp.weixin.qq.com/s/hrTDuwh0pWyJFYC93kKCrg\"

    Args:
        url_query (str): 文章链接/Article URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        url_query=url_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    url_query: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取微信公众号广告/Get Wechat MP Article Ad

     # [中文]
    ### 用途:
    - 获取微信公众号广告
    ### 参数:
    - url: 文章链接
    ### 返回:
    - 广告

    # [English]
    ### Purpose:
    - Get Wechat MP Article Ad
    ### Parameters:
    - url: Article URL
    ### Returns:
    - Ad

    # [示例/Example]
    url = \"https://mp.weixin.qq.com/s/hrTDuwh0pWyJFYC93kKCrg\"

    Args:
        url_query (str): 文章链接/Article URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            url_query=url_query,
        )
    ).parsed
