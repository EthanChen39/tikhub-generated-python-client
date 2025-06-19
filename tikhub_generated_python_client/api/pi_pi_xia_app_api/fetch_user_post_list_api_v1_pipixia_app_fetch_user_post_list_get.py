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
    user_id: str,
    cursor: Union[Unset, str] = "0",
    feed_count: Union[Unset, str] = "0",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["user_id"] = user_id

    params["cursor"] = cursor

    params["feed_count"] = feed_count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/pipixia/app/fetch_user_post_list",
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
    user_id: str,
    cursor: Union[Unset, str] = "0",
    feed_count: Union[Unset, str] = "0",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户作品列表/Get user post list

     # [中文]
    ### 用途:
    - 获取用户作品列表，如视频、图文等。
    ### 参数:
    - user_id: 用户id，可以从分享链接中获取。
    - cursor: 翻页游标，默认为0，后续页码从上一页返回的 `loadmore_cursor` Key中获取对应值。
    - feed_count: 翻页数量，默认为0，后续每次翻页加1，比如第一页为0，第二页为1，第三页为2，以此类推。
    ### 返回:
    - 用户作品列表

    # [English]
    ### Purpose:
    - Get user post list, such as videos, photos, etc.
    ### Parameters:
    - user_id: AKA user id, can be obtained from the share link.
    - cursor: Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in
    the previous page.
    - feed_count: Page count, default is 0, add 1 for each page, such as 0 for the first page, 1 for the
    second page, 2 for the third page, and so on.
    ### Return:
    - User post list

    # [示例/Example]
    user_id = \"1310254082831248\"
    cursor = \"0\"
    feed_count = \"0\"

    Args:
        user_id (str): 用户id/User id
        cursor (Union[Unset, str]): 翻页游标/Page cursor Default: '0'.
        feed_count (Union[Unset, str]): 翻页数量/Page count Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        cursor=cursor,
        feed_count=feed_count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: str,
    cursor: Union[Unset, str] = "0",
    feed_count: Union[Unset, str] = "0",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户作品列表/Get user post list

     # [中文]
    ### 用途:
    - 获取用户作品列表，如视频、图文等。
    ### 参数:
    - user_id: 用户id，可以从分享链接中获取。
    - cursor: 翻页游标，默认为0，后续页码从上一页返回的 `loadmore_cursor` Key中获取对应值。
    - feed_count: 翻页数量，默认为0，后续每次翻页加1，比如第一页为0，第二页为1，第三页为2，以此类推。
    ### 返回:
    - 用户作品列表

    # [English]
    ### Purpose:
    - Get user post list, such as videos, photos, etc.
    ### Parameters:
    - user_id: AKA user id, can be obtained from the share link.
    - cursor: Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in
    the previous page.
    - feed_count: Page count, default is 0, add 1 for each page, such as 0 for the first page, 1 for the
    second page, 2 for the third page, and so on.
    ### Return:
    - User post list

    # [示例/Example]
    user_id = \"1310254082831248\"
    cursor = \"0\"
    feed_count = \"0\"

    Args:
        user_id (str): 用户id/User id
        cursor (Union[Unset, str]): 翻页游标/Page cursor Default: '0'.
        feed_count (Union[Unset, str]): 翻页数量/Page count Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        cursor=cursor,
        feed_count=feed_count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: str,
    cursor: Union[Unset, str] = "0",
    feed_count: Union[Unset, str] = "0",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户作品列表/Get user post list

     # [中文]
    ### 用途:
    - 获取用户作品列表，如视频、图文等。
    ### 参数:
    - user_id: 用户id，可以从分享链接中获取。
    - cursor: 翻页游标，默认为0，后续页码从上一页返回的 `loadmore_cursor` Key中获取对应值。
    - feed_count: 翻页数量，默认为0，后续每次翻页加1，比如第一页为0，第二页为1，第三页为2，以此类推。
    ### 返回:
    - 用户作品列表

    # [English]
    ### Purpose:
    - Get user post list, such as videos, photos, etc.
    ### Parameters:
    - user_id: AKA user id, can be obtained from the share link.
    - cursor: Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in
    the previous page.
    - feed_count: Page count, default is 0, add 1 for each page, such as 0 for the first page, 1 for the
    second page, 2 for the third page, and so on.
    ### Return:
    - User post list

    # [示例/Example]
    user_id = \"1310254082831248\"
    cursor = \"0\"
    feed_count = \"0\"

    Args:
        user_id (str): 用户id/User id
        cursor (Union[Unset, str]): 翻页游标/Page cursor Default: '0'.
        feed_count (Union[Unset, str]): 翻页数量/Page count Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        cursor=cursor,
        feed_count=feed_count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: str,
    cursor: Union[Unset, str] = "0",
    feed_count: Union[Unset, str] = "0",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户作品列表/Get user post list

     # [中文]
    ### 用途:
    - 获取用户作品列表，如视频、图文等。
    ### 参数:
    - user_id: 用户id，可以从分享链接中获取。
    - cursor: 翻页游标，默认为0，后续页码从上一页返回的 `loadmore_cursor` Key中获取对应值。
    - feed_count: 翻页数量，默认为0，后续每次翻页加1，比如第一页为0，第二页为1，第三页为2，以此类推。
    ### 返回:
    - 用户作品列表

    # [English]
    ### Purpose:
    - Get user post list, such as videos, photos, etc.
    ### Parameters:
    - user_id: AKA user id, can be obtained from the share link.
    - cursor: Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in
    the previous page.
    - feed_count: Page count, default is 0, add 1 for each page, such as 0 for the first page, 1 for the
    second page, 2 for the third page, and so on.
    ### Return:
    - User post list

    # [示例/Example]
    user_id = \"1310254082831248\"
    cursor = \"0\"
    feed_count = \"0\"

    Args:
        user_id (str): 用户id/User id
        cursor (Union[Unset, str]): 翻页游标/Page cursor Default: '0'.
        feed_count (Union[Unset, str]): 翻页数量/Page count Default: '0'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            cursor=cursor,
            feed_count=feed_count,
        )
    ).parsed
