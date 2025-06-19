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
    page: Union[Unset, int] = 1,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/xiaohongshu/web/search_users",
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
    page: Union[Unset, int] = 1,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索用户/Search users

     # [中文]
    ### 用途:
    - 搜索用户
    ### 参数:
    - keyword: 搜索关键词
    - page: 页码，默认为1
    ### 返回:
    - 用户列表

    # [English]
    ### Purpose:
    - Search users
    ### Parameters:
    - keyword: Keyword
    - page: Page, default is 1
    ### Return:
    - User list

    # [示例/Example]
    keyword=\"美食\"
    page=1

    Args:
        keyword (str): 搜索关键词/Keyword
        page (Union[Unset, int]): 页码/Page Default: 1.

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
    page: Union[Unset, int] = 1,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索用户/Search users

     # [中文]
    ### 用途:
    - 搜索用户
    ### 参数:
    - keyword: 搜索关键词
    - page: 页码，默认为1
    ### 返回:
    - 用户列表

    # [English]
    ### Purpose:
    - Search users
    ### Parameters:
    - keyword: Keyword
    - page: Page, default is 1
    ### Return:
    - User list

    # [示例/Example]
    keyword=\"美食\"
    page=1

    Args:
        keyword (str): 搜索关键词/Keyword
        page (Union[Unset, int]): 页码/Page Default: 1.

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
    page: Union[Unset, int] = 1,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索用户/Search users

     # [中文]
    ### 用途:
    - 搜索用户
    ### 参数:
    - keyword: 搜索关键词
    - page: 页码，默认为1
    ### 返回:
    - 用户列表

    # [English]
    ### Purpose:
    - Search users
    ### Parameters:
    - keyword: Keyword
    - page: Page, default is 1
    ### Return:
    - User list

    # [示例/Example]
    keyword=\"美食\"
    page=1

    Args:
        keyword (str): 搜索关键词/Keyword
        page (Union[Unset, int]): 页码/Page Default: 1.

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
    page: Union[Unset, int] = 1,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索用户/Search users

     # [中文]
    ### 用途:
    - 搜索用户
    ### 参数:
    - keyword: 搜索关键词
    - page: 页码，默认为1
    ### 返回:
    - 用户列表

    # [English]
    ### Purpose:
    - Search users
    ### Parameters:
    - keyword: Keyword
    - page: Page, default is 1
    ### Return:
    - User list

    # [示例/Example]
    keyword=\"美食\"
    page=1

    Args:
        keyword (str): 搜索关键词/Keyword
        page (Union[Unset, int]): 页码/Page Default: 1.

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
