from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_fetch_home_feed_api_v1_tiktok_web_fetch_home_feed_post import (
    BodyFetchHomeFeedApiV1TiktokWebFetchHomeFeedPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: BodyFetchHomeFeedApiV1TiktokWebFetchHomeFeedPost,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tiktok/web/fetch_home_feed",
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
    body: BodyFetchHomeFeedApiV1TiktokWebFetchHomeFeedPost,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""首页推荐作品/Home Feed

     # [中文]
    ### 用途:
    - 首页推荐作品
    ### 参数:
    - count: 每页数量
    - cookie: 用户自己的cookie，可选参数，用于接口返回数据的个性化推荐。
    ### 返回:
    - 首页推荐作品

    # [English]
    ### Purpose:
    - Home Feed
    ### Parameters:
    - count: Number per page
    - cookie: User's own cookie, optional parameter, used for personalized recommendations of interface
    return data.
    ### Return:
    - Home Feed

    # [示例/Example]
    count = 15
    Cookie = \"Your_Cookie\"

    Args:
        body (BodyFetchHomeFeedApiV1TiktokWebFetchHomeFeedPost):

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
    body: BodyFetchHomeFeedApiV1TiktokWebFetchHomeFeedPost,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""首页推荐作品/Home Feed

     # [中文]
    ### 用途:
    - 首页推荐作品
    ### 参数:
    - count: 每页数量
    - cookie: 用户自己的cookie，可选参数，用于接口返回数据的个性化推荐。
    ### 返回:
    - 首页推荐作品

    # [English]
    ### Purpose:
    - Home Feed
    ### Parameters:
    - count: Number per page
    - cookie: User's own cookie, optional parameter, used for personalized recommendations of interface
    return data.
    ### Return:
    - Home Feed

    # [示例/Example]
    count = 15
    Cookie = \"Your_Cookie\"

    Args:
        body (BodyFetchHomeFeedApiV1TiktokWebFetchHomeFeedPost):

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
    body: BodyFetchHomeFeedApiV1TiktokWebFetchHomeFeedPost,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""首页推荐作品/Home Feed

     # [中文]
    ### 用途:
    - 首页推荐作品
    ### 参数:
    - count: 每页数量
    - cookie: 用户自己的cookie，可选参数，用于接口返回数据的个性化推荐。
    ### 返回:
    - 首页推荐作品

    # [English]
    ### Purpose:
    - Home Feed
    ### Parameters:
    - count: Number per page
    - cookie: User's own cookie, optional parameter, used for personalized recommendations of interface
    return data.
    ### Return:
    - Home Feed

    # [示例/Example]
    count = 15
    Cookie = \"Your_Cookie\"

    Args:
        body (BodyFetchHomeFeedApiV1TiktokWebFetchHomeFeedPost):

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
    body: BodyFetchHomeFeedApiV1TiktokWebFetchHomeFeedPost,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""首页推荐作品/Home Feed

     # [中文]
    ### 用途:
    - 首页推荐作品
    ### 参数:
    - count: 每页数量
    - cookie: 用户自己的cookie，可选参数，用于接口返回数据的个性化推荐。
    ### 返回:
    - 首页推荐作品

    # [English]
    ### Purpose:
    - Home Feed
    ### Parameters:
    - count: Number per page
    - cookie: User's own cookie, optional parameter, used for personalized recommendations of interface
    return data.
    ### Return:
    - Home Feed

    # [示例/Example]
    count = 15
    Cookie = \"Your_Cookie\"

    Args:
        body (BodyFetchHomeFeedApiV1TiktokWebFetchHomeFeedPost):

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
