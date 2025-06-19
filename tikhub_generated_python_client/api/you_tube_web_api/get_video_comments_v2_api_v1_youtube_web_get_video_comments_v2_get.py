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
    video_id: str,
    lang: Union[Unset, str] = "",
    sort_by: Union[Unset, str] = "top",
    next_token: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["video_id"] = video_id

    params["lang"] = lang

    params["sortBy"] = sort_by

    params["nextToken"] = next_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/youtube/web/get_video_comments_v2",
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
    video_id: str,
    lang: Union[Unset, str] = "",
    sort_by: Union[Unset, str] = "top",
    next_token: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频评论V2/Get video comments V2

     # [中文]
    ### 用途:
    - 获取单个视频的评论。
    ### 参数:
    - video_id: 视频ID，从URL中获取，例如：https://www.youtube.com/watch?v=LuIL5JATZsc，这里的id就是LuIL5JATZsc。
    - lang: 评论结果语言代码，默认为\"\"。
    - sortBy: 排序方式，默认为top。
        - top: 按照热度排序。
        - newest: 按照最新排序。
    - nextToken: 用于继续获取评论的令牌。默认为None。
    ### 返回:
    - 视频评论。
    ### 说明:
    - 并发限制，当前并发数为4/秒。

    # [English]
    ### Purpose:
    - Get comments of a single video.
    ### Parameters:
    - id: Video ID, get it from the URL, for example: https://www.youtube.com/watch?v=LuIL5JATZsc, the
    id is LuIL5JATZsc.
    - lang: Comment result language code, default is \"\".
    - sortBy: Sort by, default is top.
        - top: Sort by popularity.
        - newest: Sort by newest.
    - nextToken: Token to continue fetching comments. Default is None.
    ### Returns:
    - Video comments.
    ### Note:
    - Concurrency limit, the current concurrency is 4/sec.

    # [示例/Example]
    video_id = \"LuIL5JATZsc\"
    lang = \"en-US\"
    sortBy = \"top\"
    nextToken = None

    Args:
        video_id (str): 视频ID/Video ID
        lang (Union[Unset, str]): 评论结果语言代码/Comment result language code Default: ''.
        sort_by (Union[Unset, str]): 排序方式/Sort by Default: 'top'.
        next_token (Union[Unset, str]): 翻页令牌/Pagination token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        video_id=video_id,
        lang=lang,
        sort_by=sort_by,
        next_token=next_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    video_id: str,
    lang: Union[Unset, str] = "",
    sort_by: Union[Unset, str] = "top",
    next_token: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频评论V2/Get video comments V2

     # [中文]
    ### 用途:
    - 获取单个视频的评论。
    ### 参数:
    - video_id: 视频ID，从URL中获取，例如：https://www.youtube.com/watch?v=LuIL5JATZsc，这里的id就是LuIL5JATZsc。
    - lang: 评论结果语言代码，默认为\"\"。
    - sortBy: 排序方式，默认为top。
        - top: 按照热度排序。
        - newest: 按照最新排序。
    - nextToken: 用于继续获取评论的令牌。默认为None。
    ### 返回:
    - 视频评论。
    ### 说明:
    - 并发限制，当前并发数为4/秒。

    # [English]
    ### Purpose:
    - Get comments of a single video.
    ### Parameters:
    - id: Video ID, get it from the URL, for example: https://www.youtube.com/watch?v=LuIL5JATZsc, the
    id is LuIL5JATZsc.
    - lang: Comment result language code, default is \"\".
    - sortBy: Sort by, default is top.
        - top: Sort by popularity.
        - newest: Sort by newest.
    - nextToken: Token to continue fetching comments. Default is None.
    ### Returns:
    - Video comments.
    ### Note:
    - Concurrency limit, the current concurrency is 4/sec.

    # [示例/Example]
    video_id = \"LuIL5JATZsc\"
    lang = \"en-US\"
    sortBy = \"top\"
    nextToken = None

    Args:
        video_id (str): 视频ID/Video ID
        lang (Union[Unset, str]): 评论结果语言代码/Comment result language code Default: ''.
        sort_by (Union[Unset, str]): 排序方式/Sort by Default: 'top'.
        next_token (Union[Unset, str]): 翻页令牌/Pagination token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        video_id=video_id,
        lang=lang,
        sort_by=sort_by,
        next_token=next_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    video_id: str,
    lang: Union[Unset, str] = "",
    sort_by: Union[Unset, str] = "top",
    next_token: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频评论V2/Get video comments V2

     # [中文]
    ### 用途:
    - 获取单个视频的评论。
    ### 参数:
    - video_id: 视频ID，从URL中获取，例如：https://www.youtube.com/watch?v=LuIL5JATZsc，这里的id就是LuIL5JATZsc。
    - lang: 评论结果语言代码，默认为\"\"。
    - sortBy: 排序方式，默认为top。
        - top: 按照热度排序。
        - newest: 按照最新排序。
    - nextToken: 用于继续获取评论的令牌。默认为None。
    ### 返回:
    - 视频评论。
    ### 说明:
    - 并发限制，当前并发数为4/秒。

    # [English]
    ### Purpose:
    - Get comments of a single video.
    ### Parameters:
    - id: Video ID, get it from the URL, for example: https://www.youtube.com/watch?v=LuIL5JATZsc, the
    id is LuIL5JATZsc.
    - lang: Comment result language code, default is \"\".
    - sortBy: Sort by, default is top.
        - top: Sort by popularity.
        - newest: Sort by newest.
    - nextToken: Token to continue fetching comments. Default is None.
    ### Returns:
    - Video comments.
    ### Note:
    - Concurrency limit, the current concurrency is 4/sec.

    # [示例/Example]
    video_id = \"LuIL5JATZsc\"
    lang = \"en-US\"
    sortBy = \"top\"
    nextToken = None

    Args:
        video_id (str): 视频ID/Video ID
        lang (Union[Unset, str]): 评论结果语言代码/Comment result language code Default: ''.
        sort_by (Union[Unset, str]): 排序方式/Sort by Default: 'top'.
        next_token (Union[Unset, str]): 翻页令牌/Pagination token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        video_id=video_id,
        lang=lang,
        sort_by=sort_by,
        next_token=next_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    video_id: str,
    lang: Union[Unset, str] = "",
    sort_by: Union[Unset, str] = "top",
    next_token: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频评论V2/Get video comments V2

     # [中文]
    ### 用途:
    - 获取单个视频的评论。
    ### 参数:
    - video_id: 视频ID，从URL中获取，例如：https://www.youtube.com/watch?v=LuIL5JATZsc，这里的id就是LuIL5JATZsc。
    - lang: 评论结果语言代码，默认为\"\"。
    - sortBy: 排序方式，默认为top。
        - top: 按照热度排序。
        - newest: 按照最新排序。
    - nextToken: 用于继续获取评论的令牌。默认为None。
    ### 返回:
    - 视频评论。
    ### 说明:
    - 并发限制，当前并发数为4/秒。

    # [English]
    ### Purpose:
    - Get comments of a single video.
    ### Parameters:
    - id: Video ID, get it from the URL, for example: https://www.youtube.com/watch?v=LuIL5JATZsc, the
    id is LuIL5JATZsc.
    - lang: Comment result language code, default is \"\".
    - sortBy: Sort by, default is top.
        - top: Sort by popularity.
        - newest: Sort by newest.
    - nextToken: Token to continue fetching comments. Default is None.
    ### Returns:
    - Video comments.
    ### Note:
    - Concurrency limit, the current concurrency is 4/sec.

    # [示例/Example]
    video_id = \"LuIL5JATZsc\"
    lang = \"en-US\"
    sortBy = \"top\"
    nextToken = None

    Args:
        video_id (str): 视频ID/Video ID
        lang (Union[Unset, str]): 评论结果语言代码/Comment result language code Default: ''.
        sort_by (Union[Unset, str]): 排序方式/Sort by Default: 'top'.
        next_token (Union[Unset, str]): 翻页令牌/Pagination token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            video_id=video_id,
            lang=lang,
            sort_by=sort_by,
            next_token=next_token,
        )
    ).parsed
