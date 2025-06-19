from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fetch_scholar_search_v3_api_v1_zhihu_web_fetch_scholar_search_v3_post_filter_fields import (
    FetchScholarSearchV3ApiV1ZhihuWebFetchScholarSearchV3PostFilterFields,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: FetchScholarSearchV3ApiV1ZhihuWebFetchScholarSearchV3PostFilterFields,
    keyword: str,
    offset: Union[Unset, str] = "0",
    limit: Union[Unset, str] = "25",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/zhihu/web/fetch_scholar_search_v3",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: FetchScholarSearchV3ApiV1ZhihuWebFetchScholarSearchV3PostFilterFields,
    keyword: str,
    offset: Union[Unset, str] = "0",
    limit: Union[Unset, str] = "25",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎论文搜索V3/Get Zhihu Scholar Search V3

     # [中文]
    ### 用途:
    - 获取知乎论文搜索V3
    ### 参数:
    - keyword: 搜索关键词
    - offset: 偏移量
    - limit: 每页论文数量
    - filter_fields: 过滤字段
    ### 返回:
    - 知乎论文搜索V3

    # [English]
    ### Purpose:
    - Get Zhihu Scholar Search V3
    ### Parameters:
    - keyword: Search Keywords
    - offset: Offset
    - limit: Number of papers per page
    - filter_fields: Filter Fields
    ### Returns:
    - Zhihu Scholar Search V3

    # [示例/Example]
    keyword = \"人工智能\"
    offset = \"0\"
    limit = \"25\"

    Args:
        keyword (str): 搜索关键词/Search Keywords
        offset (Union[Unset, str]): 偏移量/Offset Default: '0'.
        limit (Union[Unset, str]): 每页论文数量/Number of papers per page Default: '25'.
        body (FetchScholarSearchV3ApiV1ZhihuWebFetchScholarSearchV3PostFilterFields): 过滤字段/Filter
            Fields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        body=body,
        keyword=keyword,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: FetchScholarSearchV3ApiV1ZhihuWebFetchScholarSearchV3PostFilterFields,
    keyword: str,
    offset: Union[Unset, str] = "0",
    limit: Union[Unset, str] = "25",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎论文搜索V3/Get Zhihu Scholar Search V3

     # [中文]
    ### 用途:
    - 获取知乎论文搜索V3
    ### 参数:
    - keyword: 搜索关键词
    - offset: 偏移量
    - limit: 每页论文数量
    - filter_fields: 过滤字段
    ### 返回:
    - 知乎论文搜索V3

    # [English]
    ### Purpose:
    - Get Zhihu Scholar Search V3
    ### Parameters:
    - keyword: Search Keywords
    - offset: Offset
    - limit: Number of papers per page
    - filter_fields: Filter Fields
    ### Returns:
    - Zhihu Scholar Search V3

    # [示例/Example]
    keyword = \"人工智能\"
    offset = \"0\"
    limit = \"25\"

    Args:
        keyword (str): 搜索关键词/Search Keywords
        offset (Union[Unset, str]): 偏移量/Offset Default: '0'.
        limit (Union[Unset, str]): 每页论文数量/Number of papers per page Default: '25'.
        body (FetchScholarSearchV3ApiV1ZhihuWebFetchScholarSearchV3PostFilterFields): 过滤字段/Filter
            Fields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        body=body,
        keyword=keyword,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: FetchScholarSearchV3ApiV1ZhihuWebFetchScholarSearchV3PostFilterFields,
    keyword: str,
    offset: Union[Unset, str] = "0",
    limit: Union[Unset, str] = "25",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎论文搜索V3/Get Zhihu Scholar Search V3

     # [中文]
    ### 用途:
    - 获取知乎论文搜索V3
    ### 参数:
    - keyword: 搜索关键词
    - offset: 偏移量
    - limit: 每页论文数量
    - filter_fields: 过滤字段
    ### 返回:
    - 知乎论文搜索V3

    # [English]
    ### Purpose:
    - Get Zhihu Scholar Search V3
    ### Parameters:
    - keyword: Search Keywords
    - offset: Offset
    - limit: Number of papers per page
    - filter_fields: Filter Fields
    ### Returns:
    - Zhihu Scholar Search V3

    # [示例/Example]
    keyword = \"人工智能\"
    offset = \"0\"
    limit = \"25\"

    Args:
        keyword (str): 搜索关键词/Search Keywords
        offset (Union[Unset, str]): 偏移量/Offset Default: '0'.
        limit (Union[Unset, str]): 每页论文数量/Number of papers per page Default: '25'.
        body (FetchScholarSearchV3ApiV1ZhihuWebFetchScholarSearchV3PostFilterFields): 过滤字段/Filter
            Fields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        body=body,
        keyword=keyword,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: FetchScholarSearchV3ApiV1ZhihuWebFetchScholarSearchV3PostFilterFields,
    keyword: str,
    offset: Union[Unset, str] = "0",
    limit: Union[Unset, str] = "25",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎论文搜索V3/Get Zhihu Scholar Search V3

     # [中文]
    ### 用途:
    - 获取知乎论文搜索V3
    ### 参数:
    - keyword: 搜索关键词
    - offset: 偏移量
    - limit: 每页论文数量
    - filter_fields: 过滤字段
    ### 返回:
    - 知乎论文搜索V3

    # [English]
    ### Purpose:
    - Get Zhihu Scholar Search V3
    ### Parameters:
    - keyword: Search Keywords
    - offset: Offset
    - limit: Number of papers per page
    - filter_fields: Filter Fields
    ### Returns:
    - Zhihu Scholar Search V3

    # [示例/Example]
    keyword = \"人工智能\"
    offset = \"0\"
    limit = \"25\"

    Args:
        keyword (str): 搜索关键词/Search Keywords
        offset (Union[Unset, str]): 偏移量/Offset Default: '0'.
        limit (Union[Unset, str]): 每页论文数量/Number of papers per page Default: '25'.
        body (FetchScholarSearchV3ApiV1ZhihuWebFetchScholarSearchV3PostFilterFields): 过滤字段/Filter
            Fields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            keyword=keyword,
            offset=offset,
            limit=limit,
        )
    ).parsed
