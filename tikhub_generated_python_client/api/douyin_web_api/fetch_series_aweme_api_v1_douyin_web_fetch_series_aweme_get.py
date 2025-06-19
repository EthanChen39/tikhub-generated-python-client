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
    offset: int,
    count: int,
    content_type: int,
    cookie: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["offset"] = offset

    params["count"] = count

    params["content_type"] = content_type

    params["cookie"] = cookie

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/douyin/web/fetch_series_aweme",
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
    offset: int,
    count: int,
    content_type: int,
    cookie: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """短剧作品/Series Video

     # [中文]
    ### 用途:
    - 短剧作品
    ### 参数:
    - offset: 页码，默认为0
    - count: 每页数量，默认为16
    - content_type: 子类型，默认为0
        - 0: 热榜
        - 101: 甜宠
        - 102: 搞笑
        - 104: 正能量
        - 105: 成长
        - 106: 悬疑
        - 109: 家庭
        - 110: 都市
        - 112: 奇幻
        - 113: 玄幻
        - 114: 职场
        - 115: 青春
        - 116: 古装
        - 117: 动作
        - 119: 逆袭
        - 124: 其他
    - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题
    - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie
    ### 返回:
    - 短剧作品数据

    # [English]
    ### Purpose:
    - Series Video
    ### Parameters:
    - offset: Page number, default is 0
    - count: Number per page, default is 16
    - content_type: Subtype, default is 0
        - 0: Hot list
        - 101: Sweet pet
        - 102: Funny
        - 104: Positive energy
        - 105: Growth
        - 106: Suspense
        - 109: Family
        - 110: Urban
        - 112: Fantasy
        - 113: Fantasy
        - 114: Workplace
        - 115: Youth
        - 116: Ancient costume
        - 117: Action
        - 119: Counterattack
        - 124: Other
    - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may
    be a problem of data duplication when paging
    - Guest cookie acquisition interface:
    https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie

    ### Return:
    - Series Video data

    Args:
        offset (int): 页码/Page number
        count (int): 每页数量/Number per page
        content_type (int): 短剧类型/Subtype
        cookie (Union[Unset, str]): 用户自行提供的Cookie/User provided Cookie

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        offset=offset,
        count=count,
        content_type=content_type,
        cookie=cookie,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    offset: int,
    count: int,
    content_type: int,
    cookie: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """短剧作品/Series Video

     # [中文]
    ### 用途:
    - 短剧作品
    ### 参数:
    - offset: 页码，默认为0
    - count: 每页数量，默认为16
    - content_type: 子类型，默认为0
        - 0: 热榜
        - 101: 甜宠
        - 102: 搞笑
        - 104: 正能量
        - 105: 成长
        - 106: 悬疑
        - 109: 家庭
        - 110: 都市
        - 112: 奇幻
        - 113: 玄幻
        - 114: 职场
        - 115: 青春
        - 116: 古装
        - 117: 动作
        - 119: 逆袭
        - 124: 其他
    - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题
    - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie
    ### 返回:
    - 短剧作品数据

    # [English]
    ### Purpose:
    - Series Video
    ### Parameters:
    - offset: Page number, default is 0
    - count: Number per page, default is 16
    - content_type: Subtype, default is 0
        - 0: Hot list
        - 101: Sweet pet
        - 102: Funny
        - 104: Positive energy
        - 105: Growth
        - 106: Suspense
        - 109: Family
        - 110: Urban
        - 112: Fantasy
        - 113: Fantasy
        - 114: Workplace
        - 115: Youth
        - 116: Ancient costume
        - 117: Action
        - 119: Counterattack
        - 124: Other
    - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may
    be a problem of data duplication when paging
    - Guest cookie acquisition interface:
    https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie

    ### Return:
    - Series Video data

    Args:
        offset (int): 页码/Page number
        count (int): 每页数量/Number per page
        content_type (int): 短剧类型/Subtype
        cookie (Union[Unset, str]): 用户自行提供的Cookie/User provided Cookie

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        offset=offset,
        count=count,
        content_type=content_type,
        cookie=cookie,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    offset: int,
    count: int,
    content_type: int,
    cookie: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    """短剧作品/Series Video

     # [中文]
    ### 用途:
    - 短剧作品
    ### 参数:
    - offset: 页码，默认为0
    - count: 每页数量，默认为16
    - content_type: 子类型，默认为0
        - 0: 热榜
        - 101: 甜宠
        - 102: 搞笑
        - 104: 正能量
        - 105: 成长
        - 106: 悬疑
        - 109: 家庭
        - 110: 都市
        - 112: 奇幻
        - 113: 玄幻
        - 114: 职场
        - 115: 青春
        - 116: 古装
        - 117: 动作
        - 119: 逆袭
        - 124: 其他
    - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题
    - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie
    ### 返回:
    - 短剧作品数据

    # [English]
    ### Purpose:
    - Series Video
    ### Parameters:
    - offset: Page number, default is 0
    - count: Number per page, default is 16
    - content_type: Subtype, default is 0
        - 0: Hot list
        - 101: Sweet pet
        - 102: Funny
        - 104: Positive energy
        - 105: Growth
        - 106: Suspense
        - 109: Family
        - 110: Urban
        - 112: Fantasy
        - 113: Fantasy
        - 114: Workplace
        - 115: Youth
        - 116: Ancient costume
        - 117: Action
        - 119: Counterattack
        - 124: Other
    - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may
    be a problem of data duplication when paging
    - Guest cookie acquisition interface:
    https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie

    ### Return:
    - Series Video data

    Args:
        offset (int): 页码/Page number
        count (int): 每页数量/Number per page
        content_type (int): 短剧类型/Subtype
        cookie (Union[Unset, str]): 用户自行提供的Cookie/User provided Cookie

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        offset=offset,
        count=count,
        content_type=content_type,
        cookie=cookie,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    offset: int,
    count: int,
    content_type: int,
    cookie: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    """短剧作品/Series Video

     # [中文]
    ### 用途:
    - 短剧作品
    ### 参数:
    - offset: 页码，默认为0
    - count: 每页数量，默认为16
    - content_type: 子类型，默认为0
        - 0: 热榜
        - 101: 甜宠
        - 102: 搞笑
        - 104: 正能量
        - 105: 成长
        - 106: 悬疑
        - 109: 家庭
        - 110: 都市
        - 112: 奇幻
        - 113: 玄幻
        - 114: 职场
        - 115: 青春
        - 116: 古装
        - 117: 动作
        - 119: 逆袭
        - 124: 其他
    - cookie: 用户自行提供的Cookie，推荐使用自己的抖音Cookie，否则在翻页时可能会出现数据重复的问题
    - 游客cookie获取接口：https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie
    ### 返回:
    - 短剧作品数据

    # [English]
    ### Purpose:
    - Series Video
    ### Parameters:
    - offset: Page number, default is 0
    - count: Number per page, default is 16
    - content_type: Subtype, default is 0
        - 0: Hot list
        - 101: Sweet pet
        - 102: Funny
        - 104: Positive energy
        - 105: Growth
        - 106: Suspense
        - 109: Family
        - 110: Urban
        - 112: Fantasy
        - 113: Fantasy
        - 114: Workplace
        - 115: Youth
        - 116: Ancient costume
        - 117: Action
        - 119: Counterattack
        - 124: Other
    - cookie: User provided Cookie, it is recommended to use your own Douyin Cookie, otherwise there may
    be a problem of data duplication when paging
    - Guest cookie acquisition interface:
    https://api.tikhub.io/api/v1/douyin/web/fetch_douyin_web_guest_cookie

    ### Return:
    - Series Video data

    Args:
        offset (int): 页码/Page number
        count (int): 每页数量/Number per page
        content_type (int): 短剧类型/Subtype
        cookie (Union[Unset, str]): 用户自行提供的Cookie/User provided Cookie

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            count=count,
            content_type=content_type,
            cookie=cookie,
        )
    ).parsed
