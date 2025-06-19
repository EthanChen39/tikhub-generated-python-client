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
    limit: Union[Unset, str] = "25",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/zhihu/web/fetch_topic_search_v3",
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
    limit: Union[Unset, str] = "25",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎话题搜索V3/Get Zhihu Topic Search V3

     # [中文]
    ### 用途:
    - 获取知乎话题搜索V3
    ### 参数:
    - keyword: 搜索关键词
    - offset: 偏移量
    - limit: 每页话题数量
    ### 返回:
    - 知乎话题搜索V3

    # [English]
    ### Purpose:
    - Get Zhihu Topic Search V3
    ### Parameters:
    - keyword: Search Keywords
    - offset: Offset
    - limit: Number of topics per page
    ### Returns:
    - Zhihu Topic Search V3

    # [示例/Example]
    keyword = \"deepseek\"
    offset = \"0\"
    limit = \"25\"

    Args:
        keyword (str): 搜索关键词/Search Keywords
        offset (Union[Unset, str]): 偏移量/Offset Default: '0'.
        limit (Union[Unset, str]): 每页话题数量/Number of topics per page Default: '25'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
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
    keyword: str,
    offset: Union[Unset, str] = "0",
    limit: Union[Unset, str] = "25",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎话题搜索V3/Get Zhihu Topic Search V3

     # [中文]
    ### 用途:
    - 获取知乎话题搜索V3
    ### 参数:
    - keyword: 搜索关键词
    - offset: 偏移量
    - limit: 每页话题数量
    ### 返回:
    - 知乎话题搜索V3

    # [English]
    ### Purpose:
    - Get Zhihu Topic Search V3
    ### Parameters:
    - keyword: Search Keywords
    - offset: Offset
    - limit: Number of topics per page
    ### Returns:
    - Zhihu Topic Search V3

    # [示例/Example]
    keyword = \"deepseek\"
    offset = \"0\"
    limit = \"25\"

    Args:
        keyword (str): 搜索关键词/Search Keywords
        offset (Union[Unset, str]): 偏移量/Offset Default: '0'.
        limit (Union[Unset, str]): 每页话题数量/Number of topics per page Default: '25'.

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
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    offset: Union[Unset, str] = "0",
    limit: Union[Unset, str] = "25",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎话题搜索V3/Get Zhihu Topic Search V3

     # [中文]
    ### 用途:
    - 获取知乎话题搜索V3
    ### 参数:
    - keyword: 搜索关键词
    - offset: 偏移量
    - limit: 每页话题数量
    ### 返回:
    - 知乎话题搜索V3

    # [English]
    ### Purpose:
    - Get Zhihu Topic Search V3
    ### Parameters:
    - keyword: Search Keywords
    - offset: Offset
    - limit: Number of topics per page
    ### Returns:
    - Zhihu Topic Search V3

    # [示例/Example]
    keyword = \"deepseek\"
    offset = \"0\"
    limit = \"25\"

    Args:
        keyword (str): 搜索关键词/Search Keywords
        offset (Union[Unset, str]): 偏移量/Offset Default: '0'.
        limit (Union[Unset, str]): 每页话题数量/Number of topics per page Default: '25'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
    offset: Union[Unset, str] = "0",
    limit: Union[Unset, str] = "25",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎话题搜索V3/Get Zhihu Topic Search V3

     # [中文]
    ### 用途:
    - 获取知乎话题搜索V3
    ### 参数:
    - keyword: 搜索关键词
    - offset: 偏移量
    - limit: 每页话题数量
    ### 返回:
    - 知乎话题搜索V3

    # [English]
    ### Purpose:
    - Get Zhihu Topic Search V3
    ### Parameters:
    - keyword: Search Keywords
    - offset: Offset
    - limit: Number of topics per page
    ### Returns:
    - Zhihu Topic Search V3

    # [示例/Example]
    keyword = \"deepseek\"
    offset = \"0\"
    limit = \"25\"

    Args:
        keyword (str): 搜索关键词/Search Keywords
        offset (Union[Unset, str]): 偏移量/Offset Default: '0'.
        limit (Union[Unset, str]): 每页话题数量/Number of topics per page Default: '25'.

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
            limit=limit,
        )
    ).parsed
