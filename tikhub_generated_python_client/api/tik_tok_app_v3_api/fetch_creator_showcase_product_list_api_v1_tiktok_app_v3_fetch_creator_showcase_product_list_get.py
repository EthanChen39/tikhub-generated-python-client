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
    kol_id: str,
    count: Union[Unset, int] = 20,
    next_scroll_param: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["kol_id"] = kol_id

    params["count"] = count

    params["next_scroll_param"] = next_scroll_param

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/app/v3/fetch_creator_showcase_product_list",
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
    kol_id: str,
    count: Union[Unset, int] = 20,
    next_scroll_param: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者橱窗商品列表/Get creator showcase product list

     # [中文]
    ### 用途:
    - 获取创作者橱窗商品列表
    ### 参数:
    - kol_id: 创作者的sec_user_id
    - count: 数量
    - next_scroll_param: 翻页参数，第一页为空字符串，后续请求使用上一次请求返回的next_scroll_param值。
    ### 返回:
    - 创作者橱窗商品列表

    # [English]
    ### Purpose:
    - Get creator showcase product list
    ### Parameters:
    - kol_id: Creator's sec_user_id
    - count: Number
    - next_scroll_param: Page parameter, empty string for the first page, use the next_scroll_param
    value returned by the last request for subsequent requests.
    ### Return:
    - Creator showcase product list

    # [示例/Example]
    kol_id = \"MS4wLjABAAAARujvKaVWqgbVCwuxQghA99TUa5I-4g6jVzMXZd9FJIXSdJwJM47vm4-2T1K3gsux\"
    count = 20
    next_scroll_param = \"\"

    Args:
        kol_id (str): 创作者的sec_user_id/Creator's sec_user_id
        count (Union[Unset, int]): 数量/Number Default: 20.
        next_scroll_param (Union[Unset, str]): 翻页参数/Page parameter Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        kol_id=kol_id,
        count=count,
        next_scroll_param=next_scroll_param,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    kol_id: str,
    count: Union[Unset, int] = 20,
    next_scroll_param: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者橱窗商品列表/Get creator showcase product list

     # [中文]
    ### 用途:
    - 获取创作者橱窗商品列表
    ### 参数:
    - kol_id: 创作者的sec_user_id
    - count: 数量
    - next_scroll_param: 翻页参数，第一页为空字符串，后续请求使用上一次请求返回的next_scroll_param值。
    ### 返回:
    - 创作者橱窗商品列表

    # [English]
    ### Purpose:
    - Get creator showcase product list
    ### Parameters:
    - kol_id: Creator's sec_user_id
    - count: Number
    - next_scroll_param: Page parameter, empty string for the first page, use the next_scroll_param
    value returned by the last request for subsequent requests.
    ### Return:
    - Creator showcase product list

    # [示例/Example]
    kol_id = \"MS4wLjABAAAARujvKaVWqgbVCwuxQghA99TUa5I-4g6jVzMXZd9FJIXSdJwJM47vm4-2T1K3gsux\"
    count = 20
    next_scroll_param = \"\"

    Args:
        kol_id (str): 创作者的sec_user_id/Creator's sec_user_id
        count (Union[Unset, int]): 数量/Number Default: 20.
        next_scroll_param (Union[Unset, str]): 翻页参数/Page parameter Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        kol_id=kol_id,
        count=count,
        next_scroll_param=next_scroll_param,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    kol_id: str,
    count: Union[Unset, int] = 20,
    next_scroll_param: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者橱窗商品列表/Get creator showcase product list

     # [中文]
    ### 用途:
    - 获取创作者橱窗商品列表
    ### 参数:
    - kol_id: 创作者的sec_user_id
    - count: 数量
    - next_scroll_param: 翻页参数，第一页为空字符串，后续请求使用上一次请求返回的next_scroll_param值。
    ### 返回:
    - 创作者橱窗商品列表

    # [English]
    ### Purpose:
    - Get creator showcase product list
    ### Parameters:
    - kol_id: Creator's sec_user_id
    - count: Number
    - next_scroll_param: Page parameter, empty string for the first page, use the next_scroll_param
    value returned by the last request for subsequent requests.
    ### Return:
    - Creator showcase product list

    # [示例/Example]
    kol_id = \"MS4wLjABAAAARujvKaVWqgbVCwuxQghA99TUa5I-4g6jVzMXZd9FJIXSdJwJM47vm4-2T1K3gsux\"
    count = 20
    next_scroll_param = \"\"

    Args:
        kol_id (str): 创作者的sec_user_id/Creator's sec_user_id
        count (Union[Unset, int]): 数量/Number Default: 20.
        next_scroll_param (Union[Unset, str]): 翻页参数/Page parameter Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        kol_id=kol_id,
        count=count,
        next_scroll_param=next_scroll_param,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    kol_id: str,
    count: Union[Unset, int] = 20,
    next_scroll_param: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者橱窗商品列表/Get creator showcase product list

     # [中文]
    ### 用途:
    - 获取创作者橱窗商品列表
    ### 参数:
    - kol_id: 创作者的sec_user_id
    - count: 数量
    - next_scroll_param: 翻页参数，第一页为空字符串，后续请求使用上一次请求返回的next_scroll_param值。
    ### 返回:
    - 创作者橱窗商品列表

    # [English]
    ### Purpose:
    - Get creator showcase product list
    ### Parameters:
    - kol_id: Creator's sec_user_id
    - count: Number
    - next_scroll_param: Page parameter, empty string for the first page, use the next_scroll_param
    value returned by the last request for subsequent requests.
    ### Return:
    - Creator showcase product list

    # [示例/Example]
    kol_id = \"MS4wLjABAAAARujvKaVWqgbVCwuxQghA99TUa5I-4g6jVzMXZd9FJIXSdJwJM47vm4-2T1K3gsux\"
    count = 20
    next_scroll_param = \"\"

    Args:
        kol_id (str): 创作者的sec_user_id/Creator's sec_user_id
        count (Union[Unset, int]): 数量/Number Default: 20.
        next_scroll_param (Union[Unset, str]): 翻页参数/Page parameter Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            kol_id=kol_id,
            count=count,
            next_scroll_param=next_scroll_param,
        )
    ).parsed
