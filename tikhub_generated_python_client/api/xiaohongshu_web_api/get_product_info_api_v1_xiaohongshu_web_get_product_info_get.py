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
    share_text: Union[Unset, str] = "",
    item_id: Union[Unset, str] = "",
    xsec_token: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["share_text"] = share_text

    params["item_id"] = item_id

    params["xsec_token"] = xsec_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/xiaohongshu/web/get_product_info",
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
    share_text: Union[Unset, str] = "",
    item_id: Union[Unset, str] = "",
    xsec_token: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取小红书商品信息/Get Xiaohongshu product info

     # [中文]
    ### 用途:
    - 通过分享链接获取小红书的商品信息
    ### 参数:
    - share_text: 小红书分享链接（支持APP和Web端分享链接）
    - item_id: 商品ID
    - xsec_token: X-Sec-Token
    - 如果share_text不为空，则item_id和xsec_token会被忽略
    - 如果share_text为空，则item_id和xsec_token不能为空
    ### 返回:
    - 商品信息

    # [English]
    ### Purpose:
    - Get Xiaohongshu product info by share link
    ### Parameters:
    - share_text: Xiaohongshu sharing link (support APP and Web sharing link)
    - item_id: Item ID
    - xsec_token: X-Sec-Token
    - If share_text is not empty, item_id and xsec_token will be ignored
    - If share_text is empty, item_id and xsec_token cannot be empty
    ### Return:
    - Product info

    # [示例/Example]
    item_id=\"65fc2e6d6b92310001d24efb\"
    xsec_token=\"XBC6LTqeaEDeJETMoXo436Eg-74GxFemVnNHeONYobv7k=\"

    Args:
        share_text (Union[Unset, str]): 分享链接/Share link Default: ''.
        item_id (Union[Unset, str]): 商品ID/Item ID Default: ''.
        xsec_token (Union[Unset, str]): X-Sec-Token Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        share_text=share_text,
        item_id=item_id,
        xsec_token=xsec_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    share_text: Union[Unset, str] = "",
    item_id: Union[Unset, str] = "",
    xsec_token: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取小红书商品信息/Get Xiaohongshu product info

     # [中文]
    ### 用途:
    - 通过分享链接获取小红书的商品信息
    ### 参数:
    - share_text: 小红书分享链接（支持APP和Web端分享链接）
    - item_id: 商品ID
    - xsec_token: X-Sec-Token
    - 如果share_text不为空，则item_id和xsec_token会被忽略
    - 如果share_text为空，则item_id和xsec_token不能为空
    ### 返回:
    - 商品信息

    # [English]
    ### Purpose:
    - Get Xiaohongshu product info by share link
    ### Parameters:
    - share_text: Xiaohongshu sharing link (support APP and Web sharing link)
    - item_id: Item ID
    - xsec_token: X-Sec-Token
    - If share_text is not empty, item_id and xsec_token will be ignored
    - If share_text is empty, item_id and xsec_token cannot be empty
    ### Return:
    - Product info

    # [示例/Example]
    item_id=\"65fc2e6d6b92310001d24efb\"
    xsec_token=\"XBC6LTqeaEDeJETMoXo436Eg-74GxFemVnNHeONYobv7k=\"

    Args:
        share_text (Union[Unset, str]): 分享链接/Share link Default: ''.
        item_id (Union[Unset, str]): 商品ID/Item ID Default: ''.
        xsec_token (Union[Unset, str]): X-Sec-Token Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        share_text=share_text,
        item_id=item_id,
        xsec_token=xsec_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    share_text: Union[Unset, str] = "",
    item_id: Union[Unset, str] = "",
    xsec_token: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取小红书商品信息/Get Xiaohongshu product info

     # [中文]
    ### 用途:
    - 通过分享链接获取小红书的商品信息
    ### 参数:
    - share_text: 小红书分享链接（支持APP和Web端分享链接）
    - item_id: 商品ID
    - xsec_token: X-Sec-Token
    - 如果share_text不为空，则item_id和xsec_token会被忽略
    - 如果share_text为空，则item_id和xsec_token不能为空
    ### 返回:
    - 商品信息

    # [English]
    ### Purpose:
    - Get Xiaohongshu product info by share link
    ### Parameters:
    - share_text: Xiaohongshu sharing link (support APP and Web sharing link)
    - item_id: Item ID
    - xsec_token: X-Sec-Token
    - If share_text is not empty, item_id and xsec_token will be ignored
    - If share_text is empty, item_id and xsec_token cannot be empty
    ### Return:
    - Product info

    # [示例/Example]
    item_id=\"65fc2e6d6b92310001d24efb\"
    xsec_token=\"XBC6LTqeaEDeJETMoXo436Eg-74GxFemVnNHeONYobv7k=\"

    Args:
        share_text (Union[Unset, str]): 分享链接/Share link Default: ''.
        item_id (Union[Unset, str]): 商品ID/Item ID Default: ''.
        xsec_token (Union[Unset, str]): X-Sec-Token Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        share_text=share_text,
        item_id=item_id,
        xsec_token=xsec_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    share_text: Union[Unset, str] = "",
    item_id: Union[Unset, str] = "",
    xsec_token: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取小红书商品信息/Get Xiaohongshu product info

     # [中文]
    ### 用途:
    - 通过分享链接获取小红书的商品信息
    ### 参数:
    - share_text: 小红书分享链接（支持APP和Web端分享链接）
    - item_id: 商品ID
    - xsec_token: X-Sec-Token
    - 如果share_text不为空，则item_id和xsec_token会被忽略
    - 如果share_text为空，则item_id和xsec_token不能为空
    ### 返回:
    - 商品信息

    # [English]
    ### Purpose:
    - Get Xiaohongshu product info by share link
    ### Parameters:
    - share_text: Xiaohongshu sharing link (support APP and Web sharing link)
    - item_id: Item ID
    - xsec_token: X-Sec-Token
    - If share_text is not empty, item_id and xsec_token will be ignored
    - If share_text is empty, item_id and xsec_token cannot be empty
    ### Return:
    - Product info

    # [示例/Example]
    item_id=\"65fc2e6d6b92310001d24efb\"
    xsec_token=\"XBC6LTqeaEDeJETMoXo436Eg-74GxFemVnNHeONYobv7k=\"

    Args:
        share_text (Union[Unset, str]): 分享链接/Share link Default: ''.
        item_id (Union[Unset, str]): 商品ID/Item ID Default: ''.
        xsec_token (Union[Unset, str]): X-Sec-Token Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            share_text=share_text,
            item_id=item_id,
            xsec_token=xsec_token,
        )
    ).parsed
