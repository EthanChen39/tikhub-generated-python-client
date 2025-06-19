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
    article_id: str,
    limit: Union[Unset, str] = "12",
    offset: Union[Unset, str] = "0",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["article_id"] = article_id

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/zhihu/web/fetch_column_recommend",
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
    article_id: str,
    limit: Union[Unset, str] = "12",
    offset: Union[Unset, str] = "0",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎相似专栏推荐/Get Zhihu Similar Column Recommend

     # [中文]
    ### 用途:
    - 获取知乎相似专栏推荐
    ### 参数:
    - article_id: 文章ID
    - limit: 每页专栏数量
    - offset: 偏移量
    ### 返回:
    - 知乎相似专栏推荐

    # [English]
    ### Purpose:
    - Get Zhihu Similar Column Recommend
    ### Parameters:
    - article_id: Article ID
    - limit: Number of columns per page
    - offset: Offset
    ### Returns:
    - Zhihu Similar Column Recommend

    # [示例/Example]
    article_id = \"669214677\"
    limit = \"12\"
    offset = \"0\"

    Args:
        article_id (str): 文章ID/Article ID
        limit (Union[Unset, str]): 每页专栏数量/Number of columns per page Default: '12'.
        offset (Union[Unset, str]): 偏移量/Offset Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        article_id=article_id,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    article_id: str,
    limit: Union[Unset, str] = "12",
    offset: Union[Unset, str] = "0",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎相似专栏推荐/Get Zhihu Similar Column Recommend

     # [中文]
    ### 用途:
    - 获取知乎相似专栏推荐
    ### 参数:
    - article_id: 文章ID
    - limit: 每页专栏数量
    - offset: 偏移量
    ### 返回:
    - 知乎相似专栏推荐

    # [English]
    ### Purpose:
    - Get Zhihu Similar Column Recommend
    ### Parameters:
    - article_id: Article ID
    - limit: Number of columns per page
    - offset: Offset
    ### Returns:
    - Zhihu Similar Column Recommend

    # [示例/Example]
    article_id = \"669214677\"
    limit = \"12\"
    offset = \"0\"

    Args:
        article_id (str): 文章ID/Article ID
        limit (Union[Unset, str]): 每页专栏数量/Number of columns per page Default: '12'.
        offset (Union[Unset, str]): 偏移量/Offset Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        article_id=article_id,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    article_id: str,
    limit: Union[Unset, str] = "12",
    offset: Union[Unset, str] = "0",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎相似专栏推荐/Get Zhihu Similar Column Recommend

     # [中文]
    ### 用途:
    - 获取知乎相似专栏推荐
    ### 参数:
    - article_id: 文章ID
    - limit: 每页专栏数量
    - offset: 偏移量
    ### 返回:
    - 知乎相似专栏推荐

    # [English]
    ### Purpose:
    - Get Zhihu Similar Column Recommend
    ### Parameters:
    - article_id: Article ID
    - limit: Number of columns per page
    - offset: Offset
    ### Returns:
    - Zhihu Similar Column Recommend

    # [示例/Example]
    article_id = \"669214677\"
    limit = \"12\"
    offset = \"0\"

    Args:
        article_id (str): 文章ID/Article ID
        limit (Union[Unset, str]): 每页专栏数量/Number of columns per page Default: '12'.
        offset (Union[Unset, str]): 偏移量/Offset Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        article_id=article_id,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    article_id: str,
    limit: Union[Unset, str] = "12",
    offset: Union[Unset, str] = "0",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎相似专栏推荐/Get Zhihu Similar Column Recommend

     # [中文]
    ### 用途:
    - 获取知乎相似专栏推荐
    ### 参数:
    - article_id: 文章ID
    - limit: 每页专栏数量
    - offset: 偏移量
    ### 返回:
    - 知乎相似专栏推荐

    # [English]
    ### Purpose:
    - Get Zhihu Similar Column Recommend
    ### Parameters:
    - article_id: Article ID
    - limit: Number of columns per page
    - offset: Offset
    ### Returns:
    - Zhihu Similar Column Recommend

    # [示例/Example]
    article_id = \"669214677\"
    limit = \"12\"
    offset = \"0\"

    Args:
        article_id (str): 文章ID/Article ID
        limit (Union[Unset, str]): 每页专栏数量/Number of columns per page Default: '12'.
        offset (Union[Unset, str]): 偏移量/Offset Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            article_id=article_id,
            limit=limit,
            offset=offset,
        )
    ).parsed
