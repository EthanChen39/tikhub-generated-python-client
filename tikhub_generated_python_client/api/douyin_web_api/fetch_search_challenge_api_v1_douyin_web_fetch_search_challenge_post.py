from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...models.search_challenge_request import SearchChallengeRequest
from ...types import Response


def _get_kwargs(
    *,
    body: SearchChallengeRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/douyin/web/fetch_search_challenge",
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
    body: SearchChallengeRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索话题/Search Challenge

     # [中文]
    ### 用途:
    - 搜索话题，此接口不带Cookie请求时只能获取到前30条数据，建议自行提供Cookie获取更多数据。
    - Cookie获取方式：打开网页抖音，登录后，按F12打开开发者工具，点击Network，刷新页面，找到第一个请求，复制Cookie。
    ### 参数:
    - keyword: 关键词
    - cursor: 偏移量
    - count: 数量
    - cookie: 用户自行提供的Cookie，用于获取更多数据。
    ### 返回:
    - 话题搜索结果

    # [English]
    ### Purpose:
    - Search Challenge, when this interface is requested without Cookie, only the first 30 data can be
    obtained, it is recommended to provide Cookie to get more data.
    - Cookie acquisition method: Open the Douyin webpage, log in, press F12 to open the developer tool,
    click Network, refresh the page, find the first request, copy the Cookie.
    ### Parameters:
    - keyword: Keyword
    - cursor: Offset
    - count: Number
    - cookie: User provided Cookie, used to get more data.
    ### Return:
    - Challenge search results

    # [示例/Example]
    keyword = \"动漫\"
    cursor = 0
    count = 20

    Args:
        body (SearchChallengeRequest):

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
    body: SearchChallengeRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索话题/Search Challenge

     # [中文]
    ### 用途:
    - 搜索话题，此接口不带Cookie请求时只能获取到前30条数据，建议自行提供Cookie获取更多数据。
    - Cookie获取方式：打开网页抖音，登录后，按F12打开开发者工具，点击Network，刷新页面，找到第一个请求，复制Cookie。
    ### 参数:
    - keyword: 关键词
    - cursor: 偏移量
    - count: 数量
    - cookie: 用户自行提供的Cookie，用于获取更多数据。
    ### 返回:
    - 话题搜索结果

    # [English]
    ### Purpose:
    - Search Challenge, when this interface is requested without Cookie, only the first 30 data can be
    obtained, it is recommended to provide Cookie to get more data.
    - Cookie acquisition method: Open the Douyin webpage, log in, press F12 to open the developer tool,
    click Network, refresh the page, find the first request, copy the Cookie.
    ### Parameters:
    - keyword: Keyword
    - cursor: Offset
    - count: Number
    - cookie: User provided Cookie, used to get more data.
    ### Return:
    - Challenge search results

    # [示例/Example]
    keyword = \"动漫\"
    cursor = 0
    count = 20

    Args:
        body (SearchChallengeRequest):

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
    body: SearchChallengeRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索话题/Search Challenge

     # [中文]
    ### 用途:
    - 搜索话题，此接口不带Cookie请求时只能获取到前30条数据，建议自行提供Cookie获取更多数据。
    - Cookie获取方式：打开网页抖音，登录后，按F12打开开发者工具，点击Network，刷新页面，找到第一个请求，复制Cookie。
    ### 参数:
    - keyword: 关键词
    - cursor: 偏移量
    - count: 数量
    - cookie: 用户自行提供的Cookie，用于获取更多数据。
    ### 返回:
    - 话题搜索结果

    # [English]
    ### Purpose:
    - Search Challenge, when this interface is requested without Cookie, only the first 30 data can be
    obtained, it is recommended to provide Cookie to get more data.
    - Cookie acquisition method: Open the Douyin webpage, log in, press F12 to open the developer tool,
    click Network, refresh the page, find the first request, copy the Cookie.
    ### Parameters:
    - keyword: Keyword
    - cursor: Offset
    - count: Number
    - cookie: User provided Cookie, used to get more data.
    ### Return:
    - Challenge search results

    # [示例/Example]
    keyword = \"动漫\"
    cursor = 0
    count = 20

    Args:
        body (SearchChallengeRequest):

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
    body: SearchChallengeRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索话题/Search Challenge

     # [中文]
    ### 用途:
    - 搜索话题，此接口不带Cookie请求时只能获取到前30条数据，建议自行提供Cookie获取更多数据。
    - Cookie获取方式：打开网页抖音，登录后，按F12打开开发者工具，点击Network，刷新页面，找到第一个请求，复制Cookie。
    ### 参数:
    - keyword: 关键词
    - cursor: 偏移量
    - count: 数量
    - cookie: 用户自行提供的Cookie，用于获取更多数据。
    ### 返回:
    - 话题搜索结果

    # [English]
    ### Purpose:
    - Search Challenge, when this interface is requested without Cookie, only the first 30 data can be
    obtained, it is recommended to provide Cookie to get more data.
    - Cookie acquisition method: Open the Douyin webpage, log in, press F12 to open the developer tool,
    click Network, refresh the page, find the first request, copy the Cookie.
    ### Parameters:
    - keyword: Keyword
    - cursor: Offset
    - count: Number
    - cookie: User provided Cookie, used to get more data.
    ### Return:
    - Challenge search results

    # [示例/Example]
    keyword = \"动漫\"
    cursor = 0
    count = 20

    Args:
        body (SearchChallengeRequest):

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
