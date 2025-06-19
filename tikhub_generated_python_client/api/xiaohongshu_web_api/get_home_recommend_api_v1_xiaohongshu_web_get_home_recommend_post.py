from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_home_feed_request import GetHomeFeedRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: GetHomeFeedRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/xiaohongshu/web/get_home_recommend",
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
    body: GetHomeFeedRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取首页推荐/Get home recommend

     # [中文]
    ### 用途:
    - 获取首页推荐
    ### 参数:
    - feed_type: 推荐类型
        - 全部: 0
        - 穿搭: 1
        - 美食: 2
        - 彩妆: 3
        - 影视: 4
        - 职场: 5
        - 情感: 6
        - 家居: 7
        - 游戏: 8
        - 旅行: 9
        - 健身: 10
    - need_filter_image: 是否只看图文笔记，默认为 False
    - cookie: 可选参数，用户自行提供的已登录的网页Cookie获取个性化推荐，如果不提供，则使用游客模式
    - proxy: 可选参数，网络代理，可降低封号概率，格式：http://用户名:密码@IP:端口/Proxy, format: http://username:password@IP:port
    ### 返回:
    - 推荐列表

    # [English]
    ### Purpose:
    - Get home recommend
    ### Parameters:
    - feed_type: Feed type
        - Dress: 1
        - Food: 2
        - Makeup: 3
        - Film: 4
        - Workplace: 5
        - Emotion: 6
        - Home: 7
        - Game: 8
        - Travel: 9
        - Fitness: 10
    - need_filter_image: Whether to view only image notes, default is False
    - cookie: Optional parameter, user-provided logged-in web Cookie to get personalized
    recommendations, if not provided, use visitor mode
    - proxy: Optional parameter, network proxy, can reduce the probability of account ban, format:
    http://username:password@IP:port
    ### Return:
    - Recommend list

    # [示例/Example]
    feed_type=\"0\"
    need_filter_image=False

    Args:
        body (GetHomeFeedRequest):

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
    body: GetHomeFeedRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取首页推荐/Get home recommend

     # [中文]
    ### 用途:
    - 获取首页推荐
    ### 参数:
    - feed_type: 推荐类型
        - 全部: 0
        - 穿搭: 1
        - 美食: 2
        - 彩妆: 3
        - 影视: 4
        - 职场: 5
        - 情感: 6
        - 家居: 7
        - 游戏: 8
        - 旅行: 9
        - 健身: 10
    - need_filter_image: 是否只看图文笔记，默认为 False
    - cookie: 可选参数，用户自行提供的已登录的网页Cookie获取个性化推荐，如果不提供，则使用游客模式
    - proxy: 可选参数，网络代理，可降低封号概率，格式：http://用户名:密码@IP:端口/Proxy, format: http://username:password@IP:port
    ### 返回:
    - 推荐列表

    # [English]
    ### Purpose:
    - Get home recommend
    ### Parameters:
    - feed_type: Feed type
        - Dress: 1
        - Food: 2
        - Makeup: 3
        - Film: 4
        - Workplace: 5
        - Emotion: 6
        - Home: 7
        - Game: 8
        - Travel: 9
        - Fitness: 10
    - need_filter_image: Whether to view only image notes, default is False
    - cookie: Optional parameter, user-provided logged-in web Cookie to get personalized
    recommendations, if not provided, use visitor mode
    - proxy: Optional parameter, network proxy, can reduce the probability of account ban, format:
    http://username:password@IP:port
    ### Return:
    - Recommend list

    # [示例/Example]
    feed_type=\"0\"
    need_filter_image=False

    Args:
        body (GetHomeFeedRequest):

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
    body: GetHomeFeedRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取首页推荐/Get home recommend

     # [中文]
    ### 用途:
    - 获取首页推荐
    ### 参数:
    - feed_type: 推荐类型
        - 全部: 0
        - 穿搭: 1
        - 美食: 2
        - 彩妆: 3
        - 影视: 4
        - 职场: 5
        - 情感: 6
        - 家居: 7
        - 游戏: 8
        - 旅行: 9
        - 健身: 10
    - need_filter_image: 是否只看图文笔记，默认为 False
    - cookie: 可选参数，用户自行提供的已登录的网页Cookie获取个性化推荐，如果不提供，则使用游客模式
    - proxy: 可选参数，网络代理，可降低封号概率，格式：http://用户名:密码@IP:端口/Proxy, format: http://username:password@IP:port
    ### 返回:
    - 推荐列表

    # [English]
    ### Purpose:
    - Get home recommend
    ### Parameters:
    - feed_type: Feed type
        - Dress: 1
        - Food: 2
        - Makeup: 3
        - Film: 4
        - Workplace: 5
        - Emotion: 6
        - Home: 7
        - Game: 8
        - Travel: 9
        - Fitness: 10
    - need_filter_image: Whether to view only image notes, default is False
    - cookie: Optional parameter, user-provided logged-in web Cookie to get personalized
    recommendations, if not provided, use visitor mode
    - proxy: Optional parameter, network proxy, can reduce the probability of account ban, format:
    http://username:password@IP:port
    ### Return:
    - Recommend list

    # [示例/Example]
    feed_type=\"0\"
    need_filter_image=False

    Args:
        body (GetHomeFeedRequest):

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
    body: GetHomeFeedRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取首页推荐/Get home recommend

     # [中文]
    ### 用途:
    - 获取首页推荐
    ### 参数:
    - feed_type: 推荐类型
        - 全部: 0
        - 穿搭: 1
        - 美食: 2
        - 彩妆: 3
        - 影视: 4
        - 职场: 5
        - 情感: 6
        - 家居: 7
        - 游戏: 8
        - 旅行: 9
        - 健身: 10
    - need_filter_image: 是否只看图文笔记，默认为 False
    - cookie: 可选参数，用户自行提供的已登录的网页Cookie获取个性化推荐，如果不提供，则使用游客模式
    - proxy: 可选参数，网络代理，可降低封号概率，格式：http://用户名:密码@IP:端口/Proxy, format: http://username:password@IP:port
    ### 返回:
    - 推荐列表

    # [English]
    ### Purpose:
    - Get home recommend
    ### Parameters:
    - feed_type: Feed type
        - Dress: 1
        - Food: 2
        - Makeup: 3
        - Film: 4
        - Workplace: 5
        - Emotion: 6
        - Home: 7
        - Game: 8
        - Travel: 9
        - Fitness: 10
    - need_filter_image: Whether to view only image notes, default is False
    - cookie: Optional parameter, user-provided logged-in web Cookie to get personalized
    recommendations, if not provided, use visitor mode
    - proxy: Optional parameter, network proxy, can reduce the probability of account ban, format:
    http://username:password@IP:port
    ### Return:
    - Recommend list

    # [示例/Example]
    feed_type=\"0\"
    need_filter_image=False

    Args:
        body (GetHomeFeedRequest):

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
