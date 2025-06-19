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
    offset: Union[Unset, str] = "0",
    search_type: Union[Unset, str] = "1",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["offset"] = offset

    params["search_type"] = search_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/pipixia/app/fetch_search",
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
    offset: Union[Unset, str] = "0",
    search_type: Union[Unset, str] = "1",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索接口/Search API

     # [中文]
    ### 用途:
    - 搜索接口，支持搜索用户、作品等。
    ### 参数:
    - keyword: 搜索关键词。
    - offset: 翻页游标，默认为0，后续页码从上一页返回的 `offset` Key中获取对应值。
    - search_type: 搜索类型，可用值如下：
        - 1: 综合
        - 8: 热门
        - 9: 新鲜
        - 2：视频
        - 3：图文
        - 4：用户
        - 5：话题
    ### 返回:
    - 搜索结果

    # [English]
    ### Purpose:
    - Search API, support search user, post, etc.
    ### Parameters:
    - keyword: Search keyword.
    - offset: Page cursor, default is 0, get the corresponding value from the `offset` Key in the
    previous page.
    - search_type: Search type, available values are as follows:
        - 1: Comprehensive
        - 8: Hot
        - 9: Fresh
        - 2: Video
        - 3: Photo
        - 4: User
        - 5: Hashtag
    ### Return:
    - Search result

    # [示例/Example]
    keyword = \"皮皮虾\"
    offset = \"0\"
    search_type = \"1\"

    Args:
        keyword (str): 搜索关键词/Search keyword
        offset (Union[Unset, str]): 翻页游标/Page cursor Default: '0'.
        search_type (Union[Unset, str]): 搜索类型/Search type Default: '1'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        offset=offset,
        search_type=search_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    keyword: str,
    offset: Union[Unset, str] = "0",
    search_type: Union[Unset, str] = "1",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索接口/Search API

     # [中文]
    ### 用途:
    - 搜索接口，支持搜索用户、作品等。
    ### 参数:
    - keyword: 搜索关键词。
    - offset: 翻页游标，默认为0，后续页码从上一页返回的 `offset` Key中获取对应值。
    - search_type: 搜索类型，可用值如下：
        - 1: 综合
        - 8: 热门
        - 9: 新鲜
        - 2：视频
        - 3：图文
        - 4：用户
        - 5：话题
    ### 返回:
    - 搜索结果

    # [English]
    ### Purpose:
    - Search API, support search user, post, etc.
    ### Parameters:
    - keyword: Search keyword.
    - offset: Page cursor, default is 0, get the corresponding value from the `offset` Key in the
    previous page.
    - search_type: Search type, available values are as follows:
        - 1: Comprehensive
        - 8: Hot
        - 9: Fresh
        - 2: Video
        - 3: Photo
        - 4: User
        - 5: Hashtag
    ### Return:
    - Search result

    # [示例/Example]
    keyword = \"皮皮虾\"
    offset = \"0\"
    search_type = \"1\"

    Args:
        keyword (str): 搜索关键词/Search keyword
        offset (Union[Unset, str]): 翻页游标/Page cursor Default: '0'.
        search_type (Union[Unset, str]): 搜索类型/Search type Default: '1'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        keyword=keyword,
        offset=offset,
        search_type=search_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    offset: Union[Unset, str] = "0",
    search_type: Union[Unset, str] = "1",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索接口/Search API

     # [中文]
    ### 用途:
    - 搜索接口，支持搜索用户、作品等。
    ### 参数:
    - keyword: 搜索关键词。
    - offset: 翻页游标，默认为0，后续页码从上一页返回的 `offset` Key中获取对应值。
    - search_type: 搜索类型，可用值如下：
        - 1: 综合
        - 8: 热门
        - 9: 新鲜
        - 2：视频
        - 3：图文
        - 4：用户
        - 5：话题
    ### 返回:
    - 搜索结果

    # [English]
    ### Purpose:
    - Search API, support search user, post, etc.
    ### Parameters:
    - keyword: Search keyword.
    - offset: Page cursor, default is 0, get the corresponding value from the `offset` Key in the
    previous page.
    - search_type: Search type, available values are as follows:
        - 1: Comprehensive
        - 8: Hot
        - 9: Fresh
        - 2: Video
        - 3: Photo
        - 4: User
        - 5: Hashtag
    ### Return:
    - Search result

    # [示例/Example]
    keyword = \"皮皮虾\"
    offset = \"0\"
    search_type = \"1\"

    Args:
        keyword (str): 搜索关键词/Search keyword
        offset (Union[Unset, str]): 翻页游标/Page cursor Default: '0'.
        search_type (Union[Unset, str]): 搜索类型/Search type Default: '1'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        offset=offset,
        search_type=search_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
    offset: Union[Unset, str] = "0",
    search_type: Union[Unset, str] = "1",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索接口/Search API

     # [中文]
    ### 用途:
    - 搜索接口，支持搜索用户、作品等。
    ### 参数:
    - keyword: 搜索关键词。
    - offset: 翻页游标，默认为0，后续页码从上一页返回的 `offset` Key中获取对应值。
    - search_type: 搜索类型，可用值如下：
        - 1: 综合
        - 8: 热门
        - 9: 新鲜
        - 2：视频
        - 3：图文
        - 4：用户
        - 5：话题
    ### 返回:
    - 搜索结果

    # [English]
    ### Purpose:
    - Search API, support search user, post, etc.
    ### Parameters:
    - keyword: Search keyword.
    - offset: Page cursor, default is 0, get the corresponding value from the `offset` Key in the
    previous page.
    - search_type: Search type, available values are as follows:
        - 1: Comprehensive
        - 8: Hot
        - 9: Fresh
        - 2: Video
        - 3: Photo
        - 4: User
        - 5: Hashtag
    ### Return:
    - Search result

    # [示例/Example]
    keyword = \"皮皮虾\"
    offset = \"0\"
    search_type = \"1\"

    Args:
        keyword (str): 搜索关键词/Search keyword
        offset (Union[Unset, str]): 翻页游标/Page cursor Default: '0'.
        search_type (Union[Unset, str]): 搜索类型/Search type Default: '1'.

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
            offset=offset,
            search_type=search_type,
        )
    ).parsed
