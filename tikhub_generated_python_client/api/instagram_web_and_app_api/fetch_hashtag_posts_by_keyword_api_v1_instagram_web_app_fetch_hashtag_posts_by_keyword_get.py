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
    pagination_token: Union[Unset, str] = UNSET,
    feed_type: Union[Unset, str] = "top",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["pagination_token"] = pagination_token

    params["feed_type"] = feed_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/instagram/web_app/fetch_hashtag_posts_by_keyword",
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
    pagination_token: Union[Unset, str] = UNSET,
    feed_type: Union[Unset, str] = "top",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""根据关键词获取话题帖子/Get hashtag posts by query

     # [中文]
    ### 用途:
    - 根据关键词获取话题帖子
    - 由于此接口收到后端代理服务器的影响，请在请求此接口时适当调整timeout参数。
    - 建议将timeout设置为60秒，以确保能够获取到数据，大多数情况下，数据获取时间在10秒以内。
    ### 参数:
    - keyword: 关键词
    - pagination_token: 翻页游标，用于翻页，第一页不需要传值，后续页需要传入上一页的返回值。
    - feed_type: Feed类型
        - top: 热门（默认）
        - recent: 最新
        - clips: 快拍
    ### 返回:
    - 话题帖子

    # [English]
    ### Purpose:
    - Get hashtag posts by query
    - Due to the impact of the backend proxy server, please adjust the timeout parameter appropriately
    when requesting this interface.
    - It is recommended to set the timeout to 60 seconds to ensure that the data can be obtained. In
    most cases, the data acquisition time is within 10 seconds.
    ### Parameters:
    - keyword: Query
    - pagination_token: Pagination token, used for pagination, no need to pass value for the first page,
    pass the return value of the previous page for subsequent pages.
    - feed_type: Feed type
        - top: Top (default)
        - recent: Recent (sort by time)
        - clips: Clips (show only Reels)
    ### Return:
    - Hashtag posts

    # [示例/Example]
    keyword = \"GitHub\"
    pagination_token = None

    Args:
        keyword (str): 关键词/Query
        pagination_token (Union[Unset, str]): 翻页令牌/Pagination token
        feed_type (Union[Unset, str]): Feed类型/Feed type Default: 'top'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        pagination_token=pagination_token,
        feed_type=feed_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    keyword: str,
    pagination_token: Union[Unset, str] = UNSET,
    feed_type: Union[Unset, str] = "top",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""根据关键词获取话题帖子/Get hashtag posts by query

     # [中文]
    ### 用途:
    - 根据关键词获取话题帖子
    - 由于此接口收到后端代理服务器的影响，请在请求此接口时适当调整timeout参数。
    - 建议将timeout设置为60秒，以确保能够获取到数据，大多数情况下，数据获取时间在10秒以内。
    ### 参数:
    - keyword: 关键词
    - pagination_token: 翻页游标，用于翻页，第一页不需要传值，后续页需要传入上一页的返回值。
    - feed_type: Feed类型
        - top: 热门（默认）
        - recent: 最新
        - clips: 快拍
    ### 返回:
    - 话题帖子

    # [English]
    ### Purpose:
    - Get hashtag posts by query
    - Due to the impact of the backend proxy server, please adjust the timeout parameter appropriately
    when requesting this interface.
    - It is recommended to set the timeout to 60 seconds to ensure that the data can be obtained. In
    most cases, the data acquisition time is within 10 seconds.
    ### Parameters:
    - keyword: Query
    - pagination_token: Pagination token, used for pagination, no need to pass value for the first page,
    pass the return value of the previous page for subsequent pages.
    - feed_type: Feed type
        - top: Top (default)
        - recent: Recent (sort by time)
        - clips: Clips (show only Reels)
    ### Return:
    - Hashtag posts

    # [示例/Example]
    keyword = \"GitHub\"
    pagination_token = None

    Args:
        keyword (str): 关键词/Query
        pagination_token (Union[Unset, str]): 翻页令牌/Pagination token
        feed_type (Union[Unset, str]): Feed类型/Feed type Default: 'top'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        keyword=keyword,
        pagination_token=pagination_token,
        feed_type=feed_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    pagination_token: Union[Unset, str] = UNSET,
    feed_type: Union[Unset, str] = "top",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""根据关键词获取话题帖子/Get hashtag posts by query

     # [中文]
    ### 用途:
    - 根据关键词获取话题帖子
    - 由于此接口收到后端代理服务器的影响，请在请求此接口时适当调整timeout参数。
    - 建议将timeout设置为60秒，以确保能够获取到数据，大多数情况下，数据获取时间在10秒以内。
    ### 参数:
    - keyword: 关键词
    - pagination_token: 翻页游标，用于翻页，第一页不需要传值，后续页需要传入上一页的返回值。
    - feed_type: Feed类型
        - top: 热门（默认）
        - recent: 最新
        - clips: 快拍
    ### 返回:
    - 话题帖子

    # [English]
    ### Purpose:
    - Get hashtag posts by query
    - Due to the impact of the backend proxy server, please adjust the timeout parameter appropriately
    when requesting this interface.
    - It is recommended to set the timeout to 60 seconds to ensure that the data can be obtained. In
    most cases, the data acquisition time is within 10 seconds.
    ### Parameters:
    - keyword: Query
    - pagination_token: Pagination token, used for pagination, no need to pass value for the first page,
    pass the return value of the previous page for subsequent pages.
    - feed_type: Feed type
        - top: Top (default)
        - recent: Recent (sort by time)
        - clips: Clips (show only Reels)
    ### Return:
    - Hashtag posts

    # [示例/Example]
    keyword = \"GitHub\"
    pagination_token = None

    Args:
        keyword (str): 关键词/Query
        pagination_token (Union[Unset, str]): 翻页令牌/Pagination token
        feed_type (Union[Unset, str]): Feed类型/Feed type Default: 'top'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        pagination_token=pagination_token,
        feed_type=feed_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
    pagination_token: Union[Unset, str] = UNSET,
    feed_type: Union[Unset, str] = "top",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""根据关键词获取话题帖子/Get hashtag posts by query

     # [中文]
    ### 用途:
    - 根据关键词获取话题帖子
    - 由于此接口收到后端代理服务器的影响，请在请求此接口时适当调整timeout参数。
    - 建议将timeout设置为60秒，以确保能够获取到数据，大多数情况下，数据获取时间在10秒以内。
    ### 参数:
    - keyword: 关键词
    - pagination_token: 翻页游标，用于翻页，第一页不需要传值，后续页需要传入上一页的返回值。
    - feed_type: Feed类型
        - top: 热门（默认）
        - recent: 最新
        - clips: 快拍
    ### 返回:
    - 话题帖子

    # [English]
    ### Purpose:
    - Get hashtag posts by query
    - Due to the impact of the backend proxy server, please adjust the timeout parameter appropriately
    when requesting this interface.
    - It is recommended to set the timeout to 60 seconds to ensure that the data can be obtained. In
    most cases, the data acquisition time is within 10 seconds.
    ### Parameters:
    - keyword: Query
    - pagination_token: Pagination token, used for pagination, no need to pass value for the first page,
    pass the return value of the previous page for subsequent pages.
    - feed_type: Feed type
        - top: Top (default)
        - recent: Recent (sort by time)
        - clips: Clips (show only Reels)
    ### Return:
    - Hashtag posts

    # [示例/Example]
    keyword = \"GitHub\"
    pagination_token = None

    Args:
        keyword (str): 关键词/Query
        pagination_token (Union[Unset, str]): 翻页令牌/Pagination token
        feed_type (Union[Unset, str]): Feed类型/Feed type Default: 'top'.

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
            pagination_token=pagination_token,
            feed_type=feed_type,
        )
    ).parsed
