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
    channel_id: str,
    lang: Union[Unset, str] = "en-US",
    sort_by: Union[Unset, str] = "newest",
    content_type: Union[Unset, str] = "videos",
    next_token: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["channel_id"] = channel_id

    params["lang"] = lang

    params["sortBy"] = sort_by

    params["contentType"] = content_type

    params["nextToken"] = next_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/youtube/web/get_channel_videos_v2",
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
    channel_id: str,
    lang: Union[Unset, str] = "en-US",
    sort_by: Union[Unset, str] = "newest",
    content_type: Union[Unset, str] = "videos",
    next_token: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取频道视频 V2/Get channel videos V2

     # [中文]

    ### 用途:
    - 获取频道视频 V2，支持获取频道视频列表，频道短视频列表，频道直播列表。

    ### 参数:
    - channel_id: 频道ID或频道名称，如果是频道名称，则需要在前面加上 `@` 符号，例如：@LinusTechTips。
    - lang: 视频结果语言代码，默认为 `en-US`，任何语言代码均可，当提交不支持的语言代码时，默认使用 `en-US` 作为语言代码。
    - sortBy: 排序方式，默认为 `newest`，可选值为 `newest` 和 `oldest` 和 `mostPopular`：
        - newest: 按照最新排序，默认值。
        - oldest: 按照最旧排序。
        - mostPopular: 按照最热排序。
    - contentType: 内容类型，默认为 `videos`，可选值为 `videos` 和 `shorts` 和 `live`：
        - videos: 视频列表，默认值。
        - shorts: 短视频列表。
        - live: 直播列表。
    - nextToken: 用于继续获取视频的令牌。可选参数，默认值为空，从第一页开始获取。
        - 如果获取第一页，则nextToken参数为None。
        - 如果获取第二页，则nextToken参数为第一页请求返回的nextToken。

    ### 返回:
    - 频道视频列表，包含视频ID、标题、缩略图、观看次数、点赞次数、评论数、视频时长等信息。

    # [English]

    ### Purpose:
    - Get channel videos V2, support getting channel video list, channel short video list, channel live
    list.

    ### Parameters:
    - channel_id: Channel ID or channel name, if it is a channel name, add `@` symbol in front of it,
    for example: @LinusTechTips.
    - lang: Video result language code, default is `en-US`, any language code is supported, when
    submitting unsupported language code, default use `en-US` as language code.
    - sortBy: Sort by, default is `newest`, optional values are `newest` and `oldest` and `mostPopular`:
        - newest: Sort by newest, default value.
        - oldest: Sort by oldest.
        - mostPopular: Sort by most popular.
    - contentType: Content type, default is `videos`, optional values are `videos`
        - videos: Video list, default value.
        - shorts: Short video list.
        - live: Live list.
    - nextToken: Token to continue fetching videos. Optional parameter, default value is empty, start
    from the first page.
        - If fetching the first page, the nextToken parameter is None.
        - If fetching the second page, the nextToken parameter is the nextToken returned by the first
    page request.
    ### Returns:
    - Channel video list, including video ID, title, thumbnail, view count, like count, comment count,
    video duration and other information.

    # [示例/Example]
    channel_id = \"UCXuqSBlHAE6Xw-yeJA0Tunw\"
    lang = \"en-US\"
    sortBy = \"newest\"
    contentType = \"videos\"
    nextToken = None

    Args:
        channel_id (str): 频道ID/Channel ID
        lang (Union[Unset, str]): 视频结果语言代码/Video result language code Default: 'en-US'.
        sort_by (Union[Unset, str]): 排序方式/Sort by Default: 'newest'.
        content_type (Union[Unset, str]): 内容类型/Content type Default: 'videos'.
        next_token (Union[Unset, str]): 翻页令牌/Pagination token Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        lang=lang,
        sort_by=sort_by,
        content_type=content_type,
        next_token=next_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    channel_id: str,
    lang: Union[Unset, str] = "en-US",
    sort_by: Union[Unset, str] = "newest",
    content_type: Union[Unset, str] = "videos",
    next_token: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取频道视频 V2/Get channel videos V2

     # [中文]

    ### 用途:
    - 获取频道视频 V2，支持获取频道视频列表，频道短视频列表，频道直播列表。

    ### 参数:
    - channel_id: 频道ID或频道名称，如果是频道名称，则需要在前面加上 `@` 符号，例如：@LinusTechTips。
    - lang: 视频结果语言代码，默认为 `en-US`，任何语言代码均可，当提交不支持的语言代码时，默认使用 `en-US` 作为语言代码。
    - sortBy: 排序方式，默认为 `newest`，可选值为 `newest` 和 `oldest` 和 `mostPopular`：
        - newest: 按照最新排序，默认值。
        - oldest: 按照最旧排序。
        - mostPopular: 按照最热排序。
    - contentType: 内容类型，默认为 `videos`，可选值为 `videos` 和 `shorts` 和 `live`：
        - videos: 视频列表，默认值。
        - shorts: 短视频列表。
        - live: 直播列表。
    - nextToken: 用于继续获取视频的令牌。可选参数，默认值为空，从第一页开始获取。
        - 如果获取第一页，则nextToken参数为None。
        - 如果获取第二页，则nextToken参数为第一页请求返回的nextToken。

    ### 返回:
    - 频道视频列表，包含视频ID、标题、缩略图、观看次数、点赞次数、评论数、视频时长等信息。

    # [English]

    ### Purpose:
    - Get channel videos V2, support getting channel video list, channel short video list, channel live
    list.

    ### Parameters:
    - channel_id: Channel ID or channel name, if it is a channel name, add `@` symbol in front of it,
    for example: @LinusTechTips.
    - lang: Video result language code, default is `en-US`, any language code is supported, when
    submitting unsupported language code, default use `en-US` as language code.
    - sortBy: Sort by, default is `newest`, optional values are `newest` and `oldest` and `mostPopular`:
        - newest: Sort by newest, default value.
        - oldest: Sort by oldest.
        - mostPopular: Sort by most popular.
    - contentType: Content type, default is `videos`, optional values are `videos`
        - videos: Video list, default value.
        - shorts: Short video list.
        - live: Live list.
    - nextToken: Token to continue fetching videos. Optional parameter, default value is empty, start
    from the first page.
        - If fetching the first page, the nextToken parameter is None.
        - If fetching the second page, the nextToken parameter is the nextToken returned by the first
    page request.
    ### Returns:
    - Channel video list, including video ID, title, thumbnail, view count, like count, comment count,
    video duration and other information.

    # [示例/Example]
    channel_id = \"UCXuqSBlHAE6Xw-yeJA0Tunw\"
    lang = \"en-US\"
    sortBy = \"newest\"
    contentType = \"videos\"
    nextToken = None

    Args:
        channel_id (str): 频道ID/Channel ID
        lang (Union[Unset, str]): 视频结果语言代码/Video result language code Default: 'en-US'.
        sort_by (Union[Unset, str]): 排序方式/Sort by Default: 'newest'.
        content_type (Union[Unset, str]): 内容类型/Content type Default: 'videos'.
        next_token (Union[Unset, str]): 翻页令牌/Pagination token Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        channel_id=channel_id,
        lang=lang,
        sort_by=sort_by,
        content_type=content_type,
        next_token=next_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    channel_id: str,
    lang: Union[Unset, str] = "en-US",
    sort_by: Union[Unset, str] = "newest",
    content_type: Union[Unset, str] = "videos",
    next_token: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取频道视频 V2/Get channel videos V2

     # [中文]

    ### 用途:
    - 获取频道视频 V2，支持获取频道视频列表，频道短视频列表，频道直播列表。

    ### 参数:
    - channel_id: 频道ID或频道名称，如果是频道名称，则需要在前面加上 `@` 符号，例如：@LinusTechTips。
    - lang: 视频结果语言代码，默认为 `en-US`，任何语言代码均可，当提交不支持的语言代码时，默认使用 `en-US` 作为语言代码。
    - sortBy: 排序方式，默认为 `newest`，可选值为 `newest` 和 `oldest` 和 `mostPopular`：
        - newest: 按照最新排序，默认值。
        - oldest: 按照最旧排序。
        - mostPopular: 按照最热排序。
    - contentType: 内容类型，默认为 `videos`，可选值为 `videos` 和 `shorts` 和 `live`：
        - videos: 视频列表，默认值。
        - shorts: 短视频列表。
        - live: 直播列表。
    - nextToken: 用于继续获取视频的令牌。可选参数，默认值为空，从第一页开始获取。
        - 如果获取第一页，则nextToken参数为None。
        - 如果获取第二页，则nextToken参数为第一页请求返回的nextToken。

    ### 返回:
    - 频道视频列表，包含视频ID、标题、缩略图、观看次数、点赞次数、评论数、视频时长等信息。

    # [English]

    ### Purpose:
    - Get channel videos V2, support getting channel video list, channel short video list, channel live
    list.

    ### Parameters:
    - channel_id: Channel ID or channel name, if it is a channel name, add `@` symbol in front of it,
    for example: @LinusTechTips.
    - lang: Video result language code, default is `en-US`, any language code is supported, when
    submitting unsupported language code, default use `en-US` as language code.
    - sortBy: Sort by, default is `newest`, optional values are `newest` and `oldest` and `mostPopular`:
        - newest: Sort by newest, default value.
        - oldest: Sort by oldest.
        - mostPopular: Sort by most popular.
    - contentType: Content type, default is `videos`, optional values are `videos`
        - videos: Video list, default value.
        - shorts: Short video list.
        - live: Live list.
    - nextToken: Token to continue fetching videos. Optional parameter, default value is empty, start
    from the first page.
        - If fetching the first page, the nextToken parameter is None.
        - If fetching the second page, the nextToken parameter is the nextToken returned by the first
    page request.
    ### Returns:
    - Channel video list, including video ID, title, thumbnail, view count, like count, comment count,
    video duration and other information.

    # [示例/Example]
    channel_id = \"UCXuqSBlHAE6Xw-yeJA0Tunw\"
    lang = \"en-US\"
    sortBy = \"newest\"
    contentType = \"videos\"
    nextToken = None

    Args:
        channel_id (str): 频道ID/Channel ID
        lang (Union[Unset, str]): 视频结果语言代码/Video result language code Default: 'en-US'.
        sort_by (Union[Unset, str]): 排序方式/Sort by Default: 'newest'.
        content_type (Union[Unset, str]): 内容类型/Content type Default: 'videos'.
        next_token (Union[Unset, str]): 翻页令牌/Pagination token Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        lang=lang,
        sort_by=sort_by,
        content_type=content_type,
        next_token=next_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    channel_id: str,
    lang: Union[Unset, str] = "en-US",
    sort_by: Union[Unset, str] = "newest",
    content_type: Union[Unset, str] = "videos",
    next_token: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取频道视频 V2/Get channel videos V2

     # [中文]

    ### 用途:
    - 获取频道视频 V2，支持获取频道视频列表，频道短视频列表，频道直播列表。

    ### 参数:
    - channel_id: 频道ID或频道名称，如果是频道名称，则需要在前面加上 `@` 符号，例如：@LinusTechTips。
    - lang: 视频结果语言代码，默认为 `en-US`，任何语言代码均可，当提交不支持的语言代码时，默认使用 `en-US` 作为语言代码。
    - sortBy: 排序方式，默认为 `newest`，可选值为 `newest` 和 `oldest` 和 `mostPopular`：
        - newest: 按照最新排序，默认值。
        - oldest: 按照最旧排序。
        - mostPopular: 按照最热排序。
    - contentType: 内容类型，默认为 `videos`，可选值为 `videos` 和 `shorts` 和 `live`：
        - videos: 视频列表，默认值。
        - shorts: 短视频列表。
        - live: 直播列表。
    - nextToken: 用于继续获取视频的令牌。可选参数，默认值为空，从第一页开始获取。
        - 如果获取第一页，则nextToken参数为None。
        - 如果获取第二页，则nextToken参数为第一页请求返回的nextToken。

    ### 返回:
    - 频道视频列表，包含视频ID、标题、缩略图、观看次数、点赞次数、评论数、视频时长等信息。

    # [English]

    ### Purpose:
    - Get channel videos V2, support getting channel video list, channel short video list, channel live
    list.

    ### Parameters:
    - channel_id: Channel ID or channel name, if it is a channel name, add `@` symbol in front of it,
    for example: @LinusTechTips.
    - lang: Video result language code, default is `en-US`, any language code is supported, when
    submitting unsupported language code, default use `en-US` as language code.
    - sortBy: Sort by, default is `newest`, optional values are `newest` and `oldest` and `mostPopular`:
        - newest: Sort by newest, default value.
        - oldest: Sort by oldest.
        - mostPopular: Sort by most popular.
    - contentType: Content type, default is `videos`, optional values are `videos`
        - videos: Video list, default value.
        - shorts: Short video list.
        - live: Live list.
    - nextToken: Token to continue fetching videos. Optional parameter, default value is empty, start
    from the first page.
        - If fetching the first page, the nextToken parameter is None.
        - If fetching the second page, the nextToken parameter is the nextToken returned by the first
    page request.
    ### Returns:
    - Channel video list, including video ID, title, thumbnail, view count, like count, comment count,
    video duration and other information.

    # [示例/Example]
    channel_id = \"UCXuqSBlHAE6Xw-yeJA0Tunw\"
    lang = \"en-US\"
    sortBy = \"newest\"
    contentType = \"videos\"
    nextToken = None

    Args:
        channel_id (str): 频道ID/Channel ID
        lang (Union[Unset, str]): 视频结果语言代码/Video result language code Default: 'en-US'.
        sort_by (Union[Unset, str]): 排序方式/Sort by Default: 'newest'.
        content_type (Union[Unset, str]): 内容类型/Content type Default: 'videos'.
        next_token (Union[Unset, str]): 翻页令牌/Pagination token Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            channel_id=channel_id,
            lang=lang,
            sort_by=sort_by,
            content_type=content_type,
            next_token=next_token,
        )
    ).parsed
