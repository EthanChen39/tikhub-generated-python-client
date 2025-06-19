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
    search_type: Union[Unset, str] = "1",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["page"] = page

    params["search_type"] = search_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/weibo/web/fetch_search_data",
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
    search_type: Union[Unset, str] = "1",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取搜索数据/Get search data

     # [中文]
    ### 用途:
    - 获取搜索数据
    ### 参数:
    - keyword: 关键词
    - page: 页数
    - search_type: 搜索类型
        - **1**: 综合
        - **61**: 实时
        - **3**: 用户
        - **60**: 热门
        - **64**: 视频
        - **63**: 图片
        - **21**: 文章
        - **38**: 话题
        - **98**: 超话
    ### 返回:
    - 搜索数据

    # [English]
    ### Purpose:
    - Get search data
    ### Parameters:
    - keyword: Keyword
    - page: Page number
    - search_type: Search type
        - **1**: Comprehensive
        - **61**: Real-time
        - **3**: User
        - **60**: Hot
        - **64**: Video
        - **63**: Picture
        - **21**: Article
        - **38**: Topic
        - **98**: Super topic
    ### Return:
    - Search data

    # [示例/Example]
    keyword = \"游戏\"
    page = \"1\"
    search_type = \"1\"

    Args:
        keyword (str): 关键词/Keyword
        page (Union[Unset, str]): 页数/Page number Default: '1'.
        search_type (Union[Unset, str]): 搜索类型/Search type Default: '1'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        page=page,
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
    page: Union[Unset, str] = "1",
    search_type: Union[Unset, str] = "1",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取搜索数据/Get search data

     # [中文]
    ### 用途:
    - 获取搜索数据
    ### 参数:
    - keyword: 关键词
    - page: 页数
    - search_type: 搜索类型
        - **1**: 综合
        - **61**: 实时
        - **3**: 用户
        - **60**: 热门
        - **64**: 视频
        - **63**: 图片
        - **21**: 文章
        - **38**: 话题
        - **98**: 超话
    ### 返回:
    - 搜索数据

    # [English]
    ### Purpose:
    - Get search data
    ### Parameters:
    - keyword: Keyword
    - page: Page number
    - search_type: Search type
        - **1**: Comprehensive
        - **61**: Real-time
        - **3**: User
        - **60**: Hot
        - **64**: Video
        - **63**: Picture
        - **21**: Article
        - **38**: Topic
        - **98**: Super topic
    ### Return:
    - Search data

    # [示例/Example]
    keyword = \"游戏\"
    page = \"1\"
    search_type = \"1\"

    Args:
        keyword (str): 关键词/Keyword
        page (Union[Unset, str]): 页数/Page number Default: '1'.
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
        page=page,
        search_type=search_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    page: Union[Unset, str] = "1",
    search_type: Union[Unset, str] = "1",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取搜索数据/Get search data

     # [中文]
    ### 用途:
    - 获取搜索数据
    ### 参数:
    - keyword: 关键词
    - page: 页数
    - search_type: 搜索类型
        - **1**: 综合
        - **61**: 实时
        - **3**: 用户
        - **60**: 热门
        - **64**: 视频
        - **63**: 图片
        - **21**: 文章
        - **38**: 话题
        - **98**: 超话
    ### 返回:
    - 搜索数据

    # [English]
    ### Purpose:
    - Get search data
    ### Parameters:
    - keyword: Keyword
    - page: Page number
    - search_type: Search type
        - **1**: Comprehensive
        - **61**: Real-time
        - **3**: User
        - **60**: Hot
        - **64**: Video
        - **63**: Picture
        - **21**: Article
        - **38**: Topic
        - **98**: Super topic
    ### Return:
    - Search data

    # [示例/Example]
    keyword = \"游戏\"
    page = \"1\"
    search_type = \"1\"

    Args:
        keyword (str): 关键词/Keyword
        page (Union[Unset, str]): 页数/Page number Default: '1'.
        search_type (Union[Unset, str]): 搜索类型/Search type Default: '1'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        page=page,
        search_type=search_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
    page: Union[Unset, str] = "1",
    search_type: Union[Unset, str] = "1",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取搜索数据/Get search data

     # [中文]
    ### 用途:
    - 获取搜索数据
    ### 参数:
    - keyword: 关键词
    - page: 页数
    - search_type: 搜索类型
        - **1**: 综合
        - **61**: 实时
        - **3**: 用户
        - **60**: 热门
        - **64**: 视频
        - **63**: 图片
        - **21**: 文章
        - **38**: 话题
        - **98**: 超话
    ### 返回:
    - 搜索数据

    # [English]
    ### Purpose:
    - Get search data
    ### Parameters:
    - keyword: Keyword
    - page: Page number
    - search_type: Search type
        - **1**: Comprehensive
        - **61**: Real-time
        - **3**: User
        - **60**: Hot
        - **64**: Video
        - **63**: Picture
        - **21**: Article
        - **38**: Topic
        - **98**: Super topic
    ### Return:
    - Search data

    # [示例/Example]
    keyword = \"游戏\"
    page = \"1\"
    search_type = \"1\"

    Args:
        keyword (str): 关键词/Keyword
        page (Union[Unset, str]): 页数/Page number Default: '1'.
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
            page=page,
            search_type=search_type,
        )
    ).parsed
