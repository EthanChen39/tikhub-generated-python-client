from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_product_related_videos_request import GetProductRelatedVideosRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: GetProductRelatedVideosRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tiktok/creator/get_product_related_videos",
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
    body: GetProductRelatedVideosRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取同款商品关联视频/Get Product Related Videos

     # [中文]
    ### 用途:
    - 获取与指定商品关联的所有视频列表和对应的互动数据（如点赞数、评论数、分享数）。
    - 可用于分析同款商品在不同创作者视频中的推广效果和差异。
    - 支持按时间筛选，默认查询指定 start_date 所在自然月内的数据。

    ### 备注:
    - 必须同时提供 item_id（当前视频 ID）和 product_id（商品 ID）。
    - 返回数据按时间范围查询，同一商品下的其他视频列表。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
    - item_id: 当前视频 ID，例如 \"7496499484705246507\"
    - product_id: 商品 ID，例如 \"1731050202505515549\"
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回内容说明:
    - `segments`（数据分段列表）:
      - `time_selector`: 时间筛选参数（period, granularity, start_timestamp, end_timestamp）
      - `filter`: 查询条件（creator_id, product_id, item_id）
      - `timed_lists`: 视频列表
        - `start_timestamp`: 开始时间戳
        - `end_timestamp`: 结束时间戳
        - `stats`:
          - `video_product_id`: 商品 ID
          - `video`:
            - `item_id`: 视频 ID
            - `video_id`: 视频内部唯一 ID
            - `name`: 视频文案标题
            - `publish_time`: 发布时间戳
            - `duration`: 视频时长（秒）
            - `video_play_info`:
              - `post_url`: 视频封面图片链接
              - `video_infos.main_url`: 视频播放地址
          - `video_like_cnt`: 视频点赞数
          - `video_comment_cnt`: 视频评论数
          - `video_share_cnt`: 视频分享数

    ### 示例请求体:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\",
      \"product_id\": \"1731050202505515549\"
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve the list of all videos associated with a specified product along with their interaction
    metrics (such as like count, comment count, share count).
    - Useful for analyzing the promotional effectiveness and differences of the same product across
    different creators' videos.
    - Supports time-based filtering, defaulting to the calendar month of the specified start_date.

    ### Notes:
    - Requires both item_id (current video ID) and product_id (product ID).
    - Returns a list of other videos where the same product is featured.

    ### Return Description:
    - `segments`:
      - `time_selector`: Time filtering parameters (period, granularity, start_timestamp, end_timestamp)
      - `filter`: Query conditions (creator_id, product_id, item_id)
      - `timed_lists`: List of related videos
        - `start_timestamp`: Start timestamp
        - `end_timestamp`: End timestamp
        - `stats`:
          - `video_product_id`: Product ID
          - `video`:
            - `item_id`: Video ID
            - `video_id`: Video internal ID
            - `name`: Video caption/title
            - `publish_time`: Publish timestamp
            - `duration`: Video duration (seconds)
            - `video_play_info`:
              - `post_url`: Video cover image link
              - `video_infos.main_url`: Main video URL
          - `video_like_cnt`: Like count
          - `video_comment_cnt`: Comment count
          - `video_share_cnt`: Share count

    ### Example Request Body:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\",
      \"product_id\": \"1731050202505515549\"
    }
    ```

    Args:
        body (GetProductRelatedVideosRequest):

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
    body: GetProductRelatedVideosRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取同款商品关联视频/Get Product Related Videos

     # [中文]
    ### 用途:
    - 获取与指定商品关联的所有视频列表和对应的互动数据（如点赞数、评论数、分享数）。
    - 可用于分析同款商品在不同创作者视频中的推广效果和差异。
    - 支持按时间筛选，默认查询指定 start_date 所在自然月内的数据。

    ### 备注:
    - 必须同时提供 item_id（当前视频 ID）和 product_id（商品 ID）。
    - 返回数据按时间范围查询，同一商品下的其他视频列表。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
    - item_id: 当前视频 ID，例如 \"7496499484705246507\"
    - product_id: 商品 ID，例如 \"1731050202505515549\"
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回内容说明:
    - `segments`（数据分段列表）:
      - `time_selector`: 时间筛选参数（period, granularity, start_timestamp, end_timestamp）
      - `filter`: 查询条件（creator_id, product_id, item_id）
      - `timed_lists`: 视频列表
        - `start_timestamp`: 开始时间戳
        - `end_timestamp`: 结束时间戳
        - `stats`:
          - `video_product_id`: 商品 ID
          - `video`:
            - `item_id`: 视频 ID
            - `video_id`: 视频内部唯一 ID
            - `name`: 视频文案标题
            - `publish_time`: 发布时间戳
            - `duration`: 视频时长（秒）
            - `video_play_info`:
              - `post_url`: 视频封面图片链接
              - `video_infos.main_url`: 视频播放地址
          - `video_like_cnt`: 视频点赞数
          - `video_comment_cnt`: 视频评论数
          - `video_share_cnt`: 视频分享数

    ### 示例请求体:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\",
      \"product_id\": \"1731050202505515549\"
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve the list of all videos associated with a specified product along with their interaction
    metrics (such as like count, comment count, share count).
    - Useful for analyzing the promotional effectiveness and differences of the same product across
    different creators' videos.
    - Supports time-based filtering, defaulting to the calendar month of the specified start_date.

    ### Notes:
    - Requires both item_id (current video ID) and product_id (product ID).
    - Returns a list of other videos where the same product is featured.

    ### Return Description:
    - `segments`:
      - `time_selector`: Time filtering parameters (period, granularity, start_timestamp, end_timestamp)
      - `filter`: Query conditions (creator_id, product_id, item_id)
      - `timed_lists`: List of related videos
        - `start_timestamp`: Start timestamp
        - `end_timestamp`: End timestamp
        - `stats`:
          - `video_product_id`: Product ID
          - `video`:
            - `item_id`: Video ID
            - `video_id`: Video internal ID
            - `name`: Video caption/title
            - `publish_time`: Publish timestamp
            - `duration`: Video duration (seconds)
            - `video_play_info`:
              - `post_url`: Video cover image link
              - `video_infos.main_url`: Main video URL
          - `video_like_cnt`: Like count
          - `video_comment_cnt`: Comment count
          - `video_share_cnt`: Share count

    ### Example Request Body:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\",
      \"product_id\": \"1731050202505515549\"
    }
    ```

    Args:
        body (GetProductRelatedVideosRequest):

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
    body: GetProductRelatedVideosRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取同款商品关联视频/Get Product Related Videos

     # [中文]
    ### 用途:
    - 获取与指定商品关联的所有视频列表和对应的互动数据（如点赞数、评论数、分享数）。
    - 可用于分析同款商品在不同创作者视频中的推广效果和差异。
    - 支持按时间筛选，默认查询指定 start_date 所在自然月内的数据。

    ### 备注:
    - 必须同时提供 item_id（当前视频 ID）和 product_id（商品 ID）。
    - 返回数据按时间范围查询，同一商品下的其他视频列表。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
    - item_id: 当前视频 ID，例如 \"7496499484705246507\"
    - product_id: 商品 ID，例如 \"1731050202505515549\"
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回内容说明:
    - `segments`（数据分段列表）:
      - `time_selector`: 时间筛选参数（period, granularity, start_timestamp, end_timestamp）
      - `filter`: 查询条件（creator_id, product_id, item_id）
      - `timed_lists`: 视频列表
        - `start_timestamp`: 开始时间戳
        - `end_timestamp`: 结束时间戳
        - `stats`:
          - `video_product_id`: 商品 ID
          - `video`:
            - `item_id`: 视频 ID
            - `video_id`: 视频内部唯一 ID
            - `name`: 视频文案标题
            - `publish_time`: 发布时间戳
            - `duration`: 视频时长（秒）
            - `video_play_info`:
              - `post_url`: 视频封面图片链接
              - `video_infos.main_url`: 视频播放地址
          - `video_like_cnt`: 视频点赞数
          - `video_comment_cnt`: 视频评论数
          - `video_share_cnt`: 视频分享数

    ### 示例请求体:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\",
      \"product_id\": \"1731050202505515549\"
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve the list of all videos associated with a specified product along with their interaction
    metrics (such as like count, comment count, share count).
    - Useful for analyzing the promotional effectiveness and differences of the same product across
    different creators' videos.
    - Supports time-based filtering, defaulting to the calendar month of the specified start_date.

    ### Notes:
    - Requires both item_id (current video ID) and product_id (product ID).
    - Returns a list of other videos where the same product is featured.

    ### Return Description:
    - `segments`:
      - `time_selector`: Time filtering parameters (period, granularity, start_timestamp, end_timestamp)
      - `filter`: Query conditions (creator_id, product_id, item_id)
      - `timed_lists`: List of related videos
        - `start_timestamp`: Start timestamp
        - `end_timestamp`: End timestamp
        - `stats`:
          - `video_product_id`: Product ID
          - `video`:
            - `item_id`: Video ID
            - `video_id`: Video internal ID
            - `name`: Video caption/title
            - `publish_time`: Publish timestamp
            - `duration`: Video duration (seconds)
            - `video_play_info`:
              - `post_url`: Video cover image link
              - `video_infos.main_url`: Main video URL
          - `video_like_cnt`: Like count
          - `video_comment_cnt`: Comment count
          - `video_share_cnt`: Share count

    ### Example Request Body:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\",
      \"product_id\": \"1731050202505515549\"
    }
    ```

    Args:
        body (GetProductRelatedVideosRequest):

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
    body: GetProductRelatedVideosRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取同款商品关联视频/Get Product Related Videos

     # [中文]
    ### 用途:
    - 获取与指定商品关联的所有视频列表和对应的互动数据（如点赞数、评论数、分享数）。
    - 可用于分析同款商品在不同创作者视频中的推广效果和差异。
    - 支持按时间筛选，默认查询指定 start_date 所在自然月内的数据。

    ### 备注:
    - 必须同时提供 item_id（当前视频 ID）和 product_id（商品 ID）。
    - 返回数据按时间范围查询，同一商品下的其他视频列表。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
    - item_id: 当前视频 ID，例如 \"7496499484705246507\"
    - product_id: 商品 ID，例如 \"1731050202505515549\"
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回内容说明:
    - `segments`（数据分段列表）:
      - `time_selector`: 时间筛选参数（period, granularity, start_timestamp, end_timestamp）
      - `filter`: 查询条件（creator_id, product_id, item_id）
      - `timed_lists`: 视频列表
        - `start_timestamp`: 开始时间戳
        - `end_timestamp`: 结束时间戳
        - `stats`:
          - `video_product_id`: 商品 ID
          - `video`:
            - `item_id`: 视频 ID
            - `video_id`: 视频内部唯一 ID
            - `name`: 视频文案标题
            - `publish_time`: 发布时间戳
            - `duration`: 视频时长（秒）
            - `video_play_info`:
              - `post_url`: 视频封面图片链接
              - `video_infos.main_url`: 视频播放地址
          - `video_like_cnt`: 视频点赞数
          - `video_comment_cnt`: 视频评论数
          - `video_share_cnt`: 视频分享数

    ### 示例请求体:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\",
      \"product_id\": \"1731050202505515549\"
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve the list of all videos associated with a specified product along with their interaction
    metrics (such as like count, comment count, share count).
    - Useful for analyzing the promotional effectiveness and differences of the same product across
    different creators' videos.
    - Supports time-based filtering, defaulting to the calendar month of the specified start_date.

    ### Notes:
    - Requires both item_id (current video ID) and product_id (product ID).
    - Returns a list of other videos where the same product is featured.

    ### Return Description:
    - `segments`:
      - `time_selector`: Time filtering parameters (period, granularity, start_timestamp, end_timestamp)
      - `filter`: Query conditions (creator_id, product_id, item_id)
      - `timed_lists`: List of related videos
        - `start_timestamp`: Start timestamp
        - `end_timestamp`: End timestamp
        - `stats`:
          - `video_product_id`: Product ID
          - `video`:
            - `item_id`: Video ID
            - `video_id`: Video internal ID
            - `name`: Video caption/title
            - `publish_time`: Publish timestamp
            - `duration`: Video duration (seconds)
            - `video_play_info`:
              - `post_url`: Video cover image link
              - `video_infos.main_url`: Main video URL
          - `video_like_cnt`: Like count
          - `video_comment_cnt`: Comment count
          - `video_share_cnt`: Share count

    ### Example Request Body:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\",
      \"product_id\": \"1731050202505515549\"
    }
    ```

    Args:
        body (GetProductRelatedVideosRequest):

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
