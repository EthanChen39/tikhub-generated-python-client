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
    short_url: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["short_url"] = short_url

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/xiaohongshu/web_v2/fetch_feed_notes_v3",
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
    short_url: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单一笔记和推荐笔记 V3/Fetch one note and feed notes V3(通过短链获取笔记详情)

     # [中文]
    ### 用途:
    - 获取单一笔记和推荐笔记
    ### 参数:
    - short_url: 短链，可以从小红书的分享链接中获取
    ### 返回:
    - 单一笔记和推荐笔记

    # [English]
    ### Purpose:
    - Get one note and feed notes
    ### Parameters:
    - short_url: Short URL, can be obtained from the sharing link of Xiaohongshu website.
    ### Return:
    - One note and feed notes

    # [示例/Example]
    short_url = \"http://xhslink.com/a/tyoREa3ciaAeb\"

    Args:
        short_url (str): 短链/Short URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        short_url=short_url,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    short_url: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单一笔记和推荐笔记 V3/Fetch one note and feed notes V3(通过短链获取笔记详情)

     # [中文]
    ### 用途:
    - 获取单一笔记和推荐笔记
    ### 参数:
    - short_url: 短链，可以从小红书的分享链接中获取
    ### 返回:
    - 单一笔记和推荐笔记

    # [English]
    ### Purpose:
    - Get one note and feed notes
    ### Parameters:
    - short_url: Short URL, can be obtained from the sharing link of Xiaohongshu website.
    ### Return:
    - One note and feed notes

    # [示例/Example]
    short_url = \"http://xhslink.com/a/tyoREa3ciaAeb\"

    Args:
        short_url (str): 短链/Short URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        short_url=short_url,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    short_url: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单一笔记和推荐笔记 V3/Fetch one note and feed notes V3(通过短链获取笔记详情)

     # [中文]
    ### 用途:
    - 获取单一笔记和推荐笔记
    ### 参数:
    - short_url: 短链，可以从小红书的分享链接中获取
    ### 返回:
    - 单一笔记和推荐笔记

    # [English]
    ### Purpose:
    - Get one note and feed notes
    ### Parameters:
    - short_url: Short URL, can be obtained from the sharing link of Xiaohongshu website.
    ### Return:
    - One note and feed notes

    # [示例/Example]
    short_url = \"http://xhslink.com/a/tyoREa3ciaAeb\"

    Args:
        short_url (str): 短链/Short URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        short_url=short_url,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    short_url: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取单一笔记和推荐笔记 V3/Fetch one note and feed notes V3(通过短链获取笔记详情)

     # [中文]
    ### 用途:
    - 获取单一笔记和推荐笔记
    ### 参数:
    - short_url: 短链，可以从小红书的分享链接中获取
    ### 返回:
    - 单一笔记和推荐笔记

    # [English]
    ### Purpose:
    - Get one note and feed notes
    ### Parameters:
    - short_url: Short URL, can be obtained from the sharing link of Xiaohongshu website.
    ### Return:
    - One note and feed notes

    # [示例/Example]
    short_url = \"http://xhslink.com/a/tyoREa3ciaAeb\"

    Args:
        short_url (str): 短链/Short URL

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            short_url=short_url,
        )
    ).parsed
