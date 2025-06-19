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
    url_query: str,
    minimal: Union[Unset, bool] = False,
    base64_url: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["url"] = url_query

    params["minimal"] = minimal

    params["base64_url"] = base64_url

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/hybrid/video_data",
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
    minimal: Union[Unset, bool] = False,
    base64_url: Union[Unset, bool] = False,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""混合解析单一视频接口/Hybrid parsing single video endpoint

     # [中文]
    ### 用途:
    - 该接口用于解析抖音/TikTok单一视频的数据。
    ### 参数:
    - `url`: 视频链接、分享链接、分享文本。
    ### 返回:
    - `data`: 视频数据。

    # [English]
    ### Purpose:
    - This endpoint is used to parse data of a single Douyin/TikTok video.
    ### Parameters:
    - `url`: Video link, share link, or share text.
    ### Returns:
    - `data`: Video data.

    # [Example]
    url = \"https://v.douyin.com/L4FJNR3/\"

    Args:
        url_query (str):
        minimal (Union[Unset, bool]): 是否返回最小数据/Whether to return minimal data Default: False.
        base64_url (Union[Unset, bool]): 是否Base64编码提交URL/Base64 encoding URL Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        url_query=url_query,
        minimal=minimal,
        base64_url=base64_url,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    url_query: str,
    minimal: Union[Unset, bool] = False,
    base64_url: Union[Unset, bool] = False,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""混合解析单一视频接口/Hybrid parsing single video endpoint

     # [中文]
    ### 用途:
    - 该接口用于解析抖音/TikTok单一视频的数据。
    ### 参数:
    - `url`: 视频链接、分享链接、分享文本。
    ### 返回:
    - `data`: 视频数据。

    # [English]
    ### Purpose:
    - This endpoint is used to parse data of a single Douyin/TikTok video.
    ### Parameters:
    - `url`: Video link, share link, or share text.
    ### Returns:
    - `data`: Video data.

    # [Example]
    url = \"https://v.douyin.com/L4FJNR3/\"

    Args:
        url_query (str):
        minimal (Union[Unset, bool]): 是否返回最小数据/Whether to return minimal data Default: False.
        base64_url (Union[Unset, bool]): 是否Base64编码提交URL/Base64 encoding URL Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        url_query=url_query,
        minimal=minimal,
        base64_url=base64_url,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    url_query: str,
    minimal: Union[Unset, bool] = False,
    base64_url: Union[Unset, bool] = False,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""混合解析单一视频接口/Hybrid parsing single video endpoint

     # [中文]
    ### 用途:
    - 该接口用于解析抖音/TikTok单一视频的数据。
    ### 参数:
    - `url`: 视频链接、分享链接、分享文本。
    ### 返回:
    - `data`: 视频数据。

    # [English]
    ### Purpose:
    - This endpoint is used to parse data of a single Douyin/TikTok video.
    ### Parameters:
    - `url`: Video link, share link, or share text.
    ### Returns:
    - `data`: Video data.

    # [Example]
    url = \"https://v.douyin.com/L4FJNR3/\"

    Args:
        url_query (str):
        minimal (Union[Unset, bool]): 是否返回最小数据/Whether to return minimal data Default: False.
        base64_url (Union[Unset, bool]): 是否Base64编码提交URL/Base64 encoding URL Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        url_query=url_query,
        minimal=minimal,
        base64_url=base64_url,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    url_query: str,
    minimal: Union[Unset, bool] = False,
    base64_url: Union[Unset, bool] = False,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""混合解析单一视频接口/Hybrid parsing single video endpoint

     # [中文]
    ### 用途:
    - 该接口用于解析抖音/TikTok单一视频的数据。
    ### 参数:
    - `url`: 视频链接、分享链接、分享文本。
    ### 返回:
    - `data`: 视频数据。

    # [English]
    ### Purpose:
    - This endpoint is used to parse data of a single Douyin/TikTok video.
    ### Parameters:
    - `url`: Video link, share link, or share text.
    ### Returns:
    - `data`: Video data.

    # [Example]
    url = \"https://v.douyin.com/L4FJNR3/\"

    Args:
        url_query (str):
        minimal (Union[Unset, bool]): 是否返回最小数据/Whether to return minimal data Default: False.
        base64_url (Union[Unset, bool]): 是否Base64编码提交URL/Base64 encoding URL Default: False.

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
            minimal=minimal,
            base64_url=base64_url,
        )
    ).parsed
