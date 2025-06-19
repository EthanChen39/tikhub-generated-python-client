from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_fetch_user_collects_api_v1_douyin_web_fetch_user_collects_post import (
    BodyFetchUserCollectsApiV1DouyinWebFetchUserCollectsPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: BodyFetchUserCollectsApiV1DouyinWebFetchUserCollectsPost,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/web/fetch_user_collects",
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
    body: BodyFetchUserCollectsApiV1DouyinWebFetchUserCollectsPost,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户收藏夹/Get user collection

     # [中文]
    ### 用途:
    - 获取用户收藏夹
    ### 参数:
    - max_cursor: 最大游标
    - count: 最大数量
    - cookie: 用户网页版抖音Cookie(此接口需要用户提供自己的Cookie)
    ### 返回:
    - 用户收藏夹数据

    # [English]
    ### Purpose:
    - Get user collection
    ### Parameters:
    - max_cursor: Maximum cursor
    - count: Maximum number
    - cookie: User's web version of Douyin Cookie (This interface requires users to provide their own
    Cookie)
    ### Return:
    - User collection data

    # [示例/Example]
    cookie = \"YOUR_COOKIE\"
    max_cursor = 0
    counts = 20

    Args:
        body (BodyFetchUserCollectsApiV1DouyinWebFetchUserCollectsPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BodyFetchUserCollectsApiV1DouyinWebFetchUserCollectsPost,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户收藏夹/Get user collection

     # [中文]
    ### 用途:
    - 获取用户收藏夹
    ### 参数:
    - max_cursor: 最大游标
    - count: 最大数量
    - cookie: 用户网页版抖音Cookie(此接口需要用户提供自己的Cookie)
    ### 返回:
    - 用户收藏夹数据

    # [English]
    ### Purpose:
    - Get user collection
    ### Parameters:
    - max_cursor: Maximum cursor
    - count: Maximum number
    - cookie: User's web version of Douyin Cookie (This interface requires users to provide their own
    Cookie)
    ### Return:
    - User collection data

    # [示例/Example]
    cookie = \"YOUR_COOKIE\"
    max_cursor = 0
    counts = 20

    Args:
        body (BodyFetchUserCollectsApiV1DouyinWebFetchUserCollectsPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyFetchUserCollectsApiV1DouyinWebFetchUserCollectsPost,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户收藏夹/Get user collection

     # [中文]
    ### 用途:
    - 获取用户收藏夹
    ### 参数:
    - max_cursor: 最大游标
    - count: 最大数量
    - cookie: 用户网页版抖音Cookie(此接口需要用户提供自己的Cookie)
    ### 返回:
    - 用户收藏夹数据

    # [English]
    ### Purpose:
    - Get user collection
    ### Parameters:
    - max_cursor: Maximum cursor
    - count: Maximum number
    - cookie: User's web version of Douyin Cookie (This interface requires users to provide their own
    Cookie)
    ### Return:
    - User collection data

    # [示例/Example]
    cookie = \"YOUR_COOKIE\"
    max_cursor = 0
    counts = 20

    Args:
        body (BodyFetchUserCollectsApiV1DouyinWebFetchUserCollectsPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BodyFetchUserCollectsApiV1DouyinWebFetchUserCollectsPost,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取用户收藏夹/Get user collection

     # [中文]
    ### 用途:
    - 获取用户收藏夹
    ### 参数:
    - max_cursor: 最大游标
    - count: 最大数量
    - cookie: 用户网页版抖音Cookie(此接口需要用户提供自己的Cookie)
    ### 返回:
    - 用户收藏夹数据

    # [English]
    ### Purpose:
    - Get user collection
    ### Parameters:
    - max_cursor: Maximum cursor
    - count: Maximum number
    - cookie: User's web version of Douyin Cookie (This interface requires users to provide their own
    Cookie)
    ### Return:
    - User collection data

    # [示例/Example]
    cookie = \"YOUR_COOKIE\"
    max_cursor = 0
    counts = 20

    Args:
        body (BodyFetchUserCollectsApiV1DouyinWebFetchUserCollectsPost):

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
        )
    ).parsed
