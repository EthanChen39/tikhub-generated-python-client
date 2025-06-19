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
    search_query: str,
    language_code: Union[Unset, str] = "en",
    order_by: Union[Unset, str] = "this_month",
    country_code: Union[Unset, str] = "us",
    continuation_token: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["search_query"] = search_query

    params["language_code"] = language_code

    params["order_by"] = order_by

    params["country_code"] = country_code

    params["continuation_token"] = continuation_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/youtube/web/search_video",
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
    search_query: str,
    language_code: Union[Unset, str] = "en",
    order_by: Union[Unset, str] = "this_month",
    country_code: Union[Unset, str] = "us",
    continuation_token: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索视频/Search video

     # [中文]
    ### 用途:
    - 搜索视频。
    ### 参数:
    - search_query: 搜索关键字。
    - language_code: 语言代码，默认为en。
    - order_by: 排序方式，默��为this_month。
    - country_code: 国家代码，默认为us。
    - continuation_token: 用于继续获取搜索结果的令牌。默认为None。
    ### 返回:
    - 搜索结果。

    # [English]
    ### Purpose:
    - Search video.
    ### Parameters:
    - search_query: Search keyword.
    - language_code: Language code, default is en.
    - order_by: Order by, default is this_month.
    - country_code: Country code, default is us.
    - continuation_token: Token to continue fetching search results. Default is None.
    ### Returns:
    - Search results.

    # [示例/Example]
    search_query = \"Minecraft\"

    Args:
        search_query (str): 搜索关键字/Search keyword
        language_code (Union[Unset, str]): 语言代码/Language code Default: 'en'.
        order_by (Union[Unset, str]): 排序方式/Order by Default: 'this_month'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'us'.
        continuation_token (Union[Unset, str]): 翻页令牌/Pagination token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        search_query=search_query,
        language_code=language_code,
        order_by=order_by,
        country_code=country_code,
        continuation_token=continuation_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    search_query: str,
    language_code: Union[Unset, str] = "en",
    order_by: Union[Unset, str] = "this_month",
    country_code: Union[Unset, str] = "us",
    continuation_token: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索视频/Search video

     # [中文]
    ### 用途:
    - 搜索视频。
    ### 参数:
    - search_query: 搜索关键字。
    - language_code: 语言代码，默认为en。
    - order_by: 排序方式，默��为this_month。
    - country_code: 国家代码，默认为us。
    - continuation_token: 用于继续获取搜索结果的令牌。默认为None。
    ### 返回:
    - 搜索结果。

    # [English]
    ### Purpose:
    - Search video.
    ### Parameters:
    - search_query: Search keyword.
    - language_code: Language code, default is en.
    - order_by: Order by, default is this_month.
    - country_code: Country code, default is us.
    - continuation_token: Token to continue fetching search results. Default is None.
    ### Returns:
    - Search results.

    # [示例/Example]
    search_query = \"Minecraft\"

    Args:
        search_query (str): 搜索关键字/Search keyword
        language_code (Union[Unset, str]): 语言代码/Language code Default: 'en'.
        order_by (Union[Unset, str]): 排序方式/Order by Default: 'this_month'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'us'.
        continuation_token (Union[Unset, str]): 翻页令牌/Pagination token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        search_query=search_query,
        language_code=language_code,
        order_by=order_by,
        country_code=country_code,
        continuation_token=continuation_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    search_query: str,
    language_code: Union[Unset, str] = "en",
    order_by: Union[Unset, str] = "this_month",
    country_code: Union[Unset, str] = "us",
    continuation_token: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索视频/Search video

     # [中文]
    ### 用途:
    - 搜索视频。
    ### 参数:
    - search_query: 搜索关键字。
    - language_code: 语言代码，默认为en。
    - order_by: 排序方式，默��为this_month。
    - country_code: 国家代码，默认为us。
    - continuation_token: 用于继续获取搜索结果的令牌。默认为None。
    ### 返回:
    - 搜索结果。

    # [English]
    ### Purpose:
    - Search video.
    ### Parameters:
    - search_query: Search keyword.
    - language_code: Language code, default is en.
    - order_by: Order by, default is this_month.
    - country_code: Country code, default is us.
    - continuation_token: Token to continue fetching search results. Default is None.
    ### Returns:
    - Search results.

    # [示例/Example]
    search_query = \"Minecraft\"

    Args:
        search_query (str): 搜索关键字/Search keyword
        language_code (Union[Unset, str]): 语言代码/Language code Default: 'en'.
        order_by (Union[Unset, str]): 排序方式/Order by Default: 'this_month'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'us'.
        continuation_token (Union[Unset, str]): 翻页令牌/Pagination token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        search_query=search_query,
        language_code=language_code,
        order_by=order_by,
        country_code=country_code,
        continuation_token=continuation_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    search_query: str,
    language_code: Union[Unset, str] = "en",
    order_by: Union[Unset, str] = "this_month",
    country_code: Union[Unset, str] = "us",
    continuation_token: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索视频/Search video

     # [中文]
    ### 用途:
    - 搜索视频。
    ### 参数:
    - search_query: 搜索关键字。
    - language_code: 语言代码，默认为en。
    - order_by: 排序方式，默��为this_month。
    - country_code: 国家代码，默认为us。
    - continuation_token: 用于继续获取搜索结果的令牌。默认为None。
    ### 返回:
    - 搜索结果。

    # [English]
    ### Purpose:
    - Search video.
    ### Parameters:
    - search_query: Search keyword.
    - language_code: Language code, default is en.
    - order_by: Order by, default is this_month.
    - country_code: Country code, default is us.
    - continuation_token: Token to continue fetching search results. Default is None.
    ### Returns:
    - Search results.

    # [示例/Example]
    search_query = \"Minecraft\"

    Args:
        search_query (str): 搜索关键字/Search keyword
        language_code (Union[Unset, str]): 语言代码/Language code Default: 'en'.
        order_by (Union[Unset, str]): 排序方式/Order by Default: 'this_month'.
        country_code (Union[Unset, str]): 国家代码/Country code Default: 'us'.
        continuation_token (Union[Unset, str]): 翻页令牌/Pagination token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            search_query=search_query,
            language_code=language_code,
            order_by=order_by,
            country_code=country_code,
            continuation_token=continuation_token,
        )
    ).parsed
