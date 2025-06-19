from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_video_audience_stats_request import GetVideoAudienceStatsRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: GetVideoAudienceStatsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tiktok/creator/get_video_audience_stats",
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
    body: GetVideoAudienceStatsRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频受众分析数据/Get Video Audience Analysis Data

     # [中文]
    ### 用途:
    - 获取指定 TikTok 视频观众的用户画像统计数据，包括性别分布、年龄分布、地区分布等维度。
    - 可用于精准了解视频观众群体特征，指导内容创作、商品选择和营销策略优化。
    - 支持按时间段（日/周/月）分析变化趋势。

    ### 备注:
    - 此接口需要提供 item_id（视频 ID）。
    - 受众画像数据来源于观看和互动用户的统计特征。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
    - item_id: 视频 ID，例如 \"7496499484705246507\"
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回内容说明:
    - `segments`（数据分段列表）:
      - `time_selector`: 时间筛选参数（period, granularity, start_timestamp, end_timestamp）
      - `filter`: 查询条件（creator_id, item_id）
      - `timed_profile`: 分段画像统计数据
        - `start_timestamp`: 开始时间戳
        - `end_timestamp`: 结束时间戳
        - `stats`:
          - `follower_genders`: 性别分布
            - `key`: 性别（female/male）
            - `value`: 占比（字符串，0-1）
          - `follower_ages`: 年龄段分布
            - `key`: 年龄段（如 \"18-24\", \"25-34\", 等）
            - `value`: 占比（字符串，0-1）
          - `follower_regions`: 地区分布
            - `key`: 国家代码（如 \"US\"）
            - `value`: 占比（字符串，0-1）
          - `profile_type`: 画像类型，固定值 2（受众画像）

    ### 示例请求体:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\"
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve audience profile statistics for a specified TikTok video, including gender distribution,
    age distribution, and regional distribution.
    - Useful for accurately understanding the characteristics of the video audience to guide content
    creation, product selection, and marketing strategy optimization.
    - Supports trend analysis across different time intervals (daily/weekly/monthly).

    ### Notes:
    - Requires item_id (video ID).
    - Audience profile data is based on characteristics of users who viewed and interacted with the
    video.

    ### Return Description:
    - `segments`:
      - `time_selector`: Time filtering parameters (period, granularity, start_timestamp, end_timestamp)
      - `filter`: Query conditions (creator_id, item_id)
      - `timed_profile`: Audience profile statistics
        - `start_timestamp`: Start timestamp
        - `end_timestamp`: End timestamp
        - `stats`:
          - `follower_genders`: Gender distribution
            - `key`: Gender (\"female\" or \"male\")
            - `value`: Proportion (string, range 0-1)
          - `follower_ages`: Age group distribution
            - `key`: Age group (e.g., \"18-24\", \"25-34\")
            - `value`: Proportion (string, range 0-1)
          - `follower_regions`: Regional distribution
            - `key`: Country code (e.g., \"US\")
            - `value`: Proportion (string, range 0-1)
          - `profile_type`: Profile type, fixed value 2 (Audience Profile)

    ### Example Request Body:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\"
    }
    ```

    Args:
        body (GetVideoAudienceStatsRequest):

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
    body: GetVideoAudienceStatsRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频受众分析数据/Get Video Audience Analysis Data

     # [中文]
    ### 用途:
    - 获取指定 TikTok 视频观众的用户画像统计数据，包括性别分布、年龄分布、地区分布等维度。
    - 可用于精准了解视频观众群体特征，指导内容创作、商品选择和营销策略优化。
    - 支持按时间段（日/周/月）分析变化趋势。

    ### 备注:
    - 此接口需要提供 item_id（视频 ID）。
    - 受众画像数据来源于观看和互动用户的统计特征。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
    - item_id: 视频 ID，例如 \"7496499484705246507\"
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回内容说明:
    - `segments`（数据分段列表）:
      - `time_selector`: 时间筛选参数（period, granularity, start_timestamp, end_timestamp）
      - `filter`: 查询条件（creator_id, item_id）
      - `timed_profile`: 分段画像统计数据
        - `start_timestamp`: 开始时间戳
        - `end_timestamp`: 结束时间戳
        - `stats`:
          - `follower_genders`: 性别分布
            - `key`: 性别（female/male）
            - `value`: 占比（字符串，0-1）
          - `follower_ages`: 年龄段分布
            - `key`: 年龄段（如 \"18-24\", \"25-34\", 等）
            - `value`: 占比（字符串，0-1）
          - `follower_regions`: 地区分布
            - `key`: 国家代码（如 \"US\"）
            - `value`: 占比（字符串，0-1）
          - `profile_type`: 画像类型，固定值 2（受众画像）

    ### 示例请求体:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\"
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve audience profile statistics for a specified TikTok video, including gender distribution,
    age distribution, and regional distribution.
    - Useful for accurately understanding the characteristics of the video audience to guide content
    creation, product selection, and marketing strategy optimization.
    - Supports trend analysis across different time intervals (daily/weekly/monthly).

    ### Notes:
    - Requires item_id (video ID).
    - Audience profile data is based on characteristics of users who viewed and interacted with the
    video.

    ### Return Description:
    - `segments`:
      - `time_selector`: Time filtering parameters (period, granularity, start_timestamp, end_timestamp)
      - `filter`: Query conditions (creator_id, item_id)
      - `timed_profile`: Audience profile statistics
        - `start_timestamp`: Start timestamp
        - `end_timestamp`: End timestamp
        - `stats`:
          - `follower_genders`: Gender distribution
            - `key`: Gender (\"female\" or \"male\")
            - `value`: Proportion (string, range 0-1)
          - `follower_ages`: Age group distribution
            - `key`: Age group (e.g., \"18-24\", \"25-34\")
            - `value`: Proportion (string, range 0-1)
          - `follower_regions`: Regional distribution
            - `key`: Country code (e.g., \"US\")
            - `value`: Proportion (string, range 0-1)
          - `profile_type`: Profile type, fixed value 2 (Audience Profile)

    ### Example Request Body:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\"
    }
    ```

    Args:
        body (GetVideoAudienceStatsRequest):

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
    body: GetVideoAudienceStatsRequest,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频受众分析数据/Get Video Audience Analysis Data

     # [中文]
    ### 用途:
    - 获取指定 TikTok 视频观众的用户画像统计数据，包括性别分布、年龄分布、地区分布等维度。
    - 可用于精准了解视频观众群体特征，指导内容创作、商品选择和营销策略优化。
    - 支持按时间段（日/周/月）分析变化趋势。

    ### 备注:
    - 此接口需要提供 item_id（视频 ID）。
    - 受众画像数据来源于观看和互动用户的统计特征。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
    - item_id: 视频 ID，例如 \"7496499484705246507\"
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回内容说明:
    - `segments`（数据分段列表）:
      - `time_selector`: 时间筛选参数（period, granularity, start_timestamp, end_timestamp）
      - `filter`: 查询条件（creator_id, item_id）
      - `timed_profile`: 分段画像统计数据
        - `start_timestamp`: 开始时间戳
        - `end_timestamp`: 结束时间戳
        - `stats`:
          - `follower_genders`: 性别分布
            - `key`: 性别（female/male）
            - `value`: 占比（字符串，0-1）
          - `follower_ages`: 年龄段分布
            - `key`: 年龄段（如 \"18-24\", \"25-34\", 等）
            - `value`: 占比（字符串，0-1）
          - `follower_regions`: 地区分布
            - `key`: 国家代码（如 \"US\"）
            - `value`: 占比（字符串，0-1）
          - `profile_type`: 画像类型，固定值 2（受众画像）

    ### 示例请求体:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\"
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve audience profile statistics for a specified TikTok video, including gender distribution,
    age distribution, and regional distribution.
    - Useful for accurately understanding the characteristics of the video audience to guide content
    creation, product selection, and marketing strategy optimization.
    - Supports trend analysis across different time intervals (daily/weekly/monthly).

    ### Notes:
    - Requires item_id (video ID).
    - Audience profile data is based on characteristics of users who viewed and interacted with the
    video.

    ### Return Description:
    - `segments`:
      - `time_selector`: Time filtering parameters (period, granularity, start_timestamp, end_timestamp)
      - `filter`: Query conditions (creator_id, item_id)
      - `timed_profile`: Audience profile statistics
        - `start_timestamp`: Start timestamp
        - `end_timestamp`: End timestamp
        - `stats`:
          - `follower_genders`: Gender distribution
            - `key`: Gender (\"female\" or \"male\")
            - `value`: Proportion (string, range 0-1)
          - `follower_ages`: Age group distribution
            - `key`: Age group (e.g., \"18-24\", \"25-34\")
            - `value`: Proportion (string, range 0-1)
          - `follower_regions`: Regional distribution
            - `key`: Country code (e.g., \"US\")
            - `value`: Proportion (string, range 0-1)
          - `profile_type`: Profile type, fixed value 2 (Audience Profile)

    ### Example Request Body:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\"
    }
    ```

    Args:
        body (GetVideoAudienceStatsRequest):

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
    body: GetVideoAudienceStatsRequest,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取视频受众分析数据/Get Video Audience Analysis Data

     # [中文]
    ### 用途:
    - 获取指定 TikTok 视频观众的用户画像统计数据，包括性别分布、年龄分布、地区分布等维度。
    - 可用于精准了解视频观众群体特征，指导内容创作、商品选择和营销策略优化。
    - 支持按时间段（日/周/月）分析变化趋势。

    ### 备注:
    - 此接口需要提供 item_id（视频 ID）。
    - 受众画像数据来源于观看和互动用户的统计特征。

    ### 参数:
    - cookie: 用户 Cookie 字符串（用于身份认证）
    - start_date: 查询起始日期，格式为 'MM-DD-YYYY'，如 '04-01-2025'
    - item_id: 视频 ID，例如 \"7496499484705246507\"
    - proxy: 可选 HTTP 代理地址，如不使用可省略
        - 示例格式: `http://username:password@host:port`

    ### 返回内容说明:
    - `segments`（数据分段列表）:
      - `time_selector`: 时间筛选参数（period, granularity, start_timestamp, end_timestamp）
      - `filter`: 查询条件（creator_id, item_id）
      - `timed_profile`: 分段画像统计数据
        - `start_timestamp`: 开始时间戳
        - `end_timestamp`: 结束时间戳
        - `stats`:
          - `follower_genders`: 性别分布
            - `key`: 性别（female/male）
            - `value`: 占比（字符串，0-1）
          - `follower_ages`: 年龄段分布
            - `key`: 年龄段（如 \"18-24\", \"25-34\", 等）
            - `value`: 占比（字符串，0-1）
          - `follower_regions`: 地区分布
            - `key`: 国家代码（如 \"US\"）
            - `value`: 占比（字符串，0-1）
          - `profile_type`: 画像类型，固定值 2（受众画像）

    ### 示例请求体:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\"
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve audience profile statistics for a specified TikTok video, including gender distribution,
    age distribution, and regional distribution.
    - Useful for accurately understanding the characteristics of the video audience to guide content
    creation, product selection, and marketing strategy optimization.
    - Supports trend analysis across different time intervals (daily/weekly/monthly).

    ### Notes:
    - Requires item_id (video ID).
    - Audience profile data is based on characteristics of users who viewed and interacted with the
    video.

    ### Return Description:
    - `segments`:
      - `time_selector`: Time filtering parameters (period, granularity, start_timestamp, end_timestamp)
      - `filter`: Query conditions (creator_id, item_id)
      - `timed_profile`: Audience profile statistics
        - `start_timestamp`: Start timestamp
        - `end_timestamp`: End timestamp
        - `stats`:
          - `follower_genders`: Gender distribution
            - `key`: Gender (\"female\" or \"male\")
            - `value`: Proportion (string, range 0-1)
          - `follower_ages`: Age group distribution
            - `key`: Age group (e.g., \"18-24\", \"25-34\")
            - `value`: Proportion (string, range 0-1)
          - `follower_regions`: Regional distribution
            - `key`: Country code (e.g., \"US\")
            - `value`: Proportion (string, range 0-1)
          - `profile_type`: Profile type, fixed value 2 (Audience Profile)

    ### Example Request Body:
    ```json
    {
      \"cookie\": \"your_cookie\",
      \"start_date\": \"04-01-2025\",
      \"item_id\": \"7496499484705246507\"
    }
    ```

    Args:
        body (GetVideoAudienceStatsRequest):

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
