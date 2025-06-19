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
    search_type: Union[Unset, str] = "Top",
    cursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["search_type"] = search_type

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/twitter/web/fetch_search_timeline",
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
    search_type: Union[Unset, str] = "Top",
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索/Search

     # [中文]
    ### 用途:
    - 搜索
    ### 参数:
    - keyword: 搜索关键字
    - search_type: 搜索类型，默认为Top，其他可选值为Latest，Media，People, Lists
    - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取
    ### 返回:
    - 搜索结果

    # [English]
    ### Purpose:
    - Search
    ### Parameters:
    - keyword: Search keyword
    - search_type: Search type, default is Top, other optional values are Latest, Media, People, Lists
    - cursor: Cursor, default is None, used for paging, obtained from the last request
    ### Return:
    - Search results

    # [示例/Example]
    keyword = \"Elon Musk\"
    search_type = \"Top\"
    cursor = None

    Args:
        keyword (str): 搜索关键字/Search Keyword
        search_type (Union[Unset, str]): 搜索类型/Search Type Default: 'Top'.
        cursor (Union[Unset, str]): 游标/Cursor

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        search_type=search_type,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    keyword: str,
    search_type: Union[Unset, str] = "Top",
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索/Search

     # [中文]
    ### 用途:
    - 搜索
    ### 参数:
    - keyword: 搜索关键字
    - search_type: 搜索类型，默认为Top，其他可选值为Latest，Media，People, Lists
    - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取
    ### 返回:
    - 搜索结果

    # [English]
    ### Purpose:
    - Search
    ### Parameters:
    - keyword: Search keyword
    - search_type: Search type, default is Top, other optional values are Latest, Media, People, Lists
    - cursor: Cursor, default is None, used for paging, obtained from the last request
    ### Return:
    - Search results

    # [示例/Example]
    keyword = \"Elon Musk\"
    search_type = \"Top\"
    cursor = None

    Args:
        keyword (str): 搜索关键字/Search Keyword
        search_type (Union[Unset, str]): 搜索类型/Search Type Default: 'Top'.
        cursor (Union[Unset, str]): 游标/Cursor

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        keyword=keyword,
        search_type=search_type,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    search_type: Union[Unset, str] = "Top",
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索/Search

     # [中文]
    ### 用途:
    - 搜索
    ### 参数:
    - keyword: 搜索关键字
    - search_type: 搜索类型，默认为Top，其他可选值为Latest，Media，People, Lists
    - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取
    ### 返回:
    - 搜索结果

    # [English]
    ### Purpose:
    - Search
    ### Parameters:
    - keyword: Search keyword
    - search_type: Search type, default is Top, other optional values are Latest, Media, People, Lists
    - cursor: Cursor, default is None, used for paging, obtained from the last request
    ### Return:
    - Search results

    # [示例/Example]
    keyword = \"Elon Musk\"
    search_type = \"Top\"
    cursor = None

    Args:
        keyword (str): 搜索关键字/Search Keyword
        search_type (Union[Unset, str]): 搜索类型/Search Type Default: 'Top'.
        cursor (Union[Unset, str]): 游标/Cursor

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        search_type=search_type,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
    search_type: Union[Unset, str] = "Top",
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索/Search

     # [中文]
    ### 用途:
    - 搜索
    ### 参数:
    - keyword: 搜索关键字
    - search_type: 搜索类型，默认为Top，其他可选值为Latest，Media，People, Lists
    - cursor: 游标，默认为None，用于翻页，后续从上一次请求的返回结果中获取
    ### 返回:
    - 搜索结果

    # [English]
    ### Purpose:
    - Search
    ### Parameters:
    - keyword: Search keyword
    - search_type: Search type, default is Top, other optional values are Latest, Media, People, Lists
    - cursor: Cursor, default is None, used for paging, obtained from the last request
    ### Return:
    - Search results

    # [示例/Example]
    keyword = \"Elon Musk\"
    search_type = \"Top\"
    cursor = None

    Args:
        keyword (str): 搜索关键字/Search Keyword
        search_type (Union[Unset, str]): 搜索类型/Search Type Default: 'Top'.
        cursor (Union[Unset, str]): 游标/Cursor

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
            search_type=search_type,
            cursor=cursor,
        )
    ).parsed
