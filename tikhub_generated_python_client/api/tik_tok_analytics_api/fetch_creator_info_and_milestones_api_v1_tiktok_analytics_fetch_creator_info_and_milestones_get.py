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
    user_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["user_id"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tiktok/analytics/fetch_creator_info_and_milestones",
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
    user_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者信息和里程碑数据/Get creator info and milestones

     # [中文]
    ### 用途:
    - 获取TikTok创作者账号的基本信息和关键统计数据
    - 查看创作者账号的成长历程和达成的重要里程碑
    - 分析创作者账号发展轨迹，了解粉丝增长和内容影响力变化

    ### 参数:
    - user_id: 创作者用户ID，必填参数，可从用户主页URL或TikTok后台获取

    ### 返回内容说明:
    - `user_id`: 请求的创作者ID
    - `creator_info`: The creator's basic information
      - `nickname`: 创作者昵称
      - `sec_user_id`: 安全用户ID
      - `unique_id`: 唯一用户名
      - `avatar_url`: 头像URL
      - `follower_count`: 粉丝数量
      - `like_count`: 获赞总数
    - `milestones`: 创作者账号里程碑列表，每个里程碑包含:
      - `milestone`: 里程碑类型ID
      - `milestone_title`: 里程碑标题（如\"达到100万粉丝\"）
      - `milestone_year`: 里程碑达成年份
      - `milestone_month_day`: 里程碑达成月日
      - `creator_summary`: 里程碑相关描述

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/fetch_creator_info_and_milestones\",
      \"params\": {
        \"user_id\": \"107955\"
      },
      \"data\": {
        \"user_id\": \"107955\",
        \"creator_info\": {
          \"avatar_url\": \"https://p19-pu-sign-useast8.tiktokcdn-us.com/tos-
    useast5-avt-0068-tx/ba67b11de451691939223e9d978e613a~tplv-tiktokx-cropcenter:720:720.webp\",
          \"follower_count\": 89812099,
          \"like_count\": 382411162,
          \"nickname\": \"TikTok\",
          \"sec_user_id\": \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\",
          \"unique_id\": \"tiktok\"
        },
        \"milestones\": [
          {
            \"milestone\": 6,
            \"milestone_month_day\": \"10/4\",
            \"milestone_title\": \"Reached 1 million followers\",
            \"milestone_year\": \"2015\"
          },
          {
            \"milestone\": 1,
            \"milestone_month_day\": \"2/27\",
            \"milestone_title\": \"Started posting on TikTok\",
            \"milestone_year\": \"2015\"
          }
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve basic information and key metrics for TikTok creator accounts
    - View creator growth journey and important achieved milestones
    - Analyze creator account development trajectory, understand follower growth and content influence
    changes

    ### Parameters:
    - user_id: Creator user ID, required parameter, can be obtained from user profile URL or TikTok
    backend

    ### Return Description:
    - `user_id`: The requested creator ID
    - `creator_info`: The creator's basic information
      - `nickname`: Creator's display name
      - `sec_user_id`: Security user ID
      - `unique_id`: Unique username
      - `avatar_url`: Profile picture URL
      - `follower_count`: Number of followers
      - `like_count`: Total number of likes received
    - `milestones`: List of creator account milestones, each milestone includes:
      - `milestone`: Milestone type ID
      - `milestone_title`: Milestone title (e.g., \"Reached 1 million followers\")
      - `milestone_year`: Year when the milestone was achieved
      - `milestone_month_day`: Month and day when the milestone was achieved
      - `creator_summary`: Milestone-related description

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/fetch_creator_info_and_milestones\",
      \"params\": {
        \"user_id\": \"107955\"
      },
      \"data\": {
        \"user_id\": \"107955\",
        \"creator_info\": {
          \"avatar_url\": \"https://p19-pu-sign-useast8.tiktokcdn-us.com/tos-
    useast5-avt-0068-tx/ba67b11de451691939223e9d978e613a~tplv-tiktokx-cropcenter:720:720.webp\",
          \"follower_count\": 89812099,
          \"like_count\": 382411162,
          \"nickname\": \"TikTok\",
          \"sec_user_id\": \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\",
          \"unique_id\": \"tiktok\"
        },
        \"milestones\": [
          {
            \"milestone\": 6,
            \"milestone_month_day\": \"10/4\",
            \"milestone_title\": \"Reached 1 million followers\",
            \"milestone_year\": \"2015\"
          },
          {
            \"milestone\": 1,
            \"milestone_month_day\": \"2/27\",
            \"milestone_title\": \"Started posting on TikTok\",
            \"milestone_year\": \"2015\"
          }
        ]
      }
    }
    ```

    Args:
        user_id (str): 用户id/User id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者信息和里程碑数据/Get creator info and milestones

     # [中文]
    ### 用途:
    - 获取TikTok创作者账号的基本信息和关键统计数据
    - 查看创作者账号的成长历程和达成的重要里程碑
    - 分析创作者账号发展轨迹，了解粉丝增长和内容影响力变化

    ### 参数:
    - user_id: 创作者用户ID，必填参数，可从用户主页URL或TikTok后台获取

    ### 返回内容说明:
    - `user_id`: 请求的创作者ID
    - `creator_info`: The creator's basic information
      - `nickname`: 创作者昵称
      - `sec_user_id`: 安全用户ID
      - `unique_id`: 唯一用户名
      - `avatar_url`: 头像URL
      - `follower_count`: 粉丝数量
      - `like_count`: 获赞总数
    - `milestones`: 创作者账号里程碑列表，每个里程碑包含:
      - `milestone`: 里程碑类型ID
      - `milestone_title`: 里程碑标题（如\"达到100万粉丝\"）
      - `milestone_year`: 里程碑达成年份
      - `milestone_month_day`: 里程碑达成月日
      - `creator_summary`: 里程碑相关描述

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/fetch_creator_info_and_milestones\",
      \"params\": {
        \"user_id\": \"107955\"
      },
      \"data\": {
        \"user_id\": \"107955\",
        \"creator_info\": {
          \"avatar_url\": \"https://p19-pu-sign-useast8.tiktokcdn-us.com/tos-
    useast5-avt-0068-tx/ba67b11de451691939223e9d978e613a~tplv-tiktokx-cropcenter:720:720.webp\",
          \"follower_count\": 89812099,
          \"like_count\": 382411162,
          \"nickname\": \"TikTok\",
          \"sec_user_id\": \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\",
          \"unique_id\": \"tiktok\"
        },
        \"milestones\": [
          {
            \"milestone\": 6,
            \"milestone_month_day\": \"10/4\",
            \"milestone_title\": \"Reached 1 million followers\",
            \"milestone_year\": \"2015\"
          },
          {
            \"milestone\": 1,
            \"milestone_month_day\": \"2/27\",
            \"milestone_title\": \"Started posting on TikTok\",
            \"milestone_year\": \"2015\"
          }
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve basic information and key metrics for TikTok creator accounts
    - View creator growth journey and important achieved milestones
    - Analyze creator account development trajectory, understand follower growth and content influence
    changes

    ### Parameters:
    - user_id: Creator user ID, required parameter, can be obtained from user profile URL or TikTok
    backend

    ### Return Description:
    - `user_id`: The requested creator ID
    - `creator_info`: The creator's basic information
      - `nickname`: Creator's display name
      - `sec_user_id`: Security user ID
      - `unique_id`: Unique username
      - `avatar_url`: Profile picture URL
      - `follower_count`: Number of followers
      - `like_count`: Total number of likes received
    - `milestones`: List of creator account milestones, each milestone includes:
      - `milestone`: Milestone type ID
      - `milestone_title`: Milestone title (e.g., \"Reached 1 million followers\")
      - `milestone_year`: Year when the milestone was achieved
      - `milestone_month_day`: Month and day when the milestone was achieved
      - `creator_summary`: Milestone-related description

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/fetch_creator_info_and_milestones\",
      \"params\": {
        \"user_id\": \"107955\"
      },
      \"data\": {
        \"user_id\": \"107955\",
        \"creator_info\": {
          \"avatar_url\": \"https://p19-pu-sign-useast8.tiktokcdn-us.com/tos-
    useast5-avt-0068-tx/ba67b11de451691939223e9d978e613a~tplv-tiktokx-cropcenter:720:720.webp\",
          \"follower_count\": 89812099,
          \"like_count\": 382411162,
          \"nickname\": \"TikTok\",
          \"sec_user_id\": \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\",
          \"unique_id\": \"tiktok\"
        },
        \"milestones\": [
          {
            \"milestone\": 6,
            \"milestone_month_day\": \"10/4\",
            \"milestone_title\": \"Reached 1 million followers\",
            \"milestone_year\": \"2015\"
          },
          {
            \"milestone\": 1,
            \"milestone_month_day\": \"2/27\",
            \"milestone_title\": \"Started posting on TikTok\",
            \"milestone_year\": \"2015\"
          }
        ]
      }
    }
    ```

    Args:
        user_id (str): 用户id/User id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: str,
) -> Response[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者信息和里程碑数据/Get creator info and milestones

     # [中文]
    ### 用途:
    - 获取TikTok创作者账号的基本信息和关键统计数据
    - 查看创作者账号的成长历程和达成的重要里程碑
    - 分析创作者账号发展轨迹，了解粉丝增长和内容影响力变化

    ### 参数:
    - user_id: 创作者用户ID，必填参数，可从用户主页URL或TikTok后台获取

    ### 返回内容说明:
    - `user_id`: 请求的创作者ID
    - `creator_info`: The creator's basic information
      - `nickname`: 创作者昵称
      - `sec_user_id`: 安全用户ID
      - `unique_id`: 唯一用户名
      - `avatar_url`: 头像URL
      - `follower_count`: 粉丝数量
      - `like_count`: 获赞总数
    - `milestones`: 创作者账号里程碑列表，每个里程碑包含:
      - `milestone`: 里程碑类型ID
      - `milestone_title`: 里程碑标题（如\"达到100万粉丝\"）
      - `milestone_year`: 里程碑达成年份
      - `milestone_month_day`: 里程碑达成月日
      - `creator_summary`: 里程碑相关描述

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/fetch_creator_info_and_milestones\",
      \"params\": {
        \"user_id\": \"107955\"
      },
      \"data\": {
        \"user_id\": \"107955\",
        \"creator_info\": {
          \"avatar_url\": \"https://p19-pu-sign-useast8.tiktokcdn-us.com/tos-
    useast5-avt-0068-tx/ba67b11de451691939223e9d978e613a~tplv-tiktokx-cropcenter:720:720.webp\",
          \"follower_count\": 89812099,
          \"like_count\": 382411162,
          \"nickname\": \"TikTok\",
          \"sec_user_id\": \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\",
          \"unique_id\": \"tiktok\"
        },
        \"milestones\": [
          {
            \"milestone\": 6,
            \"milestone_month_day\": \"10/4\",
            \"milestone_title\": \"Reached 1 million followers\",
            \"milestone_year\": \"2015\"
          },
          {
            \"milestone\": 1,
            \"milestone_month_day\": \"2/27\",
            \"milestone_title\": \"Started posting on TikTok\",
            \"milestone_year\": \"2015\"
          }
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve basic information and key metrics for TikTok creator accounts
    - View creator growth journey and important achieved milestones
    - Analyze creator account development trajectory, understand follower growth and content influence
    changes

    ### Parameters:
    - user_id: Creator user ID, required parameter, can be obtained from user profile URL or TikTok
    backend

    ### Return Description:
    - `user_id`: The requested creator ID
    - `creator_info`: The creator's basic information
      - `nickname`: Creator's display name
      - `sec_user_id`: Security user ID
      - `unique_id`: Unique username
      - `avatar_url`: Profile picture URL
      - `follower_count`: Number of followers
      - `like_count`: Total number of likes received
    - `milestones`: List of creator account milestones, each milestone includes:
      - `milestone`: Milestone type ID
      - `milestone_title`: Milestone title (e.g., \"Reached 1 million followers\")
      - `milestone_year`: Year when the milestone was achieved
      - `milestone_month_day`: Month and day when the milestone was achieved
      - `creator_summary`: Milestone-related description

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/fetch_creator_info_and_milestones\",
      \"params\": {
        \"user_id\": \"107955\"
      },
      \"data\": {
        \"user_id\": \"107955\",
        \"creator_info\": {
          \"avatar_url\": \"https://p19-pu-sign-useast8.tiktokcdn-us.com/tos-
    useast5-avt-0068-tx/ba67b11de451691939223e9d978e613a~tplv-tiktokx-cropcenter:720:720.webp\",
          \"follower_count\": 89812099,
          \"like_count\": 382411162,
          \"nickname\": \"TikTok\",
          \"sec_user_id\": \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\",
          \"unique_id\": \"tiktok\"
        },
        \"milestones\": [
          {
            \"milestone\": 6,
            \"milestone_month_day\": \"10/4\",
            \"milestone_title\": \"Reached 1 million followers\",
            \"milestone_year\": \"2015\"
          },
          {
            \"milestone\": 1,
            \"milestone_month_day\": \"2/27\",
            \"milestone_title\": \"Started posting on TikTok\",
            \"milestone_year\": \"2015\"
          }
        ]
      }
    }
    ```

    Args:
        user_id (str): 用户id/User id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ResponseModel]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: str,
) -> Optional[Union[HTTPValidationError, ResponseModel]]:
    r"""获取创作者信息和里程碑数据/Get creator info and milestones

     # [中文]
    ### 用途:
    - 获取TikTok创作者账号的基本信息和关键统计数据
    - 查看创作者账号的成长历程和达成的重要里程碑
    - 分析创作者账号发展轨迹，了解粉丝增长和内容影响力变化

    ### 参数:
    - user_id: 创作者用户ID，必填参数，可从用户主页URL或TikTok后台获取

    ### 返回内容说明:
    - `user_id`: 请求的创作者ID
    - `creator_info`: The creator's basic information
      - `nickname`: 创作者昵称
      - `sec_user_id`: 安全用户ID
      - `unique_id`: 唯一用户名
      - `avatar_url`: 头像URL
      - `follower_count`: 粉丝数量
      - `like_count`: 获赞总数
    - `milestones`: 创作者账号里程碑列表，每个里程碑包含:
      - `milestone`: 里程碑类型ID
      - `milestone_title`: 里程碑标题（如\"达到100万粉丝\"）
      - `milestone_year`: 里程碑达成年份
      - `milestone_month_day`: 里程碑达成月日
      - `creator_summary`: 里程碑相关描述

    ### 示例响应:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/fetch_creator_info_and_milestones\",
      \"params\": {
        \"user_id\": \"107955\"
      },
      \"data\": {
        \"user_id\": \"107955\",
        \"creator_info\": {
          \"avatar_url\": \"https://p19-pu-sign-useast8.tiktokcdn-us.com/tos-
    useast5-avt-0068-tx/ba67b11de451691939223e9d978e613a~tplv-tiktokx-cropcenter:720:720.webp\",
          \"follower_count\": 89812099,
          \"like_count\": 382411162,
          \"nickname\": \"TikTok\",
          \"sec_user_id\": \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\",
          \"unique_id\": \"tiktok\"
        },
        \"milestones\": [
          {
            \"milestone\": 6,
            \"milestone_month_day\": \"10/4\",
            \"milestone_title\": \"Reached 1 million followers\",
            \"milestone_year\": \"2015\"
          },
          {
            \"milestone\": 1,
            \"milestone_month_day\": \"2/27\",
            \"milestone_title\": \"Started posting on TikTok\",
            \"milestone_year\": \"2015\"
          }
        ]
      }
    }
    ```

    # [English]
    ### Purpose:
    - Retrieve basic information and key metrics for TikTok creator accounts
    - View creator growth journey and important achieved milestones
    - Analyze creator account development trajectory, understand follower growth and content influence
    changes

    ### Parameters:
    - user_id: Creator user ID, required parameter, can be obtained from user profile URL or TikTok
    backend

    ### Return Description:
    - `user_id`: The requested creator ID
    - `creator_info`: The creator's basic information
      - `nickname`: Creator's display name
      - `sec_user_id`: Security user ID
      - `unique_id`: Unique username
      - `avatar_url`: Profile picture URL
      - `follower_count`: Number of followers
      - `like_count`: Total number of likes received
    - `milestones`: List of creator account milestones, each milestone includes:
      - `milestone`: Milestone type ID
      - `milestone_title`: Milestone title (e.g., \"Reached 1 million followers\")
      - `milestone_year`: Year when the milestone was achieved
      - `milestone_month_day`: Month and day when the milestone was achieved
      - `creator_summary`: Milestone-related description

    ### Example Response:
    ```json
    {
      \"code\": 200,
      \"router\": \"/api/v1/tiktok/analytics/fetch_creator_info_and_milestones\",
      \"params\": {
        \"user_id\": \"107955\"
      },
      \"data\": {
        \"user_id\": \"107955\",
        \"creator_info\": {
          \"avatar_url\": \"https://p19-pu-sign-useast8.tiktokcdn-us.com/tos-
    useast5-avt-0068-tx/ba67b11de451691939223e9d978e613a~tplv-tiktokx-cropcenter:720:720.webp\",
          \"follower_count\": 89812099,
          \"like_count\": 382411162,
          \"nickname\": \"TikTok\",
          \"sec_user_id\": \"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM\",
          \"unique_id\": \"tiktok\"
        },
        \"milestones\": [
          {
            \"milestone\": 6,
            \"milestone_month_day\": \"10/4\",
            \"milestone_title\": \"Reached 1 million followers\",
            \"milestone_year\": \"2015\"
          },
          {
            \"milestone\": 1,
            \"milestone_month_day\": \"2/27\",
            \"milestone_title\": \"Started posting on TikTok\",
            \"milestone_year\": \"2015\"
          }
        ]
      }
    }
    ```

    Args:
        user_id (str): 用户id/User id

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ResponseModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
        )
    ).parsed
