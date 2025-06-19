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
    url_query: str,
    pagination_token: Union[Unset, str] = UNSET,
    sort_type: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["url"] = url_query

    params["pagination_token"] = pagination_token

    params["sort_type"] = sort_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/instagram/web_app/fetch_post_comments_by_url",
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
    url_query: str,
    pagination_token: Union[Unset, str] = UNSET,
    sort_type: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""根据URL获取帖子评论数据/Get post comments by URL

     # [中文]
    ### 用途:
    - 根据Instagram帖子URL获取帖子评论数据
    - 由于此接口收到后端代理服务器的影响，请在请求此接口时适当调整timeout参数。
    - 建议将timeout设置为60秒，以确保能够获取到数据，大多数情况下，数据获取时间在10秒以内。
    ### 参数:
    - url: Instagram帖子URL
    - pagination_token: 分页token，第一次请求不需要传值，后续页需要传入上一页的返回值。
    - sort_type: 排序方式
        - recent:：最新
        - popular：热门
    ### 返回:
    - 帖子评论数据

    # [English]
    ### Purpose:
    - Get post comments by Instagram post URL
    - Due to the impact of the backend proxy server, please adjust the timeout parameter appropriately
    when requesting this interface.
    - It is recommended to set the timeout to 60 seconds to ensure that the data can be obtained. In
    most cases, the data acquisition time is within 10 seconds.
    ### Parameters:
    - url: Instagram post URL
    - pagination_token: Pagination token, no need to pass value for the first request, pass the return
    value of the previous page for subsequent pages.
    - sort_type: Sort Type
        - recent: Recnet
        - popular: Popular
    ### Return:
    - Post comments data

    # [示例/Example]
    url = \"https://www.instagram.com/p/C3OqtMeRxrV/\"
    pagination_token = None
    sort_type = \"recent\"

    Args:
        url_query (str): Instagram帖子URL/Instagram post URL
        pagination_token (Union[Unset, str]): 分页token/Pagination token
        sort_type (Union[Unset, str]): 排序方式/Sort type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        url_query=url_query,
        pagination_token=pagination_token,
        sort_type=sort_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    url_query: str,
    pagination_token: Union[Unset, str] = UNSET,
    sort_type: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""根据URL获取帖子评论数据/Get post comments by URL

     # [中文]
    ### 用途:
    - 根据Instagram帖子URL获取帖子评论数据
    - 由于此接口收到后端代理服务器的影响，请在请求此接口时适当调整timeout参数。
    - 建议将timeout设置为60秒，以确保能够获取到数据，大多数情况下，数据获取时间在10秒以内。
    ### 参数:
    - url: Instagram帖子URL
    - pagination_token: 分页token，第一次请求不需要传值，后续页需要传入上一页的返回值。
    - sort_type: 排序方式
        - recent:：最新
        - popular：热门
    ### 返回:
    - 帖子评论数据

    # [English]
    ### Purpose:
    - Get post comments by Instagram post URL
    - Due to the impact of the backend proxy server, please adjust the timeout parameter appropriately
    when requesting this interface.
    - It is recommended to set the timeout to 60 seconds to ensure that the data can be obtained. In
    most cases, the data acquisition time is within 10 seconds.
    ### Parameters:
    - url: Instagram post URL
    - pagination_token: Pagination token, no need to pass value for the first request, pass the return
    value of the previous page for subsequent pages.
    - sort_type: Sort Type
        - recent: Recnet
        - popular: Popular
    ### Return:
    - Post comments data

    # [示例/Example]
    url = \"https://www.instagram.com/p/C3OqtMeRxrV/\"
    pagination_token = None
    sort_type = \"recent\"

    Args:
        url_query (str): Instagram帖子URL/Instagram post URL
        pagination_token (Union[Unset, str]): 分页token/Pagination token
        sort_type (Union[Unset, str]): 排序方式/Sort type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        url_query=url_query,
        pagination_token=pagination_token,
        sort_type=sort_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    url_query: str,
    pagination_token: Union[Unset, str] = UNSET,
    sort_type: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""根据URL获取帖子评论数据/Get post comments by URL

     # [中文]
    ### 用途:
    - 根据Instagram帖子URL获取帖子评论数据
    - 由于此接口收到后端代理服务器的影响，请在请求此接口时适当调整timeout参数。
    - 建议将timeout设置为60秒，以确保能够获取到数据，大多数情况下，数据获取时间在10秒以内。
    ### 参数:
    - url: Instagram帖子URL
    - pagination_token: 分页token，第一次请求不需要传值，后续页需要传入上一页的返回值。
    - sort_type: 排序方式
        - recent:：最新
        - popular：热门
    ### 返回:
    - 帖子评论数据

    # [English]
    ### Purpose:
    - Get post comments by Instagram post URL
    - Due to the impact of the backend proxy server, please adjust the timeout parameter appropriately
    when requesting this interface.
    - It is recommended to set the timeout to 60 seconds to ensure that the data can be obtained. In
    most cases, the data acquisition time is within 10 seconds.
    ### Parameters:
    - url: Instagram post URL
    - pagination_token: Pagination token, no need to pass value for the first request, pass the return
    value of the previous page for subsequent pages.
    - sort_type: Sort Type
        - recent: Recnet
        - popular: Popular
    ### Return:
    - Post comments data

    # [示例/Example]
    url = \"https://www.instagram.com/p/C3OqtMeRxrV/\"
    pagination_token = None
    sort_type = \"recent\"

    Args:
        url_query (str): Instagram帖子URL/Instagram post URL
        pagination_token (Union[Unset, str]): 分页token/Pagination token
        sort_type (Union[Unset, str]): 排序方式/Sort type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        url_query=url_query,
        pagination_token=pagination_token,
        sort_type=sort_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    url_query: str,
    pagination_token: Union[Unset, str] = UNSET,
    sort_type: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""根据URL获取帖子评论数据/Get post comments by URL

     # [中文]
    ### 用途:
    - 根据Instagram帖子URL获取帖子评论数据
    - 由于此接口收到后端代理服务器的影响，请在请求此接口时适当调整timeout参数。
    - 建议将timeout设置为60秒，以确保能够获取到数据，大多数情况下，数据获取时间在10秒以内。
    ### 参数:
    - url: Instagram帖子URL
    - pagination_token: 分页token，第一次请求不需要传值，后续页需要传入上一页的返回值。
    - sort_type: 排序方式
        - recent:：最新
        - popular：热门
    ### 返回:
    - 帖子评论数据

    # [English]
    ### Purpose:
    - Get post comments by Instagram post URL
    - Due to the impact of the backend proxy server, please adjust the timeout parameter appropriately
    when requesting this interface.
    - It is recommended to set the timeout to 60 seconds to ensure that the data can be obtained. In
    most cases, the data acquisition time is within 10 seconds.
    ### Parameters:
    - url: Instagram post URL
    - pagination_token: Pagination token, no need to pass value for the first request, pass the return
    value of the previous page for subsequent pages.
    - sort_type: Sort Type
        - recent: Recnet
        - popular: Popular
    ### Return:
    - Post comments data

    # [示例/Example]
    url = \"https://www.instagram.com/p/C3OqtMeRxrV/\"
    pagination_token = None
    sort_type = \"recent\"

    Args:
        url_query (str): Instagram帖子URL/Instagram post URL
        pagination_token (Union[Unset, str]): 分页token/Pagination token
        sort_type (Union[Unset, str]): 排序方式/Sort type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            url_query=url_query,
            pagination_token=pagination_token,
            sort_type=sort_type,
        )
    ).parsed
