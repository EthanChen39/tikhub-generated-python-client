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
    column_id: str,
    limit: Union[Unset, str] = "10",
    offset: Union[Unset, str] = "0",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["column_id"] = column_id

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/zhihu/web/fetch_column_articles",
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
    column_id: str,
    limit: Union[Unset, str] = "10",
    offset: Union[Unset, str] = "0",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎专栏文章列表/Get Zhihu Column Articles

     # [中文]
    ### 用途:
    - 获取知乎专栏文章列表
    ### 参数:
    - column_id: 专栏ID
    - limit: 每页文章数量
    - offset: 偏移量
    ### 返回:
    - 知乎专栏文章列表

    # [English]
    ### Purpose:
    - Get Zhihu Column Articles
    ### Parameters:
    - column_id: Column ID
    - limit: Number of articles per page
    - offset: Offset
    ### Returns:
    - Zhihu Column Articles

    # [示例/Example]
    column_id = \"zhangjiawei\"
    limit = \"10\"
    offset = \"0\"

    Args:
        column_id (str): 专栏ID/Column ID
        limit (Union[Unset, str]): 每页文章数量/Number of articles per page Default: '10'.
        offset (Union[Unset, str]): 偏移量/Offset Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        column_id=column_id,
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
    column_id: str,
    limit: Union[Unset, str] = "10",
    offset: Union[Unset, str] = "0",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎专栏文章列表/Get Zhihu Column Articles

     # [中文]
    ### 用途:
    - 获取知乎专栏文章列表
    ### 参数:
    - column_id: 专栏ID
    - limit: 每页文章数量
    - offset: 偏移量
    ### 返回:
    - 知乎专栏文章列表

    # [English]
    ### Purpose:
    - Get Zhihu Column Articles
    ### Parameters:
    - column_id: Column ID
    - limit: Number of articles per page
    - offset: Offset
    ### Returns:
    - Zhihu Column Articles

    # [示例/Example]
    column_id = \"zhangjiawei\"
    limit = \"10\"
    offset = \"0\"

    Args:
        column_id (str): 专栏ID/Column ID
        limit (Union[Unset, str]): 每页文章数量/Number of articles per page Default: '10'.
        offset (Union[Unset, str]): 偏移量/Offset Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        column_id=column_id,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    column_id: str,
    limit: Union[Unset, str] = "10",
    offset: Union[Unset, str] = "0",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎专栏文章列表/Get Zhihu Column Articles

     # [中文]
    ### 用途:
    - 获取知乎专栏文章列表
    ### 参数:
    - column_id: 专栏ID
    - limit: 每页文章数量
    - offset: 偏移量
    ### 返回:
    - 知乎专栏文章列表

    # [English]
    ### Purpose:
    - Get Zhihu Column Articles
    ### Parameters:
    - column_id: Column ID
    - limit: Number of articles per page
    - offset: Offset
    ### Returns:
    - Zhihu Column Articles

    # [示例/Example]
    column_id = \"zhangjiawei\"
    limit = \"10\"
    offset = \"0\"

    Args:
        column_id (str): 专栏ID/Column ID
        limit (Union[Unset, str]): 每页文章数量/Number of articles per page Default: '10'.
        offset (Union[Unset, str]): 偏移量/Offset Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        column_id=column_id,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    column_id: str,
    limit: Union[Unset, str] = "10",
    offset: Union[Unset, str] = "0",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取知乎专栏文章列表/Get Zhihu Column Articles

     # [中文]
    ### 用途:
    - 获取知乎专栏文章列表
    ### 参数:
    - column_id: 专栏ID
    - limit: 每页文章数量
    - offset: 偏移量
    ### 返回:
    - 知乎专栏文章列表

    # [English]
    ### Purpose:
    - Get Zhihu Column Articles
    ### Parameters:
    - column_id: Column ID
    - limit: Number of articles per page
    - offset: Offset
    ### Returns:
    - Zhihu Column Articles

    # [示例/Example]
    column_id = \"zhangjiawei\"
    limit = \"10\"
    offset = \"0\"

    Args:
        column_id (str): 专栏ID/Column ID
        limit (Union[Unset, str]): 每页文章数量/Number of articles per page Default: '10'.
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
            column_id=column_id,
            limit=limit,
            offset=offset,
        )
    ).parsed
