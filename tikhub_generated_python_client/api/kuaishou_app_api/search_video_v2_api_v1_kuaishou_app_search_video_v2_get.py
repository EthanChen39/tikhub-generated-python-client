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
    keyword: str,
    page: Union[Unset, str] = "1",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/kuaishou/app/search_video_v2",
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
    keyword: str,
    page: Union[Unset, str] = "1",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索视频V2/Search video V2

     # [中文]
    ### 用途:
    - 搜索视频 V2
    - 此接口收费较贵，但稳定性更高，具体价格请在用户后台查看价格表。
    ### 参数:
    - keyword: 搜索关键词
    - page: 视频页数，从1开始
    ### 返回:
    - 视频数据

    # [English]
    ### Purpose:
    - Search video V2
    - This API is more expensive, but more stable, please check the price list in the user background
    for specific prices.
    ### Parameters:
    - keyword: Search keyword
    - page: Page number, starting from 1
    ### Returns:
    - Videos data

    # [示例/Example]
    keyword = \"人工智能\"
    page = \"1\"

    Args:
        keyword (str):
        page (Union[Unset, str]):  Default: '1'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    keyword: str,
    page: Union[Unset, str] = "1",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索视频V2/Search video V2

     # [中文]
    ### 用途:
    - 搜索视频 V2
    - 此接口收费较贵，但稳定性更高，具体价格请在用户后台查看价格表。
    ### 参数:
    - keyword: 搜索关键词
    - page: 视频页数，从1开始
    ### 返回:
    - 视频数据

    # [English]
    ### Purpose:
    - Search video V2
    - This API is more expensive, but more stable, please check the price list in the user background
    for specific prices.
    ### Parameters:
    - keyword: Search keyword
    - page: Page number, starting from 1
    ### Returns:
    - Videos data

    # [示例/Example]
    keyword = \"人工智能\"
    page = \"1\"

    Args:
        keyword (str):
        page (Union[Unset, str]):  Default: '1'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        keyword=keyword,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    page: Union[Unset, str] = "1",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索视频V2/Search video V2

     # [中文]
    ### 用途:
    - 搜索视频 V2
    - 此接口收费较贵，但稳定性更高，具体价格请在用户后台查看价格表。
    ### 参数:
    - keyword: 搜索关键词
    - page: 视频页数，从1开始
    ### 返回:
    - 视频数据

    # [English]
    ### Purpose:
    - Search video V2
    - This API is more expensive, but more stable, please check the price list in the user background
    for specific prices.
    ### Parameters:
    - keyword: Search keyword
    - page: Page number, starting from 1
    ### Returns:
    - Videos data

    # [示例/Example]
    keyword = \"人工智能\"
    page = \"1\"

    Args:
        keyword (str):
        page (Union[Unset, str]):  Default: '1'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
    page: Union[Unset, str] = "1",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索视频V2/Search video V2

     # [中文]
    ### 用途:
    - 搜索视频 V2
    - 此接口收费较贵，但稳定性更高，具体价格请在用户后台查看价格表。
    ### 参数:
    - keyword: 搜索关键词
    - page: 视频页数，从1开始
    ### 返回:
    - 视频数据

    # [English]
    ### Purpose:
    - Search video V2
    - This API is more expensive, but more stable, please check the price list in the user background
    for specific prices.
    ### Parameters:
    - keyword: Search keyword
    - page: Page number, starting from 1
    ### Returns:
    - Videos data

    # [示例/Example]
    keyword = \"人工智能\"
    page = \"1\"

    Args:
        keyword (str):
        page (Union[Unset, str]):  Default: '1'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            keyword=keyword,
            page=page,
        )
    ).parsed
