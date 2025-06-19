from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.response_model import ResponseModel
from ...types import UNSET, Response


def _get_kwargs(
    *,
    item_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["item_id"] = item_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/analytics/fetch_video_metrics",
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
    item_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取作品的统计数据/Get video metrics

     # [中文]
    ### 用途:
    - 获取TikTok视频的详细统计数据，包括观看量、点赞数、评论数和收藏数等核心指标
    - 提供总量统计以及从发布日期起14天的每日趋势数据，便于分析视频表现
    - 帮助创作者分析内容效果，评估用户互动情况，优化内容策略

    ### 参数:
    - item_id: 视频作品ID，必填参数，可从视频分享链接或TikTok Studio获取

    ### 返回内容说明:
    - `item_id`: 请求的视频ID
    - `video_views`: 视频总观看次数
      - `value`: 观看次数数值
    - `video_views_14_days`: 近14天的每日观看量趋势数据
      - `interval`: 数据间隔类型
      - `value`: 每日数据列表
    - `likes`: 视频总点赞数
      - `value`: 点赞数值
    - `likes_14_days`: 近14天的每日点赞数趋势数据
    - `comments`: 视频总评论数
      - `value`: 评论数值
    - `comments_14_days`: 近14天的每日评论数趋势数据
    - `favorites`: 视频总收藏数
      - `value`: 收藏数值
    - `favorites_14_days`: 近14天的每日收藏数趋势数据
    - `video_summary`: 视频表现的概览分析
      - `title`: 概览标题
      - `content`: 概览内容
      - `summary_type`: 概览类型

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/fetch_video_metrics\",
      \"params\": {
        \"item_id\": \"7502551047378832671\"
      },
      \"data\": {
        \"item_id\": \"7502551047378832671\",
        \"video_views\": {
          \"value\": 1555500
        },
        \"likes\": {
          \"value\": 11571
        },
        \"comments\": {
          \"value\": 6920
        },
        \"favorites\": {
          \"value\": 1243
        },
        \"video_summary\": {
          \"title\": \"Overview\",
          \"content\": \"This post received more comments per view than most other posts.\"
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve detailed analytics data for TikTok videos, including views, likes, comments, and
    favorites
    - Provide total statistics and daily trends for 14 days since the release date, facilitating video
    performance analysis
    - Help creators analyze content effectiveness, evaluate user engagement, and optimize content
    strategy

    ### Parameters:
    - item_id: Video ID, required parameter, can be obtained from video sharing links or TikTok Studio

    ### Return Description:
    - `item_id`: The requested video ID
    - `video_views`: Total number of video views
      - `value`: View count value
    - `video_views_14_days`: Daily view trends for the past 14 days
      - `interval`: Data interval type
      - `value`: List of daily data
    - `likes`: Total number of likes on the video
      - `value`: Like count value
    - `likes_14_days`: Daily like trends for the past 14 days
    - `comments`: Total number of comments on the video
      - `value`: Comment count value
    - `comments_14_days`: Daily comment trends for the past 14 days
    - `favorites`: Total number of times the video was favorited
      - `value`: Favorite count value
    - `favorites_14_days`: Daily favorite trends for the past 14 days
    - `video_summary`: Overview analysis of video performance
      - `title`: Overview title
      - `content`: Overview content
      - `summary_type`: Overview type

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/fetch_video_metrics\",
      \"params\": {
        \"item_id\": \"7502551047378832671\"
      },
      \"data\": {
        \"item_id\": \"7502551047378832671\",
        \"video_views\": {
          \"value\": 1555500
        },
        \"likes\": {
          \"value\": 11571
        },
        \"comments\": {
          \"value\": 6920
        },
        \"favorites\": {
          \"value\": 1243
        },
        \"video_summary\": {
          \"title\": \"Overview\",
          \"content\": \"This post received more comments per view than most other posts.\"
        }
      }
    }
    ```

    Args:
        item_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    item_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取作品的统计数据/Get video metrics

     # [中文]
    ### 用途:
    - 获取TikTok视频的详细统计数据，包括观看量、点赞数、评论数和收藏数等核心指标
    - 提供总量统计以及从发布日期起14天的每日趋势数据，便于分析视频表现
    - 帮助创作者分析内容效果，评估用户互动情况，优化内容策略

    ### 参数:
    - item_id: 视频作品ID，必填参数，可从视频分享链接或TikTok Studio获取

    ### 返回内容说明:
    - `item_id`: 请求的视频ID
    - `video_views`: 视频总观看次数
      - `value`: 观看次数数值
    - `video_views_14_days`: 近14天的每日观看量趋势数据
      - `interval`: 数据间隔类型
      - `value`: 每日数据列表
    - `likes`: 视频总点赞数
      - `value`: 点赞数值
    - `likes_14_days`: 近14天的每日点赞数趋势数据
    - `comments`: 视频总评论数
      - `value`: 评论数值
    - `comments_14_days`: 近14天的每日评论数趋势数据
    - `favorites`: 视频总收藏数
      - `value`: 收藏数值
    - `favorites_14_days`: 近14天的每日收藏数趋势数据
    - `video_summary`: 视频表现的概览分析
      - `title`: 概览标题
      - `content`: 概览内容
      - `summary_type`: 概览类型

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/fetch_video_metrics\",
      \"params\": {
        \"item_id\": \"7502551047378832671\"
      },
      \"data\": {
        \"item_id\": \"7502551047378832671\",
        \"video_views\": {
          \"value\": 1555500
        },
        \"likes\": {
          \"value\": 11571
        },
        \"comments\": {
          \"value\": 6920
        },
        \"favorites\": {
          \"value\": 1243
        },
        \"video_summary\": {
          \"title\": \"Overview\",
          \"content\": \"This post received more comments per view than most other posts.\"
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve detailed analytics data for TikTok videos, including views, likes, comments, and
    favorites
    - Provide total statistics and daily trends for 14 days since the release date, facilitating video
    performance analysis
    - Help creators analyze content effectiveness, evaluate user engagement, and optimize content
    strategy

    ### Parameters:
    - item_id: Video ID, required parameter, can be obtained from video sharing links or TikTok Studio

    ### Return Description:
    - `item_id`: The requested video ID
    - `video_views`: Total number of video views
      - `value`: View count value
    - `video_views_14_days`: Daily view trends for the past 14 days
      - `interval`: Data interval type
      - `value`: List of daily data
    - `likes`: Total number of likes on the video
      - `value`: Like count value
    - `likes_14_days`: Daily like trends for the past 14 days
    - `comments`: Total number of comments on the video
      - `value`: Comment count value
    - `comments_14_days`: Daily comment trends for the past 14 days
    - `favorites`: Total number of times the video was favorited
      - `value`: Favorite count value
    - `favorites_14_days`: Daily favorite trends for the past 14 days
    - `video_summary`: Overview analysis of video performance
      - `title`: Overview title
      - `content`: Overview content
      - `summary_type`: Overview type

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/fetch_video_metrics\",
      \"params\": {
        \"item_id\": \"7502551047378832671\"
      },
      \"data\": {
        \"item_id\": \"7502551047378832671\",
        \"video_views\": {
          \"value\": 1555500
        },
        \"likes\": {
          \"value\": 11571
        },
        \"comments\": {
          \"value\": 6920
        },
        \"favorites\": {
          \"value\": 1243
        },
        \"video_summary\": {
          \"title\": \"Overview\",
          \"content\": \"This post received more comments per view than most other posts.\"
        }
      }
    }
    ```

    Args:
        item_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        item_id=item_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    item_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取作品的统计数据/Get video metrics

     # [中文]
    ### 用途:
    - 获取TikTok视频的详细统计数据，包括观看量、点赞数、评论数和收藏数等核心指标
    - 提供总量统计以及从发布日期起14天的每日趋势数据，便于分析视频表现
    - 帮助创作者分析内容效果，评估用户互动情况，优化内容策略

    ### 参数:
    - item_id: 视频作品ID，必填参数，可从视频分享链接或TikTok Studio获取

    ### 返回内容说明:
    - `item_id`: 请求的视频ID
    - `video_views`: 视频总观看次数
      - `value`: 观看次数数值
    - `video_views_14_days`: 近14天的每日观看量趋势数据
      - `interval`: 数据间隔类型
      - `value`: 每日数据列表
    - `likes`: 视频总点赞数
      - `value`: 点赞数值
    - `likes_14_days`: 近14天的每日点赞数趋势数据
    - `comments`: 视频总评论数
      - `value`: 评论数值
    - `comments_14_days`: 近14天的每日评论数趋势数据
    - `favorites`: 视频总收藏数
      - `value`: 收藏数值
    - `favorites_14_days`: 近14天的每日收藏数趋势数据
    - `video_summary`: 视频表现的概览分析
      - `title`: 概览标题
      - `content`: 概览内容
      - `summary_type`: 概览类型

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/fetch_video_metrics\",
      \"params\": {
        \"item_id\": \"7502551047378832671\"
      },
      \"data\": {
        \"item_id\": \"7502551047378832671\",
        \"video_views\": {
          \"value\": 1555500
        },
        \"likes\": {
          \"value\": 11571
        },
        \"comments\": {
          \"value\": 6920
        },
        \"favorites\": {
          \"value\": 1243
        },
        \"video_summary\": {
          \"title\": \"Overview\",
          \"content\": \"This post received more comments per view than most other posts.\"
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve detailed analytics data for TikTok videos, including views, likes, comments, and
    favorites
    - Provide total statistics and daily trends for 14 days since the release date, facilitating video
    performance analysis
    - Help creators analyze content effectiveness, evaluate user engagement, and optimize content
    strategy

    ### Parameters:
    - item_id: Video ID, required parameter, can be obtained from video sharing links or TikTok Studio

    ### Return Description:
    - `item_id`: The requested video ID
    - `video_views`: Total number of video views
      - `value`: View count value
    - `video_views_14_days`: Daily view trends for the past 14 days
      - `interval`: Data interval type
      - `value`: List of daily data
    - `likes`: Total number of likes on the video
      - `value`: Like count value
    - `likes_14_days`: Daily like trends for the past 14 days
    - `comments`: Total number of comments on the video
      - `value`: Comment count value
    - `comments_14_days`: Daily comment trends for the past 14 days
    - `favorites`: Total number of times the video was favorited
      - `value`: Favorite count value
    - `favorites_14_days`: Daily favorite trends for the past 14 days
    - `video_summary`: Overview analysis of video performance
      - `title`: Overview title
      - `content`: Overview content
      - `summary_type`: Overview type

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/fetch_video_metrics\",
      \"params\": {
        \"item_id\": \"7502551047378832671\"
      },
      \"data\": {
        \"item_id\": \"7502551047378832671\",
        \"video_views\": {
          \"value\": 1555500
        },
        \"likes\": {
          \"value\": 11571
        },
        \"comments\": {
          \"value\": 6920
        },
        \"favorites\": {
          \"value\": 1243
        },
        \"video_summary\": {
          \"title\": \"Overview\",
          \"content\": \"This post received more comments per view than most other posts.\"
        }
      }
    }
    ```

    Args:
        item_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    item_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取作品的统计数据/Get video metrics

     # [中文]
    ### 用途:
    - 获取TikTok视频的详细统计数据，包括观看量、点赞数、评论数和收藏数等核心指标
    - 提供总量统计以及从发布日期起14天的每日趋势数据，便于分析视频表现
    - 帮助创作者分析内容效果，评估用户互动情况，优化内容策略

    ### 参数:
    - item_id: 视频作品ID，必填参数，可从视频分享链接或TikTok Studio获取

    ### 返回内容说明:
    - `item_id`: 请求的视频ID
    - `video_views`: 视频总观看次数
      - `value`: 观看次数数值
    - `video_views_14_days`: 近14天的每日观看量趋势数据
      - `interval`: 数据间隔类型
      - `value`: 每日数据列表
    - `likes`: 视频总点赞数
      - `value`: 点赞数值
    - `likes_14_days`: 近14天的每日点赞数趋势数据
    - `comments`: 视频总评论数
      - `value`: 评论数值
    - `comments_14_days`: 近14天的每日评论数趋势数据
    - `favorites`: 视频总收藏数
      - `value`: 收藏数值
    - `favorites_14_days`: 近14天的每日收藏数趋势数据
    - `video_summary`: 视频表现的概览分析
      - `title`: 概览标题
      - `content`: 概览内容
      - `summary_type`: 概览类型

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/fetch_video_metrics\",
      \"params\": {
        \"item_id\": \"7502551047378832671\"
      },
      \"data\": {
        \"item_id\": \"7502551047378832671\",
        \"video_views\": {
          \"value\": 1555500
        },
        \"likes\": {
          \"value\": 11571
        },
        \"comments\": {
          \"value\": 6920
        },
        \"favorites\": {
          \"value\": 1243
        },
        \"video_summary\": {
          \"title\": \"Overview\",
          \"content\": \"This post received more comments per view than most other posts.\"
        }
      }
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve detailed analytics data for TikTok videos, including views, likes, comments, and
    favorites
    - Provide total statistics and daily trends for 14 days since the release date, facilitating video
    performance analysis
    - Help creators analyze content effectiveness, evaluate user engagement, and optimize content
    strategy

    ### Parameters:
    - item_id: Video ID, required parameter, can be obtained from video sharing links or TikTok Studio

    ### Return Description:
    - `item_id`: The requested video ID
    - `video_views`: Total number of video views
      - `value`: View count value
    - `video_views_14_days`: Daily view trends for the past 14 days
      - `interval`: Data interval type
      - `value`: List of daily data
    - `likes`: Total number of likes on the video
      - `value`: Like count value
    - `likes_14_days`: Daily like trends for the past 14 days
    - `comments`: Total number of comments on the video
      - `value`: Comment count value
    - `comments_14_days`: Daily comment trends for the past 14 days
    - `favorites`: Total number of times the video was favorited
      - `value`: Favorite count value
    - `favorites_14_days`: Daily favorite trends for the past 14 days
    - `video_summary`: Overview analysis of video performance
      - `title`: Overview title
      - `content`: Overview content
      - `summary_type`: Overview type

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/fetch_video_metrics\",
      \"params\": {
        \"item_id\": \"7502551047378832671\"
      },
      \"data\": {
        \"item_id\": \"7502551047378832671\",
        \"video_views\": {
          \"value\": 1555500
        },
        \"likes\": {
          \"value\": 11571
        },
        \"comments\": {
          \"value\": 6920
        },
        \"favorites\": {
          \"value\": 1243
        },
        \"video_summary\": {
          \"title\": \"Overview\",
          \"content\": \"This post received more comments per view than most other posts.\"
        }
      }
    }
    ```

    Args:
        item_id (str): 作品id/Video id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            item_id=item_id,
        )
    ).parsed
