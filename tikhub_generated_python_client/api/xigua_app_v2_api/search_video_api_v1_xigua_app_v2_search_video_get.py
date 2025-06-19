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
    offset: Union[Unset, int] = 0,
    order_type: Union[Unset, str] = UNSET,
    min_duration: Union[Unset, int] = UNSET,
    max_duration: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["offset"] = offset

    params["order_type"] = order_type

    params["min_duration"] = min_duration

    params["max_duration"] = max_duration

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/xigua/app/v2/search_video",
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
    offset: Union[Unset, int] = 0,
    order_type: Union[Unset, str] = UNSET,
    min_duration: Union[Unset, int] = UNSET,
    max_duration: Union[Unset, int] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索视频/Search video

     # [中文]
    ### 用途:
    - 搜索视频
    ### 参数:
    - keyword: 关键词
    - offset: 偏移量，第一次请求传0，后续请求传上一次请求返回的offset
    - order_type: 排序方式，为空时按照默认排序，以下为可选排序方式。
        - 最新: publish_time
        - 最热: play_count
    - min_duration: 最小时长，默认空，单位秒。
    - max_duration: 最大时长，默认空，单位秒。
    ### 返回:
    - 视频列表

    # [English]
    ### Purpose:
    - Search video
    ### Parameters:
    - keyword: Keyword
    - offset: Offset, pass 0 for the first request, pass the offset returned by the previous request for
    subsequent requests
    - order_type: Order type, empty for default sorting, the following are optional sorting methods.
        - Newest: publish_time
        - Hottest: play_count
    - min_duration: Minimum duration, default empty, in seconds.
    - max_duration: Maximum duration, default empty, in seconds.
    ### Return:
    - Video list

    # [示例/Example]
    > 搜索关键字为“抖音”的视频，按照播放量排序，时长1-180秒(1-3分钟)
    > Search for videos with the keyword \"抖音\", sorted by play count, duration 1-180 seconds (1-3
    minutes)
    keyword: \"抖音\"
    order_type: \"play_count\"
    min_duration: 1
    max_duration: 180

    Args:
        keyword (str): 关键词/Keyword
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        order_type (Union[Unset, str]): 排序方式/Order type
        min_duration (Union[Unset, int]): 最小时长/Minimum duration
        max_duration (Union[Unset, int]): 最大时长/Maximum duration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        offset=offset,
        order_type=order_type,
        min_duration=min_duration,
        max_duration=max_duration,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    keyword: str,
    offset: Union[Unset, int] = 0,
    order_type: Union[Unset, str] = UNSET,
    min_duration: Union[Unset, int] = UNSET,
    max_duration: Union[Unset, int] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索视频/Search video

     # [中文]
    ### 用途:
    - 搜索视频
    ### 参数:
    - keyword: 关键词
    - offset: 偏移量，第一次请求传0，后续请求传上一次请求返回的offset
    - order_type: 排序方式，为空时按照默认排序，以下为可选排序方式。
        - 最新: publish_time
        - 最热: play_count
    - min_duration: 最小时长，默认空，单位秒。
    - max_duration: 最大时长，默认空，单位秒。
    ### 返回:
    - 视频列表

    # [English]
    ### Purpose:
    - Search video
    ### Parameters:
    - keyword: Keyword
    - offset: Offset, pass 0 for the first request, pass the offset returned by the previous request for
    subsequent requests
    - order_type: Order type, empty for default sorting, the following are optional sorting methods.
        - Newest: publish_time
        - Hottest: play_count
    - min_duration: Minimum duration, default empty, in seconds.
    - max_duration: Maximum duration, default empty, in seconds.
    ### Return:
    - Video list

    # [示例/Example]
    > 搜索关键字为“抖音”的视频，按照播放量排序，时长1-180秒(1-3分钟)
    > Search for videos with the keyword \"抖音\", sorted by play count, duration 1-180 seconds (1-3
    minutes)
    keyword: \"抖音\"
    order_type: \"play_count\"
    min_duration: 1
    max_duration: 180

    Args:
        keyword (str): 关键词/Keyword
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        order_type (Union[Unset, str]): 排序方式/Order type
        min_duration (Union[Unset, int]): 最小时长/Minimum duration
        max_duration (Union[Unset, int]): 最大时长/Maximum duration

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
        order_type=order_type,
        min_duration=min_duration,
        max_duration=max_duration,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    offset: Union[Unset, int] = 0,
    order_type: Union[Unset, str] = UNSET,
    min_duration: Union[Unset, int] = UNSET,
    max_duration: Union[Unset, int] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索视频/Search video

     # [中文]
    ### 用途:
    - 搜索视频
    ### 参数:
    - keyword: 关键词
    - offset: 偏移量，第一次请求传0，后续请求传上一次请求返回的offset
    - order_type: 排序方式，为空时按照默认排序，以下为可选排序方式。
        - 最新: publish_time
        - 最热: play_count
    - min_duration: 最小时长，默认空，单位秒。
    - max_duration: 最大时长，默认空，单位秒。
    ### 返回:
    - 视频列表

    # [English]
    ### Purpose:
    - Search video
    ### Parameters:
    - keyword: Keyword
    - offset: Offset, pass 0 for the first request, pass the offset returned by the previous request for
    subsequent requests
    - order_type: Order type, empty for default sorting, the following are optional sorting methods.
        - Newest: publish_time
        - Hottest: play_count
    - min_duration: Minimum duration, default empty, in seconds.
    - max_duration: Maximum duration, default empty, in seconds.
    ### Return:
    - Video list

    # [示例/Example]
    > 搜索关键字为“抖音”的视频，按照播放量排序，时长1-180秒(1-3分钟)
    > Search for videos with the keyword \"抖音\", sorted by play count, duration 1-180 seconds (1-3
    minutes)
    keyword: \"抖音\"
    order_type: \"play_count\"
    min_duration: 1
    max_duration: 180

    Args:
        keyword (str): 关键词/Keyword
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        order_type (Union[Unset, str]): 排序方式/Order type
        min_duration (Union[Unset, int]): 最小时长/Minimum duration
        max_duration (Union[Unset, int]): 最大时长/Maximum duration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        offset=offset,
        order_type=order_type,
        min_duration=min_duration,
        max_duration=max_duration,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
    offset: Union[Unset, int] = 0,
    order_type: Union[Unset, str] = UNSET,
    min_duration: Union[Unset, int] = UNSET,
    max_duration: Union[Unset, int] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""搜索视频/Search video

     # [中文]
    ### 用途:
    - 搜索视频
    ### 参数:
    - keyword: 关键词
    - offset: 偏移量，第一次请求传0，后续请求传上一次请求返回的offset
    - order_type: 排序方式，为空时按照默认排序，以下为可选排序方式。
        - 最新: publish_time
        - 最热: play_count
    - min_duration: 最小时长，默认空，单位秒。
    - max_duration: 最大时长，默认空，单位秒。
    ### 返回:
    - 视频列表

    # [English]
    ### Purpose:
    - Search video
    ### Parameters:
    - keyword: Keyword
    - offset: Offset, pass 0 for the first request, pass the offset returned by the previous request for
    subsequent requests
    - order_type: Order type, empty for default sorting, the following are optional sorting methods.
        - Newest: publish_time
        - Hottest: play_count
    - min_duration: Minimum duration, default empty, in seconds.
    - max_duration: Maximum duration, default empty, in seconds.
    ### Return:
    - Video list

    # [示例/Example]
    > 搜索关键字为“抖音”的视频，按照播放量排序，时长1-180秒(1-3分钟)
    > Search for videos with the keyword \"抖音\", sorted by play count, duration 1-180 seconds (1-3
    minutes)
    keyword: \"抖音\"
    order_type: \"play_count\"
    min_duration: 1
    max_duration: 180

    Args:
        keyword (str): 关键词/Keyword
        offset (Union[Unset, int]): 偏移量/Offset Default: 0.
        order_type (Union[Unset, str]): 排序方式/Order type
        min_duration (Union[Unset, int]): 最小时长/Minimum duration
        max_duration (Union[Unset, int]): 最大时长/Maximum duration

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
            order_type=order_type,
            min_duration=min_duration,
            max_duration=max_duration,
        )
    ).parsed
